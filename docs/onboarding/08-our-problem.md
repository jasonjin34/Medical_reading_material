# 8 · What we are working on

> ⏱ About 20 min · Day 1 · Understand

!!! abstract "After this module you can answer"
    - What does each of the group's research topics ask?
    - Why would running anomaly detection directly on Lake give a false success?
    - Where is the knowledge from modules 1–7 used in each topic?

## Content

!!! note "In progress"
    The text of this module is being written.

## Terms in this module

| English | 中文 | In one sentence |
|---|---|---|
| [Anomaly detection](glossary.md#anomaly-detection) | 异常检测 | Identifying samples or regions that deviate from a learned notion of 'normal', often by training only on normal data — the first stage of the detect→model→revert pipeline. |
| [Altered state (reference vs altered)](glossary.md#altered-state) | 改变态（参考态 vs 改变态） | Lake 2023's label for cell states that differ from healthy (degenerative, adaptive/repairing, cycling, transitioning), as opposed to 'reference'; assigned by experts after clustering, and also found in healthy donors. |
| [One-class classification](glossary.md#one-class-classification) | 单类分类 | Learning a boundary from examples of a single normal class so that anything falling outside it is flagged as anomalous. |
| [Domain shift](glossary.md#domain-shift) | 域偏移 | A drop in model performance when test data differs from training data, for example due to a different scanner or staining protocol. |
| [AUROC / AUC (area under the ROC curve)](glossary.md#auroc) | AUROC / AUC(ROC 曲线下面积) | A threshold-independent measure of a classifier's ability to rank positives above negatives; 0.5 is chance and 1.0 is perfect discrimination. |
