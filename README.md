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
| [MISSION.md](MISSION.md) | the whole plan: system, energy, costs, tests, kill-conditions |
| [GRAVEYARD.md](GRAVEYARD.md) | ideas that were killed or corrected, with the arithmetic that killed them |
| [making-system/TILTUP_DETAILING.md](making-system/TILTUP_DETAILING.md) | how a panel gets from the pit to a braced wall |
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
