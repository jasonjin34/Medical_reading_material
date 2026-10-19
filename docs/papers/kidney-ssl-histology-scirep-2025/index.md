# Unbiased self supervised learning of kidney histology reveals phenotypic and prognostic insights

> **Bibkey** `Pandit_2025` · **Venue** Scientific Reports (2025) · **Category** histopath · **Relevance** medium · **Access** open
> **Link** <https://doi.org/10.1038/s41598-025-19193-2> · `status: complete`

---

## One-liner
NYU (Tsirigos lab) with JHU/UPenn applies Histomorphological Phenotype Learning (HPL), a self-supervised framework first built for lung-cancer H&E, to 1,421 PAS-stained kidney WSIs: with no pathologist labels, tile embeddings are clustered into histomorphological phenotype clusters (HPCs) and each slide becomes a vector of HPC area fractions. The clusters are visually consistent across five internal/external sets, track pathologist quantifications such as interstitial fibrosis (MIL AUC 0.83), and predict kidney-function decline in the TRIDENT diabetic-nephropathy cohort.

## Problem
Computational pathology mostly relies on supervised learning with costly, subjective annotations (e.g. 39 pathologists outlining 4,704 lung WSIs), and kidney pathologists are especially scarce — many institutions lack even one on site. The question: can reproducible kidney tissue patterns be obtained **disease-subtype-agnostically** and label-free, and can these patterns recapitulate pathologist slide-level assessment and associate with clinical outcomes and genotype?

## Method
**Preprocessing**: DeepPATH tiling into non-overlapping 224×224 tiles, dropping tiles with >50% background, Reinhard stain normalization; separate models at 5×, 10× and 20×. **Self-supervision**: Barlow Twins (ResNet layers plus one self-attention layer) on two augmented views of each tile, pushing the cross-correlation matrix toward identity, yielding 128-d embeddings; stopped at epoch 30 by validation loss. **Two Leiden rounds**: a high-resolution first round to visually identify and remove artifact clusters (blur, edges, non-tissue) — labels also used to strip artifact tiles from external sets; a second round on remaining tissue tiles with cluster count chosen at the elbow of a disruption score (tile-to-centroid distance) on validation, giving 77/100/99 HPCs at 5×/10×/20×. **Slide representation**: each element = percentage of tissue area in an HPC. **Downstream**: Spearman correlation with pathologist quantification (Bonferroni); CLAM (MIL) on HPC composition to predict interstitial fibrosis >5%; Kaplan–Meier and Cox models (four LASSO-selected HPCs) for ESKD or ≥40% eGFR decline; patient-level hierarchical clustering into five groups compared on clinical variables and three SNPs (UMOD rs12917707, SLC34A1 rs6420094, SLC7A9 rs12460876). Embeddings are also compared with ImageNet ResNet-50 and UNI.

## Data
1,421 PAS WSIs from 21 cohorts. **Development**: non-neoplastic tissue from 739 UPenn nephrectomy wedge biopsies, split evenly (stratified by diabetes and eGFR) into train 247 / val 246 / test 246 (mean age 61, eGFR 67, 35.2% diabetic). **External sets received a year later**: an independent test set of 262 slides (UPenn tissue, scanned at NYU on a different scanner); DDKT pre-implantation donor core biopsies, 181 slides (106 donors, 75 with left/right pairs); TRIDENT diabetic-nephropathy clinical biopsies, 239 slides from 19 institutions with longitudinal follow-up. Tile counts: 425,807 (5×), 1,670,210 (10×), 6,748,666 (20×).

## Key results
- **Cross-cohort consistency**: in a tile-set matching exercise (21 participants), experts scored 94.2% (SD 11.7%) and non-experts 90.0% (SD 13.1%); in DDKT, left/right kidneys of the same donor are much closer in slide-vector space than across donors (p = 4.5e-23).
- **Recapitulating pathology**: fibrosis-associated HPCs stay correlated across validation, test, independent test and TRIDENT, and highlighted regions match pathologist fibrosis annotations; CLAM predicting fibrosis >5% reaches AUC 0.79 (test) and 0.83 (independent test). HPL clusters associate with fibrosis significantly more strongly than ResNet-50 or UNI clusters, and UNI clusters on paired PAS/H&E slides of the same TRIDENT core show **stain-specific and patient-specific batch effects**.
- **Prognosis**: in TRIDENT, the top tertile of HPC 49 (blindly annotated as global sclerosis amid IFTA) shows more kidney-function decline, and HPC 53 (histologically unremarkable proximal tubules) less. Cox models: clinical baseline (age, sex, ACR, eGFR; N = 182) c-statistic 0.82 → 0.84 with four HPCs; histology baseline (fibrosis, RPS score, epithelial hyperplasia; N = 177) 0.76 → 0.80.
- **Patient groups**: of five groups, group 4 (marker HPC 8, medullary morphology) has markedly lower eGFR (p = 2.0e-10) and higher dipstick protein (p = 0.008); group 0 has more type 1 diabetes (p = 0.006); group 1 differs in SLC34A1 rs6420094 allele frequency.

## Contributions
- Transfers HPL from lung-cancer H&E to highly heterogeneous PAS kidney tissue, externally validated across 21 cohorts, scanners and biopsy types (wedge → core).
- A single interpretable representation (slide = HPC-composition vector) feeding pathology quantification, prognosis (Cox) and genotype association.
- An explicit artifact-cluster identification/removal step and a human matching test of cross-cohort consistency — two practical checks of unsupervised-phenotype trustworthiness.

## Limitations
- Training data are nephrectomy wedge biopsies (mostly common diabetic/hypertensive change), excluding core biopsies, rare etiologies and transplant recipients — not the full nephrology spectrum.
- PAS only; trade-offs in magnification and cluster count (interpretability vs coverage) are under-explored; HPC meaning relies on post hoc pathologist inspection.
- Prognostic gains are modest (c-statistic +0.02 / +0.04) and selection and evaluation share the TRIDENT cohort with no independent external validation; the SNP analysis is small (N = 183) with three loci.
- Data are not public (available on request from the corresponding author).

## Relation to our direction
Not an anomaly-detection paper, but it is Plan A's **histology-side precedent for a "normal/phenotype atlas"**: label-free, reproducible morphological clusters learned at scale on kidney tissue and shown to map onto real pathology (fibrosis, sclerosis). Three uses along detect → model → revert: **(1) building the reference distribution** — the HPC-composition vector is itself a low-dimensional tissue-state representation; fitting its distribution on healthy/reference kidney makes deviation a slide- or region-level anomaly score — a simple, interpretable baseline; **(2) artifact vs disease** — the authors remove blur/edge tiles by manually spotting artifact clusters, exactly the step Plan A wants to automate: our hypothesis is that **cross-modal agreement** between H&E and Xenium/snRNA separates artifacts from lesions, and this manual artifact-cluster step is the comparator; **(3) foundation-model batch effects** — UNI clusters show stain- and patient-specific batch effects on PAS vs H&E of the same tissue, warning that anomaly scores from generic pathology-FM embeddings may report stain/batch differences as anomalies, so KidneyAnomalyBench needs a dedicated "same tissue, different stain/batch" control set. TRIDENT is a diabetic-nephropathy cohort, in the same CKD space as the DKD spatial atlas (`dkd-spatial-atlas-nature-2026`) and our in-house biopsies; its IFTA/sclerosis-linked clusters can serve as weak labels for "known anomalies". The link to Plan B is weak; the one point is that HPC → outcome associations are the typical "significant but small-effect" claims an agent produces on kidney data — good test cases for claim verification.

## Reusable assets
- **Code:** the HPL pipeline (Barlow Twins + Leiden + slide composition vectors).
<https://github.com/AdalbertoCq/Histomorphological-Phenotype-Learning>
- **HPC tile browser:** representative tiles for all magnifications and sets.
<https://genome.med.nyu.edu/public/pmedlab/SSL_kidney/representative_tiles>
- **Evaluation designs:** tile-set matching (cross-cohort consistency), left/right-kidney pair distance test, and HPC → Cox incremental c-statistic — reusable for evaluating unsupervised kidney representations.
- **Data:** not public; on request from the corresponding author.

## Follow-ups
- The original HPL paper (Quiros et al., lung-cancer H&E).
- Repeat the fibrosis-association comparison with UNI2-h (`uni2-h-model`) as backbone after stain-batch correction.
- Whether KPMP has public PAS WSIs to reproduce this HPC atlas as an external reference for Plan A.

## Cite
```bibtex
@article{Pandit_2025, title={Unbiased self supervised learning of kidney histology reveals phenotypic and prognostic insights}, volume={15}, ISSN={2045-2322}, url={http://dx.doi.org/10.1038/s41598-025-19193-2}, DOI={10.1038/s41598-025-19193-2}, number={1}, journal={Scientific Reports}, publisher={Springer Science and Business Media LLC}, author={Pandit, Krutika and Coudray, Nicolas and Quiros, Adalberto Claudio and Surapaneni, Aditya and Upadhyay, Dhairya and Vanguri, Rami Sesha and Hirohama, Daigoro and Mohandes, Samer and Schlosser, Pascal and Thiessen-Philbrook, Heather and Wen, Yumeng and Parikh, Chirag R. and Rhee, Eugene P. and Waikar, Sushrut S. and Schmidt, Insa and Rosenberg, Avi Z. and Palmer, Matthew B. and Susztak, Katalin and Grams, Morgan E. and Tsirigos, Aristotelis and {TRIDENT Study Investigators}}, year={2025}, month=Oct }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
