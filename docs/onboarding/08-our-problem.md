# 8 · From data to research questions

> ⏱ About 25 min · Day 1 · Understand

!!! abstract "After this module you can answer"
    - What is the group's overall direction, and why is the first step "find the abnormal cells"?
    - Written as a machine-learning problem, what are the input, the output and the metric?
    - Why is this problem harder than it looks?

Modules 1–7 were about the data: where it comes from, what it looks like, where its traps are. This module changes the angle: **given this data, what problem does machine learning solve, and where is it hard?**

## Step 1 · The direction: detect → model → revert

The group's long-term direction has three steps:

1. **Detect**: find the cells that disease or a drug has changed. In the data, that means finding the "abnormal" rows of X.
2. **Model**: turn the tissue into a "virtual tissue" that can be changed and queried on a computer.
3. **Revert**: predict which gene changes would bring abnormal cells back to normal, then test that in the wet lab.

Steps 2 and 3 build on step 1: if we get "which cells are abnormal" wrong, the model and the predicted genes mean nothing. So the group's current work is on step 1, and on **how to tell whether an analysis result can be trusted**. This page covers step 1 only.

## Step 2 · Detection as a machine-learning problem

The natural framing is **anomaly detection**: **train only on normal samples, give each new sample a score for how abnormal it is, and flag the high scores.**

The classic image example: show a model only photos of good screws, then ask it to pick out the scratched ones. It never saw a scratch in training, hence **one-class classification**. Why not train a "normal vs disease" classifier? Disease takes many forms and few of them come with labels; healthy samples are much easier to get.

Mapped onto our data:

| Image anomaly detection | Our data |
|---|---|
| one image | one cell = one row of X |
| photos of good screws | **healthy reference**: `reference`-state cells from healthy donors |
| scratched screw | `altered`-state cell (`state.l1`, module 2) |
| anomaly score | e.g. distance to the nearest healthy cells |
| how good is it? | AUROC, with Lake's labels as the answer |

**AUROC** can be read as: pick one abnormal and one normal cell at random; it is the chance the model scores the abnormal one higher. 0.5 is a coin flip, 1 is perfect.

In real use you also need a **threshold**: above which score do you raise an alarm? A common choice is the 95th percentile on some healthy donors, hoping for 5% false alarms on other healthy donors too.

!!! tip "Computer analogy"
    It is like monitoring: build a baseline from normal logs and alert on anything that drifts from it. The hard part is never computing a distance; it is three things: **is a high score caused by a real problem? what is the alert actually about? does the baseline still hold on another machine?** The next step covers exactly these three.

## Step 3 · Why it is harder than it looks

### Difficulty 1: a high score may not mean it learned disease

Lake's altered labels were assigned by experts reading clusters, partly using quality signals such as "few genes detected, high mitochondrial fraction" (modules 2 and 6). As a result, the largest altered group, degenerative, looks a lot like low-quality cells. Medians we counted from the GEO label table:

| state.l2 | Genes detected | `percent.mt` |
|---|---|---|
| reference | 1,736 | 0.63 |
| degenerative | 791 | 2.95 |

So a **scorer that knows no biology and only counts genes** can reach a decent AUROC on degenerative cells. In module 9 you will run this yourself: a proper kNN method does no better.

**Takeaway:** a high AUROC does not mean a method learned disease. Always compare against a simple QC-only baseline, and report each cell state separately.

### Difficulty 2: an abnormal row has more causes than disease

Module 6 showed that an abnormal-looking row may be disease, a measurement artifact (doublets, ambient RNA), a handling change (dissociation stress) or a batch effect. Anomaly detection only answers "is it far from the healthy reference?", **not "why is it far?"**

Lake labels only the disease side; no cell is labelled as an artifact. So Lake alone cannot tell you how many flagged cells are really artifacts.

**Takeaway:** answering "why is it far?" needs a different kind of data, where **the experimental design itself gives the answer**, such as doublets found by genotype after pooling donors (modules 5.2, 6 and 7).

### Difficulty 3: new donors or a new assay shift the baseline

The threshold is set on one group of healthy donors. On a different group of healthy donors, is the false-alarm rate still 5%? In module 9 you will see that changing just a few people moves it anywhere from **0.9% to 6.3%**. We expect a new lab or assay to shift it more (not yet measured; in [mBDRC 2026](../datasets/mbdrc-2026.md) the assay explains far more expression variance than the donor). When training and deployment data differ like this, it is called **domain shift**.

**Takeaway:** a method that works on one dataset may not work on the next. Test on unseen donors, and ideally on other labs and other assays.

## Step 4 · Where the group's topics start

These three difficulties are the common starting point of the group's current topics. What each topic asks, what it will produce and where it stands are under the **[Research topics](../research/index.md)** tab, not repeated here. Read them with one question in mind: **which difficulty is this topic dealing with?**

## Step 5 · Where the earlier modules come in

| Module | What you need it for |
|---|---|
| 1 · X and obs | split by donor, never by cell; know where labels live |
| 2 · Cells and RNA | an anomaly is a wrong **state** within a cell type, so score per type |
| 3 · Kidney | PT and TAL hold 80% of altered nuclei (our count); know where to look |
| 4 · Patients and tissue | "healthy donor" does not mean "every cell is normal" |
| 5 · Assays | sources of shift, and of known answers (pooling, genotypes) |
| 6 · Artifacts | difficulty 2: the other causes of an abnormal row |
| 7 · Datasets | which dataset gives which kind of answer |

## Self-check

??? question "1. Why does the group start with detection rather than going straight to reversion?"
    Reversion predicts which gene changes bring abnormal cells back to normal, which assumes we know which cells are truly abnormal. Get detection wrong and everything after it is wrong.

??? question "2. A method reaches AUROC 0.8 on Lake's degenerative cells. Does that show it learned to recognise disease?"
    No. Degenerative cells have few genes and a high mitochondrial fraction, so a scorer that only counts genes gets about the same score. Compare against a QC-only baseline and report per state.

??? question "3. A threshold set for 5% false alarms on some healthy donors: is it still 5% on other healthy donors?"
    Not necessarily. Changing a few people can move it between 0.9% and 6.3%; a new lab or assay is expected to move it more (domain shift).

## Terms in this module

| Term | In one sentence |
|---|---|
| [Anomaly detection](glossary.md#anomaly-detection) | Identifying samples or regions that deviate from a learned notion of 'normal', often by training only on normal data — the first stage of the detect→model→revert pipeline. |
| [Altered state (reference vs altered)](glossary.md#altered-state) | Lake 2023's label for cell states that differ from healthy (degenerative, adaptive/repairing, cycling, transitioning), as opposed to 'reference'; assigned by experts after clustering, and also found in healthy donors. |
| [One-class classification](glossary.md#one-class-classification) | Learning a boundary from examples of a single normal class so that anything falling outside it is flagged as anomalous. |
| [Domain shift](glossary.md#domain-shift) | A difference between the training and test data distributions, for example due to a different scanner, staining protocol or assay; it typically lowers model performance. |
| [AUROC / AUC (area under the ROC curve)](glossary.md#auroc) | A threshold-independent measure of a classifier's ability to rank positives above negatives; 0.5 is chance and 1.0 is perfect discrimination. |
