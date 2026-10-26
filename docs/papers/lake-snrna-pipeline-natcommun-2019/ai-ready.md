<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# A single-nucleus RNA-sequencing pipeline to decipher the molecular anatomy and pathophysiology of human kidneys

- **Authors:** Lake, Blue B.; Chen, Song; Hoshi, Masato; Plongthongkum, Nongluk; Salamon, Diane; Knoten, Amanda; Vijayan, Anitha; Venkatesh, Ramakrishna; Kim, Eric H.; Gao, Derek; Gaut, Joseph; Zhang, Kun; Jain, Sanjay
- **Venue / Year:** Nature Communications · 2019
- **DOI:** 10.1038/s41467-019-10861-2
- **URL:** https://doi.org/10.1038/s41467-019-10861-2
- **Bibkey:** Lake_2019
- **Status:** complete

## Abstract
Defining cellular and molecular identities within the kidney is necessary to understand its organization and function in health and disease. Here we demonstrate a reproducible method with minimal artifacts for single-nucleus Droplet-based RNA sequencing (snDrop-Seq) that we use to resolve thirty distinct cell populations in human adult kidney. We define molecular transition states along more than ten nephron segments spanning two major kidney regions. We further delineate cell type-specific expression of genes associated with chronic kidney disease, diabetes and hypertension, providing insight into possible targeted therapies. This includes expression of a hypertension-associated mechano-sensory ion channel in mesangial cells, and identification of proximal tubule cell populations defined by pathogenic expression signatures. Our fully optimized, quality-controlled transcriptomic profiling pipeline constitutes a tool for the generation of healthy and diseased molecular atlases applicable to clinical samples.

## Full text / Extract
Source: full-text PDF (Nat Commun 10:2832, open access, PMC6597610) plus GEO GSE121862 sample annotations. Supplementary Data/Figures not read.

### Study design
- Tissue: tumour-free regions of living-patient partial/total nephrectomies and discarded deceased-donor kidneys (Washington University, KTRC), plus tumour nephrectomies from University of Michigan (KPMP). No biopsies in the dataset; the pipeline uses ~6 mm3 tissue on average, "compatible with clinically relevant biopsy samples".
- Processing methods compared (Fig. 1a): frozen whole tissue; O.C.T. cryosections (~40 um) frozen (cryoF), in Wisconsin cold-storage solution (cryoW) or in RNAlater (cryoR); fresh tissue partially dissociated with papain/collagenase (dissocPC) or trypsin/collagenase (dissocTC). GEO: "7 different tissue processing methods" (GEO also lists a whole-tissue "RNAlater 6 Hours" condition).
- Only nuclei from O.C.T. cryosections and dissociated fresh tissue were snDrop-seq compatible; fluorescent sorting of nuclei impeded success.
- Platform: snDrop-seq (modified Drop-seq), Illumina HiSeq 2500 (GPL16791). Pipeline: https://github.com/chensong611/Dropseq_pipeline
- Scale: 27 experiments, 47 libraries, 15 individuals, two institutions; 17,659 nuclei after QC; mean 1,082 UMIs per nucleus; 30 clusters (PAGODA2).
- QC: >400 non-MT transcripts; >400 and <5000 genes; MT genes excluded; gene/UMI-ratio outlier filter; clusters <30 nuclei removed; one 120-nucleus marker-less cluster removed.

### Processing-related findings (verbatim where quoted)
- "we observed the fewest MTs and stress-induced artifacts in cryoR samples compared to cryosections processed differently (cryoW, cryoF) or fresh dissociated samples (dissocPC, dissocTC), while global gene and transcript levels appeared unaffected"
- TAL-1 (cluster 12) and S3 PT (PT-5, cluster 7) "showed MT enrichment consistent with the nephrectomy procedure-related warm ischemia".
- Method comparisons showed high correspondence, "with cryoW showing the lowest correlation in gene expression values".
- "Differential expression analysis between the different methods revealed a stress response signature (including FOS, FOSB, DNAJB1) that was specifically associated with whole cell dissociative methods".
- PC-2 (cluster 17) "was found to be mostly attributed by dissocP/T processing methods ... and as such likely represented a dissociation artifact".
- PT-3 (cluster 5), inflammatory genes, came predominantly from a single individual.
- "CryoR samples showed the fewest expression artifacts while also exhibiting higher experimental success rates (>90%)".

### Biology
- 30 populations incl. POD, PT-1..5, DTL, ATL-1..3, TAL-1..2, DCT, CNT, PC-1..3, IC-A1/A2/B, EC-1..3, GC, MC, vSMC/P, INT, IMM.
- 111/674 CKD eQTL genes and 56/220 hypertension-risk genes differentially expressed across clusters; PODs enriched for CKD loci, MCs for hypertension loci; PIEZO2 in mesangial cells; CFH+ S2 PT and FGA/FGB+ S3 PT populations; KIT and CALCA in medullary IC-A2.

### Data availability (GSE121862)
- 47 GSMs (GSM3448110-GSM3448156), one per library, each annotated with experiment, barcode, ppid, region, tissue collection, tissue processing, sex, source.
- GSE121862_UCSD-WU_Single_Nuclei_Cluster_Annotated_Raw_UMI_Matrix.tsv.gz: 17,659 nuclei; column names C{cluster}_NK{library}_{cell barcode}; MT genes absent.
- GSE121862_UCSD-WU_Single_Nuclei_Cluster_Annotations.csv.gz: 30 cluster IDs, abbreviations, annotations.
- Raw reads: SRA SRP166966.
- Per-nucleus processing method is recoverable by joining the NK library ID to the GEO sample annotation.
