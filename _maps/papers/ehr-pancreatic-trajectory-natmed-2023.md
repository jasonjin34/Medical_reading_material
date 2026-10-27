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

> CancerRiskNet: using only timestamped ICD diagnosis-code sequences (disease trajectories), a Transformer trained on the Danish National Patient Registry (DNPR; 6.2M patients and 23,985 pancreatic cancer cases after filtering) predicts whether pancreatic cancer occurs within 3/6/12/36/60 months after the assessment time. The 36-month AUROC is 0.879, and the abstract reports 0.83 when the last 3 months before diagnosis are removed from training. Applied unchanged to the US Veterans Affairs system (US-VA) it drops to 0.710; retrained on VA data it reaches 0.775 (abstract: 0.78) (Abstract; Results).

> CancerRiskNet:只用带时间戳的 ICD 诊断码序列(disease trajectory,疾病轨迹),在丹麦全国患者登记(DNPR;过滤后 620 万人、23,985 例胰腺癌)上训练 Transformer,同时预测评估时刻之后 3/6/12/36/60 个月内是否发生胰腺癌;36 个月窗口 AUROC 0.879,训练时去掉确诊前 3 个月的数据后摘要报告 0.83;不改参数直接用于美国退伍军人系统(US-VA)降到 0.710,在 VA 上重新训练后为 0.775(摘要:0.78)(Abstract;Results)。

## Related papers / 相关论文
- [[_maps/papers/ehr-delphi2m-nature-2025|Delphi-2M]] — cites
- [[_maps/papers/ehr-pancreatic-llm-npjdigitmed-2025|LLM-embedding pancreatic risk]] — cites

## Concepts / 概念
- [[_maps/concepts/risk-trajectory|Risk & disease trajectories]]

## Deep-read / 精读

![[papers/ehr-pancreatic-trajectory-natmed-2023/deep-read]]
