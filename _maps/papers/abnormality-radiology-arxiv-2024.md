---
title: Abnormality-Driven Representation Learning for Radiology Imaging
aliases:
- Abnormality radiology (Ligero 2024)
plans:
- A
track:
- A0
year: 2024
relevance: medium
category: imaging
recommended_by: core-reading
views:
- plan-a
- reading-list
- overview
tags:
- paper
- plan/A
---

# Abnormality-Driven Representation Learning for Radiology Imaging

> CLEAR treats a CT scan as a stack of 2D axial slices: a frozen encoder trained by self-supervised contrastive learning embeds each slice, and attention-based multiple-instance learning (ABMIL) aggregates them into a patient-level prediction; the proposed LeCL feeds lesion-centred crops to one encoder branch so that representations focus on abnormalities. With 22–36M-parameter models it matches or slightly beats BiomedCLIP on three tasks.

> CLEAR 框架把 CT 当作一叠 2D 轴位切片:用自监督对比学习训练的编码器(冻结)给每张切片提特征,再用注意力多示例学习(ABMIL)聚合成病人级预测;其中提出的 LeCL 在对比学习中让一路编码器看到以病灶为中心的裁剪,使表征更关注异常。用约 2–4 千万参数的模型,在三项任务上与 BiomedCLIP 相当或略好。

## Concepts / 概念
- [[_maps/concepts/foundation-model|Foundation models]]
- [[_maps/concepts/virtual-tissue|Virtual tissue / cell]]

## Deep-read / 精读

![[papers/abnormality-radiology-arxiv-2024/deep-read]]
