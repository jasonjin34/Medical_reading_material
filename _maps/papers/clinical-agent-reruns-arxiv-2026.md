---
title: 'Same Patient, Different Order: Action-Level Reliability of Clinical LLM Agents
  Under Repeated Runs'
aliases:
- Same patient, different order
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

# Same Patient, Different Order: Action-Level Reliability of Clinical LLM Agents Under Repeated Runs

> The authors propose a "same-input rerun" protocol: replay each MedAgentBench task five times with patient and all inputs fixed, and compare not the score but the orders (FHIR write requests) the agent actually issues. Action-level divergence is pervasive and often invisible to the benchmark's verdict: for Llama-3.1-8B at temperature 0.7, all 43 ordering groups emit a different order set across five identical runs, yet in 22 of them the benchmark reports the same verdict.

> 作者提出「same-input rerun」协议:在 MedAgentBench 上把同一任务、同一患者、全部输入固定重跑 5 次,比较的不是分数而是 agent 实际下达的医嘱(FHIR 写请求)—— 结果显示动作层面的分歧普遍存在且常常不被 benchmark 的判分记录:Llama-3.1-8B 在 0.7 温度下 43/43 个下单任务组每次下达的医嘱集合都不同,其中 22 组的 benchmark 判定却完全相同。

## Related papers / 相关论文
- [[_maps/papers/holistic-agent-leaderboard-iclr-2026|Holistic Agent Leaderboard]] — rerun stability
- [[_maps/papers/medagentbench-nejmai-2025|MedAgentBench]] — reruns on MedAgentBench

## Concepts / 概念
- [[_maps/concepts/rerun-stability|Rerun stability & replay]]

## Deep-read / 精读

![[papers/clinical-agent-reruns-arxiv-2026/deep-read]]
