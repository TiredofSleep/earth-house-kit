# NSF SBIR Project Pitch — DRAFT
### For seedfund.nsf.gov. Paste each section into the matching box of the online form.

> **Before submitting:**
> - Check the current form's section names and character limits on seedfund.nsf.gov. This draft
>   assumes 3,500 / 3,500 / 1,750 / 1,750 characters including spaces;
>   `python business/pitch_check.py` counts them.
> - Fill every `[FILL: …]`.
> - **Eligibility:** NSF SBIR needs a for-profit US small business (<500 employees, majority
>   US-owned). The PI must be primarily employed by it (>50%) at the time of award. Form the company
>   (LLC or C-corp) first.
> - **Topic:** pick the closest current topic, likely Advanced Manufacturing (building materials /
>   robotics) or Advanced Materials. Confirm on the portal.
> - Every performance number in this draft is **modelled**, not measured. It says so, and that is the
>   point: Phase I measures them.

**Proposed title:** Mortarless, post-tensioned building systems from functionally graded fired-clay
units made of local soil and rice-husk fuel

**Company:** [FILL: company name, LLC/C-corp], Malvern / Hot Springs, Arkansas
**Technical contact / PI:** Brayden Sanders, [FILL: email, phone]

---

## 1. The Technology Innovation

Masonry lost to wood and steel framing not on performance but on labour: mortar, skilled masons, and curing time. Fired clay is non-combustible, rot- and termite-proof, and lasts centuries, but a US brick wall needs many hours of skilled labour per square metre. We propose a manufacturing system that removes mortar and site masonry entirely. It turns local clay and agricultural waste into precision building components that assemble like a kit.

The innovation has four linked parts, none demonstrated together before:

1. Functionally graded fired-clay units made in one pass by die extrusion and paste 3D printing from a single site clay. Each has a dense outer skin fluxed with recycled glass cullet (low absorption, frost resistance), an insulating core whose micro-pores come from burned-out rice husk, dense load-bearing rims, and a breathable interior face. Heat-flow modelling predicts U ≈ 0.42 W/m²K for an 8 in wall at ~104 kg/m², against ~2.7 for solid earth walls.

2. Mortarless dry-stack panels. Fired units are ground flat (±0.5 mm), dry-stacked by a gantry robot, and clamped by post-tensioned rods into storey-height wall panels, then tilted up. Nothing cures: a panel can be assembled, tensioned and erected the same day. Every rod and wedge stays inspectable and replaceable.

3. A post-tensioned ribbed dome from the same units. Deep ribs carry the thrust, thin graded webs span between them, and one stainless tendon per rib clamps the joints and resists wind uplift. Thrust-line (safe-theorem) analysis predicts it passes 50 m/s wind, unbalanced snow and 0.3 g lateral load with 35% less clay than a solid shell.

4. Design-to-kit software. A house design file becomes the full parts list, fabrication routing (die or printer), steel, fuel and truckloads, plus automated structural checks.

Firing uses rice husk, a farm residue, in efficient kilns (0.9–3 MJ/kg fired). The factory's machines run on solar in daylight while the kiln fires on husk overnight.

The closest precedents each solve only part of this: ground clay blocks set with adhesive, post-tensioned concrete-block walls, mortared prefabricated brick panels, and printed concrete that is cement-heavy. Our literature review found no tested load-bearing system of printed or extruded, fired, graded, dry-stacked, post-tensioned clay units. The knowledge gaps (graded-body co-firing, dry-joint prestress loss, full-panel behaviour) are the research risk this project addresses. Modelled cost for a 322 ft² shell kit is ~$20–40/ft², against $35–77 for structural insulated panel (SIP) shell kits.

## 2. The Technical Objectives and Challenges

Phase I answers one question: can graded fired-clay units from one local clay be made precisely and consistently enough to form mortarless post-tensioned panels that behave as our models predict? Objectives and pass/fail targets:

O1 Graded units. Co-extrude or co-print three zones (cullet skin, rice-husk core, dense rims) from Malvern-area clay and fire at 1,000–1,080 °C. Targets:
- no delamination or interface cracking in 95% of units;
- adjacent-zone total shrinkage within 10% (relative);
- skin 24-h absorption ≤8% and saturation coefficient ≤0.78 (ASTM C216 severe weathering);
- core thermal conductivity ≤0.30 W/mK;
- unit compressive strength ≥20 MPa.

Challenges: husk lowers shrinkage and cullet raises it; cristobalite from husk ash and quartz inversion can crack units on cooling; husk kilns vary ±50 °C. Approach: bilayer test bars for every zone pair, graded transitions, and firing curves logged by thermocouple.

O2 Precision. Grind fired bed faces to ±0.5 mm height and ≤0.2 mm flatness with a low-cost pass-through diamond grinder, and measure throughput and wheel wear. Unground dry joints reach only ~23% contact and split early, so this is the enabling step.

O3 Dry-joint prestress. On post-tensioned prisms and columns, measure seating and creep loss over 30 days, with and without disc springs (target ≤35% total). Also measure prism strength against unit strength, and joint friction under clamp. Challenge: published data are for concrete block and mortared brick, not ground fired clay.

O4 Full-scale panel. Robotically assemble an 8×4 ft panel (48 units), tension it, and tilt it with a load cell. Test it in bending to failure. Compare cracking, joint opening and capacity with the model.

O5 Validation. Update the open-source structural and thermal models with the measured data. Run a hot-box or heat-flux test of an 8 in graded wall section.

Why this is high-risk R&D: no data exist for any of these properties in this material combination. Graded-body co-firing, dry-joint prestress loss in fired clay, and full-panel behaviour are each unknowns that could independently stop the system. Phase I resolves each with a measured go/no-go, and we will report failures as findings. Phase II would scale to a robotic pilot line, a tested ribbed dome, and fire, impact and freeze-thaw qualification toward code evaluation.

## 3. The Market Opportunity

About a million US single-family homes start each year [FILL: verify with Census], and the structure, foundation and exterior shell is ~40% of construction cost (NAHB 2024: ~$162/ft² total). Our first customers need permanence and resilience at shell-kit prices:
- rural owner-builders and farms (agricultural and storage buildings, often outside residential code, as a first market);
- backyard units and studios;
- homes in tornado and wildfire regions, where a non-combustible, rot-proof masonry shell is a selling point;
- community and residential safe rooms, where FEMA mitigation funding can pay up to 75%.

Modelled pricing: a 322 ft² ribbed-dome shell kit at ~$20–40/ft² ex-works, against $35–77 for SIP shells and $50–100 for log shells. Freight adds ~$1–4k per truckload within 300–1,000 miles.

The business is a regional kit factory sited where firing clay and rice husk meet. Malvern, Arkansas has a century of brickmaking and Arkansas grows the most US rice. The same plant can be replicated across rice regions in AR, LA, MS, MO, TX and CA. A customer designs online; the software prices parts, steel and trucks, and the kit ships as factory-assembled panels. Revenue comes from kits, design and engineering, and assembly training. Our advantage is manufacturing know-how, certification and the design software, not the raw material.

## 4. The Company and Team

[FILL: company name] is a Malvern/Hot Springs, Arkansas startup formed to commercialize this system. Founder and PI Brayden Sanders [FILL: background, relevant experience, % time] has led the concept and built an open engineering repository. It contains structural, thermal, dome, drainage, production-line and cost models, 20+ checked scripts, and sourced literature reviews, all governed by a rule that every number is computed, cited, or flagged for measurement.

Location: Malvern calls itself the "Brick Capital of the World", with three active brick plants nearby, a skilled clay-products workforce, and proven firing clays. Rice-husk supply lies ~90 miles east.

Partners and gaps: we are recruiting
- a university partner in ceramics and structural testing [FILL: e.g., University of Arkansas; confirm];
- a licensed structural engineer as advisor;
- Arkansas MEP for manufacturing feasibility.

A ceramics/materials co-investigator would join as a consultant or through STTR. [FILL: names once confirmed.]

Plan: Phase I at a small bench lab with a test kiln, extruder, clay printer, grinder and load frame, plus university testing. Arkansas's SBIR matching grant would extend Phase I.
