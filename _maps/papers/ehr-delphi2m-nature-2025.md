---
title: Learning the natural history of human disease with generative transformers
aliases:
- Delphi-2M
plans:
- EHR
track: []
year: 2025
relevance: high
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

# Learning the natural history of human disease with generative transformers

> Delphi-2M turns GPT-2 into a continuous-time, competing-risk generative model of multi-morbidity: given a person's sequence of first ICD-10 diagnoses (1,256 diseases + death) plus sex/BMI/smoking/alcohol, it predicts both what the next event is and when it happens. Trained on 0.4M UK Biobank participants with only 2.2M parameters, it reaches an average age-stratified AUC of ~0.76 across >1,000 diseases, 0.67 on 1.93M Danish individuals with no parameter changes, and can sample synthetic health trajectories up to 20 years ahead.

> Delphi-2M 把 GPT-2 改造成连续时间、多病种竞争风险的生成模型:输入一个人的 ICD-10 首诊序列(1,256 种疾病 + 死亡)及性别/BMI/吸烟/饮酒,同时输出下一事件是什么以及何时发生;在 40 万 UK Biobank 参与者上训练、仅 220 万参数,对 >1,000 种疾病的平均年龄分层 AUC 约 0.76,不改参数迁移到 193 万丹麦人上仍有 0.67,还能采样未来 20 年的合成健康轨迹。

## Related papers / 相关论文
- [[_maps/papers/ehr-apollo-arxiv-2026|APOLLO virtual patient]] — patient-trajectory foundation model
- [[_maps/papers/ehr-comet-natmachintell-2025|COMET (EHR + omics)]] — UK Biobank EHR modelling
- [[_maps/papers/ehr-pancreatic-trajectory-natmed-2023|Pancreatic cancer trajectories]] — cites

## Concepts / 概念
- [[_maps/concepts/virtual-tissue|Virtual tissue / cell]]

## Deep-read / 精读

![[papers/ehr-delphi2m-nature-2025/deep-read]]
