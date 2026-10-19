---
title: A Baseline for Detecting Misclassified and Out-of-Distribution Examples in
  Neural Networks
aliases:
- MSP baseline
plans:
- A
track:
- A0
year: 2017
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

# A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks

> The founding paper of OOD detection: a trained classifier's maximum softmax probability (MSP) is not a usable confidence on its own (an MNIST classifier assigns 91% "confidence" to Gaussian noise), but correctly classified examples have statistically higher MSP than misclassified and out-of-distribution ones, so thresholding MSP detects errors and OOD inputs across vision, NLP and speech. The authors also define standard tasks and metrics (AUROC plus two AUPRs) and show with an "auxiliary decoder + abnormality module" that the baseline can be beaten.

> OOD 检测领域的起点论文:训练好的分类器给出的最大 softmax 概率(MSP)本身不能当作置信度(MNIST 分类器对高斯噪声也给出 91% 的「置信度」),但正确分类样本的 MSP 统计上高于错分样本和分布外样本,所以把 MSP 当阈值分数,就能在视觉、NLP、语音任务上检出错误和 OOD;作者同时定义了一套标准任务与指标(AUROC + 两种 AUPR),并用一个「辅助解码器 + 异常模块」说明这个基线可以被超越。

## Related papers / 相关论文
- [[_maps/papers/energy-ood-neurips-2020|Energy OOD]] — energy replaces softmax score
- [[_maps/papers/generalized-ood-survey-ijcv-2024|Generalized OOD survey]] — baseline in OpenOOD
- [[_maps/papers/mahalanobis-ood-neurips-2018|Mahalanobis OOD]] — MSP as baseline

## Deep-read / 精读

![[papers/msp-ood-iclr-2017/deep-read]]
