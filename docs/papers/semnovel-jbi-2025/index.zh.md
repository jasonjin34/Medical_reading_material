# SemNovel – A new approach to detecting semantic novelty of biomedical publications using embeddings of large language models

> **文献键** `Peng_2025` · **来源** Journal of Biomedical Informatics(2025) · **类别** other · **相关度** medium · **获取** open
> **链接** <https://doi.org/10.1016/j.jbi.2025.104952> · `status: abstract-only`

---

## 一句话
SemNovel 用 LLM embedding 把整个 PubMed 投影成一个「语义宇宙」,以一篇论文到既往文献的距离作为**语义新颖性分数**,该分数与未来引用量正相关,并能把诺奖级研究从普通论文里挑出来。

## 研究问题
文献量爆炸,却**没有公认的「新颖性」度量**。已有做法用孤立的文章特征(关键词、MeSH 词、参考文献)量化新颖性,丢掉了正文语义里的上下文与细微差别。

## 方法
用 LLM-embedder(`BAAI/llm-embedder`,以 Llama2-7B-Chat 为基础、BGE base 为 embedding 骨干)构建语义空间,把全库 PubMed 投影进去;用 t-SNE 做二维可视化;每篇文章按其与既往文献的距离算出 SemNovel 分数。验证走两条路:与未来影响力(引用数)的相关性,以及区分突破性研究的能力。另配一个交互界面供用户查询分数。

## 数据
全量 PubMed 文献库;引用数作为未来影响力标签;诺奖获奖研究作为「突破性」正例;并在 PD-1/PD-L1 领域做了纵向趋势案例分析与跨学科合作分析。

## 主要结果
SemNovel 分数与未来引用量正相关(Spearman ρ = 0.1782,p < 0.001),且**独立于期刊影响因子、发表年份与作者数**,优于此前的语义新颖性指标;能显著区分高新颖性论文,包括诺奖研究(Kolmogorov-Smirnov 检验 p < 0.001);在 PD-1/PD-L1 领域展示了研究演进趋势,并显示跨学科合作与更高新颖性相关。

## 创新点
- 把新颖性度量从「特征计数」推进到「语义嵌入距离」,保留正文语义。
- 全 PubMed 规模的「语义宇宙」构建与可视化。
- 用诺奖研究与引用量做双重外部验证,而非只报内部一致性。
- 提供交互界面,把指标做成可用工具。

## 局限
- 与引用量的相关系数不高(ρ ≈ 0.18):有统计显著性,但**预测个体论文影响力的能力有限**。
- 「新颖」不等于「正确」或「有价值」——距离远也可能只是离题或低质量。
- 依赖特定 embedding 模型,换骨干后分数的稳定性未知。
- 诺奖作为「突破性」标签存在事后偏差与领域偏倚。

## 与本研究方向的关系
这篇不在 detect → model → revert 主链上,但它其实是**「异常检测」思想在文献空间的一次实例化**:先用嵌入构建「正常/既有」的语义分布,再把离该分布远的点标为新颖 —— 与本方向「学正常、以偏离度打分」的范式在方法论上同构,只是对象从组织换成了论文。可迁移的有两点:(1) **以距离为分数 + 外部标签验证**的评估思路(引用量、诺奖 ≈ 组织学的专家标注);(2) 它的诚实之处 —— 明确报告 ρ ≈ 0.18 这样的弱相关,而非只强调显著性,这是做异常评分时该有的报告规范。此外,若后续要做「agent 提名的假设有多新」这类判断,这是现成的度量工具。

## 可复用资产
- **代码:** SemNovel 官方仓库(Xu Lab)。
<https://github.com/BIDS-Xu-Lab/SemNovel>
- **模型:** LLM-embedder 骨干。
<https://huggingface.co/BAAI/llm-embedder>
- **评估思路:** 与引用量的偏相关(控制 JIF/年份/作者数)+ 用诺奖研究做 KS 检验。

## 待读
- 拿到全文,确认语义宇宙的构建细节与 SemNovel 分数的具体定义(距离度量、邻域大小)。
- 对比此前的新颖性指标(基于 MeSH/参考文献组合)的原始论文。

## 引用
```bibtex
@article{Peng_2025, title={SemNovel – A new approach to detecting semantic novelty of biomedical publications using embeddings of large language models}, volume={172}, ISSN={1532-0464}, url={http://dx.doi.org/10.1016/j.jbi.2025.104952}, DOI={10.1016/j.jbi.2025.104952}, journal={Journal of Biomedical Informatics}, publisher={Elsevier BV}, author={Peng, Xueqing and Xie, Yutong and He, Huan and Ondov, Brian and Raja, Kalpana and Liu, Qijia and Mei, Qiaozhu and Xu, Hua}, year={2025}, month=Dec, pages={104952} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
