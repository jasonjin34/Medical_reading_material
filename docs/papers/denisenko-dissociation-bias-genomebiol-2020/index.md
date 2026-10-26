# Systematic assessment of tissue dissociation and storage biases in single-cell and single-nucleus RNA-seq workflows

> **Bibkey** `Denisenko_2020` · **Venue** Genome Biology (2020) · **Category** single-cell · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1186/s13059-020-02048-6> · `status: complete`

---

## One-liner
A single-system (healthy adult mouse kidney, 10x Chromium), triplicate comparison of 37 °C vs on-ice cold-protease dissociation, fresh vs cryopreserved vs methanol-fixed cells, and scRNA-seq vs three snRNA-seq nuclei workflows (with bulk RNA-seq controls), quantifying protocol-induced expression artifacts (stress genes) and cell-composition biases; all data public as GSE141115.

## Problem
Solid tissue must be dissociated/preserved/nuclei-isolated before 10x profiling; each step can alter transcriptional profiles (e.g., 37 °C enzymatic digestion inducing immediate-early genes) or the representation of cell types. Prior assessments were scattered across tissues and conditions and lacked bulk comparisons. This paper quantifies these biases side by side in one organ to guide design and interpretation.

## Method
**Experimental arms (all n=3 biological replicates, one kidney per mouse):**

- **Batch 1 (C57BL/6J male, 19 wk, 10x v2):** 37 °C dissociation (Miltenyi Multi Tissue Dissociation Kit 2, gentleMACS `37C_Multi_E`) vs cold dissociation (on-ice *B. licheniformis* cold-active protease, adapted from Adam et al.); each suspension split into fresh / cryopreserved (50% FBS + 40% RPMI-1640 + 10% DMSO, gradient-cooled → liquid N2, 6 weeks) / methanol-fixed (80% MeOH, −20 °C → −80 °C, 3 months); plus bulk RNA-seq of both dissociated suspensions.
- **Batch 2 (Balb/c male, 18 wk, 10x v2):** cold-dissociation scRNA-seq vs SN_FANS_3x500g snRNA-seq (flash-frozen whole kidney), plus whole-kidney bulk.
- **Batch 3 (Balb/c female, 15 wk, 10x v3):** repeat of fresh vs cryopreserved cold-dissociated scRNA-seq (2-week storage, 1200g spins); three snRNA-seq workflows: SN_FANS_3x500g (3 washes, 500g, FANS), SN_FANS_1x2000g (1 wash, 2000g, FANS), SN_sucrose (sucrose cushion, no sorting); plus whole-kidney and cold-dissociated-suspension bulk.

**Analysis:** Cell Ranger 2.1.1 (mm10; pre-mRNA reference counting introns for snRNA) → EmptyDrops → filtering (genes in ≥10 cells; 200–3000 genes/cell, <50% mito; nuclei additionally ≥450 UMIs (v2) / ≥900 (v3) with mito genes removed; Scater UMI/gene-ratio outliers removed) → Seurat v2 CCA integration, Wilcoxon DE. Annotation: scMatch against three public mouse-kidney references + two rounds of signature-score refinement, CNT resolved by sub-clustering (15 cell types). Stress score: 17 literature stress genes hand-picked from the warm-induced list, AddModuleScore, 1000-random-gene-set Monte-Carlo test. Composition via chi-square; bulk via edgeR exact test and BSEQ-sc deconvolution.

## Data
In total 77,656 single-cell, 98,303 single-nucleus and 15 bulk profiles (GEO GSE141115: 27 scRNA, 12 snRNA, 15 bulk samples; Illumina NovaSeq 6000). Batch-1 fresh scRNA: 23,108 cells (cold 11,851 / warm 11,257); methanol-fixed 11,627 (cold) / 5,545 (warm); cryopreserved 3,519 (cold) / 3,483 (warm). Per-arm nuclei counts are in Additional file 14 (not individually checked here).

**GEO contents (verified):** one `GSM*_<lib>.txt.gz` per sample, tab-delimited raw UMI counts, genes × cells (columns like `BG1_BG20C_<barcode>`). The matrices are post-QC cells: batch-1 cold-fresh libraries have 2,356 + 4,084 + 5,411 = 11,851 columns, matching the paper exactly; cold-cryopreserved 897 + 1,629 + 993 = 3,519 also matches. Gene sets are uniform within a batch (13,392 genes for batch-1 fresh, 13,347 for cryo). Arm labels are sample-level (GSM title/characteristics: strain, sex, workflow, 10x chemistry); per-cell cell-type labels live in the paper's Additional file 3 (Table S2), not in GEO. No unfiltered Cell Ranger matrices; FASTQs are on SRA (SRP233496).

## Key results
- **37 °C dissociation induces stress:** bulk shows 71 genes up in warm and 5 up in cold (logFC>2, FDR<0.05); logFC>4 includes *Fosb, Fos, Jun, Junb, Atf3, Egr1, Hspa1a, Hspa1b*; top GO term "regulation of cell death". In scRNA, 64 genes up in warm in ≥1 cell type; *Junb/Jund* DE in 7 cell types, *Jun/Fos* in 5.
- **17-gene stress signature:** *Fosb, Fos, Jun, Junb, Jund, Atf3, Egr1, Hspa1a, Hspa1b, Hsp90ab1, Hspa8, Hspb1, Ier3, Ier2, Btg1, Btg2, Dusp1*; "significantly high stress scores were detected only in warm-dissociated samples in eight out of 14 cell types", with "immune and endothelial cells … particularly sensitive".
- **Dissociation composition bias:** 8 populations depleted in warm (incl. podocytes, mesangial, endothelial; chi-square p<0.001), overlapping the high-stress types; podocytes 3 cells (0.03%) warm vs 330 (2.78%) cold. aLOH (4.99% vs 2.52%) and PT (71.36% vs 63.34%) higher in warm. Cold samples have more hemoglobin transcripts (erythrocyte contamination).
- **Cryopreservation loses epithelium:** PT drops from 63.12%/70.86% fresh (cold/warm) to 0.31%/0.57% cryopreserved; usable cells ~30% of fresh; cryo also induces stress genes (IEGs, HSPs). Repeat (Balb/c female, v3, 2 weeks, 1200g): PT 55.55% → 7.65%.
- **Methanol keeps composition but leaks ambient RNA:** composition close to fresh, macrophages moderately reduced (5.36%→3.2% cold; 4.28%→2.54% warm); the same tubular and hemoglobin transcripts appear across most cell types, indicating damage-driven ambient RNA contamination.
- **sc vs sn:** the three nuclei workflows were comparable, SN_FANS_1x2000g with more mito contamination; median genes 1,819 per nucleus vs 981 per cell. Immune cells 0.73% in snRNA vs 6.03% in scRNA (BSEQ-sc estimates 1.51% female, 4.84% male Balb/c); snRNA recovers only macrophages, no T (1.38% in scRNA), B (0.77%), NK (0.65%); podocytes 0.7% vs 3.28%; LoH and mesangial more abundant in snRNA. lncRNAs higher in snRNA; mito/ribosomal genes higher in scRNA.

## Contributions
- Side-by-side, same-organ, same-lab, triplicate comparison of 2 dissociations × 3 storage states + 3 nuclei workflows + bulk, so biases are directly comparable.
- A reusable 17-gene dissociation-stress signature, and evidence that stress sensitivity couples with cell-type loss.
- Shows severe PT-epithelium loss after cryopreserving kidney suspensions (reproducible across strain, sex, 10x chemistry) and lymphocyte loss in snRNA-seq.

## Limitations
- Healthy mouse kidney only; no disease and no human tissue.
- Batch is confounded with strain/sex/chemistry (batch 1 C57 male v2; batch 3 Balb/c female v3), so sc-vs-sn and the cryo repeat cannot fully separate these factors.
- No composition ground truth: BSEQ-sc deconvolution contradicts the Clark et al. anatomical estimates, and the authors say they "will continue to search for approaches to better define the 'ground truth'".
- The stress signature was hand-picked from warm-induced genes rather than derived independently; tooling (Seurat v2, Cell Ranger 2.1.1) is dated.
- Cold and 37 °C protocols also differ in mechanical steps and spin speeds, so temperature is not the only variable.

## Relation to our direction
Sits at the **detect** stage as a negative-control / nuisance-factor resource. Plan A builds a human-kidney single-cell benchmark testing whether anomaly detectors separate **disease** from **measurement/procurement artifacts**. This dataset provides known, controlled technical perturbations: (1) 37 °C vs cold → dissociation stress (17-gene signature; immune and endothelial most sensitive; podocyte loss); (2) fresh vs cryo vs methanol → storage artifacts (epithelial loss, stress, ambient RNA); (3) sc vs sn → platform/composition bias. Because all tissue is healthy, any cell a detector flags here is a *technical* anomaly, not disease, so it can serve as a false-positive calibration set. Being **mouse**, it is for later calibration / transfer checks only, not the main benchmark; the 17-gene signature needs mapping to human orthologs (FOS, JUN, HSPA1A, …) before annotating artifacts in human kidney data. Caveats: arm labels in GEO are sample-level, and batch is confounded with strain/sex/chemistry.

## Reusable assets
- **Code:** no code repository given in the paper.
- **Data:** GEO GSE141115 (54 samples, post-QC UMI count matrices, sample-level arm labels); SRA SRP233496 (FASTQs); per-cell type labels in Additional file 3, per-arm cell counts in Additional file 14, DE tables in Additional files 1/4/5/7–10.
- **Checkpoints:** none; reusable items are the 17-gene stress signature and the scMatch mouse-kidney references (Additional files 19/21).

## Follow-ups
- Adam et al. 2017 (cold-active protease dissociation, Development) — the original cold method.
- van den Brink et al. 2017 Nat Methods (dissociation-induced transcriptional changes).
- Wu et al. 2019 JASN (kidney sc vs sn) and Slyper et al. (cited as bioRxiv 2019; sc/sn toolbox for fresh and frozen human tumours).
- Human-tissue counterparts (e.g., human kidney biopsy dissociation/storage artifacts) and SoupX / DecontX for ambient-RNA removal.

## Cite
```bibtex
@article{Denisenko_2020, title={Systematic assessment of tissue dissociation and storage biases in single-cell and single-nucleus RNA-seq workflows}, volume={21}, ISSN={1474-760X}, url={http://dx.doi.org/10.1186/s13059-020-02048-6}, DOI={10.1186/s13059-020-02048-6}, number={1}, journal={Genome Biology}, publisher={Springer Science and Business Media LLC}, author={Denisenko, Elena and Guo, Belinda B. and Jones, Matthew and Hou, Rui and de Kock, Leanne and Lassmann, Timo and Poppe, Daniel and Clément, Olivier and Simmons, Rebecca K. and Lister, Ryan and Forrest, Alistair R. R.}, year={2020}, month=June }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
