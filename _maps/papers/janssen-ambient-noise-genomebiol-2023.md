---
title: The effect of background noise and its removal on the analysis of single-cell
  expression data
aliases:
- Ambient truth, mouse kidney (Janssen)
plans:
- A
track:
- A2
year: 2023
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

# The effect of background noise and its removal on the analysis of single-cell expression data

> Kidney cells from two mouse subspecies (*M. m. castaneus* CAST/EiJ and *M. m. domesticus* C57BL/6J and 129S1/SvImJ) are pooled in one 10x channel so that subspecies-diagnostic homozygous SNPs separate endogenous from foreign molecules, giving a genotype-based ground truth for the per-cell background-noise fraction ρ_cell. Background noise varies widely between replicates and cells (3–35% of UMIs on average), comes mostly from ambient RNA rather than barcode swapping, and — used as ground truth to benchmark CellBender / DecontX / SoupX — CellBender gives the most precise estimates and the biggest gain for marker genes, while clustering and classification are fairly robust to background noise.

> 把来自两个小鼠亚种(*M. m. castaneus* CAST/EiJ 与 *M. m. domesticus* C57BL/6J、129S1/SvImJ)的肾脏细胞混在同一个 10x 通道里,用亚种间纯合 SNP 区分「本细胞的分子」和「外来分子」,从而得到每个细胞背景噪声比例 ρ_cell 的基因型真值;发现背景噪声在重复间、细胞间差异很大(平均 3–35% 的 UMI),主要来自 ambient RNA 而非 barcode swapping,并以此真值评测 CellBender / DecontX / SoupX —— CellBender 估计最准、对 marker 基因改善最大,而聚类与分类对背景噪声相当稳健。

## Related papers / 相关论文
- [[_maps/papers/denisenko-dissociation-bias-genomebiol-2020|Dissociation bias, mouse kidney]] — cites

## Concepts / 概念
- [[_maps/concepts/ambient-rna|Ambient RNA]]

## Deep-read / 精读

![[papers/janssen-ambient-noise-genomebiol-2023/deep-read]]
