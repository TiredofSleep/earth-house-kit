#!/usr/bin/env python3
"""
site_profile.py -- portable, data-driven site analysis.
  python3 site_profile.py                      # every site in sites/
  python3 site_profile.py sites/hot_springs_ar.json
A new region = a new JSON file in sites/. A new material = an entry in data/materials.json.
No code changes needed for either.
"""
import json, glob, sys, os
from common import WALL_KG

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "data", "materials.json"), encoding="utf-8") as fh:
    LIB = json.load(fh)
WALL = round(WALL_KG)                                         # geometry lives in common.py
P = [WALL * f for f in LIB["pozzolan_frac_of_wall"]]          # pozzolan kg per house (low, high)

def has(av, k):
    v = str(av.get(k, "no")).lower()
    return not (v.startswith("no") or v.startswith("unknown"))

def bulk(soil):
    r, out = LIB["soil_rules"], []
    if soil.get("organic"):
        return "reject", ["REJECT: organic/topsoil won't bind -- strip it and dig deeper"]
    c = soil["clay"]
    if soil.get("clay_type") == "expansive":
        out.append("expansive clay: not for walls -- blend in >=50% sand or use another pit")
    if c < r["sandy_below_clay_pct"]:
        cls = "sandy"; out.append("very sandy: compacts well, the binder does all the binding")
    elif c <= r["ideal_max_clay_pct"]:
        cls = "ideal"; out.append("good bulk soil")
    elif c <= r["clayey_max_clay_pct"]:
        cls = "clayey"; out.append("clayey: blend in sand to cut shrinkage")
    else:
        cls = "heavy"; out.append("heavy clay: blend ~1:1 or more with sand")
    if soil["silt"] > r["silty_above_pct"]:
        out.append("silty: erodes easily -- stabilize and detail for water")
    return cls, out

def pozzolans(soil, av):
    """returns [(key, description, conditional)] ranked; conditional = needs a lab result first"""
    opts = []
    if has(av, "volcanic_ash"): opts.append(("volcanic_ash", "local volcanic ash (no firing)", False))
    if has(av, "fly_ash"):      opts.append(("fly_ash", "fly ash (no firing)", False))
    if has(av, "rice_husk"):    opts.append(("rice_husk_ash", "rice husk ash (made by the kiln fuel)", False))
    if has(av, "bagasse"):      opts.append(("bagasse_ash", "bagasse ash (made by the kiln fuel)", False))
    kc = str(av.get("kaolinitic_clay", "")).lower()
    if soil.get("clay_type") == "kaolinitic":
        opts.append(("calcined_clay", "fired site clay", False))
    elif kc.startswith("hauled"):
        opts.append(("calcined_clay", "fired hauled kaolinitic clay", False))
    elif soil.get("clay_type") == "unknown" and soil["clay"] >= 15 and not soil.get("organic"):
        opts.append(("calcined_clay", "fired site clay", True))
    return sorted(opts, key=lambda o: LIB["pozzolans"][o[0]]["rank"])

UNFIRED = ("volcanic_ash", "fly_ash")
FIRED = ("calcined_clay", "rice_husk_ash", "bagasse_ash")

def recipes(site, cls, pz):
    s, av, pr = site["soil"], site["available"], site.get("priorities", [])
    lime = "hot-mixed quicklime" if has(av, "quicklime") else "hydrated lime"
    if s.get("clay_type") == "expansive":
        return ["walls: none from this soil as dug -- blend >=50% sand (then re-run as a new site file)"
                " or use another pit",
                "lime 5-10% for footings, floors and paths"]
    sure = [d for k, d, c in pz if not c]
    maybe = [d for k, d, c in pz if c]
    clay_sure = any(k == "calcined_clay" and not c for k, d, c in pz)
    out = []
    if s.get("sulfate_or_salt"):
        fired = [d for k, d, c in pz if k in FIRED and not c]
        return ([f"geopolymer: {fired[0]} + activator (test sulfate resistance first)"] if fired
                else ["no safe binder identified -- test before building"])
    if sure:
        out.append(f"Roman: {' + '.join(sure[:2])} + {lime}")
    if clay_sure:
        out.append("geopolymer: fired clay + activator")
    if maybe:
        extra = " + ".join(sure[:1] + maybe)
        out.append(f"IF XRD CONFIRMS KAOLINITE: Roman: {extra} + {lime}; or geopolymer: fired site clay + activator")
    if cls in ("clayey", "heavy") and (has(av, "quicklime") or has(av, "hydrated_lime")):
        out.append("lime alone, 5-10%")
    if cls in ("sandy", "ideal") and has(av, "cement"):
        out.append("cement 6-8%" + ("  (fallback: priority is cement-free)" if "cement_free" in pr else ""))
    if "cement_free" in pr:
        out.sort(key=lambda r: "cement" in r)
    return out or ["no binder identified -- add local materials to the site file"]

def kiln(pz, av):
    keys = {k: c for k, d, c in pz}
    out, F = [], LIB["kiln_fuels"]
    if any(k in keys and not keys[k] for k in UNFIRED):
        out.append("NO KILN NEEDED: a local pozzolan needs no firing (firing below is optional)")
    if not any(k in keys for k in FIRED):
        return out or ["no kiln needed"]
    e = LIB["pozzolans"]["calcined_clay"]["ideal_kwh_per_kg"]
    clay = "calcined_clay" in keys
    flag = " [only if XRD confirms]" if clay and keys["calcined_clay"] else ""
    fuel_found = False
    for fuel, ash in (("rice_husk", "rice_husk_ash"), ("bagasse", "bagasse_ash"), ("wood", None)):
        if not has(av, fuel):
            continue
        fuel_found, f = True, F[fuel]
        if clay:
            lo = P[0] * e / (f["kwh_per_kg"][1] * f["kiln_efficiency"][1] + f["ash_fraction"][1] * e)
            hi = P[1] * e / (f["kwh_per_kg"][0] * f["kiln_efficiency"][0] + f["ash_fraction"][0] * e)
            vol = (lo / f["bulk_density"][1], hi / f["bulk_density"][0])
            line = (f"{fuel.replace('_',' ')}-fired kiln co-firing clay at ~650-700 C{flag}: "
                    f"{lo:,.0f}-{hi:,.0f} kg fuel/house (~{vol[0]:.0f}-{vol[1]:.0f} m3)")
            if ash:
                line += f", also yields {lo*f['ash_fraction'][0]:.0f}-{hi*f['ash_fraction'][1]:.0f} kg {ash.replace('_',' ')}"
            out.append(line)
        if ash and ash in keys:
            lo, hi = P[0] / f["ash_fraction"][1], P[1] / f["ash_fraction"][0]
            out.append(f"{fuel.replace('_',' ')} ash as the WHOLE pozzolan: {lo/1000:.1f}-{hi/1000:.1f} t fuel/house; "
                       "surplus heat can fire clay for the next house or dry soil")
        if f.get("caution"):
            out.append(f"{fuel}: {f['caution']}")
    if clay:
        sp = F["solar_electric"]["kwh_per_kg_clay_incl_losses"]
        out.append(f"solar-electric kiln{' (fallback)' if fuel_found else ''}{flag}: "
                   f"{P[0]*sp[0]:,.0f}-{P[1]*sp[1]:,.0f} kWh/house, weather-limited")
    return out

def todo(site, pz):
    s, av, t = site["soil"], site["available"], []
    if "_note" in s or "UNTESTED" in site["name"]:
        t.append("jar test + shrinkage box to replace placeholder soil numbers")
    if s.get("clay_type") in (None, "unknown") and s["clay"] >= 15:
        t.append("XRD/TGA mineralogy: is the clay kaolinitic (binder) or expansive (reject)?")
    if s["clay"] > 20: t.append("swell test")
    for k, v in av.items():
        if "TO-VERIFY" in str(v): t.append(f"confirm supply/price: {k}")
    if any(k == "rice_husk_ash" for k, d, c in pz):
        t.append("test-burn husks at 600-700 C; check ash colour and lime-ash cube strength")
    if s.get("sulfate_or_salt"): t.append("soluble sulfate/salt lab test")
    return t

def hazards(recs, pz):
    h = set()
    B = LIB["binders"]
    for r in recs:
        if "quicklime" in r: h.add("quicklime: " + B["quicklime_hot_mix"]["hazard"])
        if "activator" in r: h.add("activator: " + B["geopolymer_activator"]["hazard"])
    if any(k in ("rice_husk_ash", "bagasse_ash") for k, d, c in pz):
        h.add("ash dust: respirator; never overburn (>~800 C makes crystalline silica)")
    if any(k == "calcined_clay" for k, d, c in pz):
        h.add("kiln ~700 C and milling dust: heat PPE, respirator")
    return sorted(h)

def validate(site, path):
    s = site["soil"]
    for k in ("sand_gravel", "silt", "clay"):
        if k not in s:
            raise SystemExit(f"{path}: soil.{k} missing")
    total = s["sand_gravel"] + s["silt"] + s["clay"]
    if abs(total - 100) > 2:
        raise SystemExit(f"{path}: sand_gravel + silt + clay = {total}%, should be ~100%")

def profile(path):
    with open(path, encoding="utf-8") as fh:
        site = json.load(fh)
    validate(site, path)
    cls, notes = bulk(site["soil"])
    print("\n" + "=" * 70 + f"\n{site['name']}\n" + "=" * 70)
    s = site["soil"]
    print(f"soil: sand/gravel {s['sand_gravel']}%  silt {s['silt']}%  clay {s['clay']}%  ({s.get('clay_type','?')})")
    for n in notes: print("  bulk: " + n)
    if cls == "reject":
        return
    pz = pozzolans(s, site["available"])
    print("  pozzolans: " + ("; ".join(d + (" [needs XRD]" if c else "") for k, d, c in pz) if pz else "none local"))
    recs = recipes(site, cls, pz)
    for i, r in enumerate(recs, 1): print(f"  binder {i}: {r}")
    for k in kiln(pz, site["available"]): print("  kiln: " + k)
    for h in hazards(recs, pz): print("  hazard: " + h)
    for t in todo(site, pz): print("  TO-MEASURE: " + t)

if __name__ == "__main__":
    paths = sys.argv[1:] or sorted(glob.glob(os.path.join(HERE, "sites", "*.json")))
    print(f"pozzolan per house: {P[0]:,.0f}-{P[1]:,.0f} kg (5-8% of {WALL:,} kg of wall)")
    for p in paths:
        profile(p)
