#!/usr/bin/env python3
"""
tiltup_check.py -- can a reinforced earth panel cast flat in the ground be tilted up?
Run: python3 tiltup_check.py
1. lift stress vs earth cracking strength (with a safety margin), pick point optimized
2. breakaway: bed suction at the first lift
3. what the steel carries -- limited by the EARTH crushing, not just by the steel yielding
4. bond the earth must supply, surface-grid variant
5. openings (doors/windows) and the hoist/insert loads
6. wind on a braced panel before the bond beam and roof tie it in
Detailing that uses these numbers: making-system/TILTUP_DETAILING.md
"""
import numpy as np
from common import (FT, IN, G, RHO_LIFT, PANEL_H, PANEL_W, PANEL_T, IMPACT, MOR, MOR_SAFETY,
                    F_C, SUCTION_KPA, BAR4_AREA, BAR4_DIA, COVER, lift_moments, flexural_capacity)

BARS = 4                                  # #4 bars per 4 ft of width in the tension layer


def panel(height_ft=8, width_ft=4, thick_in=6):
    L, b, h = height_ft * FT, width_ft * FT, thick_in * IN
    mass = RHO_LIFT * L * b * h
    w = mass * G / L                                  # N per m along the span
    S = b * h**2 / 6
    return mass, L, b, h, w, S


def stress(M, S):
    return M * IMPACT / S / 1e6


def best_pick(w, L, S):
    """pick fraction minimizing the larger face stress (no steel credit)"""
    return min((max(lift_moments(w, L, f * L)), f) for f in np.linspace(0.55, 1.0, 91))


def lift_stresses(dims=(8, 4, 6)):
    mass, L, b, h, w, S = panel(*dims)
    M_top = lift_moments(w, L, L)[0]
    M_opt, f_opt = best_pick(w, L, S)
    return dict(mass=mass, top=stress(M_top, S), opt=stress(M_opt, S), f_opt=f_opt)


def breakaway(dims=(8, 4, 6), f=0.71):
    """first instant of the lift: self-weight + suction, no impact factor (tilt-up practice
    checks breakaway and dynamic lift separately; the larger governs)"""
    mass, L, b, h, w, S = panel(*dims)
    out = []
    for q in SUCTION_KPA:
        w_s = w + q * 1e3 * b
        out.append(max(lift_moments(w_s, L, f * L)) / S / 1e6)
    return out


def steel(dims=(8, 4, 6), f=0.71, depth="buried"):
    """returns demand, capacity per earth strength, bond demand"""
    mass, L, b, h, w, S = panel(*dims)
    As = BARS * dims[1] / 4 * BAR4_AREA
    if depth == "buried":
        d = h - COVER - BAR4_DIA / 2
        perim = np.pi * BAR4_DIA
    else:                                             # surface grid: half-embedded in the bed face
        d = h - BAR4_DIA / 2
        perim = np.pi * BAR4_DIA / 2
    Md = max(lift_moments(w, L, f * L)) * IMPACT
    caps = [flexural_capacity(As, d, b, fc * 1e6) for fc in F_C]
    z = min(c[3] for c in caps)                       # smallest lever arm -> largest bar force
    T = Md / z
    bond = T / (BARS * dims[1] / 4) / (perim * 0.6)   # over 0.6 m of bar
    return dict(Md=Md, caps=caps, bond=bond / 1e6, d=d)


def opening_stress(dims=(8, 4, 6), opening_w_ft=2.0, f=0.71):
    """rough: the whole-panel lift moment carried by the solid strips beside the opening.
    Ignores the weight removed and the corner stress concentration (which is worse)."""
    s = lift_stresses(dims)["opt"]
    return s * dims[1] / (dims[1] - opening_w_ft)


def hoist(dims=(8, 4, 6), f=0.71):
    """vertical hoist line during a tilt about the base: F = W * (L/2) / a, any angle"""
    mass = panel(*dims)[0]
    static = mass / (2 * f)
    return static, static * IMPACT


def setting(dims=(8, 4, 6), inserts=2):
    """after the tilt the panel hangs vertical from top-edge inserts to be set on the plinth:
    the hoist takes the full weight; the earth hangs on the vertical grid bars by bond"""
    mass, L, b, h, w, S = panel(*dims)
    dyn = mass * IMPACT
    vbars = BARS * dims[1] / 4
    bond = mass * G * IMPACT / (vbars * np.pi * BAR4_DIA * L) / 1e6
    return mass, dyn, dyn / inserts, bond


def wind_braced(dims=(8, 4, 6), brace_frac=2 / 3, v_ms=(40, 50), cp=1.2):
    """panel standing on its base (pinned), one brace line at brace_frac of height.
    q = 0.613 V^2 (Pa). Wind speeds [TO-VERIFY: ASCE 7 / ASCE 37 for the site and season]."""
    mass, L, b, h, w_self, S = panel(*dims)
    out = []
    for v in v_ms:
        q = 0.613 * v**2 * cp
        w = q * b
        a = brace_frac * L
        sag, hog = lift_moments(w, L, a)
        brace_h = w * L * L / 2 / a                   # horizontal reaction at the brace line
        out.append(dict(v=v, q=q, stress=max(sag, hog) / S / 1e6,
                        brace_axial_45=brace_h * 2**0.5, brace_h=brace_h))
    return out


if __name__ == "__main__":
    print("=" * 70)
    print("TILT-UP CHECK: earth panel cast flat, tilted about its base")
    print(f"moist density at lift {RHO_LIFT:.0f} kg/m^3, x{IMPACT} impact factor")
    print("=" * 70)
    for dims in [(8, 4, 6), (8, 4, 8), (8, 16, 6)]:
        r = lift_stresses(dims)
        print(f"\n{dims[0]}x{dims[1]} ft x {dims[2]} in panel: {r['mass']:,.0f} kg")
        print(f"  lift stress, pick at top edge:          {r['top']:.2f} MPa")
        print(f"  lift stress, pick at {r['f_opt']:.2f} of height:     {r['opt']:.2f} MPa")
        print(f"  -> required modulus of rupture at lift age (x{MOR_SAFETY}): >= {r['opt']*MOR_SAFETY:.2f} MPa"
              f"   (stabilized earth: {MOR[0]}-{MOR[1]} MPa [TO-MEASURE])")

    b_lo, b_hi = breakaway()
    print(f"\nBREAKAWAY (8x4x6, pick 0.71, suction {SUCTION_KPA[0]}-{SUCTION_KPA[1]} kPa, no impact):"
          f" {b_lo:.2f}-{b_hi:.2f} MPa")
    print("  vs the dynamic lift above: suction can govern. Break the bed first -- sand bond breaker,")
    print("  free the pit edges, jack or rock one edge -- before the hoist takes the panel.")

    s = steel()
    print(f"\nSTEEL (4 x #4 per 4 ft, {COVER/IN:.0f} in cover, d = {s['d']*1000:.0f} mm), lift demand {s['Md']/1e3:.2f} kN*m:")
    for fc, (Mn, c, fs, z) in zip(F_C, s["caps"]):
        state = "steel yields" if fs >= 420e6 else f"EARTH CRUSHES FIRST (steel at {fs/1e6:.0f} MPa)"
        print(f"  earth f'c {fc:.1f} MPa: capacity {Mn/1e3:.1f} kN*m -> {Mn/s['Md']:.1f}x margin  [{state}]")
    print(f"  bond the earth must supply if the panel cracks: ~{s['bond']:.2f} MPa per bar over 0.6 m"
          " [TO-MEASURE: pull-out]")

    print("\nOPENINGS (whole-panel moment through the strips beside the opening, corners ignored):")
    for ow in (1.0, 2.0, 3.0):
        print(f"  {ow:.0f} ft opening in a 4 ft panel: ~{opening_stress(opening_w_ft=ow):.2f} MPa")
    print("  -> don't cut openings into 4 ft panels: make doors/windows the GAP between panels,")
    print("     spanned by a lintel panel or the bond beam (see making-system/TILTUP_DETAILING.md).")

    st, dyn = hoist()
    print(f"\nHOIST (8x4x6, pick 0.71): {st:.0f} kg static on the line, {dyn:.0f} kg with impact;"
          f" per insert (2 per panel): {dyn/2:.0f} kg")
    st16, dyn16 = hoist((8, 16, 6))
    print(f"  8x16 ft panel: {dyn16/1000:.1f} t with impact -> beyond a simple A-frame; start with 8x4")
    m, sdyn, per, hb = setting()
    print(f"SETTING on the plinth (hanging vertical from 2 top-edge inserts): {m:.0f} kg static,"
          f" {sdyn:,.0f} kg with impact, {per:.0f} kg per insert")
    print(f"  the earth hangs on the vertical bars by bond: ~{hb:.3f} MPa -> trivial; the welded")
    print(f"  perimeter frame carries the bottom edge. Size the hoist for SETTING, not the tilt.")
    print(f"  hoist line travel during the tilt: the pick moves {0.71*PANEL_H/FT:.1f} ft toward the base -> use a")
    print(f"  trolley beam or rolling gantry so the line stays vertical.")

    print("\nWIND ON A BRACED PANEL (8x4x6, brace at 2/3 height, Cp 1.2):")
    for r in wind_braced():
        print(f"  {r['v']} m/s ({r['v']*2.237:.0f} mph): {r['q']/1e3:.2f} kPa, panel stress {r['stress']:.2f} MPa,"
              f" brace force {r['brace_axial_45']/1e3:.1f} kN at 45 deg")

    mass, L, b, h, w, S = panel()
    cure = mass / 1.1 * 900 * 50 / 3.6e6
    print(f"\nOPTIONAL grid cure heat (20->70 C): {cure:.0f} kWh ideal, ~{2*cure:.0f}-{4*cure:.0f} kWh"
          " with ground losses, per 4x8 panel")
    print("\nVERDICT: pick near 0.7 of height; the steel carries the lift with margin even when the")
    print("earth crushes first. Open questions: modulus of rupture at lift age, bed suction, bond.")

    # -----------------------------------------------------------------------
    # SURFACE GRID: steel laid on the pit floor, half-embedded in the panel's bottom face.
    # -----------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("SURFACE GRID (steel on the pit floor = bottom face), 8x4 ft x 6 in")
    print("=" * 70)
    print(f"{'pick at':>8} {'bottom face (steel)':>20} {'top face (earth only)':>22}")
    for frac in (1.00, 0.95, 0.90, 0.85, 0.80, 0.71):
        sag, hog = lift_moments(w, L, frac * L)
        print(f"{frac:>8.2f} {stress(sag, S):>17.2f} MPa {stress(hog, S):>19.2f} MPa")
    s = steel(f=0.90, depth="surface")
    margins = [c[0] / s["Md"] for c in s["caps"]]
    print(f"\npick at 0.90: steel carries {margins[0]:.1f}-{margins[1]:.1f}x the {s['Md']/1e3:.2f} kN*m demand"
          f" (earth f'c {F_C[0]}-{F_C[1]} MPa)")
    print(f"bond on a half-buried bar: ~{s['bond']:.2f} MPa over 0.6 m -> add anchor legs; don't rely on grip alone")
    print("the steel face WILL likely crack in the lift (stress above most MOR values) -- the steel")
    print("carries it; expect hairline cracks on that face and plaster over them.")
