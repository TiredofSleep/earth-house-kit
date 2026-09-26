#!/usr/bin/env python3
"""
business_model.py -- what does a kit cost, delivered, from a clay + rice-husk factory?
Run: python3 business_model.py                  (every design in houses/, both plant stages)

The factory sits where clay and husk are already abundant; each order is a DESIGN FILE
(houses/*.json -> house_designer.py -> every part). The price of an order is:
    parts   = fired tonnes x variable cost/t  +  printed and ground parts  +  steel and hardware
    fixed   = the plant's fixed cost per year / tonnes sold per year, charged per fired tonne
    margin  on parts + fixed
    freight = truckloads x (miles x rate + loading), at least a minimum charge per truck
Costs are mostly FIXED (plant, kilns, staff, certification) and materials are nearly free, so the
price of a kit is set mainly by how full the factory runs. The model shows that directly.
Assumptions: data/business.json (DRAFT until sourced; see business/BUSINESS_CASE.md).
"""
import glob, json, os, re, sys
from math import ceil
import house_designer as hd

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "data", "business.json"), encoding="utf-8") as fh:
    B = json.load(fh)
with open(os.path.join(HERE, "data", "business_lean.json"), encoding="utf-8") as fh:
    LEAN = json.load(fh)
SCEN = {"lean": False}


def val(section, key):
    if SCEN["lean"] and key in LEAN.get(section, {}):
        return LEAN[section][key]
    return B[section][key]


def group(kind):
    for g in ("wall", "dome", "siding", "plinth"):
        if kind.startswith(g):
            return g
    return "drainage"


def annual_fixed(stage, i):
    s = B["plant_stages"][stage]
    capex = sum(v[i] for v in s["capex"].values()) * (LEAN["capex_factor"] if SCEN["lean"] else 1)
    r, n = B["capital"]["interest"], B["capital"]["life_yr"]
    crf = r * (1 + r) ** n / ((1 + r) ** n - 1)                  # capital recovery factor
    fixed = sum(v[i] for v in s["fixed_annual"].values()) * (LEAN["fixed_factor"] if SCEN["lean"] else 1)
    return capex, capex * crf + fixed


def variable_per_t(i, husk_t_per_t):
    v = lambda k: val("variable", k)[i]
    labor = v("production labor (h per t fired)") * v("labor rate ($/h, loaded)")
    energy = v("electricity (kWh per t fired)") * v("electricity ($/kWh)")
    base = (v("clay dig, haul, prep ($/t fired)") + labor + energy
            + v("kiln, die, printer wear + consumables ($/t fired)")
            + v("pallets, strapping, loading ($/t)")
            + husk_t_per_t * v("rice husk ($/t husk, delivered)"))
    return base / (1 - v("rejects (share of fired mass)"))


def kit(path):
    spec = hd.load(path)
    parts, info = hd.design(spec)
    s = hd.summarize(parts)
    printed = s["by_method"]["print"]
    ground = sum(c for k, c in parts.units.items() if k.startswith("wall") or k.startswith("dome.voussoir"))
    steel = {"rod_kg": 0.0, "channel_kg": 0.0, "panels": 0, "keys": 0, "splices": 0, "rail_m": 0.0, "batten_m": 0.0}
    for (kind, unit), count in parts.other.items():
        m = re.search(r"x ([\d.]+) m", unit)
        L = float(m.group(1)) if m else 0
        if kind.startswith("M16"):
            steel["rod_kg"] += count * L * 1.58
        elif kind.startswith("steel end channel"):
            steel["channel_kg"] += count * L * 8.0
        elif kind.startswith("panels:"):
            steel["panels"] += count
        elif "wedge pair" in kind:
            steel["keys"] += count
        elif kind.startswith("ring splice"):
            steel["splices"] += count
        elif kind.startswith("siding rail"):
            steel["rail_m"] += count * L
        elif kind.startswith("siding batten"):
            steel["batten_m"] += count
    by_group = {}
    for kind, count in parts.units.items():
        g = group(kind)
        by_group[g] = by_group.get(g, 0) + count * hd.KIT[kind]["clay_kg"] / 1000
    return dict(name=spec["name"], area_ft2=info["area_ft2"], fired_t=s["clay_kg"] / 1000, by_group=by_group,
                husk_t=(s["husks"][0] / 1000, s["husks"][1] / 1000), printed=printed, ground=ground,
                steel=steel, checks=info["checks"])


def fired_t(k):
    if not SCEN["lean"]:
        return k["fired_t"]
    return sum(t * LEAN["mass_factor"].get(g, 1.0) for g, t in k["by_group"].items())


def price(k, stage, i, tonnes_sold, miles, stainless=False):
    h = {key: val("hardware", key) for key in B["hardware"]}
    husk_ratio = k["husk_t"][i] / k["fired_t"]
    ft = fired_t(k)
    parts = ft * variable_per_t(i, husk_ratio)
    parts += k["printed"] * val("per_part", "printed part extra ($ each: machine + labor)")[i]
    parts += k["ground"] * val("per_part", "ground unit extra ($ each)")[i]
    st = k["steel"]
    rod_rate = h["rod stainless 316 ($/kg)"][i] if stainless else h["rod M16 8.8 galvanized ($/kg)"][i]
    parts += (st["rod_kg"] * rod_rate + st["channel_kg"] * h["steel channel C100 galvanized ($/kg)"][i]
              + st["panels"] * h["hardware per panel (disc springs, nuts, plates, dowels) ($)"][i]
              + st["keys"] * h["fold key + wedge pair, stainless ($ each)"][i]
              + st["splices"] * h["ring splice plate + bolts ($ each)"][i]
              + st["rail_m"] * h["siding rail ($/m)"][i] + st["batten_m"] * h["siding batten ($/m)"][i])
    _, fixed_yr = annual_fixed(stage, i)
    fixed = ft * fixed_yr / tonnes_sold
    ex_works = (parts + fixed) * (1 + B["margin"])
    f = B["freight"]
    trucks = ceil((ft + (st["rod_kg"] + st["channel_kg"]) / 1000) / f["payload_t"])
    freight = trucks * max(f["min_charge_per_truck"], miles * f["rate_per_mile"][i]) + trucks * f["loading_per_truck"]
    return dict(parts=parts, fixed=fixed, ex_works=ex_works, trucks=trucks, freight=freight,
                delivered=ex_works + freight, fired_t=ft)


def money(x):
    return f"${x:,.0f}"


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    kits = [kit(p) for p in sorted(glob.glob(os.path.join(HERE, "houses", "*.json")))]
    kits.sort(key=lambda k: k["fired_t"])
    print("=" * 110)
    print("KIT FACTORY: clay + rice husk on site, kits shipped by flatbed (DRAFT assumptions: data/business.json)")
    print("=" * 110)
    for stage in B["plant_stages"]:
        cap = B["plant_stages"][stage]["capacity_t_per_yr"]
        capex = [annual_fixed(stage, i)[0] for i in (0, 1)]
        fixed = [annual_fixed(stage, i)[1] for i in (0, 1)]
        print(f"\n{stage.upper()} plant: capacity {cap:,} t/yr fired; capex {money(capex[0])}-{money(capex[1])};"
              f" fixed cost incl. capital {money(fixed[0])}-{money(fixed[1])}/yr")
        for util in (0.3, 0.6, 0.9):
            t = cap * util
            print(f"  running {util*100:.0f}% full ({t:,.0f} t/yr): fixed cost {money(fixed[0]/t)}-{money(fixed[1]/t)} per fired tonne")
        print(f"  {'kit':44s} {'ft2':>5} {'tonnes':>6} {'trucks':>6}  {'ex-works at 30% / 90% full':>30}  {'$/ft2 at 90%':>13}")
        for k in kits:
            lo30, hi30 = (price(k, stage, i, cap * 0.3, 300)["ex_works"] for i in (0, 1))
            lo90, hi90 = (price(k, stage, i, cap * 0.9, 300)["ex_works"] for i in (0, 1))
            tr = price(k, stage, 0, cap * 0.9, 300)["trucks"]
            print(f"  {k['name'][:44]:44s} {k['area_ft2']:5.0f} {k['fired_t']:6.1f} {tr:6d}"
                  f"  {money(lo30):>8}-{money(hi30):<8} / {money(lo90):>7}-{money(hi90):<8}"
                  f" {lo90/k['area_ft2']:5.0f}-{hi90/k['area_ft2']:<5.0f}")
    k16 = next(k for k in kits if "Ring 16" in k["name"])
    print("\nFREIGHT for the Ring 16 kit (production plant, 90% full):")
    for miles in (100, 300, 600, 1000):
        lo, hi = (price(k16, "production", i, 5400, miles) for i in (0, 1))
        print(f"  {miles:5d} miles: {lo['trucks']} truck(s), freight {money(lo['freight'])}-{money(hi['freight'])},"
              f" delivered {money(lo['delivered'])}-{money(hi['delivered'])}")
    p = price(k16, "production", 0, 5400, 300)
    print(f"\nwhere the money goes (Ring 16, production plant 90% full, low case): parts {money(p['parts'])},"
          f" fixed {money(p['fixed'])}, margin {money((p['parts']+p['fixed'])*B['margin'])}, freight {money(p['freight'])}")
    MARKET = 65.0      # $/ft2 shell: SIP shells ~$58 typical, log $50-100, site-built structure share ~$65 (NAHB)
    print(f"\nBREAK-EVEN if kits sell at ${MARKET:.0f}/ft2 (shell-kit market), freight paid by the buyer:")
    for stage in B["plant_stages"]:
        cap = B["plant_stages"][stage]["capacity_t_per_yr"]
        for kname in ("Studio 12", "Ring 16"):
            kk = next(k for k in kits if kname in k["name"])
            price_kit = MARKET * kk["area_ft2"]
            out = []
            for i in (0, 1):
                parts = price(kk, stage, i, cap, 0)["parts"]
                contrib = price_kit - parts
                n = annual_fixed(stage, i)[1] / contrib if contrib > 0 else float("inf")
                out.append((n, n * kk["fired_t"] / cap * 100, parts))
            print(f"  {stage:10s} {kname:9s}: sells ${price_kit:,.0f}, parts ${out[0][2]:,.0f}-${out[1][2]:,.0f}"
                  f" -> break-even {out[0][0]:,.0f}-{out[1][0]:,.0f} kits/yr ({out[0][1]:.0f}-{out[1][1]:.0f}% of capacity)")
    print("\ncompare (shell or kit, $/ft2):")
    for name, (a, b) in B["compare_per_ft2"].items():
        print(f"  {name:36s} ${a}-{b}")
    print("\nNOTE: the kit is the SHELL (walls, dome, skin, siding, plinth, drainage). Not included: site work,")
    print("rubble trench stone, doors, windows, wiring, plumbing, finishes, assembly labor, permits.")

    print("\n" + "=" * 110)
    print("LEAN vs BASELINE (production plant, 90% full, 300 miles): same kits, less clay, less handling")
    print("=" * 110)
    print("lean = graded 6 in walls (-35%), ribbed dome (-40%, TO-DESIGN), gravel drip trench instead of fired")
    print("       drainage parts, extrusion-first labor 1.5-4 h/t, capital-light plant (capex x0.5, fixed x0.8)")
    print(f"  {'kit':44s} {'tonnes':>13} {'ex-works (low case)':>23} {'$/ft2':>11} {'lean delivered':>21}")
    for k in kits:
        rows = []
        for lean in (False, True):
            SCEN["lean"] = lean
            rows.append([price(k, "production", i, 5400, 300) for i in (0, 1)])
        SCEN["lean"] = False
        b, l = rows
        print(f"  {k['name'][:44]:44s} {b[0]['fired_t']:5.1f} -> {l[0]['fired_t']:5.1f}"
              f"  {money(b[0]['ex_works']):>9} -> {money(l[0]['ex_works']):>9}"
              f"  {b[0]['ex_works']/k['area_ft2']:4.0f} -> {l[0]['ex_works']/k['area_ft2']:3.0f}"
              f"  {money(l[0]['delivered'])}-{money(l[1]['delivered'])}")
    SCEN["lean"] = True
    k16 = next(k for k in kits if "Ring 16" in k["name"])
    for i, label in ((0, "low"), (1, "high")):
        p = price(k16, "production", i, 5400, 300)
        print(f"LEAN Ring 16, {label} case: parts {money(p['parts'])}, fixed {money(p['fixed'])},"
              f" margin {money((p['parts']+p['fixed'])*B['margin'])}, freight {money(p['freight'])}")
    SCEN["lean"] = False
