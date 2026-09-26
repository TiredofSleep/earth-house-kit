# FIRED-UNIT PANEL — printed rock units, dry-stacked, clamped, tilted up
### v0.1 · numbers: `brick_panel_check.py`, `thermal_check.py`, `form_check.py` · routes compared in `rock/ROCK_OPTIONS.md`

> **Status: a design hypothesis with sourced parts and no tested whole.** Each piece has
> precedent: fired clay, ground dry-stack blocks, post-tensioned masonry, prefabricated brick
> panels and tilt-up. We found **no tested system of printed, fired, dry-stacked load-bearing clay
> units** — that combination is new, so every number below is [TO-MEASURE] until Phase R (§9).
> Engineer review required.

---

## 1. The system in one paragraph

Soil with enough clay is printed into thin-walled cellular units: a bead of clay, not a glob of
wet mud. The units dry in hours, and a portable fibre-hood kiln fires them to ~1000 °C with rice
husk. Their bed faces are ground flat. On a casting bed they are dry-stacked flat into a panel
with **no mortar and no grout**. Their cells line up into channels, and two threaded rods run
through them against steel end channels. The rods are tensioned, and the panel is clamped rock:
**~282 kg (4.5 in) or ~413 kg (8 in, insulating) for 8×4 ft**, against ~897 kg for compacted
earth. It is assembled, tensioned and tilted up **the same day**, because nothing has to cure.

---

## 2. Why this shape of process

| constraint | answer |
|---|---|
| the kiln wants small pieces (fires evenly, portable) | small units, ~4.7 kg each |
| the build wants big pieces (fewer lifts and joints) | units clamped into storey-height panels; the hoist sets the size |
| thick clay dries slowly and cracks | 6–8 mm walls dry in hours: drying time goes with the square of thickness |
| steel inside fired clay cracks it | rods sit in open cells, never embedded, and can be replaced |
| mortar and grout mean cure waits | dry-stack plus post-tensioning: zero wet trades |

Precedent for the panel itself: storey-height prefabricated brick panels, some prestressed, since
the 1950s (BIA Technical Note 40; ASTM C901).

---

## 3. The unit

**Two sizes of the same idea:**

| unit | envelope | clay share | fired mass | for |
|---|---|---|---|---|
| **cellular 4.5 in** | 295 × 193 × 114 mm | ~40% | ~4.7 kg | mild climates, partitions, first tests |
| **thermal 8 in** | 295 × 193 × 200 mm | ~32% | ~6.8 kg | outside walls: U ≈ 0.62 W/m²K, 9 h lag |

**Cross-section: staggered rows, not straight or diagonal webs.** `thermal_check.py` solves 2-D
heat flow through each pattern (8 in wall, lime plaster both faces, husk in the cells):

| pattern | U (W/m²K) | time lag | why |
|---|---|---|---|
| straight-through webs, 1 row | 1.25 (4.5 in) | 4.5 h | each web is a heat highway |
| diamond lattice | 1.75 (4.5 in) | 4.1 h | more webs, more clay, more bridges |
| diagonal truss, 3 rows | 0.76 | 8.2 h | better, but diagonal webs still bridge |
| **staggered, 6 rows** | **0.62** | **9.0 h** | heat must zigzag through thin clay at every row |

This is the geometry the European high-perforation clay block industry arrived at (Poroton,
Porotherm): many thin rows, with webs offset row to row. **Rice husk in the cells matters as much
as the pattern**: it cuts a one-row unit's conductivity by more than half against still air.

**The rod cells are the exception.** Two cells per panel column carry the rods. Give them
double-bead walls and solid webs on each side: post-tensioned dry-stack walls with thin webs have
failed in web shear (Sokairge et al. 2017). Leave the rod cells empty of husk so the rods can be
inspected, re-tensioned and replaced (§8).

**Print rules** (from the clay-printing literature; see the research note in `rock/`):
1. **Uniform walls:** one or two beads everywhere, no thick-thin transitions, filleted corners.
   Uneven shell thickness is the first cause of drying cracks.
2. **Layer height ~35–50% of bead width** (≈2.5–4 mm for a 6–8 mm bead). De-air the paste.
3. **Keep overhangs ≤ 30–45°.** Triangular infill tolerated up to ~60° with the fewest failures.
4. **Print the cells along Z.** The unit stands on end while printing; that makes the cells straight
   vertical tubes, easy to print and clean.
5. **Compensate shrinkage by axis.** Printed clay shrinks more along Z than across (e.g. 8–9% XY
   vs 11% Z in one fired test). Scale the print file per axis, from test firings of the site clay.
6. **Dry slowly and evenly** (covered, turned), and fire at ~2–5 °C/min to ~1000 °C.

**Keys locate; they never carry load.** Dry joints have no cohesion. Shear crosses them by friction
under prestress (μ ≈ 0.5–0.6). Print shallow drafted keys that stand ~1 mm *short* of bearing, the
way Hydraform blocks bear on their shoulders with a 3–4 mm gap at the key. The keys stop units
sliding while you stack; the rods do the rest. Topological-interlock faces (osteomorphic shapes)
are a research option. They tolerate losing blocks, and their best interlock angle is ~20°, but
they depend entirely on a peripheral constraint, which here is the rods and end channels.

**Precision: grind after firing, don't hope.** Industrial dry-set clay blocks hold height ±0.5 mm,
bed-face flatness ≤ 0.2 mm and parallelism ≤ 0.6 mm (Poroton Plan-T Dryfix approval) by grinding
fired blocks. Unground dry joints touch over only ~23% of their area, and face shells split at
17–92% of ultimate load. Even the tightest standard size classes are 5–10× too loose. So:
**print Z ~2–3 mm oversize and grind both bed faces flat and parallel.** A portable surface grinder
on a jig does it [TO-MEASURE rate]. If grinding proves impractical in the field, a thin stiff
interlayer (~7 GPa cast layer: +32% capacity) is the fallback. A soft pad is not: a 3 GPa layer
*cut* capacity 41% by splitting the units.

---

## 4. The panel

| | 4.5 in cellular | 8 in thermal |
|---|---|---|
| layout | 6 columns × 8 units = 48 units | same plan, deeper unit |
| mass (8×4 ft) | ~282 kg | ~413 kg |
| rods | 2 × M16 8.8 galvanized, 30% of yield | 2 × M16, 25% of yield |
| clamp on the clay | 1.08 MPa (27% of low f′m) | 0.63 MPa (20% of low f′m) |
| joints stay closed | lift ×1.5 and 40 m/s wind, **after 35% loss** | same |
| if joints open | rods carry 11.7× the lift, 3.1× the 50 m/s wind | 18.8×, 7.3× |

- **End channels** (steel C, top and bottom) anchor the rods and double as the **setting lugs**
  (top), the **footing connection** (bottom, bolted to the plinth angle) and the **bond-beam
  connection** (top). Put bearing plates under the nuts. Keep channel bearing ≤ 0.5 f′m.
- **Losses are seating, not creep.** Dry joints bed in: ~24 joints × 0.05 mm is ~1.2 mm over the
  panel, which is 25–30% of the rod stretch. Put **Belleville disc-spring stacks** under the nuts,
  **overload once and re-tension at 24 h**, and design for 20–35% loss (TMS/CMHA practice). Fired
  clay also expands slightly with moisture in its first months (+3×10⁻⁴), which *raises* rod force.
  Age units a few weeks after firing where possible.
- **Lifting inserts ≥ 4× panel weight** (BIA TN 40): ≥ 1,130 kg (4.5 in) or ≥ 1,652 kg (8 in).
- **Tilt as in `TILTUP_DETAILING.md`**, with three changes: no pit (a flat sand-and-plastic bed),
  no bed suction worth the name (dry units, no cast face), and a hoist a third the size.
- **The panel's size is set by the hoist, not the kiln:** an 8×16 ft cellular panel is ~1.2 t.

**Assembly sequence (per panel, two people):** lay the bottom channel on the bed jig → stack units
column by column, keys engaged → slide the rods through the aligned rod cells → top channel, disc
springs, nuts → tension to the set torque in two passes → pour husk into the insulation cells from
the top end and cap → overload, relax, re-tension → tilt. The 24 h re-torque can happen standing.

---

## 5. Why it is fast, lean and portable (per house)

| | compacted-earth pit panels | printed fired dry-stack |
|---|---|---|
| wall mass | 14.6 t | ~4.6 t (4.5 in) |
| heaviest panel | ~897 kg | ~282–413 kg |
| cure before lift | 7–28 days | none |
| fuel | kiln binder via solar | 0.25–0.85 t of husks |
| bought per house | 0.7 t cement or lime | ~0.46 t of rods and channels, reusable if demounted |
| shipped rig | kiln, mill, mixer, compactor, pits | printer(s) or pug mill + die, fibre-hood kiln, grinder, bed jig, torque wrench, small hoist |

**Throughput limits** (`brick_panel_check.py`):
- **Printing** 816 units at one 8×4 mm bead per nozzle is ~370 nozzle-hours per house, so plan
  multi-nozzle heads or several printers.
- **Die extrusion:** the universal unit is a constant section, so a small pug mill with a
  cellular die makes it in 4–14 machine-hours. **Use the die for the universal unit and print only
  what varies:** rod-end units, insert units, corners, sills, lintels.
- **Firing** takes 4–7 firings of a 0.5–1 t fibre hood.

---

## 6. Thermal protection

- Outside walls use the **8 in thermal unit, husk-filled, staggered rows**: U ≈ 0.62 W/m²K, ~9 h
  lag, decrement 0.42. That is close to a mass-wall code target of ~0.56 [TO-VERIFY local code],
  at 133 kg/m² against 289 kg/m² for compacted earth, which has U 2.69.
- **Mass inside, insulation outside.** The daily cycle favours heavy interior faces. Options:
  fill the inner row of cells with sand, or finish with a thick interior lime or earth plaster.
- **Lime plaster both faces:** it is vapour-open, sacrificial, and closes the dry joints against wind.

---

## 7. The shape: stability, heat, and a 500-year structure

### The plan: a polygon, not a box (`form_check.py`)
| plan | modules | floor | floor per panel | wall per floor | wind drag |
|---|---|---|---|---|---|
| square 20×20 ft | 20 | 400 ft² | 23.5 ft² | 1.60 | Cd ~1.2–1.4 |
| **16-gon** | 16 | 322 ft² | 24.7 ft² | 1.59 | Cd ~0.6–0.9 |
| **20-gon** | 20 | **505 ft²** | **29.7 ft²** | **1.27** | Cd ~0.6–0.9 |

The same 20 panels enclose **26% more floor** as a 20-gon. There is 20% less wall per unit floor
to gain or lose heat, and roughly half the wind drag [TO-VERIFY Cd]. A closed ring **braces
itself**: every joint is a fold, so temporary braces come off as soon as the ring closes.

### The roof: compression only (worked out in `dome_check.py` and `KIT_OF_PARTS.md` §3)
**Result:** a spherical cap stopped at 51.8° is all compression. Use 16 in deep cellular voussoirs
(2.0–2.6× the minimum masonry-dome thickness), cut from one die, each with a seat step. The rim
thrust becomes ~14–24 kN of ring tension in the panels' bolted top channels, which carry it 11–18×.

The structures that have stood for centuries in fired brick are compression shapes: vaults and
domes. A fired-unit **dome or cone** over a polygon removes the steel roof, this kit's biggest
per-house cost, and the last short-lived part. It needs its outward thrust taken by the ring beam
or by buttressing. That is the next calculation [TO-CHECK: thrust of a 6–8 m fired-unit dome
against a ring of 8 in panels]. In heavy-rain climates a dome needs a maintained waterproof lime
skin or a light secondary rain roof.

### The 500-year rules
We cannot test 500 years, and MISSION's rule stands: **no longevity claim beyond what the evidence
supports**. What we can do is design out every known way such buildings die:

1. **Gravity alone holds it up.** Walls and dome work in compression. The rods are for lifting,
   wind and earthquakes: insurance, not the structure.
2. **No hidden steel.** Rods sit in open cells: inspectable, re-tensionable, **replaceable**. Use
   stainless 316 where the budget allows. Galvanized rods get a planned replacement (~50–100
   years) instead of a silent failure inside the wall.
3. **Every part is replaceable.** Dry-stack means a damaged unit can be swapped out: slacken the
   rods, replace the unit, re-tension. Topologically interlocked assemblies survive losing a
   quarter of their blocks.
4. **Fire the units hard enough to shrug off water and frost**: ~1000 °C, low absorption. Test
   against ASTM C216 severe-weathering criteria [TO-MEASURE].
5. **Good boots and a good hat:** a raised plinth, and an overhang or a skin the dome sheds water
   from.
6. **A sacrificial skin:** lime plaster, renewed every 5–20 years, takes the weather so the units
   never do.
7. **The weak links are known and scheduled:** rods, plaster, roof skin, the solar system. Each has
   a service interval; nothing critical fails unseen.

**Allowed claim:** "designed so that nothing critical fails unseen, every part can be replaced,
and the structure stands by compression alone." **Not allowed:** "lasts 500 years."

---

## 8. Kill-conditions
- Site clay won't fire to ≥ 20 MPa units even blended → haul clay for units only, or use the
  geopolymer route.
- Printed units crack or warp more than 2–3 mm of grind stock can fix → die-extruded units.
- Grinding can't reach ±0.5 mm / 0.2 mm in the field → the ~7 GPa interlayer, or the grouted panel.
- Seating loss over 35% after the re-torque, or joints open during the tilt → more prestress, a
  deeper unit, or the grouted panel.
- Printing plus die extrusion can't make one house of units in about a week → hand-molded hollow
  units and a grouted panel.

---

## 9. Phase R — the bench tests, cheapest first
1. **Fire bars of the home clay** at 900 / 1000 / 1050 °C (Phase A test kiln): shrinkage per axis,
   strength, absorption. *Gate:* ≥ 20 MPa, absorption low enough for severe weathering.
2. **Print, dry, fire 10 cellular units:** cracks, warp, shrinkage by axis; tune the per-axis scale.
3. **Grind 10 units:** reach ±0.5 mm height and 0.2 mm flatness with a jig and a cup wheel; time it.
4. **Compression of units and dry-stacked prisms**, perpendicular and parallel to the print layers.
5. **One dry-stacked column, tensioned:** seating loss over 24 h and 30 days, with and without
   disc springs.
6. **One 8×4 ft panel:** assemble, tension, tilt with a load cell, then bend it to failure.
7. **Thermal:** hot-box or heat-flux-meter test of an 8 in wall section against `thermal_check.py`.

---

## Sources (details and URLs in the research notes and `data/rock_routes.json`)
- BIA Technical Notes 3A (material properties), 9 (manufacturing), 18 (volume changes), 40
  (prefabricated brick masonry).
- Wienerberger Poroton Plan-T10 Dryfix approval Z-17.1-1088 (ground-unit tolerances).
- Chewe Ngapeya (Univ. Luxembourg): dry-stack contact, interlayers.
- CMHA TEK 14-20A (post-tensioned masonry, losses), TEK 14-22 (dry-stack).
- TMS 402 / TMS 1430-21 (dry-stack guidelines).
- Sokairge et al. 2017; Kohail et al. 2019 (post-tensioned dry-stack walls).
- Hydraform wall tests (CIB).
- Mirkhalaf et al., PNAS 2018 and Dyskin/Estrin (topological interlocking).
- Clay-printing studies (Eazao, WASP, PMC11012627).
