---
title: A benchmark study of vision and pathology foundation models for computational
  pathology
aliases:
- Pathology FM benchmark
plans:
- A
track:
- A5
year: 2026
relevance: high
category: foundation
recommended_by: sikander
views:
- plan-a
- sikander
- overview
tags:
- paper
- plan/A
---

# A benchmark study of vision and pathology foundation models for computational pathology

> PathBench evaluates 32 foundation models — general vision (VM), general vision-language (VLM), pathology-specific vision (Path-VM) and pathology-specific vision-language (Path-VLM) — under one standardized frozen-feature + linear-probing protocol across 41 tasks, 53 datasets and >17,500 whole-slide images. Path-VMs lead, Path-VLMs lag, neither model size nor pretraining scale consistently predicts downstream performance, and late decision-level ensembling further improves robustness across datasets.

> PathBench 把 32 个基础模型(通用视觉 VM、通用视觉-语言 VLM、病理专用视觉 Path-VM、病理专用视觉-语言 Path-VLM)放进同一套「冻结特征 + linear probing」协议,在 41 个任务、53 个数据集、17,500+ 张全切片上统一评测,结论是:Path-VM 最强、Path-VLM 反而落后、模型规模与预训练数据量都不能稳定预测下游表现,而后期决策级集成能进一步提升跨数据集稳健性。

## Related papers / 相关论文
- [[_maps/papers/biomednlp-natcommun-2025|BioNLP LLM benchmark]] — scale ≠ performance
- [[_maps/papers/fm-arxiv-2604|Generative histopathology FM]] — pathology FM benchmark
- [[_maps/papers/hest1k-2024|HEST-1k]] — linear-probe eval protocol
- [[_maps/papers/uni2-h-model|UNI2-h]] — pathology FM benchmark
- [[_maps/papers/virchow-2024|Virchow]] — pathology FM benchmark

## Deep-read / 精读

![[papers/pathbench-natcommun-2026/deep-read]]
