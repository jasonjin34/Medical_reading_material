<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# Single-cell multi-omic and spatial profiling of human kidneys implicates the fibrotic microenvironment in kidney disease progression

- **Authors:** Abedini, Amin; Levinsohn, Jonathan; Klötzer, Konstantin A.; Dumoulin, Bernhard; Ma, Ziyuan; Frederick, Julia; Dhillon, Poonam; Balzer, Michael S.; Shrestha, Rojesh; Liu, Hongbo; Vitale, Steven; Bergeson, Andi M.; Devalaraja-Narashimha, Kishor; Grandi, Paola; Bhattacharyya, Tanmoy; Hu, Erding; Pullen, Steven S.; Boustany-Kari, Carine M.; Guarnieri, Paolo; Karihaloo, Anil; Traum, Daniel; Yan, Hanying; Coleman, Kyle; Palmer, Matthew; Sarov-Blat, Lea; Morton, Lori; Hunter, Christopher A.; Kaestner, Klaus H.; Li, Mingyao; Susztak, Katalin
- **Venue / Year:** Nature Genetics · 2024
- **DOI:** 10.1038/s41588-024-01802-x
- **URL:** https://doi.org/10.1038/s41588-024-01802-x
- **Bibkey:** Abedini_2024
- **Status:** complete

## Abstract
Kidneys are intricate three-dimensional structures in the body, yet the spatial and molecular principles of kidney health and disease remain inadequately understood. We generated high-quality datasets for 81 samples, including single-cell, single-nuclear, spot-level (Visium) and single-cell resolution (CosMx) spatial-RNA expression and single-nuclear open chromatin, capturing cells from healthy, diabetic and hypertensive diseased human kidneys. Combining these data, we identify cell types and map them to their locations within the tissue. Unbiased deconvolution of the spatial data identifies the following four distinct microenvironments: glomerular, immune, tubule and fibrotic. We describe the complex organization of microenvironments in health and disease and find that the fibrotic microenvironment is able to molecularly classify human kidneys and offers an improved prognosis compared to traditional histopathology. We provide a comprehensive spatially resolved molecular roadmap of the human kidney and the fibrotic process, demonstrating the clinical utility of spatial transcriptomics.

*Editor's summary (Nature):* A spatial transcriptomic analysis of healthy kidneys and those from individuals with chronic kidney disease characterizes the fibrotic microenvironment and highlights features that could be used to predict prognosis.

## Full text / Extract
<!-- Key methods/data extracted from the PMC author manuscript (PMC11592391), Supplementary Note, Supplementary Tables 1–2, Reporting Summary and GEO GSE211785. Quotes are verbatim; counts derived from the tables are marked "derived". -->

### Cohort and tissue
- Reporting Summary: "The un-affected portions of nephrectomies mostly due to tumor were obtained. Consent was exempted because the samples were collected were considered as medical discard."
- Methods: "Left-over kidney samples were irreversibly de-identified, and no personal identifiers were gathered." "Cortical and outer medullary areas of the human kidney were used for scRNA-seq, snRNA-seq and snATAC–seq."
- Results: "81 human kidney tissue samples from 58 participants (62% male and age of 64.1 ± 14.0 years)." "(1) healthy control (n = 36) determined by eGFR > 60 ml min−1 1.73 m−2 and fibrosis score of <10%, and (2) CKD (n = 45) determined by (eGFR) < 60 ml min−1 1.73 m−2 or kidney fibrosis score of >10%, including 20 with the clinical histopathological diagnosis of DKD and 25 with the clinical diagnosis of hypertensive-attributed CKD."
- Reporting Summary (per library): "29 scRNA-seq data were generated (Control:15, DKD:4, HKD: 10). 18 snRNA-seq data were generated; (Control:7, DKD:4, HKD:7). 18 snATAC-seq data were generated (Control: 10, DKD:6, HKD: 2). 14 spRNA-seq data were generated (Control:3, DKD:6, HKD:5)."
- Derived from Supplementary Table 1 (unique donor IDs; control/DKD/HKD): scRNA 14/4/8; snRNA 7/3/8; snATAC 7/4/2; Visium 3/6/5; CosMx 1/1. Donors with both scRNA and snRNA: HK2833, HK2867, HK2893, HK2895, HK2899 (control), HK2770, HK2774, HK2891 (HKD). 57 unique IDs are listed (text says 58).
- Derived from GEO cell metadata: scRNA 126,963 cells; snRNA 155,647 nuclei; snATAC 55,955 nuclei; total 338,565.

### Assays
- scRNA-seq: "Fresh human kidneys (0.5 g) collected in RPMI media were minced ... Multi Tissue Dissociation Kit 1 ... incubated for 30 min at 37 °C ... greater than 80% viability." 10X Chromium Next GEM Single Cell 3′ v3.1, NovaSeq 6000.
- snRNA-seq: "10–30 mg of frozen kidney tissue was minced" with NP40 lysis buffer and gentleMACS; same 10X 3′ v3.1 chemistry.
- snATAC-seq: same nuclei isolation; "Chromium single-cell ATAC Library and Gel Bead Kit" (Chip E) — separate libraries, not multiome.
- Visium FFPE: "samples with DV200 > 50% were selected"; 5 μm sections; H&E imaged on Keyence BZ-X810.
- CosMx: "human universal cell characterization RNA probes, plus 50 additional custom probes"; ~1,000 genes; 2 samples (HK3039 healthy, HK2844 DKD).

### QC and processing (Supplementary Note)
- "Ambient RNA was corrected using SoupX (v1.5.0) and doublets were removed by DoubletFinder (v2.0) with default parameters."
- "The QC filters applied were: (a) cells with n_feature counts more than 3000 or less than 200, (b) cells with more than 15% mitochondrial counts (for snRNAseq data) and more than 50% mitochondrial counts (for scRNAseq data), and (c) cells with more than 15% ribosomal gene counts."
- "Clusters expressing multiple cell types of specific marker genes were excluded as potential doublets." "Cells were considered doublets and eliminated from the dataset if the original annotation was incompatible with the predicted cell type."
- snATAC: "peak_region_fragments < 3000 & peak_region_fragments > 20000 & pct_reads_in_peaks < 15 & nucleosome_signal > 4 & TSS.enrichment < 2" removed.
- Integration: "We used SCVI (v0.20.3) ... using the sample, nFeature_RNA, nCount_RNA, and tech factors as covariates."
- Statistics: "For comparisons within our single-cell data, we treat each cell as an independent observation, after merging samples."

### Key results
- 44 main and 114 cell subtypes/states; integrated with KPMP to 588,425 cells/nuclei.
- Four Visium NMF microenvironments; FME correlates with pathologist fibrosis (r = 0.75, P = 0.003).
- iPT_VCAM1+ "was present in healthy samples"; iPT_HAVCR1+ mostly in CKD and FME.
- In 245 bulk tubule samples with fibrosis <10%: fibrosis score "HR = 1.17, 95% CI: 0.49–2.83"; FME-GS cluster 1 "HR = 3.95, 95% CI: 1.71–9.12"; top-10 LASSO genes P = 0.021.

### Data and code availability
- "Raw data, processed data and metadata from the snRNA-seq, scRNA-seq, snATAC–seq and spRNA-seq have been deposited in Gene Expression Omnibus with the accession code GSE211785."
- GEO overall design: "**Raw data were not provided due to privacy concerns**"; processed files: merged PreSCVI/PostSCVI h5ad, PostSCVI with KPMP, CosMx annotated h5ad, counts .rds, metadata, Visium tif/json. No licence statement found on GEO or the GitHub repos.
- Code: https://github.com/amin69upenn/Human_Kidney_Multiomics_and_Spatial_Atlas_ and https://github.com/jlevins2010/FME_atlas
