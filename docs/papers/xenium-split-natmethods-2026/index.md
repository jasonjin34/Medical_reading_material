# Resolving sensitivity, specificity and signal contamination in Xenium spatial transcriptomics

> **Bibkey** `Bilous_2026` · **Venue** Nature Methods (2026) · **Category** spatial · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1038/s41592-026-03089-8> · `status: complete`

---

## One-liner
Using 41 breast-cancer and NSCLC sections from 27 donors (targeted Breast/Lung/Custom IO panels plus the 5K PRIME panel, with matched snRNA-seq and IHC), the authors systematically characterize Xenium sensitivity, specificity and **transcript-spillover contamination**, and propose SPLIT: take RCTD doublet-mode cell-type weights and split each contaminated cell's counts into "primary" and "secondary" parts according to reference profiles, keeping the purified primary profile.

## Problem
Xenium is widely adopted, yet its data properties lack large-scale characterization: prior comparisons covered few patients or tissue microarrays, and none directly compared targeted panels with the 5K panel for sensitivity/specificity. More importantly, segmentation errors and **in-plane (x–y)** spillover of transcripts into neighbours create "artificial transcriptomic doublets" — not physical doublets in the single-cell sense but signal-level mixing; z-axis overlap explains only part of it. Existing corrections (weighted NMF + CRF, resolVI, FastReseg, ProSeg, etc.) are either heuristic or hard to interpret, and validated on few samples.

## Method
**Annotation**: RCTD in doublet mode with matched snRNA-seq (or an external scRNA-seq) reference estimates each Xenium cell's primary/secondary cell types and weights w1, w2; the authors stress that RCTD "doublets" in Xenium are almost never true doublets, so cells with a secondary signal are called "contaminated" and those without "pure". **Spillover quantification**: compare a cell's contamination w2 with the local abundance of that same (secondary) cell type in its 2D neighbourhood; high cosine similarity → contamination comes from neighbour spillover; averaging over cell-type pairs gives a **spillover index** measuring each type's tendency to contaminate others. **SPLIT**: using RCTD weights and reference profiles, proportionally assign each contaminated cell's transcripts to primary vs secondary sources and keep the primary profile by default; optional **spatial gating** decomposes only where the secondary type is actually abundant nearby, avoiding splitting real phenotypes absent from the reference (e.g. cycling tumour cells); **SPLIT-shift** can reassign the primary phenotype to a secondary one based on neighbourhood homogeneity. **Orthogonal validation**: multiplex IHC after Xenium (CD8, tumour markers). **Comparison**: SPLIT vs resolVI vs ovrlpy, crossed with default 5-µm expansion, nucleus-only (0 µm), multimodal, Baysor, ProSeg and Segger segmentation, scored on scib bioconservation/batch, retained cells and genes, malignant→T-cell contamination strength (neighbourhood logistic regression), and cosine similarity to Chromium T-cell pseudobulk.

## Data
Generated data: 19 breast-cancer FFPE sections (17 donors) + 22 NSCLC FFPE sections (10 donors), 41 total; breast with the Breast targeted panel, NSCLC with the Lung targeted panel, a custom immuno-oncology panel (Custom IO) and the 5K PRIME panel; some samples have technical replicates (adjacent sections), matched snRNA-seq (Chromium) and multiplex IHC. External references: an extended lung-cancer scRNA atlas (318 patients, >1M cells) and the Wu et al. breast scRNA. Public Xenium data were used to confirm spillover generality. Xenium data at GEO GSE311609; snRNA references on cellxgene.

## Key results
- **High reproducibility**: technical replicates (adjacent sections) agree almost perfectly; with only Seurat log-normalization and no integration, non-malignant cells align across patients (malignant cells cluster by patient, as expected).
- **Targeted panels are more sensitive than 5K**: restricted to 194 shared genes, 5K and Lung separate cell types comparably, but **~60% of 5K cells fail QC for low transcript counts**, detecting far fewer transcripts for the same genes — sensitivity close to Chromium; cell-type composition still agrees well across panels; the two targeted panels (sharing only 87 genes) agree best.
- **Spillover is pervasive**: w2 is strongly cosine-similar to neighbourhood abundance of the same type, reproducibly across public multi-tissue Xenium data and segmentations; more abundant types have higher spillover indices, **malignant cells highest**; IHC shows tumour-specific transcripts extending into adjacent CD8+ T cells, sometimes strongly enough that RCTD swaps primary and secondary; low-RNA cells (e.g. T cells) are hit hardest.
- **Nucleus-only segmentation (0 µm) is still contaminated**, and correction helps; 5K with multimodal segmentation shows much lower contamination, though the authors caution this may just reflect lower statistical power from fewer transcripts per gene.
- **Method comparison**: all corrections improve cell-type separation and reduce contamination; **SPLIT gives the best separation and the highest cosine similarity to Chromium profiles** (the authors concede this partly follows from SPLIT using the Chromium reference); **ovrlpy and resolVI substantially reduce detected genes, leaving many near-empty cells**; resolVI sometimes slightly worsens iLISI. Among segmenters ProSeg beats Baysor, multimodal and Segger; **ProSeg + SPLIT is best overall**. Breast samples agree.
- **Biology**: uncorrected, tumour-adjacent T cells show spurious malignant/epithelial signatures; after SPLIT, T cells near tumour show stronger exhaustion signatures (HAVCR2/TIM-3, CTLA4, PDCD1, LAG3, CXCL13); resolVI and ovrlpy are inconsistent, with resolVI occasionally suppressing both contamination and T-cell programs.

## Contributions
- One of the largest systematic Xenium evaluations, and the first direct comparison of targeted vs 5K panels on the sensitivity–coverage trade-off.
- Reinterprets RCTD doublet weights as a **contamination measure** and introduces a cell-type-level **spillover index**.
- SPLIT: a simple, interpretable, reference-based signal decomposition that composes with any segmentation and uses spatial gating to avoid over-correction.
- Orthogonal validation with IHC protein signal (protein staining is less prone to spillover).

## Limitations
- **Reference-dependent**: states absent from the reference can be wrongly split; a reference-free version is planned.
- Primary analyses cover only two cancer types; each cell is modelled with only a primary plus one secondary source.
- The "most similar to Chromium" metric favours SPLIT (acknowledged); the comparison with resolVI contradicts resolVI's own paper — each group wins on metrics it designed.
- Lower 5K contamination may be purely a power artefact; not disentangled.

## Relation to our direction
For **the artifact-injection topic** this is close to an operating manual: a multi-modal design of this kind (snRNA + snATAC + Xenium + H&E) **has both snRNA/snATAC and Xenium**, exactly SPLIT's prerequisite of a matched snRNA reference + RCTD. Three directly usable pieces: **(1) "contaminated vs pure" + spillover index as artifact labels** — in kidney, proximal-tubule cells are the most abundant type and will likely play this paper's "malignant cell" role, spilling into small, RNA-poor immune cells; in KidneyAnomalyBench an "immune cell expressing PT markers" anomaly that tracks neighbourhood PT abundance should be ranked as probable spillover. **(2) Cross-modal agreement**: validating transcript signals with spillover-resistant IHC is isomorphic to the artifact-injection topic's "cross-modal agreement separates artifacts from disease" — mappable to H&E morphology and snATAC. **(3) Panel choice**: the 5K panel's low sensitivity (~60% of cells failing QC) means low-count cells are themselves an anomaly source and must be stratified. **Key tension**: SPLIT is reference-driven, so states absent from the reference get split back into known types — yet anomaly detection is precisely about what the reference lacks. Running SPLIT with a healthy reference could "purify" disease-specific states (e.g. the inflammatory PT of `inflammatory-pt-natcommun-2025`) into ordinary PT. Use a disease-inclusive reference or the spatially gated mode, and make "anomaly stability before vs after correction" part of the benchmark. For **the agent-trustworthiness topic**: this paper and the resolVI paper rank the same methods oppositely — a textbook case of "authors choose the metrics → self-evaluation bias", a good exemplar for the claim-to-evidence class "comparative claims need independent evidence"; the authors' cautious reading of 5K's low contamination (possibly low power) is also the kind of reasoning an agent should reproduce.

## Reusable assets
- **Code:** the SPLIT R package, the full Xenium analysis pipeline, and reproduction code.
<https://github.com/bdsc-tds/SPLIT>
<https://github.com/bdsc-tds/xenium_analysis_pipeline>
<https://github.com/bdsc-tds/Bilous2026>
- **Data:** 41 Xenium sections (GEO GSE311609) and matched snRNA references (cellxgene).
<https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE311609>
<https://cellxgene.cziscience.com/collections/bd552f76-1f1b-43a3-b9ee-0aace57e90d6>
- **Eval protocol:** the full segmentation × correction grid; neighbourhood logistic regression for contamination strength; the spillover index.

## Follow-ups
- Marco Salas et al.'s Xenium quality assessment; Mitchel et al. on misassignment-driven spurious communication; ProSeg (Jones et al.).
- Reproduce the resolVI / SPLIT / ovrlpy three-way comparison on kidney Xenium to see whether conclusions depend on tissue and metric.

## Cite
```bibtex
@article{Bilous_2026, title={Resolving sensitivity, specificity and signal contamination in Xenium spatial transcriptomics}, volume={23}, ISSN={1548-7105}, url={http://dx.doi.org/10.1038/s41592-026-03089-8}, DOI={10.1038/s41592-026-03089-8}, number={6}, journal={Nature Methods}, publisher={Springer Science and Business Media LLC}, author={Bilous, Mariia and Buszta, Daria and Bac, Jonathan and Kang, Senbai and Dong, Yixing and Tissot, Stephanie and Andre, Sylvie and Alexandre Gaveta, Marina and Voize, Christel and Peters, Solange and Homicsko, Krisztian and Gottardo, Raphael}, year={2026}, month=Apr, pages={1152–1162} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
