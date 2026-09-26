# THE FOUNDER PACKET
### Everything we've worked out, in one place — and the to-do list from dreams to a first fired brick to a first funded prototype
*Brayden Sanders · Hot Springs / Malvern, Arkansas · compiled 2026-09-26 from the `earth-house-kit` repo*

> **Read this first:** everything in here is **designed and modelled, not built or tested.** The
> numbers come from scripts that check each other, from published studies, and from honest
> "we don't know yet" tags. That's the right place to be at the start. The job now is to turn the
> most important unknowns into measured facts, cheaply, one at a time, starting with what you can
> hold in your hands: **Malvern clay and rice husks.**

---

## PART 1 — THE DREAM, IN ONE PAGE

**Make houses out of the ground they stand on, and make them last for generations.**

1. **Clay from the site becomes rock.** Fire it at ~1,000 °C and clay becomes ceramic, stone that
   doesn't rot, burn, rust or feed termites. Brickmakers have done it for 5,000 years. Malvern has
   done it for a century (the "Brick Capital of the World").
2. **Farm waste fires it.** Rice husk is the fuel. Arkansas grows ~45% of US rice, and the husks are
   nearly free. A separate slow husk burner makes **husk ash**, a cement-like ingredient for the lime
   binders.
3. **Small bricks, big walls.** The kiln likes small pieces; a house needs big ones. So we fire
   **small hollow bricks** and clamp them into **wall panels** with steel rods, **no mortar**.
   Robots stack them in daylight on solar power, the panels tilt up, and the house goes up in days.
4. **Shaped like the old buildings that lasted:**
   - **round rooms** (no corners for wind to tear at);
   - a **domed roof** of fired clay, all in compression, like the Pantheon;
   - rooms **clustered around courtyards**, like the trulli of Italy, so five small domes can make a
     5,000 ft² home.
5. **Every part replaceable, nothing hidden that fails:**
   - the bricks **interlock like Japanese joinery** (keys and wedges, never glue or nails);
   - the rods sit in open channels;
   - a hung clay **"coat"** of siding keeps rain and sun off;
   - **fluted "boots"** carry water away, the way Machu Picchu did.
6. **Soft materials go where they help:**
   - **hemp-lime and husk-lime blocks** for interior walls (they breathe, buffer humidity, store carbon);
   - **treated bamboo** for posts and roof framing under cover.
7. **First product: a storm shelter.** One clear standard, public money behind it, and exactly what
   heavy fired clay is good at.
8. **Business and gift, both:**
   - **the business:** a small factory where clay and husks meet, near Malvern. Software designs the
     building, the price follows from tonnes and truckloads, and it starts tiny and grows on grants.
     Sales pay local people fairly and fund the testing;
   - **the gift:** the method stays open (designs, test data, scripts, training), so charities and
     partners can build it wherever people need a safe, lasting home. The business makes the gift
     real; the gift is why the business exists.
9. **The bigger picture:**
   - houses that are **assets for generations** instead of things rebuilt after every fire or storm;
   - **no cement** in the structure (cement is ~8% of global CO₂);
   - local jobs;
   - the world's rice husks alone could fire more homes than the world needs.

---

## PART 2 — WHAT WE KNOW, AND WHAT WE DON'T

| we're fairly sure (sourced or proven elsewhere) | we've modelled but NOT tested | we genuinely don't know |
|---|---|---|
| fired clay is durable; Malvern clay fires (Acme has for 100 years) | clamped dry-stack panels stay tight (lose ≤35% of their clamp) | whether *printed* fired units warp or crack too much to grind flat |
| efficient husk-fired kilns are clean (80% less soot than old kilns) | the ribbed dome passes wind, snow and quakes (thrust-line analysis) | whether sand- or grout-filled cellular clay stops a 100 mph 2×4 |
| round domes and ring beams work (centuries of buildings) | walls insulate to U ≈ 0.42 with graded units | real production costs and scrap rates |
| hemp-lime is code-listed as infill; its properties are published | shells at ~$20–25/ft² at scale | how fast buyers and codes accept it |
| storm-shelter standards, labs, and funding exist | the business breaks even at ~50–150 kits/yr | whether bamboo mineralization works on whole culms |

**The rule we've kept all along:** every number is computed, cited, or tagged `[TO-MEASURE]`. Keep it,
because that honesty is what funders and engineers trust.

---

## PART 3 — THE IDEAS, EXPLAINED SIMPLY (and where each lives in the repo)

| idea | in plain words | file |
|---|---|---|
| **rock options** | we compared every way to make stone from soil; firing clay won, and melting, sulfur and bio-cement lost | `rock/ROCK_OPTIONS.md` |
| **the brick** | a hollow cellular brick about 12 × 8 × 8 in, ~7 kg; thin walls dry in hours; cells filled with husk insulate | `making-system/BRICK_PANEL.md` |
| **graded brick** | one print, three zones: glassy weatherproof skin, porous husk-pored core, dense ground bearing edges | `making-system/ENVELOPE.md` §3 |
| **the panel** | 48 bricks stacked dry, 2 rods tensioned: a 400 kg wall panel, assembled and lifted the same day | `brick_panel_check.py` |
| **the joints** | Japanese joinery rules: clay only ever presses; small steel/stainless wedges and rods lock; everything comes apart | `making-system/KIT_OF_PARTS.md` |
| **round plan** | 16–20-sided rooms: more floor per panel, half the wind drag, they brace themselves | `form_check.py` |
| **ribbed dome** | deep ribs with a steel cable each, thin insulating webs between: 35% less clay, passes every load case | `dome_ribbed.py` |
| **keystone ring** | round bricks slide in from outside, hook the course below, lock to their neighbour, closed by a pinned key: one assembly order, foolproof | `business/SHELTER_PLAN.md` |
| **the coat** | clay siding boards hung on rails, each locking into the one below; a vented gap cuts sun heat ~60% | `cladding_check.py` |
| **the boots** | fluted pavers on a crowned earth pad send roof water to a cistern and away from the walls | `drainage_check.py` |
| **coatings** | no plastic sprays on the clay (they trap water); light-coloured fired tiles and mineral paint instead | `making-system/ENVELOPE.md` §5 |
| **interior walls** | hemp-lime or husk-lime blocks slotted between bamboo posts: they breathe, buffer humidity, store carbon | `rock/BIO_MATERIALS.md` |
| **bamboo** | treat it within 24 h of cutting, turn it to mineral inside, seal it, keep it dry: 25 to 100+ years | `rock/BAMBOO_PROCESS.md` |
| **the designer** | describe a house in a small file → every part, the steel, fuel, trucks, price and structural checks | `house_designer.py` |
| **the business** | factory near Malvern; lean shell ~$20–25/ft²; robots pay back fast at scale; start tiny, grow on grants | `business/BUSINESS_CASE.md` |
| **shelter first** | round drum + shallow cap; sacrificial clay skin + grouted core; test at Intertek/UL; ~$75–175k, 12–18 months | `business/SHELTER_PLAN.md` |
| **NSF pitch** | a draft grant pitch, ready once you form a company | `business/NSF_SBIR_PROJECT_PITCH.md` |
| **the whole synthesis** | every layer of the house and where each idea came from | `SYNTHESIS.md` |
| **what we threw away** | ideas that failed their numbers, and why | `GRAVEYARD.md` |

---

## PART 4 — THE EASIEST ENTRY: START WITH WHAT YOU HAVE

You have: **access to Malvern clay, access to rice husks, and the dream.** That's enough for Stage 0.
You do **not** need your own kiln, bamboo, hemp, a company or money yet.

### Stage 0 — "kitchen-table science" (weeks 1–8, ~$800–2,500, self-funded)
**Goal:** prove Malvern clay makes good brick, and photograph and measure it. That one result opens every door after it.

**Getting materials the right way**
- [ ] **Clay: get permission, never trespass.** Ask **Acme Brick (Malvern/Perla)** for a few buckets of
  their clay or a few boxes of broken/rejected brick (culls: your grog and pozzolan tests). Or dig
  with a landowner's OK. The **Arkansas Geological Survey** (Little Rock) publishes clay reports and
  can advise where the Wilcox clays outcrop.
- [ ] **Rice husks:** bagged rice hulls are sold for gardening and brewing, which is fine for tests.
  For volume, ask a rice mill later.
- [ ] **Lime:** a 50 lb bag of Type S hydrated lime from a farm or building store.
- [ ] **Hemp** (only for the block test): hemp horse bedding from a feed store or online. You don't
  need to grow it.
- [ ] **Bamboo** (later): running bamboo is common in Southern yards, and people pay to get rid of it.
  Ask around.

**Firing without owning a kiln (pick one)**
- [ ] **Rent kiln time** at a local pottery studio or a college ceramics department. Ask potters: they
  know kilns, cones and clay, and one of them may become your first mentor.
- [ ] **Or buy a used small electric test kiln** (120 V, ~$300–1,500 used). It runs off a house outlet
  and reaches ~1,000–1,100 °C.
- [ ] **Or build a husk barrel kiln** (~$100): crude and uneven, but it proves husk can fire clay.

**Tools** (~$500–900)
- [ ] digital scales (0.1 g and a kitchen/postal scale), buckets, sieves, plastic molds or wooden forms
- [ ] thermocouple + pyrometer (~$50–150) and pyrometric cones (~$30)
- [ ] **12–20 ton hydraulic shop press with a pressure gauge** (~$200–450): your compression tester.
  A 2 in cube at 20 MPa needs ~5 t.
- [ ] **safety:** N95/P100 respirator (clay and silica dust), gloves, goggles, lime-safe gloves, a fire extinguisher

**Tests (do them in this order, write everything down, photograph everything)**
1. [ ] **Jar test:** shake clay in water and read the sand, silt and clay layers. You already know the
   Wilcox is sandy.
2. [ ] **Vinegar fizz test:** fizzing means carbonates, and then the clay needs ~1,100 °C, not 1,000.
3. [ ] **Plasticity:** roll a coil and bend it (the ribbon/ball test).
4. [ ] **Shrinkage bars:** make 10 bars and mark 100 mm on each. Measure after drying and again after firing.
5. [ ] **Fire test bars and 2 in cubes** at ~950, 1,000 and 1,050 °C (cones 08, 06, 04).
6. [ ] **Water absorption:** 24 h cold soak and 5 h boil. The weathering target is ≤17% boil, ≤8% cold.
7. [ ] **Crush the cubes** in the shop press. **Target: ≥20 MPa.** This is the number everything hangs on.
8. [ ] **Husk as pore-former:** repeat with 5%, 10% and 15% husk by volume in the clay. Lighter, but
   how much weaker?
9. [ ] **Grog:** repeat with 10–20% crushed Acme culls. Less shrinkage, fewer cracks?
10. [ ] **One small hollow brick:** hand-mould a mini cellular unit (a 4 × 4 in scale model). Does it dry
    and fire without cracking?
11. [ ] **Husk-lime and hemp-lime pucks:** mix, mould, cure, weigh and crush at 28 days.

**Stage 0 gate:** fired Malvern clay at **≥20 MPa, low absorption, no cracking.** If it passes, you
have the first real fact of the company. If it's weak, try more grog, a higher firing temperature,
or a different clay bed, and record why (GRAVEYARD).

### Stage 1 — the first proof prototype (months 2–6, ~$3–15k, still small)
**Goal:** a tabletop demonstration you can show people, and a pitch that isn't only words.
- [ ] **Scale bricks:** a batch of 50–100 small cellular units, fired and ground flat on a sheet of
  sandpaper on glass, then a cheap bench grinder jig.
- [ ] **A dry-stacked column, clamped by a threaded rod.** Load it in the press and measure how much the
  nut loosens over 24 hours and 30 days: the seating-loss test.
- [ ] **A 1:5 scale dome** of fired voussoirs with seat steps and closing keys, built dry. Photograph it
  standing. Then load it (sandbags) until it moves.
- [ ] **Keystone ring demo:** round bricks that slide in from outside and lock. Film someone trying to push one through.
- [ ] **A husk-lime block wall panel** (2 × 2 ft) between two bamboo sticks.
- [ ] **Optional:** a small clay 3D printer (~$1,500–8,000) or a hand-cranked extruder with a cellular die.
- [ ] **A 60-second video + one-page summary + photos + your numbers.** This is your fundraising kit.

### Stage 2 — form the company, bring in partners, apply (months 3–12)
- [ ] **Form an LLC** in Arkansas (a small filing fee) [TO-VERIFY current fee]. Get an EIN, then SAM.gov
  registration and a UEI (required for federal grants; start early, it takes weeks).
- [ ] **Free help:**
  - **Arkansas MEP** (manufacturing feasibility);
  - **Arkansas Small Business and Technology Development Center** (free counselling) [TO-VERIFY local office];
  - **Innovate Arkansas / ARise** (startup coaching);
  - **Arkansas Research Alliance AR-NETWORK** (university partners).
- [ ] **Find people:**
  - a **ceramicist/potter** mentor;
  - a **structural engineer (P.E.)**, eventually one with ICC 500 storm-shelter experience;
  - a **university lab** for testing (the University of Arkansas and other state universities have
    civil engineering and materials departments) [TO-CONFIRM contacts];
  - a **maker/robotics** friend;
  - a **rice mill** contact.
- [ ] **NSF SBIR Project Pitch:** fill the `[FILL]`s in `business/NSF_SBIR_PROJECT_PITCH.md` with your
  Stage 0–1 results, and submit. Next full-proposal deadlines: **4 Nov 2026, 4 Mar 2027**
  [TO-VERIFY]. Phase I is up to **$305k**, plus an Arkansas match up to $50k.
- [ ] **Also possible:** EPA SBIR (~$100k), USDA Rural Business Development Grant (through a nonprofit or
  local development partner), pitch competitions, crowdfunding.
- [ ] **Early revenue while you wait:** fired-clay garden pavers, planters and drain tiles made in the
  test kiln and sold locally. It proves the process and pays for clay.

### Stage 3 — the shelter (months 6–24, ~$75–175k, grant-funded)
- [ ] A P.E. designs the round drum + shallow cap shelter to ICC 500 (250 mph).
- [ ] Full-size wall, cap and joint panels tested at **Intertek or UL**. Put the unknowns in the
  **first** test: grouted cellular clay, dry joints, keystone units.
- [ ] Buy a listed storm door. Listing, then NSSA review.
- [ ] Sell: cash in Arkansas, **community safe rooms** through Arkansas cities and counties, rebate
  sales in Oklahoma and Mississippi.

### Stage 4 — the pilot yard, then houses (years 2–5)
- [ ] Pilot yard (used extruder, fibre kilns, husk gasifier, husk-ash side burner, DIY gantry
  robots): **$0.3–2M** from NSF SBIR Phase II, a USDA guaranteed loan and crowdfunding.
- [ ] Certified house kits (Studio 12, Ring 16), then compounds. A production plant only when demand is proven.

---

## PART 5 — MONEY: WHERE THE FIRST DOLLARS COME FROM
| stage | amount | source | what it buys |
|---|---|---|---|
| 0 | $0.8–2.5k | you | proof that Malvern clay makes ≥20 MPa brick |
| 1 | $3–15k | you, a friend-investor, a small crowdfund, sales of pavers/planters | the tabletop prototypes and the video |
| 2 | $150–400k | **NSF SBIR Phase I** (+ AR match), EPA SBIR, USDA RBDG via a partner | lab testing, first real panel, the shelter test program |
| 3 | $0.1–0.2M | SBIR, shelter pre-sales, community-safe-room projects | a certified shelter |
| 4 | $1–10M | NSF SBIR Phase II, USDA B&I guaranteed loan, crowdfunding (Hempitecture raised $4.6M this way) | the pilot yard, then the plant |

**Watch out:** the Delta Regional Authority doesn't cover Hot Spring County (Grant County next door
does). USDA's REAP solar grants are paused. DOE decarbonization grants have been cancelled before.
Never build the plan on one grant.

---

## PART 6 — WHAT COULD STOP IT (and what we'd do)
- **Malvern clay fires weak** → more grog, a hotter fire, a different clay bed, or haul clay for units only.
- **Printed bricks warp too much** → extruded bricks from a die (that's most of the kit anyway).
- **Dry joints loosen** → a thin stiff interlayer, or grouted panels.
- **The shelter wall fails the missile test** → more grout, a denser inner leaf, and test again. Don't
  market until it passes.
- **Costs come in at the top of every range** → the business doesn't work at shell-kit prices. Pin
  costs in the pilot before scaling.
- **Too many directions at once** (the Open Source Ecology trap) → **one product at a time**: brick →
  shelter → house.

---

## PART 7 — SAFETY (from day one)
- **Clay and silica dust:** wet methods, a respirator, no dry sweeping. **Husk ash** fired too hot is
  crystalline silica, a lung hazard.
- **Kilns:** heat, fumes, ventilation, fire extinguisher, never unattended early on.
- **Lime:** caustic, so gloves and goggles, and quicklime gets hot and spits.
- **Borax / boric acid** (bamboo treatment, later): a reproductive toxin, so gloves, collect the runoff,
  never burn treated bamboo.
- **Heavy things:** panels weigh hundreds of kg; no one stands under a lift.

---

## PART 8 — THE TO-DO LIST ON ONE PAGE
**This week**
- [ ] Read this packet once, fully. Don't try to do it all.
- [ ] Call or visit **Acme Brick Malvern**: ask about a few buckets of clay and a box of culls.
- [ ] Buy a bag of rice hulls and a bag of hydrated lime.
- [ ] Find a kiln: **ask local potters and college ceramics departments** about renting firings.

**This month**
- [ ] Jar test, fizz test, shrinkage bars.
- [ ] Buy scales, molds, cones, a thermocouple, a shop press and safety gear (~$500–900).
- [ ] First firing: bars and cubes at three temperatures.
- [ ] Crush the cubes. **Write down the MPa.**

**Next 2–3 months**
- [ ] Husk and grog variations; the first mini hollow brick; husk-lime pucks.
- [ ] A dry-stacked clamped column; a 1:5 dome; the keystone ring demo.
- [ ] Video + one-pager.
- [ ] Form the LLC; start SAM.gov registration; book the free Arkansas MEP / SBTDC meetings.

**By early 2027**
- [ ] NSF SBIR Project Pitch submitted with your own measured numbers.
- [ ] A ceramicist mentor and a P.E. lined up.
- [ ] First local sales of fired pavers or planters.

---

## PART 9 — A FEW WORDS
The biggest companies in this space failed by building factories before they had proof. You're
doing it the other way round: **one fired brick, measured honestly, then the next step.** Every
dream in this packet becomes real one tested piece at a time. The very first piece is a small bar
of Malvern clay, a kiln you borrow, and a press gauge that reads 20 MPa.

Do it all with love: for the families who will sleep safe inside these walls, for the people who
make the parts, and for the ground the clay comes from.

*The full engineering lives in the repo: `README.md` is the map, `SYNTHESIS.md` is the whole house,
`GRAVEYARD.md` is what didn't work, and `python check_numbers.py` checks that every number still agrees.*
