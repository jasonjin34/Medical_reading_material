# MedRAGChecker: Claim-Level Verification for Biomedical Retrieval-Augmented Generation

> **Bibkey** `Ji2026_260106519` · **Venue** arXiv preprint (2026) · **Category** agents · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2601.06519>
> `status: complete` — 基于 arXiv HTML 全文精读(正文 + Limitations;附录未逐条核对)。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> MedRAGChecker 把生物医学 RAG 的长答案拆成原子 claim(SPO 三元组),用「蒸馏出的 NLI 检查器 + 知识图谱(KG)一致性信号」逐条核验,并用 **selective gating** 只在「NLI 很确信蕴含、KG 很确信冲突」时才融合 KG —— 核心发现是 **KG 覆盖率决定 KG 是帮忙还是添乱**:覆盖率 62.7% 的 DRKG 把幻觉率推高到 34.2%,覆盖率 94.2% 的 BioPortal 把它压到 25.2%。
<!-- EN --> MedRAGChecker decomposes long-form biomedical RAG answers into atomic claims (SPO triples) and verifies each with a distilled NLI checker plus a knowledge-graph (KG) consistency signal, fusing them via **selective gating** only when NLI confidently entails while the KG confidently conflicts. The headline finding is that **KG coverage decides whether the KG helps or hurts**: DRKG (62.7% coverage) inflates the hallucination rate to 34.2%, while BioPortal (94.2% coverage) lowers it to 25.2%.

## 研究问题 / Problem
<!-- ZH --> 生物医学 RAG 的长答案里混着有支撑、证据不足、被证据反驳的 claim;整答案打分会掩盖个别但临床上危险的错误。标准做法把每条 claim 当 NLI 假设去对检索证据,但在生物医学里「文本上被蕴含」不等于「临床上正确」(例:检索段落没提 Reye 综合征,NLI 就会把「阿司匹林对病毒感染儿童安全」判为蕴含)。已有工作把 KG 加进来,却**默认 KG 只会有帮助** —— 作者指出这一假设不安全:KG 缺少相关实体对时会给出虚假的「矛盾」判决,而此前没人量化过 KG 覆盖率如何驱动核验质量。
<!-- EN --> Long-form biomedical RAG answers mix supported, under-evidenced and contradicted claims, and whole-answer scoring hides isolated but clinically dangerous errors. The standard approach treats each claim as an NLI hypothesis against retrieved evidence, but in biomedicine textual entailment is not clinical correctness (e.g. if retrieved passages omit Reye's syndrome, NLI entails "aspirin is safe for children with viral infections"). Prior work adds KGs under the **implicit assumption that a KG can only help**; the authors argue this is unsafe — a KG lacking the relevant entity pair produces spurious Contradict verdicts — and nobody had measured how KG coverage drives verification quality.

## 方法 / Method
<!-- ZH --> **(1) Claim 抽取**:GPT-4.1 作 teacher 把答案拆成 SPO 三元组,再 SFT 蒸馏到 Med42-Llama3-8B 等小模型,推理时不调 teacher。**(2) 文本 NLI**:把 GPT-4.1 的三分类判决(Entail/Neutral/Contradict)蒸馏到 Meditron3-8B、Med-Qwen2-7B、Med42-Llama3-8B(LoRA),再做 **F1 加权集成**,让少数类(Contradict)专长的模型权重更大。**(3) KG 核验**:通用接口 = 实体链接 → 可信度打分 → 融合。DRKG(9.7 万实体、580 万边,药物重定位为主)用字符串匹配 + TransE 打分;BioPortal(SNOMED-CT、MeSH、NCIt、DOID、RxNorm 等多本体枢纽)用 Jaccard + SapBERT 余弦 + 同义词匹配链接,取直接属性(适应症/禁忌,0.9)、层级祖先(0.2–0.7)、LOOM 跨本体映射(0.8)三者最大值。KG 模块不调用 GPT-4.1,作为部分独立于 teacher 的外部锚点。**(4) 融合**:在 logit 空间加权融合 NLI 与 KG;**selective gating** 只在 NLI 高置信蕴含且 KG 高置信冲突时启用融合,否则退回 NLI。**指标**:Faithfulness、Hallucination rate、SafetyErr(KG 对齐的药–病、药–不良反应 claim 被判 Contradict 的比例),以及 decision-flip(NLI-only 与融合判决不一致的 claim)。
<!-- EN --> **(1) Claim extraction**: a GPT-4.1 teacher decomposes answers into SPO triples; this is SFT-distilled into small models (e.g. Med42-Llama3-8B) so no teacher calls are made at inference. **(2) Textual NLI**: GPT-4.1 three-way verdicts (Entail/Neutral/Contradict) are distilled (LoRA) into Meditron3-8B, Med-Qwen2-7B and Med42-Llama3-8B, combined by an **F1-weighted ensemble** so minority-class (Contradict) specialists count more. **(3) KG verification**: a generic interface of entity linking → plausibility scoring → fusion. DRKG (97K entities, 5.8M edges, drug-repurposing-centric) uses string matching plus TransE scores; BioPortal (a multi-ontology hub: SNOMED-CT, MeSH, NCIt, DOID, RxNorm) links via Jaccard + SapBERT cosine + synonym match and scores by the max of direct property lookup (indication/contraindication, 0.9), hierarchical ancestors (0.2–0.7) and LOOM cross-ontology mappings (0.8). The KG module makes no GPT-4.1 calls — a partially teacher-independent anchor. **(4) Fusion**: logit-space weighted fusion of NLI and KG; **selective gating** applies fusion only when NLI is confident of entailment and the KG is confident of conflict, otherwise falls back to NLI. **Metrics**: Faithfulness, Hallucination rate, SafetyErr (fraction of KG-aligned drug–disease / drug–adverse-event claims labelled Contradict), and decision-flip claims (where NLI-only and fused verdicts differ).

## 数据 / Data
<!-- ZH --> 四个生物医学 QA 基准:PubMedQA、MedQuAD、LiveQA、MedRedQA;PubMed 检索的 RAG 流水线(固定检索设置);三个生成器 Meditron3-8B、Med-Qwen2-7B、Med42-Llama3-8B(PMC-LLaMA-13B 因每答案只抽出 1.19 条 claim、BERT-F1=45.7 而被移出主比较)。teacher 标注数据 80/10/10 划分。人工评估:100 题 × 3 生成器 × 2 标注者。
<!-- EN --> Four biomedical QA benchmarks: PubMedQA, MedQuAD, LiveQA, MedRedQA; a PubMed-based RAG pipeline with fixed retrieval settings; three generators — Meditron3-8B, Med-Qwen2-7B, Med42-Llama3-8B (PMC-LLaMA-13B excluded from the main comparison for degenerate extraction: 1.19 claims/answer, BERT-F1 45.7). Teacher-labelled data split 80/10/10. Human study: 100 questions × 3 generators × 2 annotators.

## 主要结果 / Key results
<!-- ZH --> **覆盖率决定 KG 效果**:两种 KG 都提升 faithfulness(DRKG +2.6pp,BioPortal +3.4pp),但对幻觉率方向相反 —— DRKG 把幻觉率从 29.2% 推到 34.2%(+5.0pp),BioPortal 降到 25.2%(−4.0pp),9.0pp 的差距对应 31.5pp 的覆盖率差(62.7% vs 94.2%)。例:Meditron3-8B 下 DRKG 让幻觉率从 14.6% 近乎翻倍到 27.3%,BioPortal 保持 13.5%。DRKG 在 PubMedQA 上只覆盖 45% 的 claim、LiveQA 上 78%;BioPortal 各数据集约 93%。SafetyErr 在两种 KG 下都下降 —— 失败只来自**未覆盖 claim 泄漏的弱信号**。**人类对齐**:在 decision-flip claim 上,人类与 BioPortal 融合判决一致 69.8%,与 NLI-only 一致 63.4%;macro-F1 59.2→64.7。**Gating**:平均只在 12.3% 的 KG-linked claim 上触发(9.4%–14.7%);同一 KG 下 gating 让幻觉率再降 0.7–2.4pp。KG 在 72% 的药–不良反应 flip、68% 的药–病治疗 flip 上正确推翻 NLI,但在 23% 的生活方式类 claim 上因虚假层级匹配而出错。**蒸馏**:学生集成 3 分类 macro-F1 60.5;每分钟 180 条 claim(单张 A100),约比 GPT-4.1 teacher 便宜 50×、快 7×。**对比通用评估器**:与 RAGAS、RAGChecker faithfulness 相当(如 LiveQA 82.5 vs 74.9 vs 70.8),但多出 claim 级与安全关键诊断。
<!-- EN --> **Coverage drives KG effect**: both KGs raise faithfulness (DRKG +2.6pp, BioPortal +3.4pp) but move hallucination in opposite directions — DRKG raises it from 29.2% to 34.2% (+5.0pp), BioPortal lowers it to 25.2% (−4.0pp); the 9.0pp swing tracks a 31.5pp coverage gap (62.7% vs 94.2%). E.g. for Meditron3-8B, DRKG nearly doubles hallucination (14.6% → 27.3%) while BioPortal keeps it at 13.5%. DRKG covers only 45% of PubMedQA claims vs 78% on LiveQA; BioPortal ~93% everywhere. SafetyErr drops under both KGs — failures come only from **weak signals leaking from uncovered claims**. **Human alignment**: on decision-flip claims, annotators agree with BioPortal-fused verdicts 69.8% vs 63.4% for NLI-only; macro-F1 59.2 → 64.7. **Gating** fires on 12.3% of KG-linked claims on average (9.4–14.7%) and cuts hallucination a further 0.7–2.4pp at fixed KG. The KG correctly overrides NLI on 72% of drug–adverse-event flips and 68% of drug–disease-treatment flips, but hurts 23% of lifestyle claims via spurious hierarchical matches. **Distillation**: the student ensemble reaches 3-way macro-F1 60.5 and runs 180 claims/min on one A100 — ~50× cheaper and 7× faster than the GPT-4.1 teacher. **Versus generic evaluators**: faithfulness comparable to RAGAS and RAGChecker (e.g. LiveQA 82.5 vs 74.9 vs 70.8), plus claim-level and safety-critical diagnostics they lack.

## 创新点 / Contributions
- <!-- ZH --> 把「KG 一定有帮助」这一隐含假设变成可测量的问题:**同一套链接/打分/融合机制、只换 KG**,隔离出覆盖率这个主导变量。 <!-- EN --> Turns the implicit "a KG can only help" assumption into a measurable question: **identical linking/scoring/fusion, swap only the KG**, isolating coverage as the dominant variable.
- <!-- ZH --> Selective gating:非对称融合规则,只在误报代价最大的区间(NLI 确信蕴含 × KG 确信冲突)让外部结构知识介入。 <!-- EN --> Selective gating: an asymmetric fusion rule that lets structured knowledge intervene only in the regime where a false signal does most damage (confident NLI entailment × confident KG conflict).
- <!-- ZH --> 把 GPT-4.1 teacher 蒸馏成可本地部署的 7–8B 检查器集成,API-free。 <!-- EN --> Distils a GPT-4.1 teacher into a locally deployable 7–8B checker ensemble — API-free.
- <!-- ZH --> SafetyErr 与 decision-flip 指标:把「临床危险错误」从「一般不准确」中分离出来。 <!-- EN --> SafetyErr and decision-flip metrics separate clinically dangerous errors from benign inaccuracies.

## 局限 / Limitations
- <!-- ZH --> claim 抽取与主 NLI 信号都来自 GPT-4.1,**评估存在部分循环**;absolute 数值在 MedRedQA 上随 teacher 而变(teacher 间一致性低)。 <!-- EN --> Claim extraction and the main NLI signal derive from GPT-4.1, so **evaluation is partly circular**; absolute values on MedRedQA are teacher-conditional (low inter-teacher agreement).
- <!-- ZH --> Contradict 是少数类,微妙矛盾仍可能漏检;学生集成 F1-C 仅 41.3。 <!-- EN --> Contradict is a minority class and subtle contradictions can be missed; the ensemble's F1-C is only 41.3.
- <!-- ZH --> 即使 BioPortal 也不覆盖所有实体/关系;SapBERT + API 搜索的实体链接对罕见实体、复杂改写、多跳 claim 会失败。 <!-- EN --> Even BioPortal does not cover everything; SapBERT + API entity linking fails on rare entities, paraphrases and multi-hop claims.
- <!-- ZH --> 人工评估规模小(100 题 × 3 × 2),整体正确性评分的标注者一致性低。 <!-- EN --> Small human study (100 × 3 × 2); low inter-annotator agreement on holistic correctness ratings.
- <!-- ZH --> 只处理文本 QA,未涉及组学数据或数值型结论。 <!-- EN --> Text QA only — no omics data or numerical conclusions.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 这是 **Agent 可信度课题(可信生物医学 agent 的 claim-to-evidence 核验)最直接的方法模板**。它的流水线 —— 原子 claim → 文本 NLI → 结构化知识一致性 → 有条件融合 —— 可以几乎原样迁移到「agent 分析肾脏组学后写出的结论」:把「基因 X 在 PT 细胞的损伤状态中上调」拆成 SPO,再对照 (a) agent 自己的分析产物(差异表达表、Xenium 空间统计)做「数据蕴含」检查,(b) 对照 KPMP/Lake 图谱、GO/Reactome 做「先验知识一致性」检查。**最有价值的是覆盖率教训**:肾脏专用知识(细胞亚型、损伤状态、snATAC 峰–基因连接)在通用 KG 里覆盖很差,照搬 KG 融合会像 DRKG 一样**制造虚假矛盾、抬高幻觉率** —— 所以 Agent 可信度课题的校准 verifier 必须显式建模「知识源是否覆盖该 claim」,对未覆盖 claim 退回数据级证据,这正是 selective gating 的思路。它的 SafetyErr(只统计安全关键关系)也启发我们为组学 failure taxonomy 定义「结论翻转型错误」(例如把方向、细胞类型或扰动效应弄反)并单独计分。对伪影注入课题的启示是间接的:「覆盖率不足的参考会把正常判成异常」与用不完整健康参考图谱做异常检测是同一个失效模式。
<!-- EN --> This is the **most direct method template for the agent-trustworthiness topic (claim-to-evidence verification of trustworthy biomedical agents)**. Its pipeline — atomic claims → textual NLI → structured-knowledge consistency → conditional fusion — ports almost unchanged to "conclusions an agent writes after analysing kidney omics": decompose "gene X is up-regulated in injured PT cells" into SPO, then check (a) **data entailment** against the agent's own artefacts (DE tables, Xenium spatial statistics) and (b) **prior-knowledge consistency** against KPMP/Lake atlases and GO/Reactome. **The coverage lesson is the most valuable part**: kidney-specific knowledge (cell subtypes, injury states, snATAC peak–gene links) is poorly covered by generic KGs, so naive KG fusion would, like DRKG, **manufacture false contradictions and inflate hallucination**. The agent-trustworthiness topic's calibrated verifier must therefore model "does the knowledge source cover this claim?" explicitly and fall back to data-level evidence when it does not — exactly the selective-gating idea. Its SafetyErr (scoring only safety-critical relations) also suggests defining "conclusion-flipping errors" in the omics failure taxonomy (wrong direction, wrong cell type, wrong perturbation effect) and scoring them separately. For the artifact-injection topic the lesson is indirect: "an under-covering reference turns normal into anomalous" is the same failure mode as anomaly detection against an incomplete healthy reference atlas.

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码 / prompts / 诊断输出:** <!-- EN --> **Code, prompts, diagnostics:**
<!-- ZH/EN --> <https://github.com/JoyDajunSpaceCraft/MedicalRagChecker>
- <!-- ZH --> **KG 后端:** DRKG(<https://github.com/gnn4dr/DRKG/>)与 BioPortal 公共 API;SapBERT 实体链接。 <!-- EN --> **KG back-ends:** DRKG (<https://github.com/gnn4dr/DRKG/>) and the public BioPortal API; SapBERT entity linking.
- <!-- ZH --> **评测协议:** NLI-only vs +KG(vanilla)vs +KG(gated)三设置对照;decision-flip 人工一致性作为「融合是否真有用」的检验。 <!-- EN --> **Eval protocol:** NLI-only vs +KG (vanilla) vs +KG (gated); human agreement on decision-flip claims as the test of whether fusion genuinely helps.
- <!-- ZH --> **基线:** RAGAS、RAGChecker。 <!-- EN --> **Baselines:** RAGAS, RAGChecker.

## 待读 / Follow-ups
- <!-- ZH --> RAGChecker(Ru et al., 2024)与 FActScore(Min et al., 2023)—— claim 级评估的源头。 <!-- EN --> RAGChecker (Ru et al., 2024) and FActScore (Min et al., 2023) — the origins of claim-level evaluation.
- <!-- ZH --> HealthFC(Vladika et al., 2024)临床事实核查基线。 <!-- EN --> HealthFC (Vladika et al., 2024) clinical fact-checking baseline.
- <!-- ZH --> 附录 E(teacher 敏感性)与附录 G(按关系类型分层的 flip 分析)—— 设计 Agent 可信度课题 verifier 校准实验时需细读。 <!-- EN --> Appendix E (teacher sensitivity) and Appendix G (flip analysis by relation type) — read closely when designing the agent-trustworthiness topic verifier calibration.

## 引用 / Cite
```bibtex
@misc{Ji2026_260106519,
  title = {MedRAGChecker: Claim-Level Verification for Biomedical Retrieval-Augmented Generation},
  author = {Yuelyu Ji and Min Gu Kwak and Hang Zhang and Xizhi Wu and Chenyu Li and Yanshan Wang},
  year = {2026},
  eprint = {2601.06519},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2601.06519}
}
```
