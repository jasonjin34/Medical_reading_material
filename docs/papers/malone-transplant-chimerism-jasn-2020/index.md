# Harnessing Expressed Single Nucleotide Variation and Single Cell RNA Sequencing To Define Immune Cell Chimerism in the Rejecting Kidney Transplant

> **Bibkey** `Malone_2020` · **Venue** Journal of the American Society of Nephrology (2020) · **Category** single-cell · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1681/asn.2020030326> · `status: complete`

---

## One-liner
Donor/recipient paired whole-exome sequencing provides an SNV reference (.vcf); Demuxlet on 10x 5′ scRNA-seq of five kidney-transplant biopsies (81,139 cells) assigns each cell to donor or recipient, showing donor macrophages persist in non-rejecting grafts with transcriptional programs distinct from recipient macrophages.

## Problem
Donor-derived immune cells in solid-organ transplants are assumed to decline after surgery, but whether they persist in kidney allografts or contribute to rejection was unknown, partly because there was no good way to tell donor from recipient cells (previously Y-chromosome tracking in sex-mismatched pairs). The paper uses expressed SNVs + scRNA-seq to define leukocyte chimerism at single-cell resolution.

## Method
(1) Fresh dissociation (0.25% trypsin + DNase I, ~30 min, ~90% viability); two 10x Chromium lanes per biopsy (target 10,000 cells/lane), **5′ kits** plus T-cell VDJ libraries; 50,000 reads/cell for gene expression. (2) Cell Ranger 3.0 → Seurat v3; QC 200–2500 genes/cell, <25% mitochondrial; over-clustering, then "clusters containing two or more different cell type–defining markers were removed as doublet clusters" and low-gene clusters removed as debris; Seurat v3 integration. (3) WES of peripheral-blood germline DNA (target 50×), BWA-MEM → Picard → GATK BQSR → GATK best-practice filtering of common variants (AF > 0.05); one combined donor+recipient .vcf per pair (mean 120,896 coding SNVs). (4) Demuxlet (default parameters, α = 0, 0.5, 1) on the combined .vcf + Cell Ranger BAM; each cell labelled donor/recipient from the BEST column. (5) DE (Seurat FindMarkers) + ToppFun pathways, Spearman correlations, VDJ Loupe for T-cell clones.

## Data
Five indication kidney-transplant biopsies (Washington University): 3 acute antibody-mediated rejection (ABMR, all DSA-positive) + 2 non-rejection AKI; 5 days to 7 years post-transplant. Plus an "independent data set": serial pre-/1-month post-treatment biopsies from one ABMR patient (Fig 3G; **3′** kits per GEO; not part of the 81,139-cell set). GEO **GSE145927**: 7 scRNA samples (Biopsy1_Day28, Biopsy2_Day2542, Biopsy3_Day11, Biopsy4_Day5, Biopsy5_Day232 = 5′; Biopsy6_Pre-treatment, Biopsy7_Post-treatment = 3′) + 10 WES samples (5 donor/recipient pairs, PBMC, IDT xGen Exome v1, NovaSeq 6000). Processed files: one `*rawcounts.csv.gz` per sample (gene × cell UMI counts, **post-QC cells only**; e.g. the Day11 file has 5,395 cells = biopsy65 in the metadata) + `GSE145927_MGI.metadata.csv.gz` (81,139 cells: biopsy, nCount/nFeature, percent.mt, clusters, `SNV_GT` donor/recipient, `stim` rejn/no_rejn, cell type). Raw FASTQs (scRNA and WES) are in SRA **SRP250734 / PRJNA608747** and the run table lists public download paths (not dbGaP); the GEO WES samples carry no processed files (no VCF).

## Key results
- 81,139 cells passed QC (mean 1,124 genes / 2,497 transcripts); 8 kidney clusters + 2 immune clusters; 5,027 macrophages and 3,647 lymphocytes (T 3,067, B 190, plasma 231; plus 111 mast cells on subclustering).
- Median SNVs per cell 71–231, minimum 17; authors report ~90% accuracy overall and near 100% above the lower quartile.
- "Despite manual filtering and removal of doublet cells … the Demuxlet tool identified 3%–10.5% of cells as doublets."
- Macrophages: 3,798 recipient / 1,229 donor; lymphocytes: 1,528 recipient / 2,119 donor. Non-rejecting samples had roughly equal donor/recipient macrophages; rejecting samples were recipient-dominated (e.g. 97% recipient at day 11 rejection; 35.8% donor at day 28 non-rejection). Donor lymphocyte share fell with time (very few by day 232).
- Recipient macrophages: IL-6, IFN, FCγR pathways, CD16/CD68; donor macrophages: complement (C1QA/B/C), antigen presentation, F13A1, CD14. Recipient T cells correlated with rejecting T cells (Spearman 0.8; NKG7/GNLY/GZMB/PRF1); donor T cells with non-rejecting T cells (1.0), enriched for oxidative phosphorylation (quiescent).
- VDJ: only 120/3,115 T cells had complete VDJ (34 donor, all from the day-11 rejection sample; 86 recipient).

## Contributions
- First use of paired donor/recipient WES + Demuxlet on human kidney-transplant biopsy scRNA-seq to define leukocyte chimerism cell by cell.
- Shows donor macrophages persist in non-rejecting grafts with programs distinct from recipient macrophages (complement/antigen presentation vs. inflammatory activation).
- Releases 5′ scRNA plus paired WES raw data — a human kidney tissue dataset with genetic-identity labels.

## Limitations
- Very small (5 biopsies, 3 vs 2); the authors call it proof-of-concept; rejection status is confounded with time post-transplant.
- The main text does not report Demuxlet origin fractions for epithelial/endothelial/stromal cells and says nothing about ambient RNA or soup contamination; "all parenchymal cells are donor-derived" is a biological expectation, not a reported result (supplement not retrieved; unverified).
- Demuxlet doublet calls are not in the GEO metadata (only donor/recipient labels in the final set); doublets were partly removed manually before, so the public matrices do not preserve the natural doublet distribution.
- **The public metadata `SNV_GT` disagrees with the paper** (our own tabulation): macrophages donor 4,715 / recipient 312 (paper: donor 1,229 / recipient 3,798), and the recipient fraction is nearly flat across cell types within each biopsy (biopsy65: 22.6–29.3%; biopsy62: 3.6–5.6%), unlike genuine cell-type-specific chimerism. Possibly a barcode/label misjoin or a different meaning — re-run demuxlet/vireo from SRA before using it.
- The text says HiSeq while the SRA run table says NovaSeq 6000 — minor, but another record/text mismatch.

## Relation to our direction
Sits in the artifact-injection topic's **detect** stage as a source of *artifact ground truth*. Our benchmark asks whether anomaly detectors separate disease (rejection/AKI) from measurement artifacts (ambient RNA, doublets) with donor-level false-alarm control. Value here: (1) **Doublet ground truth**: each lane mixes two genotypes, so demuxlet can flag heterotypic-genotype (donor+recipient) doublets — 3–10.5% reported — but same-genotype (donor+donor) doublets, likely the majority in donor-epithelium-dominated tissue, are invisible to genotype; it is partial truth that needs extrapolation from the cross-genotype rate (as in the Demuxlet paper). (2) **Ambient ground truth (our own inference; the paper does not say this)**: kidney parenchymal epithelium should be donor-only, so recipient-specific allele reads in epithelial barcodes directly estimate ambient/soup contamination from infiltrating recipient immune cells — the same logic as Janssen 2023's mouse-strain mixing estimate of background noise. The paper neither proposes nor validates this. (3) Rejection vs non-rejection provides a real disease signal as a contrast. Caveats: only 5 donor pairs, so donor-level false-alarm control has little power; (1) and (2) require SRA BAM/FASTQ (≈30–65 GB per scRNA run) plus our own WES variant calling — the GEO processed files are not enough.

## Reusable assets
- **Code:** none released; standard tools (Cell Ranger 3.0, Seurat v3, GATK, Demuxlet).
- **Data:** GEO GSE145927 (post-QC count matrices + 81,139-cell metadata incl. `SNV_GT`, but see Limitations); SRA SRP250734 (17 scRNA runs + 10 WES runs, public FASTQ). No VCF, no raw-droplet matrices, no doublet labels.
- **Checkpoints:** none.

## Follow-ups
- Supplement (Supplemental Methods on doublet removal, Supp Table 1 clinical data, Supp Fig 1 per-sample droplet histograms) — not retrieved; download manually.
- Kang et al. 2018 (Demuxlet, Nat Biotechnol) — extrapolating total doublets from cross-genotype doublets.
- Compare with janssen-ambient-noise-genomebiol-2023: its genotype-based ambient estimate transfers directly.
- Resolve the `SNV_GT` vs paper mismatch (contact authors or re-run from SRA).

## Cite
```bibtex
@article{Malone_2020, title={Harnessing Expressed Single Nucleotide Variation and Single Cell RNA Sequencing To Define Immune Cell Chimerism in the Rejecting Kidney Transplant}, volume={31}, ISSN={1533-3450}, url={http://dx.doi.org/10.1681/ASN.2020030326}, DOI={10.1681/asn.2020030326}, number={9}, journal={Journal of the American Society of Nephrology}, publisher={Ovid Technologies (Wolters Kluwer Health)}, author={Malone, Andrew F. and Wu, Haojia and Fronick, Catrina and Fulton, Robert and Gaut, Joseph P. and Humphreys, Benjamin D.}, year={2020}, month=July, pages={1977–1986} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
