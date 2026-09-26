#!/usr/bin/env python3
"""
system_sizing.py (v0.2) -- energy sizing for the earth house-kit.
Run: python3 system_sizing.py
Keeps the killed design on record, shows why the in-wall binder design was
superseded, and sizes the v0.2 batch-kiln build phase and the village run phase.
"""
C_WATER, L_VAP, C_CLAY = 4186, 2.26e6, 900
KWH = lambda j: j / 3.6e6
PANEL_KG = 1.22 * 2.44 * 0.152 * 1800
PANELS = 17

def in_wall_fire(fraction, moisture=0.15, loss=3.0):
    fired = PANEL_KG * fraction
    w = fired * moisture
    e = w * C_WATER * 85 + w * L_VAP + fired * C_CLAY * 600 + fired * 0.14 * L_VAP * 0.5
    return KWH(e) * loss

if __name__ == "__main__":
    print("=" * 62)
    print("EARTH HOUSE-KIT ENERGY SIZING v0.2")
    print("=" * 62)
    full = in_wall_fire(1.0) * PANELS
    print(f"\n(1) fire the WHOLE wall in place [KILLED]: {full:,.0f} kWh/house,"
          f" ~{full/15/30:.0f} months on 3 kW, ~{in_wall_fire(1.0)*1.2:.0f} kWh battery/panel")
    part = in_wall_fire(0.15) * PANELS
    print(f"(2) fire 15% binder IN the wall [SUPERSEDED]: {part:,.0f} kWh/house --"
          " pointless to heat a whole wall to fire 15% of it")
    for frac, spec in [(0.10, 0.43), (0.15, 0.85)]:
        e = PANEL_KG * PANELS * frac * spec
        print(f"(3) batch-kiln binder, {int(frac*100)}% @ {spec} kWh/kg incl. milling: {e:,.0f} kWh/house")
    print("    -> fire by day straight off a 20 kW array; the battery only smooths clouds.")
    print("       no 133-888 kWh battery, no in-wall injection, no in-wall shrinkage cracking.")

    load = 3.1          # kWh/day per finished house (thermal mass handles heating/cooling)
    array_day = 20 * 5 * 0.8
    batt_usable = 50 * 0.8
    print(f"\n(4) village RUN phase: {load} kWh/day/house; 20 kW array ~{array_day:.0f} kWh/sunny day")
    print(f"    energy supports ~{array_day/load:.0f} houses on sunny days;")
    print(f"    a 50 kWh battery ({batt_usable:.0f} kWh usable) gives 10 houses ~{batt_usable/(10*load):.1f} days"
          " of full-load autonomy -> size battery to the cloudiest week, not the average day.")
