---
title: Deep One-Class Classification
aliases:
- Deep SVDD
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

# Deep One-Class Classification

> Deep SVDD is, per the authors, the first deep method trained directly on an anomaly-detection objective: a network φ is trained so that normal data's representations fall into a minimum-volume hypersphere around a fixed centre c, and the test-time anomaly score is ‖φ(x) − c‖². The paper also proves which design choices cause "hypersphere collapse" (bias terms, bounded activations, a learnable centre) and the ν-property of the soft-boundary variant.

> Deep SVDD 是第一个直接以异常检测为目标训练的深度方法(作者自述):训练一个神经网络 φ,让正常数据的表示尽量落进一个以固定中心 c 为圆心、体积最小的超球,测试时异常分数就是 ‖φ(x) − c‖²;论文同时证明了哪些网络设计会导致"超球坍缩"(偏置项、有界激活、可学习的中心),以及软边界版本的 ν-性质。

## Related papers / 相关论文
- [[_maps/papers/ad-unifying-review-procieee-2021|Unifying AD review]] — hypersphere model, shallow ↔ deep
- [[_maps/papers/anogan-ipmi-2017|AnoGAN]] — AnoGAN as deep baseline
- [[_maps/papers/draem-iccv-2021|DRAEM]] — cites
- [[_maps/papers/generalized-ood-survey-ijcv-2024|Generalized OOD survey]] — one-class AD reviewed
- [[_maps/papers/histo-anomaly-bi-repo|BI histo-AD code]] — one-class boundary on learned features
- [[_maps/papers/meatrd-aaai-2025|MEATRD]] — cites

## Deep-read / 精读

![[papers/deep-svdd-icml-2018/deep-read]]
