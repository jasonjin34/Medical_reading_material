# Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents

> **Bibkey** `Rao2026_260403173` · **Venue** arXiv preprint (2026) · **Category** agents · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2604.03173>
> `status: complete` — 基于 arXiv HTML 全文精读(正文 + Limitations;附录未逐条核对)。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> 在 10 个模型/agent(DRBench,53,090 个 URL)和 3 个模型(ExpertQA,168,021 个 URL,32 个学科)上量化引用 URL 的可靠性:**3%–13% 的引用 URL 是幻觉**(Wayback Machine 无任何存档、很可能从未存在),5%–18% 无法解析;deep research agent 引用最多、幻觉率也最高;作者发布 83 行的 `urlhealth` 工具,作为 agent 的自我纠错工具可把无法解析的 URL 降低 6–79×、到 1% 以下。
<!-- EN --> Quantifies citation-URL reliability across 10 models/agents on DRBench (53,090 URLs) and 3 models on ExpertQA (168,021 URLs, 32 fields): **3–13% of cited URLs are hallucinated** (no Wayback Machine record — likely never existed) and 5–18% are non-resolving; deep research agents cite the most and hallucinate the most. The authors release `urlhealth`, an 83-line tool that, used for agentic self-correction, cuts non-resolving URLs 6–79× to under 1%.

## 研究问题 / Problem
<!-- ZH --> 所有主流厂商都提供带行内引用的 deep research 模式,用户把引用当证据,但引用 URL 的可靠性从未被跨模型、跨厂商、跨学科系统测量,也没有可复用的检测/缓解工具。归因文献问的是「来源是否支持 claim」,本文问的是**逻辑上更前置的问题:来源是否存在**—— 若 3%–13% 的 URL 是编造的,所有 support 类指标都会系统性高估可靠性。六个 RQ:流行度、系统类型、学科差异、失败构成(编造 vs 链接失效)、数量 vs 质量、缓解。
<!-- EN --> Every major provider offers a deep-research mode with inline citations and users treat them as evidence, yet citation-URL reliability had never been measured systematically across models, providers and fields, and no reusable detection/mitigation tooling existed. The attribution literature asks "does the source support the claim?"; this paper asks the **logically prior question: does the source exist?** — if 3–13% of URLs are fabricated, support metrics systematically overestimate reliability. Six RQs: prevalence, system type, field variation, failure composition (fabrication vs link rot), quantity vs quality, mitigation.

## 方法 / Method
<!-- ZH --> **操作化定义**:non-resolving = HTTP 4xx/5xx 或连接失败(**排除 403**,因多为反爬;无头浏览器审计显示 403 中 99.7% 实际可访问);hallucinated = non-resolving 且 Wayback Machine 任何时间都没有快照;stale = non-resolving 但有快照(自然链接失效)。由于 Wayback 覆盖不完整,幻觉率是**保守下界**。**流程**:正则(DRBench)或厂商 API 结构(ExpertQA)抽 URL → HEAD 请求(405/403/501 回退 GET,浏览器 UA)→ 对 non-resolving 查 Wayback。**urlhealth**:把 URL 分为 LIVE / DEAD(404 有存档)/ LIKELY_HALLUCINATED(404 无存档)/ UNKNOWN,pip 包 + agentskills.io skill。**自我纠错实验**:435 道 ExpertQA 题(20% 抽样),Claude Sonnet 4.5、GPT-5.1 在同一轮中把 urlhealth 作为函数工具与 web search 并用;Gemini 2.5 Pro 因 API 不允许 grounding 与自定义工具同时用,采用两阶段。
<!-- EN --> **Operational definitions**: non-resolving = HTTP 4xx/5xx or connection failure (**403 excluded** as mostly bot-blocking; a headless-browser audit finds 99.7% of 403s live); hallucinated = non-resolving with no Wayback snapshot at any time; stale = non-resolving but archived (natural link rot). Because Wayback coverage is incomplete, hallucination rates are **conservative lower bounds**. **Pipeline**: extract URLs by regex (DRBench) or provider API structures (ExpertQA) → HEAD request (GET fallback on 405/403/501, browser UA) → Wayback lookup for non-resolving URLs. **urlhealth** classifies URLs as LIVE / DEAD (404, archived) / LIKELY_HALLUCINATED (404, unarchived) / UNKNOWN; shipped as a pip package and an agentskills.io skill. **Self-correction**: 435 ExpertQA questions (20% sample); Claude Sonnet 4.5 and GPT-5.1 call urlhealth as a function tool alongside web search in the same turn; Gemini 2.5 Pro uses a two-phase setup because its API forbids combining grounding with custom tools.

## 数据 / Data
<!-- ZH --> **DRBench**(Du et al., 2025):100 个中英文研究查询(金融、科学、技术),预先收集了 23 个模型的输出,本文分析其中 Google/OpenAI/Anthropic 的 10 个(2 个 deep research agent + 8 个搜索增强 LLM)。**ExpertQA**(Malaviya et al., 2024):2,177 个专家问题,32 个学科;本文用 claude-sonnet-4-5、gemini-2.5-pro、gpt-5.1 重新生成带编号引用的结构化回答。
<!-- EN --> **DRBench** (Du et al., 2025): 100 multilingual (Chinese/English) research queries in finance, science and technology with pre-collected outputs from 23 models; 10 from Google/OpenAI/Anthropic are analysed (2 deep-research agents + 8 search-augmented LLMs). **ExpertQA** (Malaviya et al., 2024): 2,177 expert questions across 32 fields; the authors regenerate structured answers with numbered citations from claude-sonnet-4-5, gemini-2.5-pro and gpt-5.1.

## 主要结果 / Key results
<!-- ZH --> **RQ1**:DRBench 上 non-resolving 从 5.4%(gpt-4.1)到 18.5%(gemini-2.5-pro-deepresearch),hallucinated 从 3.0%(claude-3-5-sonnet-search)到 13.3%(gemini-2.5-pro-deepresearch);ExpertQA 总体 non-resolving 8.22%(gpt-5.1 8.47%、claude-sonnet-4-5 9.38%、gemini-2.5-pro 4.20%)。**RQ2**:两个 deep research agent 合并幻觉率 10.7% vs 八个搜索增强模型 4.8%;non-resolving 16.2% vs 6.8%。gemini-2.5-pro-deepresearch 每查询 113.1 个 URL;openai-deepresearch 41.2 个,幻觉率仅 3.5% 但 non-resolving 10.1%(65% 为 stale)。**RQ3**:学科间 5.4%(商科)到 11.4%(神学);Claude Sonnet 4.5 在数学 4.0% 到医疗 17.4%,差 4.3×;**医疗/医学在三个模型上都偏高**(Claude 17.4%、GPT 7.1%、Gemini 5.3%)。**RQ4**:四个 OpenAI 搜索增强模型 stale=0 —— 它们的每个失效 URL 都是编造的;Claude 与 deep research agent 则有明显 stale 比例,说明是真实检索遇到过期索引。**RQ5**:更多引用 ≠ 更可靠(gpt-5.1 每题 46.4 个 URL,失效率是 gemini 的 2 倍)。**RQ6**:urlhealth 作为工具后 non-resolving 率:GPT-5.1 16.0%→0.6%、Gemini 6.1%→0.1%、Claude 4.9%→0.8%(均 p<0.001);但 UNKNOWN 仍有 10%–20%(反爬/付费墙),是自动核验的实际上限。**工具使用能力很关键**:gpt-5-nano 调用了工具却不按结果行动,最终 NOT_LIVE 7.5%,48 个幻觉 URL 在最多 14 轮纠错后仍存在。
<!-- EN --> **RQ1**: on DRBench, non-resolving ranges from 5.4% (gpt-4.1) to 18.5% (gemini-2.5-pro-deepresearch) and hallucinated from 3.0% (claude-3-5-sonnet-search) to 13.3% (gemini-2.5-pro-deepresearch); ExpertQA overall non-resolving is 8.22% (gpt-5.1 8.47%, claude-sonnet-4-5 9.38%, gemini-2.5-pro 4.20%). **RQ2**: pooled hallucination 10.7% for the two deep-research agents vs 4.8% for eight search-augmented models; non-resolving 16.2% vs 6.8%. gemini-2.5-pro-deepresearch cites 113.1 URLs/query; openai-deepresearch 41.2, with only 3.5% hallucinated but 10.1% non-resolving (65% stale). **RQ3**: 5.4% (Business) to 11.4% (Theology); Claude Sonnet 4.5 ranges 4.0% (Mathematics) to 17.4% (Healthcare/Medicine), 4.3×; **Healthcare/Medicine is elevated for all three** (Claude 17.4%, GPT 7.1%, Gemini 5.3%). **RQ4**: four OpenAI search-augmented models have zero stale URLs — every failing URL is fabricated; Claude and the deep-research agents show substantial stale fractions, consistent with genuine retrieval over a partly stale index. **RQ5**: more citations ≠ more reliable (gpt-5.1 cites 46.4 URLs/question with 2× Gemini's failure rate). **RQ6**: with urlhealth as a tool, non-resolving drops GPT-5.1 16.0% → 0.6%, Gemini 6.1% → 0.1%, Claude 4.9% → 0.8% (all p < 0.001), but 10–20% remain UNKNOWN (bot-blocking/paywalls) — a practical ceiling. **Tool-use competence matters**: gpt-5-nano called the tool but ignored its results (7.5% NOT_LIVE; 48 hallucinated URLs persisted over up to 14 rounds).

## 创新点 / Contributions
- <!-- ZH --> 用 Wayback Machine 把「失效」拆成**编造 vs 链接失效**,两者需要完全不同的缓解(更好的 grounding vs 更新的索引/事后校验)。 <!-- EN --> Uses the Wayback Machine to split failures into **fabrication vs link rot**, which require different mitigations (better grounding vs fresher indices / post-hoc validation).
- <!-- ZH --> 迄今最大规模的检索增强场景 URL 有效性测量(22 万+ URL),修正了 SourceCheckup「RAG 不产生 URL 幻觉」的结论。 <!-- EN --> The largest URL-validity measurement in retrieval-augmented settings to date (220K+ URLs), qualifying SourceCheckup's "RAG avoids URL hallucination" conclusion.
- <!-- ZH --> 极简、模型无关的开源工具 + agent 自我纠错实验,证明「存在性核验」可在实践中修复。 <!-- EN --> A minimal, model-agnostic open tool plus agentic self-correction experiments showing existence verification is correctable in practice.

## 局限 / Limitations
- <!-- ZH --> 幻觉判定依赖 Wayback 覆盖,存在 stale/hallucinated 互相误分;URL 存活是时点测量,受反爬影响。 <!-- EN --> Hallucination labels depend on Wayback coverage (stale/hallucinated misclassification both ways); liveness is a point-in-time measurement affected by bot-blocking.
- <!-- ZH --> 只覆盖 URL 型引用;编造片段(引用页里没有的原文)与伪造书目元数据(错作者、假 DOI)只做了定性描述。 <!-- EN --> URL citations only; fabricated snippets and invented bibliographic metadata (wrong authors, fake DOIs) are documented only qualitatively.
- <!-- ZH --> **只测「来源存在」,不测「来源支持 claim」**:一个 LIVE 的 URL 仍可能完全不支持对应陈述。 <!-- EN --> **Measures existence, not support**: a LIVE URL may still not support the statement.
- <!-- ZH --> 三家厂商、两个以英文为主的基准;自我纠错只用 20% 子集(受 API 限额影响)。 <!-- EN --> Three providers, two English-dominated benchmarks; self-correction on a 20% subset (API quota limits).

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 对 **课题 2** 来说这是 claim-to-evidence 核验链条的**第 0 层:证据是否存在**。在组学 agent 场景中,对应物不是 URL,而是 agent 报告里引用的**文件路径、图、表、单元格输出、数据集 accession(GEO/KPMP)、基因 ID**—— 这些都可能被「编造」(报告引用了从未生成的 `de_results.csv`)或「失效」(中间文件被覆盖、notebook 状态丢失)。本文的分类法可直接移植为 omics-specific failure taxonomy 的一支:**artefact-fabricated / artefact-stale / artefact-live-but-unsupported**,urlhealth 的 LIVE/DEAD/HALLUCINATED/UNKNOWN 四分类也可以换成对 agent 工作目录与 provenance log 的存在性检查。两点实验发现尤其可借:(1) deep research 这类长程多步系统**幻觉率更高** —— 多步分析 agent 也应预期类似的误差累积;(2) 「给工具 ≠ 会用工具」,小模型会无视核验结果 —— 设计 verifier-in-the-loop 时要测量 agent 是否真正按 verifier 反馈改正,而不只是调用了它。与课题 1 无直接关系。
<!-- EN --> For **Topic 2** this is **layer 0 of the claim-to-evidence chain: does the evidence exist?** In an omics-agent setting the analogue of a URL is a **file path, figure, table, cell output, dataset accession (GEO/KPMP) or gene ID** cited in the agent's report — any of which can be "fabricated" (the report cites a `de_results.csv` that was never produced) or "stale" (an intermediate file overwritten, notebook state lost). The taxonomy ports directly into one branch of an omics-specific failure taxonomy — **artefact-fabricated / artefact-stale / artefact-live-but-unsupported** — and urlhealth's LIVE/DEAD/HALLUCINATED/UNKNOWN scheme can become an existence check over the agent's working directory and provenance log. Two findings transfer: (1) long-horizon multi-step systems hallucinate **more** — expect similar error accumulation in multi-step analysis agents; (2) "having a tool ≠ using it" — small models ignore verification results, so a verifier-in-the-loop design must measure whether the agent actually acts on verifier feedback, not merely whether it calls it. No direct bearing on Topic 1.

## 可复用资产 / Reusable assets
- <!-- ZH --> **工具:** `urlhealth`(83 行 Python,pip 包 + agentskills.io skill,MIT 许可;论文称工具与全部数据公开,但正文未给出仓库链接)。 <!-- EN --> **Tool:** `urlhealth` (83 lines of Python; pip package + agentskills.io skill, MIT; the paper says tool and data are public but gives no repository link in the main text).
- <!-- ZH --> **基准:** DRBench、ExpertQA。 <!-- EN --> **Benchmarks:** DRBench, ExpertQA.
- <!-- ZH --> **核验协议:** HEAD→GET 回退 + 排除 403 + Wayback 存档判定 + 无头浏览器抽查 UNKNOWN。 <!-- EN --> **Verification protocol:** HEAD→GET fallback, 403 exclusion, Wayback archive test, headless-browser audit of UNKNOWNs.
<!-- ZH/EN --> <https://archive.org/help/wayback_api.php>

## 待读 / Follow-ups
- <!-- ZH --> GhostCite(Xu et al., 2026)、CiteAudit(Yuan et al., 2026)、CiteGuard(Choi et al., 2026)—— 引用核验的并行工作。 <!-- EN --> GhostCite (Xu et al., 2026), CiteAudit (Yuan et al., 2026), CiteGuard (Choi et al., 2026) — parallel citation-verification work.
- <!-- ZH --> DRACO(Zhong et al., 2026):deep research 的引用质量与事实准确度轴。 <!-- EN --> DRACO (Zhong et al., 2026): citation-quality and factual-accuracy axes for deep research.
- <!-- ZH --> 与本仓库 sourcecheckup-natcommun-2025、deeptrace-arxiv-2025 对读:存在性 → 支持性 → 端到端审计。 <!-- EN --> Read with sourcecheckup-natcommun-2025 and deeptrace-arxiv-2025: existence → support → end-to-end audit.

## 引用 / Cite
```bibtex
@misc{Rao2026_260403173,
  title = {Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents},
  author = {Delip Rao and Eric Wong and Chris Callison-Burch},
  year = {2026},
  eprint = {2604.03173},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2604.03173}
}
```
