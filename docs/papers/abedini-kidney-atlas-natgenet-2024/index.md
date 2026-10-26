# Single-cell multi-omic and spatial profiling of human kidneys implicates the fibrotic microenvironment in kidney disease progression

> **Bibkey** `Abedini_2024` · **Venue** Nature Genetics (2024) · **Category** single-cell · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1038/s41588-024-01802-x> · `status: complete`

---

## One-liner
A UPenn (Susztak lab) multi-omic and spatial atlas of the human kidney: 81 samples from 58 participants (Supplementary Table 1 actually lists 57 IDs) profiled by scRNA-seq, snRNA-seq and snATAC-seq (three separate libraries, not multiome), Visium FFPE and CosMx. The integrated SCVI atlas holds 338,565 cells/nuclei in 44 main types and 114 subtypes/states. NMF on Visium finds four microenvironments (glomerular, tubule, fibrotic, immune). A fibrotic-microenvironment gene signature (FME-GS) predicts kidney-function decline in 245 bulk tubule samples with fibrosis < 10% (HR = 3.95), where the pathologist's fibrosis score does not (HR = 1.17).

## Problem
Diabetes and hypertension cause > 75% of CKD, and fibrosis is the common end-stage of all progressive CKD. Yet the cellular make-up and spatial organisation of fibrotic lesions are poorly known: prior work focused on ECM accumulation. Dissociated single-cell data also drop location, so cells defined only by anatomy (mesangial cells, PECs, fibroblast subtypes) are hard to pin to a molecular identity. Clinically, prognosis in early CKD (preserved eGFR, fibrosis < 10%) is hard to call, and the pathologist's fibrosis score predicts outcome inconsistently.

## Method
**Wet lab**: scRNA-seq uses **fresh** tissue (0.5 g) digested with Miltenyi Multi Tissue Dissociation Kit 1 at 37 °C for 30 min, then RBC lysis, giving > 80% viability. snRNA-seq uses **frozen** tissue (10–30 mg), NP40 lysis and gentleMACS homogenisation. Both run on 10x Chromium Next GEM 3′ v3.1 (Chip G) and are sequenced on NovaSeq 6000. snATAC-seq uses the same nuclei prep with 10x Chromium Single Cell ATAC (Chip E), in **libraries separate from RNA, not multiome**. Visium is the FFPE probe-based assay, with samples required to have DV200 > 50% and 5 µm sections. CosMx uses the ~1,000-gene universal cell characterization panel plus 50 custom probes. IMC (Hyperion) and immunofluorescence provide protein validation.
**Bioinformatics** (Supplementary Note): Cell Ranger v6.0.1 / Cell Ranger ATAC. Ambient RNA is corrected with SoupX v1.5.0 and doublets are removed with DoubletFinder v2.0 (default parameters). Thresholds are nFeature 200–3000, mitochondrial fraction < 15% (sn) and < 50% (sc), and ribosomal fraction < 15%. Clusters co-expressing markers of several cell types are then removed, and cells whose annotation disagrees with label transfer from a published reference are dropped as doublets. Harmony is applied to sn and sc separately. SCVI (v0.20.3, with sample, nFeature_RNA, nCount_RNA and tech as covariates) integrates the three modalities into one atlas, and a version merged with KPMP has ~600k cells. Visium is deconvolved with Cell2location and mapped to near single-cell resolution with CellTrek (149,717 points); STutility NMF then splits it into microenvironments. Cell communication uses CellChat and COMMOT, the iPT trajectory uses Monocle3, FME-GS is clustered on bulk data, prognosis uses Kaplan–Meier/Cox, and LASSO is run on top.

## Data
**Tissue source**: the Reporting Summary says "The un-affected portions of nephrectomies mostly due to tumor"; the tissue was medical discard, so consent was exempted. Cortex and outer medulla were sampled. **Groups**: the main text gives 36 control samples (eGFR > 60 and fibrosis < 10%) and 45 CKD samples (20 DKD, 25 HKD).
**Donors** (Supplementary Table 1, unique IDs, control / DKD / HKD): scRNA 14 / 4 / 8, i.e. 26 donors in 29 libraries (HK1635, HK1650 and HK1664 each have G and T libraries); snRNA 7 / 3 / 8, i.e. 18 donors; snATAC 7 / 4 / 2, i.e. 13 donors in 18 libraries (replicate libraries); Visium 3 / 6 / 5, i.e. 14 donors; CosMx 1 / 1 (HK3039 control, HK2844 DKD). **Eight donors have both sc and sn** (controls HK2833, HK2867, HK2893, HK2895, HK2899; HKD HK2770, HK2774, HK2891). In total 16 control donors have sc or sn RNA.
**Cells** (GEO cell-level metadata): scRNA 126,963 (control 53,311 / disease 73,652), snRNA 155,647 (53,416 / 102,231), snATAC 55,955 (30,103 / 25,852; the text says 57,847), 338,565 in total.
**Inconsistent counts across sources**: the Reporting Summary counts libraries, giving sc 15/4/10, sn 7/4/7 and ATAC 10/6/2. The text calls Visium "seven DKD and four HKD", while Supplementary Table 1 has 6 DKD / 5 HKD. GEO sample labels also conflict with Supplementary Table 1: for example, HK2478 is HKD on GEO but DKD in the table, and GEO labels "Disease18_snRNAseq" as Control.
**External bulk cohort**: 292 microdissected tubule bulk RNA-seq samples (GSE115098, GSE173343).

## Key results
- **Atlas**: 338,565 cells/nuclei in 6 superfamilies, 44 main types and 114 subtypes/states. It includes 11 endothelial types (FBLN5+ afferent/efferent arterioles, MCTP1+ vasa recta), rare EPO-producing cells, SLC47A2-high PT and a full set of immune subsets; integrated with KPMP it holds 588,425 cells.
- **Stroma**: 12 subtypes, with markers that separate them: mesangial ITGA8/POSTN, VSMC/pericyte MYH11/NOTCH3/NTRK3, fibroblast KCNK2/FAP, myofibroblast COL1A1/SYNPO2. Myofibroblasts have the highest ECM score and are more frequent in disease samples.
- **FME**: the NMF fibrotic microenvironment correlates with the pathologist's fibrosis score (r = 0.75, P = 0.003). It contains fibroblasts, myofibroblasts, endothelium, immune cells (early tertiary-lymphoid-like aggregates) and iPT, and is enriched for SPP1, CXCL12, CCL19/21, PDGFB and TGFB1 signalling.
- **Two iPT subtypes**: iPT_VCAM1+ is metabolic and "present in healthy samples"; iPT_HAVCR1+ (KIM1) is adhesion/matrix-like and found mostly in CKD samples and the FME. Monocle shows a continuous PT → iPT path. CosMx further splits iPT into iPT_APOE, iPT_SPP1 and iPT_KRT7, which have different neighbours.
- **Prognosis**: in 292 bulk samples, the FME-GS cluster 1 is ~4× more likely to reach the endpoint (40% eGFR decline or ESRD). In 245 samples with fibrosis < 10%, FME-GS gives HR = 3.95 (95% CI 1.71–9.12) and the pathologist's fibrosis score gives HR = 1.17 (0.49–2.83). The top 10 LASSO genes alone remain significant (P = 0.021); a random gene set does not.

## Contributions
- Uses sc, sn, ATAC, Visium, CosMx and IMC on one set of nephrectomy samples for cross-validation, giving molecular markers to anatomy-defined cells (PEC, mesangial cells, fibroblast subtypes).
- Reframes fibrosis from ECM accumulation to a multicellular spatial microenvironment (FME), and shows its signature predicts prognosis in early CKD better than pathology scores.
- Publicly releases processed h5ad objects (including the joint integration with KPMP) and interactive websites.

## Limitations
- Admitted by the authors: HKD may not be a single entity; FME-GS needs external-cohort validation; the function of iPT and immune cells needs mechanistic experiments.
- Single-cell statistics "treat each cell as an independent observation" (pseudo-replication), so P-values for between-group proportion differences are optimistic.
- Design confounds: sc uses fresh enzymatic digestion and sn uses frozen tissue, and the two have different group mixes. The early HK1xxx batch is almost all sc, while the later HK28xx batch has both sc and sn. In Supplementary Table 2, control scRNA libraries have a median of median-genes/cell of ~358 versus ~598 for disease, with some controls as low as 17 (HK2662) and 70 (HK2899 SC). In other words, **measurement quality is correlated with the disease label**.
- Counts disagree across the text, supplementary tables, Reporting Summary and GEO (see Data). Raw FASTQs are not released ("Raw data were not provided due to privacy concerns").
- "Healthy" controls are tumour-nephrectomy adjacent tissue, and 8 of 25 control donors are marked hypertensive; the authors also see iPT_VCAM1+ cells and low-grade fibrosis in controls.

## Relation to our direction
**Stage**: the data foundation for the detect stage. In Plan A (a human-kidney single-cell benchmark testing whether anomaly detectors separate disease from measurement/procurement artifacts, with donor-level conformal false-alarm control), it is the **second cohort**: healthy donors from a different lab test whether the false-alarm rate transfers.
**What helps**: (1) The control arm is usable: 14 sc donors and 7 sn donors, 16 unique. Five controls have both sc and sn, giving natural **same-donor, different-protocol** pairs that directly test whether protocol artifacts trigger false alarms. (2) Cell-level QC covariates (nCount, nFeature, percent_mt) and a tech label are available for building artifact axes. (3) The tissue comes from tumour nephrectomy, unlike KPMP living-donor biopsies or Lake 2023's mixed sources, so it provides a "procurement" shift.
**Risks** (these belong in the benchmark design): (a) Control sc libraries are systematically lower quality, so a detector compared naively on disease versus control may learn quality rather than disease; calibrate the conformal step within controls first. (b) The GEO objects are already SoupX-corrected (nCount_RNA is non-integer in the metadata) and already filtered by DoubletFinder, an nFeature ≤ 3000 cap, mitochondrial-fraction thresholds and marker-based doublet removal. **Artifacts are therefore partly removed, unevenly across samples**, and without FASTQs nothing can be reprocessed uniformly. (c) Each modality has few donors (only 7 sn controls), so the calibration set for donor-level conformal is tiny; use leave-one-donor-out, or pool sc and sn and stratify by tech. (d) Some samples have very few cells (HK2976 SN 12, HK2899 SC 183, HK1635_T SC 491); set a minimum-cell threshold. (e) Controls include hypertensive donors and iPT_VCAM1+ cells, so the "healthy" label is itself noisy; run sensitivity analyses on eGFR/fibrosis. (f) The GEO series is also linked to four other PMIDs, and other datasets from the same lab may share donors (**unverified**); deduplicate by HK ID before merging cohorts.

## Reusable assets
- **Code:** GitHub `amin69upenn/Human_Kidney_Multiomics_and_Spatial_Atlas_` and `jlevins2010/FME_atlas`; neither repo has a LICENSE file.
- **Data:** GEO GSE211785 offers processed data only: merged PreSCVI h5ad (4.7 GB), PostSCVI h5ad (5.5 GB), an h5ad jointly integrated with KPMP (9.0 GB), counts .rds (1.7 GB), cell metadata (9.1 MB), CosMx h5ad (620 MB), Visium counts .rds (135 MB) and Visium tif/json (RAW.tar, 1.2 GB, also holds only the tif/json for 7 Visium samples). No explicit licence statement was found. Interactive sites: susztaklab.com/hk_genemap and susztaklab.com/samui. Bulk data are in GSE115098 and GSE173343.
- **Checkpoints:** No pretrained weights; the PostSCVI h5ad may contain the SCVI latent (not downloaded to check).

## Follow-ups
- Download the PreSCVI h5ad and check three things: whether `X` and the layers hold raw integer counts or SoupX-corrected counts; whether per-sample batch/HK IDs are kept; and whether sc and sn share one gene set.
- Check the four other PMIDs linked to GSE211785 (38217002, 38514613, 40796935, 41376591) for donor overlap between these same-lab datasets and this one.
- Compare with the Lake 2023 (KPMP) controls, using procurement route (nephrectomy, biopsy, deceased donor) as the benchmark's procurement axis.

## Cite
```bibtex
@article{Abedini_2024, title={Single-cell multi-omic and spatial profiling of human kidneys implicates the fibrotic microenvironment in kidney disease progression}, volume={56}, ISSN={1546-1718}, url={http://dx.doi.org/10.1038/s41588-024-01802-x}, DOI={10.1038/s41588-024-01802-x}, number={8}, journal={Nature Genetics}, publisher={Springer Science and Business Media LLC}, author={Abedini, Amin and Levinsohn, Jonathan and Klötzer, Konstantin A. and Dumoulin, Bernhard and Ma, Ziyuan and Frederick, Julia and Dhillon, Poonam and Balzer, Michael S. and Shrestha, Rojesh and Liu, Hongbo and Vitale, Steven and Bergeson, Andi M. and Devalaraja-Narashimha, Kishor and Grandi, Paola and Bhattacharyya, Tanmoy and Hu, Erding and Pullen, Steven S. and Boustany-Kari, Carine M. and Guarnieri, Paolo and Karihaloo, Anil and Traum, Daniel and Yan, Hanying and Coleman, Kyle and Palmer, Matthew and Sarov-Blat, Lea and Morton, Lori and Hunter, Christopher A. and Kaestner, Klaus H. and Li, Mingyao and Susztak, Katalin}, year={2024}, month=July, pages={1712–1724} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
