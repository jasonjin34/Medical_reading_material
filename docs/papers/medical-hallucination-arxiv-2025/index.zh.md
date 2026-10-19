# Medical Hallucinations in Foundation Models and Their Impact on Healthcare

> **文献键** `Kim2025_250305777` · **来源** arXiv preprint(2025) · **类别** agents · **相关度** medium · **获取** open
> **链接** <https://arxiv.org/abs/2503.05777> · `status: complete`

---

## 一句话
一篇「综述 + 基准实验 + 医生标注 + 临床调查」的综合性工作:把医学幻觉定义为**可能改变临床决策的**错误/不一致/无据输出,给出五大类分类法;在 Med-HALT 上测 11 个模型发现**通用模型反而比医学专用模型更少幻觉**(基线无幻觉比例中位数 76.6% vs 51.3%),CoT 是最稳定的缓解手段;医生在 NEJM 病例上的标注显示,错误更多出在**时间顺序与化验数据理解**而非诊断本身。

## 研究问题
基础模型进入临床流程,但其「看似合理却错误」的输出在医学中风险极高:用户与 AI 之间存在巨大的知识不对称,捏造药物、禁忌用药、错误影像解读都可能直接伤害患者。医学场景还有特殊难点:知识快速更新、要求精确、概念高度互联(小错误会级联)、术语与语境专业。作者想回答:医学幻觉与一般幻觉有何不同、如何分类、成因是什么、如何检测与缓解、真实临床人员如何经历它,以及监管与法律含义。

## 方法
**分类法**(图 2 / 表 2):五大簇 —— (a) 事实错误(非事实、事实、输入冲突型);(b) 过时引用(记忆型);(c) 虚假相关(偏见诱导、拼接、多模态整合型);(d) 捏造来源或指南(流程型、研究型);(e) 不完整推理链(推理、决策、诊断型),并类比临床医生的认知偏差(如确认偏误)。**基准实验**(第 6 节):Med-HALT 七个任务各抽 50 例共 350 例 —— 推理类(False Confidence、None of the Above、Fake Questions)与记忆类(Abstract-to-Link、PMID-to-Title、Title-to-Link、Link-to-Title);五种条件:Base、System Prompt、CoT(「Let's think step by step.」)、MedRAG(基于 KG 的医学 RAG)、Internet Search(SerpAPI 谷歌搜索);指标为 Med-HALT pointwise 分(对 +1、错 −0.25)与 UMLSBERT 语义相似度;统计用 Mann–Whitney 与 Benjamini–Hochberg FDR 校正。**医生标注**(第 7 节):20 份 NEJM 病例记录,三类任务(时间顺序、化验数据理解、诊断预测),5 个模型,7 名 MD 级标注者按幻觉类型与 0–5 级临床风险标注,用平均成对 Jaccard 指数衡量一致性。**调查**(第 8 节):31 题在线问卷,2024-09-15 至 12-18,MIT COUHES IRB 豁免。

## 数据
Med-HALT(350 例);NEJM 病例记录(20 份);调查 75 人参与、70 份完整回答(研究人员 29、医生 23、数据科学家 15、生物医学工程 5、其他 3)。11 个模型:通用 7 个(o3-mini、o1、GPT-4o、GPT-4o mini、GPT-5、Gemini-2.5 Pro、DeepSeek-R1),医学专用 4 个(PMC-LLaMA、AlpaCare-13B、MedAlpaca-13B、MedGemma)。医生标注的 5 个模型为 o1、gemini-2.0-flash-exp、gpt-4o、gemini-1.5-flash、claude-3.5 sonnet。

## 主要结果
**Med-HALT**:gemini-2.5-pro 基线 87.6%、CoT 后 97.9%;deepseek-r1 86.6%、o3-mini 80.4%、gpt-5 71.2%、o1 64.0%、gpt-4o 54.4%、gpt-4o-mini 48.3%。医学专用:medgemma 52.6%、pmc-llama 40.8%、medalpaca 32.0%、alpacare 28.6%。通用 vs 专用基线中位数 **76.6% vs 51.3%**(差 25.2%,95% CI 18.7–31.3%,U=27.0,p=0.012,秩二列 r=−0.64)。**CoT**:在 71% 的模型中显著改善(p<0.05),FDR 校正后 64% 仍显著;46 项模型内检验中 22 项原本显著,校正后保留 19 项(86.4% 保留率)。o3-mini:基线 80.4% → System Prompt 81.4% → CoT 90.7%。**搜索增强**:gpt-5 71.2%→87.6%(+16.5%);pmc-llama 40.8%→59.9%(相对 +46.1%);但 deepseek-r1 86.6%→84.3%,强模型可能被嘈杂检索拖累 —— 建议自适应检索。语义相似度上通用强模型 0.8–0.9,医学模型 0.1–0.5。**NEJM 医生标注**:诊断预测幻觉率最低(0%–22%),时间顺序(0.25%–24.6%)与化验数据理解(0.25%–18.7%)更高;GPT-4o 在时间顺序 24.6%、化验 18.7% 最高且多被判为「显著/相当」临床风险;Claude-3.5 与 o1 在诊断预测上 0%。**调查**:摘要报告 91.8% 遇到过医学幻觉、84.7% 认为可能伤害患者;正文给出原始计数:59 人中 50 人认为所见幻觉可能影响患者健康,85%(51 人)用交叉核对外部来源应对。(注:摘要称「64–72% 的残余幻觉源于因果/时间推理失败」,正文未找到对应的完整推导;摘要「CoT 在 86.4% 的比较中显著降低幻觉」实为 FDR 保留率,解读需谨慎。)

## 创新点
- 以「是否可能改变临床决策」为核心的医学幻觉定义,以及五大簇 + 细分类型的分类法(配临床示例)。
- 通用 vs 医学专用模型的系统对比,挑战「领域微调更安全」的假设。
- 医生在真实病例上按类型 + 0–5 临床风险双维标注,揭示时间与化验信息抽取是薄弱环节。
- 多国临床人员调查 + 监管与法律责任讨论,把技术问题连接到部署实践。

## 局限
- Med-HALT 每任务仅 50 例;评分依赖 UMLSBERT 相似度与 pointwise 分,作者自己承认它们不直接反映临床安全。
- 医生标注只用 20 份 NEJM 病例、且与基准实验使用的模型集不同;正文自陈存在「输出日志与图示数据不一致」需进一步核查。
- 调查样本小(70 份完整回答),摘要百分比与正文计数的分母不完全一致;多个结论(「推理驱动而非知识缺失」)的论证强度高于证据。
- 医学专用模型都是较小的旧模型,与前沿通用模型的比较混杂了规模与年代因素。

## 与本研究方向的关系
对 **Plan B** 主要提供两样东西。一是**分类法的骨架**:五大簇中「输入冲突型」(结论与给定数据矛盾)、「拼接型」(把无关信息合成一个结论)、「多模态整合型」、「捏造来源/指南」与「不完整推理链」,都能在组学 agent 中找到对应 —— 例如把 snRNA 与 Xenium 的结果错误拼接、把空间邻近误读为因果、或引用不存在的标记基因列表;Plan B 的 omics-specific taxonomy 可以以它为上层框架,再细化出组学特有的类型(批次 vs 生物学混淆、细胞注释错误、统计显著性误读)。二是**医生标注协议**:「幻觉类型 × 0–5 临床风险」的双维标注,加上多标注者的成对 Jaccard 一致性,可以直接作为 KidneyAnomalyBench / Plan B 专家标注的模板(把「临床风险」换成「若据此做湿实验验证会浪费多少/误导多严重」)。它的发现「错误集中在时间顺序与化验数值抽取」也提示:agent 处理组学结果中的**数值与元数据**(样本分组、时间点、阈值)可能比高层生物学推断更容易出错,verifier 应优先核验这些。「通用强模型优于领域微调模型」对选择 Plan B 的被评 agent 底座有参考价值,但证据存在规模混杂。与 Plan A 无直接关系。

## 可复用资产
- **项目页(标注指南、标注界面图 11–13):**
<https://medical-hallucination.github.io/>
- **基准:** Med-HALT(Pal et al., 2023);MedRAG(Xiong et al., 2024)作为 RAG 基线。
- **分类法与风险等级表:** 表 2(类型定义与示例)、表 6–7(标注用类型与 0–5 风险定义)。
- **调查问卷:** 31 题临床人员 AI/幻觉问卷(附录)。

## 待读
- Med-HALT 原文(Pal et al., 2023)与 Hegselmann et al. (2024) 的幻觉类型学、Asgari et al. (2025) 的临床风险框架 —— 本文标注协议的两个来源。
- 第 5.4 节不确定性量化方法,用于 Plan B 校准 verifier 的相关工作梳理。
- 与本仓库 llm-judge-healthcare-arxiv-2026、medragchecker-arxiv-2026 对读:定义 → 评估器 → 核验方法。

## 引用
```bibtex
@misc{Kim2025_250305777,
  title = {Medical Hallucinations in Foundation Models and Their Impact on Healthcare},
  author = {Kim, Yubin and Jeong, Hyewon and Chen, Shan and Li, Shuyue Stella and Park, Chanwoo and Lu, Mingyu and Alhamoud, Kumail and Mun, Jimin and Grau, Cristina and Jung, Minseok and Gameiro, Rodrigo and Fan, Lizhou and Park, Eugene and Lin, Tristan and Yoon, Joonsik and Yoon, Wonjin and Sap, Maarten and Tsvetkov, Yulia and Liang, Paul and Xu, Xuhai and Liu, Xin and Park, Chunjong and Lee, Hyeonhoon and Park, Hae Won and McDuff, Daniel and Tulebaev, Samir and Breazeal, Cynthia},
  year = {2025},
  eprint = {2503.05777},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2503.05777}
}
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
