# A single-nucleus RNA-sequencing pipeline to decipher the molecular anatomy and pathophysiology of human kidneys

> **Bibkey** `Lake_2019` · **Venue** Nature Communications (2019) · **Category** single-cell · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1038/s41467-019-10861-2> · `status: complete`

---

## One-liner
An early KPMP methods paper: after comparing 7 kidney tissue preservation/processing methods, it profiles adult human kidney with snDrop-seq (15 individuals, 27 experiments, 47 libraries), yielding 17,659 post-QC nuclei in 30 clusters; it concludes that **O.C.T. cryosections preserved in RNAlater (cryoR)** give the fewest MT transcripts and stress artifacts with >90% success, whereas enzymatic dissociation (dissocPC/TC) induces a FOS/FOSB/DNAJB1 stress signature and an artifact cluster (PC-2).

## Problem
In epithelium- and ECM-rich solid tissues like kidney, enzymatic dissociation causes "activation of gene expression artifacts, poor viability and disproportionate cell-type recovery". The authors want a reproducible single-nucleus pipeline that works on biopsy-scale tissue with parallel histology, and that records **preanalytical procurement/processing parameters** so biological variation can be separated from technical artifacts — then use it to build a molecular "blueprint" of adult kidney and map CKD/hypertension genes to cell types.

## Method
**Procurement**: living patients undergoing partial/total nephrectomy and discarded deceased-donor kidneys at Washington University (KTRC), plus tumour nephrectomies from University of Michigan (KPMP); all from tumour-free regions, histologically confirmed. **Processing** (Fig. 1a): frozen whole tissue; O.C.T.-embedded cryosections (~40 µm, 7 sections) kept frozen (cryoF), in Wisconsin cold-storage solution (cryoW) or in RNAlater (cryoR); fresh tissue partially dissociated with papain/collagenase (dissocPC) or trypsin/collagenase (dissocTC), then stored in RNAlater. GEO additionally labels a whole-tissue "RNAlater 6 Hours" condition. Fluorescent sorting of nuclei impeded snDrop-seq success on kidney (Supp. Fig. 1a). **Sequencing**: snDrop-seq (modified Drop-seq, HiSeq 2500; pipeline at github.com/chensong611/Dropseq_pipeline). **QC**: >400 non-MT transcripts, >400 and <5000 genes, MT genes removed; PAGODA2 gene/UMI-ratio outlier filter, per-batch scaling; top 2000 overdispersed genes → PCA → kNN (k=30, 150 PCs) → infomap; two rounds removing clusters <30 nuclei, plus one 120-nucleus cluster with no markers; UMAP in Seurat 2.3.4. **Analysis**: Wilcoxon DE, SWNE, Monocle2 trajectories, cluster specificity of CKD-eQTL / blood-pressure GWAS genes; average-expression correlation by processing method, individual, source and sex (Supp. Fig. 6).

## Data
15 individuals (WashU 10: PPID 3351, 3395, 3411, 3412, 3414, 3431, 3432, 3434, 3435, 3444; UMich 5: 17-1606, 18-139, 18-142, 18-162, 18-312), 27 experiments / 47 libraries (GEO GSM3448110–GSM3448156), cortex and medulla. 17,659 post-QC nuclei, mean 1,082 UMIs per nucleus ("1082 unique transcripts"). Each GEO library carries experiment, barcode, ppid, region, tissue collection (radical / lap / robotic partial / partial nephrectomy, "donor kidney from MAT", Nephrectomy), tissue processing, sex and source. Public files: a cluster-annotated raw UMI matrix (columns `C{cluster}_NK{library}_{barcode}`, 17,659 columns, MT genes removed) and a 30-cluster annotation table; raw reads in SRA SRP166966. **No biopsies are in this dataset**: "biopsy" appears only as a claim of biopsy-scale compatibility (mean 6 mm³ tissue) and in a comparison with external data GSE114156.

## Key results
- **Processing**: only nuclei from O.C.T. cryosections and from fresh dissociated tissue were snDrop-seq-compatible; cryoR beat cryoW and cryoF; cryoR "showed the fewest expression artifacts while also exhibiting higher experimental success rates (>90%)".
- **MT transcripts as a quality readout**: "we observed the fewest MTs and stress-induced artifacts in cryoR samples compared to cryosections processed differently (cryoW, cryoF) or fresh dissociated samples (dissocPC, dissocTC), while global gene and transcript levels appeared unaffected".
- **Warm ischaemia**: TAL-1 (cluster 12, annotated "Thick ascending limb—surgery") and PT-5 (S3, cluster 7) show MT enrichment "consistent with the nephrectomy procedure-related warm ischemia".
- **Dissociation stress**: DE between methods revealed "a stress response signature (including FOS, FOSB, DNAJB1)" specific to whole-cell dissociative methods and present in most cell types; PC-2 (cluster 17) came mostly from dissocP/T and "likely represented a dissociation artifact".
- **Concordance**: average expression correlated highly across methods, "with cryoW showing the lowest correlation"; within-individual correlation slightly exceeded between-individual; PT-3 (cluster 5, inflammatory genes) came mostly from one individual, possibly disease or procedure. The authors flag clusters 5, 12, 17 as possible processing/collection/patient artifacts.
- **Biology**: 30 clusters; 111/674 CKD-eQTL genes and 56/220 hypertension genes differentially expressed across clusters; POD enriched for CKD loci, MC for hypertension loci; PIEZO2 specific to MC; CFH+ S2 PT and FGA/FGB+ S3 PT populations; medullary IC-A2 expresses KIT and CALCA.

### GEO check: patients with several methods
Computed here by joining library IDs in the public matrix column names to GEO sample annotations (our own count, not reported in the paper):

| PPID | 来源 | 区域 | 处理 → 核数 |
|---|---|---|---|
| 3351 | radical nephrectomy | Cortex | Fresh Frozen (Dry Ice) 23; RNAlater 6 Hours 72 |
| 3395 | radical nephrectomy | Cortex-Medulla | Flash Frozen OCT cryosection 1,193; RNAlater 6 Hours 375; cryosection + RNAlater 314 |
| 3411 | partial nephrectomy | Cortex | cryosection (dry-ice) 383; cryosection + RNAlater 328 |
| 3414 | donor kidney from MAT | Medulla (+ Cortex) | cryosection 1,401; + Wisc 1,533; + RNAlater 3,102 (medulla) / 481 (cortex) |
| 3435 | robotic partial nephrectomy | Medulla | cryosection + Wisc 342; + RNAlater 338; Papain-Collagenase + RNAlater 223 |
| 3431 | lap nephrectomy | Cortex / Medulla | Papain-Collagenase 781 (cortex); cryosection 834 (medulla) — method confounded with region |
| 18-162 | UMich nephrectomy | Cortex | cryosection 386; + RNAlater 604 |
| 18-312 | UMich nephrectomy | Cortex | cryosection 674; + RNAlater 940 |

Single-method individuals: 3432 (Trypsin-Collagenase 1,086), 3434 (Papain-Collagenase + RNAlater 353), 3412 (donor, cryoR 404), 3444 (cryoR 50), 17-1606 (cryoR 886), 18-139 (cryoR 447), 18-142 (cryoR 106). Deceased donors are only 3414 and 3412. GEO uses 13 processing strings split by section count (5/7/10); collapsing them into the paper's 7 methods is our inference, not checked against Supplementary Data 2.

## Contributions
- One of the first systematic comparisons of human kidney preservation/processing on single-nucleus data; set cryoR as the KPMP standard.
- Ties preanalytical parameters, histology and QC metrics (MT fraction, stress genes) together to explain artifact clusters.
- An early 30-population snRNA atlas of adult kidney with cell-type mapping of CKD/hypertension genes.

## Limitations
- Small (17,659 nuclei), low-sensitivity snDrop-seq (~1,082 UMIs/nucleus), sparse immune coverage; medulla from ~3 individuals.
- The method comparison is not balanced: most methods were run on 1–3 individuals and are often confounded with region, individual and experiment date (batch); the main text compares methods by average-expression correlation and DE without per-method effect-size tables.
- MT genes are removed from the public matrix; recomputing MT fraction requires re-aligning SRA raw reads.
- Use as a "normal" reference is limited by donor comorbidities (stated by the authors).

## Relation to our direction
It sits at the **detect** stage as a **negative control / nuisance source**. Topic 1's benchmark asks whether anomaly detectors separate disease from measurement/procurement artifacts; this dataset gives real **same-patient, same-region, different preservation/processing** pairs: 18-162, 18-312, 3411 (cortex cryoF vs cryoR), 3414 (medulla cryoF / cryoW / cryoR), 3435 (medulla cryoW / cryoR / dissocPC), 3395, 3351. Each nucleus's processing method is recoverable from public files (matrix column names carry the library NK#; each GEO library has tissue processing, ppid and region), so it supplies artifact-label ground truth: e.g. fit on cryoR and score how anomalous dissociated nuclei (FOS/FOSB/DNAJB1 stress, PC-2 cluster) and cryoW nuclei look. Warm ischaemia (TAL-1, PT-5) gives a procurement-related artifact axis without per-nucleus labels. Caveats: methods were usually run on different dates/batches, so processing is partly confounded with batch; there are no disease labels (only histology reports in Supp. Data 1), so it covers the artifact side only; the disease side must come from KPMP AKI/CKD (e.g. Lake 2023). snDrop-seq vs 10x is itself another artifact axis.

## Reusable assets
- **Code:** snDrop-seq alignment/counting pipeline https://github.com/chensong611/Dropseq_pipeline; step-by-step wet-lab protocol at https://kpmp.org/resources/
- **Data:** GEO GSE121862 (47 GSMs with per-library metadata; ~20 MB cluster-annotated raw UMI matrix + 30-cluster annotation table); raw reads at SRA SRP166966.
- **Checkpoints:** none.

## Follow-ups
- Get Supplementary Data 1–3 (preanalytical parameters, pathology, per-experiment method and success rate) and Supp. Figs 5/6 (MT fraction and correlation by method); verify the 13 GEO processing strings → 7 methods mapping.
- Re-align from SRA to recover per-nucleus MT fraction as a quality covariate.
- Compare with ischaemia-related altered states in reference tissue in the Lake 2023 KPMP atlas (`lake-kidney-atlas-nature-2023`).

## Cite
```bibtex
@article{Lake_2019, title={A single-nucleus RNA-sequencing pipeline to decipher the molecular anatomy and pathophysiology of human kidneys}, volume={10}, ISSN={2041-1723}, url={http://dx.doi.org/10.1038/s41467-019-10861-2}, DOI={10.1038/s41467-019-10861-2}, number={1}, journal={Nature Communications}, publisher={Springer Science and Business Media LLC}, author={Lake, Blue B. and Chen, Song and Hoshi, Masato and Plongthongkum, Nongluk and Salamon, Diane and Knoten, Amanda and Vijayan, Anitha and Venkatesh, Ramakrishna and Kim, Eric H. and Gao, Derek and Gaut, Joseph and Zhang, Kun and Jain, Sanjay}, year={2019}, month=June }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
