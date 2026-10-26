# A Benchmark for Anomaly Detection in Kidney Single-Cell Omics

> Topic 1 · Status: direction and core question decided; data and tasks under discussion; code not started. No results are reported until the code produces them.

## The question

**Is an abnormal-looking cell caused by disease, or by measurement?**

In kidney single-cell and single-nucleus data, some cells do not match healthy tissue. They may be diseased, or their abnormality may come from how they were measured (doublets, ambient RNA, low-quality cells, stress during procurement or dissociation), and the two look alike. Current methods flag both as "anomalous", but no dataset with known answers exists to test whether they can tell the two apart, or how many false alarms they raise. So we cannot say how far findings built on these anomalous cells can be trusted.

## Why it matters

- **Measurement effects have produced false biology.** In human brain single-nucleus data, a population annotated as "immature oligodendrocytes" turned out to be glia contaminated with neuronal ambient RNA, and doublets create "intermediate states" that do not exist in the sample.
- **Kidney data are especially exposed.** In mixed-strain mouse kidney, background contamination was clearly higher in single-nucleus than in matched single-cell samples ([Janssen 2023](../papers/janssen-ambient-noise-genomebiol-2023/index.md): 35% vs 11%, 17% vs 3%), and single-nucleus is the usual assay for kidney biopsies.
- **Disease and measurement signals overlap.** Lake 2023 picked candidate injury states partly by few genes detected and many mitochondrial transcripts, which are also the usual signs of a low-quality cell (our reading); altered states also occur in healthy reference tissue, which the authors attribute possibly to ischaemia during acquisition or normal ageing ([Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md)). From the GEO label table we counted that 26% of nuclei from healthy donors are altered.

## Why it is unsolved

- **Artifact benchmarks have no disease axis.** Doublets and ambient RNA have their own benchmarks (for example the [ambient-removal benchmark](../papers/ambient-rna-bench-biorxiv-2026/index.md)), but each covers one artifact and no disease states.
- **Disease-state detection does not separate artifacts.** Methods that find altered cell states against a healthy reference (for example [Dann 2023](../papers/healthy-ref-natgenet-2023/index.md)) aim at disease states and do not judge whether a flagged cell is an artifact.
- **There is no error control.** Common annotation pipelines give no statistical guarantee; conformal methods can bound the false-alarm rate ([Bates 2023](../papers/conformal-outliers-annstat-2023/index.md), [conformal for single-cell](../papers/conformal-scrna-bioinformatics-2025/index.md)) but have not been tested systematically on kidney data.
- **There is no test bed.** General anomaly-detection benchmarks contain no single-cell or omics expression data, and we found no anomaly-detection benchmark for kidney omics (search, October 2026).

## What we will produce

**The dataset and benchmark are the lead; the method is not.**

1. **A kidney dataset with known answers**: every cell labelled as diseased, measurement-caused or healthy, with a statement of how reliable that label is.
2. **A benchmark**: a few tasks with fixed splits and metrics, comparing a dozen classic anomaly-detection methods and the usual single-cell QC tools.
3. **A reference method**: a healthy reference, a nearest-neighbour score, donor-level calibration with false-alarm control, and a disease-or-measurement call. It gives the benchmark a starting point; it is not the contribution.
4. **Released code**: processing scripts, donor splits, artifact-injection code, labels and benchmark code. Raw data are not redistributed.

## Data

Public kidney data only: human first, mouse only for calibration. What each dataset measures, on how many people, and how to download it is in [Datasets](../datasets/index.md); here we only say what it does in this topic. Grouped by which side of the answer it provides:

| Dataset | Answers | Role |
|---|---|---|
| [Lake 2023](../datasets/lake-2023.md) | disease | healthy reference + disease-state labels |
| [mBDRC 2026](../datasets/mbdrc-2026.md) | measurement | same donors measured by three assays: any "anomaly" between them is a false alarm |
| [Abedini 2024](../datasets/abedini-2024.md) | disease | second lab and cohort: do false alarms stay under control? |
| [Janssen 2023](../datasets/janssen-2023.md) | measurement | mouse; real ambient measured by genotype, used to calibrate injection |
| [Hoeft 2024](../datasets/hoeft-2024.md) | measurement | under discussion: real human-kidney doublets and ambient from pooled donors |
| [Lake 2019](../datasets/lake-2019.md) | measurement | under discussion: same patients, different storage and processing |

**Splits:** by donor, not by cell, so no person appears in both training and testing; the split files ship with the dataset.

## Tasks and ground truth

Ground truth comes in three tiers: **tier 1** is artifacts we inject ourselves, known exactly; **tier 2** is fixed by experimental design, such as one donor measured by several assays; **tier 3** is expert annotation, such as Lake's altered states.

| Task | Question | Ground truth | Metric |
|---|---|---|---|
| T1 | find diseased cells | tier 3 | AUROC, AUPRC |
| T2 | find measurement errors | tier 1 | AUROC, AUPRC |
| T2b | is an assay change flagged as anomalous? | tier 2 | false-alarm rate ≤ α |
| T3 | separate disease from measurement | tiers 1–3 | macro-F1, confusion matrix |
| T4 | do false alarms stay controlled in a new lab? | every call on healthy donors is false | observed rate vs α |

!!! warning "A known trap"
    Using Lake's altered labels directly as disease ground truth is circular: in the single-nucleus data the largest altered group (degenerative) has less than half the genes of normal nuclei and about five times the mitochondrial fraction, so a scorer that looks only at QC metrics could score well. The benchmark therefore needs a QC-only baseline and reports results per state (degenerative / adaptive).

## Open questions

- Should T2b be its own task or part of T4?
- Should Hoeft 2024 and Lake 2019 join the main line?
- How to split Lake's altered cells: those with independent evidence, those called only from QC-like features, and those in healthy donors.
- The number of healthy donors in Abedini 2024 and its licence (sets the size of T4 and whether derived labels can be released).
- The list of methods to compare.

## Reading path

Finish [Onboarding](../onboarding/index.md) first, then read in this order:

1. [Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md): the kidney atlas and its altered states
2. [Janssen 2023](../papers/janssen-ambient-noise-genomebiol-2023/index.md): how large real ambient contamination is
3. [Dann 2023](../papers/healthy-ref-natgenet-2023/index.md): finding altered states against a healthy reference
4. [Bates 2023](../papers/conformal-outliers-annstat-2023/index.md): conformal p-values and false-alarm control
5. [PatchCore](../papers/patchcore-cvpr-2022/index.md): the nearest-neighbour idea from image anomaly detection

After that, see the must-reads in the "Topic 1" view of the [knowledge map](../knowledge-map.md) and the [method × data matrix](../knowledge-map.md), whose dashed cells are the gaps this topic fills.
