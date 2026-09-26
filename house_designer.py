#!/usr/bin/env python3
"""
house_designer.py -- design a house from a kit of interlocking fired parts; get the parts list.
Run: python3 house_designer.py                      (every design in houses/)
     python3 house_designer.py houses/ring20_dome.json

A house is DATA (houses/*.json): plan polygon, wall unit, openings, roof. The kit is DATA too:
unit types (data/kit_units.json) and joints (data/joints.json). This script turns a design into:
  - every part by type and count, and whether a DIE extrudes it or a PRINTER makes it
  - rods, channels, keys and wedges
  - fired clay, husks, kiln firings, printer nozzle-hours, die machine-hours
  - the structural checks (panel clamp, dome thrust and ring) for THIS design
A new house is a new JSON file, never a code change (the same rule as sites/ and site_profile.py).
"""
import glob, json, os, sys
from math import ceil, pi, radians
from common import FT, IN, G, PANEL_H
from form_check import polygon
import brick_panel_check as bp
import dome_check as dc
import dome_thrust as dt

HERE = os.path.dirname(os.path.abspath(__file__))
MODULE = 4 * FT
UNIT_L, UNIT_W = bp.UNIT_L, bp.UNIT_W            # 295 x 193 mm in the wall plane
COLS = 6                                          # unit columns per 4 ft module


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


KIT = load(os.path.join(HERE, "data", "kit_units.json"))
JOINTS = load(os.path.join(HERE, "data", "joints.json"))


def rows_for(height_m):
    return max(1, round((height_m + bp.JOINT) / (UNIT_L + bp.JOINT)))


class Parts:
    def __init__(self):
        self.units, self.other = {}, {}

    def add(self, kind, n):
        if n:
            self.units[kind] = self.units.get(kind, 0) + n

    def add_other(self, kind, n, unit=""):
        if n:
            k = (kind, unit)
            self.other[k] = self.other.get(k, 0) + n


def wall_panel(parts, rows, wall_unit, label):
    """one module-wide panel of `rows` units: 2 rod columns, 2 edge columns, 2 plain columns"""
    n = rows * COLS
    parts.add(f"{wall_unit}.rod_end", 4)                         # top+bottom of the 2 rod columns
    seats = min(3, rows)                                         # fold-joint key seats per edge
    parts.add(f"{wall_unit}.key_seat", 2 * seats)
    parts.add(f"{wall_unit}.edge", 2 * rows - 2 * seats)         # the rest of both edge columns: edge die
    parts.add(f"{wall_unit}.insert", 2 if rows >= 6 else 0)      # tilting inserts on full-height panels
    universal = n - 4 - 2 * rows - (2 if rows >= 6 else 0)
    parts.add(f"{wall_unit}.universal", universal)
    parts.add_other("M16 8.8 rod", 2, f"x {rows * (UNIT_L + bp.JOINT):.2f} m")
    parts.add_other("steel end channel (C100)", 2, f"x {MODULE:.2f} m")
    parts.add_other("disc-spring stack + nut + plate", 4)
    parts.add_other(f"panels: {label}", 1)


def design(spec):
    parts = Parts()
    n = spec["plan"]["modules"]
    wall_unit = spec["wall"]["unit"]
    H = spec["wall"].get("height_ft", 8) * FT
    full_rows = rows_for(H)
    openings = spec.get("openings", [])
    area_ft2, span_ft = polygon(n)
    a = span_ft * FT / 2

    # walls
    n_full = n - len(openings)
    for _ in range(n_full):
        wall_panel(parts, full_rows, wall_unit, "full height")
    for o in openings:
        if o["type"] == "door":
            head = o.get("head_ft", 6.67) * FT
            wall_panel(parts, rows_for(H - head), wall_unit, "door lintel")
            parts.add_other("door frame (timber or steel)", 1)
        else:
            sill, head = o.get("sill_ft", 3) * FT, o.get("head_ft", 6.67) * FT
            wall_panel(parts, rows_for(sill), wall_unit, "window sill")
            wall_panel(parts, rows_for(H - head), wall_unit, "window lintel")
            parts.add_other("window frame", 1)

    # folds: every module joint in the ring is a fold of 360/n degrees
    j = JOINTS["panel_fold"]
    parts.add_other(f"fold joint: {j['name']}", n)
    parts.add_other(f"  {j['key']}", n * j["keys_per_joint"])
    bj = JOINTS["base_slider"]
    parts.add_other(f"base: {bj['name']}", n, "(per panel, 2 stainless dowels each)")

    # ring beam from the panels' top channels, spliced at every fold
    rj = JOINTS["ring_splice"]
    parts.add_other(f"ring splice: {rj['name']}", n)

    # roof
    roof = spec.get("roof", {})
    checks = {}
    if roof.get("type") == "dome_cap":
        unit = dc.UNITS[roof.get("unit_name", "8 in thermal")]
        r = dc.dome(a, roof.get("phi0_deg", 51.8), unit, dc.LIVE_KPA[1])
        courses = ceil(r["courses"])
        per_course_face = 0.295 * dc.COURSE
        voussoirs = ceil(r["area"] / per_course_face)
        oculus = roof.get("oculus_m", 0)
        if oculus:
            voussoirs -= ceil(pi * (oculus / 2) ** 2 / per_course_face)
            parts.add("dome.oculus_ring", ceil(pi * oculus / 0.193))
            parts.add_other("oculus cap / skylight", 1)
        parts.add(f"dome.voussoir {roof.get('unit_name', '8 in thermal')}", voussoirs)
        parts.add("dome.eave (corbelled drip course)", ceil(n * MODULE / UNIT_W))
        dj = JOINTS["dome_course"]
        parts.add_other(f"dome joint: {dj['name']}", 1, "(every voussoir)")
        parts.add_other(f"  {JOINTS['dome_key_course']['name']}", courses, "(one closing key per course)")
        if roof.get("skin") == "tiled":
            parts.add("dome.scale_tile", ceil(r["area"] / 0.03))          # ~0.03 m2 exposed per tile [TO-MEASURE]
            parts.add_other("cocciopesto render (lime + crushed kiln rejects), 20 mm", round(r["area"] * 0.02, 1), "m3")
        skin_pa = 1.15e3 if roof.get("skin") == "tiled" else dc.SKIN_KPA * 1e3
        A = dt.arch(r["R"], radians(roof.get("phi0_deg", 51.8)), unit["t"], unit["kg_m2"] * G + skin_pa)
        worst = []
        for name, case in dt.CASES:
            res = dt.solve(A, dt.loads(A, case))
            worst.append((res["gsf"], res["slide"] / dt.MU_ALLOW, name))
        checks["uneven"] = worst
        checks["dome"] = r
        checks["dome_courses"] = courses
    checks["panel"] = bp.drystack(bp.THERMAL_UNIT if "8in" in wall_unit else bp.UNITS["printed cellular brick"],
                                  t=(8 if "8in" in wall_unit else 4.5) * IN,
                                  lock=0.25 if "8in" in wall_unit else 0.30)
    return parts, dict(area_ft2=area_ft2, span_m=2 * a, checks=checks)


def summarize(parts):
    by_method = {"die": 0, "print": 0}
    clay_kg = 0.0
    print_l = 0.0
    for kind, count in parts.units.items():
        k = KIT[kind]
        by_method[k["method"]] += count
        clay_kg += count * k["clay_kg"]
        if k["method"] == "print":
            print_l += count * k["clay_kg"] / bp.RHO_FIRED * bp.WET_PER_FIRED * 1000
    die_l = (clay_kg / bp.RHO_FIRED * bp.WET_PER_FIRED * 1000) - print_l
    husks = (clay_kg * bp.FIRE_MJ_PER_KG[0] / bp.HUSK_MJ[1], clay_kg * bp.FIRE_MJ_PER_KG[1] / bp.HUSK_MJ[0])
    firings = (clay_kg / bp.KILN_LOAD_KG[1], clay_kg / bp.KILN_LOAD_KG[0])
    return dict(by_method=by_method, clay_kg=clay_kg, husks=husks, firings=firings,
                nozzle_h=print_l / bp.PRINT_L_H, die_h=(die_l / bp.DIE_L_H[1], die_l / bp.DIE_L_H[0]))


def report(path):
    spec = load(path)
    parts, info = design(spec)
    s = summarize(parts)
    print("=" * 96)
    print(f"{spec['name']}   ({os.path.basename(path)})")
    print(f"{spec['plan']['modules']}-gon, {info['area_ft2']:.0f} ft^2 ({info['area_ft2']*0.0929:.0f} m^2),"
          f" span {info['span_m']:.2f} m; walls: {spec['wall']['unit']}; roof: {spec.get('roof', {}).get('type', 'none')}")
    print("=" * 96)
    print("FIRED UNITS")
    for kind, count in sorted(parts.units.items()):
        k = KIT[kind]
        print(f"  {count:6,d}  {kind:44s} {k['method']:5s}  {k['clay_kg']:.1f} kg  {k['role']}")
    total = sum(parts.units.values())
    print(f"  {total:6,d}  total: {s['by_method']['die']:,} die-extruded, {s['by_method']['print']:,} printed")
    print("\nSTEEL, KEYS, FRAMES")
    for (kind, unit), count in parts.other.items():
        num = f"{count:6,d}" if isinstance(count, int) else f"{count:6.1f}"
        print(f"  {num}  {kind} {unit}")
    print("\nMAKING IT")
    print(f"  fired clay {s['clay_kg']/1e3:.1f} t -> husks {s['husks'][0]/1e3:.2f}-{s['husks'][1]/1e3:.2f} t,"
          f" kiln firings {s['firings'][0]:.0f}-{s['firings'][1]:.0f} (0.5-1 t hood)")
    print(f"  printer: {s['nozzle_h']:,.0f} nozzle-hours (8 nozzles x 20 h/day: {s['nozzle_h']/160:.1f} days);"
          f" die: {s['die_h'][0]:.0f}-{s['die_h'][1]:.0f} machine-hours")
    c = info["checks"]
    p = c["panel"]
    need = max(p["p_lift"], p["p_wind"])
    after = p["p_set"] * (1 - bp.PT_LOSS[1])
    print("\nCHECKS")
    print(f"  wall panel: {p['mass']:.0f} kg; clamp after 35% loss {after/1e3:.1f} kN vs {need/1e3:.1f} kN needed"
          f" -> {'OK' if after >= need else 'FAIL'}")
    if "dome" in c:
        r = c["dome"]
        ring = dc.RING["area"] * dc.RING["fy"]
        print(f"  dome: rise {r['rise']:.2f} m, {c['dome_courses']} courses, shell stress {r['sigma']:.3f} MPa,"
              f" rim thrust {r['H']/1e3:.2f} kN/m, ring tension {r['T']/1e3:.1f} kN"
              f" (channel ring {ring/r['T']:.0f}x) -> OK")
        g_min = min(worst := c["uneven"])
        sl_max = max(w[1] for w in worst)
        verdict = "OK" if g_min[0] >= 1.5 and sl_max <= 1 else ("STANDS, thin margin -> 3-D analysis first" if g_min[0] >= 1 else "FAILS")
        print(f"  uneven loads (half snow, wind 50 m/s, quake 0.3 g; slices only, no hoop help): worst GSF"
              f" {g_min[0]:.2f} ({g_min[2]}), worst sliding {sl_max:.2f} of allowed -> {verdict}")
        gsf_ok = "OK" if r["gsf"] >= dc.GSF_TARGET else f"UNDER {dc.GSF_TARGET}x -> deeper voussoir or smaller plan"
        print(f"  dome thickness: {r['gsf']:.1f}x the minimum for a masonry dome -> {gsf_ok}")
        print(f"  dome dry-build: {r['keyed'][1]*100:.0f}-{r['keyed'][0]*100:.0f}% of the dome has beds too steep for dry friction"
              f" -> '{JOINTS['dome_course']['name']}' holds each voussoir until its course closes")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    paths = sys.argv[1:] or sorted(glob.glob(os.path.join(HERE, "houses", "*.json")))
    for p in paths:
        report(p)
        print()
