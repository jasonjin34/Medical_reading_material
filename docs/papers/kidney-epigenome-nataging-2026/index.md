# A cross-species single-cell kidney epigenome atlas reveals epithelial-dominant aging-like states in disease

> **Bibkey** `Jeong_2026` · **Venue** Nature Aging (2026) · **Category** single-cell · **Relevance** medium · **Access** open
> **Link** <https://doi.org/10.1038/s43587-026-01221-z> · `status: complete`

---

## One-liner
The authors build a cross-species (human + mouse) single-cell kidney epigenome atlas — single-cell DNA methylation (sciMET) + matched 10x Multiome (RNA+ATAC) + Xenium 5K spatial transcriptomics + scMethyl-Hi-C — and find that **disease-associated epigenetic age acceleration is concentrated in tubular epithelial cells** (on average 4.8 years), that altered PT cells' methylation and expression changes overlap normal-aging transcriptional trajectories, preferentially hit CpG-island-less lineage genes, and map to spatial niches of unresolved repair.

## Problem
Epigenetic aging is a hallmark of chronic diseases including CKD, but bulk analyses cannot say which cell types "age faster"; existing single-cell kidney studies cover transcriptome and chromatin accessibility but lack deeper, more stable epigenetic layers — DNA methylation (a long-term record of cell state) and 3D genome architecture (the physical topology of regulation). The relationship between normal age-related epigenetic drift and disease-specific alterations is also unclear.

## Method
**Single-cell methylation**: combinatorial-indexing sciMET; human samples pooled in one batch and demultiplexed by SNPs (validated with WGS, 99.2% of nuclei correctly assigned). **Multimodal integration**: matched 10x Multiome, Xenium 5K, and scMethyl-Hi-C (3D conformation + methylome in the same cell) on one healthy donor. **Methylation segmentation**: UMRs (<10% methylated, CpG-rich, promoter-like) and LMRs (10–50%, CpG-poor, enhancer-like). **Cross-species**: each cell aggregated with its 50 nearest neighbours into metacells, integrated with Harmony over 40,284 one-to-one orthologous 5-kb bins. **Aging clocks**: a global-methylation clock in mouse; in human a low-coverage-robust PC-based Horvath multi-tissue clock (accurate down to ~3× coverage), with age acceleration = predicted − chronological age residual. **Validation**: deconvolution of KPMP laser-microdissected tubulointerstitial/glomerular bulk WGBS using the single-cell atlas; S-LDSC heritability enrichment; age-associated genes from snRNA of 72 non-diseased kidneys aged 20–90; single-molecule co-methylation/methylation entropy; Xenium niches and TF activities; Hi-C A/B compartments; UK Biobank Olink plasma proteins vs eGFR.

## Data
sciMET: 57,619 high-quality nuclei — human 12 donors (7 kidney-disease patients + 5 age-matched references, 33,835 nuclei), mouse 6 animals (3 at 4 months + 3 at 20 months, all male, 23,784 nuclei); median 0.91M CpGs per cell (~3.1% coverage). Multiome: 142,459 human nuclei (9 samples), 36,563 mouse nuclei (6 samples). Xenium 5K: 383,771 cells from 4 samples (healthy, AKI, CKD). scMethyl-Hi-C: 3,072 cells, >300M long-range contacts from 1 healthy donor. External: KPMP WGBS (15 each), mouse IRI snATAC (GSE209610), the HKA atlas. Methylation data in BioStudies (S-BSST2657 human / S-BSST2647 mouse); Multiome on HuBMAP.

## Key results
- **Atlas quality**: methylation- vs Multiome-inferred composition Spearman ρ = 0.72 (sciMET detects more myeloid cells, likely because snRNA under-detects low-nuclear-RNA cells); 92.6% of UMRs overlap ATAC peaks vs 54.8% of LMRs. 208,049 human cell-type DMRs, **only 16.4% overlapping Illumina 850K array CpGs** — array studies miss most regulatory elements.
- **Cross-species**: 34% of human DMRs keep the same state in mouse, but **epithelial cells diverge significantly more than non-epithelial cells**, linked to lower sequence conservation; conserved DMRs are enriched at TSSs and Polycomb-repressed chromatin, species-specific DMRs at distal enhancers; in PT, AP-1 and MYC motifs are enriched only in divergent DMRs.
- **Mouse aging**: cell-type-specific UMRs/LMRs shift with age more than shared elements; the closer two cell types, the more vulnerable their distinguishing regulatory regions (LMRs only); age DMRs are enriched in IRI injury-associated accessible regions (fold enrichment = 2.95, P < 0.01).
- **Human disease**: sample-level pseudobulk shows age acceleration in disease (P = 0.01); at cell-type level, **epithelial cells are accelerated by 4.8 years on average (P = 2.3 × 10⁻⁴), non-epithelial cells not significantly**, with similar epithelial proportions — acceleration is cell-intrinsic, not compositional. KPMP bulk WGBS deconvolution confirms significant acceleration in tubule-rich tubulointerstitium. PT-specific DMRs are enriched for eGFR heritability, as are healthy→altered DMRs (FDR = 0.004).
- **Altered PT**: within-donor comparison of altered (adaptive/maladaptive/degenerative pooled) vs healthy PT yields 8,996 DMRs, 63.1% hypermethylated; altered PT shows reduced local methylation coordination and higher entropy, most at PT-specific regulatory regions; HNF, RXR and PPAR motifs lose accessibility and gain methylation; DMR methylation vs neighbouring-gene expression ρ = −0.49; altered-vs-healthy expression changes correlate positively with age-association scores from 72 normal kidneys (e.g. CXCL1, IGFBP6, KCNB2); genes both differentially methylated and expressed are enriched for **CpG-island-less** genes.
- **Spatial and 3D**: in Xenium 5K, altered-PT methylation-linked gene signatures are enriched in an early-repair niche (AKI-enriched; ATF4, JUN, BACH2, E2F) and a failed-repair niche (CKD-enriched; BHLHE40, MYC, MITF, WNT); PCK1 is hypermethylated and down, PLAU, MYO1C, CYTH2 hypomethylated and up. Hi-C shows higher short- to long-range contact ratios in epithelia; up-regulated altered-state genes are enriched in PT-specific B compartments, down-regulated in A; 107 "loss-of-repression" and 64 "gain-of-repression" regions, the former containing CXCL1/2/3/6, ITGA2, ANTXR1, HMGA2, ETS1, BACH2; plasma DSC2, DSG2 and TIMP2 associate negatively with eGFR in UK Biobank (54,219 participants).

## Contributions
- A first cross-species, single-cell-resolution kidney DNA-methylation atlas integrated with RNA/ATAC, spatial and 3D-genome data.
- Localizes bulk-level "disease-accelerated aging" to **tubular epithelium**, validated by deconvolving independent bulk WGBS.
- Proposes a mechanistic frame: lineage-specific regulatory elements are most vulnerable to aging and disease, with de-repression of CpG-island-less genes.
- Links single-cell epigenetic changes to clinical kidney function via heritability (S-LDSC) and population plasma proteomics.

## Limitations
- Stated by the authors: mouse aging/injury models do not fully capture human chronic disease; longitudinal studies are needed for causality; all mice are male; the human disease cohort is small and aetiologically heterogeneous, preventing stratified analysis; scMethyl-Hi-C comes from one healthy donor at sparse resolution.
- The "aging-like" interpretation is explicitly hedged: injury, inflammation, stress and de-differentiation produce overlapping signatures, **precluding definitive attribution to accelerated biological aging or senescence**.
- Altered PT pools adaptive/maladaptive/degenerative states; Xenium covers only 4 samples; some tests are not multiplicity-adjusted (described as two prespecified comparisons).

## Relation to our direction
The biggest lesson for **the artifact-injection topic** is that **age is a confounding axis**: altered PT in disease looks epigenetically and transcriptionally "older", and normal aged kidneys already carry part of the same signature (e.g. CXCL1). An anomaly detector trained on young or age-mismatched healthy references (as with some public atlases) may flag normal aging as anomalous; conversely, an old-skewed reference may absorb early disease signal. KidneyAnomalyBench should therefore **age-match references or model age as a covariate**, and report the correlation between anomaly score and donor age. Second, the paper is a template for **multiple orthogonal layers**: methylation (stable, long-term), ATAC (accessibility), RNA (transient) and space (niche) agree on the same state — exactly the "cross-modal agreement separates artifacts from disease" logic: an "anomaly" visible only in RNA with no trace in methylation/ATAC is more likely technical (e.g. ambient RNA), while elevated methylation entropy can itself serve as a cell-level "identity-erosion" anomaly score. Third, the Xenium 5K early-repair / failed-repair niches correspond to PT states in `inflammatory-pt-natcommun-2025` and `lake-kidney-atlas-nature-2023`, making them candidate expert labels for spatial anomalies. For **revert**: genes in loss-of-repression regions (CXCL family, HMGA2, ETS1, BACH2) and the HNF4A/RXR/PPAR programs are natural reversion-target candidates, though no perturbation was done here. For **the agent-trustworthiness topic**: the authors' explicit hedging of the "aging" conclusion and their disclosure of unadjusted tests are good examples for claim-to-evidence checks of "does the wording match the evidence strength?".

## Reusable assets
- **Code:** processing pipeline and figure code.
<https://github.com/hrrsjeong/sckidney_methylome_processing>
<https://github.com/hrrsjeong/sc-kidney-methylome-figures-v0.1>
- **Data:** single-nucleus methylation (BioStudies S-BSST2657 / S-BSST2647); Multiome (HuBMAP HBM233.KJSR.676; HKAv2 at HBM787.TZJP.273); KPMP WGBS.
<https://atlas.kpmp.org>
- **Methods:** the single-cell methylation atlas as a deconvolution reference for bulk methylomes; the low-coverage-robust PC-Horvath clock for cell-type-level age acceleration.

## Follow-ups
- The adaptive / maladaptive / degenerative state definitions in the Human Kidney Atlas (Lake et al., `lake-kidney-atlas-nature-2023`).
- The source of the 72 normal-kidney aging samples — possibly usable to build age-matched healthy references.

## Cite
```bibtex
@article{Jeong_2026, title={A cross-species single-cell kidney epigenome atlas reveals epithelial-dominant aging-like states in disease}, volume={6}, ISSN={2662-8465}, url={http://dx.doi.org/10.1038/s43587-026-01221-z}, DOI={10.1038/s43587-026-01221-z}, number={10}, journal={Nature Aging}, publisher={Springer Science and Business Media LLC}, author={Jeong, Hyeonsoo and Lake, Blue B. and Diep, Dinh and Li, Xuwen and Yan, Qi and Gisch, Debora L. and Kaushal, Madhurima and Reinert, Stephanie and Eadon, Michael T. and Gaut, Joseph P. and Jain, Sanjay and Zhang, Kun}, year={2026}, month=Sept, pages={2218–2233} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
