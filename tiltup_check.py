#!/usr/bin/env python3
"""
tiltup_check.py -- can a reinforced earth panel cast flat in the ground be tilted up?
Run: python3 tiltup_check.py
Checks the lift-bending stress against (a) earth cracking strength and (b) what the rebar
carries, then the rebar bond the earth must supply. Tilting about the base edge, pick near top.
"""
import numpy as np
RHO, G = 1900, 9.81          # stabilized compacted earth, kg/m^3
IMPACT = 1.5                 # dynamic factor for lifting (tilt-up practice uses ~1.2-1.5)
F_R = (0.3, 1.0)             # modulus of rupture of stabilized earth, MPa [TO-MEASURE]

def max_moment(w, L, a):
    """beam hinged at x=0 (base on ground), picked at x=a, overhang to L. max |M| per width."""
    x = np.linspace(0, L, 4001)
    R0 = w * (a**2 - (L - a)**2) / (2 * a)          # base reaction from statics
    M = np.where(x <= a, R0 * x - w * x**2 / 2, -w * (L - x)**2 / 2)
    return np.max(np.abs(M))

def panel(height_ft, width_ft, thick_in):
    L, b, h = height_ft * 0.3048, width_ft * 0.3048, thick_in * 0.0254
    mass = RHO * L * b * h
    w = mass * G / L                                  # N per m along the span
    S = b * h**2 / 6
    M_top = max_moment(w, L, L)                       # pick at the top edge
    best = min((max_moment(w, L, a), a) for a in np.linspace(0.55 * L, L, 91))
    return mass, L, b, h, S, M_top, best

if __name__ == "__main__":
    print("=" * 66)
    print("TILT-UP CHECK: earth panel cast flat, tilted about its base")
    print("=" * 66)
    for dims in [(8, 4, 6), (8, 4, 8), (8, 16, 6)]:
        mass, L, b, h, S, M_top, (M_opt, a_opt) = panel(*dims)
        s_top = M_top * IMPACT / S / 1e6
        s_opt = M_opt * IMPACT / S / 1e6
        print(f"\n{dims[0]}x{dims[1]} ft x {dims[2]} in panel: {mass:,.0f} kg")
        print(f"  lift stress, pick at top edge:        {s_top:.2f} MPa (x{IMPACT} impact)")
        print(f"  lift stress, pick at {a_opt/L:.2f} of height:   {s_opt:.2f} MPa")
        print(f"  earth cracking strength:              {F_R[0]}-{F_R[1]} MPa [TO-MEASURE]")

    # rebar: 4 x #4 bars per 4 ft of width in the tension layer, Grade 60
    mass, L, b, h, S, M_top, (M_opt, a_opt) = panel(8, 4, 6)
    As, fy = 4 * 129e-6, 420e6
    d = h - 0.038 - 0.006
    Mn = As * fy * 0.9 * d
    Md = M_opt * IMPACT
    print("\nREBAR (4 x #4 bars per 4 ft, one tension layer):")
    print(f"  moment the steel carries: {Mn/1e3:.1f} kN*m  vs lift demand {Md/1e3:.2f} kN*m"
          f"  -> {Mn/Md:.0f}x margin")
    T = Md / (0.9 * d)
    bond = T / 4 / (np.pi * 0.0127 * 0.6)
    print(f"  bond the earth must supply: ~{bond/1e6:.2f} MPa per bar over 0.6 m [TO-MEASURE: pull-out test]")

    cure = RHO * L * b * h * 900 * 50 / 3.6e6
    print(f"\nOPTIONAL grid cure heat (20->70 C): {cure:.0f} kWh ideal, ~{2*cure:.0f}-{4*cure:.0f} kWh"
          " with ground losses, per 4x8 panel")
    print("\nVERDICT: the steel carries the lift easily; the open questions are cracking")
    print("(modulus of rupture) and bond (pull-out). Both are cheap Phase A tests.")


# ---------------------------------------------------------------------------
# SURFACE GRID: steel laid on the pit floor, half-embedded in the panel's bottom face.
# During the tilt, the span sags -> bottom face in tension (the steel face).
# Beyond the pick point the panel overhangs -> TOP face in tension, with no steel there.
# ---------------------------------------------------------------------------
def moments(w, L, a):
    x = np.linspace(0, L, 4001)
    R0 = w * (a**2 - (L - a)**2) / (2 * a)
    M = np.where(x <= a, R0 * x - w * x**2 / 2, -w * (L - x)**2 / 2)
    return M.max(), -M.min()            # sagging (bottom tension), hogging (top tension)

if __name__ == "__main__":
    mass, L, b, h, S, _, _ = panel(8, 4, 6)
    w = mass * G / L
    print("\n" + "=" * 66)
    print("SURFACE GRID (steel on the pit floor = bottom face), 8x4 ft x 6 in")
    print("=" * 66)
    print(f"{'pick at':>8} {'bottom face (steel)':>20} {'top face (earth only)':>22}")
    for frac in (1.00, 0.95, 0.90, 0.85, 0.80, 0.71):
        sag, hog = moments(w, L, frac * L)
        print(f"{frac:>8.2f} {sag*IMPACT/S/1e6:>17.2f} MPa {hog*IMPACT/S/1e6:>19.2f} MPa")
    d_s = h - 0.0127 / 2
    sag, _ = moments(w, L, 0.90 * L)
    Md = sag * IMPACT
    Mn = 4 * 129e-6 * 420e6 * 0.9 * d_s
    T = Md / (0.9 * d_s)
    half_perim = np.pi * 0.0127 / 2
    bond = T / 4 / (half_perim * 0.6)
    print(f"\npick at 0.90: steel carries {Mn/1e3:.1f} kN*m vs {Md/1e3:.2f} demand ({Mn/Md:.0f}x)")
    print(f"bond on a half-buried bar: ~{bond/1e6:.2f} MPa over 0.6 m -> add anchor legs; don't rely on grip alone")
    print("VERDICT: lift near the top edge so the earth-only face stays below cracking;")
    print("the steel face takes the stretch. Anchors, not grip, hold the grid long-term.")
