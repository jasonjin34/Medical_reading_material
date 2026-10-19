---
title: Energy-based Out-of-distribution Detection
aliases:
- Energy OOD
plans:
- A
track:
- A0
year: 2020
relevance: medium
category: anomaly
recommended_by: ''
views:
- plan-a
- overview
tags:
- paper
- plan/A
---

# Energy-based Out-of-distribution Detection

> Interpret a classifier's logits as an energy-based model: the free energy E(x) = −T·logsumexp(f(x)/T) is aligned with input density, whereas log-MSP is just the energy of "logits minus the max logit", a biased score. So replace softmax confidence with energy — no training, no hyperparameters — and average FPR95 on CIFAR-10 drops by 18.03%; with auxiliary outlier data, energy-bounded fine-tuning with two squared hinge losses widens the ID/OOD energy gap and beats Outlier Exposure.

> 把分类器的 logit 解释为能量模型:free energy E(x) = −T·logsumexp(f(x)/T) 与输入密度对齐,而 log MSP 只是「logit 减去最大 logit」后的 energy,是一个有偏分数;因此直接用 energy 替代 softmax 置信度——不需训练、无超参——就能在 CIFAR-10 上把平均 FPR95 降低 18.03%;若有辅助离群数据,再用两条 squared hinge 损失做 energy-bounded 微调,拉开 ID 与 OOD 的能量差,超过 Outlier Exposure。

## Related papers / 相关论文
- [[_maps/papers/generalized-ood-survey-ijcv-2024|Generalized OOD survey]] — post-hoc output-based OOD
- [[_maps/papers/histo-nejmai-2024|Clinical-grade histo AD]] — outlier-exposure training
- [[_maps/papers/mahalanobis-ood-neurips-2018|Mahalanobis OOD]] — benchmarked baseline
- [[_maps/papers/msp-ood-iclr-2017|MSP baseline]] — energy replaces softmax score

## Deep-read / 精读

![[papers/energy-ood-neurips-2020/deep-read]]
