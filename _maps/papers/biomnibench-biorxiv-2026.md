---
title: 'BiomniBench: Process-level Evaluation of LLM Agents for Real-world Biomedical
  Research'
aliases:
- BiomniBench
plans:
- B
track:
- B3
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

# BiomniBench: Process-level Evaluation of LLM Agents for Real-world Biomedical Research

> BiomniBench is a process-level benchmark for biomedical agents: instead of scoring only the final answer, an LLM judge grades the agent's full analytical trajectory (trace.md + answer.txt) against expert-written (often original-author-written), task-specific A/B/C rubrics. The first release, BiomniBench-DA, has 100 data-analysis tasks built on the public data of Nature/Cell/Science-tier papers. The best configuration (Claude Code + Opus 4.7) reaches only 73.34/100, and the agent harness moves scores more than a model generation does.

> BiomniBench 是一个过程级(process-level)的生物医学 agent 基准:不只看最终答案,而是用专家(常为原论文作者)编写的、任务特定的 A/B/C 分级 rubric,由 LLM judge 对 agent 的完整分析轨迹(trace.md + answer.txt)打分;首发 BiomniBench-DA 含 100 个基于 Nature/Cell/Science 级论文公开数据的数据分析任务。最佳配置(Claude Code + Opus 4.7)仅 73.34/100,且 agent harness 对分数的影响大于模型换代。

## Related papers / 相关论文
- [[_maps/papers/bioml-bench-biorxiv-2025|BioML-bench]] — cites
- [[_maps/papers/biomni-biorxiv-2025|Biomni]] — cites
- [[_maps/papers/bixbench-arxiv-2025|BixBench]] — cites
- [[_maps/papers/lab-bench-arxiv-2024|LAB-Bench]] — cites
- [[_maps/papers/scbench-arxiv-2026|scBench]] — omics-analysis agent benchmarks
- [[_maps/papers/spatialagent-biorxiv-2025|SpatialAgent]] — cites

## Concepts / 概念
- [[_maps/concepts/llm-judge|LLM-as-judge]]
- [[_maps/concepts/outcome-eval|Final-answer grading]]
- [[_maps/concepts/reference-hallucination|Fabricated references]]
- [[_maps/concepts/rerun-stability|Rerun stability & replay]]
- [[_maps/concepts/trajectory-eval|Trajectory-level evaluation]]

## Deep-read / 精读

![[papers/biomnibench-biorxiv-2026/deep-read]]
