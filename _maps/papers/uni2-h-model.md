---
title: MahmoodLab/UNI2-h
aliases:
- UNI2-h
plans:
- A
track:
- A5
year: null
relevance: medium
category: foundation
recommended_by: sikander
views:
- plan-a
- sikander
- overview
tags:
- paper
- plan/A
---

# MahmoodLab/UNI2-h

> UNI2-h is Mahmood Lab's histopathology foundation model: a ViT-H/14 backbone self-supervised with DINOv2 on 200M+ H&E/IHC tiles, turning a 224×224 tissue patch into a 1536-dim embedding usable as a frozen feature extractor for downstream classification, retrieval and MIL.

> UNI2-h 是 Mahmood Lab 发布的病理学视觉基础模型:一个用 DINOv2 自监督、在 3 亿+ H&E/IHC 图块上预训练的 ViT-H/14 backbone,把 224×224 组织学 patch 编码成 1536 维特征,可直接作为下游分类/检索/MIL 的冻结特征提取器。

## Related papers / 相关论文
- [[_maps/papers/fm-arxiv-2604|Generative histopathology FM]] — pathology FM
- [[_maps/papers/kidney-ssl-histology-scirep-2025|Kidney histology SSL]] — UNI embeddings comparison
- [[_maps/papers/pathbench-natcommun-2026|Pathology FM benchmark]] — pathology FM benchmark
- [[_maps/papers/spatial-natcommun-2024|STANDS]] — FM backbone → anomaly det.
- [[_maps/papers/virchow-2024|Virchow]] — pathology FM

## Deep-read / 精读

![[papers/uni2-h-model/deep-read]]
