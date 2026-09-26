#!/usr/bin/env python3
"""
brick_panel_check.py -- tilt-up panels assembled from FIRED clay units, laid flat on a bed,
steel in grouted channels, tilted up. Compares unit shapes: solid hand-molded brick, die-extruded
hollow brick, and 3D-printed cellular / ribbed units (a thin bead of clay, not a glob).
Run: python3 brick_panel_check.py          Detailing: making-system/BRICK_PANEL.md

The idea: the KILN sets the unit size (small, portable, fires fast); the HOIST sets the panel
size. Units line up their cells into continuous channels along the panel height; bars go in
those channels and are grouted (like reinforced hollow-unit masonry); the other cells take
rice husk for insulation. Steel never goes inside fired clay. Precedent: prefabricated brick
panels, storey height, some prestressed (BIA Technical Note 40).
Unit and masonry properties are [TO-MEASURE] on fired test units (Phase A test kiln).
"""
import sys
from common import (IN, FT, G, IMPACT, MOR_SAFETY, PANEL_H, PANEL_W, PANELS_PER_HOUSE, BAR4_AREA,
                    lift_moments, flexural_capacity)

T = 4.5 * IN                       # panel thickness: one unit on its side
RHO_FIRED = 1800                   # fired clay body, kg/m^3 [TO-MEASURE]
RHO_GROUT = 2000                   # grout (lime-pozzolan, cement or geopolymer)
GROUT_BINDER = (0.20, 0.25)        # binder share of grout mass [TO-VERIFY per mix]
RHO_HUSK = 120                     # packed rice husk, lime-capped
FC_CLAY = (20, 40)                 # fired clay material strength, MPa: US molded brick units
                                   # average 36.5 MPa, hollow 46.4 (BIA TN 3A); conservative here
EFF = 0.5                          # gross masonry strength / (material x solid share) [TO-VERIFY]
MOR_JOINT = (0.35, 2.3)            # masonry flexural strength across joints, MPa (BIA TN 3A)
JOINT_SHARE = 0.06                 # grout in the joints between units, share of gross volume
CHANNEL = 0.060                    # square bar channel formed by aligned cells, m
BARS = 2                           # #4 bars per 4 ft panel, centred in the thickness
WIND_PA = 0.613 * 50**2 * 1.2      # 50 m/s, Cp 1.2
HUSK_MJ = (13.0, 16.0)
FIRE_MJ_PER_KG = (1.1, 3.0)        # zigzag kiln 1.1 .. clamp average 3.0 MJ/kg fired brick
                                   # (PMC11800390); a fibre-hood periodic kiln sits between [TO-MEASURE]
KILN_LOAD_KG = (500, 1000)         # fired units per firing, portable fibre hood ~1-2 m^3 [TO-VERIFY]
FIRE_CYCLE_H = (24, 48)            # heat 10-40 h + cool 5-24 h per periodic firing (BIA TN 9)
WALL_M2 = PANEL_H * PANEL_W * PANELS_PER_HOUSE

# the universal unit: laid flat, cells run along the panel height (m)
UNIT_L, UNIT_W, JOINT = 0.295, 0.193, 0.010      # 8 per column x 6 columns = one 8x4 ft panel

# unit shapes: share of the envelope that is fired clay; thinnest clay dimension (drying/firing)
UNITS = {
    "solid brick, hand-molded":   dict(solid=1.00, web_mm=65, method="hand mold"),
    "hollow brick, die-extruded": dict(solid=0.55, web_mm=12, method="pug mill + die"),
    "printed cellular brick":     dict(solid=0.40, web_mm=8,  method="clay printer"),
    "printed ribbed lattice":     dict(solid=0.30, web_mm=6,  method="clay printer"),
}
SOLID_DRY_DAYS = (7, 14)           # air-drying a solid 65 mm brick without cracking [TO-VERIFY];
                                   # heated industrial dryers: 24-48 h (BIA TN 9)

# forming throughput, wet litres per hour [UNSOURCED -> TO-MEASURE]
BEAD = dict(w_mm=8, h_mm=4, mm_s=60)                   # one printer nozzle
PRINT_L_H = BEAD["w_mm"] * BEAD["h_mm"] * BEAD["mm_s"] * 3600 / 1e6
DIE_L_H = (250, 1000)              # small de-airing pug mill with a cellular die
HAND_L_H = (100, 150)              # one hand-molder
WET_PER_FIRED = 1.25               # drying 2-4% + firing 2.5-4% linear shrinkage (BIA TN 9) + margin


def panel(unit, t=T, L=PANEL_H, b=PANEL_W):
    gross = L * b * t
    chan = BARS * CHANNEL**2 * L
    joints = JOINT_SHARE * gross
    clay = (gross - chan - joints) * unit["solid"]
    cells = gross - chan - joints - clay
    m = dict(clay=clay * RHO_FIRED, grout=(chan + joints) * RHO_GROUT, husk=cells * RHO_HUSK)
    m["total"] = sum(m.values())
    m["clay_m3"] = clay
    return m


def structure(unit, m, t=T, L=PANEL_H, b=PANEL_W):
    w = m["total"] * G / L
    M_lift = max(lift_moments(w, L, 0.71 * L)) * IMPACT
    M_wind = WIND_PA * b * L**2 / 8
    fm = [f * unit["solid"] * EFF for f in FC_CLAY]
    As = BARS * BAR4_AREA
    caps = [flexural_capacity(As, t / 2, b, f * 1e6)[0] for f in fm]
    sigma_gross = M_lift / (b * t**2 / 6) / 1e6            # if it acted as a solid slab
    return dict(fm=fm, M_lift=M_lift, M_wind=M_wind, caps=caps, sigma_gross=sigma_gross)


def house(unit):
    m = panel(unit)
    clay_m3 = m["clay_m3"] * PANELS_PER_HOUSE
    clay_kg = m["clay"] * PANELS_PER_HOUSE
    fuel_gj = (clay_kg * FIRE_MJ_PER_KG[0] / 1e3, clay_kg * FIRE_MJ_PER_KG[1] / 1e3)
    husks = (fuel_gj[0] * 1e3 / HUSK_MJ[1], fuel_gj[1] * 1e3 / HUSK_MJ[0])
    grout_kg = m["grout"] * PANELS_PER_HOUSE
    return dict(clay_kg=clay_kg, fuel_gj=fuel_gj, husks=husks, wet_l=clay_m3 * WET_PER_FIRED * 1000,
                grout_kg=grout_kg, binder_kg=(grout_kg * GROUT_BINDER[0], grout_kg * GROUT_BINDER[1]),
                firings=(clay_kg / KILN_LOAD_KG[1], clay_kg / KILN_LOAD_KG[0]))


FACE_SHELL = 0.016                 # printed outer shell: two 8 mm beads [design choice]
RODS = 2                           # threaded rods through the two bar channels
ROD = dict(name="M16 grade 8.8 galvanized", area=157e-6, fy=640e6, lock=0.3, kg_m=1.58)
WIND_SERVICE_PA = 0.613 * 40**2 * 1.2  # joints stay CLOSED up to 40 m/s; at 50 m/s they may open
                                       # and the rods act as tension steel (usual PT-masonry approach)
END_CHANNEL_KG_M = 8.0             # steel channel top and bottom: anchorage, lift lugs, connections
PT_LOSS = (0.20, 0.35)             # total prestress loss: brickwork >=20%, CMU ~35%; dry-joint SEATING
                                   # dominates, not creep (CMHA TEK 14-20A; research note) [TO-MEASURE]
INSERT_FACTOR = 4                  # lifting devices >= 4x panel dead weight (BIA TN 40)
THERMAL_UNIT = dict(solid=0.32, web_mm=6, method="clay printer")   # 8 in, 6 staggered rows (thermal_check.py)


def drystack(unit, t=T, L=PANEL_H, b=PANEL_W, lock=None):
    """no joint or channel grout; face-shell section; required prestress to keep joints closed"""
    gross = L * b * t
    chan = RODS * CHANNEL**2 * L
    clay = (gross - chan) * unit["solid"]
    husk = (gross - chan - clay) * RHO_HUSK
    steel = RODS * ROD["kg_m"] * L + 2 * END_CHANNEL_KG_M * b
    mass = clay * RHO_FIRED + husk + steel
    A_net = b * t * unit["solid"]                                   # clay bearing area
    I = 2 * (b * FACE_SHELL**3 / 12 + b * FACE_SHELL * ((t - FACE_SHELL) / 2) ** 2)
    S = I / (t / 2)
    M_lift = max(lift_moments(mass * G / L, L, 0.71 * L)) * IMPACT
    M_wind = WIND_PA * b * L**2 / 8
    M_service = WIND_SERVICE_PA * b * L**2 / 8
    p_lift = MOR_SAFETY * M_lift / S * A_net                        # P/A >= SF * M/S
    p_wind = M_service / S * A_net                                  # decompression at service wind
    p_set = RODS * ROD["area"] * ROD["fy"] * (lock or ROD["lock"])
    fm_lo = FC_CLAY[0] * unit["solid"] * EFF
    cap_open = flexural_capacity(RODS * ROD["area"], t / 2, b, fm_lo * 1e6, fy=ROD["fy"])[0]
    return dict(mass=mass, clay=clay * RHO_FIRED, husk=husk, steel=steel, p_lift=p_lift, p_wind=p_wind,
                s_lift=p_lift / A_net / 1e6, s_wind=p_wind / A_net / 1e6, p_set=p_set,
                s_set=p_set / A_net / 1e6, fm_lo=fm_lo, cap_open=cap_open, M_lift=M_lift, M_wind=M_wind)


def units_per_panel():
    cols = round((PANEL_W + JOINT) / (UNIT_W + JOINT))
    rows = round((PANEL_H + JOINT) / (UNIT_L + JOINT))
    return cols, rows


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 100)
    print(f"FIRED-UNIT TILT-UP PANEL: 8x4 ft x {T/IN:.1f} in, units laid flat, {BARS} #4 bars in grouted channels")
    print("=" * 100)
    print(f"{'unit':28s} {'panel':>6} {'clay':>5} {'f`m':>7} {'lift':>6} {'wind':>6} {'slab':>6}"
          f" {'fired clay':>10} {'husks':>8} {'firings':>8} {'air dry':>8}")
    print(f"{'':28s} {'kg':>6} {'kg':>5} {'MPa':>7} {'margin':>6} {'margin':>6} {'MPa':>6}"
          f" {'t/house':>10} {'t/house':>8} {'/house':>8} {'':>8}")
    for name, u in UNITS.items():
        m = panel(u); s = structure(u, m); h = house(u)
        lm = min(c / s["M_lift"] for c in s["caps"])
        wm = min(c / s["M_wind"] for c in s["caps"])
        dry = [d * (u["web_mm"] / 65) ** 2 for d in SOLID_DRY_DAYS]
        dry_s = f"{dry[0]:.0f}-{dry[1]:.0f} d" if dry[1] >= 2 else f"{dry[0]*24:.0f}-{dry[1]*24:.0f} h"
        print(f"{name:28s} {m['total']:6.0f} {m['clay']:5.0f} {s['fm'][0]:3.0f}-{s['fm'][1]:<3.0f} "
              f"{lm:5.1f}x {wm:5.1f}x {s['sigma_gross']:6.2f} {h['clay_kg']/1e3:10.1f} "
              f"{h['husks'][0]/1e3:3.1f}-{h['husks'][1]/1e3:<3.1f} {h['firings'][0]:3.0f}-{h['firings'][1]:<3.0f}  {dry_s:>8}")
    print(f"\nreference: compacted earth panel 8x4x6 in ~897 kg (tiltup_check.py)")
    print("margins = steel + masonry capacity (earth-limited f'm, low end) over the lift (x1.5 impact)"
          " and over 50 m/s wind")
    print(f"slab = lift stress if the panel acted solid; the cellular face shells see roughly twice that."
          f" Joints crack at {MOR_JOINT[0]}-{MOR_JOINT[1]} MPa")
    print("  (BIA TN 3A) -> expect hairline joint cracks on some panels; the grouted bars carry the lift.")
    print(f"air-dry time scales with (thinnest clay dimension)^2 from {SOLID_DRY_DAYS[0]}-{SOLID_DRY_DAYS[1]} days"
          " for a 65 mm solid brick [TO-MEASURE]")

    u = UNITS["printed cellular brick"]
    cols, rows = units_per_panel()
    env = UNIT_L * UNIT_W * T
    unit_kg = env * u["solid"] * RHO_FIRED
    h = house(u)
    print("\n" + "-" * 100)
    print("THE PRINTED CELLULAR PANEL, per house")
    print(f"  universal unit {UNIT_L*1000:.0f} x {UNIT_W*1000:.0f} x {T*1000:.0f} mm, ~{unit_kg:.1f} kg fired;"
          f" {cols} columns x {rows} units = {cols*rows} per panel, {cols*rows*PANELS_PER_HOUSE} per house"
          " (+ special units)")
    print(f"  fired clay {h['clay_kg']/1e3:.1f} t -> {h['fuel_gj'][0]:.1f}-{h['fuel_gj'][1]:.1f} GJ ->"
          f" {h['husks'][0]/1e3:.2f}-{h['husks'][1]/1e3:.2f} t of husks")
    print(f"  kiln: {h['firings'][0]:.0f}-{h['firings'][1]:.0f} firings of {KILN_LOAD_KG[0]}-{KILN_LOAD_KG[1]} kg,"
          f" {FIRE_CYCLE_H[0]}-{FIRE_CYCLE_H[1]} h each -> one hood: {h['firings'][0]*FIRE_CYCLE_H[0]/24:.0f}-"
          f"{h['firings'][1]*FIRE_CYCLE_H[1]/24:.0f} days; two hoods halve it")
    print(f"  grout {h['grout_kg']/1e3:.1f} t, of which binder {h['binder_kg'][0]:.0f}-{h['binder_kg'][1]:.0f} kg"
          " -- the only thing bought besides steel")
    print("  (vs 830-1,110 kg of cement to stabilize a compacted-earth house: costs_estimate.py)")

    print("\n" + "-" * 100)
    print("FORMING THROUGHPUT for one house of units (wet clay volume)")
    for name, u in UNITS.items():
        h = house(u)
        L = h["wet_l"]
        if u["method"] == "clay printer":
            nh = L / PRINT_L_H
            print(f"  {name:28s} {L:6,.0f} L wet: {nh:5,.0f} nozzle-hours "
                  f"({BEAD['w_mm']}x{BEAD['h_mm']} mm bead at {BEAD['mm_s']} mm/s = {PRINT_L_H:.1f} L/h)"
                  f" -> 8 nozzles, 20 h/day: {nh/8/20:.1f} days")
        elif u["method"] == "pug mill + die":
            print(f"  {name:28s} {L:6,.0f} L wet: {L/DIE_L_H[1]:.0f}-{L/DIE_L_H[0]:.0f} machine-hours (one extruder)")
        else:
            print(f"  {name:28s} {L:6,.0f} L wet: {L/HAND_L_H[1]:.0f}-{L/HAND_L_H[0]:.0f} person-hours of molding")
    print("-> the universal unit is a constant section, so a die extrudes it fast; the printer makes")
    print("   the parts a die can't: insert units, grout-fill holes, end keys, corners, sills, lintels.")

    u = UNITS["printed cellular brick"]
    print("\n" + "-" * 100)
    print("PANEL SCALE with printed cellular units (the hoist sets the size, not the kiln)")
    for Lft, bft in [(8, 4), (8, 8), (8, 16), (10, 16)]:
        mm = panel(u, L=Lft * FT, b=bft * FT)
        print(f"  {Lft}x{bft} ft: {mm['total']:6,.0f} kg -> setting load with impact {mm['total']*IMPACT:6,.0f} kg")
    print("  vs 897 kg for ONE 8x4 ft compacted-earth panel: a 2 t hoist sets 8x16 ft cellular panels.")

    # -------------------------------------------------------------------------------------------
    print("\n" + "=" * 100)
    print("DRY-STACK + POST-TENSIONED: precise units, no mortar, no grout, rods clamp the panel")
    print("=" * 100)
    for label, uu, tt, lock in [("4.5 in printed cellular", u, T, 0.30),
                                ("8 in printed thermal (6 staggered rows, husk)", THERMAL_UNIT, 8 * IN, 0.25)]:
        r = drystack(uu, t=tt, lock=lock)
        need = max(r["p_lift"], r["p_wind"])
        after = [r["p_set"] * (1 - l) for l in PT_LOSS]
        print(f"\n  {label}: {r['mass']:.0f} kg per 8x4 ft panel (clay {r['clay']:.0f}, husk {r['husk']:.0f},"
              f" rods + channels {r['steel']:.0f})")
        print(f"    keep joints closed: lift x{MOR_SAFETY} needs {r['p_lift']/1e3:.1f} kN, 40 m/s service wind"
              f" {r['p_wind']/1e3:.1f} kN")
        print(f"    {RODS} x {ROD['name']} locked at {lock*100:.0f}% of yield: {r['p_set']/1e3:.1f} kN"
              f" = {r['s_set']:.2f} MPa on the clay ({r['s_set']/r['fm_lo']*100:.0f}% of low f'm {r['fm_lo']:.1f} MPa)")
        ok = "OK" if after[1] >= need else "RE-TENSION after seating"
        print(f"    after {PT_LOSS[0]*100:.0f}-{PT_LOSS[1]*100:.0f}% losses: {after[1]/1e3:.1f}-{after[0]/1e3:.1f} kN"
              f" vs {need/1e3:.1f} kN needed -> {ok}")
        print(f"    if joints open, rods as tension steel: {r['cap_open']/r['M_lift']:.1f}x the lift,"
              f" {r['cap_open']/r['M_wind']:.1f}x the 50 m/s wind")
        print(f"    lifting inserts rated >= {INSERT_FACTOR} x {r['mass']:.0f} kg = {INSERT_FACTOR*r['mass']:,.0f} kg ultimate")
    print(f"\n  shear across dry joints = friction only (cohesion 0, mu ~0.5-0.6): keys LOCATE units, never carry load")
    print("  zero wet trades -> assemble, tension, tilt the SAME DAY")
    print("  losses: dry joints bed in under load -> Belleville disc-spring stacks under the nuts keep the")
    print("  force, and re-torque at 24 h [TO-MEASURE seating loss on a test panel].")
