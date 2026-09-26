#!/usr/bin/env python3
"""
dome_thrust.py -- the fired-unit dome under UNEVEN loads: half snow, wind, earthquake.
Run: python3 dome_thrust.py

Method: Heyman's safe theorem. If ANY line of thrust in equilibrium with the loads fits inside the
masonry, and no joint slides, the dome stands. We cut the dome into 'orange slices' (two opposite
lunes through the crown form one arch) and give them NO help from hoop compression -- the
conservative, lower-bound model Heyman used for cracked domes. Real domes also carry load around
the rings, so passing here means passing with margin.

For each load case we search (scipy) for the thrust line with the smallest worst-case eccentricity:
  geometric safety factor GSF = (t/2) / max|e|      (>= 1 stands; masonry practice seeks 2-3)
and check every radial joint for dry sliding: |radial force| / |tangential force| <= mu / 1.5.
Wind pressure coefficients and seismic coefficients are placeholders [TO-VERIFY per site].
"""
import sys
import numpy as np
from math import radians, degrees, atan
from scipy.optimize import minimize
from form_check import polygon
import dome_check as dc

G = 9.81
N = 90                                   # voussoir segments along the arch
Q_WIND = 0.613 * 50**2                   # 50 m/s velocity pressure, Pa
CP = [(0.0, +0.6), (0.5, -1.2), (1.0, -0.4)]   # windward rim, crown, leeward rim [TO-VERIFY EN 1991-1-4 7.2.8]
SNOW = dc.LIVE_KPA[1] * 1e3              # 0.96 kPa on plan
KH = (0.15, 0.30)                        # horizontal seismic coefficient [TO-VERIFY site hazard]
MU_ALLOW = dc.MU[0] / dc.MU_SAFETY       # 0.48 / 1.5


def cp(u):
    xs, ys = zip(*CP)
    return np.interp(u, xs, ys)


def arch(R, phi0, t, g_pa):
    """joints at angles phi_j from the crown; per radian of lune width"""
    phi = np.linspace(-phi0, phi0, N + 1)
    a, b = phi[:-1], phi[1:]
    mid = (a + b) / 2
    def absint_sin(a, b):                 # integral of |sin| from a to b
        out = np.where(a * b >= 0, np.abs(np.cos(a) - np.cos(b)), (1 - np.cos(a)) + (1 - np.cos(b)))
        return out
    area = R * R * absint_sin(a, b)       # surface area per radian of lune
    plan = R * R * np.abs(np.sin(b)**2 - np.sin(a)**2) / 2
    plan = np.where(a * b >= 0, plan, R * R * (np.sin(a)**2 + np.sin(b)**2) / 2)
    pts = np.stack([R * np.sin(mid), R * np.cos(mid)], axis=1)
    nr = np.stack([np.sin(mid), np.cos(mid)], axis=1)
    return dict(phi=phi, mid=mid, area=area, plan=plan, pts=pts, nr=nr, R=R, t=t, g=g_pa, phi0=phi0)


def loads(A, case):
    n = len(A["mid"])
    F = np.zeros((n, 2))
    W = A["g"] * A["area"]
    F[:, 1] -= W
    if case.get("snow") == "full":
        F[:, 1] -= SNOW * A["plan"]
    if case.get("snow") == "half":
        F[:, 1] -= np.where(A["mid"] > 0, SNOW * A["plan"], 0)
    if case.get("wind"):
        u = (A["mid"] + A["phi0"]) / (2 * A["phi0"])
        p = Q_WIND * cp(u)                                  # + pressure pushes inward
        F -= (p * A["area"])[:, None] * A["nr"]
    if case.get("kh"):
        F[:, 0] += case["kh"] * W
    return F


def trace(A, F, params):
    """thrust line from the left springing (vectorized); eccentricities, compression, sliding ratios"""
    Rx, Ry, eL = params
    phi, R = A["phi"], A["R"]
    nr = np.stack([np.sin(phi), np.cos(phi)], axis=1)
    tg = np.stack([np.cos(phi), -np.sin(phi)], axis=1)
    P0 = (R + eL) * nr[0]
    f = np.vstack([[0.0, 0.0], np.cumsum(F, axis=0)]) + [Rx, Ry]       # resultant left of each joint
    mom = A["pts"][:, 0] * F[:, 1] - A["pts"][:, 1] * F[:, 0]
    M = (P0[0] * Ry - P0[1] * Rx) + np.concatenate([[0.0], np.cumsum(mom)])
    cross = nr[:, 0] * f[:, 1] - nr[:, 1] * f[:, 0]
    e = np.where(np.abs(cross) > 1e-9, M / np.where(np.abs(cross) > 1e-9, cross, 1) - R, 1e9)
    comp = np.sum(f * tg, axis=1)
    slide = np.where(comp > 0, np.abs(np.sum(f * nr, axis=1)) / np.where(comp > 0, comp, 1), 1e9)
    return e, comp, slide


def solve(A, F):
    t = A["t"]
    Wtot = -F[:, 1].sum()
    def obj(p):
        e, comp, _ = trace(A, F, p)
        pen = np.sum(np.clip(-comp, 0, None)) / (Wtot + 1) * 100
        return np.max(np.abs(e)) / (t / 2) + pen
    best = None
    for hx in (0.3, 0.8, 1.5):
        for ry in (0.4, 0.6):
            for el in (-0.2, 0.2):
                r = minimize(obj, [hx * Wtot, ry * Wtot, el * t / 2], method="Nelder-Mead",
                             options=dict(xatol=1e-6, fatol=1e-7, maxiter=4000))
                if best is None or r.fun < best.fun:
                    best = r
    e, comp, slide = trace(A, F, best.x)
    return dict(gsf=1 / best.fun if best.fun > 0 else np.inf, e=e, slide=slide.max(),
                H=best.x[0], comp_ok=bool((comp > 0).all()), jmax=int(np.argmax(np.abs(e))))


CASES = [
    ("dead load (self + skin)",               dict()),
    ("dead + full snow",                      dict(snow="full")),
    ("dead + HALF snow (unbalanced)",         dict(snow="half")),
    ("dead + wind 50 m/s",                    dict(wind=True)),
    ("dead + wind + half snow",               dict(wind=True, snow="half")),
    (f"dead + earthquake kh={KH[0]}",         dict(kh=KH[0])),
    (f"dead + earthquake kh={KH[1]}",         dict(kh=KH[1])),
]

if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    SKIN_TILED = 1.15e3   # 20 mm cocciopesto + overlapping fired scale tiles + interior lime [UNSOURCED weights]
    for n_sides, uname, skin in [(16, "16 in deep dome", dc.SKIN_KPA * 1e3), (20, "16 in deep dome", dc.SKIN_KPA * 1e3),
                                 (20, "12 in deep dome", dc.SKIN_KPA * 1e3),
                                 (16, "16 in deep dome", SKIN_TILED), (20, "16 in deep dome", SKIN_TILED)]:
        area_ft2, d_ft = polygon(n_sides)
        a = d_ft * 0.3048 / 2
        phi0 = radians(51.8)
        R = a / np.sin(phi0)
        unit = dc.UNITS[uname]
        g = unit["kg_m2"] * G + skin
        A = arch(R, phi0, unit["t"], g)
        print("=" * 92)
        print(f"{n_sides}-gon, cap to 51.8 deg, R {R:.2f} m, {uname} (t {unit['t']*1000:.0f} mm),"
              f" dead {g/1e3:.2f} kPa{' (TILED SKIN)' if skin > 1000 else ''} -- orange-slice arch, NO hoop help")
        print("=" * 92)
        print(f"{'load case':34s} {'GSF':>6} {'worst joint':>12} {'sliding':>9} {'thrust':>8}  verdict")
        print(f"{'':34s} {'':>6} {'(deg)':>12} {'/allowed':>9} {'kN/rad':>8}")
        for name, case in CASES:
            F = loads(A, case)
            r = solve(A, F)
            ang = degrees(A["phi"][r["jmax"]])
            sl = r["slide"] / MU_ALLOW
            verdict = ("STANDS" if r["gsf"] >= 1 else "NO LINE FITS") + \
                      (", margin OK" if r["gsf"] >= 1.5 else (", thin margin" if r["gsf"] >= 1 else "")) + \
                      ("" if sl <= 1 else ", SLIDES at a dry joint")
            print(f"{name:34s} {r['gsf']:6.2f} {ang:12.0f} {sl:9.2f} {r['H']/1e3:8.1f}  {verdict}")
    print("\nreading the table:")
    print("- GSF >= 1: a thrust line fits inside the voussoirs with the slices carrying everything alone;")
    print("  the real dome also carries load around its rings, so it is stronger than this.")
    print("- 'sliding' = worst radial-to-tangential force ratio at a dry joint over the allowed mu/1.5;")
    print("  above 1 means a joint needs a key or seat to carry that shear.")
    print("- wind suction lifts the crown: a HEAVY dome resists it; don't lighten the crown below the dead load.")
