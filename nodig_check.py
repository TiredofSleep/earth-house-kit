#!/usr/bin/env python3
"""
nodig_check.py -- first-order numbers for treating a panel IN PLACE (no excavation).
Run: python3 nodig_check.py
Route B = electrokinetics: steel driven into the clay is used as electrodes; low-voltage DC
(straight from solar panels) pulls water out (electro-osmosis), pulls stabilizing ions in
(electromigration), and warms the soil (Joule heating). All values [TO-MEASURE] in a bench box.
"""
import numpy as np

V_PANEL = 1.22 * 2.44 * 0.152          # 8x4 ft x 6 in treated zone, m^3
F, R, T = 96485, 8.314, 298
D_CA = 7.9e-10                          # Ca2+ diffusion in water, m^2/s
TORT = (0.1, 0.4)                       # tortuosity factor in clay
K_EO = 5e-9                             # electro-osmotic permeability, m^2/(V s), typical for clays
SIGMA = (0.02, 0.2)                     # bulk conductivity of moist clay + dosing solution, S/m
E = (50, 100)                           # field, V/m (0.5-1 V/cm)
SPACING = 0.30                          # anode row to cathode row, m
HEAT_CAP = 2.5e6                        # J/(m^3 K), moist clay

print("=" * 66)
print("NO-DIG ROUTE B: electrokinetic treatment of one 8x4 ft x 6 in panel")
print("=" * 66)
print(f"treated volume {V_PANEL:.2f} m^3; electrode rows {SPACING*100:.0f} cm apart")
print(f"voltage across the rows: {E[0]*SPACING:.0f}-{E[1]*SPACING:.0f} V DC  "
      "-> a small solar string, no inverter")
for e in E:
    u_ca = [D_CA * t * 2 * F / (R * T) for t in TORT]          # ionic mobility of Ca2+
    days_ion = [SPACING / (u * e) / 86400 for u in u_ca]
    v_eo = K_EO * e
    print(f"\nat {e/100:.1f} V/cm:")
    print(f"  calcium travels the {SPACING*100:.0f} cm in ~{min(days_ion):.0f}-{max(days_ion):.0f} days (one pass)")
    print(f"  water moves toward the cathode at ~{v_eo*86400*100:.1f} cm/day (electro-osmotic dewatering)")
    p = [s * e**2 for s in SIGMA]
    print(f"  power {p[0]*V_PANEL:.0f}-{p[1]*V_PANEL:.0f} W per panel; Joule heating "
          f"+{p[0]/HEAT_CAP*86400:.0f} to +{p[1]/HEAT_CAP*86400:.0f} C/day before losses")
# energy for ~3 passes of reagent at 0.5 V/cm, both conductivity bounds
e = E[0]
u_ca = [D_CA * t * 2 * F / (R * T) for t in TORT]
t_lo = SPACING / (max(u_ca) * e) * 3
t_hi = SPACING / (min(u_ca) * e) * 3
en_lo = SIGMA[0] * e**2 * V_PANEL * t_lo / 3.6e6
en_hi = SIGMA[1] * e**2 * V_PANEL * t_hi / 3.6e6
print(f"\n3 reagent passes at 0.5 V/cm: {t_lo/86400:.0f}-{t_hi/86400:.0f} days, ~{en_lo:.0f}-{en_hi:.0f} kWh per panel")
print("  (current rises as ions enter; dry zones near electrodes self-limit it)")

# ---- tilt with the steel on TOP (grid pressed into the treated surface) ----
RHO, G, IMP = 1900, 9.81, 1.5
L, b, h = 2.44, 1.22, 0.152
w = RHO * L * b * h * G / L
S = b * h**2 / 6
def sag_hog(a):
    x = np.linspace(0, L, 4001)
    R0 = w * (a**2 - (L - a)**2) / (2 * a)
    M = np.where(x <= a, R0 * x - w * x**2 / 2, -w * (L - x)**2 / 2)
    return M.max() * IMP / S / 1e6, -M.min() * IMP / S / 1e6
print("\nTILT with the grid on the TOP face (earth-only face is now the bottom):")
print(f"{'pick at':>8} {'bottom (earth only)':>20} {'top (steel face)':>18}")
for frac in (0.71, 0.65, 0.60, 0.55):
    s_, h_ = sag_hog(frac * L)
    print(f"{frac:>8.2f} {s_:>17.2f} MPa {h_:>15.2f} MPa")
print("-> with steel on top, lift LOW (~0.6 of height) so the bare face stays unstressed")
# bars driven horizontally at mid-depth from edge trenches
Mn = 4 * 129e-6 * 420e6 * 0.9 * (h / 2)
print(f"\nbars driven in at mid-depth (from edge trenches): carry {Mn/1e3:.1f} kN*m "
      f"vs ~1.3-3 kN*m lift demand -> enough, in either direction")
