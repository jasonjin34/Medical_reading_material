---
title: Benchmarking computational decontamination of ambient RNA
aliases:
- Ambient-RNA benchmark
plans:
- A
track:
- A2
year: 2026
relevance: medium
category: single-cell
recommended_by: ''
views:
- plan-a
- overview
tags:
- paper
- plan/A
---

# Benchmarking computational decontamination of ambient RNA

> An independent benchmark using simulations, species-mixing experiments of three complexities, a mouse-kidney strain (genotype) mixing experiment and contamination-free negative controls to evaluate 7 ambient-RNA decontamination methods (CellBender, DecontX, FastCAR, scAR, scCDC, SoupX, CellClear) on how much ambient RNA they remove, how much endogenous RNA they keep, and how they change downstream interpretation; no method wins everywhere — CellBender, DecontX (full mode) or SoupX (reduced mode) are recommended — and default decontamination of clean data risks over-correction.

> 一个独立基准,用模拟数据、三种复杂度的物种混合实验、小鼠肾脏品系(基因型)混合实验和无污染负对照,评测 7 种 ambient RNA 去污染方法(CellBender、DecontX、FastCAR、scAR、scCDC、SoupX、CellClear)「去掉多少外源 RNA、保留多少内源 RNA、对下游解读有何影响」;结论是没有通吃的方法,推荐 CellBender、DecontX(full 模式)或 SoupX(reduced 模式),并警告在无污染数据上默认去污染会过度校正。

## Related papers / 相关论文
- [[_maps/papers/xenium-split-natmethods-2026|Xenium contamination (SPLIT)]] — wrong-cell signal contamination

## Concepts / 概念
- [[_maps/concepts/ambient-rna|Ambient RNA]]
- [[_maps/concepts/spillover|Signal spillover]]

## Deep-read / 精读

![[papers/ambient-rna-bench-biorxiv-2026/deep-read]]
