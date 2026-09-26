#!/usr/bin/env python3
"""
lime_heat.py -- how much heat hot-mixed quicklime puts into a panel, and how much grid
cure energy it saves. Run: python3 lime_heat.py
CaO + H2O -> Ca(OH)2 releases ~65 kJ/mol. The heat is a PULSE at mixing (minutes to hours),
not a sustained cure. It was paid for at the lime kiln; slaking returns part of it.
"""
DH = 65e3                    # J per mol CaO slaked
M_CAO, M_H2O = 0.05608, 0.018
Q_PER_KG = DH / M_CAO        # J per kg CaO
PANEL_KG = 860               # 8x4 ft x 6 in stabilized earth panel
MOISTURE = 0.10              # compaction water fraction
LIME_FRAC = (0.05, 0.07)     # quicklime as fraction of panel mass (Roman binder)
USEFUL = (0.3, 0.6)          # fraction of the pulse still in the panel once it's cast [TO-MEASURE]
GRID_CURE = (22, 43)         # kWh per panel for a 20->70 C warm cure incl. ground losses
KWH = 3.6e6

if __name__ == "__main__":
    print("=" * 62)
    print("HOT-MIX LIME HEAT")
    print("=" * 62)
    print(f"slaking heat: {Q_PER_KG/1e6:.2f} MJ per kg quicklime = {Q_PER_KG/KWH:.2f} kWh/kg")
    water = PANEL_KG * MOISTURE
    heat_cap = water * 4186 + (PANEL_KG - water) * 850          # J/K
    for i in (0, 1):
        cao = PANEL_KG * LIME_FRAC[i]
        q = cao * Q_PER_KG
        print(f"\n{int(LIME_FRAC[i]*100)}% quicklime: {cao:.0f} kg per panel")
        print(f"  heat released: {q/KWH:.1f} kWh")
        print(f"  temperature rise if none escaped: +{q/heat_cap:.0f} C")
        print(f"  extra water it consumes: {cao*M_H2O/M_CAO:.0f} kg (add to the mix)")
    lo = PANEL_KG*LIME_FRAC[0]*Q_PER_KG*USEFUL[0]/KWH
    hi = PANEL_KG*LIME_FRAC[1]*Q_PER_KG*USEFUL[1]/KWH
    print(f"\nuseful heat left in the cast panel ({int(USEFUL[0]*100)}-{int(USEFUL[1]*100)}%): {lo:.0f}-{hi:.0f} kWh")
    print(f"grid warm cure needs {GRID_CURE[0]}-{GRID_CURE[1]} kWh/panel -> lime covers "
          f"~{lo/GRID_CURE[1]*100:.0f}-{min(100, hi/GRID_CURE[0]*100):.0f}%")
    print(f"per house (17 panels): saves ~{17*lo:.0f}-{17*hi:.0f} kWh of grid heat")
    kiln = 3.18e6                                                # J/kg CaO to calcine limestone (ideal)
    print(f"\nwhere the heat came from: making quicklime takes >= {kiln/KWH:.2f} kWh/kg at the lime kiln;")
    print(f"slaking gives back {Q_PER_KG/kiln*100:.0f}% of that. a rebate, not free energy -> buy the lime.")
    print("timing: the pulse lands during mixing and casting and fades over ~a day under cover;")
    print("it replaces roughly the first day of grid heat, not the whole cure.")
