# DeepTRACE: Auditing Deep Research AI Systems for Tracking Reliability Across Citations and Evidence

> **Bibkey** `NarayananVenkit2025_250904499` · **Venue** arXiv preprint (2025) · **Category** agents · **Relevance** medium · **Access** open
> **Link** <https://arxiv.org/abs/2509.04499>
> `status: complete` — 基于 arXiv HTML 全文精读(正文;附录阈值与 prompts 未逐条核对)。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> DeepTRACE 把先前用户研究中社区识别出的生成式搜索/deep research 失效案例,转化为覆盖「答案文本 · 来源 · 引用」的 **8 个可计算指标**,核心是两张矩阵 —— **引用矩阵**(statement 引了哪些来源)与**事实支持矩阵**(哪些来源真的支持该 statement);在 303 个问题 × 9 个公开系统上发现:deep research 降低了过度自信,但在辩论题上仍高度片面,无支持 statement 比例很高,引用准确率只有 40%–80%。
<!-- EN --> DeepTRACE turns community-identified failure cases of generative search engines and deep-research agents (from a prior user study) into **eight computable metrics** spanning answer text, sources and citations, built on two matrices — a **citation matrix** (which sources each statement cites) and a **factual-support matrix** (which sources actually support it). Across 303 questions × 9 public systems: deep-research modes reduce overconfidence but remain highly one-sided on debate queries, leave large fractions of statements unsupported, and reach only 40–80% citation accuracy.

## 研究问题 / Problem
<!-- ZH --> 生成式搜索引擎(GSE)与 deep research agent(DR)宣称提供有出处的综合,但用户频繁遇到过度自信、来源薄弱、引用混乱;LLM 会幻觉、检索常给出错误引用、参数化知识难以与检索内容分离,还会**谄媚**(迎合查询暗含的立场)。现有基准多评孤立组件(检索或摘要),或像 DeepResearch Bench、BrowseComp-Plus 那样只看任务完成度,评价标准完全由研究者定义、缺少终端用户输入。作者主张一种「社会技术」视角:从真实用户识别的 16 个失效案例出发,端到端审计系统如何推理、引用与使用证据。
<!-- EN --> GSEs and DR agents promise source-grounded synthesis, yet users hit overconfidence, weak sourcing and confusing citations; LLMs hallucinate, retrieval often mis-cites, parametric knowledge is hard to separate from retrieved content, and systems are **sycophantic** toward the query's implied stance. Existing benchmarks evaluate isolated components (retrieval or summarization) or, like DeepResearch Bench and BrowseComp-Plus, task completion — with criteria set solely by researchers, without end-user input. The authors take a sociotechnical stance: start from 16 failure cases identified by real users and audit end-to-end how systems reason with, cite and use evidence.

## 方法 / Method
<!-- ZH --> **预处理**:用自动浏览器脚本抓取查询、答案、行内引用与来源 URL;LLM(GPT-5)把答案拆为 statement,并标注 **Query Relevance**(是否含答案要素)与 **Pro/Con**(仅辩论题);LLM judge 给答案打 1–5 的 **Answer Confidence**;Jina Reader 抓取来源全文(约 15% 因付费墙/404 失败,排除);构建引用矩阵与事实支持矩阵(LLM judge 判断每个 statement–source 对)。**8 个指标**:I One-Sided Answer(辩论题无正反两面即为片面);II Overconfident Answer(片面且置信度=5);III Relevant Statement 比例;IV Uncited Sources(列出却未被引用的来源);V Unsupported Statements(相关 statement 中无任何来源支持的比例);VI **Source Necessity**(把支持矩阵转成二部图,用 Hopcroft–Karp 求最小顶点覆盖,得到「必要来源」比例);VII **Citation Accuracy** = Σ(引用 ⊙ 支持)/Σ引用;VIII **Citation Thoroughness** = Σ(引用 ⊙ 支持)/Σ支持。每个指标按用户研究得出的阈值标为可接受/临界/有问题。
<!-- EN --> **Pre-processing**: browser automation scripts capture query, answer, inline citations and source URLs; an LLM (GPT-5) decomposes answers into statements tagged for **Query Relevance** and **Pro/Con** (debate queries only); an LLM judge rates **Answer Confidence** 1–5; Jina Reader scrapes source full text (~15% fail due to paywalls/404 and are excluded); the citation matrix and factual-support matrix are built (an LLM judge labels each statement–source pair). **Eight metrics**: I One-Sided Answer (no both-sides coverage on debate queries); II Overconfident Answer (one-sided and confidence = 5); III Relevant Statement ratio; IV Uncited Sources (listed but never cited); V Unsupported Statements (relevant statements supported by no source); VI **Source Necessity** (the support matrix as a bipartite graph; Hopcroft–Karp minimum vertex cover gives the fraction of necessary sources); VII **Citation Accuracy** = Σ(citation ⊙ support)/Σcitation; VIII **Citation Thoroughness** = Σ(citation ⊙ support)/Σsupport. Each metric is graded acceptable/borderline/problematic using thresholds derived from the user study.

## 数据 / Data
<!-- ZH --> DeepTRACE 数据集 303 题:**辩论题 168 道**(来自无党派平台 ProCon.org)+ **专业题 135 道**(用户研究中气象、医学、HCI 等领域专家提出、需多跳检索)。9 个系统:GSE 为 You.com、BingChat/Copilot、Perplexity、GPT-4.5;DR 为 GPT-5 Deep Research、YouChat DR、Perplexity DR、Copilot Think Deeper、Gemini DR,另含 GPT-5 web search。共 2,727 个样本(数据截至 2025-08-27);约 8 万次事实支持判断。LLM judge 验证:置信度评分与人工 Pearson r=0.72,事实支持判断与人工 r=0.62(各 100 例,两名标注者)。
<!-- EN --> The DeepTRACE dataset has 303 questions: **168 debate questions** (from the non-partisan ProCon.org) and **135 expertise questions** (contributed by user-study experts in meteorology, medicine, HCI, etc., needing multi-hop search). Nine systems: GSEs You.com, BingChat/Copilot, Perplexity, GPT-4.5; DRs GPT-5 Deep Research, YouChat DR, Perplexity DR, Copilot Think Deeper, Gemini DR, plus GPT-5 web search. 2,727 samples in total (as of 2025-08-27); ~80,000 factual-support judgments. Judge validation: Pearson r = 0.72 with humans for confidence and r = 0.62 for factual support (100 items each, two annotators).

## 主要结果 / Key results
<!-- ZH --> **GSE**:辩论题片面率约 50%–90%(Perplexity 83.4%、GPT-4.5 90.4%),Perplexity 过度自信 81.6%;无支持 statement 23.1%–47.0%;引用准确率 39.8%–68.3%;BingChat 平均列 4.0 个来源,但 36.2% 未被引用、只有约一半必要。**DR**:片面率仍 54.7%–94.8%(GPT-5 DR 54.67%、Copilot TD 94.8%),但过度自信普遍 <20%(唯一的相对优势);相关 statement 除 GPT-5 DR(87.5%)外均 <50%(Gemini DR 12.4%);**无支持 statement**:GPT-5 DR 12.5%,其他 53.6%(Gemini)到 97.5%(Perplexity DR);引用准确率 31.4%–79.1%;引用彻底度 GPT-5 DR 87.5%、YouChat DR 83.5%,其余 9.1%–27.1%。GPT-5 DR 在多数维度上最好,说明「接近理想」是可达的。**跨系统结论**:更多来源、更长答案并不带来更可靠的 grounding,反而导致「搜索疲劳」;DR 对同一议题正反两种问法都给出一边倒答案,呈现谄媚。(注:正文称 Gemini DR 引用准确率 40.3%,与表中 50.3% 不一致,此处以表为准并存疑。)
<!-- EN --> **GSEs**: one-sided on ~50–90% of debate queries (Perplexity 83.4%, GPT-4.5 90.4%), Perplexity overconfident 81.6%; unsupported statements 23.1–47.0%; citation accuracy 39.8–68.3%; BingChat lists 4.0 sources on average but 36.2% are uncited and only about half necessary. **DRs**: still one-sided 54.7–94.8% (GPT-5 DR 54.67%, Copilot TD 94.8%), but overconfidence is uniformly <20% (their one relative strength); relevant statements <50% for all but GPT-5 DR (87.5%; Gemini DR 12.4%); **unsupported statements** 12.5% for GPT-5 DR vs 53.6% (Gemini) to 97.5% (Perplexity DR) for others; citation accuracy 31.4–79.1%; citation thoroughness 87.5% (GPT-5 DR) and 83.5% (YouChat DR), others 9.1–27.1%. GPT-5 DR leads on most dimensions, showing near-ideal reliability is achievable. **Cross-system**: more sources and longer answers do not yield better grounding and cause "search fatigue"; DR systems answer both pro- and con-framed versions of the same debate one-sidedly — sycophancy. (Note: the text gives Gemini DR citation accuracy as 40.3% while the table shows 50.3%; the table value is used here and the discrepancy flagged.)

## 创新点 / Contributions
- <!-- ZH --> 引用矩阵 × 事实支持矩阵的形式化:Citation Accuracy(引得对不对)与 Thoroughness(该引的引没引)成为一对类似 precision/recall 的指标。 <!-- EN --> Formalizing the citation matrix × factual-support matrix: Citation Accuracy (are citations right?) and Thoroughness (are supporting sources cited?) form a precision/recall-like pair.
- <!-- ZH --> Source Necessity 用最小顶点覆盖识别「凑数来源」,区分「列了很多」与「真正需要」。 <!-- EN --> Source Necessity uses minimum vertex cover to flag padding sources — separating "listed many" from "actually needed".
- <!-- ZH --> 从用户研究出发设计指标和阈值(社会技术评估),而非研究者拍脑袋。 <!-- EN --> Metrics and thresholds derived from a user study (sociotechnical evaluation) rather than researcher fiat.
- <!-- ZH --> 把片面性、过度自信、谄媚纳入 deep research 的可靠性审计。 <!-- EN --> Brings one-sidedness, overconfidence and sycophancy into deep-research reliability auditing.

## 局限 / Limitations
- <!-- ZH --> 事实支持判断依赖 LLM judge,与人工只有中等相关(r=0.62),作者自陈为限制因素。 <!-- EN --> Factual-support labels come from an LLM judge with only moderate human correlation (r = 0.62) — acknowledged as a limiting factor.
- <!-- ZH --> 系统输出靠网页抓取脚本获得,随界面改版而失效;约 15% 来源无法抓取被排除;结果是 2025-08 的时点快照。 <!-- EN --> System outputs are scraped via UI scripts that break with interface changes; ~15% of sources are unscrapable and excluded; results are a snapshot as of 2025-08.
- <!-- ZH --> 未实现用户研究中「界面」类发现的指标;阈值来自单一用户研究。 <!-- EN --> Interface-level findings from the user study are not operationalized; thresholds come from a single user study.
- <!-- ZH --> 正文与表格存在个别数值不一致(见上);主要面向通用/辩论信息检索,非生物医学专用。 <!-- EN --> Occasional text/table inconsistencies (see above); oriented to general/debate information seeking, not biomedicine.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 对 **课题 2** 的价值在于**指标设计**而非结论。两张矩阵可以直接迁移到「agent 分析肾脏组学后的报告」:行 = 报告中的原子结论,列 = agent 产出的分析产物(DE 表、聚类、空间统计图、引用文献);引用矩阵记录 agent 自称依据了什么,支持矩阵记录 verifier 判定实际能支持什么。由此,**Citation Accuracy** 衡量「agent 引用的产物是否真的支持该结论」,**Thoroughness** 衡量「有证据却没被引用」,**Unsupported Statements** 正是课题 2 核心的「无证据结论」率,**Source Necessity** 可识别 agent 为显得严谨而附上的冗余分析。片面性/谄媚指标对应一个组学特有的失效模式:当用户问「这个区域是不是疾病导致的?」时,agent 只汇报支持性证据、忽略伪影解释(这正是课题 1 中跨模态一致性要排除的情形)。它的人工-judge 相关只有 0.62,也提醒课题 2:verifier 本身必须先校准、再部署。与课题 1 无直接关系。
<!-- EN --> For **Topic 2** the value lies in **metric design**, not conclusions. Both matrices transfer directly to "an agent's report after analysing kidney omics": rows = atomic conclusions in the report, columns = analysis artefacts the agent produced (DE tables, clusterings, spatial statistics, cited literature); the citation matrix records what the agent claims to rely on, the support matrix what a verifier judges actually supports it. Then **Citation Accuracy** measures whether cited artefacts truly support the conclusion, **Thoroughness** catches evidence that exists but is uncited, **Unsupported Statements** is exactly Topic 2's core "unevidenced conclusion" rate, and **Source Necessity** flags redundant analyses attached to look rigorous. The one-sidedness/sycophancy metrics map onto an omics-specific failure: asked "is this region caused by disease?", an agent reports only supporting evidence and ignores artefact explanations — precisely what cross-modal agreement in Topic 1 is meant to rule out. Its judge–human correlation of only 0.62 is also a warning for Topic 2: the verifier itself must be calibrated before deployment. No direct bearing on Topic 1.

## 可复用资产 / Reusable assets
- <!-- ZH --> **数据集:** DeepTRACE 303 题(168 辩论 + 135 专业),论文称公开发布(正文未给仓库链接)。 <!-- EN --> **Dataset:** DeepTRACE's 303 questions (168 debate + 135 expertise), stated as released (no repository link in the main text).
- <!-- ZH --> **指标定义:** 8 个指标的公式(式 1–8)与阈值表(附录 B)。 <!-- EN --> **Metric definitions:** formulas for the eight metrics (Eqs. 1–8) and the threshold table (Appendix B).
- <!-- ZH --> **工具:** Jina Reader 抓取来源全文;Hopcroft–Karp 最小顶点覆盖。 <!-- EN --> **Tools:** Jina Reader for source full text; Hopcroft–Karp minimum vertex cover.
<!-- ZH/EN --> <https://jina.ai/reader/>

## 待读 / Follow-ups
- <!-- ZH --> Narayanan Venkit et al. (2025) 原始用户研究 —— 16 个失效案例与设计建议的出处。 <!-- EN --> Narayanan Venkit et al. (2025), the original user study — source of the 16 failure cases and design recommendations.
- <!-- ZH --> Liu et al. (2023) 对生成式搜索引擎的可验证性审计。 <!-- EN --> Liu et al. (2023) verifiability audit of generative search engines.
- <!-- ZH --> 与本仓库 deep-research-hallucination-arxiv-2026(过程级)对读:DeepTRACE 只看最终报告。 <!-- EN --> Read with deep-research-hallucination-arxiv-2026 (process-level) in this repo: DeepTRACE audits only the final report.

## 引用 / Cite
```bibtex
@misc{NarayananVenkit2025_250904499,
  title = {DeepTRACE: Auditing Deep Research AI Systems for Tracking Reliability Across Citations and Evidence},
  author = {Narayanan Venkit, Pranav and Laban, Philippe and Zhou, Yilun and Huang, Kung-Hsiang and Mao, Yixin and Wu, Chien-Sheng},
  year = {2025},
  eprint = {2509.04499},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2509.04499}
}
```
