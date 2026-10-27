# 8 · What we are working on

> ⏱ About 20 min · Day 1 · Understand

!!! abstract "After this module you can answer"
    - What does each of the group's research topics ask?
    - Why would running anomaly detection directly on Lake give a false success?
    - Where is the knowledge from modules 1–7 used in each topic?

Modules 1–7 were about the data. This module puts them together as a problem a computer scientist knows, then explains why it is harder than it looks. The full design of each topic is under the **[Research topics](../research/index.md)** tab; this page only gives the shape of the problem.

Numbers on this page come from Lake 2023's GEO label table and the code in module 9, run by us.

## Step 1 · Anomaly detection in one sentence

**Train only on normal samples, give each new sample a score for how abnormal it is, and flag the high scores.**

The classic image example: the model only sees photos of good screws, and at test time it must pick out the scratched ones. It never saw a scratch during training, hence **one-class classification**.

On our data:

| Image anomaly detection | Our data |
|---|---|
| one image | one cell = one row of X |
| photos of good screws | **healthy reference**: `reference`-state cells from healthy donors |
| scratched screw | `altered`-state cell (`state.l1`, module 2) |
| anomaly score | e.g. distance to the nearest healthy cells |
| AUROC on the test set | same, with Lake's labels as the answer |

**AUROC** can be read as: pick one anomalous and one normal cell at random; it is the chance the model scores the anomalous one higher. 0.5 is a coin flip, 1 is perfect.

!!! tip "Computer analogy"
    It is the same as anomaly detection in monitoring: build a baseline from normal logs and alert on anything that drifts from it. The hard part is never computing a distance; it is **whether the baseline is clean, whether an alert is a real problem, and whether the baseline still holds on another machine**. The next three steps are about exactly these three things.

## Step 2 · Trap 1: a high score does not mean it learned disease

Module 2 explained that Lake's `state` labels were assigned by experts reading clusters and marker genes. The largest altered group, degenerative, also has the signs of a low-quality cell. Medians we counted from the GEO label table:

| state.l2 | Genes detected | `percent.mt` |
|---|---|---|
| reference | 1,736 | 0.63 |
| degenerative | 791 | 2.95 |

Fewer than half the genes, about 4.7 times the mitochondrial fraction. This is not a coincidence: Lake 2023 first flagged as possible altered states the clusters with "low genes detected, a high number of mitochondrial transcripts, a high number of endoplasmic-reticulum-associated transcripts, upregulation of injury markers… or enrichment in AKI or CKD samples" (Methods). Part of "few genes, high mito" was built into the labels themselves (modules 2 and 6). So **a "scorer" that only counts genes**, knowing no biology at all, can get a decent AUROC on degenerative cells.

In module 9 we tried the simplest healthy-reference method on proximal tubule (PT) cells (mean distance to the 10 nearest healthy cells), over 5 different donor splits:

| On held-out donors | kNN to healthy reference | Gene count only |
|---|---|---|
| degenerative vs reference | 0.76 – 0.81 | 0.76 – 0.85 |
| adaptive – epi vs reference | 0.53 – 0.71 | 0.30 – 0.34 |

On degenerative cells the kNN score is no better than counting genes, and worse in 4 of the 5 splits. So **a good AUROC on Lake may only show that a method learned "few genes"**: the false success. In the other direction, adaptive cells have more genes, so the gene-count score falls below 0.5. Altered is not one thing; results have to be reported per state.

## Step 3 · Trap 2: anomalies have two sources

Module 6 showed that an abnormal-looking row may be disease or a measurement artifact: doublets, ambient RNA, low-quality cells, dissociation stress. An anomaly detector only answers "is it far from the healthy reference?", **not "why is it far?"**

Lake's labels cover only the disease side; nothing says "this one is an artifact". So on Lake you cannot tell how many of the flagged cells are actually artifacts. Answering that needs data where **the experimental design itself gives the answer**: doublets found by genotype after pooling donors (a lower bound: two cells from the same person stay invisible, module 6), ambient RNA measured through mouse strains, the same donor's tissue measured by several assays (module 6 step 3, module 7).

## Step 4 · Trap 3: new donors or a new assay shift the baseline

In practice you must pick a threshold: above which score do you raise an alarm? A common choice is the 95th percentile on some healthy donors, hoping for 5% false alarms on other healthy donors too.

In module 9 the threshold was set on 3 healthy donors and checked on other, unseen healthy donors: across 5 splits the observed false-alarm rate ranged from **0.9% to 6.3%**, not a steady 5%. That is from changing a few people; we expect a new lab or assay to shift it more (not yet measured; in [mBDRC 2026](../datasets/mbdrc-2026.md) the assay explains far more expression variance than the donor). When training and deployment data differ like this, it is called **domain shift**.

## Step 5 · What each topic asks

These three traps are where the group's topics start. One line per topic; the topic pages have the details:

- **[Topic 1 · A Benchmark for Anomaly Detection in Kidney Single-Cell Omics](../research/anomaly-benchmark.md)**: build a dataset and benchmark with known answers, on both the disease side and the measurement side, to test whether methods can tell the two apart and keep false alarms under control. The three traps map onto its QC-only baseline, its disease-or-measurement task, and its false-alarms-in-a-new-lab task.
- **[Topic 2 · Verifying the Claims of Biomedical Analysis Agents](../research/agent-claims.md)**: when an AI agent analyses data and reports "a new injured cell population", trace whether that claim is backed by code, data or the literature. Trap 2 appears here in another form: the agent may describe doublets or low-quality cells as disease.

## Step 6 · Where the earlier modules come in

| Module | What you need it for |
|---|---|
| 1 · X and obs | split by donor, never by cell; know where labels live |
| 2 · Cells and RNA | an anomaly is a wrong **state** within a cell type, so score per type |
| 3 · Kidney | PT and TAL hold 80% of altered nuclei (our count); know where to look |
| 4 · Patients and tissue | "healthy donor" does not mean "every cell is normal" |
| 5 · Assays | single-nucleus vs single-cell, pooling and genotypes: sources of shift and of ground truth |
| 6 · Artifacts | the second source of anomalies; why QC is part of the question |
| 7 · Datasets | which dataset gives which side of the answer |

## Self-check

??? question "1. A method reaches AUROC 0.8 on Lake's degenerative cells. Does that show it learned to recognise disease?"
    No. A scorer that only counts genes reaches 0.76–0.85 on the same data. Compare against a QC-only baseline at least, and report per state.

??? question "2. Why can't Lake alone show whether a method mistakes artifacts for disease?"
    Lake's labels cover only the disease side; no cell is labelled as an artifact. You need data where the design gives the artifact answer, such as doublets found by genotype after pooling donors (a lower bound: same-person doublets stay hidden).

??? question "3. A threshold set for 5% false alarms on some healthy donors: is it still 5% on other healthy donors?"
    Not necessarily. In module 9, changing a few people moved it between 0.9% and 6.3%; we expect a new lab or assay to move it more (domain shift).

## Terms in this module

| English | 中文 | In one sentence |
|---|---|---|
| [Anomaly detection](glossary.md#anomaly-detection) | 异常检测 | Identifying samples or regions that deviate from a learned notion of 'normal', often by training only on normal data — the first stage of the detect→model→revert pipeline. |
| [Altered state (reference vs altered)](glossary.md#altered-state) | 改变态（参考态 vs 改变态） | Lake 2023's label for cell states that differ from healthy (degenerative, adaptive/repairing, cycling, transitioning), as opposed to 'reference'; assigned by experts after clustering, and also found in healthy donors. |
| [One-class classification](glossary.md#one-class-classification) | 单类分类 | Learning a boundary from examples of a single normal class so that anything falling outside it is flagged as anomalous. |
| [Domain shift](glossary.md#domain-shift) | 域偏移 | A difference between the training and test data distributions, for example due to a different scanner, staining protocol or assay; it typically lowers model performance. |
| [AUROC / AUC (area under the ROC curve)](glossary.md#auroc) | AUROC / AUC(ROC 曲线下面积) | A threshold-independent measure of a classifier's ability to rank positives above negatives; 0.5 is chance and 1.0 is perfect discrimination. |
