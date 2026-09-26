#!/usr/bin/env python3
"""
thermal_check.py -- how well do printed fired-clay cross-sections keep heat out (and in)?
Run: python3 thermal_check.py

In the finished wall the cells run VERTICALLY (along the panel height), so every web is a little
column carrying gravity load. Heat flows ACROSS the wall, through the cross-section -- so the
pattern of shells, webs and cells decides the insulation. Webs that run straight through the wall
are thermal bridges; staggered or diagonal webs make heat zigzag through thin clay.

1. steady state: 2-D finite-volume conduction through one repeat of each cross-section
   -> equivalent conductivity, R and U of the wall (lime plaster both faces)
2. daily cycle (ISO 13786 transfer matrices): time lag, decrement factor, interior heat capacity
All material values [TO-VERIFY]; the model is first-order (no moisture, 2-D, cells as solids).
"""
import sys
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve

LAM_CLAY, RHO_CLAY, C_CLAY = 0.80, 1800, 900        # fired clay body [TO-VERIFY: 0.6-1.0 W/mK]
LAM_HUSK, RHO_HUSK, C_HUSK = 0.06, 120, 1300        # packed rice husk [TO-VERIFY: 0.05-0.08]
LAM_SAND, RHO_SAND, C_SAND = 0.35, 1500, 800        # dry sand fill for interior mass [TO-VERIFY]
H_RAD = 4.7                                         # radiation across a cell, eps 0.9, ~20 C, W/m2K
PLASTER = [(0.020, 0.70, 1600, 1000), (0.015, 0.70, 1600, 1000)]   # ext, int lime plaster (d, lam, rho, c)
RSE, RSI = 0.04, 0.13
U_TARGET = 0.56                                     # ~IECC zone 3 mass wall U-0.098 IP [TO-VERIFY]


def lam_air_cell(h_mm):
    """still air in a narrow cell: conduction + radiation across its height (no convection < ~20 mm)"""
    return 0.025 + H_RAD * h_mm / 1000


# ---------- cross-sections: boolean clay masks on a 1 mm grid (y = through the wall) ----------
def _grid(t, P):
    y, x = np.mgrid[0:t, 0:P] + 0.5
    return x, y

def solid(t, P=40, **k):
    x, y = _grid(t, P)
    return np.ones_like(x, bool), t

def rows_layout(t, shell, web, n):
    row_h = (t - 2 * shell - (n - 1) * web) / n
    return row_h, [shell + j * (row_h + web) for j in range(n)]

def inline(t, P=60, shell=10, web=8, n=1, **k):
    x, y = _grid(t, P)
    row_h, y0s = rows_layout(t, shell, web, n)
    m = (y < shell) | (y > t - shell)
    for y0 in y0s:
        m |= (y >= y0 + row_h) & (y < y0 + row_h + web) & (y < t - shell)
    m |= (x % P) < web                               # webs straight through every row
    return m, row_h

def staggered(t, P=60, shell=10, web=6, n=4, **k):
    x, y = _grid(t, P)
    row_h, y0s = rows_layout(t, shell, web, n)
    m = (y < shell) | (y > t - shell)
    for j, y0 in enumerate(y0s):
        in_row = (y >= y0) & (y < y0 + row_h)
        m |= in_row & (((x - (j % 2) * P / 2) % P) < web)
        m |= (y >= y0 + row_h) & (y < y0 + row_h + web) & (y < t - shell)
    return m, row_h

def truss(t, P=60, shell=10, web=6, n=1, diamond=False, **k):
    x, y = _grid(t, P)
    row_h, y0s = rows_layout(t, shell, web, n)
    m = (y < shell) | (y > t - shell)
    half = web / 2 / np.cos(np.arctan(row_h / (P / 2)))
    for y0 in y0s:
        in_row = (y >= y0) & (y < y0 + row_h)
        for off in ((0, P / 2) if diamond else (0,)):
            s = ((x - off) % P) / (P / 2)
            yl = y0 + np.where(s <= 1, s, 2 - s) * row_h
            m |= in_row & (np.abs(y - yl) < half)
        m |= (y >= y0 + row_h) & (y < y0 + row_h + web) & (y < t - shell)
    return m, row_h


def lam_eq(mask, lam_cells, kclay=None):
    """2-D steady conduction, 1 mm cells, T=1 on the outer face, 0 on the inner, periodic sides.
    lam_cells: conductivity of non-clay cells (array or scalar). Returns W/mK of the section."""
    ny, nx = mask.shape
    k = np.where(mask, LAM_CLAY if kclay is None else kclay, lam_cells).astype(float)
    idx = np.arange(ny * nx).reshape(ny, nx)
    rows, cols, vals = [], [], []
    b = np.zeros(ny * nx)
    diag = np.zeros(ny * nx)
    def link(a, c, g):
        rows.extend([a, c, a, c]); cols.extend([c, a, a, c]); vals.extend([-g, -g, g, g])
    kE = np.roll(k, -1, axis=1)
    gE = 2 * k * kE / (k + kE)
    link(idx.ravel(), np.roll(idx, -1, axis=1).ravel(), gE.ravel())       # periodic in x
    gS = 2 * k[:-1] * k[1:] / (k[:-1] + k[1:])
    link(idx[:-1].ravel(), idx[1:].ravel(), gS.ravel())
    g_top, g_bot = 2 * k[0], 2 * k[-1]                                   # node to face: k / 0.5
    diag[idx[0]] += g_top; b[idx[0]] += g_top * 1.0
    diag[idx[-1]] += g_bot
    A = coo_matrix((np.concatenate([np.concatenate([np.atleast_1d(v) for v in vals]), diag]),
                    (np.concatenate([np.concatenate([np.atleast_1d(r) for r in rows]), np.arange(ny * nx)]),
                     np.concatenate([np.concatenate([np.atleast_1d(c) for c in cols]), np.arange(ny * nx)]))),
                   shape=(ny * nx, ny * nx)).tocsr()
    T = spsolve(A, b).reshape(ny, nx)
    q = np.sum(g_bot * T[-1])                        # W per m of wall height, per unit temperature
    return q * ny / nx


def layer_matrix(d, lam, rho, c, period=86400.0):
    if d == 0:
        return np.eye(2, dtype=complex)
    delta = np.sqrt(lam * period / (np.pi * rho * c))
    xi = d / delta
    z = xi * (1 + 1j)
    return np.array([[np.cosh(z), -delta / (2 * lam) * (1 - 1j) * np.sinh(z)],
                     [-lam / delta * (1 + 1j) * np.sinh(z), np.cosh(z)]])


def dynamic(layers):
    """ISO 13786. layers: exterior -> interior (d, lam, rho, c). Returns U, lag h, decrement, kappa_i.
    ISO order: side 1 = interior, Z = Z_se . Z_ext ... Z_int . Z_si"""
    Z = np.array([[1, -RSI], [0, 1]], dtype=complex)
    for L in reversed(layers):
        Z = layer_matrix(*L) @ Z
    Z = np.array([[1, -RSE], [0, 1]], dtype=complex) @ Z
    R = RSE + RSI + sum(L[0] / L[1] for L in layers)
    U = 1 / R
    Y12 = -1 / Z[0, 1]
    lag = (-np.angle(Y12) / (2 * np.pi) * 24) % 24
    f = abs(Y12) / U
    kappa = 86400 / (2 * np.pi) * abs((Z[1, 1] - 1) / Z[0, 1])     # interior side, J/m2K
    return U, lag, f, kappa / 1000


def section_layer(fn, t, fill="air", graded=None, **kw):
    """graded = (lam_outer_skin, lam_core_webs, lam_inner_skin): a multi-material print --
    dense fluxed outer skin, porous (pore-former) core webs, dense smooth inner skin"""
    mask, cell_h = fn(t, **kw)
    kclay = None
    if graded:
        shell = kw.get("shell", 10)
        y = np.mgrid[0:mask.shape[0], 0:mask.shape[1]][0] + 0.5
        kclay = np.where(y < shell, graded[0], np.where(y > t - shell, graded[2], graded[1]))
    lam_cells = lam_air_cell(cell_h) if fill == "air" else (LAM_HUSK if fill == "husk" else LAM_SAND)
    rho_f, c_f = {"air": (1.2, 1000), "husk": (RHO_HUSK, C_HUSK), "sand": (RHO_SAND, C_SAND)}[fill]
    solid_share = mask.mean()
    lam = lam_eq(mask, lam_cells, kclay)
    rho = solid_share * RHO_CLAY * (0.75 if graded else 1.0) + (1 - solid_share) * rho_f
    c = (solid_share * RHO_CLAY * C_CLAY + (1 - solid_share) * rho_f * c_f) / rho
    return dict(d=t / 1000, lam=lam, rho=rho, c=c, solid=solid_share, kg_m2=rho * t / 1000)


def wall(core_layers):
    layers = [PLASTER[0]] + [(L["d"], L["lam"], L["rho"], L["c"]) for L in core_layers] + [PLASTER[1]]
    return dynamic(layers)


CASES = [
    # name, list of (section fn, thickness mm, fill, kwargs) exterior -> interior
    ("compacted earth 6 in (baseline)",        [("earth", 152)]),
    ("solid fired brick 7.5 in",              [(solid, 190, "air", {})]),
    ("4.5 in: 1 row, straight webs, air",     [(inline, 114, "air", dict(n=1, web=8, shell=16))]),
    ("4.5 in: 1 row, straight webs, husk",    [(inline, 114, "husk", dict(n=1, web=8, shell=16))]),
    ("4.5 in: 4 rows staggered, air",         [(staggered, 114, "air", dict(n=4))]),
    ("4.5 in: 4 rows staggered, husk",        [(staggered, 114, "husk", dict(n=4))]),
    ("4.5 in: 2-row truss, husk",             [(truss, 114, "husk", dict(n=2))]),
    ("4.5 in: diamond lattice, husk",         [(truss, 114, "husk", dict(n=1, diamond=True))]),
    ("8 in: 6 rows staggered, husk",          [(staggered, 200, "husk", dict(n=6))]),
    ("8 in: 3-row truss, husk",               [(truss, 200, "husk", dict(n=3))]),
    ("8 in: truss husk OUT + staggered sand IN", [(truss, 100, "husk", dict(n=2)),
                                                  (staggered, 100, "sand", dict(n=3))]),
    ("8 in GRADED: dense skins, porous 0.30 core", [(staggered, 200, "husk", dict(n=6, graded=(1.0, 0.30, 0.8)))]),
    ("8 in GRADED: dense skins, porous 0.20 core", [(staggered, 200, "husk", dict(n=6, graded=(1.0, 0.20, 0.8)))]),
    ("6 in GRADED: dense skins, porous 0.20 core", [(staggered, 152, "husk", dict(n=5, graded=(1.0, 0.20, 0.8)))]),
]


def evaluate(parts):
    layers = []
    for p in parts:
        if p[0] == "earth":
            layers.append(dict(d=p[1] / 1000, lam=1.0, rho=1900, c=900, solid=1.0, kg_m2=1.9 * p[1]))
        else:
            fn, t, fill, kw = p
            layers.append(section_layer(fn, t, fill, **kw))
    U, lag, f, kappa = wall(layers)
    d = sum(L["d"] for L in layers)
    lam = d / sum(L["d"] / L["lam"] for L in layers)
    solid_share = sum(L["solid"] * L["d"] for L in layers) / d
    return dict(U=U, lag=lag, f=f, kappa=kappa, lam=lam, d=d, solid=solid_share,
                kg=sum(L["kg_m2"] for L in layers))


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 104)
    print("THERMAL: printed fired-clay cross-sections (2-D conduction + ISO 13786 daily cycle), lime plaster both faces")
    print(f"clay {LAM_CLAY} W/mK, husk {LAM_HUSK}, cells: air {lam_air_cell(10):.3f} at 10 mm (conduction + radiation)")
    print("=" * 104)
    print(f"{'wall':42s} {'clay':>5} {'kg/m2':>6} {'lam_eq':>7} {'U':>6} {'R':>5} {'lag h':>6} {'decr':>5} {'k_int':>6}")
    for name, parts in CASES:
        r = evaluate(parts)
        flag = " <- meets U target" if r["U"] <= U_TARGET else ""
        print(f"{name:42s} {r['solid']*100:4.0f}% {r['kg']:6.0f} {r['lam']:7.3f} {r['U']:6.2f} {1/r['U']:5.2f}"
              f" {r['lag']:6.1f} {r['f']:5.2f} {r['kappa']:6.0f}{flag}")
    print(f"\nU in W/m2K (target ~{U_TARGET} for a mass wall in a hot-humid climate [TO-VERIFY local code]);")
    print("lag = hours before the afternoon peak reaches the room; decr = share of the outdoor swing that")
    print("gets through; k_int = interior heat capacity, kJ/m2K (higher = steadier room).")
    print("-> straight webs are heat highways; staggering and diagonal webs make heat zigzag through thin clay.")
    print("-> husk in the cells beats air; mass on the INSIDE, insulation on the OUTSIDE.")
