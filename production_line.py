#!/usr/bin/env python3
"""
production_line.py -- the factory as a daylight robotic line: labor per tonne, robotics capex, payback.
Run: python3 production_line.py

The flow (clay pit to truck), each stage manual -> semi-automated -> robotic (supervised):
  clay winning + prep -> extrusion + auto-cutting -> SETTING onto dryer/kiln cars (gantry robot)
  -> drying (kiln waste heat + sun) -> firing (husk kiln, runs through the night on its own heat)
  -> unloading + sorting (gantry) -> continuous GRINDING line -> KITTING by house order (gantry reads the
  design file, palletizes in assembly order) -> PANEL PRE-ASSEMBLY (gantry lays units in the bed jig,
  rods tensioned) -> truck.
Machines run on the plant's solar in DAYLIGHT; the kiln and dryer run 24 h on husk and waste heat, fed
from a buffer of green ware made by day. All hours and costs are first-order [TO-VERIFY] -- see
business/BUSINESS_CASE.md for sources as they come in.
"""
import sys

# labor hours per tonne fired: (manual, semi-automated, robotic) [UNSOURCED first-order]
STAGES = {
    "clay winning + prep (loader, screen, pug feed)": (1.0, 0.40, 0.25),
    "extrusion + cutting":                             (1.0, 0.30, 0.10),
    "setting onto dryer/kiln cars":                    (2.0, 0.80, 0.10),
    "kiln + dryer tending, husk feed":                 (1.0, 0.50, 0.30),
    "unloading + sorting":                             (1.5, 0.60, 0.10),
    "grinding bed faces":                              (1.5, 0.50, 0.15),
    "kitting + palletizing by house order":            (1.0, 0.40, 0.10),
    "panel pre-assembly in the factory (optional)":    (2.0, 0.80, 0.30),
    "QA, maintenance, yard":                           (0.8, 0.60, 0.50),
}
# robotics that takes a stage from semi to robotic: (low, high) capex USD [UNSOURCED -> quotes]
ROBOTICS = {
    "auto cutter on the extruder":                      (10e3, 40e3),
    "gantry setter (open-source cartesian, 15 kg)":     (40e3, 120e3),
    "gantry unloader / sorter":                         (40e3, 120e3),
    "continuous calibrating (grinding) line":           (50e3, 250e3),
    "conveyors ~100 m":                                 (30e3, 80e3),
    "husk auger feed + kiln controls":                  (10e3, 30e3),
    "kitting gantry reading the design file":           (40e3, 120e3),
    "panel assembly gantry + tensioning station":       (40e3, 120e3),
    "vision, safety, controls":                         (20e3, 60e3),
}
LABOR_RATE = (30, 36)            # $/h loaded (Arkansas durable goods $26.27/h + burden)
DAYLIGHT_H = 8                   # machine hours per production day on solar
DAYS = 300
KWH_PER_T = (60, 150)            # extruder, grinding, robots, conveyors, fans
PV_KWH_PER_KWP = 1400            # Arkansas, ~4.7 peak-sun hours [TO-VERIFY]
UNIT_KG = 7.0                    # average fired unit


def hours(level, preassembly=True):
    i = {"manual": 0, "semi": 1, "robotic": 2}[level]
    return sum(v[i] for k, v in STAGES.items() if preassembly or "pre-assembly" not in k)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 96)
    print("DAYLIGHT ROBOTIC LINE: labor per tonne fired, by stage")
    print("=" * 96)
    print(f"{'stage':50s} {'manual':>7} {'semi':>6} {'robotic':>8}")
    for k, (m, s, r) in STAGES.items():
        print(f"{k:50s} {m:7.2f} {s:6.2f} {r:8.2f}")
    for lvl in ("manual", "semi", "robotic"):
        print(f"{'TOTAL h/t (' + lvl + ')':50s} {hours(lvl):7.2f}" if lvl == "manual" else
              f"{'TOTAL h/t (' + lvl + ')':50s} {'':7s} {hours(lvl):6.2f}" if lvl == "semi" else
              f"{'TOTAL h/t (' + lvl + ')':50s} {'':7s} {'':6s} {hours(lvl):8.2f}")
    capex = [sum(v[i] for v in ROBOTICS.values()) for i in (0, 1)]
    print(f"\nrobotics to go semi -> robotic: ${capex[0]/1e3:,.0f}k-${capex[1]/1e3:,.0f}k")
    for name, (a, b) in ROBOTICS.items():
        print(f"    {name:48s} ${a/1e3:4.0f}k-${b/1e3:4.0f}k")

    print("\nPAYBACK of the robotics, by plant size (labor saved semi -> robotic):")
    for t in (1000, 3000, 6000, 20000):
        saved_h = (hours("semi") - hours("robotic")) * t
        saved = [saved_h * r for r in LABOR_RATE]
        pb = (capex[0] / saved[1], capex[1] / saved[0])
        staff_semi = hours("semi") * t / (DAYS * DAYLIGHT_H)
        staff_rob = hours("robotic") * t / (DAYS * DAYLIGHT_H)
        print(f"  {t:6,d} t/yr: saves {saved_h:7,.0f} h (${saved[0]/1e3:,.0f}k-${saved[1]/1e3:,.0f}k/yr)"
              f" -> payback {pb[0]:.1f}-{pb[1]:.1f} yr; crew on the day shift {staff_semi:4.1f} -> {staff_rob:4.1f} people")
    print("  -> automate in steps as volume grows: semi-automated at the pilot, robotic at production scale.")

    print("\nDAYLIGHT SIZING (machines on solar, kiln on husk around the clock):")
    for t in (1000, 6000):
        rate = t / (DAYS * DAYLIGHT_H)
        units_min = rate * 1000 / UNIT_KG / 60
        kwh = [t * k for k in KWH_PER_T]
        kwp = [k / PV_KWH_PER_KWP for k in kwh]
        print(f"  {t:5,d} t/yr: line rate {rate:.2f} t/h = {units_min:.1f} units/min (one gantry at ~10 s/pick"
              f" handles 6/min); electricity {kwh[0]/1e3:.0f}-{kwh[1]/1e3:.0f} MWh/yr -> {kwp[0]:.0f}-{kwp[1]:.0f} kWp of PV")
    print("  green ware made by day buffers the kiln overnight; a day's drying stock decouples the two.")

    print("\nFACTORY PRE-ASSEMBLY also cuts SITE labor: panels arrive clamped and tested; the site crew only")
    print("  sets panels, drives the fold keys, and builds the dome -- days instead of weeks (TO-MEASURE).")
