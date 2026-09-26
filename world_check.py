#!/usr/bin/env python3
"""
world_check.py -- if fired-clay kit houses became a primary form of shelter: per-house footprint and scale.
Run: python3 world_check.py

Per house (the lean Ring 16 ribbed kit, 322 ft^2 shell) from the repo's own models, then a few
planetary-scale ratios. Global figures are widely cited round numbers [TO-VERIFY before any external use];
this is a sense-of-scale script, not a forecast.
"""
import sys
import business_model as bm

HUSK_MJ = (13.0, 16.0)
FIRE_MJ_KG = (1.1, 3.0)
STEEL_CO2 = (1.4, 2.3)          # t CO2 per t steel (scrap-EAF .. blast furnace) [TO-VERIFY]
GRID_CO2 = 0.4                  # t CO2 per MWh if machines ran on the grid instead of plant solar [TO-VERIFY]
TRUCK_CO2_T_MI = 0.00010        # t CO2 per tonne-mile, flatbed diesel (~100 g) [TO-VERIFY]
KWH_PER_T = (60, 150)

# global round numbers [TO-VERIFY]
RICE_HUSK_T_YR = 150e6          # ~20% of ~750 Mt paddy
CEMENT_SHARE_CO2 = 0.08         # cement ~8% of global CO2 (Chatham House 2018)
BUILDINGS_SHARE = 0.37          # buildings + construction, share of energy-related CO2 (UNEP GlobalABC)
US_CD_WASTE_T = 600e6           # US construction & demolition debris per year (EPA 2018)
UNITS_NEEDED_PER_DAY = 96000    # UN-Habitat: new affordable units needed daily to 2030


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    k = next(bm.kit(p) for p in __import__("glob").glob("houses/ring16_ribbed.json"))
    bm.SCEN["lean"] = True
    fired = bm.fired_t(k)
    st = bm.steel_now(k)
    bm.SCEN["lean"] = False
    steel_t = (st["rod_kg"] + st["channel_kg"]) / 1000 + st["tendon_m"] * 0.5 / 1000 + 0.05   # + fittings ~50 kg
    husk = (fired * FIRE_MJ_KG[0] / HUSK_MJ[1], fired * FIRE_MJ_KG[1] / HUSK_MJ[0])
    kwh = (fired * KWH_PER_T[0], fired * KWH_PER_T[1])
    co2_steel = (steel_t * STEEL_CO2[0], steel_t * STEEL_CO2[1])
    co2_truck = fired * 300 * TRUCK_CO2_T_MI
    co2_grid = (kwh[0] / 1000 * GRID_CO2, kwh[1] / 1000 * GRID_CO2)
    print("=" * 92)
    print("ONE HOUSE: lean Ring 16 ribbed shell, 322 ft^2 (models in this repo)")
    print("=" * 92)
    print(f"  fired clay {fired:.1f} t (site clay + sand from the same pit); steel ~{steel_t*1000:.0f} kg")
    print(f"  fuel: {husk[0]:.1f}-{husk[1]:.1f} t of rice husk (farm residue, biogenic carbon); machines {kwh[0]/1e3:.1f}-{kwh[1]/1e3:.1f} MWh (plant solar)")
    print(f"  fossil CO2: steel {co2_steel[0]:.1f}-{co2_steel[1]:.1f} t + 300-mile truck {co2_truck:.1f} t"
          f" (+{co2_grid[0]:.1f}-{co2_grid[1]:.1f} t if the machines ran on the grid)")
    tot = (co2_steel[0] + co2_truck, co2_steel[1] + co2_truck + co2_grid[1])
    print(f"  -> ~{tot[0]:.1f}-{tot[1]:.1f} t CO2 for a shell designed to last generations; no cement in the structure")

    print("\nSCALE")
    houses_fuel = (RICE_HUSK_T_YR / husk[1], RICE_HUSK_T_YR / husk[0])
    print(f"  the world's rice husk (~{RICE_HUSK_T_YR/1e6:.0f} Mt/yr) could fire ~{houses_fuel[0]/1e6:.0f}-{houses_fuel[1]/1e6:.0f}"
          f" million such shells a year;")
    need = UNITS_NEEDED_PER_DAY * 365
    print(f"  UN-Habitat's ~{UNITS_NEEDED_PER_DAY:,} units/day is ~{need/1e6:.0f} million a year -> the world's husk alone"
          f" could fuel {houses_fuel[0]/need:.1f}-{houses_fuel[1]/need:.1f}x that (plus bagasse, straw, wood waste)")
    print(f"  cement is ~{CEMENT_SHARE_CO2*100:.0f}% of global CO2 and buildings+construction ~{BUILDINGS_SHARE*100:.0f}% of energy CO2:"
          " housing that needs no cement and little cooling moves real numbers")
    print(f"  the US throws away ~{US_CD_WASTE_T/1e6:.0f} Mt/yr of construction and demolition debris; a house built once")
    print("  for 200+ years instead of rebuilt or gutted every 50-80 cuts that stream, and its broken units")
    print("  go back into the kiln as grog.")
    print("\nHONEST LIMITS: fired clay is heavy (local plants, not global shipping); soils vary (sandy regions")
    print("need other routes); firing still emits particulates unless kilns are clean; pits must be reclaimed;")
    print("masonry needs confinement in earthquake country; none of it is proven until Phase R and certification.")
