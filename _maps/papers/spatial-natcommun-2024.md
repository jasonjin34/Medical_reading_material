---
title: Detecting anomalous anatomic regions in spatial transcriptomics with STANDS
aliases:
- STANDS
plans:
- A
track:
- A3
year: 2024
relevance: medium
category: spatial
recommended_by: core-reading
views:
- plan-a
- reading-list
- overview
tags:
- paper
- plan/A
---

# Detecting anomalous anatomic regions in spatial transcriptomics with STANDS

> STANDS is a GAN-based multi-sample spatial-transcriptomics (ST) framework: it learns to reconstruct normal spots from a "normal" reference section, flags poorly reconstructed spots in target sections as anomalous tissue domains (ATDs), aligns several samples into the reference space, and clusters the anomalies into subtypes that are shared across samples or sample-specific — without any predefined anomaly marker genes.

> STANDS 是一套基于 GAN 的多样本空间转录组(ST)框架:先在"正常"参考切片上学会重建正常 spot,把重建得差的 spot 标为异常组织域(ATD);再把多个样本对齐到参考空间;最后把异常聚成"跨样本共享 / 样本特有"的亚型——全程不需要预先给出异常 marker 基因。

## Related papers / 相关论文
- [[_maps/papers/anogan-ipmi-2017|AnoGAN]] — GAN on normal data; reconstruction-residual score
- [[_maps/papers/hest1k-2024|HEST-1k]] — spatial-omics data
- [[_maps/papers/meatrd-aaai-2025|MEATRD]] — cites
- [[_maps/papers/ovrlpy-natbiotech-2026|ovrlpy]] — technical vs anatomic anomaly map
- [[_maps/papers/patchcore-cvpr-2022|PatchCore]] — memory bank of normal features
- [[_maps/papers/sardine-bioinformatics-2025|Sardine]] — cites
- [[_maps/papers/uni2-h-model|UNI2-h]] — FM backbone → anomaly det.

## Concepts / 概念
- [[_maps/concepts/anomalous-region|Anomalous tissue regions]]
- [[_maps/concepts/batch-effect|Batch effects]]
- [[_maps/concepts/cross-modal|Cross-modal agreement]]

## Deep-read / 精读

![[papers/spatial-natcommun-2024/deep-read]]
