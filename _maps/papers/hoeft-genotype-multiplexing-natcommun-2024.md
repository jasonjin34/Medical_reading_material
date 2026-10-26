---
title: Label-free single-cell RNA multiplexing leveraging genetic variability
aliases:
- SNP multiplexing (Hoeft)
plans:
- A
track:
- A2
year: 2024
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

# Label-free single-cell RNA multiplexing leveraging genetic variability

> Hayat/Kramann lab present SoupLadle: reference-free SNP deconvolution of pooled sc/snRNA-seq with Souporcell, then re-assignment of each genotype cluster to a patient by Hamming distance + Kuhn-Munkres matching against per-patient bulkRNA-seq SNPs; it gives the highest recall and least cell-type bias on PBMC, two heart snRNA cohorts and 4 frozen human kidney biopsies (snRNA, 11,490 nuclei).

> Hayat/Kramann 组提出 SoupLadle:先用 Souporcell 按 SNP 对 pooled sc/snRNA-seq 做无参考 deconvolution,再用每位患者的 bulkRNA-seq SNP 通过 Hamming 距离 + Kuhn-Munkres 匹配把 genotype cluster 还原到患者;在 PBMC、两个心脏 snRNA 队列和 4 例冷冻人肾活检 snRNA(11,490 nuclei)上召回率最高、cell-type bias 最小。

## Concepts / 概念
- [[_maps/concepts/doublet|Doublets]]

## Deep-read / 精读

![[papers/hoeft-genotype-multiplexing-natcommun-2024/deep-read]]
