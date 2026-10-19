---
title: A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial
  Attacks
aliases:
- Mahalanobis OOD
plans:
- A
track:
- A0
year: 2018
relevance: high
category: anomaly
recommended_by: ''
views:
- plan-a
- overview
tags:
- paper
- plan/A
---

# A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks

> Without retraining a pre-trained softmax classifier, fit class-conditional Gaussians with a tied covariance (GDA/LDA) in its feature space and use the Mahalanobis distance of a test sample to the closest class mean as the confidence score; with input pre-processing and a multi-layer feature ensemble, the same score reached state of the art on both OOD and adversarial-sample detection, was more robust to noisy labels and small training sets, and enabled training-free class-incremental learning.

> 不重新训练任何预训练 softmax 分类器,在它的特征空间里为每一类拟合共享协方差的类条件高斯(即 GDA/LDA),用测试样本到最近类均值的 Mahalanobis 距离作为置信分数;再加上输入预处理与多层特征集成,同一个分数同时在 OOD 检测和对抗样本检测上达到当时最优,对噪声标签和小样本训练集更稳健,还能免训练地做类增量学习。

## Related papers / 相关论文
- [[_maps/papers/cflow-ad-wacv-2022|CFLOW-AD]] — Gaussian prior as special case
- [[_maps/papers/energy-ood-neurips-2020|Energy OOD]] — benchmarked baseline
- [[_maps/papers/generalized-ood-survey-ijcv-2024|Generalized OOD survey]] — distance-based OOD
- [[_maps/papers/msp-ood-iclr-2017|MSP baseline]] — MSP as baseline
- [[_maps/papers/padim-icpr-2020|PaDiM]] — Mahalanobis scoring on pretrained features
- [[_maps/papers/refmap-eval-biorxiv-2025|Reference-mapping QC]] — distance to a reference distribution

## Deep-read / 精读

![[papers/mahalanobis-ood-neurips-2018/deep-read]]
