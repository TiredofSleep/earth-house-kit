#!/usr/bin/env python3
"""
rock_options.py -- which way of turning site soil into ROCK is quickest, leanest, most portable?
Run: python3 rock_options.py            (the routes are data: data/rock_routes.json)
     python3 rock_options.py fired_panel sulfur_concrete     (just these)

Rock is 5-20x stronger than compacted earth, so the wall can be thinner, lighter, and maybe
steel-free. For each route this sizes the wall from the material's OWN strength:
  - lift: tilted up UNREINFORCED, pick at 0.71, x1.5 impact, x1.5 margin on its modulus of rupture
  - wind: standing, pinned at the plinth and the bond beam, 50 m/s design wind, same margin
  - never thinner than T_MIN (buildability, impact, slenderness) [TO-VERIFY with an engineer]
then reports wall mass, process heat (and the husks to supply it), electricity (and array-days),
what must be bought or shipped, and time from cast to liftable.
Compacted earth is the baseline for comparison, not a candidate.
"""
import json, os, sys
from math import sqrt
from common import IN, G, PANEL_H, PANEL_W, PANELS_PER_HOUSE, IMPACT, MOR_SAFETY, lift_moments

HERE = os.path.dirname(os.path.abspath(__file__))
WALL_M2 = PANEL_H * PANEL_W * PANELS_PER_HOUSE      # 17 panels of 8x4 ft
T_MIN = 3 * IN                                      # thinnest solid rock wall considered [TO-VERIFY]
WIND_PA = 0.613 * 50**2 * 1.2                       # 50 m/s, Cp 1.2 (as tiltup_check.wind_braced)
HUSK_MJ_PER_KG = (13.0, 16.0)                       # 3.6-4.4 kWh/kg (data/materials.json)
ARRAY_KWH_PER_DAY = 60                              # usable midday energy, 20 kW array


def sigma_lift_per_1m(rho):
    """lift stress (Pa) for a 1 m thick panel; stress scales as 1/t"""
    w = rho * G * PANEL_W * 1.0
    M = max(lift_moments(w, PANEL_H, 0.71 * PANEL_H)) * IMPACT
    return M / (PANEL_W * 1.0**2 / 6)


def thickness(route):
    """(chosen t, t_lift, t_wind) in m, from the LOW end of the modulus of rupture"""
    if route.get("t_fixed_in"):
        t = route["t_fixed_in"] * IN
        return t, t, t
    rho, mor = route["rho"][0], route["mor_mpa"][0] * 1e6
    t_lift = 0.0 if route.get("laid_in_place") else sigma_lift_per_1m(rho) * MOR_SAFETY / mor
    M_wind = WIND_PA * PANEL_H**2 / 8                  # per m width, pinned top and bottom
    t_wind = sqrt(6 * M_wind * MOR_SAFETY / mor)
    t = max(T_MIN, route.get("t_min_in", 0) * IN, t_lift, t_wind)
    t = -(-t // (0.5 * IN)) * 0.5 * IN                  # round up to the next 1/2 in
    return t, t_lift, t_wind


def evaluate(key, r):
    t, t_lift, t_wind = thickness(r)
    mass = tuple(WALL_M2 * t * rho for rho in r["rho"])
    heat = tuple(mass[i] * r["heat_mj_per_kg"][i] for i in (0, 1))              # MJ
    husks = (heat[0] / HUSK_MJ_PER_KG[1], heat[1] / HUSK_MJ_PER_KG[0])
    elec = tuple(mass[i] * r["elec_kwh_per_kg"][i] for i in (0, 1))             # kWh
    bought = tuple(mass[i] * sum(v[i] for v in r["bought_frac"].values()) for i in (0, 1))
    panel_kg = PANEL_H * PANEL_W * t * r["rho"][1]
    return dict(key=key, name=r["name"], t=t, t_lift=t_lift, t_wind=t_wind, mass=mass,
                heat=heat, husks=husks, elec=elec, bought=bought, panel_kg=panel_kg,
                hours=r["hours_to_lift"], fc=r["fc_mpa"], mor=r["mor_mpa"], peak=r["peak_c"],
                r=r)


def load():
    with open(os.path.join(HERE, "data", "rock_routes.json"), encoding="utf-8") as fh:
        return json.load(fh)["routes"]


def rng(a, b, fmt="{:,.0f}"):
    return fmt.format(a) if round(a) == round(b) else f"{fmt.format(a)}-{fmt.format(b)}"


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    routes = load()
    keys = sys.argv[1:] or list(routes)
    rows = [evaluate(k, routes[k]) for k in keys]

    print("=" * 100)
    print(f"ROCK FROM SITE SOIL -- one house: {WALL_M2:.1f} m^2 of wall ({PANELS_PER_HOUSE} panels of 8x4 ft)")
    print(f"thickness from the material's own strength: unreinforced lift + {WIND_PA/1e3:.2f} kPa wind,"
          f" x{MOR_SAFETY} margin, >= {T_MIN/IN:.0f} in")
    print("=" * 100)
    print(f"{'route':30s} {'wall':>5} {'8x4 panel':>9} {'wall mass':>11} {'fc MPa':>8} "
          f"{'heat GJ':>8} {'husks t':>8} {'elec kWh':>11} {'bought t':>9} {'cast->lift':>11}")
    for x in rows:
        h = x["hours"]
        when = f"{rng(h[0], h[1])} h" if h[1] <= 48 else f"{rng(h[0]/24, h[1]/24)} d"
        print(f"{x['name'][:30]:30s} {x['t']/IN:4.1f}\" {x['panel_kg']:7,.0f}kg "
              f"{rng(x['mass'][0]/1e3, x['mass'][1]/1e3, '{:.1f}'):>9} t {rng(*x['fc']):>8} "
              f"{rng(x['heat'][0]/1e3, x['heat'][1]/1e3, '{:.1f}'):>8} "
              f"{rng(x['husks'][0]/1e3, x['husks'][1]/1e3, '{:.1f}'):>8} "
              f"{rng(*x['elec']):>11} {rng(x['bought'][0]/1e3, x['bought'][1]/1e3, '{:.1f}'):>9} {when:>11}")

    print("\nper route:")
    for x in rows:
        r = x["r"]
        lim = max(("minimum", T_MIN), ("lift", x["t_lift"]), ("wind", x["t_wind"]), key=lambda p: p[1])[0]
        print(f"\n{x['name']}  [{r['family']}]  -> {r.get('status', '?').upper()}")
        if not r.get("t_fixed_in"):
            print(f"  wall {x['t']/IN:.1f} in, set by {lim}: lift needs {x['t_lift']/IN:.1f} in, wind "
                  f"{x['t_wind']/IN:.1f} in (MOR {x['mor'][0]}-{x['mor'][1]} MPa, no steel)")
        else:
            print(f"  wall {x['t']/IN:.1f} in, reinforced (steel carries the lift)")
        print(f"  peak temperature {r['peak_c']} C; array-days for its electricity: "
              f"{rng(x['elec'][0]/ARRAY_KWH_PER_DAY, x['elec'][1]/ARRAY_KWH_PER_DAY, '{:.0f}')}")
        if r["bought_frac"]:
            items = ", ".join(f"{k} {v[0]*100:.0f}-{v[1]*100:.0f}%" for k, v in r["bought_frac"].items())
            print(f"  bought/shipped (share of wall mass): {items}")
        print(f"  soils: {r['soils']}")
        print(f"  rig: {r['rig']}")
        for n in r.get("notes", []):
            print(f"  - {n}")
        for n in r.get("src", []):
            print(f"  src: {n}")
