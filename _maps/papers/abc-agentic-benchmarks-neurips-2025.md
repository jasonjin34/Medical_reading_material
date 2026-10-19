---
title: Establishing Best Practices for Building Rigorous Agentic Benchmarks
aliases:
- ABC checklist
plans:
- B
track:
- B7
year: 2025
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

# Establishing Best Practices for Building Rigorous Agentic Benchmarks

> The authors split "can this agentic-benchmark score be trusted" into two conditions — task validity (task success ⇔ the target capability) and outcome validity (a positive evaluation ⇔ genuine task success) — and turn them into an actionable Agentic Benchmark Checklist (ABC). Auditing ten popular agentic benchmarks with it, they find 7 violate outcome validity, 7 violate task validity, and all 10 have reporting gaps, with estimation errors of up to 100% in relative terms.

> 作者把 agent 基准「分数可信」拆成两个条件 —— task validity(任务成功 ⇔ 具备目标能力)与 outcome validity(评测判定为成功 ⇔ 任务真的成功)—— 并据此写出一份可操作的 Agentic Benchmark Checklist (ABC);用它审查 10 个主流 agent 基准,发现 7 个违反 outcome validity、7 个违反 task validity、10 个全部在结果报告上有缺陷,误差最高可达相对 100%。

## Related papers / 相关论文
- [[_maps/papers/ailuminate-arxiv-2025|AILuminate]] — MLCommons benchmark rigor
- [[_maps/papers/bixbench-arxiv-2025|BixBench]] — benchmark-validity audit
- [[_maps/papers/holistic-agent-leaderboard-iclr-2026|Holistic Agent Leaderboard]] — benchmark rigor → harness

## Concepts / 概念
- [[_maps/concepts/benchmark-validity|Benchmark validity]]
- [[_maps/concepts/llm-judge|LLM-as-judge]]

## Deep-read / 精读

![[papers/abc-agentic-benchmarks-neurips-2025/deep-read]]
