# TILT-UP DETAILING — from a cured panel in the pit to a braced, tied wall
### v0.1 · HANDOFF task 0 · numbers from `tiltup_check.py` (run from the repo root)

> **Status: a first-order detailing proposal for a licensed engineer to check.** Nothing here
> is code-approved. Every number is computed in `tiltup_check.py`, cited, or tagged
> [TO-VERIFY]/[TO-MEASURE]. Tilt-up is the moment a person stands next to a ton of earth on a
> rope: follow the sequence and the stop rules in §9 without shortcuts.

---

## 1. The standard panel: start with 8×4 ft × 6 in

| panel | moist mass at lift | hoist, tilting (×1.5) | hoist, setting (×1.5) |
|---|---|---|---|
| **8×4 ft × 6 in** | **~897 kg** | ~948 kg | **~1,346 kg** |
| 8×16 ft × 6 in | ~3,588 kg | ~3.8 t | ~5.4 t |

Build the first houses from 8×4 ft panels. They need only a 2 t manual chain hoist and a light
frame. The 8×16 ft panels cut connection work (five per house instead of 17), but they need a
gantry and rigging rated for more than 5 t. Move up to them only after the 8×4 program has
logged real breakaway and setting loads.

**The house module:** a 20×20 ft plan has an 80 ft perimeter, which is 20 modules of 4 ft. That
makes 17 solid panels plus 3 module-wide openings (one door, two windows). This is the "~15%
openings" in `common.py`.

---

## 2. The casting bed (the pit)

- **Bottom:** a level, compacted pit floor, then 1–2 in of clean sand, then plastic sheet. The
  sand is the bond breaker and a drainage layer; the plastic stops the mix wicking into it.
- **Edges: don't cast against the pit walls.** A panel bonded to soil on four edges plus the
  bottom has unknown suction and friction. Dig the pit ~6 in oversize and set **removable edge
  boards** (oiled timber or steel angle) to the exact panel size. Pull them before the lift,
  which leaves a free gap all round.
- **Hinge edge:** set the pit so the panel's **base edge lies on the wall line**, beside the
  plinth. Tilting about that edge brings the panel upright next to where it will stand.
- **Grid on chairs:** 2 in of cover (durability rule, MISSION §10). The welded perimeter bar
  frame carries the lift inserts, the connection plates and the bottom edge when the panel
  hangs vertical (§4).

---

## 3. Pick points: where the steel is decides where you lift

| grid position | pick at | worst earth-only face | steel face | source |
|---|---|---|---|---|
| **buried, two faces covered (baseline)** | **0.71 of height** | 0.30 MPa (both faces, balanced) | — | `tiltup_check.py` |
| surface grid on the bed face (exoskeleton) | **0.90** | 0.03 MPa | 0.67 MPa (steel carries it) | `tiltup_check.py` |
| grid pressed into the top face (no-dig Route A) | **0.60** | 0.09 MPa | 0.55 MPa | `nodig_check.py` |

- **Required strength before the lift:** the baseline lift stress of 0.30 MPa × 1.5 safety gives
  a **modulus of rupture ≥ 0.45 MPa at lift age**. Measure it on beams cast from the same batch
  and cured beside the panel (§8). If they don't reach it, wait and re-test. Don't lift.
- **Breakaway (bed suction):** at 0.5–2.0 kPa of suction [TO-MEASURE] the first instant of the
  lift puts **0.23–0.33 MPa** on the panel. At the high end that is more than the dynamic lift.
  Break the bed before the hoist takes the load: pull the edge boards, then lift the hinge-free
  (top) edge 10–20 mm with two bottle jacks or pry bars on hardwood pads, and let air in.
- **Width:** stress doesn't depend on panel width, as long as the load is spread across it. Use
  two inserts at ¼ and ¾ of the width on a spreader bar (§5).

---

## 4. Lift inserts: lift from the steel, never from the earth

**The rule:** every lifting load goes into the steel grid. Earth only has to hold its own place
on the bars.

- **Tilting inserts (2 per panel, on the up face at 0.71 of height):** a #4 bar **hairpin** (U-bar)
  hooked under two longitudinal grid bars and tied, with the loop standing ~3 in proud of the
  face. Load: **~474 kg per insert** with impact. A #4 hairpin has two legs × 129 mm² ×
  420 MPa ≈ 108 kN of yield capacity, roughly 20× the load. The insert is set by its hooks and
  the welds to the grid, not by the bar's size.
- **Setting inserts (2 per panel, on the top edge at ¼ and ¾ of the width):** the same hairpin,
  tied to the vertical bars and the top perimeter bar, looping out of the top edge. After the
  tilt, **the panel hangs vertical from these to be lifted onto the plinth**, so they take the
  full weight: **~673 kg each** with impact. Hanging, the earth grips the vertical bars at only
  ~0.03 MPa; the perimeter frame carries the bottom edge.
- **Capacity rule:** lifting inserts ≥ 2× their maximum load, and rigging hardware (shackles,
  slings, hooks) ≥ 5× [TO-VERIFY: OSHA 29 CFR 1926.704 for tilt-up; use it as the floor].
  Proof-load each insert design in Phase A (the pull-out rig) before using it on a panel.
- **Welding rebar:** ordinary A615 rebar isn't reliably weldable. Use A706 (weldable) bar for
  anything welded, or hook and tie instead. Welding burns off galvanizing, so touch it up with
  zinc-rich paint.
- Cut the loops flush or bend them in after erection. The top-edge loops can double as roof tie
  points into the bond beam (§7).

---

## 5. Rigging, spreader bar, hoist and frame

- **Spreader bar:** a steel pipe about 4 ft long, with a lug at each end over the inserts and a
  central lug for the hook, so both sling legs hang vertical and don't pull the inserts inward.
  [TO-VERIFY size with the engineer; 2 in schedule 40 pipe is the first candidate.]
- **Hoist:** a **2 t manual chain hoist**. It is sized for *setting* (1,346 kg with impact),
  not the tilt (948 kg), which leaves ~1.5× margin. Use a load cell or crane scale on the hook
  for the first panels, to measure real breakaway and setting loads (§8).
- **Keep the line vertical.** During the tilt the pick point travels **~5.7 ft** horizontally
  toward the base edge. A fixed hook drags the line off-plumb and pulls the panel sideways. Use a
  **trolley on a beam** that spans the pit, or a **rolling gantry** that can travel. That can be
  the print-and-tilt gantry (`printer/`): the same rails, a different head.
- **Frame height:** the tilting insert ends ~5.7 ft above the base, and the setting inserts end
  8 ft above it. The hook must clear the panel top plus the spreader and slings. Plan **≥ 11 ft
  under the beam**, and more if the plinth is high [TO-VERIFY on the first build].
- **Base kick-out:** the hinge edge must not slide. Bear it against the plinth face or a staked
  timber stop while tilting.

---

## 6. Temporary bracing

`tiltup_check.py` gives these values for an 8×4 ft panel pinned at its base, braced at 2/3 of
its height:

| wind (design, during construction) | pressure (Cp 1.2) | panel stress | brace force at 45° |
|---|---|---|---|
| 40 m/s (89 mph) | 1.18 kPa | 0.10 MPa | **3.7 kN** |
| 50 m/s (112 mph) | 1.84 kPa | 0.16 MPa | **5.8 kN** |

- **One brace per 4 ft panel**, at 2/3 of the height on the inside face, 45–60° to the ground.
  Wind comes from both sides, so the brace works in **tension and compression**. Bolt it to a
  brace insert (a third hairpin) and to the ground anchor; don't just prop it.
- **Brace member:** an adjustable steel pipe brace or a 4×4 timber. A 2×4 at ~7.5 ft is too
  slender to take compression. [TO-VERIFY with the engineer.]
- **Ground anchor:** there is no floor slab to brace to, so use a helical screw anchor or a
  buried deadman **rated ≥ 2× the brace force (~12 kN)**. Pull-test the first anchors in the
  site soil [TO-MEASURE].
- **Wind speeds** are placeholders. Take the site's design wind speed and the construction-period
  reduction from ASCE 7 / ASCE 37, or the local code [TO-VERIFY]. **Stop lifting in gusty wind**
  (a common tilt-up limit is ~20–25 mph [TO-VERIFY]).
- **Braces stay** until the panel is welded to its neighbours, the bond beam is complete and the
  roof is fixed.

---

## 7. Connections and the bond beam

**Plinth and footing ("good boots"):** a strip footing with a raised plinth, **≥ 8–12 in above
grade** [TO-VERIFY], in concrete, stone-and-lime or stabilized rammed earth with a
capillary break. Cast or anchor a **continuous steel angle** along the plinth top, set to the
wall line.

**Panel to footing:** set the panel on a ¾ in lime-mortar bed. Weld or bolt the bottom perimeter
bar (or an embedded base plate) to the plinth angle at **two points per panel**. Plate-and-angle
connections tolerate field errors of an inch; starter bars into grouted sleeves don't. Base
shear for wind and seismic still needs a check [TO-DO: extend `tiltup_check.py`].

**Panel to panel:** embed plates in each vertical edge at ~¼ and ~¾ of the height, welded to the
perimeter bar. After setting, field-weld a flat bar or short angle across each joint, or bolt a
strap on. Use stainless or galvanized parts and touch up after welding (MISSION §10: stainless
at connections). Leave a **½–¾ in joint**, then backer rod and lime mortar or sealant outside,
pointed inside. Use a steel angle across the corner at corners.

**Openings, the rule: make openings between panels, never inside them.** A 2 ft window cut into
a 4 ft panel raises the lift stress to **~0.59 MPa**, and a 3 ft opening to **~1.19 MPa**, before
counting the corners (`tiltup_check.py`). Instead:
- **Door:** leave a one-module (4 ft) gap. A steel or timber door frame forms the jambs. Above
  the door, set a short **lintel panel** (4 ft × ~16 in, ~150 kg), or deepen the bond beam over
  the gap.
- **Window:** leave a one-module gap with a short **sill panel** below and a **lintel panel**
  above. Short panels are light, easy to cast in the same pit, and lift by hand-winch.

**Bond beam ("the ring"):** a continuous beam around the wall top ties every panel together,
spans the openings and anchors the roof. Guidance for earth buildings in earthquake zones calls
for one [TO-VERIFY: e.g. NZS 4299, Peru E.080].
- *With cement available:* reinforced concrete, 6 in wide × 6–8 in deep, 2–4 #4 bars, cast on the
  panel tops, with the setting-insert loops and extra hairpins as ties.
- *Cement-free:* a galvanized steel channel or angle ring welded to top plates on each panel, or a
  bolted double timber plate where termites allow.
- Roof ties (hurricane straps) run from every rafter or truss to the bond beam.

---

## 8. Quality gates per panel

| gate | how | pass |
|---|---|---|
| strength at lift age | 3 small beams from the panel's batch, cured beside it; hand-rig bending test | MOR **≥ 0.45 MPa** (8×4×6 baseline) |
| inserts | visual + record; first use of any new insert design proof-loaded in Phase A | no slip, no weld cracks |
| breakaway load | load cell on the hook; record peak before the panel frees | log it: this is the suction [TO-MEASURE] |
| crack survey | photograph both faces before and after the tilt | no new cracks on an earth-only face; hairlines on a steel face noted |
| plumb and line | level + string line after setting, before welding | ±¼ in in 8 ft [TO-VERIFY] |
| braces | anchor installed and tightened, both ends bolted | before the hook is released |

---

## 9. Sequence and stop rules

1. Cure (MISSION §9) → **strength gate** (§8). No pass means no lift.
2. Pull the edge boards → **jack the free edge 10–20 mm** to break suction.
3. Rig the spreader to the tilting inserts; hoist on a trolley or gantry directly over the pick.
4. Tilt slowly, **nobody under or beside the panel's fall zone** (panel height + a margin on
   each side). The trolley follows the pick so the line stays vertical.
5. At vertical, move the rigging to the top-edge setting inserts. Lift onto the plinth mortar bed,
   against the angle.
6. Plumb it, **brace it (anchor + both bolts) before the hook lets go**. Then do the next panel.
7. Weld the panel-to-panel and panel-to-footing connections → bond beam → roof → remove braces.

**Stop rules:** gusty wind; a strength gate not met; any insert movement or weld crack; a
cracking sound or a new crack on an earth-only face during the tilt. Lower the panel and find
out why before going on.

---

## 10. Open items (for the engineer and for `tiltup_check.py`)
- Base shear and uplift at the plinth connection under wind and seismic load.
- Out-of-plane capacity of the finished wall (panel + bond beam + roof diaphragm).
- Corner and weld detail sizes; stainless vs galvanized cost at connections (`bom/`).
- Spreader, frame and brace member sizes from an engineer, not from this document.
- Measure the real bed suction on the first 5 panels and replace `SUCTION_KPA` in `common.py`.
