---
title: AI-Based Anomaly Detection for Clinical-Grade Histopathological Diagnostics
aliases:
- Clinical-grade histo AD
plans:
- A
track:
- A6
year: 2024
relevance: high
category: histopath
recommended_by: core-reading
views:
- plan-a
- reading-list
- overview
tags:
- paper
- plan/A
---

# AI-Based Anomaly Detection for Clinical-Grade Histopathological Diagnostics

> A deep anomaly-detection model trained only on "frequent findings" (normal tissue plus common diseases) of stomach and colon biopsies — best variant: Outlier Exposure — detects the long tail of 56 rarer entities it never saw, with slide-AUROC 95.0% (stomach) and 91.0% (colon), and transfers to a second hospital and scanner without retraining.

> 只用"常见诊断"(正常组织 + 常见病)的胃、结肠活检切片训练深度异常检测模型(最佳为 Outlier Exposure),不需要见过任何罕见病,就能检出长尾中的 56 种少见病变:slide-AUROC 胃 95.0%、结肠 91.0%,并可泛化到另一家医院和另一种扫描仪。

## Related papers / 相关论文
- [[_maps/papers/energy-ood-neurips-2020|Energy OOD]] — outlier-exposure training
- [[_maps/papers/histo-anomaly-bi-repo|BI histo-AD code]] — histopath anomaly det.
- [[_maps/papers/histo-miccai-2025|Latent-diffusion AD]] — histopath anomaly det.
- [[_maps/papers/nih-kidney-ai-challenge-2026|NIH Kidney AI Challenge]] — WSI anomaly detection
- [[_maps/papers/patchcore-cvpr-2022|PatchCore]] — pretrained features + kNN distance
- [[_maps/papers/pathology-ad-bench-mlhealth-2025|Pathology AD benchmark]] — histopathology AD
- [[_maps/papers/virchow-2024|Virchow]] — FM backbone → anomaly det.

## Concepts / 概念
- [[_maps/concepts/anomalous-region|Anomalous tissue regions]]
- [[_maps/concepts/expert-validation|Expert validation]]

## Deep-read / 精读

![[papers/histo-nejmai-2024/deep-read]]
