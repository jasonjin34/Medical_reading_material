# An atlas of healthy and injured cell states and niches in the human kidney

> **Bibkey** `Lake_2023` · **Venue** Nature (2023) · **Category** spatial · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1038/s41586-023-05769-3> · `status: complete`

---

## One-liner
A KPMP / HuBMAP / HCA multimodal single-cell + spatial atlas of the human kidney: >400,000 cells/nuclei (snRNA, scRNA, SNARE-seq2 dual-omics) plus Slide-seq2, Visium and large-scale 3D imaging, spanning 45 healthy reference donors and 48 AKI/CKD patients; it defines 51 main cell types and **28 injury-associated "altered states"** (cycling, adaptive/maladaptive repair, transitioning, degenerative), localizes them to injury niches, and shows that TAL/PT adaptive-repair signatures predict decline of kidney function.

## Problem
After kidney injury, tubules and interstitium undergo dynamic acute and chronic changes; the balance between successful and maladaptive repair drives progression AKI → CKD → kidney failure. Understanding this needs single-cell definitions of **healthy reference states** and **injury-altered states**, their tissue location, neighbourhoods and interactions, and links to clinical outcomes. Earlier atlases mostly integrated healthy cell types and lacked systematic, cross-technology-validated definitions and spatial mapping of injury states.

## Method
**Single-cell multi-omics**: 10x Chromium v3 single-nucleus (snCv3) and single-cell (scCv3) RNA-seq, plus SNARE-seq2 (RNA + chromatin accessibility from the same nucleus). snCv3 is clustered first (100 clusters → 77 subclasses) and used as an anchor to map scCv3 and SNARE2 into one embedding with label transfer. **Altered states** are defined from prior studies and known injury features (Supplementary Table 10) and confirmed by mapping onto a mouse AKI (IRI) time-course. **Spatial**: Slide-seq2 (10 µm beads; 6 individuals, 67 pucks) and Visium (55 µm spots; 22 individuals, 23 samples) via deconvolution/label transfer and colocalization; 3D multiplexed immunofluorescence with label-free cytometry (3DTC, with SHG collagen) on 15 individuals for neighbourhood analysis (~1.2M neighbourhoods) and community detection into niches. **Downstream**: trajectory inference and RNA velocity, module detection, SNARE2 chromVAR TF activity and GRNs (including simulated TF perturbation), ligand–receptor analysis, GWAS/eQTL enrichment; clinical association in NEPTUNE (survival; composite of ESRD or 40% eGFR decline) and ERCB. Many samples were run on more than one assay for cross-validation and to reduce procurement/assay bias.

## Data
At abstract level: 45 healthy reference donors and 48 patients, >400,000 high-quality cells/nuclei; integrated transcriptomics covers 58 reference tissues (35 donors) and 52 diseased tissues (36 patients). Sources include healthy references (tumour-nephrectomy, deceased donors, living-donor biopsies) and KPMP AKI/CKD biopsies; single-cell assays used 15 CKD, 12 AKI and 18 living-donor biopsy cores. Visium: 146,460 spots over 22 individuals; 3DTC: 1,540,563 cells, 14 cell classes, 14 niches. Clinical: NEPTUNE (193 patients in text, 199 in the figure legend) and ERCB (131).

## Key results
- **Cell types**: 51 canonical types including rare and previously undescribed populations, with markers, open-chromatin maps and TF motifs; Slide-seq/Visium recapitulate renal corpuscle, JGA and corticomedullary transitions (ATL→M-TAL→C-TAL).
- **28 altered states**: degenerative states express SPP1, CST3, CLU, IGFBP7 with a shared FOS/JUN signature, appear early after mouse injury and fade on recovery; adaptive PT (aPT: VCAM1, DCDC2, HAVCR1) matches rodent failed repair; a new **adaptive TAL (aTAL: PROM1/CD133, DCDC2, ITGB6)** persists 6 weeks after mouse AKI; stromal altered states include MyoF, cycMyoF and aFIB (POSTN, FAP, ACTA2, collagens). **Key caveat**: altered states also occur in reference tissue, possibly from ischaemic stress during acquisition or normal ageing.
- **Spatial injury niches**: altered signatures are enriched in AKI/CKD Visium spots; immune and stromal cells colocalize more with altered epithelium; in 3DTC, CD3+ T cells occur almost only in neighbourhoods with epithelial degeneration and fibrosis (N13), while myeloid (CD68+) cells sit in healthier, actively repairing areas.
- **Repair trajectories and signalling**: aEpi trajectories run from dedifferentiated to mature states, enriched for Wnt, Notch, TGF-β, EGF, MAPK, JAK/STAT, NF-κB; GRNs highlight TFAP2B (written "TRAP2B" in the text; AP-2β), whose simulated perturbation disrupts the repair trajectory; early aTAL repair states interact first with immune, then (mid-repair) with stromal cells (NRG1/NRG3, NECTIN2, BMP6, IGF1).
- **Clinical association**: NEPTUNE Kaplan–Meier by state score: aPT P = 0.021, **aTAL P = 0.003**, degenerative P = 0.55 (log-rank trend); in ERCB, diabetes, hypertension and FSGS patients have higher aPT and shared aPT–aTAL signatures than living donors (diabetes remains higher after adjusting for age, sex and eGFR). eGFR/CKD causal variants are enriched in TAL regulatory regions (ESRR motifs). The authors caution the clinical sample sizes are small.

## Contributions
- The first human kidney healthy + injury atlas **cross-validated** across snRNA/scRNA/SNARE2/Slide-seq/Visium/3D imaging under one annotation scheme.
- Systematic definition of altered states (cycling / adaptive / transitioning / degenerative), now the shared vocabulary and reference for kidney single-cell work.
- Identification of the aTAL state, elevating TAL as a central segment in disease progression.
- Public interactive resources: Azimuth reference mapping, cellxgene, KPMP Atlas Explorer.

## Limitations
- Altered states are defined manually from prior knowledge, not discovered unsupervised, and they also appear in "healthy" references (acquisition ischaemia, ageing) — the healthy/abnormal boundary is itself blurry.
- Small clinical association samples (acknowledged) and associational, not causal; some time-course inferences rely on mouse IRI.
- Visium's 55 µm spots allow colocalization, not single-cell spatial analysis; no subcellular platforms like Xenium.
- KPMP raw sequencing data is controlled-access; tissue sources (nephrectomy, deceased donor, biopsy) differ in procurement.

## Relation to our direction
This is **Plan A's reference backbone**. The "detect" stage of detect → model → revert needs a reference manifold of "normal", and Lake 2023 is the de-facto kidney healthy reference plus injury-state annotation: (1) the **Azimuth healthy reference** can serve directly as the anomaly-detection reference (map our 95-biopsy snRNA onto it; low mapping confidence/large distance = candidate anomaly); (2) the **28 altered states give weak labels for "known anomalies"** — KidneyAnomalyBench can use them as a first tier (does a label-blind detector rank aPT/aTAL/degenerative cells highest?), then treat high-scoring cells *outside* Lake's labels as candidate discoveries for expert validation; (3) its admission that altered states also appear in reference tissue (acquisition ischaemia, ageing) is exactly the confound Plan A's cross-modal agreement idea targets: a cell that looks "injured" in one modality but disagrees in snATAC/Xenium/H&E is more likely a procurement artifact; (4) running the same samples across technologies is the direct precedent for our snRNA + snATAC + Xenium + H&E design; (5) it is a main source of the open KPMP data used by the NIH Kidney AI challenge, and its cell states support the challenge's criterion-3 patient stratification. For "model/revert": the simulated TFAP2B perturbation disrupting the repair trajectory is an early GRN-level "virtual perturbation" to compare against virtual-tissue predictions. For **Plan B**, it is the most-cited "known result" an agent analysing kidney omics will reach for — useful for building claim-to-evidence ground truth (e.g. "aTAL markers are PROM1/DCDC2/ITGB6") and tests of "restating literature vs deriving from data".

## Reusable assets
- **Data (processed):** GEO Superseries GSE183279 (snCv3, scCv3, SNARE2, Slide-seq, Visium).
<https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE183279>
- **Reference mapping:** Azimuth human kidney reference (snCv3 healthy reference).
<https://azimuth.hubmapconsortium.org/>
- **Visualization:** cellxgene collection and KPMP Atlas Explorer; 3D cytometry data on Zenodo.
<https://cellxgene.cziscience.com/collections/bcb61471-2a44-4d00-a0af-ff085512674c> · <https://atlas.kpmp.org/explorer/> · <https://doi.org/10.5281/zenodo.7120941>
- **Code:** figure-reproduction code.
<https://github.com/KPMP/Cell-State-Atlas-2022>
- **Raw data:** KPMP repository (raw sequencing controlled; 3D imaging raw data freely downloadable).
<https://atlas.kpmp.org/repository/>

## Follow-ups
- Kirita et al. mouse AKI time-course (used here to time the altered states).
- Follow-ups that score injury against Lake-style references: damage-scores (Padvitski 2026), CellSpectra (Klötzer 2025) and the DKD spatial atlas (Dumoulin 2026) in this repo.
- Later KPMP Xenium / multi-omics releases and HuBMAP kidney data, to match our modality set.

## Cite
```bibtex
@article{Lake_2023, title={An atlas of healthy and injured cell states and niches in the human kidney}, volume={619}, ISSN={1476-4687}, url={http://dx.doi.org/10.1038/s41586-023-05769-3}, DOI={10.1038/s41586-023-05769-3}, number={7970}, journal={Nature}, publisher={Springer Science and Business Media LLC}, author={Lake, Blue B. and Menon, Rajasree and Winfree, Seth and Hu, Qiwen and Melo Ferreira, Ricardo and Kalhor, Kian and Barwinska, Daria and Otto, Edgar A. and Ferkowicz, Michael and Diep, Dinh and Plongthongkum, Nongluk and Knoten, Amanda and Urata, Sarah and Mariani, Laura H. and Naik, Abhijit S. and Eddy, Sean and Zhang, Bo and Wu, Yan and Salamon, Diane and Williams, James C. and Wang, Xin and Balderrama, Karol S. and Hoover, Paul J. and Murray, Evan and Marshall, Jamie L. and Noel, Teia and Vijayan, Anitha and Hartman, Austin and Chen, Fei and Waikar, Sushrut S. and Rosas, Sylvia E. and Wilson, Francis P. and Palevsky, Paul M. and Kiryluk, Krzysztof and Sedor, John R. and Toto, Robert D. and Parikh, Chirag R. and Kim, Eric H. and Satija, Rahul and Greka, Anna and Macosko, Evan Z. and Kharchenko, Peter V. and Gaut, Joseph P. and Hodgin, Jeffrey B. and Knight, Richard and Lecker, Stewart H. and Stillman, Isaac and Amodu, Afolarin A. and Ilori, Titlayo and Maikhor, Shana and Schmidt, Insa and McMahon, Gearoid M. and Weins, Astrid and Hacohen, Nir and Bush, Lakeshia and Gonzalez-Vicente, Agustin and Taliercio, Jonathan and O’toole, John and Poggio, Emilio and Cooperman, Leslie and Jolly, Stacey and Herlitz, Leal and Nguyen, Jane and Palmer, Ellen and Sendrey, Dianna and Spates-Harden, Kassandra and Appelbaum, Paul and Barasch, Jonathan M. and Bomback, Andrew S. and D’Agati, Vivette D. and Mehl, Karla and Canetta, Pietro A. and Shang, Ning and Balderes, Olivia and Kudose, Satoru and Barisoni, Laura and Alexandrov, Theodore and Cheng, Yinghua and Dunn, Kenneth W. and Kelly, Katherine J. and Sutton, Timothy A. and Wen, Yumeng and Corona-Villalobos, Celia P. and Menez, Steven and Rosenberg, Avi and Atta, Mohammed and Johansen, Camille and Sun, Jennifer and Roy, Neil and Williams, Mark and Azeloglu, Evren U. and He, Cijang and Iyengar, Ravi and Hansen, Jens and Xiong, Yuguang and Rovin, Brad and Parikh, Samir and Madhavan, Sethu M. and Anderton, Christopher R. and Pasa-Tolic, Ljiljana and Velickovic, Dusan and Troyanskaya, Olga and Sealfon, Rachel and Tuttle, Katherine R. and Laszik, Zoltan G. and Nolan, Garry and Sarwal, Minnie and Anjani, Kavya and Sigdel, Tara and Ascani, Heather and Balis, Ulysses G. J. and Lienczewski, Chrysta and Steck, Becky and He, Yougqun and Schaub, Jennifer and Blanc, Victoria M. and Murugan, Raghavan and Randhawa, Parmjeet and Rosengart, Matthew and Tublin, Mitchell and Vita, Tina and Kellum, John A. and Hall, Daniel E. and Elder, Michele M. and Winters, James and Gilliam, Matthew and Alpers, Charles E. and Blank, Kristina N. and Carson, Jonas and De Boer, Ian H. and Dighe, Ashveena L. and Himmelfarb, Jonathan and Mooney, Sean D. and Shankland, Stuart and Williams, Kayleen and Park, Christopher and Dowd, Frederick and McClelland, Robyn L. and Daniel, Stephen and Hoofnagle, Andrew N. and Wilcox, Adam and Bansal, Shweta and Sharma, Kumar and Venkatachalam, Manjeri and Zhang, Guanshi and Pamreddy, Annapurna and Kakade, Vijaykumar R. and Moledina, Dennis and Shaw, Melissa M. and Ugwuowo, Ugochukwu and Arora, Tanima and Ardayfio, Joseph and Bebiak, Jack and Brown, Keith and Campbell, Catherine E. and Saul, John and Shpigel, Anna and Stutzke, Christy and Koewler, Robert and Campbell, Taneisha and Hayashi, Lynda and Jefferson, Nichole and Pinkeney, Roy and Roberts, Glenda V. and Eadon, Michael T. and Dagher, Pierre C. and El-Achkar, Tarek M. and Zhang, Kun and Kretzler, Matthias and Jain, Sanjay}, year={2023}, month=July, pages={585–594} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
