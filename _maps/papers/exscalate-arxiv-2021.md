---
title: 'EXSCALATE: An extreme-scale in-silico virtual screening platform to evaluate
  1 trillion compounds in 60 hours on 81 PFLOPS supercomputers'
aliases:
- EXSCALATE (HPC docking)
plans:
- VS
track: []
year: 2021
relevance: medium
category: drug-discovery
recommended_by: sikander
views:
- virtual-screening
- overview
tags:
- paper
- plan/VS
---

# EXSCALATE: An extreme-scale in-silico virtual screening platform to evaluate 1 trillion compounds in 60 hours on 81 PFLOPS supercomputers

> This is a software-engineering / HPC systems paper: the authors rewrote Dompé's Exscalate docking platform as "one MPI process per node + an asynchronous in-node reader→splitter→docker→writer pipeline + heterogeneous CUDA/C++ workers", wrapped in a workflow (a decision tree predicts each ligand's docking time → ligands are bucketed by predicted time → ~3,400 independent SLURM jobs of ~5 minutes each). On CINECA-Marconi100 + ENI-HPC5 (81 PFLOPS combined) this docked 70+ billion small molecules against 15 binding sites of 12 SARS-CoV-2 proteins in 60 hours — about 1 trillion scoring evaluations at 5M ligands/s across both machines (~2.2k ligands/s per node).

> 这是一篇软件工程 / HPC 系统论文:作者把 Dompé 的 Exscalate 对接平台重写为「每节点一个 MPI 进程 + 节点内 reader→splitter→docker→writer 异步流水线 + CUDA/C++ 异构 worker」,并在外面套一层工作流(用决策树预测每个配体的对接耗时 → 按耗时分桶 → ~3400 个独立 SLURM 作业,每个约 5 分钟),从而在 CINECA-Marconi100 + ENI-HPC5(合计 81 PFLOPS)上于 60 小时内把 700 亿个小分子对接到 SARS-CoV-2 12 个病毒蛋白的 15 个结合位点上,合计约 1 万亿次打分,双机吞吐 5M ligands/s(单节点约 2.2k ligands/s)。

## Related papers / 相关论文
- [[_maps/papers/adaptiveflow-natbiotech-2026|AdaptiveFlow]] — ultra-large docking at scale

## Deep-read / 精读

![[papers/exscalate-arxiv-2021/deep-read]]
