# BUSINESS CASE — a clay + rice-husk kit factory
### v0.1 · model: `business_model.py` (assumptions `data/business.json`, lean scenario `data/business_lean.json`) · designs: `houses/*.json`

> **The idea:** put the factory where good firing clay and rice husk already meet. Customers pick
> a design, from a storm-proof shed to a 5,000 ft² compound of linked domes. The design file
> becomes a parts list, and the price follows from **tonnes of fired clay, the types of parts, and
> truckloads**. Clay and husk are nearly free, so **the cost is mostly fixed** (plant, kilns, staff,
> certification). A factory that runs full can sell cheap.
>
> Everything here is first-order. Values without a source are tagged UNSOURCED in the data
> files; replace them with quotes before anyone invests. The open method stays open (CC BY). This
> is a separate, arm's-length company, as MISSION §5 describes for any commercial arm.

---

## 1. What a kit costs to make — and what the market pays

**Market, per ft² of shell (sources in §7):**

| comparison | $/ft² |
|---|---|
| metal building kit (kit only) | 10–25 |
| barndominium shell kit | 20–35 |
| prefab shed (Tuff Shed ~$35–41) | 25–70 |
| SIP shell kit (~$58 typical) | 35–77 |
| log home shell kit | 50–100 |
| structure + foundation + exterior share of a US site-built house (NAHB 2024: 40% of ~$162) | ~65 |

**Our kits, production plant (6,000 t/yr) running 90% full, 300 miles** (`business_model.py`):

| kit | ft² | fired t | trucks | baseline $/ft² | **lean $/ft²** | lean delivered |
|---|---|---|---|---|---|---|
| Shed 8 | 77 | 7.5 → 4.5 | 1 | 77 | **42** | $4.3k–8.8k |
| Studio 12 | 179 | 12.3 → 7.5 | 1 | 53 | **29** | $6.2k–13.3k |
| **Ring 16** | 322 | 18.1 → 11.1 | 1 | 42 | **22** | **$8.3k–18.2k** |
| Ring 20 | 505 | 24.4 → 15.1 | 2 → 1 | 35 | **19** | $10.5k–23.5k |
| Compound (13 pavilions, 5,379 ft²) | 5,379 | 279 → 172 | 14 → 9 | 39 | **21** | $122k–273k |

*(Low-case costs shown for $/ft²; delivered prices give the full low–high range. Every kit is a
**shell**: walls, dome, tiled skin, siding, plinth. Site work, doors, windows, services, finishes
and assembly are extra.)*

**What makes "lean":**
1. **Graded 6 in walls** instead of 8 in: they meet the insulation target with ~35% less clay (`thermal_check.py`).
2. **A ribbed dome**: deep ribs and a thin shell between, ~40% less clay. **Not designed yet.** It
   has to pass `dome_thrust.py` before this number means anything.
3. **A gravel drip trench dug on site** instead of fired apron, collector and drain-tile parts.
4. **Extrusion-first production**: 1.5–4 labour-hours per tonne instead of 4–12. Automated US
   plants run 60–200 kt/yr with 20–30 people, a fraction of an hour per tonne.
5. **A capital-light plant**: used extruders and forklifts, open sheds, and a zigzag or Hoffmann
   kiln built from the plant's own bricks, the way brickmakers do (capex ×0.5, UNSOURCED).

**Where the money goes (lean Ring 16, low case):** parts $4.1k, fixed $1.7k, margin $1.4k,
freight $1.1k. **Clay and husk are a few percent of it.** The levers are handling labour, steel
hardware, and keeping the plant full. That is why the lean list is about less clay and less
handling, not cheaper earth: the earth is already nearly free.

**The price premium this rests on:** commodity brick sells at ~$270/t. A kit at $22–65/ft² sells at
~$650–1,900 per tonne of fired clay. That is a **2.5–7× premium over brick**, earned by design,
precision, the system, certification and delivery. It is the business's whole margin, and the
reason certification matters (§4).

---

## 2. Plant sizes, break-even

| | pilot | production |
|---|---|---|
| capacity | 1,000 t/yr (~55 Ring 16 kits, or ~90 lean) | 6,000 t/yr (~330, or ~540 lean) |
| capex (baseline) | $0.67–2.47M | $1.9–6.2M (research brackets $1.5–5M for 5–10 kt/yr) |
| fixed cost incl. capital | $0.38–0.96M/yr | $1.1–2.6M/yr |
| **break-even at $65/ft² (Ring 16)** | ~28 kits/yr (~50% of capacity) in the low case | ~82 kits/yr (~25% of capacity) in the low case |

In the high-cost case (every input at the top of its range), a kit's parts cost as much as the
$65/ft² price and it never breaks even. **The business only works in the lean, well-run half of
the ranges.** Pin those costs with quotes and a pilot before scaling. Check again with
`python business_model.py`.

---

## 3. Where to put the factory

**Criteria:** firing-grade clay proven by test (Phase R), rice husk within trucking distance, cheap
flat land, good roads, and a market within ~300–600 miles.
- **The Malvern area**, ~20 miles from Hot Springs, is widely called the "Brick Capital of the World":
  commercial brickmaking on its clays for over a century [TO-VERIFY: current plant and clay access].
  That is the strongest evidence of firing clay near the founder.
- **The rice region** (Grand Prairie / Stuttgart, the Delta): about 4.2 Mt of paddy a year means
  ~0.8 Mt of hulls, at **$5–8 per ton FOB mill** (USDA AMS). Big mills gasify their own hulls, but
  the smaller ones sell. Land is $2.4–3.7k/acre (USDA NASS 2025). Delta soils are often expansive
  alluvial clays, so test them for firing before buying.
- **The likely answer:** a clay site near Malvern, trucking hulls ~90 miles, or a Delta site on a
  tested clay. Industrial power is 7.3 ¢/kWh (EIA); plant solar covers fans, extruders and printers.

**The truly local mode:** for a compound or a village, **bring the plant to the site**: a mobile
extruder, fibre kilns, husk gasifiers, the solar array. That's the charity kit of MISSION v0.2–0.3,
now making rock. It uses no freight and the local earth, and the factory is the village's first
employer. The Arkansas factory proves the system and trains the people who take it elsewhere.

---

## 4. The hard parts (and the order to beat them)

1. **Certification before house sales.** An ICC-ES evaluation report for a novel structural masonry
   system: ~$100–400k and 18–36 months (UNSOURCED). Engineering stamps ~$1–3k per design per state.
   WikiHouse became mortgageable only after a 10-year warranty existed.
2. **Weight vs value.** Fired clay is heavy (~35–56 kg/ft² baseline, ~22–35 lean). Steel and SIP
   kits are 3–10× lighter. A full truck over 330 miles costs ~$50/t, but a 5 t shed on its own truck
   costs ~$220/t. **Ship full trucks**: pool orders by region, and send the compound-scale plant to
   big jobs.
3. **Yield and labour.** Drying cracks in printed or cellular units, and grinding time. Scrap rate is
   the key unknown, so measure it in the pilot.
4. **Installer labour.** Buyers need assembly crews, and SIP and steel go up fast. Answer: dry
   assembly, no mortar, a hoist and a torque wrench, crew training, and an assembly manual generated
   from the design (HANDOFF R6).
5. **The contech graveyard.** Katerra (~$2B raised), Veev ($600M), Mighty Buildings and Diamond Age
   all failed by building capacity before demand. **Start capital-light.**
6. **Permits.** ADEQ air registration or permit for kilns (fee ~$28/ton of permitted emissions),
   an open-cut mining permit and reclamation bond for the clay pit.

---

## 5. The sequence (capital-light)

| stage | what | sells | why |
|---|---|---|---|
| **0. Phase R** ($5–15k) | fire the clay; print, fire, grind units; dry-stack column; a 2 m test dome | nothing yet | kills or confirms the idea cheaply |
| **1. Pilot yard** (~$0.3–1M, used gear) | 2–4 kilns, one extruder, 2 printers | **agricultural buildings, storage, studios**, which are often exempt from the residential code | revenue, yield data, a showroom |
| **2. Safe rooms** | ICC 500 / FEMA P-361 missile testing of a fired-unit safe room | tornado shelters ($3–12k installed; FEMA grants cover up to 75%) | a storm-proof, fireproof product in tornado country; needs a pass first |
| **3. Certified houses** | ICC-ES report, stamped designs | Ring 16 / Studio 12 shells, then compounds | the premium market |
| **4. Production plant or mobile plants** | continuous kiln, or site plants for compounds and villages | volume | only after demand is proven |

---

## 6. Why it could win anyway
- **Nothing to burn, rot, rust or feed termites.** In wildfire and tornado country that's a
  selling point, once proven. Fired clay is non-combustible.
- **Insulated, heavy, quiet, and it lasts.** A graded wall at U ≈ 0.42 with an 11 h lag, a vented
  rainscreen, and every part replaceable.
- **Cheap raw materials from farm waste and dirt**, with the plant powered by its own solar.
- **The design software is the storefront.** A buyer picks polygons and openings; the price, parts,
  trucks and structural checks come back instantly (`house_designer.py`, `business_model.py`).

---

## 7. Sources (from the research note; verify before external use)
- USGS Mineral Commodity Summaries 2026 (clays): common clay $21/t; 13.0 Mt; 43% to brick.
- Brick prices ~$500–850 per 1,000 (homeguide); ~2 t per 1,000.
- US brick plant scale and staffing (PMC3734502); Glen-Gery, US Brick, Boral expansions.
- WASP 40100 ~$11k; 3D PotterBot ~$8k; import shuttle kilns ~$6k/m³; forklifts $8–43k.
- USDA NASS land values 2025; USDA AMS rice hulls $5–8/ton FOB; UA extension 2025 rice crop.
- EIA industrial electricity AR 7.26 ¢/kWh; FRED Arkansas durable-goods wage $26.27/h.
- DAT flatbed $2.66/mi linehaul (Sep 2026), 46–48k lb payload.
- Tuff Shed, homeguide (ADU, barndominium, log, safe rooms), Mighty Small Homes (SIP), NAHB 2024
  cost of construction ($162/ft²), Monolithic Dome pricing.
- ICC-ES rules of procedure; ADEQ air permitting guide; Arkansas Open-Cut Land Reclamation Act.
- Katerra, Veev, Mighty Buildings coverage (failory, TechCrunch, 3DPrint).
