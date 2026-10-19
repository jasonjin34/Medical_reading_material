---
title: 'HeurekaBench: A Benchmarking Framework for AI Co-scientist'
aliases:
- HeurekaBench
plans:
- B
track:
- B2
year: 2026
relevance: medium
category: agents
recommended_by: ''
views:
- plan-b
- overview
tags:
- paper
- plan/B
---

# HeurekaBench: A Benchmarking Framework for AI Co-scientist

> HeurekaBench (Brbić lab, EPFL) is a framework for constructing "AI co-scientist" benchmarks: a multi-LLM pipeline extracts insights from published papers and their code repositories, matches and composes code workflows, and keeps an insight only after humans run the code and confirm it reproduces the paper's result; validated insights become open-ended (OEQ) and multiple-choice (MCQ) questions. Instantiated for single-cell biology as sc-HeurekaBench (41 validated insights, 50 OEQ + 50 MCQ), scored by an LLM judge that decomposes answers into atomic facts, it compares Biomni, CellVoyager and BixBench-Agent and ablates planner, critic and retriever choices.

> HeurekaBench(EPFL Brbić 组)是一个构造"AI co-scientist"基准的框架:用多 LLM 流水线从已发表论文及其代码仓库中抽取洞见、匹配并生成代码流程,再由人实际运行代码、确认能复现论文结果后才保留,最后转成开放题(OEQ)与选择题(MCQ);在单细胞领域实例化为 sc-HeurekaBench(41 条验证洞见、50 OEQ + 50 MCQ),用原子事实分解的 LLM 评审打分,并用它比较 Biomni、CellVoyager、BixBench-Agent 及 planner / critic / retriever 设计。

## Related papers / 相关论文
- [[_maps/papers/biomni-biorxiv-2025|Biomni]] — cites
- [[_maps/papers/bixbench-arxiv-2025|BixBench]] — cites
- [[_maps/papers/cellvoyager-natmethods-2026|CellVoyager]] — cites
- [[_maps/papers/co-scientist-nature-2026|Co-Scientist]] — cites
- [[_maps/papers/lab-bench-arxiv-2024|LAB-Bench]] — cites
- [[_maps/papers/robin-nature-2026|Robin]] — cites
- [[_maps/papers/scbench-long-arxiv-2026|scBench-Long]] — claims reproduced before grading

## Concepts / 概念
- [[_maps/concepts/claim-evidence|Claim → evidence chains]]
- [[_maps/concepts/omics-agent|Single-cell analysis agents]]
- [[_maps/concepts/outcome-eval|Final-answer grading]]
- [[_maps/concepts/research-agent|AI scientist agents]]

## Deep-read / 精读

![[papers/heurekabench-arxiv-2026/deep-read]]
