#!/usr/bin/env python3
"""
shelter_check.py -- which SHAPE makes the best above-ground tornado shelter from fired-clay units?
Run: python3 shelter_check.py

Same floor (~77 ft^2, the Shed 8 footprint), same walls (8 in cellular units with SAND-filled cells
for mass and impact), four shapes:
  box      -- square, 8 ft walls, flat roof
  pyramid  -- square, 5 ft walls + 55 deg pyramid roof
  dome     -- 8-gon, 8 ft walls + dome cap to 51.8 deg (the house design)
  cone     -- ROUND, 5 ft walls + steep corbelled cone (trullo): horizontal courses stepping inward
Checks at a tornado design wind of 250 mph (ICC 500-style, internal pressure +/-0.55):
  peak local suction (corners/edges), net roof uplift vs the shelter's own weight -> tie-down needed,
  debris-missile energy normal to the surface (15 lb 2x4: 100 mph horizontal, 67 mph vertical),
  corbel overhang per course (can it be built dry, no formwork?), clay and sand mass.
All pressure coefficients are first-order placeholders [TO-VERIFY ASCE 7 / ICC 500]. A shelter is only
a shelter after a certified test: this script ranks shapes, it doesn't certify anything.
"""
import sys
from math import pi, sqrt, tan, sin, cos, radians, degrees

MPH = 0.44704
V = 250 * MPH
KZ = 0.85                                  # low building, exposure C [TO-VERIFY]
Q = 0.613 * V**2 * KZ                      # Pa
GCPI = 0.55                                # internal pressure coefficient, shelters [TO-VERIFY ICC 500]
FLOOR = 77 * 0.0929                        # m^2
UNIT_DEPTH, COURSE_H, UNIT_LEN = 0.200, 0.193, 0.295
SHELL_KG_M2 = 115 + 0.62 * UNIT_DEPTH * 1600   # clay 115 + sand in ~62% voids of an 8 in unit
MISSILE_KG = 15 * 0.4536
E_WALL = 0.5 * MISSILE_KG * (100 * MPH) ** 2   # J, horizontal on walls
E_ROOF = 0.5 * MISSILE_KG * (67 * MPH) ** 2    # J, vertical on roofs

# per shape: (average roof Cp, worst local Cp, roof slope deg, has corners?) [TO-VERIFY]
CP = {
    "box":     dict(roof_avg=-1.3, local=-2.8, slope=0,    corners=True),
    "pyramid": dict(roof_avg=-0.45, local=-1.5, slope=55,  corners=True),
    "dome":    dict(roof_avg=-0.70, local=-1.2, slope=None, corners=False),
    "cone":    dict(roof_avg=-0.45, local=-1.2, slope=65,  corners=False),
}


def geometry():
    g = {}
    s = sqrt(FLOOR)                                        # square side
    g["box"] = dict(wall_h=2.44, wall_area=4 * s * 2.44, roof_area=FLOOR, roof_plan=FLOOR,
                    headroom=2.44)
    wall_h = 1.52
    rise = (s / 2) * tan(radians(55))
    slant = (s / 2) / cos(radians(55))
    g["pyramid"] = dict(wall_h=wall_h, wall_area=4 * s * wall_h, roof_area=4 * 0.5 * s * slant,
                        roof_plan=FLOOR, headroom=wall_h + rise)
    r8 = sqrt(FLOOR / (2 * sqrt(2)))                      # 8-gon circumradius for this area
    a = r8
    R = a / sin(radians(51.8))
    rise_d = R * (1 - cos(radians(51.8)))
    g["dome"] = dict(wall_h=2.44, wall_area=8 * 2 * a * sin(pi / 8) * 2.44,
                     roof_area=2 * pi * R * rise_d, roof_plan=pi * a * a, headroom=2.44 + rise_d)
    rc = sqrt(FLOOR / pi)
    rise_c = rc * tan(radians(65))
    slant_c = rc / cos(radians(65))
    g["cone"] = dict(wall_h=wall_h, wall_area=2 * pi * rc * wall_h, roof_area=pi * rc * slant_c,
                     roof_plan=pi * rc * rc, headroom=wall_h + rise_c)
    return g


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    g = geometry()
    print("=" * 108)
    print(f"ABOVE-GROUND TORNADO SHELTER, ~77 ft^2 floor, 250 mph (q = {Q/1e3:.2f} kPa), GCpi +/-{GCPI},"
          f" sand-filled 8 in units ({SHELL_KG_M2:.0f} kg/m2)")
    print("=" * 108)
    print(f"{'shape':8s} {'peak suction':>13} {'roof uplift':>12} {'roof weight':>12} {'tie-down':>10}"
          f" {'wall missile':>13} {'roof missile':>13} {'dry, no':>9} {'mass':>7} {'headroom':>9}")
    print(f"{'':8s} {'kPa':>13} {'kN':>12} {'kN':>12} {'kN':>10} {'kJ normal':>13} {'kJ normal':>13}"
          f" {'formwork':>9} {'t':>7} {'m':>9}")
    rows = {}
    for name, geo in g.items():
        c = CP[name]
        peak = (abs(c["local"]) + GCPI) * Q
        uplift = (abs(c["roof_avg"]) + GCPI) * Q * geo["roof_plan"]
        w_roof = SHELL_KG_M2 * geo["roof_area"] * 9.81
        w_walls = SHELL_KG_M2 * geo["wall_area"] * 9.81
        tie = max(uplift - w_roof, 0)
        sl = c["slope"]
        if sl is None:                                     # dome: crown is flat
            e_roof, e_wall_roof = E_ROOF, 0
        elif sl < 30:
            e_roof = E_ROOF * cos(radians(sl)) ** 2
        else:                                              # steep faces: treat as walls AND roofs, report the worse
            e_roof = max(E_ROOF * cos(radians(sl)) ** 2, E_WALL * sin(radians(sl)) ** 2)
        if name == "cone":
            step = COURSE_H / tan(radians(sl))
            dry = f"{step/UNIT_LEN*100:.0f}% oh"
        elif name == "pyramid":
            step = COURSE_H / tan(radians(sl))
            dry = f"{step/UNIT_LEN*100:.0f}% oh*"
        elif name == "dome":
            dry = "seats+key"
        else:
            dry = "NO (slab)"
        mass = SHELL_KG_M2 * (geo["roof_area"] + geo["wall_area"]) / 1000
        rows[name] = (peak, tie)
        print(f"{name:8s} {peak/1e3:13.1f} {uplift/1e3:12.0f} {w_roof/1e3:12.0f} {tie/1e3:10.0f}"
              f" {E_WALL/1e3:13.1f} {e_roof/1e3:13.1f} {dry:>9} {mass:7.1f} {geo['headroom']:9.2f}")
    print(f"\n  wall missile: 15 lb 2x4 at 100 mph = {E_WALL/1e3:.1f} kJ; roof missile at 67 mph = {E_ROOF/1e3:.1f} kJ"
          " (normal component; steep faces checked both ways)")
    print("  'oh' = corbel overhang per course as a share of the unit's radial length (units laid 295 mm deep);")
    print("  a closed round ring carries more overhang by hoop compression than a straight course (* pyramid")
    print("  faces are straight: no ring action, corners need special units).")
    print("\nreading it:")
    print("- ROUND beats square: no corner zones, where local suction peaks (the box's worst suction is ~2x the")
    print("  cone's), and the same load from any wind direction -- tornado winds rotate through all of them.")
    print("- STEEP beats flat: a 65 deg cone face turns the falling 2x4 into a glancing blow and sees mild")
    print("  suction; the flat box roof takes the full vertical missile AND the worst uplift, and it needs a")
    print("  reinforced slab -- the one thing fired clay can't be.")
    print("- the dome is round (good) but its crown is flat to a falling missile and sucked hardest by wind.")
    print("- 'tie-down' is the AVERAGE roof uplift beyond the roof's weight. LOCALLY every shape's peak suction")
    print(f"  (11-22 kPa) far exceeds the units' own weight ({SHELL_KG_M2*9.81/1e3:.1f} kPa), so courses would peel:")
    print("  every shape needs ties -- post-tensioned rods (cone: along the generators, from footing to a crown")
    print("  cap), the same rods as the wall panels. Sand in the cells adds weight and impact mass.")
    print("- the round corbelled cone -- the trullo -- is the lead shelter shape: round, steep, heavy, built")
    print("  course by course dry with horizontal beds and no formwork. It must pass ICC 500 missile tests.")
