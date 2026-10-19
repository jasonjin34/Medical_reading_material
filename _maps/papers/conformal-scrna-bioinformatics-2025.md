---
title: Conformal inference for reliable single cell RNA-seq annotation
aliases:
- Conformal annotation
plans:
- A
- B
track:
- A3
- B4
year: 2025
relevance: medium
category: single-cell
recommended_by: ''
views:
- plan-a
- plan-b
- bridge
- overview
tags:
- paper
- plan/A
- plan/B
---

# Conformal inference for reliable single cell RNA-seq annotation

> Adds distribution-free statistical guarantees to automatic scRNA-seq annotation with conformal prediction: an autoencoder + conformal p-values first detects cell types absent from the reference (OOD) with false-positive rate ≤ α₀; the remaining cells get prediction sets with coverage guarantees (standard / classwise / cluster Mondrian taxonomies; APS / RAPS / THR non-conformity scores), where set size is the uncertainty. Departures of the conformal p-values from uniformity also diagnose broken reference–query exchangeability.

> 用 conformal prediction 给 scRNA-seq 自动注释加上分布无关的统计保证:先用自编码器 + conformal p 值检测参照中不存在的细胞类型(OOD),控制假阳性率 ≤ α₀;再对剩下的细胞输出带覆盖保证的预测集合(标准 / classwise / cluster 三种 Mondrian 分类方式,APS / RAPS / THR 三种非一致性分数),集合大小即不确定性;conformal p 值分布偏离均匀还可以用来诊断参照与 query 之间的可交换性是否被破坏。

## Related papers / 相关论文
- [[_maps/papers/citation-faithfulness-arxiv-2026|Citation faithfulness guard]] — conformal guarantees
- [[_maps/papers/conformal-outliers-annstat-2023|Conformal p-values]] — cites
- [[_maps/papers/refmap-eval-biorxiv-2025|Reference-mapping QC]] — reference–query shift
- [[_maps/papers/scatac-novel-genomeres-2026|Novel types in scATAC]] — out-of-reference cell types

## Concepts / 概念
- [[_maps/concepts/conformal|Conformal guarantees]]
- [[_maps/concepts/ood-detection|OOD / novelty detection]]

## Deep-read / 精读

![[papers/conformal-scrna-bioinformatics-2025/deep-read]]
