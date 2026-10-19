# BioML-bench: Evaluation of AI Agents for End-to-End Biomedical ML

> **文献键** `Miller_2025` · **来源** bioRxiv(2025) · **类别** agents · **相关度** medium · **获取** open
> **链接** <https://doi.org/10.1101/2025.09.01.673319> · `status: complete`

---

## 一句话
BioML-bench 把 MLE-bench 的「任务 capsule + 自动评分」范式搬到生物医学:24 个端到端 ML 任务(药物发现、医学影像、蛋白工程、单细胞),agent 需自己建 pipeline、训模型、提交预测,再映射到**以领域专家为主的公开排行榜**百分位。四个 agent(Biomni、STELLA、AIDE、MLAgentBench)平均只到 **34–39 百分位**,且**生物医学专用 agent 并无一致优势**。

## 研究问题
现有生物医学 agent 的评估多是问答(如 LAB-Bench)或窄域生信任务;没有基准检验 agent 能否完成治疗开发中核心的**有监督 ML 挑战**(扰动响应建模、毒性预测等)的完整流程。MLE-bench 证明了端到端可执行评估可行,但其 Kaggle 任务的排行榜由众包而非领域专家构成;BixBench 主要是文本答案、不涉及监督学习。

## 方法
框架改自 MLE-bench,增加生物医学任务域、新 agent、新指标与 h5ad 等生信文件格式支持,并提供云部署配置与 mkdocs 文档。每个 task capsule 给出结构化任务描述、训练数据、测试特征和示例提交文件;agent 在 Docker(预建 conda 环境)中运行,提交结果自动校验并用任务原始指标(AUROC、Spearman 等)打分。**Agent**:Biomni v0.0.5(Claude Sonnet 4)、STELLA(OpenRouter 默认模型)、AIDE v6.3.3 与 MLAgentBench(均 GPT-4.1),另有输出无信息预测的 Dummy。每个 agent–任务组合 **4 次独立重复**。**指标**:排行榜百分位、跨 agent 平均排名、超过人类中位数比例、获奖牌比例(沿用 MLE-bench 定义)、完成率;分 **penalized**(失败记 0 百分位)与 **non-penalized**(失败剔除)两种口径。**算力**:影像任务单张 NVIDIA L4(16 vCPU、64 GB)限 16 小时;其他任务纯 CPU 限 8 小时。

## 数据
共 24 个任务:**药物发现 9 个**(PolarisHub / TDC:EGFR 抑制剂分类、肝微粒体清除率、血浆蛋白结合、溶解度、CYP2D6、logP、hERG、BBB、Caco-2);**医学影像 4 个**(Kaggle:OSIC 肺纤维化 FVC 预测、PatchCamelyon 组织病理转移检测、RSNA 脑瘤 MGMT 甲基化、UW 消化道分割);**蛋白工程 6 个**(ProteinGym:SARS-CoV-2 spike RBD、Tsuboyama 2023 稳定性、indel 等);**单细胞 5 个**(OpenProblems:CITE-seq 模态预测、PBMC 小分子扰动响应、**跨糖尿病肾病(DKD)数据集的细胞类型 label projection**、Slide-seqV2 空间可变基因、乳腺癌细胞通讯)。

## 主要结果
**Penalized 总体**:Biomni 排行榜百分位 **34.45 ± 5.36**(最佳,平均排名 1.88,完成率 100%)、STELLA 31.84 ± 5.82(完成率 91.7%)、AIDE 28.50 ± 5.22(完成率 80.2%)、MLAgentBench 21.43 ± 4.40、Dummy 2.50。**Non-penalized**:STELLA 39.45 ± 6.52 反超,AIDE 37.41 ± 5.85,Biomni 34.45;三者差距大多在 SEM 之内。超过人类中位数比例最高约 34–43%,获奖牌比例 ≤ 21%。**按领域(penalized)**:单细胞 Biomni 55.62 最强(STELLA 54.23、AIDE 53.17 紧随);影像 MLAgentBench 21.73 最佳;蛋白与药物 Biomni 领先;去掉惩罚后 STELLA 在影像大幅领先、AIDE 在蛋白领先、Biomni 在药物领先。**策略**:94 个超中位数的运行显示,强 agent 更常尝试多样的特征工程与模型类型;AIDE 在 Tsuboyama 2023 上用 BLOSUM、保守性、理化特征拿到 **100 百分位**,但同一 agent 同一任务另一次重跑只有 **54 百分位** —— 策略在重复运行间并不稳定。**架构**:Biomni 和 MLAgentBench 约 50% 用随机森林,AIDE 常用堆叠/梯度提升;**深度学习几乎从未被选为最终模型,即便是影像任务**,而人类排行榜以 DL 为主。**失败**:41 次失败运行主要源于脚手架问题 —— 资源耗尽(复制大图像)、静默错误(try–except 回退导致脚本跑完却没存预测)、卡在无谓的环境安装、框架未捕获异常、超时。

## 创新点
- 第一个跨四个生物医学领域的**端到端可执行 ML** agent 基准,以专家主导的排行榜为人类基线。
- 同时报告 penalized / non-penalized 两种口径,把「能力」与「脚手架可靠性」拆开。
- 对成功运行的策略、选用架构和失败运行的原因做了人工日志分析。
- pip 可安装、带文档的开源包,降低复现门槛。

## 局限
- 每个 agent 用各自默认 LLM(GPT-4.1 / Claude Sonnet 4 / OpenRouter 默认),**agent 设计与底座模型混淆**;作者自认需系统地变换 LLM。
- 公开排行榜混合了不同水平、投入与算力,作为人类基线并不完美;只有 24 个任务,每领域 4–9 个,误差条很宽。
- 只看预测分数,不检查 agent 是否有数据泄漏、是否正确使用验证集,或其方法叙述是否属实。
- 未与 AutoML(H2O、Lazy Predict)对照,无法判断 LLM agent 相对自动化 pipeline 的增益。

## 与本研究方向的关系
对 **Plan B**,有三条具体证据:(1) AIDE 在同一任务两次重跑得到 100 vs 54 百分位,是「rerun stability」轴的直接案例 —— 结论/性能在重跑间可能剧烈波动;(2) 失败模式中的「**静默错误**」(try–except 回退使脚本看似成功却没有产出)正是 claim-to-evidence 验证要抓的那类问题:agent 报告「已完成」,但证据(预测文件)不存在 —— 应写进我们的 omics failure taxonomy;(3) agent 设计与底座 LLM 的混淆提示我们的评估要像 DeepEvidence 那样固定底座。对 **Plan A**,它的单细胞任务里有 **跨 DKD 数据集的 label projection**(来自 OpenProblems),这是与肾脏 omics 直接相关的现成任务,可作为 KidneyAnomalyBench 中「参考映射/标签迁移」基线的对照;但 BioML-bench 只评估预测指标,不评估异常或伪影识别。对 detect → model → revert 主线,它显示 agent 倾向用经典 ML(随机森林、梯度提升)而回避深度学习,这意味着让 agent 自动搭建 virtual tissue 模型(本质上是 DL)目前不现实。

## 可复用资产
- **代码 / 包:** BioML-bench(pip 可装,含文档与教程)。
<https://github.com/science-machine/biomlbench>
- **任务来源:** PolarisHub、TDC、Kaggle、ProteinGym、OpenProblems(含 DKD label projection 任务)。
- **报告口径:** penalized / non-penalized 双口径 + 完成率,可用于区分能力与可靠性。

## 待读
- MLE-bench(arXiv 2410.07095)、STELLA(arXiv 2507.02004)、AIDE(arXiv 2502.13138)。
- OpenProblems 的 DKD label-projection 任务细节(数据来源、指标),看能否用作 Plan A 的基线。
- 是否有后续版本固定底座 LLM 或加入 AutoML 对照。

## 引用
```bibtex
@article{Miller_2025, title={BioML-bench: Evaluation of AI Agents for End-to-End Biomedical ML}, url={http://dx.doi.org/10.1101/2025.09.01.673319}, DOI={10.1101/2025.09.01.673319}, publisher={openRxiv}, author={Miller, Henry E. and Greenig, Matthew and Tenmann, Benjamin and Wang, Bo}, year={2025}, month=Sept }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
