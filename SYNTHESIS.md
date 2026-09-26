# THE SYNTHESIS — the best of what has worked, combined into one house
### v0.1 · the whole system in one page, layer by layer, with where each idea comes from

> **The vision:** one family of fired-clay parts — corner and fold bricks, clamped wall panels,
> domed roofs — all made from the site's soil, all interlocking without mortar or nails, all
> replaceable, designed to outlast modern buildings by avoiding the ways modern buildings die.
> Nothing in it is new on its own. Each layer is something that has already worked somewhere,
> for decades or centuries. **The combination is new, and untested** — Phase R decides it.
>
> Status key: **modelled** = a script in this repo checks it · **sourced** = published evidence
> (see `rock/RESEARCH_NOTES.md`) · **TO-TEST** = needs a bench or full-scale test.

---

## 1. The house, layer by layer

| layer | what we build | borrowed from | status |
|---|---|---|---|
| **foundation** | rubble-trench or gabion ring to below frost depth, drained to daylight; helical piles only on bad soil | Frank Lloyd Wright's rubble trench; gabion plinths in post-quake Nepal; frost-protected shallow foundations (HUD) | sourced |
| **plinth ("good boots")** | fired-clay or stone plinth ring ≥ 8–12 in above grade, clean-stone capillary break + damp-proof course | earth-building practice; BSI-123 (capillarity) | sourced |
| **optional isolation** | two-layer geotextile over HDPE sliding joint under the plinth ring, ≥ 75 mm movement gap | brick-masonry sliding-plinth tests (~70% less roof acceleration); μ≈0.1 geotextile/UHMWPE | sourced, TO-TEST |
| **units** | die-extruded cellular fired-clay units (8 in, 6 staggered rows, husk-filled), printed where the shape varies; fired to ASTM C216 severe-weathering grade | Poroton/Porotherm high-perforation clay blocks; brick industry; clay 3D printing | modelled (`thermal_check.py`), TO-TEST |
| **precision** | bed faces ground after firing: ±0.5 mm height, ≤ 0.2 mm flat | Poroton Plan-T Dryfix ground blocks | sourced, TO-TEST |
| **wall panels** | 48 units dry-stacked flat, clamped by 2 rods against steel end channels, tilted up — 413 kg | prefab brick panels (BIA TN 40); post-tensioned masonry; tilt-up | modelled (`brick_panel_check.py`) |
| **corners / folds** | polygon folds joined by wedged fired key blocks (shachi-sen style), re-drivable | Japanese kigumi locking; Greek cramps (separate keys, never stone hooks) | sourced, TO-TEST |
| **confinement** | plinth ring + rods + wall-top steel ring = a closed cage around dry masonry | **confined masonry** (1–2 storey houses mostly undamaged in the 2010 M8.8 Chile quake); corner confinement +64% load, +288% drift in dry-stack tests | sourced |
| **plan** | 16–20-sided polygon: 26% more floor per panel than a square, half the wind drag, self-bracing | round vernacular houses; tilt-up bracing logic | modelled (`form_check.py`) |
| **openings** | module-wide gaps with sill and lintel panels, never cut into panels | Inca trapezoidal openings (short lintels); tilt-up practice | modelled (`tiltup_check.py`) |
| **roof** | spherical cap to 51.8°, all in compression; one die makes every voussoir; each seats on a step until its course closes with a key | Armadillo Vault (399 dry stones, 16 m span); Nubian domes (course by course); Brunelleschi's herringbone | modelled (`dome_check.py`, `dome_thrust.py`) |
| **ring** | panels' top channels bolted into the tension ring (11–18× capacity) | Poleni's hoops on St Peter's; Armadillo's ties | modelled |
| **roof skin ("good hat")** | 20 mm cocciopesto (lime + crushed kiln rejects) under overlapping fired scale tiles, corbelled drip eave, limewash every 1–3 years | Roman cocciopesto (2,000-year cisterns); tiled domes; Dieste's thin topping | sourced; **its weight is what makes the dome pass wind** (§2) |
| **climate: hot-humid** | shade + reflective skin, cross-ventilation through low windward inlets, rain-capped closable cupola at the oculus, ceiling fan, a small solar dehumidifier holding 50–60% RH | CBE Berkeley fan studies (+2.7 °C comfort at 0.5 m/s); EPA mold guidance | sourced |
| **climate: hot-dry** | the same shell plus night flushing, courtyards, jaali, windcatchers with evaporative cooling (10 °C+ drops) | Iranian and Middle Eastern vernacular | sourced |
| **floor** | gravel capillary break, barrier, insulating layer, site-fired floor tiles in lime | earthen and tile floor practice | sourced |
| **water** | drip-ring gutter at the dome base, 1–2 L/m² first flush, partly buried 5–10 m³ ferrocement or lime-lined cistern, ceramic pot filter from the same kiln | Texas A&M rainwater guidance; ferrocement tanks (50–100 year life) | sourced |
| **cooking & sanitation** | induction on the microgrid; urine-diverting dry toilet in an annex, 12-month vault storage | WHO household air pollution; Eawag sanitation compendium | sourced |
| **energy** | 20 kW PV + 50 kWh LFP that runs the build, then the village; PAYG meters, ring-fenced battery fund, paid local technicians, battery kept cool inside a mass enclosure | Chhattisgarh mini-grids (1,400+ working) vs Sundarbans (abandoned: no O&M) | sourced |
| **kiln** | portable fibre-lined downdraft kiln fired by a forced-draft husk gasifier; flue heat dries green ware; pyrometer + cones on every batch | Olsen fast-fire kiln; VSBK/zigzag heat recovery (0.84–1.16 MJ/kg, ~80% less PM2.5 than old kilns) | sourced, TO-TEST |
| **production** | die for the bulk, printer for the variable parts, grinder, bed jig; **balance the line** — soil prep and firing set the pace, not the machine | Open Source Ecology's CEB press lesson (one shoveller ≈ 250 bricks/day) | modelled (`house_designer.py`) |
| **program** | build the hard half (shell, roof, wet core); owners add **linked satellite domes** later by pre-designed rules; train a paid local production team; open files + a certification route from day one | Elemental's half-houses (92 of 93 expanded); Mapungubwe ($110/m², 100+ trained); WikiHouse (mortgageable only after a warranty) | sourced |

---

## 2. The dome under uneven loads (`dome_thrust.py`)

Heyman's safe theorem, the dome cut into orange slices with **no help from hoop compression** (the
cautious model — real domes are stronger). Geometric safety factor = how much room the line of
thrust has inside the voussoirs; ≥ 1 stands, ≥ 1.5 we call margin.

| 16 in voussoirs, tiled skin | 16-gon (322 ft²) | 20-gon (505 ft²) |
|---|---|---|
| dead, full snow | 2.8–2.9 | 2.3 |
| half snow (unbalanced) | 2.4 | 1.9 |
| **wind 50 m/s** | **1.62** | **1.29** |
| wind + half snow | 2.1 | 1.7 |
| earthquake 0.15 g / 0.3 g | 2.2 / 1.66 | 1.8 / 1.31 |
| worst dry-joint sliding (of allowed) | 0.91 | 0.92 |

- **Wind governs, not weight.** Suction over the crown (Cp ≈ −1.2) nearly cancels a light dome's
  weight; with the thin 0.55 kPa skin, the dry joints went past the allowed friction. **The heavier
  tiled skin (~1.15 kPa) is what fixes it** — the waterproofing layer is also the ballast.
- The 12 in dome fails wind outright (no line fits) — the 16 in voussoir stands.
- **Decision: build the 16-gon first.** It passes every case with margin even in the cautious model.
  The 20-gon stands in every case but with thin margins; it waits for a 3-D thrust-network or
  discrete-element analysis that counts the hoop action.
- Wind pressure coefficients and seismic levels are placeholders [TO-VERIFY per site].

---

## 3. What we deliberately did NOT borrow (and why)

| tempting idea | why not | source |
|---|---|---|
| Guastavino/timbrel "no formwork" | it works because fast-setting gypsum glues each tile; dry units have no glue | SUDU / Block 2010 |
| earth tubes, evaporative coolers, misting windcatchers in Arkansas | humid air condenses in tubes (mold); evaporative cooling collapses at 80–90% RH | earth-tube and evaporative-cooling reviews |
| night flushing as the main summer strategy in humid climates | small diurnal swing, wet night air: negligible gain | Kumasi, Ghana study |
| salt glazing the units | needs ~1,250–1,300 °C and releases HCl; our kilns reach ~1,000–1,100 | ceramics practice |
| cement renders or mortars on fired clay | crack, trap water, bring salts (efflorescence) | BIA TN 23A |
| carbon steel set tight in the masonry | rust expands and splits it (the Acropolis's 20th-century repairs) | YSMA |
| 50 machines before one finished house | Open Source Ecology's scope creep | OSE |
| owners extending a closed dome ad hoc | Iquique's welding-spark fires; lightweight add-ons | Carrasco & O'Brien 2021 |

---

## 4. Why it could outlast modern buildings — stated honestly

Modern buildings mostly die of **hidden steel rusting, water getting in, and parts that can't be
replaced**. This system is designed against each:
- **no hidden steel** — rods loose in open cells, channels in plain sight, keys in stainless or titanium;
- **stone-like units in compression** — fired clay fired to severe-weathering grade, stressed at ~1–5% of strength;
- **water kept out in layers** — raised plinth, drip eave, cocciopesto, tiles, limewash, lime not cement;
- **everything replaceable** — dry joints, re-drivable wedges, re-tensionable rods, a sacrificial skin;
- **earthquakes met by friction and confinement**, not by brittle strength.

**Allowed claim:** "designed so that nothing critical fails unseen and every part can be replaced."
**Not allowed:** "lasts 500 years" or "outlasts concrete" — nobody can test that; the tests we can run are in Phase R.

---

## 5. What decides it (in order)
1. **Phase R bench tests** (`making-system/BRICK_PANEL.md` §9): fire the home clay to severe-weathering
   grade; print, fire, grind units; dry-stack seating loss; wedged fold key; seat-step sliding.
2. **Two full-scale prototypes per new soil — one loaded to failure, one kept** (the SUDU/Block recommendation).
3. **A 2 m dry test dome**, then the 16-gon House #0.
4. **3-D thrust analysis** before any 20-gon.
5. **A certification path** with a structural engineer from the first prototype (WikiHouse's lesson).

Sources: `rock/RESEARCH_NOTES.md` (all sections). Detail: `making-system/BRICK_PANEL.md`,
`making-system/KIT_OF_PARTS.md`, `rock/ROCK_OPTIONS.md`.
