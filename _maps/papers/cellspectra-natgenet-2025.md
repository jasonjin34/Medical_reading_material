---
title: Analysis of individual patient pathway coordination in a cross-species single-cell
  kidney atlas
aliases:
- CellSpectra
plans:
- A
track:
- A1
year: 2025
relevance: high
category: single-cell
recommended_by: ''
views:
- plan-a
- overview
tags:
- paper
- plan/A
---

# Analysis of individual patient pathway coordination in a cross-species single-cell kidney atlas

> Two things: (1) SISKA 1.0 — a cross-species single-nucleus kidney atlas (human, mouse, rat; >1M cells, >140 samples) with 21 main cell types and ~80 cross-species-conserved cell states; (2) CellSpectra — a single-sample statistic: for each cell type × pathway, the first SVD axis of the reference samples' pseudobulk matrix defines the "coordination pattern"; a query sample is regressed onto it, and lowered R² plus a χ² test flags loss of coordination in that sample. This powers a patient-level single-cell functional profiling report, rodent-model selection for a patient, and — in a folic-acid kidney-injury model — the CellSpectra-nominated TNF pathway was targeted with etanercept, improving kidney function.

> 两件事:(1) SISKA 1.0 —— 人、小鼠、大鼠 > 100 万细胞、> 140 个样本的跨物种单细胞(snRNA)肾脏图谱,21 个主要细胞类型、近 80 个跨物种保守的细胞状态;(2) CellSpectra —— 一个单样本统计工具:对每个细胞类型 × 通路,用参照样本伪 bulk 矩阵的 SVD 第一主轴作为"协调模式",把待测样本回归上去,R² 降低 + χ² 检验即判为该样本该通路"协调性丢失";据此生成患者级单细胞功能画像报告、为患者选择最匹配的啮齿类模型,并在叶酸肾损伤模型中由 CellSpectra 提名的 TNF 通路用 etanercept 干预改善了肾功能。

## Related papers / 相关论文
- [[_maps/papers/abedini-kidney-atlas-natgenet-2024|Kidney atlas (Abedini 2024)]] — cites
- [[_maps/papers/damage-scores-cellgenomics-2026|Damage scores]] — per-sample injury scoring
- [[_maps/papers/lake-kidney-atlas-nature-2023|Kidney atlas (Lake 2023)]] — cites

## Concepts / 概念
- [[_maps/concepts/cross-modal|Cross-modal agreement]]
- [[_maps/concepts/damage-score|Damage score]]

## Deep-read / 精读

![[papers/cellspectra-natgenet-2025/deep-read]]
