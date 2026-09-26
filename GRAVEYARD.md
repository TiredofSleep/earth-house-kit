# GRAVEYARD — killed, superseded, and corrected ideas
Kept on purpose so nobody rebuilds them. Each entry: the idea, what killed it, the correct form.

| idea | killed by | correct form |
|---|---|---|
| Fire the whole wall in place with a grid | energy: ~12,600 kWh/house, ~28 months on 3 kW, ~888 kWh battery per panel | fire only the binder (10–15%) |
| Fire the 15% binder inside the wall | pointless: heats a whole wall to fire 15% of it; needs a big battery, in-wall injection, and fights calcination shrinkage cracking | fire the binder in a batch kiln, mix before compaction |
| "The fired wall powers the house" | physics: firing energy is spent as heat; a fired wall stores nothing recoverable | the solar runs the build, then runs the homes; thermal mass keeps demand low |
| Pour cold activator onto glowing clay | flash-boil blowback hazard | (earth-panel branch only) inject on the cooldown, ~110–180 °C |
| Collapse air pockets to "fuse ground into rock" / sonofusion | not a physical process; bubble-fusion claims failed replication | compaction removes voids; binding is chemical (geopolymer or cement) |
| "CSEB is non-structural without a frame" | wrong: CSEB is used for load-bearing walls | differentiator = supply-chain independence + bundled mini-grid + optional cement-free binder |
| "The cement-free binder is the cost advantage" | arithmetic: saves ~$80–670 per house vs cement; carbon credits ~$6–39 per house | binder wins where cement is scarce or carbon matters; else use cement |
| "The reusable rig is the main cost" | the cost model: labor, roofs, power, field program dominate | cut roof and labor cost first; reuse the rig |
| Run it as a venture | no moat (open, established methods), slow cash-poor customers, thin lumpy margins | open-method charity deployed through partners; local builders can be social enterprises |
| "The rebar carries 16× the lift" (v0.3) | the formula let the steel yield; with 1–2 MPa earth on the compression side the earth crushes first (`common.flexural_capacity`) | 3.0–5.7× — still ample, stated honestly |
| "0.28 MPa lift stress vs ~0.3 MPa cracking = uncracked" (v0.3) | no safety margin, dry weight instead of the moist panel, no bed suction | moist panel 0.30 MPa × 1.5 → MOR ≥ 0.45 MPa at lift age; suction checked separately (0.23–0.33 MPa at breakaway) |
| "Quicklime at the head boils off the mix water" (v0.3) | energy: the slaking heat only warms the mix ~45–65 °C (`lime_heat.py`); it can't boil it | it binds 16–22% of the water chemically; evaporation is [TO-MEASURE]; watch for late slaking |
| Driving bars in at mid-depth for the no-dig lift (v0.3: "~15 kN·m, enough") | earth-limited capacity is only 1.1–2.0× the demand; bars near mid-depth have almost no lever arm | press the grid into the top face and lift at ~0.6 |
| Melt the soil into rock (in-situ vitrification, cast basalt, microwave sintering) for walls | energy: 0.72–1.0 MWh/t and ~3.5 MW for in-situ melting, 1–2 years to cool; 6–12 MWh per house even at 3 in (`rock_options.py`); lab microwave sintering 69–98 MJ/kg | fire clay at ~1000 °C instead: 0.9–3.0 MJ/kg from farm waste |
| Fire the whole house in place (Khalili's Geltaftan) | tried in Iran in the 1970s–80s and abandoned: fuel cost and pollution; heating a room from inside wastes most of the heat and fires unevenly | fire small units in an insulated kiln, then assemble |
| Sulfur concrete walls | melts at 115–120 °C, burns to SO₂; forbids swelling clay in the aggregate (ACI 548.2R) | not for homes; maybe plinths, tanks, drains |
| Bio-cement (MICP/EICP) as the general route | sands only; about 1 kg of ammonium chloride waste per kg of calcite; 2–6 t of reagents per house | niche for sandy sites |
| 12 in deep dome voussoirs | `dome_thrust.py`: under 50 m/s wind no thrust line fits and dry joints slide | 16 in deep voussoirs + the heavier tiled skin |
| Guastavino/timbrel 'no formwork' for dry units | the trick is fast-setting gypsum gluing each tile; dry units have no glue | seat steps + closing keys, course by course, light guide arches |
| Earth tubes / evaporative cooling / night flushing as the summer plan in Arkansas | humid air: condensation and mold in tubes, evaporative cooling collapses at 80–90% RH, night air too wet | shade, fans, cross-ventilation, a small solar dehumidifier |
| Salt-glazed units | needs ~1,250–1,300 °C and releases HCl; field kilns reach ~1,000–1,100 °C | engobe the outer face, or fire exterior units hotter |
| A 'hydrophobic' fired outer face as the rain barrier | fired ceramics are hydrophilic; real water beading needs siloxane that lasts 10–15 years | dense (cullet/engobe) skin for durability, hung replaceable siding as the rain barrier |
| Siding hung on nibs alone | BS 5534 won't accept nibs against wind suction | each board locks into the one below (2–5% of strength at 50 m/s) |
| Husk ash as a flux for a vitrified skin | it's ~90–97% silica: refractory at 1,000 °C, forms cristobalite | glass cullet as the skin flux; husk as the core pore former |
| Spray coatings on the masonry (carbon-fibre epoxy, polyurea, elastomerics, BaSO4 paint) | trap vapour and salts (BIA TN 6A), hide cracks, 7–20 year recoat cycles, irreversible; radiative cooling fades in humid air; none passes ICC 500 missile tests on masonry | light engobed tiles, silicate paint, siloxane on the plinth only, lime TRM kept as a repair, one ICC 500 safe room |
| A river 'sand-bar harvesting' structure on the Ouachita at Malvern | ~98% of the watershed above Malvern is behind three dams that trap sand; harvesting a sediment-starved reach causes bed incision downstream (Kondolf, 'Hungry Water'); 404/401/ESA/State Lands permits | screen the Wilcox sand beds in the clay pit, grog from kiln rejects, buy quarry sand at Jones Mill |
| Plain dry (unstressed) dome ribs | wind: GSF ~1.2 and joints slide (`dome_ribbed.py`) | one stainless tendon per rib, 20 kN |
| A steep cone/pyramid shelter 'deflects' the debris missile | ICC 500 fires the 2x4 perpendicular, and every surface >= 30 deg takes the full 100 mph missile; ASCE 7 has no coefficients for steep cones | round drum + shallow cap under 30 deg (`shelter_check.py`) |
| Dry-stacked or sand-filled clay alone as a shelter wall | 4 in solid brick shattered at ~76 mph (9 lb missile); only grouted/reinforced masonry and cavity walls have passed 100 mph | sacrificial fired skin + cavity + grouted cellular core (SHELTER_PLAN.md) |
| Arkansas residential safe-room rebates as the first funding | Arkansas's program ended in 2016; Arkansas FEMA money funds community safe rooms | community/school safe rooms in Arkansas; residential rebates in OK and MS |
| Bamboo in place of steel rods, tendons or hoop bands | ~1/13 the stiffness of steel, creep and moisture movement can't hold prestress; joints ~30-50% of the culm | steel/stainless in tension; bamboo only as visible, replaceable roof framing (rock/BIO_MATERIALS.md) |
| Mycelium or bacteria as self-healing agents inside the structure | dry-stacked fired clay has no mortar joints to heal; living agents need water and nutrients in walls meant to stay dry | replaceable parts + self-healing lime renders renewed on schedule |
| 'Petrified' or ceramized whole bamboo | mineralization is lab-scale on small samples; silicate leaches; biomorphic SiC needs >1,400 C and is brittle | revisit when research reaches whole culms |
| Concrete from clayey site soil | clay fines: 10–14% cement on clay soil gave only 1.5–3.4 MPa | only with screened sand/gravel |

## Overturned (kills that were wrong)

| idea | wrongly killed by | what overturned it |
|---|---|---|
| Tilt-up earth panels cast flat in the ground | an unchecked one-liner: "earth is weak in lift tension" | `tiltup_check.py`: 0.30 MPa with the pick at ~0.71 of height (moist panel, ×1.5 impact) vs ~0.3–1.0 MPa cracking strength; rebar carries 3.0–5.7× the lift. Now the core of the kit. |
| Relief cavities + injection (the founder's no-dig concept) | not killed — dropped in v0.2 when the binder moved to the kiln, and never put back | revived in §15 Route B as electrode wells, feed/drain points, and shrinkage relief for electro-osmotic consolidation |
