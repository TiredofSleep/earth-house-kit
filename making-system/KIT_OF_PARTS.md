# KIT OF PARTS — houses from interlocking fired units, joined without nails or mortar
### v0.1 · `house_designer.py` (designs in `houses/*.json`, parts in `data/kit_units.json`, joints in `data/joints.json`) · `dome_check.py`

> **The idea:** a house is a small vocabulary of fired-clay parts and a handful of joints,
> assembled dry the way Japanese carpenters assemble a frame: no nails, no glue, locked by
> geometry and wedges, and able to be taken apart and re-tightened. A house design is a data file;
> the designer turns it into every part, the steel and keys, the fuel and machine time, and the
> structural checks. **Nothing here is tested** (Phase R, `BRICK_PANEL.md` §9).

---

## 1. Translating Japanese joinery into fired clay

Japanese joints (kigumi) and fired clay are opposite materials:

| | timber | fired clay |
|---|---|---|
| tension and bending | good | **very poor**: it cracks |
| compression | good | **excellent** (20–40 MPa units) |
| how kigumi carries tension | as bearing on a hooked face, e.g. the head of a gooseneck or a dovetail | a clay hook's neck would shatter |
| how kigumi locks | wedges (kusabi), draw-pins (komisen), paired wedges (shachi-sen) | **the part we keep** |

So we copy **the locking, not the hooks.** Fired clay only ever bears in compression. The pulling
and locking is done by small, replaceable keys: steel rods, tapered wedges, dowels. Stone
builders did the same. Greek ashlar was held by iron or bronze cramps set in lead, Egyptian
masonry by wooden dovetail cramps, and some Inca walls by poured bronze cramps. Always a separate
key, never a stone hook.

| Japanese device | what it does in timber | the fired-clay kit's version |
|---|---|---|
| **komisen** (draw-pin, offset holes) | driving the pin pulls the joint shut; can be driven out | **the rod clamp**: rods through open cells pull every bed joint shut; re-torqued or removed from the top |
| **shachi-sen** (paired wedges, ~3 mm spare travel) | draws a tenon tight; re-driven when wood shrinks | **the fold joint**: a wedge pair draws two panels onto a fired key block, with spare travel to re-drive |
| **kusabi** on nuki (1–2 mm oversize) | pre-compresses the joint; stiffens it | the same wedges driven 1–2 mm oversize to pre-compress the fold |
| **kanawa-tsugi** (stepped splice, wedge last) | wedge pre-compresses the bearing steps; repairable from the side | the principle: **the last piece in is the lock**, driven from outside, so any joint can be opened for repair |
| sliding dovetail, watari-ago | locate and hold members | **locator keys** that stand ~1 mm short of bearing: they place units, they never carry load |

---

## 2. The joints (`data/joints.json`)

1. **Locator keys (unit to unit).** Shallow, drafted, ~1 mm short of bearing, as Hydraform
   blocks bear on their shoulders. Load goes through **ground rim bands** on the shells and webs
   (Greek anathyrosis: contact only where you've made it flat). Shear crosses by friction under
   the clamp (μ 0.48–0.62).
2. **Rod clamp (the panel).** Two rods in 60 mm cells, disc springs, top and bottom channels.
   Rods sit **loose**, so rust can never burst the clay. The Acropolis's 20th-century steel
   repairs, set tight in concrete, did split the marble. Titanium and stainless haven't.
   **316 stainless** for a long-life build; galvanized with scheduled replacement for a budget one.
3. **Wedged key at each fold (panel to panel).** Three per fold: a large fired key block sits
   across the two edge units' seats, and a tapered wedge pair (316 stainless or titanium) draws
   the panels onto it. Driven 1–2 mm oversize, with ~3 mm left to re-drive. In an earthquake the
   fold **slips by friction and re-seats**. Dry and interlocking systems lose energy through
   friction and rocking, never by the brittle part yielding. Confining the corners of dry walls
   raised lateral load 64% and drift 288% in tests, and every fold of the polygon is a confined
   corner.
4. **Friction slider at the plinth.** The bottom channel bears on the plinth; stainless dowels in
   oversized sockets stop large slips, as the dowels and wooden centre-plugs between Greek column
   drums do. Drum columns on shake tables rock and slide with little permanent offset.
5. **Ring splice.** The panels' top channels, bolted across each fold, are the dome's tension ring,
   as Poleni's hoops are on St Peter's and ties are on the Armadillo Vault. It stays in plain
   sight and can be re-tightened.
6. **Seat step (dome voussoirs).** See §3.
7. **Closing key (each dome course).** The last voussoir of a course is tapered and pressed in, like
   a keystone. Interlocking-puzzle research calls this the one key part that locks the set.

8. **Keystone ring course** (drum shelter, round walls). Units tapered wider outside slide in
   radially and hook, by an inside-bottom groove, over a tongue on the course below. Each engages the
   previous unit's radial groove, so there is **one assembly order**, and the pinned closing key locks
   the course. This is the recursive-interlock idea from the research, built in clay.

**Key materials:** titanium or 316 stainless, or a large fired-clay block in pure compression.
**Never carbon steel set tight.** Hardwood only where it stays dry and can be replaced: blackwood
cramps lasted ~3,000 years, but only in Egypt's dry climate. Give metal keys clearance and a
compliant bed. Stainless expands ~2× as much as fired clay with heat.

---

## 3. The dome (`dome_check.py`)

| over | dome | rise | shell stress | rim thrust | ring tension | thickness vs minimum |
|---|---|---|---|---|---|---|
| 16-gon, 322 ft² | cap to 51.8°, 16 in cellular voussoirs | 1.5 m | ~0.1 MPa | ~4.5 kN/m | ~14 kN (ring 18×) | **2.6×** |
| 20-gon, 505 ft² | cap to 51.8°, 16 in cellular voussoirs | 1.9 m | 0.135 MPa | 6.0 kN/m | 23.5 kN (ring 11×) | **2.0×** |

- **Why a cap to 51.8°:** in membrane theory a spherical dome's hoop force turns to tension
  beyond 51.8° from the crown. Stop there and **every part of the dome is in compression**; only
  the steel ring at the rim is in tension. A hemisphere is taller and cracks along its meridians,
  as the Pantheon and St Peter's did. It still stands, but why accept that.
- **Why deep units:** the minimum thickness of a masonry dome is ~0.04 × radius for a cap
  (Zessin, Lau & Ochsendorf) and 0.042–0.043 for a hemisphere (Heyman; Coccia et al.). **Depth,
  not weight,** keeps the line of thrust inside the shell. A 16 in cellular voussoir with extra
  rows of husk-filled cells weighs about what an 8 in one does but is twice as deep. The target is
  ≥ 2× the minimum, a margin of our own choosing [UNSOURCED]. The stresses are tiny either way (~2%
  of strength).
- **One die for the whole dome:** on a sphere every course subtends the same angle, so every
  voussoir has the **same cross-section**. Only the end-cut angle changes per course, cut on a jig
  while leather-hard. The dome is extruded, not printed.
- **Building it with no mortar and no formwork.** Nubian domes rise without centering because
  earth mortar holds each brick by suction until its course closes. We have no mortar, and every
  course of a 51.8° cap has beds steeper than dry friction allows (18–22° with a 1.5 margin). So
  each voussoir has a **seat step**: a small ledge whose bearing face is flat enough for dry
  friction, loaded only in compression. A clay hook would be loaded in tension; a seat step never
  is. A cord from the dome's centre sets each unit, as Nubian masons use a compass cord. Each
  course closes with its **key voussoir**, and from then on hoop compression holds it. That is the
  job Brunelleschi's herringbone bricks did in Florence.
- **The good hat:** the first course is a corbelled **eave** that overhangs the wall with a drip
  edge. An **oculus** at the crown vents hot air by the stack effect. In a rainy climate the dome
  needs a maintained lime skin or a light rain cover.

---

### Uneven loads (`dome_thrust.py`)
Half snow, 50 m/s wind and 0.15–0.3 g earthquake, orange-slice arches with no hoop help: **wind
governs**, because crown suction nearly cancels a light dome's weight. With the tiled cocciopesto skin
(~1.15 kPa) the 16-gon passes every case at ≥ 1.62 and no joint slides. The 20-gon stands everywhere
but with thin margins (1.29 wind, 1.31 quake) and waits for a 3-D analysis. The 12 in dome fails. Full
table in `SYNTHESIS.md` §2.

### The ribbed dome (`dome_ribbed.py`) — the default roof from v0.1 of the kit
A thrust line needs depth only where the thrust goes, so put the depth in **ribs** and let **thin webs** span between them (Gothic ribbed vaults; ETH's Rippmann floor; Dieste's prestressed brick vaults).

- **Ribs:** 16 in deep units along the meridians, **one on every second wall fold** (8 on the 16-gon,
  10 on the 20-gon), meeting a compression ring at the oculus. The section is constant, with skewback
  seats on both sides for the webs, so **one die** makes them all.
- **Webs:** the **6 in graded wall unit** (U ≈ 0.56 by itself), spanning rib to rib as shallow arches,
  built course by course on the skewbacks. Each bay-course closes with a key unit.
- **One tendon per rib:** a **10 mm stainless wire rope** with swaged threaded ends, nut-tensioned at
  the oculus to 20 kN, and checked at 13 kN after 35% loss. It clamps every rib joint shut, and its
  curve pulls the rib inward (P/R) against wind suction. That puts only **~1.2 MPa** on the rib clay,
  with the rope at 36% of its breaking load. It's the same rod-clamp idea as the wall panels, curved.
- **Results** (half snow, 50 m/s wind, 0.3 g quake, ribs alone with no hoop help):

| house | dome clay vs 16 in cellular | worst rib GSF | worst sliding | webs |
|---|---|---|---|---|
| 16-gon, 8 ribs | **−35%** (3.2 vs 4.9 t) | **4.2** | 0.46 | GSF ≥ 14, net load stays downward |
| 20-gon, 10 ribs | **−35%** (5.0 vs 7.7 t) | **2.9** | 0.53 | GSF ≥ 18 |
| 24-gon hall, 12 ribs | — | 2.2 | 0.58 | — |

- **Without the tendons the ribs fail in wind** (GSF ~1.2, joints slide): a rib and its light web
  are pushed around by suction. **With them, the 20-gon passes every case**, which the solid dome
  never did. Webs stay loaded downward only because the tiled skin is heavy, so the skin stays.
- Build order: a temporary central mast holds the oculus ring; ribs go up and are tensioned; webs
  are laid course by course between them; the mast comes out.

## 4. The designer (`house_designer.py`)

```
python house_designer.py houses/ring20_dome.json
```

A design file names the polygon, the wall unit, the openings and the roof. The designer returns
the parts list. For the 20-gon house:

| | |
|---|---|
| fired parts | **2,038**: 1,659 die-extruded (universal, edge, voussoir), 379 printed (rod ends, inserts, key seats, eaves, oculus) |
| fired clay | 15.0 t → 1.0–3.5 t of husks, 15–30 firings of a 0.5–1 t fibre hood |
| machines | printer ~2 days (8 nozzles); die 8–33 machine-hours |
| steel and keys | 34 full rods + short rods for sill and lintel panels, channels, 60 fold keys and wedge pairs, 20 ring splices, 20 base sliders |
| checks | wall panel clamp OK after 35% loss; dome all-compression, ring 11×, thickness 2.0× |

**Design new houses by writing a new file.** Change the number of modules, the openings or the
dome depth, and the designer re-sizes every part and re-runs the checks.

---

## 5. What makes it "Japanese" beyond the joints
- **Demountable:** every lock is driven from outside. Pull the wedges, slacken the rods, and a
  panel comes out. A cracked unit gets replaced, not patched.
- **Adjustable over time:** wedges and rods keep spare travel, for re-driving after the joints
  seat, as shachi-sen allow for timber shrinkage.
- **Precise, not forced:** ground rim bands, and keys that locate but don't bear.
- **Earthquake behaviour by friction:** joints that slip and re-seat, instead of a rigid box that cracks.

## 6. Open work
- **Uneven loads on the dome** (half-dome snow, wind, earthquake): thrust-network or
  discrete-element analysis, not only membrane theory.
- **Assembly order:** directional blocking graphs (DESIA) so every panel and course has exactly one
  last key. This also becomes the build manual.
- **Geometry files:** parametric print paths and die drawings for each part, with per-axis shrinkage.
- **Phase R additions:** wedge-and-key fold test (pre-compression, slip, re-drive); seat-step
  voussoir sliding test; a 2 m test dome built dry, closed, and loaded.

Sources: joinery, stone, dome and interlocking sections of `rock/RESEARCH_NOTES.md`.
