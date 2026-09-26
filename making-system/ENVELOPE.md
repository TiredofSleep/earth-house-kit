# THE ENVELOPE — a coat, a pair of boots, and units graded like bone
### v0.1 · `cladding_check.py`, `drainage_check.py`, `thermal_check.py` · sources in `rock/RESEARCH_NOTES.md`

> The structure (clamped fired panels, fired dome) is designed to stand for centuries **if it stays
> dry**. This layer keeps it dry: a hung, sloped, replaceable **coat** of fired siding; a
> **foundation that clears water away on purpose**; and wall units **printed in graded materials** —
> dense where they bear and weather, porous where they insulate. Nothing here is tested yet.

---

## 1. The coat: fired siding that hangs, locks and sheds water

**Lineage:** English vertical tile hanging (since the late 1600s; tiles outlast their fixings),
Japanese *shitami-bari* (removable clapboard over earthen walls), and modern terracotta rainscreens
(NBK, Argeton, Boston Valley).

**How it goes together (no nails into the clay):**
1. **Rails:** vertical rails clamp to each panel's top and bottom steel channels, forming a
   ~20 mm ventilated, drained cavity. Anything from 3 mm stops capillary wicking; ~19 mm and up
   dries well.
2. **Battens:** horizontal battens run across the rails at the board gauge (150 mm).
3. **Boards:** extruded double-leaf fired boards, 1,200 × 200 × 25 mm, ~6.8 kg (~38 kg/m²; the
   commercial benchmark is 30–40 mm and ~50 kg/m²). Each hangs on a batten and **locks into the
   board below**, the way rainscreen clips carry the tile above and hold the one below. Nibs alone
   are never accepted against wind (BS 5534 requires positive fixing).
4. **Lap and drip:** 50 mm headlap (BS 5534 minimum 37.5 mm; IRC lap siding 32 mm). Each board
   tilts ~10° over the one below and has an undercut drip edge.
5. **Base:** siding starts ≥ 150 mm above grade (IRC R317), with a weep at the plinth.

**Results (`cladding_check.py`):**
- **Wind:** the lock works at **2–5% of board strength** at 50 m/s with corner suction. This is
  the kit's one clay "hook", allowed only because the stress is tiny. Knocks are the real risk,
  so every board **lifts out alone without tools**, as the TerraClad spec requires.
- **Sun:** the ventilated cavity cuts heat into the room by **~60%** in our model; published
  measurements give 30–70%, most on east and west faces. Up to 27% lower annual cooling in hot-humid climates.
- **What it changes:** the wall units behind **stay dry**. Only the boards, dome tiles and plinth
  need severe-weathering grade (≤ 8% boil absorption, freeze-thaw tested). The structure can use
  cheaper, more porous, better-insulating bodies.

**Why separate boards instead of a water-shedding face on every unit:** truly hydrophobic fired
clay doesn't exist. Water beading needs a siloxane repellent that lasts 10–15 years. A dense unit
face still gets wet, and it can't be replaced without unclamping a panel. Boards can be replaced
one at a time, and the cavity behind them vents heat.

---

## 2. The boots: fluted fired bricks on a crowned, compacted earth pad

**Lineage:** Machu Picchu. About **60% of its construction effort is underground**, in foundations and
drainage. It has 129 wall drain outlets, drip channels cut under its eaves, drains designed for
~200 mm/h, and has stood roughly 400 years of 1,940 mm/yr rain without failure. Also Roman road
camber and ditches, F.L. Wright's rubble trench, clay field drain tile (1838, still working a
century later), and Bangladesh's raised plinths (116,500+ homes).

**The water path (`drainage_check.py`):**
```
dome + scale tiles -> corbelled drip eave (30 cm out)
  -> FLUTED APRON: fired pavers on the crowned pad, falling 5% outward, flutes running radially
  -> COLLECTOR RING: a fluted channel course falling 1% to the cistern (first flush first)
  -> PLINTH units below grade with vertical flutes = a drainage plane
  -> fired-clay DRAIN TILE at the bottom of a rubble trench, 1% to daylight
```

| Hot Springs design storm (NOAA Atlas 14, 5-min) | 16-gon | 20-gon |
|---|---|---|
| 10-yr, 214 mm/h: flow off the dome | 2.2 L/s | 3.3 L/s |
| apron flute capacity vs the drip | **49×** | ~40× |
| collector ring capacity at the inlet | **5×** | ~3.5× |
| 100-yr, 300 mm/h: apron / collector | 35× / 4× | ~29× / ~2.8× |
| rain harvested per year | ~38 m³ | ~58 m³ |

- **The flutes are about control, not capacity.** They break the splash, stop water running back
  toward the wall, and send every drop outward. **The collector ring is the channel to size and
  keep clean.**
- **The pad:** compacted to ≥ 95% standard Proctor in 150–200 mm lifts. Assume 1,500 psf bearing
  unless tested. Crowned so the ground falls ≥ 5% for 3 m (IRC R401.3) and paving ≥ 2%.
- **Test the soil at every site: plasticity index > 35 means expansive clay.** Porters Creek
  Clay, highly expansive, outcrops ~30 km from Hot Springs. On such soil, replace the pad with
  granular fill so it can't heave.
- Footings go ≥ 12 in below grade and below the frost line (Arkansas). Plinth units and pavers need ≤ 8–13% absorption (ASTM C4 / C67).

---

## 3. Units graded like bone: dense rims and skin, porous core

One print, several materials, all the **same site clay** so they shrink together:

| zone | mix | why | λ (W/mK) |
|---|---|---|---|
| **outer skin** 6–10 mm (or a dipped engobe ~0.5 mm) | clay + 10–20% fine glass cullet (+ grog to match shrinkage) | densifies at ~1,000 °C; engobes took absorption 14.8% → 3.2%, frost cycles 15 → 65 | 0.6–0.8 |
| **core webs** | clay + 10–15 vol% **rice husk** (coarse) | burned-out husk leaves fine pores: 4–10 MPa, λ 0.17–0.30 | 0.18–0.30 |
| **bearing rims** 15–25 mm | clay + sand/grog, no pore former | the dry-stack bearing faces: dense, strong, ground flat | 0.5–0.8 |
| **interior face** | clay + ~5% pore former, unglazed, open | breathes; finish with a thin **unfired clay plaster** for humidity buffering (MBV > 1) | ~0.6 |

**Result (`thermal_check.py`):** an 8 in graded unit gives **U ≈ 0.42 W/m²K (0.39 with an optimised
core), an 11–12 h time lag and decrement ~0.28**. That is a third better than the ungraded unit
(0.62) and six times better than compacted earth (2.69). It is also ~22% lighter. A 6 in graded
unit reaches the ~0.56 target on its own.

**Rules that stop graded prints from delaminating:**
1. Same base clay everywhere; change pore former or flux by ≤ ~10 vol% per step, **graded over
   5–10 mm, not switched abruptly**.
2. Keep total shrinkage of neighbouring zones within ~10% relative. Husk *lowers* shrinkage and
   cullet *raises* it, so balance the skin with grog.
3. Before production, fire **bilayer test bars** for every pair of neighbouring zones and reject any
   that bow.
4. **Firing:**
   - slow and oxidising through 200–700 °C so the husk burns out without black cores;
   - peak 1,000–1,080 °C; the skin needs ≥ 990 °C for frost durability;
   - **cool slowly through 600–540 °C** (quartz) **and 250–180 °C** (cristobalite from husk ash
     jumps 0.7% there).
5. Glass cullet is the skin flux. **Husk ash is not a flux**: it's silica, refractory at these temperatures.

---

## 4. How the three fit together
- The **coat** keeps rain and sun off. The **boots** carry water away. **Graded units** do the
  insulating and bearing, and never see weather.
- Durability moves to the parts that are **cheap and replaceable** (boards, tiles, pavers, render)
  and away from the parts that are hard to replace (clamped panels, dome).
- Every drop has a planned path from the dome to the cistern or the drain tile. None depends on a sealant.

## 5. Phase R additions
- Boards: extrude, fire, test absorption and freeze-thaw (ASTM C67), and load the lock in wind
  suction. Hang a 2 m test wall and spray it (ASTM E331-style).
- Apron and collector: build a 3 m segment and run a hose at the 10-yr and 100-yr flows.
- Graded bars: shrinkage and bowing for each zone pair, then λ of a graded unit by heat-flux meter.
- Soil at every site: plasticity index, carbonate fizz test, Proctor.
