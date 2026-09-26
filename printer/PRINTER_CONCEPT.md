# PRINT-AND-TILT — a compaction printer for earth panels
### Concept v0.1. Numbers in `print_check.py` (run from the repo root). Everything [TO-MEASURE] until built.

## The idea in one line
Don't extrude wet mud upward like everyone else. **Build the panel flat, on its steel grid, in the
casting bed, by laying and compacting thin lifts of near-dry mix — then tilt it up.**

## Why extrusion is the wrong move for earth
Extrusion needs a wet, soft mix so it can pass through a nozzle. Wet earth is weak when dry,
shrinks and cracks (hence the straw), and can't carry the next layer until it dries — so print
speed is set by drying, not by the machine. And steel can't easily run across stacked layers.

## What this printer does instead

| problem | extrusion printers | print-and-tilt |
|---|---|---|
| **strength** | wet, uncompacted, lower density | **compacted at optimum moisture** by a floating vibrating shoe — rammed-earth density [TO-MEASURE] |
| **waiting to dry** | each layer must stiffen first | **none**: compacted earth stands up immediately (why rammed-earth forms come off right after ramming); flat panels don't stack height anyway |
| **drying the panel** | air only | **quicklime hot-mixed at the head** binds 24–44% of the mix water chemically or boils it off within hours, and heats the lift for the lime-pozzolan reaction — the way road crews dry wet clay |
| **steel** | hard to place across layers | **grid laid on the bed first**, printed onto; it ends up on the bottom face = the interior face after tilting (exoskeleton, anchors) |
| **stiffness per kg** | solid walls | **printed ribs**: 3 in skin + ribs to 8 in = ~30% less earth, same stiffness, 40% lower lift stress; ribs to 12 in = 3.5× stiffer for tall walls |
| **insulation** | straw in the mix | **rice husk packed between the ribs**, lime-capped: thermal mass inside, insulation outside |
| **curing** | ambient | **electrified bed**: the grid heats the panel (warm cure) and, as the cathode over a sand drainage layer, can pull water down and out electrically |
| **relief cavities** | — | the head leaves them as printed voids: shrinkage relief, electrode wells, grout or tie points |

## Machine architecture
- **Frame:** a low gantry on two rails that run along the casting-bed edges (the bed edges *are*
  the rails). Spans an 8×16 ft bed; ~12–18 in of vertical travel. Steel tube, V-wheels.
- **Head:** hopper → auger feed → water/quicklime dosing at the outlet (hot mix happens here) →
  **floating vibrating compaction shoe** (a stripped-down plate compactor on a spring suspension),
  plus retractable pins to leave the relief cavities.
- **Why the shoe floats:** like a road paver's screed, the shoe rides on the mix. The gantry only
  tows and lifts it, so the frame never has to resist the compaction force — which keeps the frame
  light and cheap.
- **Tool changer:** the same gantry can carry a **tiller head** over native ground. That makes it
  the no-dig machine too (MISSION §15 Route A): spread binder, till in place, compact, press the
  grid, wire-cut, tilt — with one frame.
- **Power:** motors + vibrator ~1–3 kW; runs off the kit's solar system during the day.
- **Control:** open-source CNC controller; the "print" is a simple raster of lifts plus rib and
  void paths.

## Throughput
Head capacity ~2.7 m³/h (≈6 panels/h). **The mixer is the bottleneck:** a 350 L pan mixer feeds
~1 m³/h ≈ 2 panels/h. A house's 17 panels of material is a day or two of mixing, versus 4–6 crew
days for the pit route. Curing and tilting are unchanged.

## Rough cost [TO-VERIFY with quotes]
Frame and rails $1.5–4k · motors, drivers, controller $0.8–2.5k · hopper and auger feed $0.5–1.5k ·
floating shoe (repurposed plate compactor) $0.5–1.5k · dosing and sensors $0.3–1k → **~$3.6–10.5k**,
reusable across villages, replacing forms and most of the spreading/compacting labor.

## Build it in stages (don't motorize first)
1. **Hand-towed shoe on rails** over a 4×8 ft test bed: does a floating vibrating shoe reach
   rammed-earth density in 5 cm lifts? Core it and measure. **Gate.**
2. **Hot-mix at the outlet by hand:** dose quicklime and water at the pour; log temperature and
   moisture of each lift over 24 h. **Gate.**
3. **Ribbed panel:** form ribs with simple guides, cure, tilt, and check cracking against
   `print_check.py`.
4. **Motorize X/Y**, then add the auger feed and rib/void paths.
5. **Tiller head** for the no-dig route.

## Kill-conditions
- Shoe-compacted density or strength falls >30% below pit-route panels → change to a tamping
  (ramming) head before building anything else.
- Hot mix sets faster than lifts can be placed (cold joints between lifts) → reduce quicklime,
  or scarify and wet between lifts.
- Ribs crack at the skin junction during the tilt → add fillets or run grid bars up into the ribs.

## Relationship to WASP
WASP prints tall walls and domes by wet extrusion; this prints flat panels by compaction and
tilts them. Different trade-offs. Their printed domes may still be the best earth *roof* in dry
climates — worth a partnership conversation, not a race.
