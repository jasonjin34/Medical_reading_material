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
recommended_by: sikander
views:
- sikander
- ehr
- overview
tags:
- paper
- plan/EHR
---

# A multimodal and temporal foundation model for virtual patient representations at healthcare system scale

> APOLLO (Mahmood lab): a multimodal temporal Transformer pretrained with masked modelling on 33 years of records from 17 Mass General Brigham hospitals — 7.2M patients, 25.3B medical events, 28 modalities (structured codes, labs, vitals, medications, note and report text, pathology/blood-smear images) — compressing a whole care journey into a "virtual patient" embedding. Frozen embeddings with a linear Cox head substantially beat an age–sex baseline across 261 prognostic and 61 retrieval tasks on a 1.4M-patient test set.

> APOLLO(Mahmood 组):在 Mass General Brigham 17 家医院 33 年、720 万病人、253 亿条医疗事件、28 种模态(结构化码、化验、生命体征、用药、病程记录与报告文本、病理/血涂片图像)上做掩码预训练的多模态时间 Transformer,把整个就医历程压成一个「虚拟病人」向量;冻结向量 + 线性 Cox 头在 140 万人测试集的 261 个预后任务和 61 个检索任务上大幅超过年龄-性别基线。

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
