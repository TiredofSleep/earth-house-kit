#!/usr/bin/env python3
"""
form_check.py -- what building SHAPE gets the most from each 4 ft panel?
Run: python3 form_check.py

Every panel is a 4 ft module. A square plan puts 20 modules around 400 ft^2. A polygon plan of the
same modules encloses more floor per panel, exposes less wall per unit of floor (less heat gain and
loss), meets the wind with a rounded face, and -- once the ring is closed -- braces itself: every
joint is a fold, so the walls stiffen each other and the temporary braces come off sooner.
A round plan also takes a compression-only roof (dome or cone of fired units): the shape that
has stood for centuries in fired brick.
"""
from math import pi, tan, sin

MODULE_FT = 4
OPENINGS = 3                    # one door + two windows, one module each (TILTUP_DETAILING.md)
FT2_M2 = 0.0929
CD = {"box": (1.2, 1.4), "round": (0.6, 0.9)}   # overall drag coefficient, low-rise [TO-VERIFY: ASCE 7 / EN 1991-1-4]


def polygon(n, s=MODULE_FT):
    area = n * s * s / (4 * tan(pi / n))
    R = s / (2 * sin(pi / n))
    return area, 2 * R


PLANS = [("square 20x20 ft", 20, 400.0, None, "box"),
         ("rectangle 16x24 ft", 20, 384.0, None, "box")]
for n in (8, 12, 16, 20, 24):
    a, d = polygon(n)
    PLANS.append((f"{n}-gon, {n} modules", n, a, d, "round" if n >= 12 else "box"))

if __name__ == "__main__":
    print("=" * 96)
    print(f"PLAN SHAPE: 4 ft panel modules, {OPENINGS} module-wide openings, 8 ft walls")
    print("=" * 96)
    print(f"{'plan':24s} {'modules':>7} {'panels':>6} {'floor ft2':>9} {'m2':>5} {'ft2/panel':>9}"
          f" {'wall/floor':>10} {'span ft':>8} {'wind Cd':>8}")
    base = 400.0 / (20 - OPENINGS)
    for name, n, area, d, kind in PLANS:
        panels = n - OPENINGS
        wall_ratio = n * MODULE_FT * 8 / area
        span = f"{d:.1f}" if d else ("20.0" if "square" in name else "16.0")
        print(f"{name:24s} {n:7d} {panels:6d} {area:9.0f} {area*FT2_M2:5.0f} {area/panels:9.1f}"
              f" {wall_ratio:10.2f} {span:>8} {CD[kind][0]}-{CD[kind][1]:<4}")
    a16, d16 = polygon(16)
    a20, d20 = polygon(20)
    print(f"\n-> a 20-gon uses the SAME 20 modules as the square and encloses {polygon(20)[0]/400*100-100:.0f}% more floor"
          f" ({polygon(20)[0]:.0f} vs 400 ft^2);")
    print(f"   per panel: {a20/(20-OPENINGS):.1f} vs {base:.1f} ft^2. A 16-gon gives {a16:.0f} ft^2 from 13 panels.")
    print("-> a closed polygon braces itself: only the first panels of the ring need full temporary bracing.")
    print(f"-> roof: a 16-gon spans {d16:.1f} ft ({d16*0.3048:.1f} m) across; a 20-gon {d20:.1f} ft ({d20*0.3048:.1f} m)."
          " Nubian vaults")
    print("   span ~3-4 m; a dome of fired units over 6-8 m needs its thrust taken by a ring or buttressing")
    print("   [TO-CHECK: dome thrust vs panel and ring capacity] -- see making-system/BRICK_PANEL.md section 7.")
