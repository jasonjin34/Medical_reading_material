---
title: 'MedAgentBench: A Virtual EHR Environment to Benchmark Medical LLM Agents'
aliases:
- MedAgentBench
plans:
- B
track:
- B3
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

# MedAgentBench: A Virtual EHR Environment to Benchmark Medical LLM Agents

> MedAgentBench (Stanford; Andrew Ng / Jonathan Chen groups) is the first benchmark requiring an LLM agent to autonomously read and write records in a FHIR-compliant virtual EHR: 300 verifiable clinical tasks (10 categories) written by internal-medicine physicians, over 100 patient profiles derived from de-identified real Stanford STARR cases (~785k records). In the preprint the best model, Claude 3.5 Sonnet v2, reaches 69.67% overall success; write (action) tasks are generally harder than read (query) tasks.

> MedAgentBench(Stanford,Andrew Ng / Jonathan Chen 组)是第一个要求 LLM agent 在 FHIR 兼容的虚拟 EHR 里自主读写病历的基准:300 个由内科医生编写、可验证的临床任务(10 类),100 名基于 Stanford STARR 去标识真实病例的患者档案(约 78.5 万条记录);预印本中最佳模型 Claude 3.5 Sonnet v2 总成功率 69.67%,写操作(action)普遍比查询(query)更难。

## Related papers / 相关论文
- [[_maps/papers/clinical-agent-reruns-arxiv-2026|Same patient, different order]] — reruns on MedAgentBench
- [[_maps/papers/ehr-apollo-arxiv-2026|APOLLO virtual patient]] — EHR environment
- [[_maps/papers/llm-judge-healthcare-arxiv-2026|LLM-as-judge in healthcare]] — healthcare LLM evaluation

## Concepts / 概念
- [[_maps/concepts/rerun-stability|Rerun stability & replay]]

## Deep-read / 精读

![[papers/medagentbench-nejmai-2025/deep-read]]
