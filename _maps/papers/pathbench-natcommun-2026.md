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

> This Stanford (Gevaert lab) benchmark evaluates 32 foundation models in four categories — general vision (VM), general vision-language (VLM), pathology vision (Path-VM) and pathology vision-language (Path-VLM) — all frozen with only a linear probe trained, on 41 tasks, 53 datasets and >17,500 WSIs. Path-VMs lead but differences among the top models are mostly non-significant, Path-VMs beat Path-VLMs, neither model size nor pretraining data size consistently predicts downstream performance, and majority-vote ensembling improves aggregate performance (Abstract).

> 这篇 Stanford(Gevaert 组)的 benchmark 把 32 个基础模型分成四类——通用视觉 VM、通用视觉-语言 VLM、病理专用视觉 Path-VM、病理专用视觉-语言 Path-VLM——全部冻结、只训 linear probe,在 41 个任务、53 个数据集、17,500+ 张 WSI 上统一评测:Path-VM 稳居前列但头部模型之间差异多不显著,Path-VM 优于 Path-VLM,模型规模和预训练数据量都不能稳定预测下游表现,多数投票集成在总体上进一步提升(Abstract)。

## Related papers / 相关论文
- [[_maps/papers/biomednlp-natcommun-2025|BioNLP LLM benchmark]] — scale ≠ performance
- [[_maps/papers/fm-arxiv-2604|Generative histopathology FM]] — pathology FM benchmark
- [[_maps/papers/hest1k-2024|HEST-1k]] — linear-probe eval protocol
- [[_maps/papers/uni2-h-model|UNI2-h]] — pathology FM benchmark
- [[_maps/papers/virchow-2024|Virchow]] — pathology FM benchmark

## Concepts / 概念
- [[_maps/concepts/ood-detection|OOD / novelty detection]]

## Deep-read / 精读

![[papers/pathbench-natcommun-2026/deep-read]]
