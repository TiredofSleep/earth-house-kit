# BAMBOO: feed it at death, turn it to mineral inside, seal it — a lab process toward 50+ years
### v0.1 · research Sep 2026 · the founder's idea, tested against the literature

> **The idea:** feed the culm something at the end of its life, transform it inside the culm into
> a lasting mineral, and protect it with a final dip, to make a support structure that is rigid but
> still flexible and lasts 50+ years.
> **What the evidence says:**
> - The **moment of death** (treatment within 24 h of cutting) is the proven feeding point.
> - Mineralizing inside bamboo **works in the lab and keeps stiffness and strength**.
> - The "ionized dip" is best read as **plasma activation + a pigmented silicate/siloxane coat**.
> - **50+ years comes mostly from keeping the culm dry and covered.** Chemistry takes it from ~5
>   years to ~25; detailing takes it to 100+.
> - Everything past step 2 below is **frontier on whole culms**.

---

## The process

| step | what | parameters (from the literature) | status |
|---|---|---|---|
| **0. Harvest** | 4–6-year-old culms, dry season (low starch) | treat within **24 h** of cutting | proven |
| **1. Feed at death: modified Boucherie** | push preservative through the green culm's own sap channels | 5% boric acid + 5% borax (or 5–8% DOT); 1.0–1.7 bar (15–25 psi); 30–60 min, until the outflow matches the inlet; target **4–5 kg/m³** boric-acid equivalent for use under cover. *Optional frontier:* add 2–5% silicic acid or silicate to the same feed (Yamaguchi's silicic–boric complexes resisted leaching) | proven (borate); Si + B frontier on bamboo |
| **2. Diffuse and dry** | let it spread, then dry | stand upright 2 weeks under cover, then dry to ~12% moisture | proven |
| **3a. Turn it to mineral: silica route** | fill the cell walls with silicate, then gel it in place | pierce diaphragms or drill near nodes; vacuum ~700 mmHg 30 min; 10–20% sodium silicate at 60 °C, 1–2 h; dry 24 h; then 5% NaHCO₃ or 5–10% CaCl₂ at 55–60 °C, 3 h (precipitates insoluble silica / calcium silicate); rinse, dry at 60–80 °C | lab-proven on wood and bamboo samples; **frontier on whole culms** |
| **3b. …or calcium carbonate route** | deposit calcite inside the cell walls (ETH/Empa method) | CaCl₂ + dimethyl carbonate / NaOH cycles to ~15–18% weight gain; bamboo samples: MOE +1–3%, MOR +3–10%, better fire resistance, less decay loss | frontier on culms |
| **4. Seal against water** | water-repellent silica network | TEOS + methyl/alkyl silane sol; on bamboo with silicate: **water absorption −84.5%, swelling −52–58%, contact angle 147°, LOI 36%, MOE +15%, MOR +9%** (Chem Eng J 2025). Or oil heat treatment, **but never above 180 °C** (brittle above ~200 °C: tensile strength halves) | lab-proven |
| **5. The "ionized dip": surface** | plasma-activate the waxy skin, then coat | glow-discharge plasma takes the skin's contact angle from >110° to <20° so coatings bond; then a **pigmented potassium-silicate or siloxane coat with UV absorbers** (silicate alone doesn't stop UV greying) | frontier on bamboo; renew every ~5–10 years |
| **6. Detail it dry** | the step that gives the decades | under cover, moisture below 20% (fungi and most insects need more), off the ground on fired-clay plinths, deep eaves, joints that can be replaced | proven: **Japanese smoked roof bamboo 100–200 years; Colombian guadua houses 100+ years** |

## Service life, honestly
| condition | life |
|---|---|
| untreated, ground contact | 1–3 years |
| untreated, under cover | 4–6 (10–15 in a dry climate) |
| well treated, open weather | ~15 |
| well treated, under cover | **~25**; 30+ with combined measures |
| kept dry and covered, well detailed (smoked minka roofs, guadua bahareque) | **100+** |

So the 50+ year target is realistic for **covered, dry, visible, replaceable** bamboo: roof framing,
partition posts, verandah frames under the eaves. Exposed culms stay a ~15-year part.

## The risk to watch: "rigid but flexible"
Mineralization usually keeps or raises stiffness and strength. But **work-to-failure and impact
toughness are almost never measured**, and water glass alone lowered bending strength ~9% in pine.
Heat above ~180–200 °C clearly embrittles bamboo. **Every step gets a toughness test**, not only
strength.

## Tests
- **Uptake:** retention by weight plus ICP (boron, silicon, calcium); curcumin test for boron depth;
  SEM-EDX or micro-CT for where the mineral went.
- **Fixation:** leaching per EN 84 / AWPA E11, then ICP of what stayed.
- **Decay:** EN 113 / AWPA E10 before and after leaching. **Termites:** EN 117/118 or AWPA E1, plus a 3-year field graveyard.
- **Mechanics:** ISO 22157:2019 (compression, bending, shear, tension) **plus work-to-failure and a pendulum impact test**.
- **Fire:** cone calorimeter (ISO 5660), LOI. **Weathering:** QUV (ASTM G154) plus 2+ years outdoors;
  colour, checking, contact angle, coating adhesion.

## Safety
- **Boric acid and borax are EU reproductive-toxicity 1B.** Wear gloves, control dust, collect and
  reuse the Boucherie outflow, and **never burn treated offcuts**.
- **Silicates are alkaline** (eye and skin protection). Copper is toxic to water life.
- **Avoid CCA, CCB and creosote.**

## Where it enters the kit
Interior partition posts (already in `house_designer.py`), roof framing under the dome's eave
extensions, verandahs and shade structures, and scaffolding and the dome-building mast. **Never** as
the steel in tension (GRAVEYARD).

Sources: INBAR TOTEM sap displacement; Janssen / Practical Action (CTC-N); ABARI; Yamaguchi 2002–03
(WST); Altun 2010 (Wood Research); Pries & Mai 2013; Merk/Burgert (Holzforschung 2016, Empa);
Ind Crops Prod 2023; ACS Sust Chem Eng 2026; Chem Eng J 2024 (HAP) and 2025 (silicate + silane);
Wood Research 2016; PMC9919539 (heat and brittleness); Tang 2019 (tung-oil heat treatment); Forests 2020
(plasma); Pfeffer/Mai 2011 (silicate weathering); Kaminski 2016; ECHA boric acid CLH. URLs in the
research-notes file and the agent brief this doc was built from.
