# Research notes: rock routes, dry-stack, printing
### Sourced figures behind `data/rock_routes.json`, `rock/ROCK_OPTIONS.md` and `making-system/BRICK_PANEL.md`

Gathered 2026-09-26 by literature search. **(S)** = read in the primary document; **(snip)** =
from an abstract or search summary, so check the URL before citing; **UNSOURCED** = estimate or
calculation. Many publisher pages were paywalled.

## Firing clay
- Kiln energy (MJ/kg fired brick), averages (S): clamp 3.0, fixed-chimney 1.4, zigzag 1.1, hybrid
  Hoffmann 1.2, VSBK 0.9, tunnel 2.5; overall 0.5–5. https://pmc.ncbi.nlm.nih.gov/articles/PMC11800390/
- Clamps internationally 1.9–7.2 MJ/kg (snip). https://breathelife2030.org/wp-content/uploads/2016/09/12.pdf
- Firing 980–1150 °C (S): BIA TN 3A https://www.gobrick.com/media/file/TN_3A_Brick_Masonry_Material_Properties.pdf
- Times and shrinkage (S): drying 24–48 h, firing 10–40 h, cooling ≤10 h (tunnel) or 5–24 h
  (periodic); shrinkage 2–4% drying + 2.5–4% firing. BIA TN 9 https://www.gobrick.com/media/file/9-manufacturing-of-brick.pdf
- US unit compressive strength (S, TN 3A): extruded 77.9, molded 36.5, hollow 46.4 MPa. Masonry
  modulus of rupture only 0.35–2.3 MPa.
- Prefabricated brick panels (S): storey height, some prestressed, since the 1950s (France,
  Switzerland, Denmark); US SCR panel; ASTM C901; lifting devices ≥4× dead weight; stainless
  304/316 or coated ties. BIA TN 40 https://www.gobrick.com/media/file/40-prefabricated-brick-masonry---introduction.pdf
- Large porcelain slabs 1600×3200 mm at 6–20 mm (snip). https://www.xtone-surface.com/en/products/porcelain-slabs/

## Killed or niche routes
- **In-situ vitrification** (S): 0.72 MWh/t measured (vendor ~1 MWh/t); ~3.5 MW; 1600–2000 °C;
  melts take 1–2 years to cool; $370–740/t (1995). EPA https://semspub.epa.gov/work/HQ/189960.pdf
- **Cast basalt** (S): ≥300–450 MPa compressive, ≥45 MPa bending, 2900–3000 kg/m³.
  https://m.eutit.com/files/ke_stazeni_aj/e01_basalt_en.pdf
- **Microwave sintering** (snip): lab energy 69–98 MJ/kg; lunar results depend on nanophase
  metallic iron, which Earth soils lack.
- **Khalili Geltaftan** (S): house fired as its own kiln, oil burners ~24 h, ≥1000 °C, ≥48 h
  cooling; abandoned for fuel cost and pollution. https://en.wikipedia.org/wiki/Ceramic_house
- **Sulfur concrete** (S, ACI 548.2R-93): 15–17.5% sulfur cement; mixed at 127–141 °C; ≥27.6 MPa
  and 5.2 MPa flexural at 1 day; no swelling clay, aggregate absorption <2%. Melts at 115–120 °C,
  ignites at 232 °C. http://civilwares.free.fr/ACI/MCP04/5482r_93.pdf
- **Bio-cement** (snip): EICP ~8% CaCO₃ gives >4 MPa, ~20% gives >10 MPa; sands only. Per kg of
  CaCO₃: 0.60 kg urea + 1.11 kg CaCl₂ in, 1.07 kg NH₄Cl out (stoichiometry). Biolith tile 25 MPa,
  interior only. https://www.sciencedirect.com/science/article/pii/S2949929123000074
- **Geopolymer** (snip): soil geopolymer ~9–15 MPa; one-part metakaolin 38.8 MPa at 28 d;
  activator ~10% of precursor; heat cure cuts flexural strength 38–45%.
- **Cement with clay soil** (snip): 10–14% cement gave 1.5–3.4 MPa.
  https://pubs.acs.org/doi/10.1021/acsomega.4c10911
- **Sand-lime** (snip): autoclaved at 170–200 °C and 0.85–1.6 MPa for 6–12 h, ~10–30 MPa.

## Dry-stack and interlocking
- Hydraform (S): units bear on their shoulders with a 3–4 mm gap at the key; wall strength 0.2–0.4
  of unit strength. https://www.irbnet.de/daten/iconda/CIB17357.pdf
- Dry-stack vs mortared prisms (S): −15% strength, −62% stiffness; cohesion 0; friction 0.48–0.62.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC5458854/
- TMS 1430-21: unground dry-stack assemblies are limited to ~10.3 MPa.
  https://www.structuremag.org/article/new-dry-stack-guidelines-from-the-masonry-society/
- Contact and interlayers (S): raw dry joints reach 23% contact; face shells split at 17–92% of
  ultimate; a 7 GPa interlayer gave 55% contact and +31.9% capacity; a soft 3 GPa layer gave
  −41.3%. https://orbilu.uni.lu/bitstream/10993/46894/1/p_8307_Chewe_Ngapeya_Gelen_Gael_final.pdf
- Poroton Plan-T10 Dryfix (S): height ±0.5 mm, range 0.5 mm, flatness ≤0.2 mm, parallelism
  ≤0.6 mm; PU foam beads.
  https://www.wienerberger.de/content/dam/wienerberger/germany/marketing/documents-magazines/technical/approvals/DE_MKT_DOC_TEC_PON_Z-17.1-1088_Plan-T10%20Dryfix.pdf
- Standard tolerance classes (EN 771-1 T2/R2; ASTM C652 HBX ±1.6–7.1 mm) are 5–10× too loose for
  dry-stack; industry grinds after firing.
- Post-tensioned dry-stack (snip): Kohail et al. 2019 (+66.6% lateral capacity with
  precompression); Sokairge et al. 2017 (web-shear failure with thin webs). Laursen: axial ratio
  0.12–0.17 f′m.
- Post-tensioned masonry rules (S, CMHA TEK 14-20A): zero net tension at transfer; bearing
  ≤0.5 f′mi; losses ~35% for concrete masonry. Brick ≥20%. Threaded bars lost 16.4% vs 5.4% for
  greased strand over 180 days (snip). Clay moisture expansion +3×10⁻⁴ (BIA TN 18).
- Topological interlocking (S): PNAS 2018: 50× toughness, ~25× impact energy, best angle ~20°.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC6140525/ Survives loss of 25% of blocks (snip).
  Needs a peripheral constraint, for example tendons.

## Clay printing
- Layer height 25–75% of nozzle (general); clay about 35–50% (snip, Eazao/academia).
- Overhang ~30° safe; triangular infill in terracotta to ~60° (snip).
- Cracking causes (S, WASP FAQ): uneven shell thickness, fast or uneven drying, stiff paste,
  non-absorbent beds. https://www.3dwasp.com/en/faq/shrinkage-drying-deformation-and-cracking/
- Anisotropic shrinkage: stoneware ~13% Z vs ~8% XY; robocast clay 8.2/9.1/10.8% (X/Y/Z).
  https://pmc.ncbi.nlm.nih.gov/articles/PMC11012627/
- Printed fired strength 18–33 MPa for local terracotta (snip); printed chamotte 31.4 vs cast 30.4 MPa (snip).
- WASP 40100 LDM: 4/6/8 mm nozzles, layers 0.5–5 mm, up to 150 mm/s.
  https://www.3dwasp.com/wp-content/uploads/2024/01/WASP-40100-LDM-Technical-Sheet.pdf
- HKU Ceramic Constellation: ~2,000 printed bricks, 2–3 min per brick, fired at 1025 °C.
- **Gap:** no tested printed, fired, dry-stack, load-bearing clay wall system was found.
