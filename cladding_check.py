#!/usr/bin/env python3
"""
cladding_check.py -- sloped, overlapping fired-clay siding boards that hang and lock on each other.
Run: python3 cladding_check.py

A rainscreen, the way tile-hanging and terracotta cladding work:
  wall panel -> vertical rails clamped to the panels' steel end channels (no drilling into clay),
  making a ventilated, drained cavity -> horizontal battens -> extruded fired boards hang on the
  battens by a nib and LOCK into the board below (tongue over groove), each lapping the one below
  with a drip edge, so water runs down and off, never into the wall.
Why it matters: the structural units never get wet again. Durability moves from the structure into
a thin, cheap, replaceable skin -- the same move as the dome's scale tiles.
Checks: weight, the wind-suction lock (the only clay 'hook' in the kit, so its stress must be tiny),
lap vs wind-driven rain, and how much sun the ventilated cavity keeps off the wall.
All board geometry and fixing values [TO-VERIFY] against rainscreen practice (research note).
"""
import sys

# ---------- board (extruded, cored) ----------
BOARD = dict(length=1.20, height=0.200, gauge=0.150, thick=0.022, core_share=0.45)   # m [TO-VERIFY]
RHO_FIRED = 1900                  # boards fired hotter/denser than wall units (severe-weathering grade)
MOR_BOARD = (8.0, 15.0)           # extruded terracotta flexural strength, MPa [TO-VERIFY vs data sheets]
LOCK = dict(thick=0.008, reach=0.010)      # lock lip thickness and lever arm, m
Q_WIND = 0.613 * 50**2            # Pa
CP_SUCTION = (-1.4, -2.0)         # wall field / corner zone local suction [TO-VERIFY ASCE 7 / EN 1991-1-4]
PRESSURE_EQUALIZED = 0.5          # share of suction that an open-jointed, vented rainscreen still sees [TO-VERIFY]
WALL_M2 = {"16-gon": 13 * 1.219 * 2.438, "20-gon": 17 * 1.219 * 2.438}

# ---------- sun on the wall (steady, per m2) ----------
SOLAR = 800.0                     # W/m2 on a sunlit facade, summer afternoon
ALPHA = 0.6                       # absorptance, red fired clay (a light engobe ~0.3) [TO-VERIFY]
H_OUT, H_CAV, H_RAD = 20.0, 4.0, 5.0   # outer film, cavity convection each face, board-wall radiation W/m2K
U_WALL_IN = 0.70                  # conductance from wall outer face to the room (8 in thermal wall, no Rse)


def board_mass():
    b = BOARD
    return b["length"] * b["height"] * b["thick"] * (1 - b["core_share"]) * RHO_FIRED


def lock_stress(cp):
    """suction on one board's exposed face, carried by a continuous lock lip along its length"""
    b = BOARD
    p = Q_WIND * abs(cp)
    load = p * b["length"] * b["gauge"]                    # N per board
    w = load / b["length"]                                  # N per m of lip
    M = w * LOCK["reach"]                                   # N*m per m
    S = 1.0 * LOCK["thick"] ** 2 / 6
    return load, M / S / 1e6


def solar_gain(alpha):
    """heat into the room from the sun on the wall, bare wall vs ventilated rainscreen (cavity air = ambient)"""
    S = alpha * SOLAR
    bare_Tw = S / (H_OUT + U_WALL_IN)
    bare_q = U_WALL_IN * bare_Tw
    # board: S = H_OUT*Tb + H_CAV*Tb + H_RAD*(Tb - Tw);  wall: H_RAD*(Tb - Tw) = H_CAV*Tw + U*Tw
    k = H_RAD / (H_RAD + H_CAV + U_WALL_IN)
    Tb = S / (H_OUT + H_CAV + H_RAD - H_RAD * k)
    Tw = k * Tb
    return bare_q, U_WALL_IN * Tw, bare_Tw, Tw


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    b = BOARD
    mb = board_mass()
    per_m2 = mb / (b["length"] * b["gauge"])
    lap = b["height"] - b["gauge"]
    print("=" * 90)
    print("FIRED-CLAY RAINSCREEN SIDING: hung on battens, locked board to board, lapped to shed water")
    print("=" * 90)
    print(f"board {b['length']*1000:.0f} x {b['height']*1000:.0f} x {b['thick']*1000:.0f} mm, cored {b['core_share']*100:.0f}%:"
          f" {mb:.1f} kg; exposed gauge {b['gauge']*1000:.0f} mm, headlap {lap*1000:.0f} mm -> {per_m2:.0f} kg/m2 of wall")
    print(f"slope of each board's face: it sits on the one below -> tilts out ~{b['thick']/b['gauge']*57.3:.0f} deg,"
          " plus an undercut drip at the bottom edge")
    for name, a in WALL_M2.items():
        n = a / (b["length"] * b["gauge"])
        print(f"  {name}: {a:.0f} m2 of solid wall -> ~{n:,.0f} boards, {n*mb/1000:.1f} t")

    print("\nWIND SUCTION on the lock (the only clay 'hook' in the kit -- allowed only because the stress is tiny)")
    for cp in CP_SUCTION:
        for share, label in ((1.0, "sealed"), (PRESSURE_EQUALIZED, "vented rainscreen")):
            load, s = lock_stress(cp * share)
            print(f"  Cp {cp}, {label:18s}: {load:4.0f} N per board -> lock lip {s:.2f} MPa"
                  f" = {s/MOR_BOARD[0]*100:4.1f}% of board MOR ({MOR_BOARD[0]}-{MOR_BOARD[1]} MPa)")
    print("  -> the lip works at a few % of strength; impact (a thrown stone, a ladder) is the real risk,")
    print("     so boards are cheap, extruded, and replaceable one at a time.")

    print("\nSUN ON THE WALL (summer afternoon, steady state)")
    for alpha, label in ((ALPHA, "red fired clay"), (0.3, "light engobe")):
        bq, cq, bT, cT = solar_gain(alpha)
        print(f"  {label:15s} (alpha {alpha}): bare wall surface +{bT:4.1f} C, {bq:4.1f} W/m2 into the room;"
              f" behind a ventilated rainscreen +{cT:4.1f} C, {cq:4.1f} W/m2 -> {100*(1-cq/bq):.0f}% less")
    bq, cq, _, _ = solar_gain(ALPHA)
    print("  -> the cavity shades the wall and vents the heat; combine with a light outer face for the most.")

    print("\nWATER: every drop that hits the wall runs down the board faces and off the drip edges;")
    print("  the few that pass an open joint drain down the cavity to a weep at the plinth and out.")
    print("  The structural units behind stay dry -> they no longer need severe-weathering grade;")
    print("  the BOARDS and the plinth do.")
