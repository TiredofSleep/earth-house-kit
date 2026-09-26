# Earth House-Kit

**An open method and a small reusable kit for turning a site's own soil into reinforced,
thermally massive walls, plus a solar system that powers the build and then stays behind as the
village mini-grid.** It is a charity project, meant to be deployed through local partners.

Each wall panel is **cast flat in a pit dug from the site's own soil**, around a steel grid. It
cures in place and is then **tilted up**, borrowing concrete tilt-up practice. The binder is a
small fraction of the wall, made from calcined local clay, rice-husk ash with lime (a
Roman-style recipe), or 6–8% cement where that's simpler.

> ## ⚠ Status: research, not a building method yet
> No wall has been built this way. Every number is first-order and tagged `[TO-VERIFY]` or
> `[TO-MEASURE]` until the Phase A tests (MISSION §8) and a demonstration build measure it.
> Structural earth needs review by a licensed engineer. Kilns (~700 °C), quicklime, caustic
> activators, milling dust and suspended panels can cause serious injury. **Nothing here is
> code-approved. Don't build from it.**

## Start here

| read | why |
|---|---|
| [SYNTHESIS.md](SYNTHESIS.md) | **start here:** the whole house, layer by layer, and where each proven idea comes from |
| [business/BUSINESS_CASE.md](business/BUSINESS_CASE.md) | the kit-factory business: costs, prices vs market, break-even, site, sequence |
| [MISSION.md](MISSION.md) | the whole plan: system, energy, costs, tests, kill-conditions |
| [GRAVEYARD.md](GRAVEYARD.md) | ideas that were killed or corrected, with the arithmetic that killed them |
| [making-system/TILTUP_DETAILING.md](making-system/TILTUP_DETAILING.md) | how a panel gets from the pit to a braced wall |
| [rock/ROCK_OPTIONS.md](rock/ROCK_OPTIONS.md) | **every way to turn site soil into rock**, compared: firing, melting, chemistry, biology |
| [making-system/BRICK_PANEL.md](making-system/BRICK_PANEL.md) | **the lead design:** printed fired units, dry-stacked, clamped by rods, tilted up |
| [making-system/KIT_OF_PARTS.md](making-system/KIT_OF_PARTS.md) | **design houses from interlocking parts:** Japanese-joinery locking in fired clay, the dome, the house designer |
| [making-system/ENVELOPE.md](making-system/ENVELOPE.md) | the coat (hung fired siding), the boots (fluted drainage foundation), units graded like bone |
| [printer/PRINTER_CONCEPT.md](printer/PRINTER_CONCEPT.md) | a gantry that compacts panels flat instead of extruding wet mud |
| [HANDOFF_TO_CLAUDE_CODE.md](HANDOFF_TO_CLAUDE_CODE.md) | the prioritized task list |

## The numbers are code

Every headline number in MISSION.md is computed by a script in this repo. `check_numbers.py`
runs all of them and fails if the document has drifted from what they compute.

```bash
pip install -r requirements.txt
python check_numbers.py            # run everything, check MISSION.md against it
python tiltup_check.py             # lift, breakaway, steel, openings, hoist, bracing
python costs_estimate.py           # per house, rig, power, village, Phase A
python site_profile.py sites/hot_springs_ar.json   # soil + local materials -> binder recipes
python rock_options.py             # every rock-making route: wall, energy, fuel, purchases, time
python brick_panel_check.py        # printed fired units: panel, rods, kiln, throughput
python thermal_check.py            # printed cross-sections: U-value, time lag (2-D heat flow)
python form_check.py               # plan shape: floor per panel, wind, self-bracing
python dome_check.py               # fired-unit dome: thrust, ring, thickness, dry build
python dome_thrust.py              # dome under half snow, wind, earthquake (thrust lines, sliding)
python house_designer.py           # every design in houses/: full parts list + checks
python cladding_check.py           # hung fired siding: weight, wind lock, solar gain
python drainage_check.py           # fluted drainage foundation vs NOAA design storms
python business_model.py           # kit prices: plant size, utilization, lean vs baseline, freight, break-even
```

A new site is a new JSON file in `sites/`, and a new material is an entry in
`data/materials.json`. Neither needs a code change. Shared geometry and material values
(panel size, densities, strengths, crew days) live in `common.py`.

## Contributing

- Every number is sourced, computed in a script, or tagged `[TO-VERIFY]` / `[TO-MEASURE]`.
- Every failed gate goes to GRAVEYARD.md with the arithmetic that killed it.
- No fundraising claim ahead of evidence. Say "we could not find it", never "first".
- Run `python check_numbers.py` before committing.

## License

- **Code** (`*.py`): [MIT](LICENSE).
- **Documents and data** (`*.md`, `data/`, `sites/`): [CC BY 4.0](LICENSE-DOCS.md). Use, adapt and
  deploy the method freely, including commercially, with attribution.

Copyright © 2026 Brayden Sanders.
