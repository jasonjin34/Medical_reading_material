---
title: Robust annotation and discovery of novel cell types in single-cell ATAC-seq
  data through cross-modal reference alignment
aliases:
- Novel types in scATAC
plans:
- A
track:
- A3
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

# Robust annotation and discovery of novel cell types in single-cell ATAC-seq data through cross-modal reference alignment

> CARA is a cross-modal Bayesian framework that transfers cell-type knowledge from an scRNA-seq reference to scATAC-seq: pretraining on scRNA, semi-supervised learning on the target scATAC, plus distribution alignment, dynamic class weighting and novel-type detection — jointly annotating, batch-correcting and flagging populations absent from the reference (novel, rare or aberrant).

> CARA 是一个跨模态贝叶斯框架,把 scRNA-seq 参照中的细胞类型知识迁移到 scATAC-seq:在 scRNA 上预训练,在目标 scATAC 上做半监督学习,配合分布对齐、动态类别加权和新细胞类型检测,同时完成注释、批次校正和识别参照中不存在的(新的、稀有的或异常的)细胞群。

## Related papers / 相关论文
- [[_maps/papers/conformal-scrna-bioinformatics-2025|Conformal annotation]] — out-of-reference cell types
- [[_maps/papers/multimodal-integration-bench-natmethods-2025|Integration benchmark]] — RNA–ATAC cross-modal

## Concepts / 概念
- [[_maps/concepts/batch-effect|Batch effects]]
- [[_maps/concepts/conformal|Conformal guarantees]]
- [[_maps/concepts/cross-modal|Cross-modal agreement]]

## Deep-read / 精读

![[papers/scatac-novel-genomeres-2026/deep-read]]
