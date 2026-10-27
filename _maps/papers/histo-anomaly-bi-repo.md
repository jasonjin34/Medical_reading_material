---
title: Boehringer-Ingelheim/anomaly-detection-in-histology
aliases:
- BI histo-AD code
plans:
- A
track:
- A6
year: 2022
relevance: medium
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

# Boehringer-Ingelheim/anomaly-detection-in-histology

> A PyTorch repository from Boehringer Ingelheim: a CNN is trained on healthy tissue from several species, organs and two stains (auxiliary classification + center-loss), then a one-class SVM is fit on healthy features of the target tissue to find drug-induced histological alterations in whole-slide images; companion paper: Zingman et al., *Medical Image Analysis* 2024.

> Boehringer Ingelheim 的 PyTorch 代码库:先在多物种、多器官、两种染色的健康组织上训练 CNN(辅助分类任务 + center-loss),再在目标组织的健康特征上训练 one-class SVM,用来在全切片中找出药物引起的组织病理改变;配套论文为 Zingman et al., *Medical Image Analysis* 2024。

## Related papers / 相关论文
- [[_maps/papers/deep-svdd-icml-2018|Deep SVDD]] — one-class boundary on learned features
- [[_maps/papers/histo-nejmai-2024|Clinical-grade histo AD]] — histopath anomaly det.
- [[_maps/papers/pathology-ad-bench-mlhealth-2025|Pathology AD benchmark]] — histology AD methods

## Concepts / 概念
- [[_maps/concepts/expert-validation|Expert validation]]

## Deep-read / 精读

![[papers/histo-anomaly-bi-repo/deep-read]]
