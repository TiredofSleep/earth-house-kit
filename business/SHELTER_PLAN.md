# SHELTER-FIRST PLAN — a certified above-ground tornado safe room
### v0.1 · model: `shelter_check.py` · sources: the storm-shelter section of `rock/RESEARCH_NOTES.md`

> **Why a shelter first:** it's small, it answers to **one standard** (ICC 500 / FEMA P-361 / P-320),
> it has a known test path of about **$75–175k over 12–18 months** (a whole-house evaluation is far
> longer and costlier), and its selling point is exactly what fired clay has: mass, fire resistance
> and permanence. Public money can pay up to 75%.
> **But nothing is a shelter until it passes the tests.** Every number below is design-stage.

---

## 1. What the standard demands (ICC 500-2023 / FEMA P-361 2024 / P-320 2024)
- **250 mph design wind** for every FEMA-funded residential safe room, wherever it is. Kd = 1.0 because
  tornado wind direction varies. GCpi ±0.55 unless you provide the atmospheric-pressure venting that allows ±0.18.
- **Debris missile:** a 15 lb 2×4.
  - **100 mph on any surface steeper than 30°** from horizontal, and 67 mph on flatter roofs.
  - It is **always fired perpendicular**, so steep faces get no glancing credit.
  - At least 3 impacts per specimen, including joints, seams, supports and corners.
  - **Pass:** no perforation, permanent deflection under 3 in, and no spall or fragments reaching
    past the witness screen.
- **Joints:** sealed masonry control joints up to ⅜ in are exempt. **Dry-stack head joints must be
  impact-tested**, and joints are where masonry fails.
- **Doors, louvers, vents:** must be listed and labeled. **Buy a listed ICC 500 door**; don't
  develop one.
- **Occupants:** residential shelters hold up to 16 people at 3 ft² each (5 ft² for other
  residential). Community shelters are 5 ft² per person, and those for 50+ people need peer review.
- **Foundation and anchorage:** ACI 318 slab and anchors under special inspection, a published
  minimum foundation specification, and P.E. or R.A. certification at closeout.
- **Never claim "FEMA approved."** FEMA doesn't approve products. FEMA recommends NSSA certification,
  or a P.E.-sealed compliance letter.

## 2. The shape: a round drum with a shallow cap (`shelter_check.py`)

| shape (77 ft², 250 mph) | peak suction | roof missile | net tie-down | verdict |
|---|---|---|---|---|
| box, flat roof | 21.8 kPa (corners) | 3.1 kJ | 64 kN | corners; needs a reinforced slab |
| pyramid | 13.3 | 6.8 | 8 | corners; steep faces take 100 mph |
| low dome to 51.8° | 11.4 | 6.8 (lower ring ≥ 30°) | 34 | good, but its steep ring takes 100 mph |
| steep corbelled cone | 11.4 | 6.8 | 0 | **no missile credit, no ASCE 7 coefficients**: a shed shape |
| **round drum + cap under 30°** | **9.4** | **3.1** | 44 | **lead: round, no corners, roof takes only the 67 mph missile, dome coefficients exist** |

- **Round:** tornado winds come from every direction and there are no corner suction zones.
- **The cap stays under 30°** everywhere, so only the smaller roof missile applies. It's the ribbed
  dome of the houses made shallow: post-tensioned ribs, graded webs, and **ribs tied down through
  the wall rods to the footing** to carry the 44 kN of uplift.

## 3. The wall: copy what has already passed 100 mph
**Fired clay alone won't do it.** 4 in of solid face brick shattered at ~76 mph under a 9 lb
missile. What passed is a **cavity wall**: brick veneer + 2 in cavity + partially grouted 8 in CMU
with #5 bars at 24–32 in. The brick shattered and absorbed the hit, and the missile bounced off the
core. Our system already has that shape:

| layer | in our kit | job |
|---|---|---|
| sacrificial skin | **hung fired siding boards**, severe-weathering grade | shatter and absorb, replaceable |
| cavity | the ventilated rainscreen gap | lets the skin break without driving into the core |
| structural core | 8 in cellular units, **grouted cells** (not sand) around every rod and at every joint; head joints staggered | stop the missile, carry wind |
| steel | post-tensioned rods to the footing | continuous load path, clamps the joints |
| optional liner | 12-gauge steel or plywood inside | catches spall (witness-screen rule) |

**Keystone units (the founder's idea).** Print the drum's units **round and tapered, wider outside
than inside**, and slide them in radially from outside:
- **Pushed inward** (the missile's direction), a unit wedges between its neighbours like a keystone,
  and the ring shares the hit.
- **A lock operated from inside** (vertical post-tensioned rods through the cells, or a stainless pin
  dropped in from inside) stops it moving back out under suction or rebound.
- **Pull the pin and push the unit out** to replace it.
- **Wedging needs a squeezed ring:** stainless **hoop bands** (barrel hoops) every couple of courses,
  in the siding cavity where they can be inspected.

First-order check (`shelter_check.py`): ~18–45 kN of static push-in resistance per unit with 15–30 kN
of hoop compression, against an average missile contact force of ~30–100 kN. That's the same order,
so it's a real gain and not a guarantee. The siding skin, the grout and the ring's shared mass also
act first. The test decides.

**The least proven elements go into the FIRST test panel:** dry head joints, grouted cellular fired
clay and **keystone units with and without hoop bands** (hit at a unit centre and at a joint), since
no test data exist for them. A cheap failure early is the goal.

## 4. Test and certify (research estimate, UNSOURCED costs)
1. **P.E. with ICC 500 experience:** design to ICC 500-2023 at 250 mph, GCpi ±0.55, foundation and
   anchorage spec (~$15–30k, months 0–3).
2. **Buy a listed door** (~$1.5–3k each).
3. **Pre-test panels:** wall, cap, joint and seam specimens at **Intertek, UL or ICC-ES**. Texas Tech
   no longer tests commercially. Budget 2–3 rounds (~$20–60k, months 2–6).
4. **Listing / labeling or a Code Compliance Research Report,** with factory QA inspections
   (~$15–40k + annual), then **NSSA** producer membership and third-party design review (months 6–12).
5. **Total ~$75–175k, 12–18 months.** NSF SBIR Phase I can pay for the R&D testing: add the missile
   and pressure tests to Objective 4 of the pitch.

## 5. Who pays (research, 2025–2026)
- **Arkansas: no residential safe-room rebate since 2016.** FEMA money in Arkansas goes to
  **community safe rooms** (180+ funded through HMGP/PDM), via city and county applicants, with a
  P.E. letter and peer review for each project. Vilonia's 6,500 ft² school safe room had $1.3M FEMA
  funding. **In Arkansas, the grant market is community and school safe rooms; homeowners pay cash.**
- **Residential rebates next door:**
  - **Oklahoma SoonerSafe:** $3,000 or 75%, above-ground allowed.
  - **Mississippi:** 75% up to $3,500; needs a Mississippi P.E.-sealed plan and a licensed contractor.
  - **Alabama:** tax credit, the lesser of $3,000 or 50%.
  - **Kansas:** $3,500 or 75%, NSSA/ATSA members only; currently inactive.
- **FEMA HMGP** pays up to 75% after a disaster, PDM 75–90%, and BRIC was reinstated by court order in
  2026. Residential units can use FEMA's pre-calculated benefits if they stay under the state's value.

## 6. The market and the price to beat
- **Steel competitors:** Atlas ($5.0–7.8k for ~20–55 ft²), Torshel 4×8 steel ($8.7k before shipping),
  and Arkansas Industrial Fabricators in Sheridan. Above-ground shelters typically cost $4–7.5k
  installed in Texas, with a national range of $2.6–15k.
- **Our angle:** a **bigger, permanent room** (~77 ft², room for 16 people at the residential rate)
  that is also a **usable storage room, studio or safe core** of a house. It's fireproof, quiet and
  doesn't rust. To compete with steel at ~$60–100/ft² installed, it needs to land around **$9–15k
  installed**. The lean shell kit is modelled at ~$2.5–3.5k ex-works, which leaves room for grout,
  the door, the foundation and installation, **if the tests pass**.
- **Liability is real:** wrongful-death suits exist, and Alabama's AG has acted against bad
  installers. Most failures are anchorage and installation, so control the install, use special
  inspection and a documented QA trail, and never claim FEMA approval. Insurance for a small maker is
  ~$10–40k/yr (UNSOURCED).

## 7. Sequence
1. **Now:** engage a P.E. and an Intertek/UL quote; send the NSF pitch with shelter testing inside
   Objective 4; build the first wall, joint and cap panels.
2. **Month ~6:** pre-test. If dry-stack grouted clay fails, change the core (more grout, a denser
   inner leaf) and re-test. Don't market anything yet.
3. **Month ~12–18:** listing and NSSA; first sales for cash in Arkansas; community-safe-room bids
   with Arkansas cities and counties; rebate-eligible sales in Oklahoma and Mississippi through
   licensed partners.
4. **Then:** the certified wall and roof become the proven core of the house kit, the same parts
   and the same test data.
