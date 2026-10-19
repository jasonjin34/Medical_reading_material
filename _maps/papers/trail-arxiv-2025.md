---
title: 'TRAIL: Trace Reasoning and Agentic Issue Localization'
aliases:
- TRAIL
plans:
- B
track:
- B7
year: 2025
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

# TRAIL: Trace Reasoning and Agentic Issue Localization

> Patronus AI proposes an agent-error taxonomy (reasoning / planning & coordination / system execution) and releases TRAIL: 148 span-level human-annotated OpenTelemetry agent traces (from GAIA and SWE-bench Lite, 841 errors). Asked to act as trace debuggers that localize and categorize errors, LLMs do poorly — the best, Gemini-2.5-Pro, reaches only ~11% joint accuracy.

> Patronus AI 提出一套 agent 错误分类(推理 / 规划与协调 / 系统执行三大类),并发布 TRAIL:148 条人工逐 span 标注的 OpenTelemetry 结构化 agent 轨迹(来自 GAIA 与 SWE-bench Lite,共 841 个错误);让 LLM 当「轨迹调试员」去定位并分类错误时,最好的 Gemini-2.5-Pro 联合准确率也只有约 11%。

## Related papers / 相关论文
- [[_maps/papers/citation-blame-emnlp-2026|Who is to blame? (citations)]] — trace-level error localization
- [[_maps/papers/llm-judge-healthcare-arxiv-2026|LLM-as-judge in healthcare]] — LLM-as-judge reliability
- [[_maps/papers/mast-neurips-2025|MAST]] — agent failure taxonomy
- [[_maps/papers/scitrace-arxiv-2026|SciTrace]] — trajectory-level verification

## Concepts / 概念
- [[_maps/concepts/failure-taxonomy|Failure taxonomy]]
- [[_maps/concepts/human-calibration|Human / expert calibration]]

## Deep-read / 精读

![[papers/trail-arxiv-2025/deep-read]]
