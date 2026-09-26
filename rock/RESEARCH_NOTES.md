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

## Joinery, stone keys and dry domes
- Kanawa-tsugi: the wedge (sen) goes in last and pre-compresses the stepped bearing faces; tension
  becomes bearing; beats okkake-daisen-tsugi in a carpenter's comparison (snip).
  https://www.kyoto-araki.jp/kyomachiya/kigumi/kanawa.html
- Shachi-sen paired wedges draw the tenon tight, with ~3 mm spare travel to re-drive after
  shrinkage; komisen draw-pins through offset holes pull the joint shut and can be driven out.
  https://www.quaggadesigns.com/blog/yato-hozo-shachi-sen-shiguchi-japanese-joinery-explained
- Nuki wedges 1–2 mm oversize raise stiffness and capacity; loops pinch after embedment (Chang,
  Komatsu et al., Eng. Struct. 2008).
  https://www.sciencedirect.com/science/article/abs/pii/S0141029608000114
- Dougong fails by splitting at the tenon's section change: the brittle-mode warning.
  https://www.sciencedirect.com/science/article/abs/pii/S2352012422009596
- Inca dry walls came through the 1650 and 1950 Cusco quakes with minor fractures; poured bronze
  I/T cramps at some sites. https://en.wikipedia.org/wiki/Inca_architecture
- Greek anathyrosis (contact only on a dressed rim band); iron cramps set in lead lasted ~2,400
  years; Balanos's steel-in-concrete repairs rusted and split the marble; titanium since, fine for
  30+ years. https://en.wikipedia.org/wiki/Anathyrosis ;
  https://www.ysma.gr/en/monuments/parthenon/completed-interventions/
- Multi-drum columns on shake tables rock and slide with little permanent offset.
  https://link.springer.com/article/10.1007/s10518-014-9608-y
- Egyptian dovetail cramps of African blackwood (Medinet Habu). https://www.blackwoodconservation.org/5000-year-history/
- Armadillo Vault (Venice 2016): 399 dry limestone blocks, ~16 m span, 5 cm at the crown to
  8–12 cm at the supports, funicular, ties take the thrust.
  https://www.istructe.org/structural-awards/projects/2017/armadillo-vault/
- Striatus (2021): dry-assembled printed concrete blocks, layers aligned with the compression flow,
  demountable. https://www.zha.com/design/striatus/
- Nubian vaults: courses lean ~60°, held by earth-mortar suction until closed; ~3.2 m span.
  https://www.earth-auroville.com/la_voute_nubienne_en.php
- Auroville Dhyanalinga dome: 22.16 m, fired brick, no formwork, 53 → 21 cm thick.
  https://dev.earth-auroville.com/dhyanalinga-dome/
- Dome minimum thickness: hemisphere t/R ≈ 0.042 (Heyman), 0.0428 (Coccia et al. 2016); segmental
  ≈ 0.04 (Zessin, Lau & Ochsendorf); hoop tension below 51.8° from the crown in membrane theory.
  https://link.springer.com/article/10.1007/s00707-016-1630-5 ; https://www.mdpi.com/2075-5309/11/6/241
- St Peter's cracked despite iron hoops; Poleni added five more in the 1740s.
  https://www.sciencedirect.com/science/article/pii/S2095263522000784
- Corner confinement of dry-stack walls: +64% lateral load, +288% drift (snip).
  https://www.sciencedirect.com/science/article/abs/pii/S0267726122005553
- Interlocking assemblies: recursive puzzles (Song, Fu, Cohen-Or 2012); DESIA (Wang, Song, Pauly
  2018); topological interlocking assemblies (Wang et al. 2019). https://dl.acm.org/doi/10.1145/3272127.3275034
- **Gaps:** no shake tests of Inca walls; no data on fired-clay interlocking keys; Armadillo and
  Striatus interface pads not confirmed (paywalled).

## Building systems to synthesize (precedents)
- Dieste reinforced ceramic: Gaussian vaults to ~45 m, 18–25 cm thick, steel in grouted joints,
  prestressed lengthwise; movable formwork reused strip by strip. https://en.wikipedia.org/wiki/Gaussian_vault
- Guastavino tile vaults: first layer set in fast-setting gypsum = no formwork (needs adhesion).
  https://en.wikipedia.org/wiki/Guastavino_tile
- SUDU (Addis Ababa 2010): 5.8 m floor vault <10 cm; diaphragms critical under asymmetric load;
  double curvature more stable; waterproofing "very delicate"; build 2 prototypes, test 1 to failure.
  https://block.arch.ethz.ch/brg/files/Block_2010_ATDF_tile-vaulted-systems-for%20africa_1425211564.pdf
- Mapungubwe: ~200,000 site-pressed tiles (5 MPa), vaults 5–20 m, ~$110/m², 31 labour-h/m², ~30%
  cheaper than an RC shell, 100+ trained; unskilled easier to train than relying on existing skills.
  https://block.arch.ethz.ch/brg/files/Ramage_2010_ATDF_Mapungubwe_1425208976.pdf
- Isler shells: light prestress "practically eliminates" cracking (secondary).
- Segal self-build (Lewisham): dry, bolted, demountable, one grid; needed land + a sponsor.
  https://world-habitat.org/awards/winners/walter-segal-self-build-housing-project-london/
- WikiHouse: 0.1 mm CNC blocks, mortgageable after a 10-year structural warranty; each building
  still needs engineer sign-off; the sawtooth roof leaked. https://www.wikihouse.cc/product
- Open Source Ecology CEB press: 16 bricks/min in trials, ~0.5/min sustained by one shoveller.
  https://www.opensourceecology.org/liberator-2-production-rate-calculations/
- Elemental Quinta Monroy: 92 of 93 households expanded; welding-spark fires in add-ons.
  http://www.scielo.br/j/urbe/a/ZCgQWz9QtCjQhSdxvxQQY6q/?lang=en
- Confined masonry: 1–2 storey houses mostly undamaged in Maule 2010; wall density 2–5%.
  https://www.confinedmasonry.org/wp-content/uploads/2009/09/ConfinedMasonryDesignGuide82011.pdf
- Low-cost isolation: geotextile sliding plinth ~70% less roof acceleration, 50 mm slide (Nanda);
  rubber-soil 40–50%; mostly lab/scale evidence.
- Rubble trench, frost-protected shallow foundations, capillary breaks: see HUD FPSF guide,
  https://buildingscience.com/documents/building-science-insights-newsletters/bsi-123-capillarity-sucks
- Nubian Vault Association: 7,000+ houses, ~1,200 masons; plastic + ≥6 cm plaster in wetter climates.
- Hydraform dry-stack house on a shake table: minor damage, 4.6 mm permanent shift.
  https://scielo.org.za/scielo.php?script=sci_arttext&pid=S1021-20192011000100003

## Climate, envelope, water, kilns, energy
- Hot Springs July: 33.3 °C high / 21.5 °C low, dew point ≥18 °C: summer is humidity-limited.
- Fans: comfort limit 25.6 → ~28.3 °C at 0.5 m/s. https://cbe-berkeley.gitbook.io/fans-guidebook/
- Night flushing negligible in humid Kumasi. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3708435/
- Earth tubes condense and mold in humid climates; radiant cooling needs dehumidification.
- RH <50% vs ≥70% slows mold growth up to ~90%. https://www.epa.gov/mold/mold-course-chapter-2
- Kahgel mud roofs need renewal every 1–2 years; Auroville domes: lime-alum-tannin top coat.
  https://www.earth-auroville.com/stabilised_earth_waterproofing_en.php
- Cocciopesto: lime + crushed fired brick, Roman cisterns.
  https://www.unrv.com/articles/how-romans-waterproofed-buildings-baths-and-cisterns.php
- ASTM C216 SW: 5-h boil ≤17% (avg), saturation coefficient ≤0.78, or cold absorption ≤8%.
  https://s3.amazonaws.com/brickit-images/files/ASTM_C_216.pdf
- Firing 1,000–1,100 °C: 13.8–18.2 MPa, 6–9% absorption; calcareous clays need ~1,100 °C.
  https://nopr.niscpr.res.in/bitstream/123456789/4811/1/JSIR%2065(2)%20153-159.pdf
- Efflorescence sources are mostly cement and soil contact. https://www.gobrick.com/media/file/23a-tn23a.pdf
- VSBK 0.84, zigzag 1.16, FCBTK ~1.59 MJ/kg; zigzag −80% PM2.5 vs FCBTK.
  https://www.osti.gov/pages/servlets/purl/3484616 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC9447410/
- First flush 1–2 L/m²; ferrocement tanks 50–100 year life.
- LFP 4,000–6,000 cycles to 80%; heat shortens life. https://www.okrasolar.com/blog/a-better-way-to-estimate-battery-lifetime
- Mini-grids: Sundarbans plants abandoned (no O&M); Chhattisgarh 1,400+ succeeded.
  https://link.springer.com/article/10.1186/s13705-018-0185-9
