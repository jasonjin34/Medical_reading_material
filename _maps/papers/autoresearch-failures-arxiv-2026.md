---
title: 'How Do Agents Fail on AutoResearch: End-to-End Diagnostic Evaluation on 100
  Real-World Frontier Research Tasks'
aliases:
- AutoResearch failures
plans:
- B
track:
- B7
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

# How Do Agents Fail on AutoResearch: End-to-End Diagnostic Evaluation on 100 Real-World Frontier Research Tasks

> AutoResearchEval runs 8 harness–model combinations on 100 real research tasks derived from frontier papers (7 domains, full lifecycle: ideation → retrieval → execution → analysis → writing → self-review), yielding 800 full trajectories; an agent-as-a-judge that reads every artefact (code, logs, data, reports) annotates them, inducing ARFT, a taxonomy of 45 failure patterns. The conclusion: failures converge on one root cause — agents lack a metacognitive loop (they don't check output against evidence, don't act on problems they find, and don't question the path itself).

> AutoResearchEval 用 100 个来自前沿论文的真实科研任务(7 个领域、覆盖 ideation → 检索 → 执行 → 分析 → 写作 → 自审全生命周期)跑 8 种 harness–模型组合,得到 800 条完整轨迹;再用读取全部产物(代码、日志、数据、报告)的 agent-as-a-judge 标注,归纳出 45 种失败模式的 ARFT 分类法 —— 结论是所有失败汇聚到一个根因:agent 缺少元认知闭环(不核对产出与证据、发现问题也不修正、不质疑路径本身)。

## Related papers / 相关论文
- [[_maps/papers/kosmos-arxiv-2025|Kosmos]] — AI-scientist research
- [[_maps/papers/mast-neurips-2025|MAST]] — agent failure taxonomy
- [[_maps/papers/scirigor-arxiv-2026|SciRIGOR]] — unsupported claims

## Concepts / 概念
- [[_maps/concepts/benchmark-validity|Benchmark validity]]
- [[_maps/concepts/failure-taxonomy|Failure taxonomy]]
- [[_maps/concepts/research-agent|AI scientist agents]]
- [[_maps/concepts/trajectory-eval|Trajectory-level evaluation]]

## Deep-read / 精读

![[papers/autoresearch-failures-arxiv-2026/deep-read]]
