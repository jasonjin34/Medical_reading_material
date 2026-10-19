# SemNovel – A new approach to detecting semantic novelty of biomedical publications using embeddings of large language models

> **Bibkey** `Peng_2025` · **Venue** Journal of Biomedical Informatics (2025) · **Category** other · **Relevance** medium · **Access** open
> **Link** <https://doi.org/10.1016/j.jbi.2025.104952>
> `status: abstract-only` — 精读基于摘要与公开落地页;把 PDF 放到本文件夹的 `source.pdf` 后可补全全文精读。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> SemNovel 用 LLM embedding 把整个 PubMed 投影成一个「语义宇宙」,以一篇论文到既往文献的距离作为**语义新颖性分数**,该分数与未来引用量正相关,并能把诺奖级研究从普通论文里挑出来。
<!-- EN --> SemNovel projects all of PubMed into a "semantic universe" using LLM embeddings and scores a paper's **semantic novelty** by its distance from prior literature; the score correlates positively with future citations and separates Nobel-Prize-winning work from ordinary papers.

## 研究问题 / Problem
<!-- ZH --> 文献量爆炸,却**没有公认的「新颖性」度量**。已有做法用孤立的文章特征(关键词、MeSH 词、参考文献)量化新颖性,丢掉了正文语义里的上下文与细微差别。
<!-- EN --> Literature is exploding, yet there is **no widely accepted measure of novelty**. Existing approaches quantify it from isolated article features (keywords, MeSH terms, references), discarding the context and nuance carried by the semantic content of the text.

## 方法 / Method
<!-- ZH --> 用 LLM-embedder(`BAAI/llm-embedder`,以 Llama2-7B-Chat 为基础、BGE base 为 embedding 骨干)构建语义空间,把全库 PubMed 投影进去;用 t-SNE 做二维可视化;每篇文章按其与既往文献的距离算出 SemNovel 分数。验证走两条路:与未来影响力(引用数)的相关性,以及区分突破性研究的能力。另配一个交互界面供用户查询分数。
<!-- EN --> A semantic universe is built with LLM-embedder (`BAAI/llm-embedder`, Llama2-7B-Chat as foundation, BGE base as embedding backbone), into which the whole PubMed library is projected; t-SNE gives 2D visualization; each article's SemNovel score is its distance from prior publications. Validation runs two ways: correlation with future impact (citations), and ability to distinguish groundbreaking studies. An interactive interface is provided for analyzing scores.

## 数据 / Data
<!-- ZH --> 全量 PubMed 文献库;引用数作为未来影响力标签;诺奖获奖研究作为「突破性」正例;并在 PD-1/PD-L1 领域做了纵向趋势案例分析与跨学科合作分析。
<!-- EN --> The full PubMed corpus; citation counts as the future-impact label; Nobel-Prize-winning studies as "groundbreaking" positives; plus a longitudinal case study in the PD-1/PD-L1 field and an analysis of interdisciplinary collaboration.

## 主要结果 / Key results
<!-- ZH --> SemNovel 分数与未来引用量正相关(Spearman ρ = 0.1782,p < 0.001),且**独立于期刊影响因子、发表年份与作者数**,优于此前的语义新颖性指标;能显著区分高新颖性论文,包括诺奖研究(Kolmogorov-Smirnov 检验 p < 0.001);在 PD-1/PD-L1 领域展示了研究演进趋势,并显示跨学科合作与更高新颖性相关。
<!-- EN --> The SemNovel score correlates positively with future citations (Spearman ρ = 0.1782, p < 0.001), **independent of journal impact factor, publication year and author count**, outperforming prior semantic-novelty indicators; it separates highly novel papers including Nobel-Prize studies (Kolmogorov–Smirnov test, p < 0.001); it traces research evolution in the PD-1/PD-L1 field and links interdisciplinary collaboration to higher novelty.

## 创新点 / Contributions
- <!-- ZH --> 把新颖性度量从「特征计数」推进到「语义嵌入距离」,保留正文语义。 <!-- EN --> Moves novelty measurement from feature counting to semantic-embedding distance, preserving textual meaning.
- <!-- ZH --> 全 PubMed 规模的「语义宇宙」构建与可视化。 <!-- EN --> Builds and visualizes a "semantic universe" at full-PubMed scale.
- <!-- ZH --> 用诺奖研究与引用量做双重外部验证,而非只报内部一致性。 <!-- EN --> Dual external validation against Nobel-Prize studies and citation impact, not just internal consistency.
- <!-- ZH --> 提供交互界面,把指标做成可用工具。 <!-- EN --> Ships an interactive interface, turning the metric into a usable tool.

## 局限 / Limitations
- <!-- ZH --> 与引用量的相关系数不高(ρ ≈ 0.18):有统计显著性,但**预测个体论文影响力的能力有限**。 <!-- EN --> Correlation with citations is weak (ρ ≈ 0.18): statistically significant but of **limited power for predicting any individual paper's impact**.
- <!-- ZH --> 「新颖」不等于「正确」或「有价值」——距离远也可能只是离题或低质量。 <!-- EN --> "Novel" is not "correct" or "valuable" — distance can also mean off-topic or low quality.
- <!-- ZH --> 依赖特定 embedding 模型,换骨干后分数的稳定性未知。 <!-- EN --> Tied to one embedding model; score stability under a different backbone is unknown.
- <!-- ZH --> 诺奖作为「突破性」标签存在事后偏差与领域偏倚。 <!-- EN --> Nobel Prizes as the "groundbreaking" label carry hindsight bias and field skew.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 这篇不在 detect → model → revert 主链上,但它其实是**「异常检测」思想在文献空间的一次实例化**:先用嵌入构建「正常/既有」的语义分布,再把离该分布远的点标为新颖 —— 与本方向「学正常、以偏离度打分」的范式在方法论上同构,只是对象从组织换成了论文。可迁移的有两点:(1) **以距离为分数 + 外部标签验证**的评估思路(引用量、诺奖 ≈ 组织学的专家标注);(2) 它的诚实之处 —— 明确报告 ρ ≈ 0.18 这样的弱相关,而非只强调显著性,这是做异常评分时该有的报告规范。此外,若后续要做「agent 提名的假设有多新」这类判断,这是现成的度量工具。
<!-- EN --> Not on the detect → model → revert chain, but effectively an **instantiation of the anomaly-detection idea in literature space**: build an embedding distribution of what already exists, then flag points far from it as novel — methodologically isomorphic to this direction's "learn normal, score by deviation," with tissue swapped for papers. Two transferable pieces: (1) the **distance-as-score plus external-label validation** design (citations and Nobel Prizes ≈ expert annotation in histology); (2) its honesty — reporting a weak ρ ≈ 0.18 rather than hiding behind significance, the reporting discipline anomaly scoring needs. It is also an off-the-shelf tool if we later need to judge how novel an agent-generated hypothesis is.

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码:** SemNovel 官方仓库(Xu Lab)。 <!-- EN --> **Code:** the official SemNovel repository (Xu Lab).
<!-- ZH/EN --> <https://github.com/BIDS-Xu-Lab/SemNovel>
- <!-- ZH --> **模型:** LLM-embedder 骨干。 <!-- EN --> **Model:** the LLM-embedder backbone.
<!-- ZH/EN --> <https://huggingface.co/BAAI/llm-embedder>
- <!-- ZH --> **评估思路:** 与引用量的偏相关(控制 JIF/年份/作者数)+ 用诺奖研究做 KS 检验。 <!-- EN --> **Eval design:** partial correlation with citations (controlling JIF, year, author count) plus a KS test against Nobel-Prize studies.

## 待读 / Follow-ups
- <!-- ZH --> 拿到全文,确认语义宇宙的构建细节与 SemNovel 分数的具体定义(距离度量、邻域大小)。 <!-- EN --> Get the full text to confirm how the semantic universe is built and how the score is defined (distance metric, neighbourhood size).
- <!-- ZH --> 对比此前的新颖性指标(基于 MeSH/参考文献组合)的原始论文。 <!-- EN --> Compare against the original papers on prior novelty indicators (MeSH/reference-combination based).

## 引用 / Cite
```bibtex
@article{Peng_2025, title={SemNovel – A new approach to detecting semantic novelty of biomedical publications using embeddings of large language models}, volume={172}, ISSN={1532-0464}, url={http://dx.doi.org/10.1016/j.jbi.2025.104952}, DOI={10.1016/j.jbi.2025.104952}, journal={Journal of Biomedical Informatics}, publisher={Elsevier BV}, author={Peng, Xueqing and Xie, Yutong and He, Huan and Ondov, Brian and Raja, Kalpana and Liu, Qijia and Mei, Qiaozhu and Xu, Hua}, year={2025}, month=Dec, pages={104952} }
```
