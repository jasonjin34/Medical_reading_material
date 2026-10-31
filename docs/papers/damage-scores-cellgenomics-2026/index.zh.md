# Cell-type-specific damage scores reveal kidney and liver disease trajectories in single-cell and spatial transcriptomics

> **文献键** `Padvitski_2026` · **来源** Cell Genomics(2026) · **类别** single-cell · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1016/j.xgen.2026.101337> · `status: abstract-only`

---

## 一句话
提出一个通用框架,用**细胞类型特异的连续损伤分数**把单个细胞放在"健康 → 损伤"轴上:从大量小鼠疾病模型中挑出一致变化的 42 个基因,用 AUCell 打分,得到足细胞损伤分数 PDS(CKD/FSGS)与肝细胞损伤分数 HDS(MASLD/NASH);在小鼠与人的 scRNA、snRNA、空间转录组、蛋白组、组织学与临床数据中都能检出疾病相关损伤,能"对齐"不同疾病模型,并在未扰动的对照细胞中也分辨出损伤程度差异。

## 研究问题
退行性疾病通过逐步累积的细胞内在损伤进展,但 bulk 转录组会把它平均掉,而离散的细胞状态注释(如"injured/altered state")又把连续过程切成类别,难以刻画单个细胞在体内的渐进衰退。需要一个可迁移、可跨数据集与跨物种比较的连续损伤度量。

## 方法
(以下据预印本 v2)**基因选择**:在每个疾病模型内按差异表达 p 值给基因排名,跨模型平均排名;过滤条件为在目标细胞类型中表达、且在 ≥ 75% 研究中方向一致;取前 n 个作为损伤标记基因。**最终签名**:PDS 42 个基因(39 下调、3 上调),HDS 42 个基因(30 下调、12 上调)。**打分**:AUCell 基于排名的方法,按方向合并上调与下调基因,得到单细胞分辨率分数。**验证**:留一模型交叉验证(去掉一个疾病模型的全部样本重算签名,再在被留出模型上检验);稳健性测试(标记基因数 30–200 变化影响很小;随机打乱至多 70% 输入研究仍能区分疾病与对照)。下游:基于 PDS 的通路"指纹"分析、在相同损伤水平下比较不同模型、用足细胞 ATAC 数据构建转录调控网络、GWAS 富集。

## 数据
(据预印本 v2)**小鼠**:足细胞 37 个数据集、9 种足细胞病模型(如 Nphs2mut、Cd2apko、Pdss2mut、阿霉素、NTN、Btbr ob/ob 糖尿病、Wt1 ko/wt);肝细胞约 250 个样本、13 种肝病模型(CCl4、DDC、乙醇、链脲佐菌素、NAFLD 等);Slide-seqV2(Btbr ob/ob,GSE190094)与 Visium(NAFLD 小鼠)。**人**:KPMP snRNA-seq(n = 37,有临床数据)、scRNA-seq(n = 17)、1 个 FSGS Visium 活检;新生成的 Xenium(8 名微小病变或 FSGS 患者,238 个肾小球);NEPTUNE 尿液足细胞;肝 GSE189600(3 健康 / 3 NASH)、GSE210077(3 健康 / 3 纤维化)、2 例脂肪变 Visium。

## 主要结果
- **发表版摘要**:PDS 把足细胞损伤与 FSGS 进展联系到**昼夜节律基因表达紊乱**;HDS 在 MASLD/NASH 中识别出一个**损伤阈值**,超过后肝细胞进入衰老、代谢功能障碍状态。
- (预印本)**与功能相关**:小鼠 12 个 bulk 肾小球研究中 PDS 与白蛋白尿 Spearman ρ = 0.45(p = 0.017),新 snRNA-seq 数据 ρ = 0.78(p = 1.8 × 10⁻⁶);KPMP 中只有糖尿病状态与 PDS 与 ACR 显著相关;NEPTUNE 尿足细胞 PDS 与 UPCR 相关。
- (预印本)**空间与形态**:人 Xenium 238 个肾小球中 PDS 与足细胞密度负相关、与裂孔隔膜长度相关(p < 0.05);小鼠空间数据中肾小球 PDS 差异显著。
- (预印本)**对照细胞也有损伤谱**:对照样本平均损伤更低,但总含一小部分高损伤细胞;PDS 可像白蛋白尿在临床上那样"对齐"不同模型的损伤状态。蛋白组数据上 PDS/HDS 无一例外地分开疾病与对照。
- (预印本)**遗传**:PDS 42 基因中 8 个与肾病 GWAS 相关(基因体富集 p = 0.031,含侧翼 p = 0.002);HDS 10/42 与肝 GWAS 相关(p = 0.1,不显著)。

## 创新点
- 把"损伤"定义为跨模型共识的**连续、细胞类型特异**的单细胞分数,而非离散状态标签。
- 留一模型验证 + 打乱研究的稳健性测试,说明签名能泛化到未见过的疾病模型。
- 一个分数横跨 sc/sn/空间/蛋白/组织学/临床模态与小鼠→人,可在相同损伤水平下比较不同病因。

## 局限
- 签名源自小鼠模型,人类验证队列部分很小(肝 3 vs 3)。
- sc 与 sn 数据的 PDS 基线有小差异(作者归因于组织消化损伤)—— 说明分数会受**技术/处理伪影**影响。
- 肝细胞伪时间轨迹被分区(zonation)主导,可能掩盖损伤信号。
- 只针对足细胞与肝细胞两种细胞类型;是"已知损伤方向"的监督式签名,不能发现签名之外的新异常。
- 本笔记未读到发表版全文,上述细节需核实。

## 与本研究方向的关系
这是 **伪影注入课题** 最直接的"已知方向"对照:我们的异常检测是无监督的"离健康参照有多远",而 PDS 是有监督的"沿共识损伤方向走了多远"。两者组合很有价值:(1) **作为基线与弱标签** —— 在待测肾样本与 KPMP/Lake 数据上,检测器给出的足细胞异常分数应与 PDS 显著相关;不相关的高异常细胞要么是新型异常、要么是伪影 —— 正是需要跨模态一致性(snATAC、Xenium 足细胞密度、H&E 形态)来裁决的部分;(2) 它报告"sc 与 sn 基线不同、归因于消化损伤",以及"对照样本总有一小部分高损伤细胞" —— 这与 Lake 2023 "参照组织中也有 altered states"一致,是 KidneyAnomalyBench 必须区分的**取样/解离伪影 vs 真实损伤**;(3) 它的 Xenium 验证(PDS vs 足细胞密度、裂孔隔膜长度)示范了**转录组分数与形态学读数的跨模态对齐**,可以直接借作我们的验证协议。对 **detect → model → revert**:连续损伤轴就是 virtual tissue 里一个天然的"状态坐标",revert 的目标可以表述为"把 PDS 降回对照分布";发表版提出的 HDS 阈值(超过即衰老)提示存在**可逆窗口**,对选择回退干预的时机很关键。对 **Agent 可信度课题**:它是 agent 可调用的简单、可复现工具(签名 + AUCell),适合测试 rerun stability 与"agent 是否正确报告了分数的适用范围(仅足细胞/肝细胞、小鼠来源)"。

## 可复用资产
- **签名:** PDS / HDS 各 42 个基因(见论文补充表;须从发表版获取)。
- **代码(作者 Paula Unger Avila 的 GitHub,未在论文中核实对应关系):** HDS 相关脚本仓库。
<https://github.com/PauUng/HepatocyteDamageScore> · <https://github.com/PauUng/hepatocyte-damage-score-paper>
- **数据:** KPMP、GSE190094(Slide-seqV2)、GSE189600、GSE210077 等公开数据;新 Xenium 数据见发表版数据声明。
- **预印本:**
<https://doi.org/10.1101/2025.02.20.639269>

## 待读
- 获取发表版 PDF,核实数字、昼夜节律机制与 HDS 阈值,补全代码/数据可用性。
- 把 PDS 思路扩展到 PT/TAL(对照 Lake 2023 的 aPT/aTAL 与 CellSpectra 的通路协调分数)。
- 比较"监督式损伤分数"与"无监督参照距离"在肾脏 Xenium 数据上的一致性。

## 引用
```bibtex
@article{Padvitski_2026, title={Cell-type-specific damage scores reveal kidney and liver disease trajectories in single-cell and spatial transcriptomics}, volume={6}, ISSN={2666-979X}, url={http://dx.doi.org/10.1016/j.xgen.2026.101337}, DOI={10.1016/j.xgen.2026.101337}, number={10}, journal={Cell Genomics}, publisher={Elsevier BV}, author={Padvitski, Tsimafei and Unger Avila, Paula and Chen, He and Özel, Cem and Braun, Fabian and Kroll, Marie-Kristin and Vossen, Christian and Wienand, Peter and Butt, Linus and Unnersjö-Jess, David and Schumacher, Anna-Lena and Folz-Donahue, Kat and Göbel, Heike and Kuppe, Christoph and Müller, Roman-Ulrich and Westermark, Pål Olof and Brinkkötter, Paul Thomas and Schermer, Bernhard and Benzing, Thomas and Wunderlich, Frank Thomas and Kann, Martin and Beyer, Andreas}, year={2026}, month=Oct, pages={101337} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
