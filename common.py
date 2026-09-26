#!/usr/bin/env python3
"""
common.py -- one home for the geometry, material values and beam helpers the scripts share.
Change a number here and every script (and check_numbers.py) follows. Not meant to be run.
"""
from math import sqrt
import numpy as np

FT, IN = 0.3048, 0.0254
G = 9.81

# ---------- the standard panel and house ----------
PANEL_H, PANEL_W, PANEL_T = 8 * FT, 4 * FT, 6 * IN      # 8 ft tall (tilt span) x 4 ft wide x 6 in
PANEL_M3 = PANEL_H * PANEL_W * PANEL_T
PANELS_PER_HOUSE = 17                                   # 20x20 ft house, 8 ft walls, ~15% openings

# ---------- earth ----------
RHO_DRY = 1800            # compacted stabilized earth, dry density, kg/m^3 [TO-MEASURE]
MOISTURE = 0.10           # compaction water, fraction of dry mass [TO-MEASURE]
RHO_LIFT = RHO_DRY * (1 + MOISTURE)   # still moist at the tilt -> use for lift loads
PANEL_KG = PANEL_M3 * RHO_DRY         # dry solids per panel (binder fractions apply to this)
PANEL_LIFT_KG = PANEL_M3 * RHO_LIFT   # what the hoist actually lifts
WALL_KG = PANEL_KG * PANELS_PER_HOUSE

MOR = (0.3, 1.0)          # modulus of rupture of stabilized earth, MPa [TO-MEASURE, Phase A]
F_C = (1.0, 2.0)          # compressive strength at lift age, MPa [TO-MEASURE]; ~2 MPa = wall grade
MOR_SAFETY = 1.5          # required MOR / computed lift stress (tilt-up practice keeps lift stress
                          # well below cracking) [TO-VERIFY against TCA / ACI 551 guidance]
IMPACT = 1.5              # dynamic factor for lifting (tilt-up practice ~1.2-1.5)
SUCTION_KPA = (0.5, 2.0)  # bed suction/adhesion at breakaway, over the panel face [TO-MEASURE:
                          # a soil pit with a sand bond breaker is unknown territory]

# ---------- steel ----------
BAR4_AREA = 129e-6        # #4 bar, m^2
BAR4_DIA = 0.0127
FY, ES = 420e6, 200e9     # Grade 60
COVER = 2 * IN            # durability rule (MISSION.md section 10): >= 2 in of earth over buried steel

# ---------- crew ----------
CREW_SIZE = 6
CREW_DAYS = {  # working days per house for a crew of CREW_SIZE [TO-MEASURE on House #0]
    "site + footing":                     (3, 5),
    "dig pits + cast 17 panels":          (4, 6),
    "tilt, brace, connect":               (2, 4),
    "bond beam + roof":                   (5, 10),
    "openings, wiring, water, render":    (7, 12),
}
CREW_DAYS_TOTAL = tuple(sum(v[i] for v in CREW_DAYS.values()) for i in (0, 1))
PERSON_DAYS = tuple(CREW_SIZE * d for d in CREW_DAYS_TOTAL)


def lift_moments(w, L, a):
    """Panel tilting about its base edge (x=0), picked at x=a, free to L, uniform load w (N/m).
    Returns (max sagging moment, max hogging moment), N*m. Sagging puts the bottom (bed) face
    in tension; hogging (the overhang past the pick) puts the top face in tension.
    The same beam serves a braced wall under wind: base = hinge, brace at a."""
    x = np.linspace(0, L, 4001)
    R0 = w * (a**2 - (L - a)**2) / (2 * a)
    M = np.where(x <= a, R0 * x - w * x**2 / 2, -w * (L - x)**2 / 2)
    return max(float(M.max()), 0.0) + 0.0, max(float(-M.min()), 0.0) + 0.0   # +0.0 drops -0.0


def flexural_capacity(As, d, b, fc, fy=FY, Es=ES, eps_cu=0.003, beta1=0.85):
    """Nominal moment of a singly reinforced section whose compression zone is EARTH.
    Strain compatibility with the concrete rectangular stress block; earth's stress block and
    crushing strain are [TO-MEASURE]. With weak earth the steel usually does NOT yield -- the
    earth crushes first -- so As*fy*lever overstates capacity.
    Returns (Mn N*m, neutral axis c m, steel stress Pa, lever arm m)."""
    k = 0.85 * fc * b * beta1
    c = As * fy / k
    fs = fy
    if c >= d or Es * eps_cu * (d - c) / c < fy:          # steel does not yield
        T = As * Es * eps_cu
        c = (-T + sqrt(T * T + 4 * k * T * d)) / (2 * k)
        fs = Es * eps_cu * (d - c) / c
    z = d - beta1 * c / 2
    return As * fs * z, c, fs, z
