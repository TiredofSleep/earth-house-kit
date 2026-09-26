#!/usr/bin/env python3
"""
build_timeline.py -- build time for one tilt-up earth house and a 10-house village.
Run: python3 build_timeline.py   (first-order; [TO-MEASURE] on the demo build)
Binder options: geopolymer (calcined clay + activator) or Roman-style lime-pozzolan
(calcined clay + hot-mixed quicklime; less clay to fire, longer cure).
"""
from common import WALL_KG, CREW_DAYS, CREW_SIZE

KILN_KWH_DAY = 60                                 # per kiln, from a 20 kW array's midday output
BINDERS = {
    # calcined-clay fraction of wall mass, kWh/kg (fire+mill), cure days before tilt
    "geopolymer (clay + activator)":   ((0.10, 0.15), (0.43, 0.85), (7, 14)),
    "Roman lime-pozzolan (hot mixed)": ((0.05, 0.08), (0.43, 0.85), (14, 28)),
    "cement fallback (6-8%)":          ((0.0, 0.0),   (0.0, 0.0),   (7, 7)),
}

def kiln_days(frac, spec, kilns):
    return tuple(WALL_KG * frac[i] * spec[i] / (KILN_KWH_DAY * kilns) for i in (0, 1))

if __name__ == "__main__":
    work = tuple(sum(v[i] for v in CREW_DAYS.values()) for i in (0, 1))
    print("=" * 64)
    print(f"BUILD TIMELINE (crew of ~{CREW_SIZE})")
    print("=" * 64)
    print(f"crew working days per house: {work[0]}-{work[1]}")
    for k, v in CREW_DAYS.items():
        print(f"    {k:36s} {v[0]}-{v[1]} days")
    for name, (frac, spec, cure) in BINDERS.items():
        k1 = kiln_days(frac, spec, 1); k2 = kiln_days(frac, spec, 2)
        # one house: kiln runs ahead of casting; elapsed ~ max(kiln, casting start) + work + cure wait
        lo = k2[0] + work[0] + cure[0]; hi = k1[1] + work[1] + cure[1]
        print(f"\n{name}")
        print(f"    kiln sunny-days per house: {k1[0]:.0f}-{k1[1]:.0f} (1 kiln), {k2[0]:.0f}-{k2[1]:.0f} (2 kilns)")
        print(f"    cure before tilt: {cure[0]}-{cure[1]} days")
        print(f"    one house, elapsed: ~{lo/7:.0f}-{hi/7:.0f} weeks (first build: add learning time)")
        # village: kiln and crews pipelined; two crews (cast / tilt+finish)
        v_kiln = (10 * k2[0], 10 * k1[1])
        v_crew = (10 * work[0] / 2, 10 * work[1] / 2)
        v_lo = max(v_kiln[0], v_crew[0]) + cure[0]
        v_hi = max(v_kiln[1], v_crew[1]) + cure[1]
        print(f"    10-house village, 2 crews pipelined: ~{v_lo/30:.1f}-{v_hi/30:.1f} months")
