# ROCK FROM SITE SOIL — every route, compared
### v0.1 · numbers: `rock_options.py` (routes as data in `data/rock_routes.json`), `brick_panel_check.py`

> **The brief:** solid rock, not compressed earth, not printed earth. Quicker, leaner, and more
> portable than the pit-cast compacted panel. This document weighs every way we found to turn a
> site's soil into stone. Each figure is sourced in the data file or tagged UNSOURCED/[TO-MEASURE].

---

## 1. The one idea that changes everything: rock is strong, so walls get thin

Compacted earth has a modulus of rupture around 0.3–1 MPa. It needs 6 in of wall and a steel
grid, and an 8×4 ft panel weighs ~900 kg. Rock is 5–20× stronger, so the wall's thickness is set
by wind and handling instead of weakness. **Less material means less to dig, fire, carry and
lift.** Less material is also faster, and a lighter panel needs a smaller hoist, which is easier
to ship.

`rock_options.py` sizes each route's wall from its own strength: tilted up with no steel, 50 m/s
wind, a 1.5 margin, never under 3 in. It then counts energy, fuel, purchases and time for one
house (50.5 m² of wall):

| route | wall | 8×4 panel | wall mass | husks / house | bought / house | cast → lift | verdict |
|---|---|---|---|---|---|---|---|
| compacted earth (today's baseline) | 6 in + steel | ~906 kg | 14.6 t | — | 0.7 t | 7–28 d | not rock |
| **printed fired units, dry-stack + rods** | **4.5 in** | **~282–306 kg** | **4.6 t** | **0.3–1.0 t** | **0.4–0.5 t steel** | **2–5 d** | **LEAD** |
| printed fired units, grouted + bars | 4.5 in | ~315–340 kg | 5.2–5.8 t | 0.3–0.9 t | 0.3–0.5 t | 5–28 d | strong |
| fired solid brick, laid on site | 7.5 in | (laid) | 16–18 t | 0.9–4.2 t | 0.3–0.7 t | 7–20 d | proven fallback |
| fired single-piece ceramic panel | 3 in | ~453 kg | 6.9–7.7 t | 0.5–1.8 t | 0 | 5–19 d | risky: cracking |
| melted and cast rock | 3 in | ~680 kg | 9–12 t | — | 0 | 1–3 d | **killed:** 6–12 MWh/house |
| geopolymer (soil + fired clay + activator) | 4 in | ~665 kg | 10–11 t | — | 0.3–0.7 t caustic | 3–28 d | candidate |
| concrete (screened sand/gravel + cement) | 3 in | ~521 kg | 8.5–8.9 t | — | 1.1–1.5 t cement | 3–7 d | benchmark, sandy sites |
| lime-sand steam-cured | 6.5 in | ~982 kg | 15–17 t | 0.2–0.6 t | 1.1–2.0 t lime | 12–48 h | sandy sites |
| sulfur concrete | 3 in | ~544 kg | 8.5–9.2 t | 0.1 t | 1.3–1.6 t sulfur | 2–24 h | **killed for homes:** burns |
| bio-cemented sandstone | 6.5 in | ~982 kg | 15–17 t | — | 2.1–5.7 t reagents | 1–7 d | niche: sand only |

---

## 2. What the research settled

- **Firing clay is the cheapest way to make stone with heat.** Efficient brick kilns fire at **0.9–1.2
  MJ/kg** (vertical-shaft 0.9, zigzag 1.1); a traditional clamp averages 3.0. The result is units of
  36–46 MPa average (US molded and hollow brick). Brickmakers dry in 24–48 h in heated dryers, fire
  in 10–40 h, and shrink 2–4% drying plus 2.5–4% firing. [BIA TN 3A, TN 9; PMC11800390]
- **Melting is out for walls.** In-situ vitrification, which melts ground in place with electrodes,
  takes 0.72–1.0 MWh per tonne and ~3.5 MW of power, and a big melt takes 1–2 years to cool. That is
  6–12 MWh per house even at 3 in thick, or 100–190 days of the 20 kW array. Cast basalt is superb
  (≥300 MPa) but it's a factory product. [EPA SITE report; EUTIT data sheet]
- **Firing a whole house in place was tried, and abandoned.** Khalili's Geltaftan houses (Iran,
  1970s–80s) were fired as their own kiln with ~24 h of oil burners at ≥1000 °C. They were dropped
  for fuel cost and pollution: firing a room from inside wastes most of the heat and fires unevenly.
- **Site soil breaks most chemical routes.** Sulfur concrete forbids swelling clay and melts at
  115 °C. Bio-cement only works in sand and makes about its own weight in ammonium chloride.
  Cement can't reach concrete strength with clay fines (10–14% cement on clay soil gave only
  1.5–3.4 MPa). **Only firing and geopolymer actually use the clay.**
- **Big fired panels are a factory trick.** Industry makes 1.6×3.2 m porcelain slabs, but pressed
  and only 6–20 mm thick. A thick slab of site clay fired in a field kiln would very likely crack.

---

## 3. Where the gold is: small fired units, big tilted panels

Two constraints fought each other in every panel idea:

| | wants | because |
|---|---|---|
| **the kiln** | small pieces | small fires evenly, dries fast, cracks less, is portable |
| **the build** | big pieces | fewer lifts, fewer joints, less labor |

**Firing small units and assembling them into big panels resolves this.** The kiln sets the unit
size, and the hoist sets the panel size. There's a precedent: prefabricated storey-height brick
panels, some prestressed, have been built since the 1950s (BIA Technical Note 40).

**Printing the units is how to make them lean.** A thin bead of clay (6–8 mm) builds a cellular
unit that is ~40% clay:
- **Dries in hours, not weeks:** drying time goes with the square of the thickest clay section.
- **Fires evenly, and needs about a third of the fuel of solid brick.**
- **Lines up its cells into channels** along the panel for steel.
- **Leaves the other cells for rice husk,** so the wall is insulated rock.

One house of the universal unit (295 × 193 × 114 mm, ~4.7 kg) is **816 units, 3.7 t of fired clay,
0.25–0.85 t of husks** and 4–7 firings of a portable fibre-hood kiln (`brick_panel_check.py`).

**Then the precision route removes the last wet step.** Dry-stack the units with no mortar, thread
two M16 rods through the aligned channels, and tension them against steel end channels. The panel
is clamped rock: **282 kg for an 8×4 ft panel, assembled and lifted the same day**, with no cure
wait. Details in `making-system/BRICK_PANEL.md`.

**Heat and shape.** `thermal_check.py` shows the cross-section decides the insulation. Staggered
rows of thin webs with husk-filled cells beat straight or diagonal webs. An **8 in, 6-row unit
reaches U ≈ 0.62 W/m²K with a ~9 h lag** at 133 kg/m²; a 6 in compacted-earth wall is U 2.69.
`form_check.py` shows a **20-sided plan encloses 26% more floor than a square from the same 20
panels**. It braces itself once closed, and takes a compression-only fired-unit dome instead of a
steel roof. Sources for everything above: `rock/RESEARCH_NOTES.md`.

---

## 4. The cheapest tests, in order (Phase R)

1. **Will the home clay make good brick?** Fire 12 small bars of Hot Springs clay in the Phase A test
   kiln at 900 / 1000 / 1050 °C. Measure shrinkage, strength, water absorption, and whether they
   slake in water. *Gate:* units ≥ 20 MPa, no slaking. Otherwise blend sand or haul clay for units only.
2. **Print a unit.** A small paste-extrusion clay printer prints the cellular unit. Dry it, fire it,
   and measure distortion and cracking. *Gate:* no cracks, and fired dimensions repeatable enough for
   dry-stacking (see the design rules in BRICK_PANEL.md).
3. **Dry-stack a column.** Stack 8 units, tension one rod, load it, and measure seating loss over
   24 h and the compressive strength of the column.
4. **One panel.** Assemble 48 units, tension, tilt with a load cell on the hoist, and test in bending.
5. **Throughput.** Time printing against a small pug mill with a cellular die for the universal unit.

**Kill-conditions:**
- The clay won't fire to ≥ 20 MPa even blended → grouted panel of hauled-clay units, or the
  geopolymer route.
- Printed units crack or warp beyond what grinding can fix → die-extruded units plus a grout joint.
- Dry-stack seating loss exceeds ~30% of the rod force [TO-MEASURE] → thin-bed adhesive or grouted panels.
