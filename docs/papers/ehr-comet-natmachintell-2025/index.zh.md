# A machine learning approach to leveraging electronic health records for enhanced omics analysis

> **文献键** `Mataraso_2025` · **来源** Nature Machine Intelligence(2025) · **类别** ehr · **相关度** medium · **获取** open
> **链接** <https://doi.org/10.1038/s42256-024-00974-9> · `status: complete`

---

## 一句话
COMET(Aghaeepour 组,Stanford):组学研究往往只有几十到几百个样本,而同一医院的 EHR 有几万人 —— 先在「只有 EHR」的大队列上预训练一个 GRU,再把权重迁移进 EHR + 组学的多模态网络(早融合与晚融合混合),在 61 人妊娠蛋白组和 559 人 UK Biobank 癌症蛋白组上都提升了预测,并让模型挑出的蛋白更符合已知生物学。

## 研究问题
组学测量维度高,但队列规模受临床与预算限制,结果难以复现;机器学习中的「假阳性」表现为过拟合。现有改进(先验特征权重、迁移学习、深度 Cox)主要只用组学或元数据本身。EHR 越来越可得(MIMIC、UK Biobank、OMOP 标准化的院内数据库),但 EHR–组学整合有结构性矛盾:早/中融合需要两模态都完整(会丢掉大多数只有 EHR 的病人),晚融合又学不到跨模态交互。问题:如何利用**只有 EHR 的大量病人**来改善**小规模组学队列**的建模与生物学发现?

## 方法
**EHR 嵌入**:从 OMOP 的 measurement、observation、drug_exposure、condition_occurrence、procedure_occurrence 表抽取概念码;把同一病人同一天的码视为「句子」(随机打乱,因很多时间戳不可靠),用 word2vec 学 400 维嵌入,同日取平均得到每天一个 summary embedding,最多取最近 32 天。**预训练**:只有 EHR 的病人(pretraining cohort)上训练 GRU-RNN 预测同一结局(妊娠:随机选末 100 天内一点预测距分娩天数;癌症:以首次 C 开头 ICD 码时间为起点预测 3 年死亡)。**多模态架构**:三支 —— EHR 支(冻结的预训练 GRU + 线性层)、组学支(线性层;癌症任务为单隐层 MLP)、joint 支(EHR 潜表示与组学拼接后的线性层),最后一个无偏置线性层把三个预测加权合成 —— 即**早融合与晚融合的自适应混合**。损失分别为 MSE 与 BCE。**对照**:EHR-only、组学-only、joint baseline(结构与 COMET 完全相同但无预训练);ridge/logistic 回归(含把预训练系数作先验 β₀ 的变体);COMET Transformer 变体。每个实验 25 次不同划分(70/15/15),验证集预测取平均。**机制分析**:EHR 潜维度与蛋白的相关数、Integrated Gradients 蛋白重要性、外部数据集验证重要蛋白、中间节点性能、函数空间 t-SNE 轨迹。

## 数据
**妊娠队列(Stanford)**:2013–2021 年在 Stanford 分娩的 30,904 人(STARR OMOP);其中 **61 人**(171 份血浆样本,妊娠末 100 天 2–3 次采样)有基于适配体(aptamer)平台的蛋白组(1,317 个蛋白,去掉 12 个对照后 1,305 个),其余 30,843 人为预训练队列;另用同队列代谢组验证。**癌症队列(UK Biobank)**:入组前 12 个月至入组后 5 年内诊断任意癌症的 36,901 人;其中 **559 人**在确诊后 12 个月内有入组时血样蛋白组(UKB 蛋白组覆盖 53,058 人、中位 2,894 个蛋白),其余 36,342 人为预训练队列;3 年死亡率 5.5%。外部验证分别用公开妊娠蛋白组与乳腺癌蛋白组数据。

## 主要结果
- **距分娩天数**:COMET Pearson r = **0.868**(95% CI 0.825–0.900,RMSE 16.0 天);joint baseline 0.815(18.4 天);蛋白-only 0.796;EHR-only 0.768。代谢组:COMET 0.839 vs 仅代谢物 0.758。
- **3 年癌症死亡**:COMET AUROC **0.842**(0.744–0.922)、AUPRC **0.504**;joint baseline 0.786 / 0.365;EHR-only 0.749 / 0.205;蛋白-only 0.737 / 0.325。
- **预训练对线性模型也有效**:ridge 的 joint 模型加入预训练先验后 r 从 0.572 升到 0.799;Transformer 变体 r = 0.848,略低于 GRU 版 COMET。
- **EHR–蛋白对齐**:妊娠中 EHR 潜维度与蛋白的显著相关数 3,201 → **5,364**;癌症中 0 → **7,591**。COMET 最相关蛋白(IL1RL1/ST2、cystatin C、plexin-B2)已知与妊娠进程相关。
- **外部验证**:COMET 更重视的蛋白在外部妊娠数据中与分娩时间的平均 |r| = 0.22 vs 基线重视蛋白 0.12(p = 0.0276);癌症中 18 个里 9 个与死亡显著相关(基线 8 个)。
- **机制**:相同训练损失下测试损失更低,参数(函数)空间轨迹与基线分离 —— 作者称之为「通过初始化实现的正则化」。

## 创新点
- 据作者所知,**首个用 EHR 迁移学习改善组学分析**的方法。
- 解决「EHR 多、组学少」的结构不对称:预训练利用所有 EHR 病人,多模态阶段仍能学到跨模态交互。
- 以生物学一致性(而不仅是预测性能)作为评估维度:EHR 潜表示与蛋白的对齐、外部数据验证重要蛋白。
- 预训练的效益跨架构成立(GRU、Transformer、ridge、logistic)。

## 局限
- 组学队列极小(61 人 / 559 人),置信区间宽(癌症 AUROC CI 0.744–0.922);外部验证只是间接的(重要蛋白的相关性),且癌症中 9/18 vs 8/18 的差距很小。
- 只在表格型组学(蛋白组、代谢组)上验证;作者明确说**不知道对需要复杂架构的模态(如空间转录组)是否有效**。
- 预训练需要有标签的 EHR 任务(与目标任务相同);自监督预训练留待未来。
- EHR 表示较粗:word2vec + 日均值,同日码被打乱,只取最近 32 天;OMOP 映射可能有误。

## 与本研究方向的关系
在 PI 转发的五篇里,这篇是**唯一把 EHR 与分子数据连起来**的,因此它是 Sinai EHR 项目与本实验室组学/组织工作之间最直接的桥。场景完全对应:Sinai 有数百万人的 EHR,而有组学或活检的只是很小的子集(例如肾活检、BioMe 生物库样本)—— COMET 的「大 EHR 预训练 → 小组学队列迁移」正是这种不对称下的标准做法。**与心-代谢-肾方向**:把妊娠/癌症换成 CKD 进展或 DKD,把 EHR 预训练任务换成 eGFR 下降或进入透析,就得到一个可在 Sinai 上直接复现的设计;实验室 Novo 资助的 cardiometabolic-kidney 基础模型若要把 EHR 病人表示和分子数据对齐,本文给出了最小可行的评估方式(潜表示–分子相关数、重要特征的外部验证)。**与 Plan A 的关系**:作者明确把空间转录组列为未知 —— 而 Plan A 恰好是肾的 snRNA/snATAC/Xenium + H&E。一个自然的延伸是:用 EHR 预训练的病人表示作为**样本级协变量/先验**,帮助区分「临床上异常」与「技术伪迹」,与 Plan A 的跨模态一致性思路互补(临床模态成为又一个独立证据源)。**与 detect → model → revert**:COMET 把「病人尺度的临床轨迹」连接到「分子尺度的特征」,是从 EHR 层的 detect 走向分子层 model/revert 的一个接口原型;但它仍是相关性的(重要蛋白≠可干预靶点)。

## 可复用资产
- **代码:** COMET 全部代码(含 UK Biobank 队列提取查询与教程);Zenodo 10.5281/zenodo.13977341。
<https://github.com/samson920/COMET>
- **数据:** 妊娠蛋白组在 Dryad(10.5061/dryad.280gb5mpd);Stanford EHR 不可共享;UK Biobank 部分需申请。
- **评估设计:** joint baseline(同结构无预训练)作为干净消融;EHR 潜维度–分子相关计数;重要特征的外部数据验证。

## 待读
- 讨论中提到的「EHR 基础模型可直接预测蛋白表达水平」(ref 36)—— 与自监督替代标签化预训练直接相关。
- 用 Delphi/APOLLO 式自监督病人表示替换 COMET 的 GRU 预训练,看小组学队列上的增益是否更大。
- 检索已有的 EHR + 肾活检/组学整合工作(KPMP 是否有可链接的临床轨迹)。

## 引用
```bibtex
@article{Mataraso_2025, title={A machine learning approach to leveraging electronic health records for enhanced omics analysis}, volume={7}, ISSN={2522-5839}, url={http://dx.doi.org/10.1038/s42256-024-00974-9}, DOI={10.1038/s42256-024-00974-9}, number={2}, journal={Nature Machine Intelligence}, publisher={Springer Science and Business Media LLC}, author={Mataraso, Samson J. and Espinosa, Camilo A. and Seong, David and Reincke, S. Momsen and Berson, Eloise and Reiss, Jonathan D. and Kim, Yeasul and Ghanem, Marc and Shu, Chi-Hung and James, Tomin and Tan, Yuqi and Shome, Sayane and Stelzer, Ina A. and Feyaerts, Dorien and Wong, Ronald J. and Shaw, Gary M. and Angst, Martin S. and Gaudilliere, Brice and Stevenson, David K. and Aghaeepour, Nima}, year={2025}, month=Jan, pages={293–306} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
