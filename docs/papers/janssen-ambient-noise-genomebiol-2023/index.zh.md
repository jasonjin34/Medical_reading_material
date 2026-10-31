# The effect of background noise and its removal on the analysis of single-cell expression data

> **文献键** `Janssen_2023` · **来源** Genome Biology(2023) · **类别** single-cell · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1186/s13059-023-02978-x> · `status: complete`

---

## 一句话
把来自两个小鼠亚种(*M. m. castaneus* CAST/EiJ 与 *M. m. domesticus* C57BL/6J、129S1/SvImJ)的肾脏细胞混在同一个 10x 通道里,用亚种间纯合 SNP 区分「本细胞的分子」和「外来分子」,从而得到**每个细胞背景噪声比例 ρ_cell 的基因型真值**;发现背景噪声在重复间、细胞间差异很大(平均 3–35% 的 UMI),主要来自 ambient RNA 而非 barcode swapping,并以此真值评测 CellBender / DecontX / SoupX —— CellBender 估计最准、对 marker 基因改善最大,而聚类与分类对背景噪声相当稳健。

## 研究问题
液滴式 scRNA-seq / snRNA-seq 中,一个 cell barcode 上的 reads 并不全来自被包裹的细胞:破裂细胞释放的游离 **ambient RNA** 以及建库 PCR 中的 **barcode swapping**(嵌合分子)都会造成背景噪声。它会让 marker 基因在不该表达的细胞类型里被检出、降低 log2FC、甚至伪造「新细胞类型」,还会在条件间差异表达中制造假阳性。已有去噪方法(SoupX、DecontX、CellBender)常用的评测基准是人-鼠细胞系混合(只能看到跨物种的、特征空间不重叠的污染,细胞类型单一)或「排他性 marker 基因」,两者都无法刻画真实组织中**同一基因上的表达量偏移**。作者要回答:背景噪声有多大、多变、从哪来,对下游分析影响多大,去噪工具能否在没有基因型信息时正确估计并去除它。

## 方法
**实验设计**:每个 10x 通道(Chromium Next GEM 3' v3.1,目标 10,000 个细胞/核)混合 3 只小鼠(CAST/EiJ、C57BL/6J、129S1/SvImJ,6–8 周,PBS 心内灌注)的肾脏四分之一块。scRNA-seq 用新鲜组织 Liberase TH 酶解;snRNA-seq 用 RNAlater 保存的冷冻组织做 TST 核提取(nuc3 比 nuc2 多洗两次)。Cell Ranger 3.0.2(sc 用 mm10 2020A,sn 用 pre-mRNA mm10)→ DropletUtils `barcodeRanks` 拐点 ∪ Cell Ranger 细胞调用定义细胞 → cellsnp-lite(≥20 UMI、MAF≥0.1)+ Vireo 按 Mouse Genomes Project 的 VCF 解复用,去掉 doublet/未分配 → SingleR 以 Denisenko et al. 小鼠肾脏数据为参考注释 13 种细胞类型。**背景比例估计**:只用区分两亚种的纯合 SNP,改编 souporcell(Heaton et al.)的方法:每个位点可观测污染概率 p = ρ_c · A_{l,1}/(A_{l,0}+A_{l,1}),其中 A_{l,1}/(A_{l,0}+A_{l,1}) 是全实验(细胞+空液滴)的外来等位基因频率,用来外推同基因型(看不见的)污染;以二项似然在 [0,1] 上一维优化求 ρ_c 的 MLE,profile likelihood 给 95% CI。主要分析只用 CAST 细胞(占 9–43%,其污染主要来自 domesticus,因此可见比例高),排除线粒体基因。**来源分析**:用 domesticus 等位基因计数构建 endogenous(domesticus 细胞)、contamination(CAST 细胞)、empty(UMI 曲线平台区 ~500–1000 UMI 的空液滴)三种 pseudobulk 谱,比较 Spearman 相关、SCDC 反卷积细胞组成、内含子比例;用「同一 CB-UMI 对应多个基因」识别 PCR 嵌合体估计 swapping。**基准**:CellBender v0.2.0(fpr 0.01,另试 0.05/0.1)、SoupX 1.6.1(autoEstCont,另试手动 0.1/0.2)、DecontX(celda 1.12.0;default 与以空液滴为 background 两种);每细胞估计 a_c = 1 − Σx/Σr,与 ρ_c 比较 RMSLE 和 Kendall τ;下游评测 marker 基因检出率/log2FC、SingleR 预测分数、silhouette、cluster purity、与「基因型清洗」矩阵的 k-NN(k=50)重叠。

## 数据
5 个 10x 通道:scRNA-seq **rep1、rep2、rep3**(新鲜组织)与 snRNA-seq **nuc2、nuc3**(冷冻组织,分别与 rep2、rep3 来自同一批小鼠样本)。每次实验得到 5,000–20,000 个 good cells,其中 CAST 占 9–43%;正文另给出 rep3「3900 cells」、rep2「15,000 cells」(与 5,000 下限不一致,可能指不同过滤口径,待查 Fig. 1B)。>40,000 个信息 SNP(~32,000 区分亚种,~10,000 区分两 domesticus 品系);每细胞平均覆盖 ~1,000 个信息 SNP(~20% UMI),nuc2 只有 ~100 个;约 7,000 个基因带至少一个亚种信息 SNP。近端小管(PT)占 66–89% 的细胞。原始数据:GEO GSE218853(GSM6757771–75,每样本 raw 与 filtered `feature_bc_matrix.h5`;SRA PRJNA906016);Zenodo 7328632(每个重复一个 zip,含 Seurat 对象、per-cell 污染估计 RDS、raw/filtered h5);代码 GitHub Hellmann-Lab/scRNA-seq_Contamination(GPL-3.0,Zenodo 7941521)。

## 主要结果
(1) **幅度与变异**:每实验外来基因型计数中位数 2–27%(可见下界);外推后的 ρ_cell 中位数:rep3 大多数细胞 <3%,rep2 约 11%,nuc2 35%,nuc3 17%(rep1 未在正文给出,见 Fig. 2A);冷冻组织 snRNA-seq 明显高于对应的 scRNA-seq(35% vs 11%,17% vs 3%);与细胞产量无关。污染 UMI 的**绝对量在细胞间近似恒定**,因此细胞越大比例越小。(2) **来源**:每细胞污染 UMI 数与空液滴 UMI 数相当;sc 中 contamination 谱与 empty(ρ=0.73–0.85)和 endogenous(ρ=0.70–0.87)都高度相关,sn 中更像 empty(~0.85 vs ~0.50),且 sn 空液滴中 PT 比例下降;内含子比例 contamination 更接近 empty;PCR 嵌合体中位比例 0.2%(rep3)–0.7%(nuc3),对背景的贡献中位 <10% → 主要是 ambient RNA。(3) **marker 基因**:PT marker Slc34a1 在 rep2 约 60% 的非 PT 细胞中被检出;背景越高 log2FC 越小。(4) **工具估计精度**:sc 中 CellBender 与 DecontX 相近,SoupX 低估且抓不住细胞间差异;sn 中 SoupX 全局水平更好但仍无细胞间相关,CellBender/DecontX 变差;CellBender 默认参数最稳健(代价约 45 CPU 小时/通道);nuc3 所有方法都最差,后续不再分析。(5) **去噪后 marker**:rep2 中 Slc34a1 非 PT 检出率 60% → SoupX 54%、CellBender 7%、DecontX_background 9%、DecontX_default 2%;nuc2 中 DecontX_default 失败(87%),DecontX_background 20%,CellBender 4%,SoupX <1%;CellBender 对已知 marker 的 log2FC 提升最大。(6) **分类与聚类**:去噪后仅 <1%(sc)/ ≤1.3%(nuc2)细胞换标签;DecontX 让 sc 簇最纯但降低 k-NN 与真值的重叠(破坏细粒度结构),SoupX 基本不动细粒度结构;nuc2 高背景下所有方法均改善。**建议**:marker 分析总是去噪;分类/聚类/拟时序只在背景高时去噪。

## 创新点
- 第一个在**真实多细胞类型组织**中、对**同一基因特征**给出每细胞背景比例真值的实验数据集(亚种混合 + 纯合 SNP)。
- 用三种 pseudobulk 谱 + 内含子比例 + PCR 嵌合体给出背景主要来自 ambient RNA 的多重证据。
- 以基因型真值对 CellBender / DecontX / SoupX 的每细胞估计与下游影响做定量基准,包括「去噪可能破坏细粒度结构」这一 k-NN 视角。
- 同时覆盖低(rep3)、中(rep2)、高(nuc2)背景水平,并公开 raw 矩阵与每细胞估计。

## 局限
- 只有小鼠肾脏、一种平台(10x 3' v3.1)、5 个通道;PT 占 66–89%,细胞组成高度偏斜;nuc2 与 nuc3 实验条件不同(洗涤次数),不是严格重复。
- 真值只对 CAST 细胞可靠;同基因型污染靠外推(假设 SNP 覆盖的计数代表全细胞),nuc2 每细胞只有 ~100 个信息 SNP,置信区间更宽。
- 健康组织,没有疾病状态;无法区分「背景噪声」与「真实生物学状态变化」在疾病样本中的交互。
- 只评测了三个工具的固定版本(如 CellBender v0.2.0);默认参数下的结论,SoupX 给定真实背景水平时表现明显变好(Fig. S15)。
- 正文中各重复的细胞数并不完全一致(5,000–20,000 与 rep3「3900 cells」),需看补充图确认。

## 与本研究方向的关系
处在 **detect** 环节的「伪影侧」(伪影注入课题,track A2:质控与伪影)。伪影注入课题要做一个**人类肾脏单细胞基准**,测试 anomaly detector 能否把疾病相关的异常与测量伪影(ambient RNA 等)分开。本文**只用于校准我们注入的 ambient RNA 的强度与谱型**:(1) 强度 —— 每细胞背景比例的经验分布(sc 新鲜组织中位约 3–11%,sn 冷冻组织约 17–35%;每细胞 ρ_c 文件在 Zenodo 每个重复的 `perCell_noMito_CAST_binom.RDS` 中),以及「污染 UMI 绝对量近似恒定、比例随细胞大小下降」这一结构,可直接作为注入模型(固定绝对量 vs 固定比例)的依据;(2) 谱型 —— 背景谱应取自**空液滴**而非细胞平均谱(sn 中 contamination 与 empty 的相关 ~0.85 vs endogenous ~0.50),且 sn 的 ambient 谱中 PT 比例下降、内含子比例偏低;raw `feature_bc_matrix.h5` 提供了构建空液滴谱的原料。(3) 评测设计可借鉴:以「伪影真值」做 RMSLE + Kendall τ,以及用 k-NN 重叠检验「去噪是否伤害细粒度结构」—— 对应我们需要检查伪影注入/去除是否会掩盖或伪造疾病信号。注意它是**小鼠**健康肾脏,不能直接用作人类疾病基准的数据;跨物种/跨平台的强度迁移需要在人类肾脏数据(如 KPMP)的空液滴上再核对。

## 可复用资产
- **代码:** GitHub `Hellmann-Lab/scRNA-seq_Contamination`(GPL-3.0;Snakemake 流程:cellsnp-lite/Vireo 解复用、基因型背景估计 `genotype_estimation_functions.R`、CellBender/DecontX/SoupX 运行与评测脚本),Zenodo 10.5281/zenodo.7941521。
- **数据:** Zenodo 10.5281/zenodo.7328632:`rep1.zip`(1.02 GB)、`rep2.zip`(930 MB)、`rep3.zip`(315 MB)、`nuc2.zip`(812 MB)、`nuc3.zip`(313 MB),每个含 `seurat.RDS`、`seurat_CAST.RDS`、`perCell_noMito_CAST_binom.RDS`(每 CAST 细胞 ρ_c,71–310 KB)、`raw_feature_bc_matrix.h5`、`filtered_feature_bc_matrix.h5`;GEO GSE218853 提供相同的 raw/filtered h5(字节数一致)与 SRA reads。
- **模型:** 无(方法比较研究)。

## 待读
- 读 Additional file 1:Fig. 1B(每重复细胞数与 CAST 比例)、Fig. 2A(rep1 的 ρ_cell 分布)、Fig. S4、Fig. S15(参数敏感性)、Table S1。
- 下载 `perCell_noMito_CAST_binom.RDS`,在 R 中确认列名(按代码应为 cell、Strain、contPerCell_binom、CI_low、CI_high、nSNP),得到每重复 ρ_c 的分位数。
- CellBender(Fleming et al., Nat Methods 2023)、DecontX(Yang et al., Genome Biol 2020)、SoupX(Young & Behjati, GigaScience 2020)、souporcell(Heaton et al., Nat Methods 2020);Caglayan et al. Neuron 2022(脑 snRNA-seq 中 ambient RNA 伪造细胞类型)。

## 引用
```bibtex
@article{Janssen_2023, title={The effect of background noise and its removal on the analysis of single-cell expression data}, volume={24}, ISSN={1474-760X}, url={http://dx.doi.org/10.1186/s13059-023-02978-x}, DOI={10.1186/s13059-023-02978-x}, number={1}, journal={Genome Biology}, publisher={Springer Science and Business Media LLC}, author={Janssen, Philipp and Kliesmete, Zane and Vieth, Beate and Adiconis, Xian and Simmons, Sean and Marshall, Jamie and McCabe, Cristin and Heyn, Holger and Levin, Joshua Z. and Enard, Wolfgang and Hellmann, Ines}, year={2023}, month=June }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
