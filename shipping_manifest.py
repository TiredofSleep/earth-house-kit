#!/usr/bin/env python3
"""
shipping_manifest.py (v0.2) -- what ships for a 10-house village, two scenarios.
Run: python3 shipping_manifest.py
All weights/volumes are first-order [TO-MEASURE].
"""
import math
C20_M3, C20_KG = 33, 28000

RIG = {"batch kiln": (300, 1.5), "mill": (250, 0.8), "soil prep": (150, 0.6),
       "mixer": (150, 0.8), "forms / CSEB press": (800, 4.0), "compaction": (150, 0.5),
       "instruments": (50, 0.3), "QA kit": (200, 0.6), "tools & PPE": (300, 1.5)}
POWER = {"solar 20 kW": (1150, 4.5), "inverters": (150, 0.6), "LFP 50 kWh": (500, 0.9),
         "racking & BOS": (500, 2.5), "distribution cable": (600, 1.5)}
PER_HOUSE = {"rebar": (300, 0.4), "activator": (250, 0.35), "steel roof": (500, 2.0),
             "electrical + water": (250, 1.2), "doors, windows, fasteners": (300, 1.5)}

def tot(d, n=1):
    return sum(w for w, _ in d.values()) * n, sum(v for _, v in d.values()) * n

def report(label, parts):
    kg = sum(p[0] for p in parts); m3 = sum(p[1] for p in parts)
    n = math.ceil(max(m3 / C20_M3, kg / C20_KG))
    print(f"{label:44s} {kg/1000:5.1f} t  {m3:5.1f} m^3  -> {n} x 20ft")
    return m3

if __name__ == "__main__":
    print("=" * 62)
    print("VILLAGE SHIPPING MANIFEST v0.2 (10 houses)")
    print("=" * 62)
    everything = report("ship everything (rig + power + 10 houses)",
                        [tot(RIG), tot(POWER), tot(PER_HOUSE, 10)])
    core = report("regional sourcing (ship the rig only)", [tot(RIG)])
    print(f"\nper house shipped: {everything/10:.1f} m^3 (ship everything) vs "
          f"{core/10:.1f} m^3 (regional) -- the walls ship as 0.")
    print("regional sourcing buys solar, batteries, rebar, roofing and activator in-country:")
    print("  cheaper freight, local warranties, no corrosive-goods paperwork for the activator.")
