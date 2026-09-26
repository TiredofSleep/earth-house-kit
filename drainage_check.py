#!/usr/bin/env python3
"""
drainage_check.py -- a foundation that clears water away on purpose: fluted fired bricks on a
crowned, compacted earth platform.
Run: python3 drainage_check.py

The water path, from the sky to away from the house:
  dome + scale tiles -> corbelled drip eave throws water clear of the wall
  -> FLUTED APRON RING: fired pavers on the compacted, crowned earth pad, falling outward, their
     flutes running radially to carry the drip-line water outward (and break the splash)
  -> COLLECTOR RING: a fluted channel course round the apron edge, falling to the cistern inlet
     (first flush first), overflow to a rubble trench / daylight
  -> PLINTH units below grade with VERTICAL flutes on their outer face = a drainage plane down to
  -> a fired-clay drain tile at the bottom of the rubble trench, sloped to daylight.
Checks: design-storm flow from the dome, flute and channel capacity (Manning), platform falls,
and the water the cistern gets. Storm intensities are placeholders [TO-VERIFY NOAA Atlas 14].
"""
import sys
from math import pi, sqrt
from form_check import polygon

FT = 0.3048
EAVE_OVERHANG = 0.30              # corbelled eave projects beyond the wall face, m
INTENSITY_MM_H = (214, 300)       # 10-yr / 100-yr 5-minute intensity, Hot Springs (NOAA Atlas 14, 34.50N 93.06W);
                                  # Machu Picchu's drains were designed for ~200 mm/h (Wright & Valencia)
N_CLAY = 0.013                    # Manning n, smooth fired clay
FLUTE = dict(w=0.030, d=0.015, pitch=0.060)     # apron flute: 30 mm wide, 15 mm deep, every 60 mm
APRON = dict(width=0.90, fall=0.05)             # 0.9 m wide, 5% outward
CHANNEL = dict(w=0.10, d=0.075, fall=0.01)      # collector ring: 100 x 75 mm, 1% to the cistern
PAD_FALL = 0.05                   # ground falls 5% outward for 3 m (IRC R401.3); hard surfaces >= 2%
RAIN_YEAR_M = 1.30                # annual rain, Hot Springs
RUNOFF = 0.8                      # tiled dome runoff coefficient [TO-VERIFY]
FIRST_FLUSH_L_M2 = (1.0, 2.0)


def manning_q(w, d, S, n=N_CLAY):
    A = w * d
    P = w + 2 * d
    R = A / P
    return A * (1 / n) * R ** (2 / 3) * sqrt(S)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 92)
    print("FLUTED DRAINAGE FOUNDATION: drip eave -> fluted apron -> collector ring -> cistern / drain")
    print("=" * 92)
    for n in (16, 20):
        area_ft2, d_ft = polygon(n)
        r_wall = d_ft * FT / 2
        r_drip = r_wall + EAVE_OVERHANG
        roof_plan = pi * r_drip ** 2
        perim_drip = 2 * pi * r_drip
        print(f"\n{n}-gon: roof plan {roof_plan:.1f} m2, drip line {perim_drip:.1f} m round, "
              f"{EAVE_OVERHANG*100:.0f} cm out from the wall")
        for i in INTENSITY_MM_H:
            Q = roof_plan * i / 1000 / 3600                    # m3/s
            q_per_m = Q / perim_drip
            fl = manning_q(FLUTE["w"], FLUTE["d"], APRON["fall"])
            apron_cap = fl / FLUTE["pitch"]                    # m3/s per m of apron edge
            ch = manning_q(CHANNEL["w"], CHANNEL["d"], CHANNEL["fall"])
            ch_need = Q / 2                                    # ring drains both ways to one inlet
            print(f"  storm {i} mm/h: {Q*1000:.2f} L/s off the dome = {q_per_m*1000:.3f} L/s per m of drip line")
            print(f"    apron flutes ({FLUTE['w']*1000:.0f}x{FLUTE['d']*1000:.0f} mm at {APRON['fall']*100:.0f}%):"
                  f" {fl*1000:.2f} L/s each, {apron_cap*1000:.1f} L/s per m -> {apron_cap/q_per_m:,.0f}x the drip")
            print(f"    collector ring ({CHANNEL['w']*1000:.0f}x{CHANNEL['d']*1000:.0f} mm at {CHANNEL['fall']*100:.0f}%):"
                  f" {ch*1000:.1f} L/s vs {ch_need*1000:.2f} L/s at the inlet -> {ch/ch_need:.0f}x")
        yearly = RUNOFF * RAIN_YEAR_M * roof_plan
        ff = [roof_plan * f for f in FIRST_FLUSH_L_M2]
        print(f"  rain harvested: ~{yearly:.0f} m3/yr (~{yearly*1000/365:.0f} L/day average);"
              f" first flush {ff[0]:.0f}-{ff[1]:.0f} L per storm")
        print(f"  platform: crowned pad falls {PAD_FALL*100:.0f}% -> {PAD_FALL*3.05*1000:.0f} mm in the first 3 m"
              f" (IRC R401.3 asks 6 in in 10 ft); apron starts >= 150 mm below the plinth top")
    print("\nreading it:")
    print("- flutes are not about capacity (they carry 30x+ the design drip); they are about CONTROL:")
    print("  they break the splash, stop sheet flow wandering back to the wall, and point every drop outward.")
    print("- capacity sits in the collector ring; it's the one channel to size carefully and keep clean.")
    print("- the compacted earth pad is the house's platform, NOT its wall: keep it dry and crowned; on")
    print("  expansive clay replace it with granular fill (the pad must not heave).")
