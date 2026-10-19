---
title: A multi-agent system for automating scientific discovery
aliases:
- Robin
plans:
- B
track:
- B1
year: 2026
relevance: high
category: agents
recommended_by: ''
views:
- plan-b
- overview
tags:
- paper
- plan/B
---

# A multi-agent system for automating scientific discovery

> FutureHouse's Robin chains literature agents (Crow/Falcon, built on PaperQA2) and a data-analysis agent (Finch) into a lab-in-the-loop cycle: given a disease, it proposes mechanisms, in vitro models and drug candidates; humans run the suggested experiments and upload raw data; Finch runs eight independent analysis trajectories and takes a consensus; Robin updates its hypotheses. For dry AMD it proposed enhancing RPE phagocytosis, found the ROCK inhibitor ripasudil (1.89-fold over DMSO) and KL001, and via RNA-seq uncovered ABCA1 upregulation — all hypotheses, experimental directions, data analyses and data figures in the main text were produced by Robin.

> FutureHouse 的 Robin 把文献检索 agent(Crow/Falcon,基于 PaperQA2)与数据分析 agent(Finch)串成一个 lab-in-the-loop 闭环:给定疾病,自动提出机制、体外模型与候选药物,人类按其建议做实验并上传原始数据,Finch 跑 8 条独立分析轨迹取共识,Robin 再据此更新假设;在干性 AMD 上,它提出「增强 RPE 吞噬」策略,找到 ROCK 抑制剂 ripasudil(比 DMSO 提升 1.89 倍)与 KL001,并经 RNA-seq 发现 ABCA1 上调——正文所有假设、实验方向、数据分析与数据图均由 Robin 产生。

## Related papers / 相关论文
- [[_maps/papers/bixbench-arxiv-2025|BixBench]] — Finch on BixBench
- [[_maps/papers/citation-faithfulness-arxiv-2026|Citation faithfulness guard]] — cites
- [[_maps/papers/co-scientist-nature-2026|Co-Scientist]] — AI scientists
- [[_maps/papers/kosmos-arxiv-2025|Kosmos]] — FutureHouse lineage
- [[_maps/papers/paperqa2-arxiv-2024|PaperQA2]] — FutureHouse literature agent

## Concepts / 概念
- [[_maps/concepts/hallucination|Hallucination]]
- [[_maps/concepts/llm-judge|LLM-as-judge]]
- [[_maps/concepts/reference-hallucination|Fabricated references]]

## Deep-read / 精读

![[papers/robin-nature-2026/deep-read]]
