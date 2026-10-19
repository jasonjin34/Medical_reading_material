---
title: Quantitative benchmarking of anomaly detection methods in digital pathology
  images
aliases:
- Pathology AD benchmark
plans:
- A
track:
- A6
year: 2025
relevance: high
category: histopath
recommended_by: ''
views:
- plan-a
- overview
tags:
- paper
- plan/A
---

# Quantitative benchmarking of anomaly detection methods in digital pathology images

> Yuankai Huo's group (HRLB, Vanderbilt) benchmarks 23 generic anomaly-detection methods (reconstruction, feature-distribution, distillation, normalizing-flow and synthetic-anomaly families) under one protocol on real pathology (Camelyon16, Crohn's colon, mouse glomeruli), controlled synthetic pathology and MVTec industrial data, and systematically studies three under-examined factors — image scale, "reversed" anomaly patterns, and how to pick a training epoch when no anomalies are available. No method wins everywhere; feature-distribution methods are best overall; and real pathology is far harder than industrial data (mean ROC-AUC ≈ 0.645 vs 0.888).

> Vanderbilt 的 Huo 组(HRLB)把 23 种通用 anomaly detection 方法(重建、特征分布、蒸馏、normalizing flow、合成异常五大类)放到真实病理(Camelyon16、Crohn 结肠、小鼠肾小球)+ 受控合成病理 + MVTec 工业数据上统一评测,系统考察图像尺度、异常模式「反转」、以及没有异常样本时如何选 epoch 三个常被忽略的因素;结论是没有通吃的方法,特征分布类整体最好,而真实病理比工业数据难得多(平均 ROC-AUC 约 0.645 对 0.888)。

## Related papers / 相关论文
- [[_maps/papers/cflow-ad-wacv-2022|CFLOW-AD]] — cites
- [[_maps/papers/draem-iccv-2021|DRAEM]] — cites
- [[_maps/papers/histo-anomaly-bi-repo|BI histo-AD code]] — histology AD methods
- [[_maps/papers/histo-nejmai-2024|Clinical-grade histo AD]] — histopathology AD
- [[_maps/papers/medianomaly-media-2025|MedIAnomaly]] — cites
- [[_maps/papers/mvtec-ad-cvpr-2019|MVTec AD]] — cites
- [[_maps/papers/nih-kidney-ai-challenge-2026|NIH Kidney AI Challenge]] — pathology AD benchmark
- [[_maps/papers/padim-icpr-2020|PaDiM]] — cites
- [[_maps/papers/patchcore-cvpr-2022|PatchCore]] — cites

## Deep-read / 精读

![[papers/pathology-ad-bench-mlhealth-2025/deep-read]]
