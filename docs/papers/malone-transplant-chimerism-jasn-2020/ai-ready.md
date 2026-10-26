<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# Harnessing Expressed Single Nucleotide Variation and Single Cell RNA Sequencing To Define Immune Cell Chimerism in the Rejecting Kidney Transplant

- **Authors:** Malone, Andrew F.; Wu, Haojia; Fronick, Catrina; Fulton, Robert; Gaut, Joseph P.; Humphreys, Benjamin D.
- **Venue / Year:** Journal of the American Society of Nephrology · 2020
- **DOI:** 10.1681/ASN.2020030326
- **URL:** https://doi.org/10.1681/asn.2020030326
- **Bibkey:** Malone_2020
- **Status:** complete (main text read from the free PMC version, PMC7461682; supplement not retrieved)
- **PMID / PMCID:** 32669324 / PMC7461682
- **Preprint:** bioRxiv 10.1101/2020.03.10.986075
- **Data:** GEO GSE145927; SRA SRP250734 / BioProject PRJNA608747

## Abstract
Significance Statement
                    The combination of exome sequencing with single-cell RNA sequencing can reveal the recipient versus donor origin of each immune cell within human kidney allografts. This approach greatly improves upon previous techniques used to identify and describe leukocyte chimerism within a complex organ, such as Y chromosome identification for sex-mismatched transplants. Exome sequencing and single-cell RNA sequencing of single nucleotide variants indicated that donor-origin macrophages may contribute to the alloimmune response through antigen presentation and signaling, whereas donor-origin T cells remain quiescent. Therefore, teaming these techniques can paint a portrait of the chimerism that may lie behind rejection of a donor kidney.
                  
                  
                    Background
                    In solid organ transplantation, donor-derived immune cells are assumed to decline with time after surgery. Whether donor leukocytes persist within kidney transplants or play any role in rejection is unknown, however, in part because of limited techniques for distinguishing recipient from donor cells.
                  
                  
                    Methods
                    Whole-exome sequencing of donor and recipient DNA and single-cell RNA sequencing (scRNA-seq) of five human kidney transplant biopsy cores distinguished immune cell contributions from both participants. DNA-sequence comparisons used single nucleotide variants (SNVs) identified in the exome sequences across all samples.
                  
                  
                    Results
                    Analysis of expressed SNVs in the scRNA-seq data set distinguished recipient versus donor origin for all 81,139 cells examined. The leukocyte donor/recipient ratio varied with rejection status for macrophages and with time post-transplant for lymphocytes. Recipient macrophages displayed inflammatory activation whereas donor macrophages demonstrated antigen presentation and complement signaling. Recipient-origin T cells expressed cytotoxic and proinflammatory genes consistent with an effector cell phenotype, whereas donor-origin T cells appeared quiescent, expressing oxidative phosphorylation genes. Finally, both donor and recipient T cell clones within the rejecting kidney suggested lymphoid aggregation. The results indicate that donor-origin macrophages and T cells have distinct transcriptional profiles compared with their recipient counterparts, and that donor macrophages can persist for years post-transplantation.
                  
                  
                    Conclusions
                    Analysis of single nucleotide variants and their expression in single cells provides a powerful novel approach to accurately define leukocyte chimerism in a complex organ such as a transplanted kidney, coupled with the ability to examine transcriptional profiles at single-cell resolution.
                  
                  
                    Podcast
                    This article contains a podcast at https://www.asn-online.org/media/podcast/JASN/2020_08_07_JASN2020030326.mp3

## Full text / Extract
> Structured extract of the main text (the article is free to read in PMC but not under an open licence, so this is a condensed paraphrase with short quotes, not a verbatim copy).

### Cohort
- Indication kidney-transplant biopsies, Washington University (IRB-approved), freshly processed.
- 5 biopsies / 5 patients: 3 acute antibody-mediated rejection (ABMR; all with donor-specific antibodies; one ABO anti-A isoantibody case counted as DSA), 2 non-rejection AKI. Biopsies 5 days to 7 years post-transplant. All received ATG + methylprednisolone induction, then tacrolimus/MMF/prednisone; one rejecting and one non-rejecting patient also received anti-CD20.
- Separate "independent data set": serial biopsies from one ABMR patient at diagnosis (945 days) and 1 month after treatment (974 days) (Fig 3G).

### Wet lab and sequencing
- Dissociation: 0.25% trypsin + 40 U/ml DNase I at 37 °C, cells collected every 10 min through a 70-µm strainer, ~30 min in total, 40-µm final strain; ~90% viability (Trypan Blue).
- 10x Chromium, 2 lanes per biopsy, target 10,000 cells/lane; "The 5 Prime kits were used" plus T-cell VDJ libraries.
- Paired-end sequencing, 50,000 reads/cell (GEX), 5,000 reads/cell (VDJ). Text says Illumina HiSeq; SRA lists NovaSeq 6000.
- WES of donor and recipient germline DNA (peripheral blood), 50× target; BWA-MEM, Picard MarkDuplicates, GATK BQSR (CCDG functional-equivalence pipeline); CRAM; GATK best-practice filtering of common variants (AF > 0.05).

### Computational pipeline
- Cell Ranger 3.0 → Seurat v3. Filters: genes in ≥3 cells; 200–2500 genes/cell; < 25% mitochondrial.
- Per-biopsy over-clustering; "Clusters containing two or more different cell type–defining markers were removed as doublet clusters"; low-gene clusters removed as debris. Seurat v3 integration; "minimal batch effect".
- Demuxlet on each biopsy with the combined donor+recipient .vcf (mean 120,896 coding SNVs per pair) and the Cell Ranger BAM; default parameters, alpha 0, 0.5 and 1; each cell labelled from the BEST column.
- DE: Seurat FindMarkers (min.pct 0.25, logFC 0.25, adj. P < 0.05) → ToppFun (Bonferroni P ≤ 0.05). Spearman correlations of T-cell groups. VDJ via Loupe VDJ Browser (clone = complete α and β).

### Results
- 81,139 cells after filtering; mean 1,124 genes and 2,497 transcripts per cell. Eight kidney clusters (activated tubular/PT, LOH, PT, principal cells, intercalated cells, endothelial, stroma; "activated PT" enriched for secretion, apoptosis regulation, oxidative stress and leukocyte-activation GO terms) and two immune clusters: 5,027 macrophages, 3,647 lymphocytes.
- Demuxlet: median SNVs per cell 71–231 across biopsies; minimum 17; lower quartiles > 50. "This allowed for 90% accuracy for all cells in the data set and close to 100% accuracy in cells above the lower interquartile range."
- Doublets: "Despite manual filtering and removal of doublet cells … the Demuxlet tool identified 3%–10.5% of cells as doublets which allowed for improved quality control of the data set."
- Origin: macrophages 3,798 recipient / 1,229 donor; lymphocytes 1,528 recipient / 2,119 donor. Origin fractions for non-immune clusters are not stated in the main text (Fig 2B colours all 81,139 cells by origin).
- Macrophages: roughly equal donor/recipient in the two non-rejecting biopsies; recipient-dominated in rejection (donor 4–39 vs recipient 514–1,258 cells per rejecting sample; non-rejecting donor 217–964 vs recipient 389–674). 35.8% donor at day 28 (non-rejecting); 97% recipient at day 11 (rejecting). Serial biopsy: donor macrophages 3% → 11.7% after treatment (96 → 100 cells).
- Recipient macrophages: IL-6 signalling, IFN signalling, FCγR pathways; CD16 (FCGR3A), CD68; classical-activation genes. Donor macrophages: complement (C1QA/B/C), antigen presentation, immunoregulation (PD-1), F13A1, CD14; wound-healing genes. Neither group fits M1/M2 cleanly.
- Lymphocyte subclusters: T 3,067, B 190, plasma 231, mast 111. Donor lymphocyte share falls with time; few donor lymphocytes by day 232.
- Recipient T cells ~ rejecting T cells (Spearman 0.8): NKG7, GNLY, GZMB, PRF1; IL-12/STAT4, IL-6, HIFα pathways. Donor T cells ~ non-rejecting T cells (1.0): IL32, CD52, MIF, S100A6, S100A11, LTB; oxidative phosphorylation → quiescent.
- VDJ in 3 biopsies: 120/3,115 T cells with complete VDJ; 34 donor (all from the day-11 rejection biopsy), 86 recipient (from the 6.5-month rejection biopsy).
- The main text does not mention ambient RNA, background or soup contamination.

### Data availability (checked on GEO/SRA, 2026-10-26)
- GEO GSE145927 (public since 22 Jul 2020): 7 scRNA samples — Biopsy1_Day28, Biopsy2_Day2542 (7 yr), Biopsy3_Day11, Biopsy4_Day5, Biopsy5_Day232 (10x 5′), Biopsy6_Pre-treatment, Biopsy7_Post-treatment (10x 3′); 10 WES samples (donor and recipient for biopsies 1–5; PBMC; IDT xGen Exome v1.0; NovaSeq 6000) with no processed files.
- Supplementary: one `GSM*_<day>rawcounts.csv.gz` per scRNA sample (gene × barcode UMI counts of post-QC cells only; e.g. Day11 = 5,395 cells, matching metadata biopsy65), and `GSE145927_MGI.metadata.csv.gz` (81,139 rows: orig.ident biopsy62/64/65/67/68, nCount_RNA, nFeature_RNA, percent.mt, percent.ribo, cluster columns, SNV_GT donor/recipient, stim rejn/no_rejn, ident cell type). No doublet labels, no VCF, no raw-droplet matrices.
- SRA SRP250734: 17 scRNA runs (5′ runs ~32–65 GB each) and 10 WES runs (~1–1.5 GB each), listed with public download paths (no dbGaP controlled access).
- Caution (our tabulation): metadata SNV_GT gives macrophages 4,715 donor / 312 recipient, which does not match the paper's 1,229 donor / 3,798 recipient, and the recipient fraction is nearly uniform across cell types within each biopsy. Treat SNV_GT as unverified.
