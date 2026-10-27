---
title: A multimodal and temporal foundation model for virtual patient representations
  at healthcare system scale
aliases:
- APOLLO virtual patient
plans:
- EHR
track: []
year: 2026
relevance: medium
category: ehr
recommended_by: core-reading
views:
- reading-list
- ehr
- overview
tags:
- paper
- plan/EHR
---

# A multimodal and temporal foundation model for virtual patient representations at healthcare system scale

> APOLLO (Mahmood lab, Mass General Brigham): a temporal Transformer pretrained by modality-specific masked reconstruction on 7,155,044 patients, ~25.3B medical events and 28 modalities (codes, medications, labs, vitals, flowsheets, clinical text, pathology/blood-smear images) from 17 hospitals, 1992–2025, compressing a whole care history into one "virtual patient" vector. Frozen vector → PCA → linear Cox beats an age–sex baseline on most of 261 prognostic tasks in a 1.43M-patient held-out test set, and supports patient retrieval on 61 cohorts (Abstract; Results).

> APOLLO(Mahmood 组,Mass General Brigham):在 17 家医院 1992–2025 年 7,155,044 名病人、约 253 亿条医疗事件、28 种模态(诊断码、用药、化验、生命体征、flowsheet、临床文本、病理/血涂片图像)上用「模态特定 mask 的掩码重建」预训练一个时间 Transformer,把整个就医史压成一个「虚拟病人」向量;冻结向量 → PCA → 线性 Cox,在 143 万人留出测试集的 261 个预后任务上多数显著超过年龄-性别基线,并支持 61 个队列的病人检索(Abstract;Results)。

## Related papers / 相关论文
- [[_maps/papers/ehr-comet-natmachintell-2025|COMET (EHR + omics)]] — EHR pretraining → transfer
- [[_maps/papers/ehr-delphi2m-nature-2025|Delphi-2M]] — patient-trajectory foundation model
- [[_maps/papers/medagentbench-nejmai-2025|MedAgentBench]] — EHR environment

## Concepts / 概念
- [[_maps/concepts/foundation-model|Foundation models]]
- [[_maps/concepts/risk-trajectory|Risk & disease trajectories]]
- [[_maps/concepts/virtual-tissue|Virtual tissue / cell]]

## Deep-read / 精读

![[papers/ehr-apollo-arxiv-2026/deep-read]]
