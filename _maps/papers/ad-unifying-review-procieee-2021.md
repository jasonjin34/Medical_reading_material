---
title: A Unifying Review of Deep and Shallow Anomaly Detection
aliases:
- Unifying AD review
plans:
- A
track:
- A0
year: 2021
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

# A Unifying Review of Deep and Shallow Anomaly Detection

> This review (TU Berlin / Kloft / Dietterich / Müller groups) unifies anomaly detection under a probabilistic definition (an anomaly is a point in a low-density region of the normal law P⁺; the problem is density level-set estimation) and a five-dimension modelling framework (loss, model, feature map, regularisation, inference mode), pairing classic "shallow" and deep methods across three families — probabilistic/density, one-class classification, reconstruction. A common benchmark on MNIST-C and MVTec-AD plus XAI explanations shows there is no silver bullet — and that a high AUC can be a Clever Hans effect driven by spurious correlations.

> 这篇综述(TU Berlin / Kloft / Dietterich / Müller 组)把异常检测统一到一个概率定义(异常 = 正常分布 P⁺ 低密度区的点,问题即密度水平集估计)和一个五维建模框架(损失、模型、特征映射、正则、推断方式)之下,把经典"浅层"方法与深度方法按三大族——概率/密度、单类分类、重建——一一对应;再用 MNIST-C 与 MVTec-AD 的统一实验与 XAI 解释表明:没有银弹,而且高 AUC 可能是 Clever Hans(靠虚假相关取得)。

## Related papers / 相关论文
- [[_maps/papers/anogan-ipmi-2017|AnoGAN]] — reviewed: GAN reconstruction
- [[_maps/papers/deep-svdd-icml-2018|Deep SVDD]] — hypersphere model, shallow ↔ deep
- [[_maps/papers/f-anogan-media-2019|f-AnoGAN]] — reviewed: GAN + explicit encoder
- [[_maps/papers/generalized-ood-survey-ijcv-2024|Generalized OOD survey]] — sensory / semantic anomaly split
- [[_maps/papers/medianomaly-media-2025|MedIAnomaly]] — multi-paradigm AD taxonomy
- [[_maps/papers/mvtec-ad-cvpr-2019|MVTec AD]] — benchmarks on MVTec AD

## Deep-read / 精读

![[papers/ad-unifying-review-procieee-2021/deep-read]]
