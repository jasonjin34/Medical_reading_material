---
title: 'Biomni: A General-Purpose Biomedical AI Agent'
aliases:
- Biomni
plans:
- B
track:
- B1
year: 2025
relevance: high
category: agents
recommended_by: core-reading
views:
- plan-b
- reading-list
- overview
tags:
- paper
- plan/B
---

# Biomni: A General-Purpose Biomedical AI Agent

> Biomni is the Leskovec-lab general-purpose biomedical agent: an action discovery agent reads the 100 most recent papers in each of bioRxiv's 25 subject categories (2,500 papers) and extracts tasks, software and databases, which are implemented and tested by humans into the unified environment Biomni-E1 (150 specialised tools + 105 software packages + 59 databases); a CodeAct-based agent Biomni-A1 (retrieve relevant tools → write a plan → write and run code → revise the plan from results) then solves cross-domain tasks zero-shot, plus one CRISPR-cloning wet-lab run that followed its protocol verbatim (Results §"Overview of Biomni"; Fig. 1; Fig. 4).

> Biomni 是斯坦福 Leskovec 组的通用生物医学 agent:先让一个 action discovery agent 读 bioRxiv 25 个学科各 100 篇最新论文(共 2,500 篇),抽取任务、软件和数据库,经人工实现与测试后建成统一环境 Biomni-E1(150 个专用工具 + 105 个软件包 + 59 个数据库);再用基于 CodeAct 的 agent Biomni-A1(检索相关工具 → 写计划 → 写代码执行 → 根据结果修改计划)零样本完成跨领域任务,并有一个按其 protocol 原样执行的 CRISPR 克隆湿实验(Results §"Overview of Biomni";Fig. 1;Fig. 4)。

## Related papers / 相关论文
- [[_maps/papers/bioml-bench-biorxiv-2025|BioML-bench]] — cites
- [[_maps/papers/biomnibench-biorxiv-2026|BiomniBench]] — cites
- [[_maps/papers/deepevidence-natmachintell-2026|DeepEvidence]] — cites
- [[_maps/papers/fev-bioinformatics-agents-arxiv-2026|FEV review]] — bio agent review
- [[_maps/papers/heurekabench-arxiv-2026|HeurekaBench]] — cites
- [[_maps/papers/lab-bench-arxiv-2024|LAB-Bench]] — cites
- [[_maps/papers/spatialagent-biorxiv-2025|SpatialAgent]] — same lab lineage
- [[_maps/papers/virtual-biotech-biorxiv-2026|Virtual Biotech]] — cites
- [[_maps/papers/virtual-lab-nature-2025|Virtual Lab]] — multi-agent biomedical systems

## Concepts / 概念
- [[_maps/concepts/omics-agent|Single-cell analysis agents]]
- [[_maps/concepts/rerun-stability|Rerun stability & replay]]
- [[_maps/concepts/virtual-tissue|Virtual tissue / cell]]

## Deep-read / 精读

![[papers/biomni-biorxiv-2025/deep-read]]
