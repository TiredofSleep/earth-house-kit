#!/usr/bin/env python3
"""
energy_estimate.py -- honest order-of-magnitude energy budget for one geopolymer-clay
test panel. Founding calc for the earth-panel engineering repo.
Run: python3 energy_estimate.py
These numbers are deliberately conservative-honest: they show WHY drying is the slow
solar phase and calcination is the battery burst, and WHY insulation is mandatory.
"""

def panel_energy(L=0.61, W=0.61, T=0.152, rho=1800, moisture=0.20,
                 T_ambient=15, T_calcine=700):
    c_water, L_vap, c_clay = 4186, 2.26e6, 900   # SI units
    vol = L*W*T
    mass = vol*rho
    water = mass*moisture

    E_dry  = water*c_water*(100-T_ambient) + water*L_vap          # heat + boil off water
    E_calc = mass*c_clay*(T_calcine-100)                          # heat dry clay to calcine
    E_dehy = mass*0.14*L_vap*0.5                                  # dehydroxylation (rough)
    E_tot  = E_dry + E_calc + E_dehy

    kwh = lambda j: j/3.6e6
    print(f"panel {L}x{W}x{T} m  ->  {mass:.0f} kg clay, {water:.1f} kg water @ {int(moisture*100)}%")
    print(f"  Phase 1 dry-out (solar, patient):     {kwh(E_dry):5.1f} kWh   (latent-heat dominated)")
    print(f"  Phase 2 calcination burst (battery):  {kwh(E_calc):5.1f} kWh   (must SUSTAIN to soak)")
    print(f"  dehydroxylation endotherm:            {kwh(E_dehy):5.1f} kWh")
    print(f"  ---------------------------------------------")
    print(f"  subtotal (no losses):                 {kwh(E_tot):5.1f} kWh")
    print(f"  with real losses (2-4x):              {kwh(E_tot)*2:.0f}-{kwh(E_tot)*4:.0f} kWh")
    return kwh(E_tot)

if __name__ == "__main__":
    print("="*60)
    print("EARTH PANEL ENERGY BUDGET (honest, order-of-magnitude)")
    print("="*60)
    print("\n-- test panel (2x2x0.5 ft) --")
    panel_energy()
    print("\n-- drier clay (10% moisture) shows the water cost --")
    panel_energy(moisture=0.10)
    print("\nTAKEAWAYS:")
    print("  * drying is latent-heat-dominated -> slow solar, patience (cheap, unavoidable)")
    print("  * calcination is a sustained burst -> battery, sized for ENERGY not just peak")
    print("  * losses dominate without insulation -> jacket the panel, not optional")
    print("  * a full wall multiplies this hard -> prove the PANEL first; wall energy is a")
    print("    separate sobering study, a real kill-condition candidate at scale.")
