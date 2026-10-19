---
title: A visual–omics foundation model to bridge histopathology with spatial transcriptomics
aliases:
- Loki / OmiCLIP
plans:
- A
track:
- A4
year: 2025
relevance: high
category: spatial
recommended_by: ''
views:
- plan-a
- overview
tags:
- paper
- plan/A
---

# A visual–omics foundation model to bridge histopathology with spatial transcriptomics

> OmiCLIP writes each Visium spot's transcriptome as a "sentence" of gene symbols ranked by expression and contrastively aligns it with the matching H&E patch in a CLIP/CoCa setup (ST-bank: 2.2M pairs, 1,007 samples, 32 organs); the Loki platform built on top offers five modules — tissue alignment, tissue annotation, cell-type decomposition, image↔transcriptome retrieval and ST expression prediction from H&E.

> OmiCLIP 把每个 Visium spot 的转录组写成「按表达量排序的基因符号句子」,与对应 H&E patch 做 CLIP/CoCa 式对比学习(ST-bank:2.2M 对、1,007 个样本、32 个器官);在此之上的 Loki 平台提供五个模块 —— 组织对齐、组织注释、细胞类型分解、图像↔转录组检索、从 H&E 预测 ST 表达。

## Related papers / 相关论文
- [[_maps/papers/he2expr-bench-natcommun-2025|H&E→expression benchmark]] — H&E→expression
- [[_maps/papers/hest1k-2024|HEST-1k]] — histology↔ST pairs
- [[_maps/papers/virtual-tissue-2501|Virtual tissues (spatial proteomics)]] — cites

## Concepts / 概念
- [[_maps/concepts/he-to-expression|H&E → expression prediction]]
- [[_maps/concepts/zero-shot|Zero-shot use]]

## Deep-read / 精读

![[papers/loki-omiclip-natmethods-2025/deep-read]]
