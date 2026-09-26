#!/usr/bin/env python3
"""
print_check.py -- numbers for a PRINT-AND-TILT printer: a low gantry that builds panels FLAT on the
steel grid in the casting bed by ADDITIVE COMPACTION (not wet extrusion), hot-mixing quicklime at
the head, printing ribs for stiffness, then the panel is tilted up.
Run: python3 printer/print_check.py   (first-order; [TO-MEASURE] on the bench)
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from common import G, IN, IMPACT, RHO_DRY, RHO_LIFT, MOISTURE, PANEL_H as L, PANEL_W as B, lift_moments

def section(parts):
    """parts: list of (width, height, y_bottom). returns area, centroid, I, depth"""
    A = sum(w * h for w, h, y in parts)
    yb = sum(w * h * (y + h / 2) for w, h, y in parts) / A
    I = sum(w * h**3 / 12 + w * h * (y + h / 2 - yb)**2 for w, h, y in parts)
    D = max(y + h for w, h, y in parts)
    return A, yb, I, D

def lift(A, yb, I, D, frac=0.90):
    """mass, skin-face (bottom) tension, rib-tip (top) tension, MPa"""
    sag, hog = lift_moments(RHO_LIFT * A * G, L, frac * L)
    return RHO_LIFT * A * L, sag * IMPACT / (I / yb) / 1e6, hog * IMPACT / (I / (D - yb)) / 1e6

i = IN
DESIGNS = {
    "solid 6 in slab":                        [(B, 6*i, 0)],
    "3 in skin + 4 ribs to 8 in":             [(B, 3*i, 0)] + [(3*i, 5*i, 3*i)] * 4,
    "3 in skin + 4 ribs to 12 in (tall wall)": [(B, 3*i, 0)] + [(3*i, 9*i, 3*i)] * 4,
}

CAO_FRAC = (0.05, 0.07)
def lime_water(cao_frac, m_dry=RHO_DRY):
    """per m^3 of mix: water bound chemically by slaking (certain), temperature rise if the heat
    stays in the lift, and an UPPER bound on extra evaporation if all the heat left as vapour."""
    water = m_dry * MOISTURE
    cao = m_dry * cao_frac
    bound = cao * 18 / 56.08
    heat = cao * 1.16e6
    dT = heat / (water * 4186 + m_dry * 850)
    evap_max = heat / 2.4e6            # latent heat of evaporation at ~50-70 C
    return water, bound, dT, evap_max

if __name__ == "__main__":
    print("=" * 70)
    print("1. STRUCTURE: printed ribs vs a solid slab (lift at 0.90 of height, x1.5 impact)")
    print("=" * 70)
    print(f"{'design':40s} {'mass':>7} {'stiffness':>10} {'skin face':>10} {'rib tips':>9}")
    base_I = None
    for name, parts in DESIGNS.items():
        A, yb, I, D = section(parts)
        base_I = base_I or I
        m, s_bot, s_hog = lift(A, yb, I, D)
        print(f"{name:40s} {m:5.0f} kg {I/base_I:8.1f}x {s_bot:7.2f} MPa {s_hog:6.2f} MPa")
    print("-> ribs: ~30% less earth to dig, mix and lift, same or much more stiffness; skin-face")
    print("   tension (carried by the steel grid) drops; rib tips stay nearly unstressed in the lift.")
    print("   In service, wind pushing on the skin side puts the unreinforced rib tips in tension --")
    print("   [TO-CHECK] before tall ribbed walls: run a bar up each rib or keep ribs on the lee face.")
    print("   Cavities between ribs: fill with rice husk + lime cap = an insulated earth wall.")

    print("\n" + "=" * 70)
    print("2. DRY: hot-mixing quicklime at the head (per m^3 of mix)")
    print("=" * 70)
    for f in CAO_FRAC:
        water, bound, dT, evap = lime_water(f)
        print(f"{int(f*100)}% quicklime: binds {bound:.0f} kg of the {water:.0f} kg mix water chemically "
              f"({100*bound/water:.0f}%), warms the lift ~+{dT:.0f} C if the heat stays;")
        print(f"   extra evaporation from a thin, uncovered lift: 0 to at most {evap:.0f} kg "
              f"({100*evap/water:.0f}%) [TO-MEASURE]")
    print("-> it does not BOIL the mix: the pulse raises it ~45-65 C (see lime_heat.py). The bound")
    print("   water is certain; evaporation depends on lift thickness, cover and weather.")
    print("-> RISK: quicklime that hasn't fully slaked when a lift is compacted can slake later and")
    print("   swell, cracking the panel. Road crews let lime-treated clay 'mellow' first. Gate:")
    print("   compacted hot-mix cubes soaked after 7 days must show no expansion cracking.")

    print("\n" + "=" * 70)
    print("3. PRINT: compaction instead of extrusion -- no waiting for layers")
    print("=" * 70)
    head_w, speed, lift_h = 0.30, 0.05, 0.05
    rate = head_w * speed * lift_h * 3600
    panel_v = B * L * 6 * i
    print(f"compaction shoe {head_w*100:.0f} cm wide at {speed*100:.0f} cm/s, {lift_h*100:.0f} cm lifts: "
          f"{rate:.1f} m^3/h ({rate/panel_v:.0f} panels/h of head capacity, single pass [TO-MEASURE passes])")
    mixer = 1.0
    print(f"a 350 L pan mixer feeds ~{mixer:.0f} m^3/h -> ~{mixer/panel_v:.0f} panels/h: the MIXER is the bottleneck,")
    print("not the head. Compacted earth at optimum moisture stands up immediately (that's why")
    print("rammed-earth forms come off right after ramming), so lifts don't wait to dry.")
    print("The compaction shoe FLOATS on the mix like a paver screed; the gantry only tows and")
    print("lifts it, so the frame never fights the compaction force.")
