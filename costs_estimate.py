#!/usr/bin/env python3
"""
costs_estimate.py -- first-order cost model for the earth house-kit (architecture v0.2).
Run: python3 costs_estimate.py

v0.2 architecture (forced by the binder-not-bulk energy correction):
  - only 10-15% of the wall clay is calcined, in a small insulated BATCH KILN
    (not in the wall), then milled, mixed with raw soil + one-part activator,
    and compressed/rammed around rebar. The steel grid is plain rebar.
  - one 20 kW solar array + ~50 kWh LFP battery fires the kiln by day during
    the build, then runs the finished village as a mini-grid.
All prices are (low, high) USD ranges, 2026, [TO-VERIFY] with real quotes.
"""

# ---------- geometry & energy ----------
PANEL_KG = 1.22 * 2.44 * 0.152 * 1800        # one 4x8x0.5 ft wall panel of earth
PANELS = 17                                  # 20x20 ft house, 8 ft walls, ~15% openings
WALL_KG = PANEL_KG * PANELS
BINDER_FRAC = (0.10, 0.15)                   # calcined fraction [TO-MEASURE, Phase A]
KILN_KWH_PER_KG = (0.40, 0.80)               # small insulated electric batch kiln, sun-dried clay
MILL_KWH_PER_KG = (0.03, 0.05)               # grinding metakaolin to reactive fineness
ARRAY_KW = 20
KILN_KWH_PER_SUNNY_DAY = 60                  # usable midday energy for the kiln from a 20 kW array

def lo_hi(f):
    return f(0), f(1)

binder_kg = lo_hi(lambda i: WALL_KG * BINDER_FRAC[i])
fire_kwh = lo_hi(lambda i: binder_kg[i] * (KILN_KWH_PER_KG[i] + MILL_KWH_PER_KG[i]))
days_per_house = tuple(e / KILN_KWH_PER_SUNNY_DAY for e in fire_kwh)

# ---------- cost tables (low, high) ----------
PER_HOUSE = {
    "rebar (~250-350 kg)":                 (200, 400),
    "one-part activator (10-20% of binder)": (100, 500),
    "foundation materials":                (100, 400),
    "doors & windows":                     (200, 600),
    "in-house electrical (LEDs, outlets)": (150, 400),
    "water: gutters, tank, sink":          (200, 600),
    "mini-grid drop (cable, meter)":       (100, 300),
    "lift inserts + connection plates":    (100, 300),
    "paid local labor (80-150 person-days)": (400, 2000),
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
    "compaction (electric rammer)":    (500, 2500),
    "instruments & controls":          (300, 1000),
    "QA: molds + compression tester":  (1000, 5000),
    "tools & PPE":                     (500, 1500),
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
    print("=" * 66)
    print("EARTH HOUSE-KIT COST MODEL v0.2 (batch-kiln binder architecture)")
    print("=" * 66)
    print(f"\nwall earth per house: {WALL_KG:,.0f} kg ({PANELS} panels)")
    print(f"binder calcined per house: {binder_kg[0]:,.0f}-{binder_kg[1]:,.0f} kg")
    print(f"firing + milling energy per house: {fire_kwh[0]:,.0f}-{fire_kwh[1]:,.0f} kWh")
    print(f"sunny days of kiln time per house ({ARRAY_KW} kW array): {days_per_house[0]:.0f}-{days_per_house[1]:.0f}")
    print(f"10-house village firing campaign: {10*days_per_house[0]:.0f}-{10*days_per_house[1]:.0f} sunny days")
    print("  (add a 2nd kiln + ~10 kW of cheap panels to roughly halve it)")

    for name, d in [("PER HOUSE (ex roof)", PER_HOUSE), ("REUSABLE RIG", RIG),
                    ("POWER (village keeps it)", POWER), ("FIELD PROGRAM", FIELD)]:
        lo, hi = total(d)
        print(f"\n{name}: {money(lo)} - {money(hi)}")
        for k, (a, b) in d.items():
            print(f"    {k:42s} {money(a):>8} - {money(b)}")
    for k, (a, b) in ROOF.items():
        print(f"ROOF option: {k:34s} {money(a):>8} - {money(b)}")

    print("\n" + "-" * 66)
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
          f" ({pw[0]/lo*100:.0f}-{pw[1]/hi*100:.0f}% of the budget)")

    print("\n" + "-" * 66)
    print("BINDER vs CEMENT (the honest money check)")
    cement_kg = (WALL_KG * 0.06, WALL_KG * 0.08)
    bags = tuple(c / 50 for c in cement_kg)
    print(f"  cement-stabilized alternative: {cement_kg[0]:,.0f}-{cement_kg[1]:,.0f} kg cement "
          f"= {bags[0]:.0f}-{bags[1]:.0f} bags x $5-30 = {money(bags[0]*5)}-{money(bags[1]*30)} per house")
    print("  -> the calcined-clay binder saves hundreds, not thousands, per house.")
    print("     it wins where cement is scarce/unreliable or carbon matters; else use cement.")
    co2 = tuple(c * 0.7 / 1000 for c in cement_kg)
    print(f"  CO2 avoided vs cement: ~{co2[0]:.1f}-{co2[1]:.1f} t/house -> at $10-50/t credits = "
          f"{money(co2[0]*10)}-{money(co2[1]*50)} per house (a narrative, not a revenue line)")

    print("\n" + "-" * 66)
    print("PHASE A GATE (the cheap test everything hangs on)")
    phase_a = {"small 120V test kiln (new; used is cheaper)": (300, 1500),
               "commercial metakaolin, 25 kg (control binder)": (50, 150),
               "activator chemicals": (100, 300),
               "cube molds + small ball mill": (250, 750),
               "lab XRD/TGA mineralogy, 3 samples": (450, 1200),
               "compressive tests, ~40 cubes": (600, 1600),
               "PPE & tools": (150, 300)}
    for k, (a, b) in phase_a.items():
        print(f"    {k:46s} {money(a):>7} - {money(b)}")
    lo, hi = total(phase_a)
    print(f"  PHASE A TOTAL: {money(lo)} - {money(hi)}")
