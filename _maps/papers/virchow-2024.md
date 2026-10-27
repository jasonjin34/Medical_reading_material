---
title: A foundation model for clinical-grade computational pathology and rare cancers
  detection
aliases:
- Virchow
plans:
- A
track:
- A5
year: 2024
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

# A foundation model for clinical-grade computational pathology and rare cancers detection

> Virchow is a 632M-parameter ViT-H/14 pathology foundation model trained by Paige and Microsoft Research with DINOv2 self-supervision on ~1.5M H&E whole-slide images (WSIs) from MSKCC; an aggregator trained on its frozen tile embeddings performs pan-cancer detection across 16 cancer types with specimen-level AUC 0.950, and 0.937 on the 7 rare cancers (Abstract; Fig. 2b–c).

> Virchow 是 Paige 与 Microsoft Research 用 DINOv2 自监督在 MSKCC 约 150 万张 H&E 全切片(WSI)上训练的 632M 参数 ViT-H/14 病理基础模型;在它的冻结 tile 嵌入上训练一个聚合器,就能做跨 16 种癌的"泛癌检测",标本级 AUC 0.950,其中 7 种罕见癌 AUC 0.937(Abstract;Fig. 2b–c)。

## Related papers / 相关论文
- [[_maps/papers/hest1k-2024|HEST-1k]] — cites
- [[_maps/papers/histo-nejmai-2024|Clinical-grade histo AD]] — FM backbone → anomaly det.
- [[_maps/papers/pathbench-natcommun-2026|Pathology FM benchmark]] — pathology FM benchmark
- [[_maps/papers/uni2-h-model|UNI2-h]] — pathology FM

## Concepts / 概念
- [[_maps/concepts/foundation-model|Foundation models]]

## Deep-read / 精读

![[papers/virchow-2024/deep-read]]
