# GEOPOLYMER-CLAY WALL PANEL — Process Spec v0.1
## In-situ grid-calcined, cooldown-injected, rebar-integrated earth panels from native red clay
### Brayden Sanders — Hot Springs, AR. Founding document for the engineering repo.

> **What this is.** A build spec for turning native red clay into structural wall panels by:
> (1) a steel heater-grid pushed into a clay panel that doubles as reinforcement,
> (2) a solar-fed slow dry-out, (3) a battery-fed calcination spike to metakaolin,
> (4) geopolymer activator injected on the cooldown through relief/injection channels,
> self-curing on residual heat.
>
> **Engineering discipline (different from research notes).** Every phase transition is a
> **measured temperature**, not a timer. Every claim carries an **honest number or a
> [TO-MEASURE]** tag. Every hazard is stated. Kill-conditions are explicit: if a test
> fails its gate, the design changes — we do not push past a failed gate. This is a
> prototype spec, not a validated product; nothing here is code-approved and no structural
> claim is proven until the test panel is cut and measured.

---

## 0. THE CORE IDEA IN ONE PARAGRAPH

Native red clay is an iron-rich aluminosilicate — the feedstock geopolymers need. Calcining
it (~700 °C) converts it to a reactive metakaolin-like phase; an alkaline activator then
polymerizes it into a rock-hard aluminosilicate monolith. Instead of digging, firing in a
kiln, and casting back, we **calcine in place** with a pushed-in steel grid that stays as
**reinforcement**, we use **free solar for the slow (latent-heat-dominated) dry-out** and a
**battery for the concentrated calcination burst**, and we **inject the activator on the
cooldown** — into the warm (not scorching) clay, through channels that are simultaneously
**shrinkage-relief voids** and the **injection manifold**. The same heat cycle that calcines
the clay also cures the geopolymer, if injection is timed to the cooldown window.

---

## 1. THE FOUR-PHASE CYCLE (each transition is a measured temperature)

Instrument every panel with thermocouples at **core** (next to an element), **mid**, and
**face**. The thermocouples are the control system.

| phase | what happens | control signal (measured) |
|---|---|---|
| **1. Slow dry** | solar-fed, low power; drive off all water | temperature **stalls at ~100 °C** (the drying plateau — energy goes to latent heat, not temp) |
| **transition** | drying complete | **temp *breaks the plateau* and starts rising** — THIS is the trigger to start the spike |
| **2. Calcination spike** | battery-fed burst; ramp to ~700 °C and **hold to soak the mass** | temp reaches and **holds ~700 °C** for the soak dwell [TO-MEASURE: dwell time] |
| **3. Cooldown** | cut power; let it fall | watch for the **injection window (~110–180 °C, see §4)** on the way down |
| **4. Cooldown injection + self-cure** | inject activator through channels in the window; residual heat cures it | inject at measured temp; geopolymer cures as the panel finishes cooling through ~60–80 °C |

**Why the drying plateau is the key signal (this is real, standard drying-curve physics):**
while water remains, all input energy boils it off and the temperature *arrests* at ~100 °C.
The instant the clay is dry, temperature "breaks free" and climbs. **The break is the
measured, unambiguous "dry" signal** — it tells you when to stop the patient phase and dump
the battery. No guessing.

---

## 2. THE GRID — one structure, four jobs

The pushed-in steel grid is deliberately multi-purpose:
1. **Heater** — resistive current through it calcines the clay from the inside.
2. **Reinforcement** — left in place, it is the rebar (steel + fired-clay matrix).
3. **Shrinkage relief** — the channels/holes it defines give the ~14 % calcination shrinkage
   somewhere to collapse into (the "burger-hole" principle — pre-place the void the material
   shrinks toward, so cracking is controlled, not random).
4. **Injection manifold** — those same channels carry the activator in Phase 4.

**Geometry (the decisive unknown):** grid penetrates **3–4 in into a 6–8 in panel**. Clay is
a poor conductor, so heat falls off fast from each element. **Element spacing must be close
enough that heated zones overlap** or the panel calcines unevenly (fired core, raw between).
[TO-MEASURE: the actual calcination reach per element — found by cutting a test panel.]
Expected reality: a **fired core with softer faces** unless spacing is tight and the dry/
preheat is patient enough for conduction to even out. Plan for the gradient.

---

## 3. ENERGY BUDGET (honest, order-of-magnitude, for a 2×2×0.5 ft test panel)

Computed for ~102 kg clay at ~20 % moisture (see `energy_estimate.py`):

| phase | energy | note |
|---|---|---|
| Phase 1 dry-out | **~15 kWh** | dominated by **latent heat of vaporizing water** — this is *why* it's the slow, patient, solar phase |
| Phase 2 calcination (100→700 °C) | **~15 kWh** | the burst the **battery must deliver and sustain** to soak |
| dehydroxylation endotherm | **~4–5 kWh** | kaolinite→metakaolin structural-water loss |
| **subtotal (no losses)** | **~35 kWh** | for ONE small panel |
| **with real losses (2–4×)** | **~70–140 kWh** | conduction/radiation to surroundings |

**Honest takeaways this forces:**
- **Insulation is not optional.** Without it, losses dominate and the numbers explode. The
  panel must be jacketed during firing.
- **The solar/battery split is correct and necessary:** solar does the cheap slow latent-heat
  dry-out; the battery delivers the concentrated calcination burst. [TO-SPEC: battery bank
  sized for the sustained ~15+ kWh burst, not just peak power — it must *hold* 700 °C through
  the soak, not just touch it.]
- **Scaling to a real wall multiplies this hard.** A full 8-ft wall is orders of magnitude
  more energy. Prove the panel first; the wall's energy case is a separate, sobering study.

---

## 4. THE INJECTION WINDOW (the cooldown pour)

Activator is water-based (NaOH + sodium silicate), boils ~105–110 °C with dissolved salts.

| clay temp on cooldown | behavior | verdict |
|---|---|---|
| **> ~200 °C** | activator **flash-boils on contact, blows back** — no penetration | **REJECT — hazard** |
| **~110–180 °C** | hot dry porous metakaolin **wicks liquid fast**; residual heat then **cures the geopolymer for free** (standard cure is 60–80 °C — cooling *through* that range self-cures) | **CANDIDATE WINDOW** |
| **< ~80 °C** | slower uptake; may need vacuum assist | fallback |

**Why cooldown-injection works (corrected from the naive "pour cold on hot"):** pouring onto
*still-glowing* clay flash-explodes (the pan-of-water hazard). The right move is to inject on
the **cooldown, in the warm window** — hot enough to wick aggressively and self-cure, not hot
enough to flash. **The cooldown edge of the calcination spike IS the injection window, and
the residual heat IS the cure.** One heat cycle: calcine, then cure, injection riding the
cooling curve.

**Uneven-cooling consequence:** core stays hot longer than faces, so the window **arrives at
the faces first, core last** — sequence injection **outer channels → inner** as each zone
falls into the window. The thermocouples tell you when each is ready.

**Fallbacks if liquid injection won't distribute evenly:**
- **Vacuum-assisted infusion** (VARTM-style): seal the panel, pull vacuum, *draw* the
  activator through the porous calcined clay instead of pushing. Best uniformity.
- **One-part / dry activator**: blend a powdered activator (sodium silicate/aluminate) into
  the clay before firing; activate with a single water flood after. Sidesteps injection
  entirely. Real, active field.

---

## 5. THE FIRST EXPERIMENT — one instrumented panel answers everything

Build **one** 2×2×0.5 ft panel of native red clay with a steel grid at a chosen spacing,
thermocouples at core/mid/face, jacketed in insulation, on a solar+battery supply. Run the
full four-phase cycle. Inject **four test channels at four measured cooldown temperatures**
(e.g. 250, 180, 130, 90 °C). Then **cut it open.**

**One cut section measures FIVE unknowns at once:**
1. **Calcination reach** — how far the metakaolin zone extends from each element (sets grid
   spacing for real panels).
2. **Shrinkage** — % dimensional change (sets segment size / whether monolithic is possible).
3. **Crack pattern** — did the relief channels control it, or did it craze? (validates the
   burger-hole principle).
4. **Injection penetration & the pour window** — which of the four temps gave fast clean
   uptake vs blowback vs slow soak (sets the injection temperature empirically).
5. **Per-zone strength** — compressive strength of core vs face vs near-channel vs between
   (the number everything hangs on).

**Also run first, cheaper (gate before you build the grid rig):**
- **Swell test** on the raw red clay (does it expand when wet? montmorillonite content is a
  killer — shrink-swell cracking). **GATE: if it swells badly, the whole approach needs
  rethinking before spending on the grid.**
- **Bench calcination**: fire a small block to 700 °C slowly, measure shrinkage and cracking,
  raw vs calcined strength with activator. **GATE: if calcined strength is too low even on a
  clean bench sample, in-situ won't beat it.**

---

## 6. KILL-CONDITIONS (the honest gates — if these fail, the design changes)

- **Swell test fails** (clay expands significantly wet) → shrink-swell will crack every
  panel; rethink feedstock or stabilization before proceeding.
- **Bench-calcined strength too low** (metakaolin-activator pucks don't reach a usable MPa on
  *your* clay) → the chemistry doesn't work on this feedstock; no rig will fix it.
- **Calcination reach ≪ spacing** (fired zones don't overlap at buildable spacing) → can't
  get uniform panels; either impractically dense grids or abandon in-situ heating.
- **Shrinkage cracks through the reinforcement** even with relief channels + fiber → panels
  aren't structurally monolithic; fall back to smaller segments or a framed-hybrid design.
- **No safe injection window** (wicks only when cool, flashes when warm) → drop cooldown-
  injection for vacuum-infusion or one-part dry activator.
- **Energy per panel is prohibitive even insulated** → the process may be viable at bench
  scale but not for walls; that is a real and acceptable finding to reach early.

---

## 7. HONEST FRAMING (what this is and is not)

- **This is not fusion, not "fusing ground into rock."** It is **calcination + geopolymer-
  ization** — thermal activation of clay followed by alkaline chemical bonding into a
  synthetic aluminosilicate stone. Every step is established materials engineering
  (metakaolin geopolymers, in-situ thermal soil treatment, VARTM infusion, one-part
  activators). The *combination in native clay with a grid-as-rebar and cooldown injection*
  is the novel, under-explored part — and the part to prove.
- **Strength target:** clean metakaolin geopolymers reach 40–80 MPa compressive; native red
  clay will do **less** and the number is [TO-MEASURE] on your clay. Tension is weak (it's a
  stone) — that's why the steel grid and (recommended) **chopped fiber** (basalt/steel) in
  the mix, to bridge shrinkage microcracks.
- **Cast-in-place beats tilt-up** for earth panels: a fired stone is strong in compression,
  weak in the tension a crane-lift demands. Build the panel *in its final orientation* (or
  handle small segments) before attempting anything tilt-up.
- **Nothing here is permitted or code-approved.** A structural earth wall needs engineering
  sign-off; the test panel's measured strength is the first thing an engineer would ask for.

---

## 8. PROPOSED REPO STRUCTURE

```
earth-panel/
  README.md                 # this spec, top-level
  energy_estimate.py        # the energy budget calc (honest numbers)
  swell_test/               # protocol + results for the clay swell gate
  bench_calcination/        # small-block fire tests: shrinkage, crack, strength
  test_panel_01/            # the instrumented panel: design, thermocouple logs, cut-section results
  injection/                # the pour-window study (4-temp channels), vacuum + dry-activator fallbacks
  grid_design/              # element spacing, material, push-in rig, grid-as-rebar
  GRAVEYARD.md              # ideas tested and killed (start with: "pour cold on glowing clay" = flash-blowback)
```

---

## APPENDIX — the physics in one line each (all reproducible / standard)

- **Drying plateau:** temp arrests at ~100 °C until water is gone, then climbs — the "dry"
  signal. (latent heat of vaporization)
- **Calcination:** kaolinite → metakaolin at ~600–800 °C (dehydroxylation) — makes the clay
  reactive AND porous (the porosity is what lets injection work afterward).
- **Geopolymerization:** alkali dissolves Si/Al, re-polymerizes into a 3D aluminosilicate
  network — synthetic stone; cures faster warm (60–80 °C).
- **Cooldown injection:** warm porous metakaolin wicks liquid fast; residual heat self-cures;
  too hot → flash-boil (hazard).
- **Shrinkage relief:** pre-placed voids (the grid channels) give ~14 % calcination shrinkage
  a controlled place to collapse — the burger-hole principle.
- **Grid-as-rebar:** the steel heating grid, left in, is the reinforcement — one structure,
  four jobs (heat, rebar, relief, injection manifold).

*v0.1 — a prototype process spec. Every [TO-MEASURE] is a real open number; every kill-
condition is a real gate. Build the swell test and the bench block first; they gate the grid.
Then the one instrumented panel, cut open, answers the rest.*
