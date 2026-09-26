#!/usr/bin/env python3
"""
dome_ribbed.py -- a RIBBED fired-unit dome: deep ribs carry the thrust, thin webs span between them.
Run: python3 dome_ribbed.py

Why: the 16 in cellular dome passes every load case, but it's ~half the kit's clay. A thrust line
needs DEPTH only where the thrust goes. Put the depth in meridional ribs (Gothic ribbed vaults,
ETH's Rippmann floor) and let thin webs span the short gaps between them.
  ribs : 16 in deep units, one rib on each wall fold (they land where the panels meet), meeting a
         compression ring at the oculus; a constant section with skewback seats on both sides -> ONE die
  webs : 6 in graded units (thermal_check.py: U ~0.56 alone) spanning rib to rib as shallow arches,
         built course by course on the skewbacks, each bay-course closed by a key unit
Checks (Heyman safe theorem, same method as dome_thrust.py):
  1. each rib as an arch carrying its own weight + its tributary web, skin, snow, wind, earthquake
  2. each web as a shallow arch between ribs at the rim (widest span), mid-height, and near the crown,
     with the load normal to the shell -- including wind suction that nearly lifts it
  3. clay per m2 vs the 16 in cellular dome
"""
import sys
import numpy as np
from math import pi, sin, cos, radians, degrees, atan
from form_check import polygon
import dome_check as dc
import dome_thrust as dt

G = 9.81
PHI0 = radians(51.8)
RIB = dict(depth=0.406, width=0.193, clay_kg_m=30.0, total_kg_m=40.0)   # 16 in unit + skewbacks [TO-MEASURE]
WEB = dict(depth=0.152, clay_kg_m2=72.0, total_kg_m2=86.0)              # 6 in graded unit (thermal_check.py)
SOLID = dict(clay_kg_m2=dc.UNITS["16 in deep dome"]["clay_kg_m2"], total_kg_m2=dc.UNITS["16 in deep dome"]["kg_m2"])
SKIN = 1.15e3                                                          # tiled cocciopesto skin, Pa (dome_thrust.py)
N_SEG = 90


def geometry(n_sides):
    area_ft2, d_ft = polygon(n_sides)
    a = d_ft * 0.3048 / 2
    R = a / sin(PHI0)
    return a, R, 2 * pi * R * R * (1 - cos(PHI0))


def rib_arch(R, n_ribs, case):
    """two opposite ribs through the crown as one arch; loads per segment (N)"""
    phi = np.linspace(-PHI0, PHI0, N_SEG + 1)
    a_, b_ = phi[:-1], phi[1:]
    mid = (a_ + b_) / 2
    ds = R * (b_ - a_)
    bay = 2 * pi / n_ribs                                    # radians of lune per rib
    trib_w = np.maximum(bay * R * np.abs(np.sin(mid)) - RIB["width"], 0)   # web width carried, m
    w_rib = RIB["total_kg_m"] * G * ds
    w_web = (WEB["total_kg_m2"] * G + SKIN) * trib_w * ds
    W = w_rib + w_web
    F = np.zeros((N_SEG, 2))
    F[:, 1] -= W
    plan = trib_w * ds * np.abs(np.cos(mid))
    if case.get("snow") == "full":
        F[:, 1] -= dt.SNOW * plan
    if case.get("snow") == "half":
        F[:, 1] -= np.where(mid > 0, dt.SNOW * plan, 0)
    nr = np.stack([np.sin(mid), np.cos(mid)], axis=1)
    if case.get("wind"):
        u = (mid + PHI0) / (2 * PHI0)
        p = dt.Q_WIND * dt.cp(u)
        F -= (p * (trib_w + RIB["width"]) * ds)[:, None] * nr
    if case.get("kh"):
        F[:, 0] += case["kh"] * W
    A = dict(phi=phi, mid=mid, pts=np.stack([R * np.sin(mid), R * np.cos(mid)], axis=1), nr=nr,
             R=R, t=RIB["depth"], phi0=PHI0)
    return A, F


def web_arch(R, n_ribs, phi_at, case):
    """a web strip spanning between two ribs at height phi_at: a shallow circular arch in the
    hoop direction, radius = hoop radius R sin(phi), half-angle = pi/n_ribs, depth = web depth.
    Load normal to the shell: dead*cos(phi) + snow*cos^2(phi) - wind suction (Cp at that height)."""
    r_h = R * sin(phi_at)
    half = pi / n_ribs
    phi = np.linspace(-half, half, N_SEG + 1)
    a_, b_ = phi[:-1], phi[1:]
    mid = (a_ + b_) / 2
    ds = r_h * (b_ - a_)                                    # 1 m wide strip
    q = (WEB["total_kg_m2"] * G + SKIN) * cos(phi_at)
    if case.get("snow"):
        q_snow = dt.SNOW * cos(phi_at) ** 2
    else:
        q_snow = 0.0
    if case.get("wind"):
        u_wind = (PHI0 - phi_at) / (2 * PHI0)               # this height on the windward side
        u_lee = (PHI0 + phi_at) / (2 * PHI0)                # ... and on the leeward side
        q_wind = -dt.Q_WIND * min(dt.cp(u_wind), dt.cp(u_lee))   # the worse of the two (suction < 0)
    else:
        q_wind = 0.0
    load = np.full(N_SEG, q)
    if case.get("snow") == "half":
        load = load + np.where(mid > 0, q_snow, 0)
    elif case.get("snow") == "full":
        load = load + q_snow
    load = load - q_wind
    F = np.zeros((N_SEG, 2))
    F[:, 1] -= load * ds
    A = dict(phi=phi, mid=mid, pts=np.stack([r_h * np.sin(mid), r_h * np.cos(mid)], axis=1),
             nr=np.stack([np.sin(mid), np.cos(mid)], axis=1), R=r_h, t=WEB["depth"], phi0=half)
    return A, F, load.min(), 2 * r_h * sin(half)


TENDON = dict(name="10 mm stainless wire rope, swaged threaded ends, nut-tensioned at the oculus",
              lock=20e3, loss=0.35, mbl=56e3)   # MBL of 10 mm 316 7x19 rope ~56 kN [TO-VERIFY]; no wedge seating loss
P_DESIGN = TENDON["lock"] * (1 - TENDON["loss"])  # checked AFTER losses


def solve_pt(A, F, P):
    """dt.solve, with a tendon of force P along the rib centroid: every joint gets +P of compression
    and no moment (a circular tendon's radial pull P/R and end forces balance), so eccentricity
    shrinks to e*N/(N+P) and sliding to |V|/(N+P)."""
    t = A["t"]
    Wtot = -F[:, 1].sum() + 1
    def ev(p):
        e, comp, _ = dt.trace(A, F, p)
        phi = A["phi"]
        f_cum = np.vstack([[0.0, 0.0], np.cumsum(F, axis=0)]) + [p[0], p[1]]
        nr = np.stack([np.sin(phi), np.cos(phi)], axis=1)
        radial = np.abs(np.sum(f_cum * nr, axis=1))
        N = comp + P
        e2 = e * np.where(N > 0, comp / N, 1e9)
        return e2, N, radial / np.where(N > 0, N, 1e-9)
    def obj(p):
        e2, N, _ = ev(p)
        pen = np.sum(np.clip(-N, 0, None)) / Wtot * 100
        return np.max(np.abs(e2)) / (t / 2) + pen
    from scipy.optimize import minimize
    best = None
    for hx in (0.3, 0.8, 1.5):
        for ry in (0.4, 0.6):
            for el in (-0.2, 0.2):
                r = minimize(obj, [hx * Wtot, ry * Wtot, el * t / 2], method="Nelder-Mead",
                             options=dict(xatol=1e-6, fatol=1e-7, maxiter=4000))
                if best is None or r.fun < best.fun:
                    best = r
    e2, N, sl = ev(best.x)
    return dict(gsf=1 / best.fun if best.fun > 0 else np.inf, slide=sl.max())


def clay(n_sides, n_ribs):
    a, R, area = geometry(n_sides)
    rib_len = n_ribs * R * PHI0
    rib_area = rib_len * RIB["width"]
    web_area = max(area - rib_area, 0)
    clay_kg = rib_len * RIB["clay_kg_m"] + web_area * WEB["clay_kg_m2"]
    total_kg = rib_len * RIB["total_kg_m"] + web_area * WEB["total_kg_m2"]
    return dict(area=area, clay=clay_kg, total=total_kg, solid_clay=area * SOLID["clay_kg_m2"],
                solid_total=area * SOLID["total_kg_m2"], rib_len=rib_len)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    for n_sides in (16, 20):
        a, R, area = geometry(n_sides)
        for n_ribs in (n_sides, n_sides // 2):
            m = clay(n_sides, n_ribs)
            print("=" * 100)
            print(f"{n_sides}-gon cap to 51.8 deg (R {R:.2f} m, {area:.1f} m2): {n_ribs} ribs"
                  f" {RIB['depth']*1000:.0f} mm deep + {WEB['depth']*1000:.0f} mm graded webs")
            print("=" * 100)
            print(f"  clay {m['clay']/1e3:.2f} t vs {m['solid_clay']/1e3:.2f} t for the 16 in cellular dome"
                  f" -> {100*(1-m['clay']/m['solid_clay']):.0f}% less clay;"
                  f" total {m['total']/1e3:.2f} t vs {m['solid_total']/1e3:.2f} t")
            P = P_DESIGN
            print(f"  RIBS as arches (tributary web, no hoop help): plain dry joints | post-tensioned: {TENDON['name']},"
                  f" locked {TENDON['lock']/1e3:.0f} kN, checked at {P/1e3:.0f} kN after {TENDON['loss']*100:.0f}% loss")
            s_clay = TENDON["lock"] / (RIB["depth"] * RIB["width"] * 0.22) / 1e6
            print(f"  prestress on the rib clay at lock: {s_clay:.2f} MPa (22% clay rib); rope at"
                  f" {TENDON['lock']/TENDON['mbl']*100:.0f}% of its breaking load")
            for name, case in dt.CASES:
                A, F = rib_arch(R, n_ribs, case)
                r0 = dt.solve(A, F)
                r1 = solve_pt(A, F, P)
                s0, s1 = r0["slide"] / dt.MU_ALLOW, r1["slide"] / dt.MU_ALLOW
                v = lambda g, sl: "OK" if g >= 1.5 and sl <= 1 else ("thin" if g >= 1 and sl <= 1 else "FAIL")
                print(f"    {name:34s} GSF {r0['gsf']:5.2f} slide {s0:4.2f} {v(r0['gsf'], s0):4s} |"
                      f" GSF {r1['gsf']:5.2f} slide {s1:4.2f} {v(r1['gsf'], s1)}")
            print(f"  WEBS between ribs (shallow hoop arches, load normal to the shell):")
            for phi_deg in (51.8, 35, 20):
                for name, case in [("dead + half snow", dict(snow="half")), ("dead + wind (crown suction)", dict(wind=True))]:
                    A, F, qmin, span = web_arch(R, n_ribs, radians(phi_deg), case)
                    if qmin <= 0:
                        print(f"    at {phi_deg:4.1f} deg, span {span:.2f} m, {name:28s}: NET UPLIFT {qmin/1e3:.2f} kPa"
                              " -> needs hoop compression or ballast")
                        continue
                    r = dt.solve(A, F)
                    print(f"    at {phi_deg:4.1f} deg, span {span:.2f} m, {name:28s}: GSF {r['gsf']:5.2f},"
                          f" net load {qmin/1e3:.2f} kPa")
    print("\nreading it:")
    print("- ribs carry the thrust with the same deep section as the solid dome, but only along ~16 lines;")
    print("  the webs between span short, shallow arches and can be thinner, insulating graded units.")
    print("- webs are flat arches: they need their load to stay DOWNWARD. The heavy tiled skin is what keeps")
    print("  the net load positive under crown wind suction -- do not lighten the skin.")
    print("- plain dry ribs fail in wind (light + suction). ONE post-tensioned strand per rib (Dieste prestressed")
    print("  his brick vaults) clamps every joint and pulls the rib inward by P/R against the suction.")
    print("- ribs are a constant section (skewback seats on both sides): one die; webs: the 6 in wall die.")
