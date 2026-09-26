# HANDOFF — earth-house-kit → Claude Code (and any contributor)

## Start here
```
python3 check_numbers.py        # runs everything below and checks MISSION.md against it
python3 system_sizing.py
python3 shipping_manifest.py
python3 costs_estimate.py
python3 tiltup_check.py
python3 build_timeline.py
python3 site_profile.py
python3 lime_heat.py
python3 nodig_check.py
python3 printer/print_check.py
python3 earth-panel/energy_estimate.py
```
All of them run clean (`pip install -r requirements.txt` first). They are the repo's honesty
layer: any new number in MISSION.md needs a line in a script or a cited quote, and a headline
number should get a line in `check_numbers.py`. Shared geometry and material values live in
`common.py` — change them there, never by copying a constant into a script.

## What this repo is
A charity/grant project: an open method plus a small reusable kit that turns local soil into
reinforced, thermally massive walls, with a solar system that powers the build and then stays as
the village mini-grid. Read MISSION.md (v0.3.1) and GRAVEYARD.md first.

## The core idea (do not lose it again)
The wall is **cast flat in a pit dug from the site's own soil and tilted up.** The pit is the form; the grid is rebar + lift frame + optional cure heater. Read MISSION §0 and §1.

## Do not regress (the v0.2 and v0.3.1 corrections)
- Binder is fired in a **batch kiln**, not in the wall. The grid is plain rebar.
- The kit supports **both binders**: calcined clay (kaolinite-rich soils, scarce cement) and
  6–8% cement (everywhere else). Only the kiln and mill are binder-specific.
- CSEB **is** load-bearing; do not claim otherwise.
- The binder saves hundreds, not thousands, per house. Don't pitch it as the cost advantage.
- It is a **charity** deployed **through partners**. No venture framing.
- `earth-panel/` (in-situ grid firing, cooldown injection) is a **research branch**, not the kit.
- Steel capacity is **limited by the earth crushing** (`common.flexural_capacity`), not As·fy·0.9d.
- Lift checks use the **moist** panel, a 1.5 margin on cracking, and a separate breakaway
  (suction) case. Lift from the steel, never from the earth. Openings go between panels.

## The rock direction (v0.4 candidate — read `rock/ROCK_OPTIONS.md`, `making-system/BRICK_PANEL.md`)
The founder wants **solid rock, not compressed or printed earth**. The lead is printed, fired
cellular clay units, ground flat, dry-stacked with no mortar, clamped by post-tensioned rods into
panels, and tilted up. The compacted-earth kit below stays as the fallback until Phase R decides.
- R0. **Phase R bench tests** (BRICK_PANEL.md §9): fire home clay; print, fire, grind units;
  dry-stack column seating loss; one panel tilted and broken; thermal test.
- R1. **Dome/cone roof** of fired units over a 16–20-gon: thrust, ring beam, rain skin. Extend
  `form_check.py` with thrust.
- R2. **Unit geometry files:** parametric print paths (universal, rod-end, insert, corner,
  sill, lintel) with per-axis shrinkage scaling; a die design for the universal unit.
- R3. **Fibre-hood kiln + husk burner** sized for 0.5–1 t per firing (merges with task 12).
- R4. **Grinding jig:** reach ±0.5 mm and 0.2 mm flatness; field rate per unit.
- R5. **Polygon connections:** panel-to-panel at the folds, ring beam, plinth for a round plan.

## Task list (priority order)
0. ~~**Tilt-up detailing**~~ — v0.1 done: `making-system/TILTUP_DETAILING.md`; `tiltup_check.py`
   now covers breakaway suction, openings, hoist/setting loads and wind while braced. Remaining:
   base shear/uplift at the plinth, out-of-plane capacity of the finished wall, member sizes
   from an engineer, surface-grid variant for openings (task 14).
1. **Phase A protocol** in `chemistry/`: every test in MISSION §8 (incl. beam bending at lift age, pull-out + insert proof load,
   Roman hot-mix and its late-slaking expansion check, erosion), sample prep, kiln schedule,
   cube casting at 10%/15% binder and 6–8% cement, curing, lab submission, pass/fail thresholds
   (propose a minimum compressive strength with a cited basis). Add a results template.
2. **Replace [TO-VERIFY] with real quotes** in `bom/`: US prices for the Phase A and demo kit;
   one target region's prices for the village kit (solar, LFP, rebar, roofing, activator, labor).
   Update `costs_estimate.py` from the quotes.
3. **Batch kiln design** in `making-system/`: chamber size, insulation, element power (fits a
   ~20 kW array's midday output), controller, throughput (kg/day), safety.
4. **Training package** in `training/`: safety (kiln, caustic activator, milling dust), build
   manual, field QA (drop test, cube tests), written for local crews.
5. **Partner criteria + evidence pack** in `partners/` and `grant/`: what a partner provides
   (site, crew, incumbent cost per house and per connection), MOU template, and a funder
   evidence pack ordered as: strength number, demo, partner letter, cost comparison.
6. **Site climate battery sizing** in `energy-system/`: size storage to the cloudiest week using
   real solar data for a target site.

7. **Durability detailing** in `making-system/`: plinth/footing that stops wicking, roof overhang,
   galvanized grid spec and cover depth, joint sealing, render and maintenance schedule.
8. **Mini-grid sustainability** in `energy-system/`: battery/inverter replacement fund at 10–15
   years; pay-as-you-go tariff model a partner can run.
9. **Roman binder protocol** in `chemistry/`: quicklime hot-mix safety, lime:calcined-clay ratios,
   warm-cure schedule via the grid, crack self-healing test (crack cubes, wet, re-test).

10. **Field soil kit** in `chemistry/`: jar test, shrinkage box, ribbon/ball tests with photos;
    calibrate thresholds in `data/materials.json` against Phase A results; replace the Hot Springs
    placeholder soil in `sites/hot_springs_ar.json` with real test data.
11. **Grid material spec**: galvanized baseline, stainless at connections, corrosion-coupon test;
    keep the rule that each panel stands as plain earth under gravity.

12. **Husk-fired kiln** in `making-system/`: burner that holds 600–700 °C (clay + husk ash in one
    burn), feed rate, smoke control, ash handling; confirm Arkansas husk supply and price.
13. **Grow the library**: add materials (fuels, pozzolans, local limes) and sites as data, never as
    code branches. Every new site file must run clean through `site_profile.py`.

14. **Surface-grid (exoskeleton) detailing**: anchor-leg spacing and material, lift at ~0.90 of
    height, insulation under the grid for warm cure, interior vs exterior face choice, lime-plaster
    cover option. Extend the surface-grid section of `tiltup_check.py` for openings.

15. **No-dig routes** (MISSION §15): Route A procedure (tiller, mellowing, wire cut, steel on top,
    lift at ~0.6); Route B literature review (electrokinetic stabilization of clays with calcium and
    silicate — what strengths are actually reported), electrode layout, anode material, gas and pH
    management, the bench-box protocol. Don't let the pit route crowd these out again — the
    founder's original concept is no-dig.

16. **3D printing**: document WASP's published mixes and results; compare printed vs compacted
    earth; evaluate a partnership (printed domes/roofs + tilt-up walls) rather than competing.

17. **Print-and-tilt printer** (`printer/PRINTER_CONCEPT.md`): follow the staged build — hand-towed
    shoe and density gate first, then hot-mix dosing, ribbed panel, motorized gantry, tiller head.
    Write the CNC path generator (lifts, ribs, voids) as data-driven like `site_profile.py`.

## Standing rules
- Every number is sourced, computed in a script, or tagged [TO-VERIFY]/[TO-MEASURE].
- Every failed gate goes to GRAVEYARD.md with the arithmetic that killed it.
- No fundraising claim ahead of evidence.
