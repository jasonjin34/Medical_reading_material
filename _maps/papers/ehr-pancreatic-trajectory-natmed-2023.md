---
title: A deep learning algorithm to predict risk of pancreatic cancer from disease
  trajectories
aliases:
- Pancreatic cancer trajectories
plans:
- EHR
track: []
year: 2023
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

# A deep learning algorithm to predict risk of pancreatic cancer from disease trajectories

> CancerRiskNet: using only timestamped ICD diagnosis-code sequences (disease trajectories), a Transformer trained on the Danish National Patient Registry (6.2M patients, 23,985 pancreatic cancer cases) predicts pancreatic cancer risk within 3/6/12/36/60 months. 36-month AUROC is 0.879, and still 0.83 when the last 3 months before diagnosis are excluded; transferred as-is to the US Veterans Affairs system it falls to 0.71, recovering to 0.78 after local retraining — showing both that temporal order carries signal and that models do not transfer across health systems for free.

> CancerRiskNet:只用带时间戳的 ICD 诊断码序列(disease trajectory),在丹麦全国患者登记(620 万人,23,985 例胰腺癌)上训练 Transformer,预测 3/6/12/36/60 个月内发生胰腺癌的风险;36 个月 AUROC 0.879,排除确诊前 3 个月数据后仍有 0.83;直接迁移到美国退伍军人系统(US-VA)跌到 0.71,本地重训后回到 0.78 —— 明确证明「时间顺序」有信息量,也明确证明「跨医疗系统不能直接搬模型」。

## Related papers / 相关论文
- [[_maps/papers/ehr-delphi2m-nature-2025|Delphi-2M]] — cites
- [[_maps/papers/ehr-pancreatic-llm-npjdigitmed-2025|LLM-embedding pancreatic risk]] — cites

## Concepts / 概念
- [[_maps/concepts/risk-trajectory|Risk & disease trajectories]]

## Deep-read / 精读

![[papers/ehr-pancreatic-trajectory-natmed-2023/deep-read]]
