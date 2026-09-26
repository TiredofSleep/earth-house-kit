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

## Overturned (kills that were wrong)

| idea | wrongly killed by | what overturned it |
|---|---|---|
| Tilt-up earth panels cast flat in the ground | an unchecked one-liner: "earth is weak in lift tension" | `tiltup_check.py`: 0.30 MPa with the pick at ~0.71 of height (moist panel, ×1.5 impact) vs ~0.3–1.0 MPa cracking strength; rebar carries 3.0–5.7× the lift. Now the core of the kit. |
| Relief cavities + injection (the founder's no-dig concept) | not killed — dropped in v0.2 when the binder moved to the kiln, and never put back | revived in §15 Route B as electrode wells, feed/drain points, and shrinkage relief for electro-osmotic consolidation |
