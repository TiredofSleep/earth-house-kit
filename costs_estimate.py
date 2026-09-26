#!/usr/bin/env python3
"""
costs_estimate.py -- first-order cost model for the earth house-kit (v0.3: pit-cast tilt-up).
Run: python3 costs_estimate.py

Architecture: panels cast flat in pits dug from the site soil, around a rebar grid, then
tilted up. Binder: batch-kiln calcined clay + activator (geopolymer), calcined clay or husk ash
+ hot-mixed quicklime (Roman), or 6-8% cement. One ~20 kW array + ~50 kWh LFP battery runs the
build, then stays as the village mini-grid.
All prices are (low, high) USD ranges, 2026, [TO-VERIFY] with real quotes.
"""
from common import WALL_KG, PANELS_PER_HOUSE, PERSON_DAYS

# ---------- energy ----------
BINDER_FRAC = (0.10, 0.15)                   # calcined fraction [TO-MEASURE, Phase A]
KILN_KWH_PER_KG = (0.40, 0.80)               # small insulated electric batch kiln, sun-dried clay
MILL_KWH_PER_KG = (0.03, 0.05)               # grinding metakaolin to reactive fineness
ARRAY_KW = 20
KILN_KWH_PER_SUNNY_DAY = 60                  # usable midday energy for the kiln from a 20 kW array

binder_kg = tuple(WALL_KG * BINDER_FRAC[i] for i in (0, 1))
fire_kwh = tuple(binder_kg[i] * (KILN_KWH_PER_KG[i] + MILL_KWH_PER_KG[i]) for i in (0, 1))
days_per_house = tuple(e / KILN_KWH_PER_SUNNY_DAY for e in fire_kwh)

# ---------- binder bought per house ----------
CEMENT_FRAC, CEMENT_BAG_KG, CEMENT_BAG_USD = (0.06, 0.08), 50, (5, 30)
LIME_FRAC, LIME_USD_PER_T = (0.05, 0.07), (150, 400)      # quicklime, delivered [TO-VERIFY]
cement_kg = tuple(WALL_KG * f for f in CEMENT_FRAC)
cement_bags = tuple(c / CEMENT_BAG_KG for c in cement_kg)
cement_usd = (cement_bags[0] * CEMENT_BAG_USD[0], cement_bags[1] * CEMENT_BAG_USD[1])
lime_kg = tuple(WALL_KG * f for f in LIME_FRAC)
lime_usd = (lime_kg[0] / 1000 * LIME_USD_PER_T[0], lime_kg[1] / 1000 * LIME_USD_PER_T[1])
BINDER_USD = (min(cement_usd[0], lime_usd[0]), max(cement_usd[1], lime_usd[1]))

# ---------- labor ----------
LABOR_USD_PER_DAY = (5, 15)                  # paid local labor, per person-day [TO-VERIFY per region]
labor_usd = (PERSON_DAYS[0] * LABOR_USD_PER_DAY[0], PERSON_DAYS[1] * LABOR_USD_PER_DAY[1])

# ---------- cost tables (low, high) ----------
PER_HOUSE = {
    "rebar (~250-350 kg)":                   (200, 400),
    "binder: cement or quicklime":           tuple(round(x, -1) for x in BINDER_USD),
    "one-part activator (geopolymer only)":  (0, 500),
    "foundation / plinth materials":         (100, 400),
    "doors & windows":                       (200, 600),
    "in-house electrical (LEDs, outlets)":   (150, 400),
    "water: gutters, tank, sink":            (200, 600),
    "mini-grid drop (cable, meter)":         (100, 300),
    "lift inserts + connection plates":      (100, 300),
    f"paid local labor ({PERSON_DAYS[0]}-{PERSON_DAYS[1]} person-days)": tuple(round(x, -1) for x in labor_usd),
}
ROOF = {"steel roof + insulation": (900, 2000),
        "earth vault + membrane (arid sites)": (150, 500)}

RIG = {  # reusable across villages
    "batch kiln / calciner":           (2000, 7000),
    "mill (crusher + ball mill)":      (1500, 6000),
    "soil prep (sieves, crusher)":     (300, 1500),
    "mixer":                           (500, 2000),
    "tilt gear: A-frame/gantry, hoist, braces": (1500, 5000),
    "pit liners, spreader bar, chairs":  (300, 1000),
    "compaction (vibratory plate / rammer)": (500, 2500),
    "instruments & controls":          (300, 1000),
    "QA: molds + compression tester":  (1000, 5000),
    "tools & PPE":                     (500, 1500),
}
OPTIONS = {  # not in the baseline totals
    "print-and-tilt printer (printer/PRINTER_CONCEPT.md)": (3600, 10500),
    "grid cure supply (low-voltage, ~200 A DC per panel)": (300, 1500),
}
POWER = {  # stays as the village mini-grid
    "solar modules 20 kW ($0.10-0.30/W)": (2000, 6000),
    "off-grid inverters/chargers":        (2000, 7000),
    "LFP battery ~50 kWh ($120-300/kWh)": (6000, 15000),
    "racking, BOS, protection":           (2000, 5000),
    "village distribution":               (2000, 6000),
}
FIELD = {
    "local site lead, ~8 months":        (4800, 12000),
    "remote engineering + 2 site trips": (5000, 15000),
    "site clay lab tests (XRD/TGA)":     (500, 2500),
    "in-country engineering review":     (2000, 10000),
}
LOGISTICS = {
    "regional sourcing (ship 1 core container)": (5500, 12500),
    "ship everything (3 containers)":            (16500, 37500),
}
CONTINGENCY = 0.15

PHASE_A = {
    "small 120V test kiln (new; used is cheaper)":        (300, 1500),
    "commercial metakaolin, 25 kg (control binder)":      (50, 150),
    "activator chemicals + quicklime + cement":           (150, 400),
    "cube/beam molds + small ball mill":                  (300, 900),
    "lab XRD/TGA mineralogy, 3 samples":                  (450, 1200),
    "compressive tests, ~80 cubes (all binders + cores)": (1200, 3200),
    "beam-bending + pull-out rig (DIY frame, load cell)": (150, 500),
    "jar test, shrinkage box, swell test":                (20, 80),
    "erosion spray + wet-dry cycling rig":                (50, 200),
    "corrosion coupons (galv + plain bar)":               (50, 150),
    "electrokinetic bench box (Route B)":                 (100, 200),
    "till-in-place slab: tiller + plate rental":          (100, 300),
    "floating-shoe test bed: plate rental, lumber":       (150, 500),
    "rice husk test burn + printed-mix materials":        (30, 150),
    "PPE & tools":                                        (150, 300),
}


def total(d):
    return sum(v[0] for v in d.values()), sum(v[1] for v in d.values())


def village(n=10, roof="steel roof + insulation", logistics="regional sourcing (ship 1 core container)",
            include_rig=True):
    ph = total(PER_HOUSE)
    rf = ROOF[roof]
    parts = [((ph[0] + rf[0]) * n, (ph[1] + rf[1]) * n), total(POWER), total(FIELD), LOGISTICS[logistics]]
    if include_rig:
        parts.append(total(RIG))
    lo = sum(p[0] for p in parts) * (1 + CONTINGENCY)
    hi = sum(p[1] for p in parts) * (1 + CONTINGENCY)
    return lo, hi


def money(x):
    return f"${x:,.0f}"


if __name__ == "__main__":
    print("=" * 70)
    print("EARTH HOUSE-KIT COST MODEL v0.3 (pit-cast tilt-up, batch-kiln binder)")
    print("=" * 70)
    print(f"\nwall earth per house: {WALL_KG:,.0f} kg ({PANELS_PER_HOUSE} panels)")
    print(f"binder calcined per house: {binder_kg[0]:,.0f}-{binder_kg[1]:,.0f} kg")
    print(f"firing + milling energy per house: {fire_kwh[0]:,.0f}-{fire_kwh[1]:,.0f} kWh")
    print(f"sunny days of kiln time per house ({ARRAY_KW} kW array): {days_per_house[0]:.0f}-{days_per_house[1]:.0f}")
    print(f"10-house village firing campaign: {10*days_per_house[0]:.0f}-{10*days_per_house[1]:.0f} sunny days")
    print("  (add a 2nd kiln + ~10 kW of cheap panels to roughly halve it)")

    for name, d in [("PER HOUSE (ex roof)", PER_HOUSE), ("REUSABLE RIG", RIG),
                    ("POWER (village keeps it)", POWER), ("FIELD PROGRAM", FIELD),
                    ("OPTIONS (not in totals)", OPTIONS)]:
        lo, hi = total(d)
        print(f"\n{name}: {money(lo)} - {money(hi)}")
        for k, (a, b) in d.items():
            print(f"    {k:52s} {money(a):>8} - {money(b)}")
    for k, (a, b) in ROOF.items():
        print(f"ROOF option: {k:44s} {money(a):>8} - {money(b)}")

    print("\n" + "-" * 70)
    print("FIRST VILLAGE (10 houses, incl. rig, +15% contingency)")
    scen = [("steel roofs, regional sourcing", dict()),
            ("steel roofs, ship everything", dict(logistics="ship everything (3 containers)")),
            ("earth vaults, regional sourcing", dict(roof="earth vault + membrane (arid sites)"))]
    for label, kw in scen:
        lo, hi = village(**kw)
        print(f"  {label:34s} {money(lo):>9} - {money(hi):>9}   per house {money(lo/10)} - {money(hi/10)}")
    lo, hi = village(include_rig=False)
    print(f"  {'next village (rig reused)':34s} {money(lo):>9} - {money(hi):>9}   per house {money(lo/10)} - {money(hi/10)}")

    pw = total(POWER)
    lo, hi = village()
    print(f"\n  of that, the solar mini-grid the village KEEPS: {money(pw[0])} - {money(pw[1])}"
          f" ({pw[1]/hi*100:.0f}-{pw[0]/lo*100:.0f}% of the budget)")

    print("\n" + "-" * 70)
    print("BINDER vs CEMENT (the honest money check)")
    print(f"  cement-stabilized: {cement_kg[0]:,.0f}-{cement_kg[1]:,.0f} kg cement "
          f"= {cement_bags[0]:.0f}-{cement_bags[1]:.0f} bags x $5-30 = {money(cement_usd[0])}-{money(cement_usd[1])} per house")
    print(f"  Roman hot-mix: {lime_kg[0]:,.0f}-{lime_kg[1]:,.0f} kg quicklime x $150-400/t"
          f" = {money(lime_usd[0])}-{money(lime_usd[1])} per house")
    print("  -> the calcined-clay binder saves hundreds, not thousands, per house.")
    print("     it wins where cement is scarce/unreliable or carbon matters; else use cement.")
    co2 = tuple(c * 0.7 / 1000 for c in cement_kg)
    print(f"  CO2 avoided vs cement: ~{co2[0]:.1f}-{co2[1]:.1f} t/house -> at $10-50/t credits = "
          f"{money(co2[0]*10)}-{money(co2[1]*50)} per house (a narrative, not a revenue line)")

    print("\n" + "-" * 70)
    print("PHASE A GATE (the tests in MISSION.md section 8)")
    for k, (a, b) in PHASE_A.items():
        print(f"    {k:52s} {money(a):>7} - {money(b)}")
    lo, hi = total(PHASE_A)
    print(f"  PHASE A TOTAL: {money(lo)} - {money(hi)}")
    print("  (corrosion coupons are read at 6 and 12 months; the go/no-go gate doesn't wait for them)")
