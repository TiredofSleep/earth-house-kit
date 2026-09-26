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


def annual_fixed(stage, i):
    s = B["plant_stages"][stage]
    capex = sum(v[i] for v in s["capex"].values())
    r, n = B["capital"]["interest"], B["capital"]["life_yr"]
    crf = r * (1 + r) ** n / ((1 + r) ** n - 1)                  # capital recovery factor
    return capex, capex * crf + sum(v[i] for v in s["fixed_annual"].values())


def variable_per_t(i, husk_t_per_t):
    v = B["variable"]
    labor = v["production labor (h per t fired)"][i] * v["labor rate ($/h, loaded)"][i]
    energy = v["electricity (kWh per t fired)"][i] * v["electricity ($/kWh)"][i]
    base = (v["clay dig, haul, prep ($/t fired)"][i] + labor + energy
            + v["kiln, die, printer wear + consumables ($/t fired)"][i]
            + v["pallets, strapping, loading ($/t)"][i]
            + husk_t_per_t * v["rice husk ($/t husk, delivered)"][i])
    return base / (1 - v["rejects (share of fired mass)"][i])


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
    return dict(name=spec["name"], area_ft2=info["area_ft2"], fired_t=s["clay_kg"] / 1000,
                husk_t=(s["husks"][0] / 1000, s["husks"][1] / 1000), printed=printed, ground=ground,
                steel=steel, checks=info["checks"])


def price(k, stage, i, tonnes_sold, miles, stainless=False):
    h = B["hardware"]
    husk_ratio = k["husk_t"][i] / k["fired_t"]
    parts = k["fired_t"] * variable_per_t(i, husk_ratio)
    parts += k["printed"] * B["per_part"]["printed part extra ($ each: machine + labor)"][i]
    parts += k["ground"] * B["per_part"]["ground unit extra ($ each)"][i]
    st = k["steel"]
    rod_rate = h["rod stainless 316 ($/kg)"][i] if stainless else h["rod M16 8.8 galvanized ($/kg)"][i]
    parts += (st["rod_kg"] * rod_rate + st["channel_kg"] * h["steel channel C100 galvanized ($/kg)"][i]
              + st["panels"] * h["hardware per panel (disc springs, nuts, plates, dowels) ($)"][i]
              + st["keys"] * h["fold key + wedge pair, stainless ($ each)"][i]
              + st["splices"] * h["ring splice plate + bolts ($ each)"][i]
              + st["rail_m"] * h["siding rail ($/m)"][i] + st["batten_m"] * h["siding batten ($/m)"][i])
    _, fixed_yr = annual_fixed(stage, i)
    fixed = k["fired_t"] * fixed_yr / tonnes_sold
    ex_works = (parts + fixed) * (1 + B["margin"])
    f = B["freight"]
    trucks = ceil((k["fired_t"] + (st["rod_kg"] + st["channel_kg"]) / 1000) / f["payload_t"])
    freight = trucks * max(f["min_charge_per_truck"], miles * f["rate_per_mile"][i]) + trucks * f["loading_per_truck"]
    return dict(parts=parts, fixed=fixed, ex_works=ex_works, trucks=trucks, freight=freight,
                delivered=ex_works + freight)


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
    print("\ncompare (shell or kit, $/ft2, DRAFT):")
    for name, (a, b) in B["compare_per_ft2"].items():
        print(f"  {name:36s} ${a}-{b}")
    print("\nNOTE: the kit is the SHELL (walls, dome, skin, siding, plinth, drainage). Not included: site work,")
    print("rubble trench stone, doors, windows, wiring, plumbing, finishes, assembly labor, permits.")
