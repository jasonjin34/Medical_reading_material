# On the Limits of LLM-as-Judge for Scientific Novelty Assessment

> **Bibkey** `rq-bench-arxiv-2026` · **Venue** arXiv preprint (2026) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2606.12071>
> `status: complete` — 全文精读(arXiv HTML 全文,含附录表格)。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> RQ-Bench 用 746 篇近期 arXiv CS 论文重建出 1,434 个「作者锚定」的研究问题(RQ),拿来检验 LLM-as-judge 判断科研新颖性是否可靠:LLM 评委一致认为模型生成的 RQ 更新颖(「novelty mirage」),且并排比较时偏好被放大;而领域专家结论相反,更偏好作者原问题 —— 人机一致率低至 22%。
<!-- EN --> RQ-Bench reconstructs 1,434 "author-anchored" research questions (RQs) from 746 recent arXiv CS papers and uses them to test whether LLM-as-judge can reliably assess scientific novelty: LLM judges consistently rate model-generated RQs as more novel (a "novelty mirage"), and side-by-side comparison amplifies the preference — but domain experts reach the opposite conclusion and prefer the author RQs, with human–LLM agreement as low as 22%.

## 研究问题 / Problem
<!-- ZH --> 「AI scientist」流水线里,LLM 既生成想法又评判想法,整条链的可信度取决于 LLM-as-judge 是否可靠。完整 idea 的评估很难(要判方法、可行性、实验、影响),于是作者退一步研究更干净的上游对象 —— 研究问题(RQ):它先于方法,不承诺答案,且能与真实论文实际追问的问题对照。核心问题:LLM 评委对 RQ 新颖性的判断是否稳定?是否与人类专家一致?模型生成的 RQ 是否窄、是否被源论文绑死?
<!-- EN --> In "AI scientist" pipelines LLMs both generate and judge ideas, so the whole chain's credibility rests on LLM-as-judge being reliable. Full-idea evaluation is hard (method, feasibility, experiments, impact), so the authors step back to a cleaner upstream object — the research question (RQ): it precedes a method, commits to no answer, and can be compared against questions real papers actually pursued. Core questions: are LLM novelty judgments of RQs stable? Do they agree with experts? Are generated RQs narrow or source-bound?

## 方法 / Method
<!-- ZH --> **数据构建**:从 2025-01-01 至 2026-04-10 约 20 万篇 arXiv CS 论文中,按子领域取引用数前 10% 且有 LaTeX 源、被 Semantic Scholar 索引为会议/期刊发表的论文。用 qwen3.5-27b-thinking 结合引用次数、所在章节、局部上下文把每条引用分为 inspiration / competitor / 无关或经典引用,前两类视为「有影响的引用」;用 gemini-3.1-pro 抽取论文的 idea 与贡献;用 gemini-3-flash 对每条影响引用独立抽取「被作者识别并解决的 gap」;再由 gemini-3.1-pro 从 gap + 贡献合成作者锚定 RQ。校验:gemini-3.1-pro 对全文判定 98% RQ 被源论文回答,人工抽查 50 条 100% 通过。**评测**:给模型背景论文全文,要求先抽 gap 再写恰好 5 个 RQ;对每个 RQ 按 0–3 分评三项新颖性指标 —— originality、gap addressing、non-obviousness(不相加);另评两项「窄度」指标 —— source-boundedness(是否贴死某篇背景论文/数据集/指标/消融)与 diagnostic framing(是否只是诊断性分析)。两种打分设置:standalone(单独打分)与 comparative(参考 RQ 与 5 个生成 RQ 同上下文)。用「metric-level Pass@5」:5 个里最好的一个与参考 RQ 比,计 win/tie/lose;双评委(gemini-3.1-pro、deepseek-v4-pro,temperature 0、high thinking)都判赢才算 combined win。另有 0–4 分的 author-anchor overlap 诊断记忆/复现程度。
<!-- EN --> **Construction**: from ~200K arXiv CS papers (2025-01-01 to 2026-04-10), keep the top 10% by citations per subfield with LaTeX source and a conference/journal venue indexed by Semantic Scholar. qwen3.5-27b-thinking classifies each citation (using citation count, section, and local context) as inspiration / competitor / irrelevant-or-canonical; the first two count as influential. gemini-3.1-pro extracts ideas and contributions; gemini-3-flash extracts, per influential citation independently, the gaps the authors identified and addressed; gemini-3.1-pro then synthesises author-anchored RQs from gaps + contributions. Verification: gemini-3.1-pro judged 98% of RQs answered by the full source paper; humans approved 100% of 50 sampled. **Evaluation**: models get the background papers, must extract gaps and write exactly five RQs. Each RQ is scored 0–3 on three novelty metrics — originality, gap addressing, non-obviousness (not summed) — and two narrowness metrics — source-boundedness (stuck to one paper/dataset/metric/ablation) and diagnostic framing. Two settings: standalone (scored alone) and comparative (reference plus five generated RQs in one context). A "metric-level Pass@5" compares the best of five against the reference (win/tie/lose); a combined win requires both judges (gemini-3.1-pro, deepseek-v4-pro; temperature 0, high thinking). A 0–4 author-anchor overlap score diagnoses memorisation/recovery.

## 数据 / Data
<!-- ZH --> RQ-Bench:1,434 个 RQ,来自 746 篇源论文、13 个 arXiv CS 子领域;2,464 条 RQ–引用链接指向 1,375 篇被引论文;3,151 条 grounded gap。每篇源论文平均 1.92 个 RQ;每个 RQ 平均依赖 1.72 篇被引文献(52.4% 只依赖 1 篇);RQ 平均 24.7 词。被评模型 6 个:qwen3-30b-a3b-thinking-2507、gpt-oss-20b、gemma-4-31b-it、deepseek-v4-pro、gemini-3.1-pro、gpt-5.5。人工评估:来自 cs.CL / cs.LG 的 50 个样本,两位同领域专家盲评 non-obviousness。
<!-- EN --> RQ-Bench: 1,434 RQs from 746 source papers across 13 arXiv CS subfields; 2,464 RQ–citation links to 1,375 cited papers; 3,151 grounded gap statements. 1.92 RQs per source paper on average; 1.72 cited references per RQ (52.4% grounded in a single reference); mean RQ length 24.7 words. Six models evaluated: qwen3-30b-a3b-thinking-2507, gpt-oss-20b, gemma-4-31b-it, deepseek-v4-pro, gemini-3.1-pro, gpt-5.5. Human study: 50 samples from cs.CL / cs.LG, two same-field experts blind-rating non-obviousness.

## 主要结果 / Key results
<!-- ZH -->
- **Author-anchor overlap 很低**:所有模型都在 1.0–1.33 区间(gpt-5.5 最高 1.33),即「同一大方向、不同问题」—— 模型主要在生成替代问题,而非复现作者问题(也说明不是记忆)。
- **Standalone**:几乎所有模型 Best@5 分数在三项上都高于参考 RQ(如 gemini 评委下 gpt-5.5 non-obviousness 1.98 vs 参考 1.41),但 tie 很多;双评委 combined 下 gpt-5.5 的严格胜率 non-obviousness 仅 27.2%、originality 38.4%。
- **Comparative 放大偏好**:gpt-5.5 combined non-obviousness 胜率从 27.2% 升到 49.1%,tie 从 59.1% 降到 36.8%;单 gemini 评委下 gpt-5.5 胜率达 non-obv 79.3%、orig 74.0%、gap 88.9%。
- **人机严重分歧**(50 样本,comparative non-obviousness,gpt-5.5 vs 参考):专家 1 判参考赢 78%、专家 2 判 56%;而 gemini-3.1-pro 判 gpt-5.5 赢 82%、deepseek-v4-pro 判 52%。专家–专家一致 60%、LLM–LLM 一致 52%,专家–LLM 一致仅 22–40%。
- **窄度是 LLM 漏掉的维度**:双评委 combined source-boundedness 参考 RQ 0.47,gemini-3.1-pro 0.90、gpt-5.5 1.17;gpt-5.5 对参考的 lose 率 standalone 71.7%、comparative 85.4%。显式让 LLM 判 source-boundedness 时,结果与专家的 non-obviousness 判断一致率达 72–76%。语义相似度(Qwen3-Embedding-4B、all-mpnet-base-v2)则捕捉不到窄度 —— 反直觉地,参考 RQ 与背景论文的相似度反而更高。
- **改 prompt 的权衡**:去掉约束性指令后 gemini-3.1-pro 的 source-boundedness 从 1.00 降到 0.47(与参考持平),但 LLM 评的 non-obviousness / originality 同时下降;专家仍偏好参考 RQ(62% / 56%),专家–评委一致仅 30–40%。结论:LLM 评出的「新颖」与「窄」混在一起,方向与人类相反。
<!-- EN -->
- **Low author-anchor overlap**: all models fall in 1.0–1.33 (gpt-5.5 highest at 1.33), i.e. "same broad topic, different question" — models generate alternatives rather than recovering the author question (and are not simply memorising).
- **Standalone**: nearly all models' Best@5 scores exceed the reference on all three metrics (e.g. gemini judge: gpt-5.5 non-obviousness 1.98 vs reference 1.41), but ties dominate; under the two-judge combined rule gpt-5.5's strict win rate is only 27.2% on non-obviousness and 38.4% on originality.
- **Comparative amplifies preference**: gpt-5.5 combined non-obviousness win rate jumps from 27.2% to 49.1% and ties fall from 59.1% to 36.8%; with the gemini judge alone gpt-5.5 wins 79.3% (non-obv), 74.0% (orig), 88.9% (gap).
- **Sharp human–LLM disagreement** (50 samples, comparative non-obviousness, gpt-5.5 vs reference): Expert 1 picks the reference 78%, Expert 2 56%; gemini-3.1-pro picks gpt-5.5 82%, deepseek-v4-pro 52%. Expert–expert agreement 60%, LLM–LLM 52%, expert–LLM only 22–40%.
- **Narrowness is what judges miss**: two-judge combined source-boundedness is 0.47 for the reference vs 0.90 (gemini-3.1-pro) and 1.17 (gpt-5.5); gpt-5.5 loses to the reference 71.7% standalone and 85.4% comparative. When LLMs are explicitly asked to rate source-boundedness, their verdicts agree with expert non-obviousness judgments 72–76% of the time. Embedding similarity (Qwen3-Embedding-4B, all-mpnet-base-v2) does not capture narrowness — counter-intuitively, reference RQs are *more* similar to background papers.
- **Prompt trade-off**: removing constraining instructions lowers gemini-3.1-pro's source-boundedness from 1.00 to 0.47 (matching the reference), but LLM-judged non-obviousness/originality drop too; experts still prefer the reference (62% / 56%) and expert–judge agreement stays at 30–40%. LLM-judged "novelty" is conflated with narrowness, in the opposite direction to humans.

## 创新点 / Contributions
- <!-- ZH --> 把新颖性评估移到更干净的上游对象(RQ),并用真实论文重建「作者锚定」参考点,而非把它当唯一正确答案。 <!-- EN --> Moves novelty evaluation to a cleaner upstream object (the RQ) and reconstructs author-anchored reference points from real papers — explicitly not as the only valid answer.
- <!-- ZH --> 系统对比 standalone vs comparative 两种评判格式,量化出 comparative 会系统性放大对生成内容的偏好。 <!-- EN --> Systematically contrasts standalone vs comparative judging and quantifies how comparative formats amplify preference for generated content.
- <!-- ZH --> 用盲评专家实验揭示「novelty mirage」:LLM 与专家方向相反。 <!-- EN --> Uses a blinded expert study to expose the "novelty mirage": LLM judges and experts point in opposite directions.
- <!-- ZH --> 提出 **scope/narrowness(source-boundedness)** 作为新颖性评估的一等维度,并证明它与专家 non-obviousness 高度对齐,而语义相似度做不到。 <!-- EN --> Proposes **scope/narrowness (source-boundedness)** as a first-class novelty dimension, showing it aligns with expert non-obviousness where embedding similarity does not.

## 局限 / Limitations
- <!-- ZH --> 只覆盖近期 arXiv CS 论文,能否推广到生物医学等其他学科未知。 <!-- EN --> Only recent arXiv CS papers; transfer to biomedicine or other sciences is untested.
- <!-- ZH --> 人工评估规模小:50 个样本、两位专家、只评 non-obviousness 一项;专家之间一致率也只有 54–60%。 <!-- EN --> Small human study: 50 samples, two experts, non-obviousness only; expert–expert agreement itself is only 54–60%.
- <!-- ZH --> 数据集构建本身依赖 LLM(qwen / gemini)抽取引用、gap 与 RQ,且评委之一 gemini-3.1-pro 也是构建模型和被评模型之一,存在潜在自偏好。 <!-- EN --> Construction itself relies on LLMs (qwen / gemini) to extract citations, gaps and RQs, and gemini-3.1-pro is simultaneously a builder, a judge and an evaluated model — a potential self-preference confound.
- <!-- ZH --> 使用近期论文而非严格未见数据,只能用 overlap 分数间接诊断污染。 <!-- EN --> Uses recent rather than strictly unseen papers; contamination is diagnosed only indirectly via the overlap score.
- <!-- ZH --> 文中未给出代码/数据下载链接。 <!-- EN --> No code/data release link is given in the paper.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 这是一篇「评委本身不可信」的警示论文,直接落在 **课题 2(可信生物医学 agent)** 的验证器设计上。课题 2 计划用一个校准过的 verifier 检查分析肾脏组学的 agent 所提出的论断;如果 verifier 是 LLM,本文给出三个必须吸收的教训:**(1) 评判格式会改变结论** —— standalone 与 comparative 的胜率可以差 20+ 个百分点,所以 KidneyAnomalyBench / 课题 2 的评测协议必须固定格式并报告格式敏感性;**(2) 需要多评委 + 一致性报告**,并且至少一小部分由专家盲评做锚定(本文 50 样本的设计可直接借鉴为最小人类校准集);**(3) 存在 LLM 系统性漏掉、但专家看重的维度** —— 在这里是「窄度/源绑定」。对 detect → model → revert 主链,类似的隐患在 revert 阶段:agent 提名的「回正基因/扰动」如果只是对某篇源论文或某个已知通路的小修小补(source-bound),LLM 评委可能仍打高分。把「是否只是复述输入证据」作为显式检查项,是课题 2 失败分类(omics-specific failure taxonomy)里可以新增的一类。课题 1 方面关系较弱,但 KidneyAnomalyBench 若用 LLM 辅助判定「异常是否新颖/有生物学意义」,同样要以专家标注为准、把 LLM 判定当作待校准的信号。
<!-- EN --> A cautionary "the judge itself is unreliable" paper that lands directly on **Topic 2 (trustworthy biomedical agents)** verifier design. Topic 2 plans a calibrated verifier for claims made by agents analysing kidney omics; if that verifier is an LLM, three lessons apply: **(1) judging format changes the verdict** — standalone vs comparative win rates differ by 20+ points, so the KidneyAnomalyBench / Topic 2 protocol must fix the format and report format sensitivity; **(2) use multiple judges with agreement reporting**, anchored by a small blinded expert set (the 50-sample design is a usable minimal human-calibration template); **(3) there are dimensions LLM judges systematically miss but experts weigh** — here, narrowness/source-boundedness. On the detect → model → revert chain the analogous risk sits in the revert step: a nominated "reverting gene/perturbation" that is merely a tweak of one source paper or a known pathway (source-bound) may still receive high LLM scores. "Does the claim merely restate its input evidence?" is a candidate new class for Topic 2's omics-specific failure taxonomy. Relation to Topic 1 is weaker, but if KidneyAnomalyBench uses an LLM to judge whether an anomaly is novel or biologically meaningful, expert labels must remain ground truth and LLM verdicts treated as signals to calibrate.

## 可复用资产 / Reusable assets
- <!-- ZH --> **评测协议:** metric-level Pass@5、per-judge 与 combined-judge 的 win/tie/lose 定义;standalone vs comparative 双格式。 <!-- EN --> **Eval protocol:** metric-level Pass@5 with per-judge and combined-judge win/tie/lose definitions; standalone vs comparative formats.
- <!-- ZH --> **评分量表:** 0–3 分的 originality / gap-addressing / non-obviousness 与 source-boundedness / diagnostic framing 量表(附录 A.1–A.2),以及 0–4 分 author-anchor overlap 量表。 <!-- EN --> **Rubrics:** 0–3 rubrics for originality / gap-addressing / non-obviousness and source-boundedness / diagnostic framing (Appendix A.1–A.2), plus the 0–4 author-anchor overlap rubric.
- <!-- ZH --> **数据构建流水线:** 「影响引用识别 → 贡献抽取 → 逐引用 gap 抽取 → RQ 合成」可迁移到生物医学文献。论文正文未给出代码或数据链接。 <!-- EN --> **Construction pipeline:** "influential-citation detection → contribution extraction → per-citation gap extraction → RQ synthesis" is transferable to biomedical literature. The paper gives no code or data link.
<!-- ZH/EN --> <https://arxiv.org/abs/2606.12071>

## 待读 / Follow-ups
- <!-- ZH --> Si et al. 的 ideation 与 execution 研究(本仓库 `ideation-execution-gap-arxiv-2025`):专家评审 vs 执行结果。 <!-- EN --> Si et al.'s ideation and execution studies (this repo: `ideation-execution-gap-arxiv-2025`) — expert review vs execution outcomes.
- <!-- ZH --> `llm-judge-healthcare-arxiv-2026`:医疗场景下 LLM-as-judge 与人类一致性的综述证据。 <!-- EN --> `llm-judge-healthcare-arxiv-2026` — scoping evidence on LLM-as-judge human alignment in healthcare.
- <!-- ZH --> IdeaBench、ResearchBench、LiveIdeaBench 等下游 idea 基准,看它们的评委是否也有同样偏差。 <!-- EN --> Downstream idea benchmarks (IdeaBench, ResearchBench, LiveIdeaBench) — do their judges share the same bias?

## 引用 / Cite
```bibtex
@misc{rq-bench-arxiv-2026, title={On the Limits of LLM-as-Judge for Scientific Novelty Assessment}, author={Sinhahajari, Soumitra and Majumder, Navonil and Poria, Soujanya}, year={2026}, eprint={2606.12071}, archivePrefix={arXiv}, primaryClass={cs.DL}, url={https://arxiv.org/abs/2606.12071}, doi={10.48550/arXiv.2606.12071} }
```
