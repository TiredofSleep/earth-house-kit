#!/usr/bin/env python3
"""
dome_check.py -- a dome of fired printed units over the polygon house (form_check.py).
Run: python3 dome_check.py

Membrane theory for a spherical shell under its own weight + skin + roof live load:
  meridional  N_phi   = -q R / (1 + cos phi)                 (always compression)
  hoop        N_theta =  q R (1/(1 + cos phi) - cos phi)      (tension below phi = 51.8 deg)
Base thrust H = -N_phi cos(phi0) per metre of rim -> tension ring T = H * a.
Masonry can't take hoop tension: a hemisphere cracks along its meridians in the lower band and
works as a ring of arches. Heyman: that still stands if the shell is thick enough to hold the
thrust line [t/R >= ~0.042 for a hemisphere, TO-VERIFY]. A cap that stops at 51.8 deg has no
hoop tension anywhere -- all compression, the ring takes the thrust.
Also: dry units on a steep bed slide during construction until their course closes into a ring;
keys (or temporary clips) must hold them there.
"""
import sys
from math import pi, sin, cos, tan, radians, degrees, atan, asin, acos
from form_check import polygon

G = 9.81
UNITS = {  # areal self-weight of the shell (clay + husk), kg/m2 and depth, from thermal_check.py
    "4.5 in cellular": dict(t=0.114, kg_m2=90, clay_kg_m2=82),
    "8 in thermal":    dict(t=0.200, kg_m2=133, clay_kg_m2=115),
    "12 in deep dome": dict(t=0.300, kg_m2=140, clay_kg_m2=120),   # ~22% clay: deeper, same weight [TO-MEASURE]
    "16 in deep dome": dict(t=0.406, kg_m2=170, clay_kg_m2=130),   # ~18% clay, more rows of husk cells [TO-MEASURE]
}
SKIN_KPA = 0.55                    # lime plaster 20 + 15 mm, both faces
LIVE_KPA = (0.5, 0.96)             # snow ~10 psf (Arkansas) .. 20 psf roof live load [TO-VERIFY ASCE 7]
MU = (0.48, 0.62)                  # dry clay joints at 0.1-0.5 MPa (PMC5458854)
MU_SAFETY = 1.5                    # beds steeper than atan(mu/1.5) ~18-22 deg need a seat step or key
HEYMAN_T_R = 0.042                 # hemisphere minimum t/R (Heyman; 0.0428 Coccia et al. 2016)
SEGMENTAL_T_R = 0.040              # segmental dome minimum t/R (Zessin, Lau & Ochsendorf)
GSF_TARGET = 2.0                   # geometric safety factor on thickness, 2-3x the minimum [UNSOURCED margin]
FM_NET = (3.2, 8.0)                # masonry strength on the clay area, MPa (brick_panel_check.py range)
COURSE = 0.193                     # course height along the meridian = unit width, m
RING = dict(name="steel C100 end channels bolted into a ring", area=1.0e-3, fy=250e6)  # [TO-VERIFY]
ROD = dict(area=157e-6, fy=640e6)  # M16 8.8, as in the panels
FIRE_MJ_KG = (1.1, 3.0)
HUSK_MJ = (13.0, 16.0)


def forces(q, R, phi):
    n_phi = -q * R / (1 + cos(phi))
    n_th = q * R * (1 / (1 + cos(phi)) - cos(phi))
    return n_phi, n_th


def dome(a, phi0_deg, unit, live):
    phi0 = radians(phi0_deg)
    R = a / sin(phi0)
    rise = R * (1 - cos(phi0))
    area = 2 * pi * R * rise
    q = unit["kg_m2"] * G + (SKIN_KPA + live) * 1e3          # Pa on the shell surface (conservative)
    n_phi, n_th_base = forces(q, R, phi0)
    H = -n_phi * cos(phi0)                                     # N/m outward at the rim
    V = -n_phi * sin(phi0)                                     # N/m down onto the walls
    T = H * a                                                  # ring tension, N
    t_net = unit["t"] * unit["clay_kg_m2"] / (unit["t"] * 1800)  # clay-equivalent thickness
    sigma = -n_phi / (unit["t"] * (unit["clay_kg_m2"] / (1800 * unit["t"]))) / 1e6
    # hoop tension band (membrane): phi > 51.83 deg
    tension_band = max(0.0, phi0_deg - 51.83)
    # construction: bed inclination to horizontal = 90 - phi; slides if > friction angle
    fric = [degrees(atan(m / MU_SAFETY)) for m in MU]
    slide_below = [90 - f for f in fric]                        # phi below this slides (steep beds)
    def cap_area(phi):
        return 2 * pi * R * R * (1 - cos(radians(min(phi, phi0_deg))))
    keyed = [cap_area(s) / area for s in slide_below]           # share needing keys
    courses = (R * phi0) / COURSE
    fired_kg = area * unit["clay_kg_m2"]
    husks = (fired_kg * FIRE_MJ_KG[0] / HUSK_MJ[1], fired_kg * FIRE_MJ_KG[1] / HUSK_MJ[0])
    return dict(R=R, rise=rise, area=area, q=q, H=H, V=V, T=T, sigma=sigma, tension_band=tension_band,
                keyed=keyed, courses=courses, fired=fired_kg, husks=husks,
                gsf=unit["t"] / ((HEYMAN_T_R if phi0_deg >= 89 else SEGMENTAL_T_R) * R))


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ring_cap = RING["area"] * RING["fy"]
    rod_cap = ROD["area"] * ROD["fy"]
    for n in (16, 20):
        area_ft2, d_ft = polygon(n)
        a = d_ft * 0.3048 / 2
        print("=" * 104)
        print(f"{n}-gon house: {area_ft2:.0f} ft^2, rim radius {a:.2f} m (span {2*a:.2f} m); live load {LIVE_KPA[1]} kPa")
        print("=" * 104)
        print(f"{'dome':34s} {'rise':>5} {'area':>6} {'thrust':>7} {'ring T':>7} {'on walls':>8}"
              f" {'stress':>7} {'hoop-tension':>12} {'thickness':>9} {'courses':>7} {'husks':>9}")
        print(f"{'':34s} {'m':>5} {'m2':>6} {'kN/m':>7} {'kN':>7} {'kN/m':>8} {'MPa':>7} {'band':>12}"
              f" {'x minimum':>9} {'':>7} {'t':>9}")
        for uname, unit in UNITS.items():
            for phi0, label in [(90, "hemisphere"), (51.8, "cap to 51.8 deg (no hoop tension)"),
                                (40, "shallow cap to 40 deg")]:
                r = dome(a, phi0, unit, LIVE_KPA[1])
                band = f"{r['tension_band']:.0f} deg at base" if r["tension_band"] > 0 else "none"
                print(f"{(uname + ', ' + label)[:34]:34s} {r['rise']:5.2f} {r['area']:6.1f} {r['H']/1e3:7.2f}"
                      f" {r['T']/1e3:7.1f} {r['V']/1e3:8.2f} {r['sigma']:7.3f} {band:>12}"
                      f" {r['gsf']:6.1f}x{'!' if r['gsf'] < GSF_TARGET else ' '} {r['courses']:7.0f}"
                      f" {r['husks'][0]/1e3:4.2f}-{r['husks'][1]/1e3:<4.2f}")
        r = dome(a, 51.8, UNITS["12 in deep dome"], LIVE_KPA[1])
        print(f"\n  RING for the 51.8 deg cap, 12 in deep units: tension {r['T']/1e3:.1f} kN vs {RING['name']}"
              f" {ring_cap/1e3:.0f} kN at yield ({ring_cap/r['T']:.0f}x),")
        print(f"  or ONE M16 rod ring at 25% of yield ({0.25*rod_cap/1e3:.0f} kN, {0.25*rod_cap/r['T']:.1f}x) -- the same rods"
              " as the panels, inspectable and re-tensionable")
        n_units = r["area"] / (0.295 * COURSE)
        print(f"  units: ~{n_units:,.0f} printed voussoirs in {r['courses']:.0f} courses (one taper per course),"
              f" {r['area']*UNITS['12 in deep dome']['kg_m2']/1e3:.1f} t with husk fill")
        print(f"  shell stress {r['sigma']:.3f} MPa vs masonry {FM_NET[0]}-{FM_NET[1]} MPa on the clay:"
              f" {FM_NET[0]/r['sigma']:.0f}x margin")
    print("\nreading the table:")
    print("- stresses are tiny: a dome of fired units works at ~1-2% of its strength; its enemies are")
    print("  hoop tension (hemisphere), thrust at the rim (caps), and sliding while it's being built.")
    print("- the 51.8 deg cap is ALL compression -> the rim thrust goes into a steel ring made from the")
    print("  panels' top end channels (or rods): one tension element, in plain sight.")
    print(f"- 'thickness x minimum' = depth / (Heyman or segmental minimum t/R x R); '!' = under {GSF_TARGET}x."
          " Depth, not weight, keeps the")
    print("  thrust line inside the shell -> a DEEP cellular voussoir at the same weight is the answer.")
    print(f"- dry build: beds steeper than atan(mu/{MU_SAFETY}) = {degrees(atan(MU[0]/MU_SAFETY)):.0f}-"
          f"{degrees(atan(MU[1]/MU_SAFETY)):.0f} deg slide -> EVERY course of a 51.8 deg cap does. Each voussoir sits")
    print("  on a SEAT STEP (a bearing ledge, compression only -- never a clay hook in tension) until its")
    print("  course closes; then hoop compression holds it. Brunelleschi's herringbone did the same job.")
    print("- a SPHERICAL dome's courses all subtend the same angle -> one die section for every voussoir;")
    print("  only the hoop end-cut changes per course.")
