# Cell-type-specific damage scores reveal kidney and liver disease trajectories in single-cell and spatial transcriptomics

> **Bibkey** `Padvitski_2026` · **Venue** Cell Genomics (2026) · **Category** single-cell · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1016/j.xgen.2026.101337> · `status: abstract-only`

---

## One-liner
A general framework of **cell-type-specific continuous damage scores** that place individual cells on a health-to-damage axis: 42 genes with consistent changes across many mouse disease models are scored with AUCell, giving the podocyte damage score PDS (CKD/FSGS) and hepatocyte damage score HDS (MASLD/NASH); across mouse and human scRNA, snRNA, spatial transcriptomics, proteomics, histology and clinical data they detect disease-associated damage, align different disease models, and resolve damage variation even among unperturbed control cells.

## Problem
Degenerative diseases progress through gradual cell-intrinsic damage, but bulk transcriptomics averages it away and discrete cell-state annotation (e.g. "injured/altered states") chops a continuous process into categories, making it hard to resolve individual cells' gradual decline in vivo. A transferable continuous damage measure, comparable across datasets and species, is needed.

## Method
(From preprint v2.) **Gene selection**: rank genes by differential-expression p value within each disease model, average ranks across models, filter for expression in the target cell type and consistent direction in ≥75% of studies, take the top n as damage markers. **Signatures**: PDS 42 genes (39 down, 3 up), HDS 42 genes (30 down, 12 up). **Scoring**: AUCell rank-based scoring combining up- and down-regulated genes by direction, at single-cell resolution. **Validation**: leave-one-model-out (drop all samples of one model, rebuild the signature, test on the held-out model); robustness (30–200 marker genes changes little; shuffling up to 70% of input studies still separates disease from control). Downstream: PDS-based pathway fingerprinting, comparisons across models at matched damage, a podocyte transcriptional regulatory network from ATAC data, GWAS enrichment.

## Data
(From preprint v2.) **Mouse**: 37 podocyte datasets over 9 podocytopathy models (e.g. Nphs2mut, Cd2apko, Pdss2mut, doxorubicin, NTN, Btbr ob/ob diabetic, Wt1 ko/wt); ~250 hepatocyte samples over 13 liver models (CCl4, DDC, ethanol, streptozotocin, NAFLD …); Slide-seqV2 (Btbr ob/ob, GSE190094) and Visium (NAFLD mouse). **Human**: KPMP snRNA-seq (n = 37 with clinical data), scRNA-seq (n = 17), one FSGS Visium core; newly generated Xenium (8 minimal-change/FSGS patients, 238 glomeruli); NEPTUNE urine podocytes; liver GSE189600 (3 healthy / 3 NASH), GSE210077 (3 healthy / 3 fibrosis), Visium steatosis from 2 patients.

## Key results
- **Published abstract**: PDS links podocyte injury and FSGS progression to **circadian gene-expression disruption**; HDS identifies a **damage threshold** in MASLD/NASH beyond which hepatocytes adopt senescent, metabolically dysfunctional states.
- (Preprint) **Function**: PDS vs albuminuria Spearman ρ = 0.45 (p = 0.017) across 12 mouse bulk glomerular studies and ρ = 0.78 (p = 1.8 × 10⁻⁶) in new snRNA-seq; in KPMP only diabetic status and PDS correlated with ACR; in NEPTUNE urine podocytes PDS tracks UPCR.
- (Preprint) **Spatial/morphology**: in 238 human Xenium glomeruli PDS anti-correlates with podocyte density and correlates with slit-diaphragm length (p < 0.05); glomerular PDS differences are significant in mouse spatial data.
- (Preprint) **Controls carry damage too**: controls have lower mean damage but always contain a small fraction of high-damage cells; PDS can "align" damage states across models as albuminuria does clinically. On proteomics, PDS/HDS separate disease from control without exception.
- (Preprint) **Genetics**: 8/42 PDS genes are kidney-disease GWAS genes (gene-body enrichment p = 0.031; with flanks p = 0.002); 10/42 HDS genes for liver traits (p = 0.1, n.s.).

## Contributions
- Defines damage as a cross-model consensus **continuous, cell-type-specific** single-cell score rather than a discrete state label.
- Leave-one-model-out validation and study-shuffling robustness show generalization to unseen disease models.
- One score spans sc/sn/spatial/proteomic/histology/clinical modalities and mouse→human, enabling comparisons across aetiologies at matched damage.

## Limitations
- Signatures derive from mouse models; some human validation cohorts are tiny (liver 3 vs 3).
- PDS baselines differ slightly between sc and sn data (attributed to tissue-digestion damage) — the score is sensitive to **technical/processing artifacts**.
- Hepatocyte pseudotime is dominated by zonation, potentially masking damage.
- Covers only podocytes and hepatocytes; a supervised "known damage direction" signature that cannot discover anomalies outside it.
- Published full text not read here; details need verification.

## Relation to our direction
This is **Topic 1's** most direct "known-direction" counterpart: our anomaly detection is unsupervised "how far from the healthy reference", whereas PDS is supervised "how far along the consensus damage direction". Combining them is valuable: (1) **baseline and weak label** — on the kidney samples to be tested and on KPMP/Lake data, a detector's podocyte anomaly score should correlate with PDS; high-anomaly cells that do *not* correlate are either new anomaly types or artifacts — exactly what cross-modal agreement (snATAC, Xenium podocyte density, H&E morphology) must adjudicate; (2) its report that sc vs sn baselines differ due to digestion damage, and that controls always contain a few high-damage cells, matches Lake 2023's "altered states in reference tissue" — the **procurement/dissociation artifact vs true damage** distinction KidneyAnomalyBench must test; (3) its Xenium validation (PDS vs podocyte density and slit-diaphragm length) shows **cross-modal alignment of a transcriptomic score with morphological readouts**, a validation protocol to reuse. For **detect → model → revert**: the continuous damage axis is a natural "state coordinate" in a virtual tissue, and reverting can be phrased as "bring PDS back into the control distribution"; the published HDS threshold (beyond which cells turn senescent) suggests a **reversibility window**, crucial for timing revert interventions. For **Topic 2**: it is a simple, reproducible tool (signature + AUCell) an agent can call — good for testing rerun stability and whether the agent correctly states its scope (podocytes/hepatocytes only, mouse-derived).

## Reusable assets
- **Signatures:** PDS / HDS, 42 genes each (supplementary tables; obtain from the published version).
- **Code (GitHub of co-author Paula Unger Avila; correspondence to the paper not verified):** HDS script repositories.
<https://github.com/PauUng/HepatocyteDamageScore> · <https://github.com/PauUng/hepatocyte-damage-score-paper>
- **Data:** public KPMP, GSE190094 (Slide-seqV2), GSE189600, GSE210077; new Xenium data per the published data statement.
- **Preprint:**
<https://doi.org/10.1101/2025.02.20.639269>

## Follow-ups
- Get the published PDF to verify numbers, the circadian mechanism and HDS threshold, and code/data availability.
- Extend the PDS idea to PT/TAL (cf. Lake 2023 aPT/aTAL and CellSpectra pathway-coordination scores).
- Compare supervised damage scores with unsupervised reference distance on kidney Xenium data.

## Cite
```bibtex
@article{Padvitski_2026, title={Cell-type-specific damage scores reveal kidney and liver disease trajectories in single-cell and spatial transcriptomics}, volume={6}, ISSN={2666-979X}, url={http://dx.doi.org/10.1016/j.xgen.2026.101337}, DOI={10.1016/j.xgen.2026.101337}, number={10}, journal={Cell Genomics}, publisher={Elsevier BV}, author={Padvitski, Tsimafei and Unger Avila, Paula and Chen, He and Özel, Cem and Braun, Fabian and Kroll, Marie-Kristin and Vossen, Christian and Wienand, Peter and Butt, Linus and Unnersjö-Jess, David and Schumacher, Anna-Lena and Folz-Donahue, Kat and Göbel, Heike and Kuppe, Christoph and Müller, Roman-Ulrich and Westermark, Pål Olof and Brinkkötter, Paul Thomas and Schermer, Bernhard and Benzing, Thomas and Wunderlich, Frank Thomas and Kann, Martin and Beyer, Andreas}, year={2026}, month=Oct, pages={101337} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
