---
title: AI-enhanced adaptive virtual screening of large libraries for ligand discovery
aliases:
- AdaptiveFlow
plans:
- VS
track: []
year: 2026
relevance: high
category: drug-discovery
recommended_by: sikander
views:
- virtual-screening
- overview
tags:
- paper
- plan/VS
---

# AI-enhanced adaptive virtual screening of large libraries for ligand discovery

> AdaptiveFlow is an open-source (GNU GPL-2.0) ultralarge virtual screening (ULVS) platform: it prepares Enamine REAL Space 2022q1-2 into 69 billion ready-to-dock molecules partitioned by 18 molecular properties into ~12 million tranches, then runs Adaptive Target-Guided Virtual Screens (ATG-VS) — a 12-million-docking prescreen over 1–10 representative molecules per tranche, followed by a primary screen of only the best tranches (optionally with an active-learning ML classifier) — cutting exhaustive docking cost by up to 1,000-fold; it integrates ~1,500 docking protocols, scales near-linearly to 5.6 million vCPUs on AWS, and prospectively produced nanomolar inhibitors of FSP1 and PARP1 (afi-FSP1-1 Ki 0.283 µM, iParp1 IC50 8.8 nM) together with co-crystal structures.

> AdaptiveFlow 是一个开源(GNU GPL-2.0)的超大规模虚拟筛选(ULVS)平台:它把 Enamine REAL Space 2022q1-2 准备成 69 billion 个 ready-to-dock 分子、按 18 维分子性质切成约 1,200 万个 tranche(格子),再用 Adaptive Target-Guided Virtual Screen(ATG-VS)先用每格 1–10 个代表分子做 12 million 次 prescreen、只对最优的 tranche 做 primary screen(可选叠加一个主动学习式 ML 分类器),把穷举 docking 的成本最多降低 1,000 倍;平台集成约 1,500 个 docking protocol,在 AWS 上近线性扩展到 5.6 million vCPU,并在 FSP1 与 PARP1 上前瞻性地做出纳摩尔抑制剂(afi-FSP1-1 Ki 0.283 µM、iParp1 IC50 8.8 nM)与共晶结构。

## Related papers / 相关论文
- [[_maps/papers/biomni-biorxiv-2025|Biomni]] — agent tool orchestration
- [[_maps/papers/competitive-docking-npjdrugdiscov-2026|Competitive docking (AF3)]] — docking vs co-folding ranking
- [[_maps/papers/drugclip-science-2026|DrugCLIP]] — Enamine REAL library
- [[_maps/papers/exscalate-arxiv-2021|EXSCALATE (HPC docking)]] — ultra-large docking at scale

## Deep-read / 精读

![[papers/adaptiveflow-natbiotech-2026/deep-read]]
