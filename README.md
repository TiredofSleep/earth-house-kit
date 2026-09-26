# Earth House-Kit

> **[Read the founder packet →](https://claude.ai/artifact/S2nHEWyBa5oJ7Zsk9iFFoP)** the whole idea in plain words, a filterable matrix of every idea explored, and the step-by-step to-do list.

**Houses made from the ground they stand on, built to last for generations.** Local clay is
fired into rock with rice-husk fuel and the sun, shaped into small interlocking parts, and
assembled with no mortar into round homes with fired-clay domes. Every part can be replaced, and
nothing hidden is left to fail.

It is meant to reach people two ways, and both matter:

- **As a business:** a small factory near Malvern, Arkansas, where clay and rice husks meet.
  Software designs each building, from a garden shed to a 5,000 ft² cluster of domes, and prices it
  by tonnes and truckloads. The first product is a **certified above-ground storm shelter**.
  Sales keep the lights on, pay local people fairly, and fund the testing that makes the method
  trustworthy.
- **As a gift:** the method stays **open**: the designs, the test data, the scripts and the
  training. Anyone can build it, and partners and charities can take it wherever people need a safe,
  lasting home and have clay underfoot, without asking permission.

The business makes the gift real, and the gift is why the business exists.

> ## ⚠ Status: research, not a building method yet
> No house, panel or shelter has been built this way. Every number is computed from a model,
> taken from a published source, or tagged `[TO-VERIFY]` / `[TO-MEASURE]`. The next step is to
> fire Malvern clay and measure it. Structures need review by a licensed engineer. Kilns
> (~1,000 °C), lime, silica dust, borates and suspended panels can cause serious injury.
> **Nothing here is code-approved. Don't build from it.**

## Start here

| read | why |
|---|---|
| [**the founder packet (page)**](https://claude.ai/artifact/S2nHEWyBa5oJ7Zsk9iFFoP) · [FOUNDER_PACKET.md](FOUNDER_PACKET.md) | **start here:** the whole thing in plain words, and the staged to-do list from Malvern clay and rice husks |
| [SYNTHESIS.md](SYNTHESIS.md) | the winner design: the whole house, layer by layer, and where each proven idea comes from |
| [IDEAS_MATRIX.md](IDEAS_MATRIX.md) | every idea explored in one chart: pros, cons, verdict (winner / adopt / test / fallback / niche / killed), and the file behind it |
| [GRAVEYARD.md](GRAVEYARD.md) | ideas that were killed or corrected, with the arithmetic that killed them |
| [business/BUSINESS_CASE.md](business/BUSINESS_CASE.md) | the kit factory: costs, prices vs market, break-even, site, grants, and the open-method charity alongside it |
| [business/SHELTER_PLAN.md](business/SHELTER_PLAN.md) | the first product: a certified above-ground tornado safe room |
| [business/NSF_SBIR_PROJECT_PITCH.md](business/NSF_SBIR_PROJECT_PITCH.md) | the draft grant pitch |
| [rock/ROCK_OPTIONS.md](rock/ROCK_OPTIONS.md) | every way to turn site soil into rock, compared: firing, melting, chemistry, biology |
| [making-system/BRICK_PANEL.md](making-system/BRICK_PANEL.md) | the lead wall: cellular fired units, dry-stacked, clamped by rods, tilted up |
| [making-system/KIT_OF_PARTS.md](making-system/KIT_OF_PARTS.md) | designing houses from interlocking parts: Japanese-joinery locking in fired clay, the ribbed dome, the house designer |
| [making-system/ENVELOPE.md](making-system/ENVELOPE.md) | the coat (hung fired siding), the boots (fluted drainage foundation), units graded like bone, coatings |
| [rock/BIO_MATERIALS.md](rock/BIO_MATERIALS.md) | hemp, bamboo, mycelium: where living materials fit (adopt / test / avoid), and the bio-lime interior walls |
| [rock/BAMBOO_PROCESS.md](rock/BAMBOO_PROCESS.md) | feed at death, mineralize inside, seal: a lab process toward 50+ year bamboo |
| [MISSION.md](MISSION.md) | the original plan and its history: system, energy, costs, tests, kill conditions |
| [making-system/TILTUP_DETAILING.md](making-system/TILTUP_DETAILING.md) · [printer/PRINTER_CONCEPT.md](printer/PRINTER_CONCEPT.md) | the original compacted-earth panel branch, now the fallback: pit-cast tilt-up and a compaction gantry |
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
python dome_ribbed.py              # ribbed dome: post-tensioned ribs + thin webs, 35% less clay
python house_designer.py           # every design in houses/: full parts list + checks
python cladding_check.py           # hung fired siding: weight, wind lock, solar gain
python drainage_check.py           # fluted drainage foundation vs NOAA design storms
python business_model.py           # kit prices: plant size, utilization, lean vs baseline, freight, break-even
python production_line.py          # labour per tonne, daylight robotics, payback
python shelter_check.py            # storm-shelter shapes vs ICC 500 wind and missiles; keystone ring
python world_check.py              # what wide adoption would mean: carbon, husks, homes
python ideas_matrix.py             # rebuild IDEAS_MATRIX.md from data/ideas_matrix.json
```

A new site is a new JSON file in `sites/`, and a new material is an entry in
`data/materials.json`. Neither needs a code change. Shared geometry and material values
(panel size, densities, strengths, crew days) live in `common.py`.

## Contributing

- Every number is sourced, computed in a script, or tagged `[TO-VERIFY]` / `[TO-MEASURE]`.
- Every failed gate goes to GRAVEYARD.md with the arithmetic that killed it.
- No fundraising claim ahead of evidence. Say "we could not find it", never "first".
- Build with care: for the people who will live inside, the people who make the parts, and the
  ground the clay comes from.
- Run `python check_numbers.py` before committing.

## License

- **Code** (`*.py`): [MIT](LICENSE).
- **Documents and data** (`*.md`, `data/`, `sites/`): [CC BY 4.0](LICENSE-DOCS.md). Use, adapt and
  deploy the method freely, including commercially, with attribution.

Copyright © 2026 Brayden Sanders.
