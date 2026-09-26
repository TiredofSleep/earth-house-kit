#!/usr/bin/env python3
"""
print_check.py -- numbers for a PRINT-AND-TILT printer: a low gantry that builds panels FLAT on the
steel grid in the casting bed by ADDITIVE COMPACTION (not wet extrusion), hot-mixing quicklime at
the head, printing ribs for stiffness, then the panel is tilted up.
Run: python3 printer/print_check.py   (first-order; [TO-MEASURE] on the bench)
"""
import numpy as np
RHO, G, IMP = 1900, 9.81, 1.5
L, B = 2.44, 1.22                               # 8 ft span (tilt direction) x 4 ft wide

def section(parts):
    """parts: list of (width, height, y_bottom). returns area, centroid, I, depth"""
    A = sum(w * h for w, h, y in parts)
    yb = sum(w * h * (y + h / 2) for w, h, y in parts) / A
    I = sum(w * h**3 / 12 + w * h * (y + h / 2 - yb)**2 for w, h, y in parts)
    D = max(y + h for w, h, y in parts)
    return A, yb, I, D

def lift(A, yb, I, D, frac=0.90):
    w = RHO * A * G
    x = np.linspace(0, L, 4001); a = frac * L
    R0 = w * (a**2 - (L - a)**2) / (2 * a)
    M = np.where(x <= a, R0 * x - w * x**2 / 2, -w * (L - x)**2 / 2)
    sag, hog = M.max() * IMP, -M.min() * IMP
    return RHO * A * L, sag / (I / yb) / 1e6, max(sag / (I / (D - yb)), hog / (I / yb)) / 1e6, hog / (I / (D - yb)) / 1e6

i = 0.0254
designs = {
    "solid 6 in slab":                        [(B, 6*i, 0)],
    "3 in skin + 4 ribs to 8 in":             [(B, 3*i, 0)] + [(3*i, 5*i, 3*i)] * 4,
    "3 in skin + 4 ribs to 12 in (tall wall)": [(B, 3*i, 0)] + [(3*i, 9*i, 3*i)] * 4,
}
print("=" * 70)
print("1. STRUCTURE: printed ribs vs a solid slab (lift at 0.90 of height, x1.5 impact)")
print("=" * 70)
print(f"{'design':40s} {'mass':>7} {'stiffness':>10} {'skin face':>10} {'rib tips':>9}")
base_I = None
for name, parts in designs.items():
    A, yb, I, D = section(parts)
    base_I = base_I or I
    m, s_bot, _, s_hog = lift(A, yb, I, D)
    print(f"{name:40s} {m:5.0f} kg {I/base_I:8.1f}x {s_bot:7.2f} MPa {s_hog:6.2f} MPa")
print("-> ribs: ~30% less earth to dig, mix and lift, same or much more stiffness; skin-face")
print("   tension (carried by the steel grid) drops; rib tips stay nearly unstressed.")
print("   Cavities between ribs: fill with rice husk + lime cap = an insulated earth wall.")

print("\n" + "=" * 70)
print("2. DRY: hot-mixing quicklime at the head (per m^3 of mix)")
print("=" * 70)
water = RHO * 0.10
for cao_frac in (0.05, 0.07):
    cao = RHO * cao_frac
    bound = cao * 18 / 56.08
    heat = cao * 1.16e6
    evap = (0.3 * heat / 2.26e6, 0.6 * heat / 2.26e6)
    print(f"{int(cao_frac*100)}% quicklime: binds {bound:.0f} kg water chemically, "
          f"heat can boil off ~{evap[0]:.0f}-{evap[1]:.0f} kg more "
          f"-> {100*(bound+evap[0])/water:.0f}-{100*(bound+evap[1])/water:.0f}% of the {water:.0f} kg of mix water")
print("-> quicklime is already how road crews dry wet clay on site; at the head it stiffens")
print("   each lift within hours and heats it for the lime-pozzolan reaction.")

print("\n" + "=" * 70)
print("3. PRINT: compaction instead of extrusion -- no waiting for layers")
print("=" * 70)
head_w, speed, lift_h = 0.30, 0.05, 0.05
rate = head_w * speed * lift_h * 3600
panel_v = B * L * 6 * i
print(f"compaction shoe {head_w*100:.0f} cm wide at {speed*100:.0f} cm/s, {lift_h*100:.0f} cm lifts: "
      f"{rate:.1f} m^3/h ({rate/panel_v:.0f} panels/h of head capacity)")
mixer = 1.0
print(f"a 350 L pan mixer feeds ~{mixer:.0f} m^3/h -> ~{mixer/panel_v:.0f} panels/h: the MIXER is the bottleneck,")
print("not the head. Compacted earth at optimum moisture stands up immediately (that's why")
print("rammed-earth forms come off right after ramming), so lifts don't wait to dry.")
print("The compaction shoe FLOATS on the mix like a paver screed; the gantry only tows and")
print("lifts it, so the frame never fights the compaction force.")
