# Benchmarking large language models for biomedical natural language processing applications and recommendations

> **Bibkey** `Chen_2025` · **Venue** Nature Communications (2025) · **Category** other · **Relevance** medium · **Access** open
> **Link** <https://doi.org/10.1038/s41467-025-56989-2>
> `status: abstract-only` — 精读基于摘要与公开落地页;把 PDF 放到本文件夹的 `source.pdf` 后可补全全文精读。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> 在 12 个 BioNLP 基准、6 类应用上系统评测四个 LLM(GPT 与 LLaMA 代表)的 zero-shot / few-shot / 微调表现,并与 BERT、BART 的传统微调对比,结论是:**多数任务上传统微调仍胜过零样本或少样本 LLM**,GPT-4 只在医学问答等推理型任务上占优,开源 LLM 必须微调才能追平;同时系统记录了信息缺失与幻觉问题。
<!-- EN --> A systematic evaluation of four LLMs (GPT and LLaMA representatives) across 12 BioNLP benchmarks and six applications — zero-shot, few-shot and fine-tuned — against traditionally fine-tuned BERT/BART. The verdict: **traditional fine-tuning still beats zero- and few-shot LLMs on most tasks**; GPT-4 leads only on reasoning-type tasks such as medical QA; open-source LLMs need fine-tuning to close the gap. Missing information and hallucination are documented systematically.

## 研究问题 / Problem
<!-- ZH --> 生物医学文献增长使人工知识整理难以为继,BioNLP 负责自动化这件事。LLM 在通用领域表现亮眼,但**在 BioNLP 任务上到底行不行并不清楚** —— 缺基准、缺实用指南,也缺对成本与失败模式的量化。
<!-- EN --> The growth of biomedical literature outstrips manual curation, and BioNLP automates it. LLMs shine in general domains, but **their actual effectiveness on BioNLP tasks is unclear** — benchmarks, practical guidelines, and quantification of cost and failure modes are all missing.

## 方法 / Method
<!-- ZH --> 对四个 LLM(GPT 与 LLaMA 系代表)在三种使用模式下评测:zero-shot、few-shot、微调;基线是 BERT / BART 的传统微调。除了准确率,还专门检查**不一致性、信息缺失、幻觉**三类失败模式,并做成本分析 —— 这三项使它不只是排行榜,而是一份使用建议。
<!-- EN --> Four LLMs (GPT and LLaMA representatives) are evaluated in three usage modes — zero-shot, few-shot and fine-tuned — against traditionally fine-tuned BERT/BART baselines. Beyond accuracy, the study explicitly examines three failure modes — **inconsistency, missing information and hallucination** — and performs a cost analysis, which is what turns it from a leaderboard into a set of recommendations.

## 数据 / Data
<!-- ZH --> 12 个 BioNLP 基准,覆盖 6 类应用(命名实体识别、关系抽取、文本分类、问答、摘要等生物医学 NLP 常见任务族)。
<!-- EN --> 12 BioNLP benchmarks spanning six application families (named-entity recognition, relation extraction, text classification, question answering, summarization and related biomedical NLP tasks).

## 主要结果 / Key results
<!-- ZH --> ① **传统微调在多数任务上胜过零样本/少样本 LLM** —— 领域内小模型 + 标注数据仍是强基线。② 闭源 LLM(GPT-4)在**推理型任务**(如医学问答)上表现突出。③ 开源 LLM 仍需微调才能补上差距。④ LLM 输出中普遍存在**信息缺失与幻觉**。⑤ 成本分析提示:LLM 方案在很多任务上性价比并不占优。
<!-- EN --> ① **Traditional fine-tuning outperforms zero-/few-shot LLMs on most tasks** — a domain-specific small model plus labelled data remains a strong baseline. ② Closed-source LLMs (GPT-4) excel on **reasoning-type tasks** such as medical QA. ③ Open-source LLMs still require fine-tuning to close the gap. ④ **Missing information and hallucination** appear throughout LLM outputs. ⑤ Cost analysis indicates LLM-based solutions are often not the economical choice.

## 创新点 / Contributions
- <!-- ZH --> 覆盖广的 BioNLP 系统评测(12 基准 × 6 应用 × 3 使用模式),并给出实用建议而非只报分数。 <!-- EN --> A broad systematic BioNLP evaluation (12 benchmarks × 6 applications × 3 usage modes) that yields practical recommendations, not just scores.
- <!-- ZH --> 把**幻觉与信息缺失**作为一等评测对象显式量化。 <!-- EN --> Elevates **hallucination and missing information** to first-class, explicitly quantified evaluation targets.
- <!-- ZH --> 纳入成本分析,把「能不能用」和「值不值得用」分开回答。 <!-- EN --> Includes cost analysis, separating "does it work" from "is it worth it".
- <!-- ZH --> 明确保留传统微调基线,给出诚实的对照。 <!-- EN --> Keeps traditional fine-tuning baselines in the comparison, providing an honest control.

## 局限 / Limitations
- <!-- ZH --> 模型迭代极快,2025 年的具体结论(尤其闭源模型分数)会迅速过时。 <!-- EN --> Models move fast; the 2025-specific conclusions (especially closed-model scores) date quickly.
- <!-- ZH --> 只覆盖文本模态的 BioNLP 任务,不涉及影像或组学。 <!-- EN --> Covers text-only BioNLP tasks; no imaging or omics.
- <!-- ZH --> 幻觉与信息缺失的判定标准依赖人工与任务定义,跨任务可比性有限。 <!-- EN --> Hallucination and missing-information judgments depend on human assessment and task definitions, limiting cross-task comparability.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 与主链无内容交集,但它提供了本方向**反复引用的一个论据**:在有标注的专业任务上,**领域内微调的小模型仍能打败通用大模型** —— 换句话说,瓶颈常在数据与任务定义,而不在模型容量。这与 PathBench 在影像侧得到的「规模不预测性能」是同一结论的两个侧面,可以互相印证。方法论上可迁移的是它把**幻觉与信息缺失做成显式评测维度**的做法:如果之后要评估一个会引用证据的 agent,「漏了什么」和「编了什么」必须和准确率并列成为指标,而不是附注。
<!-- EN --> No topical overlap with the main chain, but it supplies **an argument this direction keeps needing**: on annotated specialist tasks, a **domain fine-tuned small model still beats a general large one** — i.e. the bottleneck is usually data and task definition, not model capacity. That is the same conclusion PathBench reaches on the imaging side ("scale does not predict performance"), and the two corroborate each other. Methodologically transferable: its treatment of **hallucination and missing information as explicit evaluation dimensions**. If we later evaluate an evidence-citing agent, "what it omitted" and "what it fabricated" must sit alongside accuracy as metrics, not in a footnote.

## 可复用资产 / Reusable assets
- <!-- ZH --> **评测协议:** 12 个 BioNLP 基准 × zero-shot / few-shot / fine-tune 三模式 × 传统微调基线,外加幻觉、信息缺失与成本三项分析维度。 <!-- EN --> **Eval protocol:** 12 BioNLP benchmarks × zero-shot / few-shot / fine-tune × traditional fine-tuning baselines, plus hallucination, missing-information and cost as analysis dimensions.
- <!-- ZH --> **论文(开放获取):** <!-- EN --> **Paper (open access):**
<!-- ZH/EN --> <https://doi.org/10.1038/s41467-025-56989-2>

## 待读 / Follow-ups
- <!-- ZH --> 取全文,记下 12 个基准的具体名单与幻觉判定标准,便于日后设计生物医学 agent 的失败模式指标。 <!-- EN --> Get the full text for the exact list of 12 benchmarks and the hallucination criteria, useful when designing failure-mode metrics for biomedical agents.
- <!-- ZH --> 与本仓库的 DeepEvidence 条目对读:后者用 agent 架构提升证据类任务表现,本篇则给出「不用 agent 时的地板」。 <!-- EN --> Read alongside this repo's DeepEvidence entry: that one raises evidence-task performance with agent architecture, this one establishes the floor without agents.

## 引用 / Cite
```bibtex
@article{Chen_2025, title={Benchmarking large language models for biomedical natural language processing applications and recommendations}, volume={16}, ISSN={2041-1723}, url={http://dx.doi.org/10.1038/s41467-025-56989-2}, DOI={10.1038/s41467-025-56989-2}, number={1}, journal={Nature Communications}, publisher={Springer Science and Business Media LLC}, author={Chen, Qingyu and Hu, Yan and Peng, Xueqing and Xie, Qianqian and Jin, Qiao and Gilson, Aidan and Singer, Maxwell B. and Ai, Xuguang and Lai, Po-Ting and Wang, Zhizheng and Keloth, Vipina K. and Raja, Kalpana and Huang, Jimin and He, Huan and Lin, Fongci and Du, Jingcheng and Zhang, Rui and Zheng, W. Jim and Adelman, Ron A. and Lu, Zhiyong and Xu, Hua}, year={2025}, month=Apr }
```
