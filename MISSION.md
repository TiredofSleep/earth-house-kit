# EARTH HOUSE-KIT — Mission v0.3
## Build and power a village from the dirt on site. Charity and grant model.
### Brayden Sanders — Hot Springs, AR. Supersedes MISSION v0.2.

> **The mission.** Give communities that need housing a small reusable kit and an open
> method that turn their own soil into durable, reinforced, thermally massive walls — with a
> solar system that powers the build and then stays behind as the village's mini-grid.
>
> **The discipline.** Every number is first-order and tagged [TO-VERIFY] or [TO-MEASURE].
> Every failed gate changes the plan. Killed ideas go in `GRAVEYARD.md` so nobody rebuilds
> them. v0.1 already killed one design by arithmetic; v0.2 corrects four more things
> (§0). That is the method working, not the mission failing.

---

## 00. WHAT CHANGED IN v0.3 — the core idea, restored

**The point is to make the wall from the ground and stand it up.** v0.2 drifted into
"compress earth into forms," and put tilt-up in the graveyard on an unchecked one-liner
("earth is weak in the tension a crane lift demands"). `tiltup_check.py` overturns that:

| panel | lift stress, pick at top edge | lift stress, pick at ~0.71 of height |
|---|---|---|
| 8×4 ft × 6 in (~860 kg) | 0.82 MPa | **0.28 MPa** |
| 8×4 ft × 8 in (~1,150 kg) | 0.61 MPa | **0.21 MPa** |
| 8×16 ft × 6 in (~3,440 kg) | 0.82 MPa | **0.28 MPa** |

(×1.5 impact factor included.) Stabilized earth cracks somewhere around 0.3–1.0 MPa
[TO-MEASURE], so with correct pick points the panel stays uncracked through the tilt. Even if
it cracks, four #4 bars per 4 ft carry **16×** the lift moment; the earth only has to grip the
bars at ~0.14 MPa. Stress depends on height and thickness, not width, so wide panels are fine
with a spreader bar. **The open questions are cracking and bond — two cheap tests, added to
Phase A.** Precedent that earth elements can be precast and craned exists (prefabricated
rammed-earth walls from Martin Rauch's workshop, e.g. the Ricola Herb Center) [TO-VERIFY];
casting flat and tilting is the new part to prove.

## 0. WHAT CHANGED IN v0.2 (corrections, owned)

1. **The binder is fired in a batch kiln, not in the wall.** v0.1 showed only ~10–15% of the
   clay needs calcining (the binder). Heating a whole wall to fire 15% of it is pointless, so
   the binder is calcined in a small insulated kiln, milled, and mixed with raw soil and a
   one-part activator before compaction. This removes the 133–888 kWh battery, the in-wall
   activator-injection problem, and in-wall calcination shrinkage cracking in one move. The
   steel grid becomes plain rebar (optionally a low-temperature cure heater, 60–80 °C). The
   in-situ grid-firing process stays alive as a research branch in `earth-panel/`.
2. **CSEB overstatement corrected.** v0.1 said compressed stabilized earth block (CSEB) walls
   are non-structural without a frame. That's wrong: CSEB is used for load-bearing walls,
   including multi-storey buildings (the Auroville Earth Institute is the classic example).
   The kit's real differentiators are supply-chain independence, the bundled mini-grid, and
   an optional cement-free binder — not "structural where CSEB isn't."
3. **The binder is not where the money is.** A cement-stabilized wall needs ~17–22 bags of
   cement per house (~$80–670). The calcined-clay binder saves hundreds, not thousands, per
   house; carbon credits on ~0.6–0.8 t CO₂ avoided are worth ~$6–39. The binder earns its
   place where cement is scarce, unreliable, or expensive to truck in, and as a climate story.
   Everywhere else, the kit should use cement stabilization. **The kit supports both binders;
   only the kiln and mill are binder-specific.**
4. **Soil decides the binder.** Calcined clay makes good binder only from kaolinite-rich
   clays (calcined-clay cement research points to roughly ≥40% kaolinite for performance
   near Portland cement) [TO-VERIFY]. Highly weathered tropical soils are often
   kaolinite-rich, which fits many target regions; smectite-rich soils (common in drylands)
   are worse. Every site gets a mineralogy test; failing sites fall back to cement.
5. **The reusable rig is not the big cost.** Labor, roofs, the power system, and the field
   program dominate. Rig reuse saves ~$1k–3.7k per house on the next village.

---

## 1. THE SYSTEM (v0.3) — cast it in the ground, stand it up

1. **Dig a panel-shaped pit** 6–8 in deep beside where the wall will stand. **The pit is the
   form; its soil is the panel.** No formwork, no hauling.
2. **Line it** with a bond breaker (plastic sheet or sand) so the panel releases.
3. **Set the steel grid** on chairs: rebar mesh with a welded perimeter, lift inserts at ~0.7
   of the panel height, and connection plates for joining neighbours and the footing.
4. **Backfill with the pit's own soil** mixed with binder and activator; **vibrate and
   compact in lifts** around the grid.
5. **Cover and cure.** Ambient in warm climates, or run current through the grid for a
   60–80 °C cure (~22–43 kWh per 4×8 panel) — the heater idea survives at low temperature.
6. **Tilt it up** with an A-frame or gantry and a hoist (an 8×4 ft panel is ~860 kg; no crane
   needed), set it on a footing with starter bars, brace it, weld or bolt it to its neighbours,
   tie the tops with a bond beam and roof.

- **Bulk:** the pit soil, compacted around the grid. Zero firing energy. This is the structure
  and the thermal mass.
- **Binder:** 10–15% of the clay, sun-dried, fired to ~700 °C in a batch kiln by day
  straight off the solar array, milled fine, mixed in with a one-part activator. Fallback:
  6–8% cement where the soil fails the mineralogy test or cement is cheap.
- **Power:** one ~20 kW array + ~50 kWh LFP battery. Build phase: runs the kiln, mill, mixer,
  and tools. Run phase: becomes the village mini-grid.
- **Finish parts:** roof, doors, windows, wiring, water catchment — dirt can't make these.
  In dry climates, earth vaults (the Nubian Vault technique) can replace the shipped roof.

---

## 2. ENERGY (see `system_sizing.py`)

| design | energy per house | status |
|---|---|---|
| fire the whole wall in place | ~12,600 kWh, ~28 months on 3 kW | **KILLED (v0.1)** |
| fire 15% binder inside the wall | ~1,900 kWh, plus big battery, injection, cracking | **SUPERSEDED (v0.2)** |
| **batch-kiln binder, 10–15%** | **~600–1,800 kWh** | **baseline** |

- On a 20 kW array (~60 kWh/sunny day available to the kiln): **10–29 sunny days of firing per
  house**, 100–300 sunny days for a 10-house village. A second kiln plus ~10 kW of panels
  roughly halves that; panels are the cheapest lever in the kit.
- **Run phase:** each finished house needs ~3.1 kWh/day because thermal mass handles heating
  and cooling. The array makes ~80 kWh on a sunny day, enough energy for ~26 houses; the
  battery is the real limit — 50 kWh gives 10 houses ~1.3 days of autonomy. **Size the battery
  to the cloudiest week of the site, not the average day.**

---

## 3. SHIPPING (see `shipping_manifest.py`)

| scenario | ships | containers |
|---|---|---|
| ship everything (rig + power + 10 houses of finish parts) | ~21 t, ~75 m³ | **3 × 20 ft** |
| **regional sourcing** (ship the rig; buy solar, battery, rebar, roofing, activator in-country) | ~2.4 t, ~11 m³ | **1 × 20 ft, room to spare** |

Regional sourcing is the default: cheaper freight in a volatile 2026 market (the Drewry World
Container Index hit $4,639 per 40 ft in July 2026, its highest since September 2024), local
warranties on batteries and inverters, and no corrosive-goods paperwork for the activator.
**The honest slogan is "a village in one crate" — the rig ships; the commodities are bought
near the site; the walls ship as zero.**

---

## 4. COSTS (see `costs_estimate.py`; 2026 USD, first-order, [TO-VERIFY] with real quotes)

| bucket | range | note |
|---|---|---|
| per house, excluding roof | $1,450–5,200 | labor is the largest swing item |
| roof per house | $900–2,000 steel · $150–500 earth vault | biggest per-house lever |
| reusable rig (once) | $8,600–32,500 | kiln, mill, forms/press, QA kit |
| power system (village keeps it) | $14,000–39,000 | ~17–19% of the budget, becomes the mini-grid |
| field program | $12,300–39,500 | site lead, engineering, lab tests, local review |

**First 10-house village (+15% contingency):**

| scenario | village total | per house (incl. power) |
|---|---|---|
| steel roofs, regional sourcing | $73k–225k | **$7.3k–22.5k** |
| steel roofs, ship everything | $86k–254k | $8.6k–25.4k |
| earth vaults, regional sourcing | $65k–208k | $6.5k–20.8k |
| next village (rig reused) | $64k–187k | $6.4k–18.7k |

**What the number means:** a permanent, reinforced house with a share of a solar mini-grid,
somewhere in the mid-four to low-five figures. Whether that is good depends on one comparison
only a partner can supply: **what they pay today per permanent house, plus what they pay per
electricity connection.** [TO-VERIFY per region.] The kit wins if it matches that on cost and
beats it on supply-chain independence or power.

**Phase A (the gate everything hangs on): $1,900–5,800.** Details in §8.

---

## 5. BUSINESS vs CHARITY — the assessment

### As a business: weak
- **Customers can't pay or pay slowly.** Buyers are NGOs and governments (track-record
  procurement, 6–24 month cycles, budgets down about a third since 2023) or low-income
  households (can't pay $6–20k upfront without housing microfinance).
- **Thin, lumpy margins.** Integrating a $65–225k village kit at 15–25% margin is $10–50k
  gross per deal, a few deals a year, with heavy field support and structural liability.
- **No moat.** The techniques are established and the work is published openly (which makes
  it prior art). Fine for a charity; fatal for a venture.
- **Where a business *can* exist:** local, in-country builders who sell houses with
  microfinance. That is exactly who the housing-innovation accelerators fund — Habitat's
  ShelterTech has required applicants to be for-profit with a validated customer base.

### As a charity: the right shape, run lean
- **The public good is the open method** — process, test data, QA protocol, training
  package, kit bill of materials. The leverage is in partners who deploy it.
- **Deploy through partners, don't run field operations from Arkansas.** Local NGOs and
  builders implement; some can become social enterprises that access for-profit innovation
  money using the open method. The charity stays a charity; the method still scales.
- **Headwind to plan around:** international humanitarian funding contracted by nearly a third
  since 2023, with a 20% drop in 2025 alone; the US and Germany account for nearly nine in ten
  dollars lost, while Gulf donors increased giving. A newcomer competes for a smaller pot, so
  **lead with evidence: a measured strength number, a built demonstration, and a cost-per-house
  comparison from a partner.**

### Recommended structure
1. **Start under a fiscal sponsor or as a small 501(c)(3)** (the streamlined IRS 1023-EZ
   route is available to small organizations) [TO-VERIFY current fee and eligibility]. An
   independent board of at least three is what funders expect.
2. **Founder-volunteer until a pilot is funded.** No salaries in Year 1.
3. **Optional, only if a commercial arm is ever wanted:** SBIR was reauthorized in April 2026
   through September 2031, and NSF Phase I awards now go up to $305,000 — but SBIR is for
   for-profit small businesses with a commercial market, not charities. If an existing LLC
   ever pursues it (e.g., for US low-carbon earth building), keep it arm's-length from the
   nonprofit: written conflict-of-interest policy, independent board approval of any dealings.

---

## 6. FUNDING PLAN (charity)

| stage | budget | typical sources | gate to pass |
|---|---|---|---|
| **Year 1a — Phase A** | $1.9k–5.8k | self-funded, crowdfunding, local Rotary/community grant | strength + mineralogy (§8) |
| **Year 1b — demonstration** | $10k–40k | small foundation grants, crowdfunding, in-kind | a built, tested, engineer-reviewed structure |
| **Year 2 — pilot village** | $65k–225k | private/corporate foundations, Rotary Global Grants, Gulf-linked donors, innovation challenges, the partner's own program budget | cost/house ≤ partner's incumbent, or clearly better on supply chain or power |
| **Year 3+ — scale** | via partners | partners' budgets and local social enterprises | replication by someone other than you |

Year 1b budget: demo structure $5–20k, professional engineer review $2–8k, entity and
insurance $1–4k, documentation $0–2k. The demonstration should be the founder's own
earth-sheltered homestead build (House #0) or a small accessory structure on the same land —
check local permit exemptions for small structures first. [TO-VERIFY locally.]

**What every funder will ask for, in order:** the strength number, the demo, the partner
letter, the cost-per-house comparison. Build them in that order.

---

## 7. FENCES AND KILL-CONDITIONS

- **The wall stores no recoverable energy.** "Builds and powers a village" means the shipped
  solar runs the build, then runs the homes, and thermal mass keeps the homes' demand low.
- **Kill / pivot conditions:**
  - Phase A fails on both binders → the soil can't make structural walls this way; stop.
  - Calcined-clay binder fails but cement works → keep going, cement-stabilized kit.
  - Cost per house can't approach a partner's incumbent → publish the open method only.
  - No partner will deploy after a successful demo → publish, don't self-deploy abroad.
- **Safety:** ~700 °C kiln, caustic activator (even the one-part form needs gloves and eye
  protection), dust from milling (respirators). The training package is part of the kit.
- **Engineering sign-off:** structural earth needs a licensed engineer's review at the demo
  and in-country. ASTM E2392 (earthen wall systems) is the natural starting reference.
- **Partner countries:** a US charity working abroad must screen partners and locations for
  sanctions compliance; established partner NGOs usually handle this well.

---

## 8. PHASE A — the $2–6k test that decides everything

Two variables, tested separately so a failure points at its cause:

| test | question |
|---|---|
| **mineralogy (XRD/TGA, 3 samples)** | is the native clay kaolinite-rich enough to make binder? |
| **swell test** | does the soil expand badly when wet (smectite)? |
| **control: commercial metakaolin + native soil** | does the native soil work as the bulk? |
| **native calcined clay + native soil** | does the native clay work as the binder? |
| **cement 6–8% + native soil** | the fallback baseline — always run it |
| **beam bending (modulus of rupture)** | will a panel stay uncracked during the tilt? (need ≥ ~0.3 MPa) |
| **rebar pull-out** | does the earth grip the steel? (need ≥ ~0.14 MPa with margin) |
| **Roman binder: calcined clay + quicklime, hot-mixed** | does the lime-pozzolan version reach tilt strength, and do cracked cubes self-heal when wetted? |
| **erosion spray + wet–dry cycling** | how fast does the panel face wear, per binder? (durability, §10) |
| **jar test + shrinkage box** | what is the home site's sand/silt/clay split, and does it need sand blended in? |
| **galvanized vs plain bar in wet earth** | corrosion coupons buried in cast cubes, inspected at 6 and 12 months |
| **surface-grid pull-off** | cast bars half-buried on a cube face, with and without anchor legs; pull them off |
| **electrokinetic box** (Route B, <$200) | tub of red clay, two electrode rows, lime water at the anode, 12–24 V from a small solar panel for 2–4 weeks; measure water removed, pH and strength across the section, temperature, energy used |
| **till-in-place slab** (Route A) | till binder into a 4×4 ft patch of native ground, compact, cure, wire-cut, pull cores for strength |
| **printed-mix control** | cast cubes of a WASP-Gaia-style mix (soil + rice straw + husk + ~10% lime) beside compacted panels; compare strength and shrinkage |
| **floating-shoe compaction** | hand-tow a vibrating shoe over 5 cm lifts on a test bed; core it: density and strength vs the pit route |
| **rice husk test burn** | burn husks at 600–700 °C in the test kiln; ash colour, lime + ash cube strength vs lime + fired clay |

Fire native clay samples in a small test kiln (a 120 V model runs off an ordinary outlet or
an existing home inverter), mill, cast cubes at 10% and 15% binder, cure, and send ~40 cubes to
a materials lab for compressive strength. Red clays in the southeastern US are often
kaolinite-bearing — a hopeful sign for the home site, confirmed only by the XRD. [TO-MEASURE]

---

## 10. DURABILITY — how long it lasts, and the Roman lesson

**Honest lifespans (with the detailing below):**

| part | expected life | note |
|---|---|---|
| stabilized earth walls | **50–100+ years** [TO-VERIFY per binder] | earth lasts centuries when kept dry: rammed-earth monuments such as sections of the Great Wall, the Alhambra's walls, and Fujian tulou |
| steel grid / rebar | decades — **the wildcard** | earth doesn't protect steel the way concrete does unless lime or cement keeps it alkaline |
| panel joints, lime/earth render | re-seal or re-render every 5–20 years | cheap, sacrificial, planned maintenance |
| steel roof | 25–50 years | earth vaults last longer but need their render kept up |
| solar modules | 25–30+ years | ~0.5%/yr output loss |
| LFP battery, inverters | **10–15 years** | **the village needs a replacement fund** — pay-as-you-go electricity fees are the standard mini-grid answer |

**What kills earth buildings is water.** Earth builders say a wall needs "good boots and a good
hat": a raised, water-resistant plinth/footing so ground moisture can't wick up, and a roof
overhang so rain never runs down the face. Those two details matter more than the binder.

**The Roman lesson (two parts):**
1. **Roman concrete had no rebar.** Modern concrete's main killer is rusting steel; Roman
   concrete worked in compression (arches, vaults, thick walls) and had nothing to rust. The
   kit needs steel to survive the tilt, so protect it: a **galvanized** grid (zinc is fine at the
   60–80 °C cure temperature), ≥2 in of earth cover, an alkaline (lime or cement) binder, and dry
   walls. Non-corroding basalt-fiber bar is an option for the body, but it can't double as the
   heater.
2. **Roman concrete is lime + pozzolan, and calcined clay is a pozzolan.** The Romans even used
   crushed fired brick with lime (cocciopesto). MIT's 2023 work, confirmed at a Pompeii
   construction site in a December 2025 study, showed they **hot-mixed**: dry quicklime blended
   with the ash before water, leaving reactive lime clasts that later dissolve into cracks and
   heal them. So the kit gets a **third binder**: kiln-fired native clay + hot-mixed quicklime.
   It halves the clay you must fire (lime supplies the rest), replaces the caustic sodium
   activator with lime (available almost everywhere), and may self-heal. The costs: quicklime
   is its own handling hazard, and lime-pozzolan cures slower — the grid's warm cure earns its
   keep here. **Self-healing in *earth* panels is unproven; Phase A tests it.**
   **Lime heat (see `lime_heat.py`):** slaking quicklime releases ~0.32 kWh per kg, so a 5–7%
   dose puts ~14–19 kWh into each 8×4 ft panel — enough to lift it ~50–70 °C if none escaped.
   But it arrives as a pulse during mixing and casting, not over the days of curing, and much of
   it escapes first. Realistically it keeps ~4–12 kWh per panel and replaces ~10–50% of the
   grid's warm-cure energy (~70–200 kWh per house), roughly the first day of heating. To keep
   more of it: mix dry, add the water at the pit, compact while warm, cover immediately
   [TO-MEASURE]. The heat was paid for at the lime kiln (slaking returns ~36% of the energy it
   took to make the quicklime), so buy the lime rather than burning your own.

**Grid material — "rebar that rusts like a shipping container" doesn't work inside a wall:**

| option | embedded in damp earth | can be the heater? | verdict |
|---|---|---|---|
| weathering steel (Cor-Ten, what containers are made of) | its protective rust only forms with wet–dry cycles in open air; sealed in a damp wall it rusts like plain steel | yes | **no** |
| plain steel | rusts unless lime/cement keeps it alkaline and the wall stays dry | yes | only with alkaline binder |
| **galvanized steel** | the zinc corrodes first, on purpose, protecting the steel | yes (fine at 60–80 °C) | **baseline** |
| stainless steel | best; several times the price [TO-VERIFY] | yes | connections and splash zone |
| basalt/glass-fiber bar | can't rust | no (doesn't conduct) | body bars where warm cure isn't needed |
| protective current through the already-wired grid (impressed-current cathodic protection) | the solar system pushes a tiny current that stops corrosion; used on bridges and marine concrete | — | research option, not baseline |

**Better configuration: the grid on the surface, not inside (the exoskeleton).** Lay the grid on
the pit floor so it ends up half-embedded in one face of the panel. Rust then pushes the steel
*away* from the wall instead of cracking the earth from inside, and the steel stays visible,
inspectable, and repaintable. `tiltup_check.py` (surface-grid section):

| lift point | steel face | earth-only face |
|---|---|---|
| top edge | 0.82 MPa | 0.00 |
| **0.90 of height** | **0.65 MPa (steel carries it, 9× margin)** | **0.03 MPa** |
| 0.71 of height | 0.29 MPa | 0.28 MPa — too close to cracking with no steel |

- **Lift near the top edge (~0.90), not at 0.71.** The pit floor is the face that stretches during
  the tilt, so the steel is exactly where it's needed; lifting high keeps the steel-free face
  almost unstressed.
- **Anchors, not grip.** A half-buried bar needs ~0.48 MPa of grip in the lift — too much to trust
  to earth. Weld short anchor legs (stainless or galvanized, 2–3 in deep) every foot or so. They
  are the only buried steel, small enough that stainless is affordable.
- **Pick which face gets the steel by where you cast.** Tilting about the footing turns the pit
  floor face toward the side the panel lay on: cast inside the footprint and the steel faces the
  interior; cast outside and it faces out.
  - **Interior face (recommended):** dry indoor air, very slow rust, paintable; or bury it under a
    lime plaster, which keeps it alkaline and gives a reinforced-plaster skin — steel or polymer
    mesh bonded to adobe and masonry faces is an established earthquake retrofit.
  - **Exterior face:** now weathering steel (Cor-Ten) actually works — it gets the wet–dry cycles
    its protective rust needs. Keep it off wet soil at the base, and expect rust streaks down the
    wall.
- **Cure heat:** with the grid on the pit floor, heat goes into the ground as well as the panel —
  lay insulation board or dry sand under the grid so the warmth goes up.

**Design rule (the Roman lesson again): each panel should stand as plain earth under its own
weight.** Steel is for the tilt, earthquakes, and connections — insurance, not the thing
holding the wall up. If the steel ever fails at year 70, the wall shouldn't.

---

## 12. SOILS — clay isn't required (see `site_profile.py`, `data/`, `sites/`)

**The best wall soil is sandy with some clay** — roughly 8–20% clay, the rest sand, gravel and
some silt [TO-VERIFY per guide]. Pure clay shrinks and cracks; it gets sand blended in. And
**the binder clay doesn't have to be the wall soil**: the kiln needs only 5–15% of the mass as
kaolinite-rich clay, which can be hauled in while the bulk comes from the pit.

| soil | walls? | binder, best first |
|---|---|---|
| sandy / desert | yes, compacts well | cement; or lime + a pozzolan |
| sandy-clay, laterite, red clays | yes (blend if >20% clay) | Roman lime + fired clay; geopolymer; lime |
| volcanic soil / ash | yes | **lime + the local ash — the original Roman recipe** |
| rice-growing silts | yes, with care (erodible) | lime + rice husk ash (a strong pozzolan) |
| expansive clay (swells, "black cotton") | no — blend ≥50% sand or dig elsewhere | lime for footings and paths |
| salty / sulfate soils | test first | geopolymer; cement and lime can be attacked |
| topsoil / organic | **never** | strip it, dig deeper |

**The analysis is data, not code.** `data/materials.json` is the materials library (soils rules,
pozzolans, binders, kiln fuels with heating values, ash yields, firing windows, hazards).
Each site is one file in `sites/` (soil test results + what's locally available). To take the
kit somewhere new, copy a site file, fill in the jar test and the local materials, and run
`python3 site_profile.py sites/<new_site>.json`. It returns the bulk-soil verdict, binder
recipes ranked (confirmed first, lab-dependent ones flagged), a kiln fuel plan with fuel mass
per house, hazards, and the site's TO-MEASURE list. Nine example sites ship with the repo.

**Field soil kit (cheap, part of the rig):** jar test (shake soil in water, read sand/silt/clay
layers), shrinkage box (clay behaviour), ribbon and ball tests, plus lab mineralogy only for the
clay that goes in the kiln.

---

## 13. THE ARKANSAS RECIPE — red clay + rice husks + lime

Arkansas is the largest rice-growing state in the US, and husks change the kiln more than the
binder:
- **Husks are fuel:** ~3.6–4.4 kWh per kg burned. A husk-fired kiln co-firing clay at ~650–700 °C
  needs roughly **130–570 kg of husks per house (~1–6 m³, a pickup load or two)** instead of
  ~300–940 kWh of solar electricity.
- **Husk ash is a pozzolan:** 15–22% of the husk's weight comes out as ash, and it's reactive if
  the burn stays ~500–700 °C — the same window as firing the clay, so one burn does both.
- **The clay becomes a bonus, not a dependency.** If the XRD says the red clay isn't
  kaolinitic, the recipe still works: **rice husk ash + hot-mixed quicklime**, with the ash as the
  whole pozzolan (~3–7 t of husks per house, lots of surplus heat to fire clay for the next house
  or dry soil).
- **The build stops waiting for sunshine.** With a husk-fired kiln, the solar array only has to
  run the mill, tools, and the finished village — roughly half the array [TO-VERIFY].
- **Hazards:** never overburn (above ~800 °C the ash turns to crystalline silica, a lung hazard,
  and loses reactivity); grey or white ash is good, black means unburned carbon; respirators for
  ash dust; smoke control on the burner.
- **Portability:** rice is grown across South and Southeast Asia, West Africa, and Latin America,
  and about a fifth of harvested paddy by weight is husk — on the order of 150 million tonnes a
  year worldwide [TO-VERIFY]. "Farm waste fires the kiln and becomes the cement" travels.

---

## 14. PRECEDENTS, WHAT'S NEW, AND THE LONGEVITY CLAIM

**Closest cousins (so nobody can say we didn't look):**
- **Concrete tilt-up** — cast flat, tilt up, brace; about 15% of North American commercial and
  industrial buildings. The lifting, bracing, and connection engineering is mature; borrow it.
- **Prefabricated rammed earth (Martin Rauch / Lehm Ton Erde)** — the Ricola Herb Center (2014)
  used ~670 factory-made earth elements of 4–6 t each, set like giant stones on mortar, made from
  local marl with volcanic tuff added for durability. His later unstabilized (cement-free)
  prefab system won a New European Bauhaus prize and claims ~50% lower cost and ~65% less
  production time than conventional rammed earth.
- **Rice husk ash, calcined clay, lime-pozzolan binders** — each studied and used on its own.

- **3D-printed earth (WASP, Italy)** — the closest thing to this whole mission, and it uses the
  Arkansas recipe. Gaia (2018): a site-soil mix with chopped rice straw, rice husk and 10%
  hydraulic lime, 40 cm walls, ~30 m² of wall printed in about 10 days for ~€900 of materials.
  TECLA (2021, with Mario Cucinella Architects): two synchronized arms, ~200 hours of printing,
  soil + water + rice husk with only ~5% binder, a double dome that is wall, roof and cladding at
  once. WASP pitches a "maker economy starter kit" for local self-build — overlap with this kit is
  real: **partner or reference, don't pretend it doesn't exist.**

**Printing vs tilt-up, honestly:**
- Printing kills formwork and most crew labor, and gives shape freedom — **domes and vaults mean an
  earth roof, which is this kit's biggest cost and crate lever.**
- But extruded earth is wet and uncompacted, so it's weaker and shrinks more (hence the straw);
  printing speed is limited by each layer drying; there's no easy way to reinforce across layers;
  and the printer is a real capital cost [TO-VERIFY price].
- Compacted, stabilized, steel-framed tilt-up panels should be denser and stronger with cheap tools
  [TO-MEASURE side by side]. **Plausible split: tilt-up walls, printed or vaulted earth roof** in dry
  climates; steel roof where rain is heavy (Arkansas).

**What appears new (not found in a quick search; say "we could not find it," never "first"):**
casting flat in a pit dug from the site's own soil, tilting up with a surface-grid exoskeleton,
and firing the binder with farm waste — packaged as an open kit with the power system included.

**Why earth lost in the first place:** not concrete's price — **labor**. Rammed earth is slow,
hand-heavy work, and concrete won on labor and codes. Prefab and tilt-up attack exactly that.

**The longevity claim, stated honestly:**
- Roman concrete has lasted ~2,000 years; modern reinforced concrete is designed for roughly
  50–100 and often fails sooner, mostly because the **steel inside rusts**, not because the cement
  gives out. Survivorship bias applies: we only see the Roman concrete that survived, and it is
  weaker than modern concrete.
- This kit borrows the three longevity moves: lime-pozzolan chemistry that keeps reacting and can
  self-heal; no steel buried where rust can crack it (surface grid + stainless anchors); and walls
  that stand in compression as plain earth.
- **Allowed claim:** "designed to avoid the main failure mode of reinforced concrete."
  **Not allowed:** "lasts longer than concrete" — no one can test 500 years; accelerated erosion,
  wet–dry, and self-healing tests plus historical analogs are the evidence. **Kill-condition:** if
  the erosion spray test shows fast face wear or cracked cubes don't heal, drop the longevity pitch.

---

## 15. NO-DIG ROUTES — drive the steel in, treat it in place, dry it, stand it up

The pit route (§1: dig, mix, backfill onto the steel) is the baseline because every step is
established. The founder's original idea was **no dig**: push the steel into the ground, treat
the soil where it lies, and stand it up. v0.2–v0.3 dropped that and parked the relief cavities
and injection in `earth-panel/`. They come back here. Every route first scrapes off the topsoil
(organic soil never binds) and digs narrow edge trenches for the footing and to free the panel.

### Route A — till in place (established; road builders do this every day)
1. Spread the binder powder (e.g. Roman lime + rice husk ash) over the panel footprint.
2. Till it 6–8 in deep with a rear-tine tiller. In heavy clay, let it **mellow** 1–2 days (lime
   breaks the clods down), then till again with water.
3. Compact with the vibratory plate.
4. Steel: press the grid into the top surface, or drive bars horizontally at mid-depth from the
   edge trenches (they carry ~15 kN·m vs ~1.3–3 needed for the lift).
5. Cover and cure (grid heat or ambient).
6. **Cut it free underneath** with a wire drawn through from the edge trenches — the way a
   potter cuts clay off the wheel — and tilt it up.

With the grid on the **top** face, lift **low (~0.6 of height)**: the bare bottom face then sees
~0.09 MPa while the steel face takes ~0.53 MPa (`nodig_check.py`). Equipment added: a tiller and a
wire saw.

### Route B — electrokinetic (no mixing at all; research track, fits clay best)
Pressure injection fails in clay — clay is too tight for liquid to flow. **Electric current moves
water and ions through clay anyway**, which is how engineers have dewatered and stabilized soft
clays since the 1930s. The driven steel becomes the electrodes:
1. Compact the surface; put a weight on top (sandbags) to consolidate as water leaves.
2. **Auger the relief cavities in rows ~30 cm apart.** They are the electrode wells and the feed
   and drain points, and they give the clay somewhere to shrink as it loses water.
3. **The steel that stays in the panel is the cathode** (negative) — which also protects it from
   rust while current flows. Temporary anodes go in the other row of wells; they corrode, so they
   are sacrificial or pulled out afterward.
4. Feed calcium into the anode wells (lime water or calcium nitrate — **not calcium chloride**,
   which releases chlorine gas at the anode and rusts steel). Optionally feed sodium silicate on
   the cathode side so the two meet mid-panel and gel (an electrically driven version of the
   two-shot silicate grouting used for underpinning) [TO-VERIFY in literature].
5. Run **15–30 V DC straight from a small solar string, no inverter**. At 0.5 V/cm calcium crosses
   the 30 cm in ~3–11 days per pass; water moves toward the cathode ~2 cm/day and is pumped or
   evaporated out of the cathode wells ("dry"); the current warms the soil +2 to +17 °C/day
   ("cure"). Three passes: ~1–5 weeks, **~5–184 kWh per panel** — a wide range the bench test
   must narrow.
6. Wire-cut underneath, tilt low (grid on top) or as the steel layout dictates.

**Honest unknowns (the gates):** published electrokinetic work shows big gains in soft clays, but
often at **foundation grade, not wall grade** [TO-VERIFY]. Treatment is uneven (strongest near
the cathode, acidic near the anode), gas forms at both electrodes, and the energy range is wide.
**Kill/pivot:** if the bench box can't reach wall grade (~2 MPa compressive, ≥0.3 MPa bending),
Route B becomes a footing and floor-slab stabilizer (still valuable) and walls use Route A or the pit.

### Route C — hybrid
Till the binder in (Route A), then run the electrodes (Route B) to push lime into the clay clods,
pull water out, and warm-cure — without extra digging.

---

## 16. PRINT-AND-TILT — the labor killer (see `printer/PRINTER_CONCEPT.md`)

A low gantry builds each panel **flat, on its steel grid, in the casting bed, by compacting thin
lifts of near-dry mix** — not by extruding wet mud upward — then the panel is tilted up.
- **Strength:** compacted, not extruded, so rammed-earth density instead of wet-mix density.
- **No drying wait:** compacted earth stands up immediately; flat panels don't stack height.
- **Self-drying:** quicklime hot-mixed at the head binds or boils off ~24–44% of the mix water.
- **Stiffness per kg:** printed ribs cut ~30% of the earth for the same stiffness, and lower the
  lift stress by 40%; rice husk packed between the ribs makes an insulated wall.
- **Throughput:** the mixer (~2 panels/hour of material) is the bottleneck, not the machine.
- **Same frame, tiller head:** it is also the no-dig machine for Route A.
- **Cost:** ~$3.6–10.5k DIY [TO-VERIFY], reusable. **Build it hand-towed first**; motorize only
  after the shoe proves it can reach rammed-earth density.

---

## 11. BUILD TIME (see `build_timeline.py`)

Crew of ~6, 17 panels per house: **21–37 crew working days per house** (site/footing 3–5,
dig + cast 4–6, tilt/brace/connect 2–4, bond beam + roof 5–10, openings/wiring/water/render 7–12).
The kiln runs ahead of the crew; curing is waiting, not work.

| binder | cure before tilt | one house, elapsed | 10-house village, 2 crews |
|---|---|---|---|
| cement fallback | ~7 days | ~4–6 weeks | ~4–6 months |
| geopolymer | 7–14 days | ~5–11 weeks | ~4–10 months |
| Roman lime-pozzolan | 14–28 days | ~5–12 weeks | ~4–7 months |

House #0 will take longer (first build, learning, testing every step) — plan 3–4 months.
Bigger panels (8×16 ft, five per house) cut tilt and connection work if the lift gear allows.

---

## 9. REPO STRUCTURE

```
earth-house-kit/
  MISSION.md              # this document (v0.2)
  GRAVEYARD.md            # killed and superseded designs, with the arithmetic
  system_sizing.py        # energy: killed / superseded / baseline designs; run phase
  shipping_manifest.py    # ship-everything vs regional-sourcing
  costs_estimate.py       # per house, rig, power, field, village, Phase A
  tiltup_check.py         # lift stress, rebar margin, bond demand for tilt-up panels
  build_timeline.py       # crew days, kiln days, cure waits, village schedule by binder
  site_profile.py         # portable site analysis: soil + local materials -> recipes, kiln fuel, hazards
  data/materials.json     # materials library (soils rules, pozzolans, binders, kiln fuels)
  sites/*.json            # one file per site (home site + 8 examples)
  lime_heat.py            # quicklime slaking heat per panel vs grid cure energy
  nodig_check.py          # no-dig routes: electrokinetic time/voltage/energy, tilt with steel on top
  printer/                # print-and-tilt compaction printer: concept + print_check.py
  chemistry/              # Phase A protocol, lab results, binder choice per site
  making-system/          # kiln, mill, forms/press, compaction, QA protocol
  energy-system/          # array/battery sizing per site climate, village mini-grid
  bom/                    # real quotes by region (replace every [TO-VERIFY])
  training/               # safety, build manual, QA for local crews
  partners/               # partner criteria, MOUs, cost comparisons
  grant/                  # funding pipeline, applications, evidence pack
  earth-panel/            # sibling research branch: in-situ grid firing (not the kit baseline)
```

---

## 10. SOURCES (verify before citing externally)

- Battery prices: BloombergNEF 2025 survey (stationary packs ~$70/kWh; all packs $108/kWh), via
  ess-news.com/?p=7552; US installed $700–1,300/kWh (EnergySage data, via jouleio.com).
- Solar modules: US median $0.28/W Q1 2026 (Anza, via pv-magazine-india.com/?p=14706); China
  FOB quotes ~$0.086/W for Q1 2026 loading (pv-magazine-india.com/?p=9622).
- Freight: Drewry WCI $4,639/40 ft on 9 July 2026 (shipuniverse.com/?p=16195).
- SBIR: reauthorized 13 April 2026 through 30 Sept 2031 (Crowell & Moring via mondaq.com); NSF
  Phase I $305k (grantedai.com).
- Humanitarian funding: Global Humanitarian Assistance Report 2026 summary (alnap.org); OCHA
  2026 appeal funding via developmentaid.org.
- ShelterTech eligibility (for-profit, validated customers): habitat.org 2022 call; regional
  transition 2026 (Columbia SIPA capstone listing).
- From domain knowledge, verify before external use: calcined-clay kaolinite threshold (LC3
  research, EPFL); Auroville Earth Institute load-bearing CSEB; Association la Voûte Nubienne
  (earth vault roofs); ASTM E2392.

*v0.3 — the wall is cast in the ground and stood up. The kit is buildable and honestly costed at ~$6.5k–22.5k per powered house for the
first village. As a business it is weak; as an open-method charity deployed through partners
it has the right shape. Everything still gates on one cheap test: Phase A.*
