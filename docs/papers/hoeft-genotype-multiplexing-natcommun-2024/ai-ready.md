<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# Label-free single-cell RNA multiplexing leveraging genetic variability

- **Authors:** Hoeft, Konrad; Bleckwehl, Tore; Schumacher, David; Kim, Hyojin; Meyer, Robert; Long, Qingqing; Zhang, Ling; Möller, Christian; Clahsen-van Groningen, Marian C.; Babler, Anne; Saritas, Turgay; Kurth, Ingo; Milting, Hendrik; Hayat, Sikander; Kramann, Rafael
- **Venue / Year:** Nature Communications 15:10612 · 2024 (received 29 Nov 2023, accepted 6 Nov 2024)
- **DOI:** 10.1038/s41467-024-54270-6 · PMCID PMC11621319 · PMID 39638798
- **URL:** https://doi.org/10.1038/s41467-024-54270-6
- **License:** CC BY 4.0
- **Bibkey:** Hoeft_2024
- **Status:** complete (extracted from the open full text + supplementary files; figure panels summarized, not transcribed)

## Abstract
Single cell RNA sequencing has provided unprecedented insights into the molecular cues and cellular heterogeneity underlying human disease. However, the high costs and complexity of single cell methods remain a major obstacle for generating large-scale human cohorts. Here, we compare current state-of-the-art single cell multiplexing technologies, and provide a widely applicable demultiplexing method, SoupLadle, that enables simple, yet robust high-throughput multiplexing leveraging genetic variability of patients.

## Structured extract

### Motivation
- Multiplexing reduces cost and batch effects. Cell labeling (CellPlex, Hashtag) adds staining/wash steps; ~20–30% of nuclei are lost per wash.
- SNP-based tools (Vireo, Souporcell, Demuxlet) without reference genotypes only deconvolute, i.e. they group cells by genotype but cannot name the patient. Vireo can use bulkRNA/WES SNPs as a prior.

### SoupLadle framework
1. bulkRNA-seq per patient; SNP calling (STAR → freebayes `-iXu --min-mapping-quality 30 --min-base-quality 10 --min-coverage 5` → bcftools/R); pre-select patients with distinct SNP profiles for pooling.
2. Pooled 10x 3′ sc/snRNA-seq.
3. Souporcell deconvolution: freebayes on the pooled BAM (`-iXu -C 2 -q 20 -n 3 -E 1 -m 30 --min-coverage 6 --max-coverage 100000 --pooled-continuous`), Vartrix allele counting (`--umi --mapq 30 --scoring-method coverage`), Souporcell v2.4 (`--num_clusters` 4–8), troublet doublets.
4. Re-assignment: normalized Hamming distance between Souporcell genotype profiles and bulk SNP profiles; Kuhn-Munkres algorithm for one-to-one assignment.
- Rationale: deconvolution uses all SNPs in the single-cell data, not only those also in the reference, which helps rare cell types.
- Comparators: CellPlex; Hashtag (TotalSeq-A anti-nuclear-pore); Souporcell (Vartrix or minimap2); Vireo 0.5.7 with cellSNP-lite (`--minMAF 0.1 --minCOUNT 100`) or Vartrix SNPs, ± bulkRNA/WES prior (`-d --forceLearnGT`). Doublet reference: scDblFinder (top 4000 genes, score > 3).
- Processing: CellRanger 7.1.0, GRCh38-2020-A; no QC cutoffs before demultiplexing; Seurat (4000 HVG, PCA/UMAP, FindClusters res 0.1).
- PBMC precision/recall against reference clustering: Precision = TP/(TP+FP), Recall = TP/(TP+FN). Bulk SNPs randomly subsampled at fractions 1.0 to 0.2, 10 times each; Wilcoxon signed-rank test.

### Datasets
- **PBMC**: 5 patients (2 M / 3 F). Each patient contributes one FACS-sorted population (CD14 Mono, CD16 Mono, CD4 T, CD8 T, CD19 B; 100,000 each), CellPlex-labelled, pooled; 10x 3′ v3.1 Chip G; 17,892 cells after CellRanger. bulkRNA (rRNA-depleted) + WES per patient.
- **Heart 1**: 5 patients (2 M / 3 F), snap-frozen myocardium (transplant / total artificial heart / LVAD patients); nuclei labelled with CellPlex + Hashtag, sorted, pooled; 10x 3′ v3.1 Chip G; 1,563 nuclei. bulkRNA + WES.
- **Heart 2**: 8 patients (5 M / 3 F), ~50,000 nuclei sorted per patient, unlabelled; 10x 3′ HT v3.1 Chip M; 11,501 nuclei. bulkRNA.
- **Kidney**: 4 frozen human kidney biopsies (3 M / 1 F); "total processed biopsies were pooled prior to sorting to reduce sample loss"; DAPI⁺ nuclei sorted (Sony SH800S); unlabelled; 10x 3′ v3.1 Dual Index, Chip G; 11,490 nuclei. bulkRNA with NEBNext Ultra II Directional **without rRNA depletion**; no WES. Disease/diagnosis not reported. Ethics: Erasmus MC MEC-2021-0840.
- Sequencing: NovaSeq, 25,000 reads/cell for sc/snRNA; 2,500 reads/cell for CellPlex/HTO; 25M reads per bulk library.
- Also a published 5′ heart scRNA dataset (Koenig et al. 2022), used only for SNP-location analysis.

### Key results
- PBMC: Souporcell has the best precision/recall. Vireo + bulkRNA/WES prior: "marginal improvement in precision, but a distinct loss in cell recall"; bulkRNA > WES. Precision of assigned singlets ≈ 98.5% for all methods; CellPlex over-calls doublets. Counts (Supp. Data 2), doublets / unassigned of 17,892: CellPlex 3,947 / 3,524; Souporcell 2,373 / 34; Vireo CellSNP bulkRNA 1,250 / 2,201; Vireo CellSNP WES 901 / 3,802. bulkRNA recovers more scRNA SNPs than WES, especially in the 3′UTR. SoupLadle beats Vireo under bulk-SNP downsampling (p < 0.0001).
- Heart 1: SoupLadle assigns nearly all nuclei; CellPlex, Hashtag and Vireo CellSNP bulkRNA ~75%; Vireo CellSNP WES ~12.5%. Overlap between methods > 95% (except WES). Hashtag and Vireo CellSNP bulkRNA show a cardiomyocyte bias.
- Heart 2: SoupLadle 99% assigned; Vireo Vartrix bulkRNA 81%; Vireo CellSNP bulkRNA 45%. SoupLadle/Vireo Vartrix overlap 100%; SoupLadle/Vireo CellSNP 96%. SoupLadle handles rare types (e.g. neuronal) better.
- Kidney: SoupLadle 96% assigned; Vireo Vartrix bulkRNA 21%; Vireo CellSNP bulkRNA < 1%. SoupLadle/Vireo Vartrix overlap ~93%. Vireo Vartrix under-assigns podocytes, fibroblasts and intercalated cells relative to PT/TAL/DCT; SoupLadle shows no apparent cell-type bias.
  - Supp. Data 2 (kidney): SoupLadle P19 3,329 · P20 3,787 · P21 1,447 · P22 2,218 · unassigned 459 · doublets 250. Vireo Vartrix bulkRNA: 928 / 120 / 687 / 540 · unassigned 9,090 · doublets 125. Vireo CellSNP bulkRNA: 11 / 20 / 37 / 16 · unassigned 11,405 · doublets 1.
  - Source Data Fig2j (SoupLadle), totals per expression cluster: Mixed/Doublets 4,488 (123 genotype doublets, 308 unassigned); Fibroblasts 2,086; Proximal Tubule 1,526; Endothelial 1,019; TAL & DCT 837; Principal 619; Low Quality 434; Podocytes 301; Intercalated 180.
- Cost: ~4-fold reduction for 8 multiplexed samples (Supp. Data 1).
- Ambient RNA: not quantified. Quote: "while we do not provide a tool for ambient RNA correction, ambient RNA can be imputed with standard packages (CellBender, SoupX) or Souporcell, which leverages the natural genetic variation of multiplexed patients to estimate ambient RNA."
- Recommendation: bulkRNA-seq rather than WES as the genotype reference, especially for snRNA, where SNPs fall mostly in introns and 3′UTRs. Best suited to frozen tissue, where bulkRNA can come from ~1 mg of tissue before multiplexing.

### Data & code availability (verified 2026-10-26)
- GEO **GSE247708** (SuperSeries) = GSE247706 (bulk VCFs, 22 samples) + GSE247707 (pooled 10x, 7 samples). BioProject PRJNA1040187.
- Kidney pooled snRNA: GSM8397034. Files: `Kidney_Pooled_barcodes.tsv.gz` (11,490 barcodes), `features.tsv.gz` (36,601 genes, Gene Expression only), `matrix.mtx.gz` (65 MB; 18,115,867 non-zeros; cellranger-7.1.0). GEO says "raw_feature_bc_matrix", but the barcode count equals the cell-called count, so it is the filtered matrix. No kidney assignment table. SRA SRR29832267 (809,030,462 spots; ENA FASTQ R1 16.5 GB, R2 32.8 GB).
- Kidney bulk: GSM8397029–32 (Patients 19–22; VCFs TS116, TS120, TS121, TS126); SRA SRR29830128–31.
- PBMC pooled GSM7899153 (2,739,993 barcodes, true raw) + CMO assignment table GSM7899154. Heart 1 pooled GSM7899155 (1,080,502 barcodes, true raw) + CMO (GSM7899156) and HTO (GSM7899157) assignment tables. Heart 2 pooled GSM8397033 (11,501 barcodes; its SRA run SRR29832268 shows 0 spots).
- WES: EGA EGAD50000000928 (controlled access).
- Code: https://github.com/ToreBle/SoupLadle ; Zenodo 10.5281/zenodo.13711299. The repo contains PBMC/heart scripts and example data, but no kidney script or per-cell outputs.
