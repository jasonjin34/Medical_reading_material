# Label-free single-cell RNA multiplexing leveraging genetic variability

> **Bibkey** `Hoeft_2024` · **Venue** Nature Communications (2024) · **Category** single-cell · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1038/s41467-024-54270-6> · `status: complete`

---

## One-liner
Hayat/Kramann lab present **SoupLadle**: reference-free SNP deconvolution of pooled sc/snRNA-seq with Souporcell, then re-assignment of each genotype cluster to a patient by Hamming distance + Kuhn-Munkres matching against per-patient bulkRNA-seq SNPs; it gives the highest recall and least cell-type bias on PBMC, two heart snRNA cohorts and **4 frozen human kidney biopsies (snRNA, 11,490 nuclei)**.

## Problem
Large human single-cell cohorts are limited by cost and batch effects. Multiplexing reduces both, but cell labeling (CellPlex/Hashtag) needs extra staining and washes that destroy nuclei ("~20–30% of nuclei are lost with each washing step"), while SNP methods without a reference genotype only "discriminate (…deconvolute), but do not re-assign cells to patients". Vireo can use bulkRNA/WES genotypes as a prior, but then only uses SNPs also covered by the reference, losing recall, especially for rare cell types. The question: how to multiplex frozen-tissue snRNA simply, with high recall, and still map every cell back to a named patient?

## Method

SoupLadle has four steps (Fig. 1h): (1) bulkRNA-seq per patient (STAR, freebayes `-iXu --min-mapping-quality 30 --min-base-quality 10 --min-coverage 5`), used **a priori** to check SNP heterogeneity and choose which samples to pool; (2) pooled 10x 3′ v3.1 sc/snRNA-seq; (3) freebayes candidate SNPs on the pooled BAM → Vartrix allele counts → Souporcell 2.4 clustering (`--num_clusters` = number of donors) + troublet doublet calls; (4) a normalized Hamming-distance matrix between Souporcell genotype clusters and bulk SNP profiles, solved one-to-one with Kuhn-Munkres (Hungarian). The key argument is that deconvolution can use **all** SNPs called in the single-cell data, not just those also in the reference, so rare cell types still get assigned. Comparators: CellPlex, Hashtag (TotalSeq-A anti-nuclear-pore), Souporcell (Vartrix or minimap2), Vireo 0.5.7 (cellSNP-lite or Vartrix SNPs; with/without bulkRNA or WES prior). Doublet reference: scDblFinder (top 4000 genes, score > 3). CellRanger 7.1.0 + GRCh38-2020-A, no QC cutoff before demultiplexing; Seurat clusters (4000 HVG, res 0.1) serve as PBMC ground truth.

## Data
| 数据集 | 设计 | 平台 | 细胞/核数 | 真值 |
|---|---|---|---|---|
| PBMC (P1–5) | 每人 FACS 分选一种 PBMC 亚群 (CD14 Mono | 10x 3′ v3.1, Chip G | 17,892 | 细胞类型 = 患者 (FACS 设计) + CellPlex |
| Heart 1 (P6–10) | 冷冻心肌 snRNA,CellPlex + Hashtag 双标记;bulkRNA + WES | 10x 3′ v3.1, Chip G | 1,563 | CellPlex / HTO |
| Heart 2 (P11–18) | 冷冻心肌 snRNA,每人 ~50,000 nuclei 分选后 pool,无标记;bulkRNA | 10x 3′ HT v3.1, Chip M | 11,501 | 仅方法间一致性 |
| **Kidney (P19–22)** | **4 例冷冻人肾活检**(3 男 1 女),"total processed biopsies were pooled prior to sorting",DAPI⁺ nuclei 分选,无标记;bulkRNA(**无 rRNA depletion**),无 WES | **10x 3′ v3.1 (Dual Index), Chip G, snRNA** | **11,490** | 仅方法间一致性 |

| Dataset | Design | Platform | Cells/nuclei | Ground truth |
|---|---|---|---|---|
| PBMC (P1–5) | one FACS-sorted PBMC subset per patient (CD14 Mono / CD16 Mono / CD4 T / CD8 T / CD19 B), 100,000 each, pooled; CellPlex; bulkRNA + WES | 10x 3′ v3.1, Chip G | 17,892 | cell type = patient (by design) + CellPlex |
| Heart 1 (P6–10) | frozen myocardium snRNA, CellPlex + Hashtag; bulkRNA + WES | 10x 3′ v3.1, Chip G | 1,563 | CellPlex / HTO |
| Heart 2 (P11–18) | frozen myocardium snRNA, ~50,000 nuclei/patient sorted and pooled, unlabeled; bulkRNA | 10x 3′ HT v3.1, Chip M | 11,501 | cross-method agreement only |
| **Kidney (P19–22)** | **4 frozen human kidney biopsies** (3 M / 1 F), "total processed biopsies were pooled prior to sorting", DAPI⁺ nuclei sorted, unlabeled; bulkRNA (**no rRNA depletion**), no WES | **10x 3′ v3.1 (Dual Index), Chip G, snRNA** | **11,490** | cross-method agreement only |

A published 5′ heart scRNA dataset (Koenig 2022) is used only for SNP-distribution analysis. **Kidney disease / clinical diagnosis is not reported** in the paper, supplement, GEO or BioSample (ethics: Erasmus MC MEC-2021-0840).

## Key results

- **PBMC**: Souporcell has the best precision/recall; adding bulkRNA/WES priors to Vireo gives "marginal improvement in precision, but a distinct loss in cell recall"; excluding doublets, all methods reach ≈ 98.5% precision. CellPlex's lower precision comes from over-calling doublets (CellPlex 3,947 doublets + 3,524 unassigned vs Souporcell 2,373 + 34, of 17,892 cells). bulkRNA recovers more scRNA SNPs than WES (especially 3′UTR). With bulk SNPs randomly downsampled (1.0→0.2, n = 10), SoupLadle beats Vireo significantly (Wilcoxon, p < 0.0001).
- **Heart 1**: SoupLadle assigns nearly all cells; CellPlex/Hashtag/Vireo CellSNP bulkRNA ~75%; Vireo CellSNP WES only ~12.5%. Cross-method overlap > 95% (except WES).
- **Heart 2 (n = 8)**: SoupLadle 99% assigned, Vireo Vartrix bulkRNA 81%, Vireo CellSNP bulkRNA 45%.
- **Kidney (n = 4, 11,490 nuclei)**: SoupLadle assigns 96% (10,781 singlets; **250 doublets = 2.2%**; 459 unassigned = 4.0%); Vireo Vartrix bulkRNA 21%; Vireo CellSNP bulkRNA < 1%. SoupLadle/Vireo Vartrix overlap ~93%. Vireo under-assigns rare types (podocytes, fibroblasts, intercalated cells); SoupLadle shows "no apparent cell-type bias".
- **(Our own tally from Source Data Fig2j.)** The kidney "Mixed/Doublets" expression cluster holds 4,488 nuclei (39%), yet SoupLadle calls only 123 of them cross-donor doublets and 308 unassigned; the other 4,057 go to a single donor. There is also a 434-nucleus "Low Quality" cluster. So most of the expression-defined "doublet/mixed" cluster is genotypically single-donor.
- Cost: ~4-fold cheaper when multiplexing 8 samples (Supplementary Data 1).
- Ambient RNA: **not quantified**. Quote: "while we do not provide a tool for ambient RNA correction, ambient RNA can be imputed with standard packages (CellBender, SoupX) or Souporcell".

## Contributions
- A head-to-head benchmark of CellPlex, Hashtag, Souporcell and Vireo (± bulkRNA/WES) on PBMC, heart and kidney, with a FACS design in PBMC that makes "cell type = patient" a ground truth.
- SoupLadle: deconvolve first, then match, which is more robust when SNPs are scarce and for rare cell types; ships as an R package with a pre-pooling SNP-heterogeneity check.
- Evidence that snRNA SNPs fall mostly in introns and 3′UTRs, so bulkRNA-seq is a better genotype reference than WES.

## Limitations
- Heart 2 and kidney have no independent label ground truth (no CellPlex/HTO), only cross-method agreement; the authors call it a "proof of concept".
- Kidney has only 4 donors, with no reported disease, age or biopsy indication; its bulkRNA was not rRNA-depleted.
- SNP methods only see **cross-donor** (heterotypic) doublets; same-donor doublets are invisible. The paper does not discuss this.
- Ambient RNA and contamination are not quantified.
- Deposition issues: the Heart_2 pooled SRA run (SRR29832268) shows 0 spots, and Heart_2 Patient 18's bulk run (SRR29830135) has exactly the same spots/bases as Heart Patient 10 (SRR26826519), which looks like a duplicate upload (**unverified**).

## Relation to our direction

This is a data / ground-truth source for the **detect** stage, not a method. Plan A builds a human-kidney single-cell benchmark that tests whether anomaly detectors separate disease from measurement artifacts (ambient RNA, doublets, protocol), with donor-level conformal false-alarm control. This dataset is a rare **real human-kidney, multi-donor pooled snRNA with per-donor bulk genotypes**:
1. **Cross-donor doublet ground truth**: genotype doublets are labels independent of expression. With 4 donors in unequal proportions only part of all doublets are cross-donor, so this is a lower bound, not the full doublet set. It is still enough to test whether expression-based doublet detectors or anomaly scores mistake rare cells or disease states for doublets. Source Data shows the expression "Mixed/Doublets" cluster is mostly single-donor, a ready pool of counter-examples.
2. **Ambient RNA ground truth**: in a multi-donor pool, the fraction of "wrong-donor alleles" in each nucleus is a genotype-based estimate of ambient/contamination (Souporcell itself estimates an ambient fraction; same idea as Janssen 2023's genotype-based ground truth). The paper does not do this, so we must recompute it from FASTQ.
3. **Donor-level conformal**: 4 donors allow a small leave-one-donor-out calibration check, but n = 4 is a sanity check, not a headline result.
4. Limitation: disease status is unknown, so the dataset cannot serve as the "disease" side of disease-vs-artifact; it only gives artifact-side ground truth.

## Reusable assets
- **Code:** SoupLadle R package https://github.com/ToreBle/SoupLadle (Zenodo 10.5281/zenodo.13711299); includes souporcell/vireo shell scripts and PBMC/heart analysis scripts, but **no kidney script and no per-cell assignment table**.
- **Data:** GEO GSE247708 (SuperSeries: GSE247706 bulk VCFs, GSE247707 pooled 10x). Kidney pooled snRNA = GSM8397034, with only `barcodes/features/matrix` (11,490 barcodes × 36,601 genes, cellranger-7.1.0). GEO labels it "raw_feature_bc_matrix", but the barcode count equals the cell-called count, so it is in fact a **filtered matrix**: no empty droplets and no assignment table. Kidney bulk VCFs = GSM8397029–32 (TS116/120/121/126). FASTQs are public under BioProject PRJNA1040187: kidney snRNA run SRR29832267 (809M spots; ENA R1 16.5 GB + R2 32.8 GB) and kidney bulk SRR29830128–31 (~1.5–1.7 GB each). WES (PBMC/heart only) is at EGA EGAD50000000928, controlled access. Source Data gives kidney cell-type × donor counts (Fig2j). PBMC (GSM7899153, 2,739,993 barcodes) and Heart 1 (GSM7899155, 1,080,502) are true raw matrices, with CMO/HTO assignment tables.
- **Checkpoints:** none (not a learned model).

## Follow-ups
- Re-run CellRanger on SRR29832267 (true raw matrix + BAM) → Souporcell (k = 4, with ambient estimate) → SoupLadle matching to the GEO kidney VCFs; reproduce 250 doublets / 459 unassigned, then compute per-nucleus cross-donor allele fractions.
- Ask the authors (Hayat/Bleckwehl) for kidney clinical/disease metadata and the per-cell assignment table.
- Compare with Janssen 2023 (genotype-based ambient ground truth) and Heaton 2020 Souporcell ambient estimation.

## Cite
```bibtex
@article{Hoeft_2024, title={Label-free single-cell RNA multiplexing leveraging genetic variability}, volume={15}, ISSN={2041-1723}, url={http://dx.doi.org/10.1038/s41467-024-54270-6}, DOI={10.1038/s41467-024-54270-6}, number={1}, journal={Nature Communications}, publisher={Springer Science and Business Media LLC}, author={Hoeft, Konrad and Bleckwehl, Tore and Schumacher, David and Kim, Hyojin and Meyer, Robert and Long, Qingqing and Zhang, Ling and Möller, Christian and Clahsen-van Groningen, Marian C. and Babler, Anne and Saritas, Turgay and Kurth, Ingo and Milting, Hendrik and Hayat, Sikander and Kramann, Rafael}, year={2024}, month=Dec }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
