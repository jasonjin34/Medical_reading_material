# Single-cell multi-omic and spatial profiling of human kidneys implicates the fibrotic microenvironment in kidney disease progression

> **文献键** `Abedini_2024` · **来源** Nature Genetics(2024) · **类别** single-cell · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1038/s41588-024-01802-x> · `status: complete`

---

## 一句话
Susztak 实验室(UPenn)的人肾多组学 + 空间图谱:来自 58 名参与者(补充表 1 实际列出 57 个 ID)的 81 份样本,做了 scRNA-seq、snRNA-seq、snATAC-seq(三者独立建库,不是 multiome)、Visium FFPE 和 CosMx。整合后的 SCVI 图谱有 338,565 个细胞/细胞核、44 种主要细胞类型和 114 种亚型/状态。Visium 经 NMF 分出四种微环境(肾小球 / 小管 / 纤维化 / 免疫)。由纤维化微环境得到的 FME 基因签名(FME-GS),在 fibrosis < 10% 的 245 例 bulk 小管样本中仍能预测肾功能下降(HR = 3.95),而病理纤维化评分做不到(HR = 1.17)。

## 研究问题
慢性肾病(CKD)的 75% 以上由糖尿病和高血压引起,纤维化是所有进展性 CKD 的共同终点。但纤维化灶的细胞组成和空间组织还不清楚:过去的工作主要盯着 ECM 堆积。解离式单细胞数据又丢掉了位置信息,所以只按解剖位置定义的细胞(系膜细胞、PEC、各类成纤维细胞)很难给出分子身份。临床上,早期 CKD(eGFR 尚保留、纤维化 < 10%)的预后很难判断,病理纤维化评分的预测价值也不稳定。

## 方法
**湿实验**:scRNA-seq 用**新鲜**肾组织(0.5 g),Miltenyi Multi Tissue Dissociation Kit 1 在 37 °C 酶解 30 min,再做 RBC lysis,活率 > 80%。snRNA-seq 用**冻存**组织(10–30 mg),NP40 裂解后 gentleMACS 匀浆。两者都用 10x Chromium Next GEM 3′ v3.1(Chip G),在 NovaSeq 6000 上测序。snATAC-seq 用同一套核提取流程,10x Chromium Single Cell ATAC(Chip E),**和 RNA 是分开建库的,不是 multiome**。Visium 是 FFPE 探针版,样本要求 DV200 > 50%,切片 5 µm。CosMx 用约 1,000 基因的 universal cell characterization panel,另加 50 个自定义探针。IMC(Hyperion)和免疫荧光做蛋白验证。
**生信**(补充材料):Cell Ranger v6.0.1 / Cell Ranger ATAC。ambient RNA 用 SoupX v1.5.0 校正,doublet 用 DoubletFinder v2.0(默认参数)去除。阈值为 nFeature 在 200–3000 之间、线粒体比例 sn < 15% 且 sc < 50%、核糖体比例 < 15%。之后先去掉同时表达多类 marker 的簇,再把注释与已发表参照的 label transfer 结果比对,不一致的细胞视为 doublet 剔除。sn 和 sc 分别用 Harmony 处理。三种模态再用 SCVI(v0.20.3,covariates 为 sample、nFeature_RNA、nCount_RNA、tech)整合成一个 atlas,并与 KPMP 合并成约 60 万个细胞的版本。Visium 用 Cell2location 反卷积、CellTrek 映射到近单细胞分辨率(149,717 个点),再用 STutility NMF 划分微环境。细胞通讯用 CellChat 和 COMMOT,iPT 轨迹用 Monocle3,FME-GS 用 bulk 层次聚类,预后用 Kaplan–Meier/Cox,另做 LASSO。

## 数据
**组织来源**:Reporting Summary 原文为 "The un-affected portions of nephrectomies mostly due to tumor"(肿瘤肾切除术的未受累部分),属于 medical discard,豁免知情同意。取材部位为皮质和外髓。**分组**:正文写 control 36 份样本(eGFR > 60 且 fibrosis < 10%),CKD 45 份(DKD 20 份、HKD 25 份)。
**供体数**(按补充表 1,唯一 ID 计,对照 / DKD / HKD):scRNA 14 / 4 / 8,共 26 名供体、29 个文库(HK1635、HK1650、HK1664 各有 G/T 两个文库);snRNA 7 / 3 / 8,共 18 人;snATAC 7 / 4 / 2,共 13 人、18 个文库(重复文库);Visium 3 / 6 / 5,共 14 人;CosMx 1 / 1(HK3039 为对照,HK2844 为 DKD)。sc 与 sn 有 **8 名供体重叠**(对照 HK2833、HK2867、HK2893、HK2895、HK2899;HKD HK2770、HK2774、HK2891)。做过 sc 或 sn RNA 的对照供体共 16 人。
**细胞数**(GEO 细胞级 metadata):scRNA 126,963 个(对照 53,311 / 疾病 73,652),snRNA 155,647 个(53,416 / 102,231),snATAC 55,955 个(30,103 / 25,852;正文写 57,847),合计 338,565 个。
**各来源计数不一致**:Reporting Summary 按文库计,sc 为 15/4/10、sn 为 7/4/7、ATAC 为 10/6/2。正文称 Visium 为 "seven DKD and four HKD",补充表 1 是 6 DKD / 5 HKD。GEO 的样本标签也和补充表 1 有冲突,例如 HK2478 在 GEO 标 HKD、在补充表标 DKD;GEO 的 "Disease18_snRNAseq" 标成 Control。
**外部 bulk 队列**:292 例显微切割的小管 bulk RNA-seq(GSE115098、GSE173343)。

## 主要结果
- **图谱**:338,565 个细胞/细胞核,6 个超家族,44 种主要类型,114 种亚型/状态。图谱中有 11 种内皮细胞(包括 FBLN5+ 入/出球小动脉和 MCTP1+ 直小血管)、稀有的 EPO 产生细胞、SLC47A2-high PT,以及完整的免疫亚群;与 KPMP 整合后共 588,425 个细胞。
- **间质**:共 12 种亚型,找到能区分它们的 marker:系膜细胞为 ITGA8/POSTN,VSMC/周细胞为 MYH11/NOTCH3/NTRK3,成纤维细胞为 KCNK2/FAP,肌成纤维细胞为 COL1A1/SYNPO2。肌成纤维细胞的 ECM 评分最高,且在疾病样本中比例更高。
- **FME**:NMF 分出的纤维化微环境与病理纤维化评分相关(r = 0.75,P = 0.003)。FME 里同时有成纤维细胞、肌成纤维细胞、内皮、免疫细胞(早期三级淋巴结构样聚集)和 iPT,并富集 SPP1、CXCL12、CCL19/21、PDGFB 和 TGFB1 信号。
- **iPT 两种亚型**:iPT_VCAM1+ 是代谢型,"present in healthy samples";iPT_HAVCR1+(KIM1)偏黏附和基质,主要出现在 CKD 样本和 FME 中。Monocle 显示一条 PT → iPT 的连续轨迹。CosMx 进一步分出 iPT_APOE、iPT_SPP1 和 iPT_KRT7,三者的邻居组成不同。
- **预后**:在 292 例 bulk 样本上,按 FME-GS 聚类得到的 cluster 1 到达终点的概率约高 4 倍(终点为 eGFR 下降 40% 或 ESRD)。在 245 例 fibrosis < 10% 的样本上,FME-GS 的 HR = 3.95(95% CI 1.71–9.12),病理纤维化评分的 HR = 1.17(0.49–2.83)。只用 LASSO 选出的前 10 个基因仍然显著(P = 0.021),随机基因集则不显著。

## 创新点
- 在同一批肾切除样本上并用 sc、sn、ATAC、Visium、CosMx、IMC 互相验证,给只按解剖位置定义的细胞(PEC、系膜细胞、成纤维细胞亚型)补上分子 marker。
- 把"纤维化"从 ECM 堆积重新定义为多细胞的空间微环境(FME),并证明 FME 签名在早期 CKD 里比病理评分更能预测预后。
- 公开发布多个处理好的 h5ad(含与 KPMP 的联合整合)以及交互网站。

## 局限
- 作者自己承认:HKD 未必是单一疾病;FME-GS 需要外部队列验证;iPT 和免疫细胞的功能需要机制实验。
- 单细胞统计 "treat each cell as an independent observation"(伪重复),组间比例差异的 P 值偏乐观。
- 设计层面有混杂:sc 用新鲜酶解,sn 用冻存组织,两者的组别构成不同。早期 HK1xxx 批次几乎全是 sc,后期 HK28xx 批次 sc 和 sn 都有。补充表 2 中,对照组 scRNA 文库的 median genes/cell 中位数约 358,疾病组约 598,有的对照低到 17(HK2662)和 70(HK2899 SC)。也就是说,**测量质量与疾病标签相关**。
- 计数在正文、补充表、Reporting Summary 和 GEO 之间多处不一致(见"数据"一节)。原始 FASTQ 未公开("Raw data were not provided due to privacy concerns")。
- "健康"对照其实是肿瘤肾切除的旁组织,而且 25 名对照中有 8 名标注了高血压;作者也观察到对照中存在 iPT_VCAM1+ 细胞以及低度纤维化。

## 与本研究方向的关系
**位置**:属于 detect 阶段的数据基础。在课题 1(人肾单细胞基准,检验异常检测器能否把疾病和测量/取材伪影分开,并在供体层面用 conformal 控制误报)中,它是**第二队列**:用另一个实验室的健康供体来检验误报率能否迁移。
**有利之处**:(1) 对照组规模可用。按供体计,sc 有 14 人、sn 有 7 人,合计 16 人。有 5 名对照同时做了 sc 和 sn,可以作为**同一供体、不同 protocol**的天然配对,直接测量"protocol 伪影会不会触发误报"。(2) 有细胞级 QC 协变量(nCount、nFeature、percent_mt)和 tech 标签,可以用来构造伪影轴。(3) 取材是肿瘤肾切除,与 KPMP 的活体活检和 Lake 2023 的混合来源不同,正好可以作为"取材方式"这一 shift。
**风险**(必须写进 benchmark 设计):(a) 对照组 sc 文库质量系统性偏低,如果直接比较疾病和对照,检测器可能学到的是质量而不是疾病,所以应该先在对照内部做 conformal 校准。(b) GEO 上的对象已经过 SoupX 校正(metadata 里的 nCount_RNA 是非整数),也已经过 DoubletFinder、nFeature ≤ 3000 截断、按线粒体比例过滤和 marker 层面的 doublet 剔除。也就是说,**伪影已被部分清掉,而且各样本的处理方式不同**,没有 FASTQ 就无法统一重处理。(c) 每个模态的供体数很少(sn 对照只有 7 人),供体层面 conformal 的校准集太小,只能做 leave-one-donor-out,或者把 sc 和 sn 合并后按 tech 分层。(d) 有些样本细胞数极少(HK2976 SN 只有 12 个、HK2899 SC 只有 183 个、HK1635_T SC 有 491 个),应设最小细胞数门槛。(e) 对照里有高血压患者和 iPT_VCAM1+ 细胞,"健康"标签本身有噪声,需要按 eGFR/fibrosis 做敏感性分析。(f) GEO 这个 series 还被 4 篇其他 PMID 引用,同实验室的其他数据可能与本数据有供体重叠(**未核实**),合并队列前需要按 HK ID 去重。

## 可复用资产
- **代码:** GitHub `amin69upenn/Human_Kidney_Multiomics_and_Spatial_Atlas_` 与 `jlevins2010/FME_atlas`,两个仓库都没有 LICENSE 文件。
- **数据:** GEO GSE211785 只提供处理后数据:merged PreSCVI h5ad(4.7 GB)、PostSCVI h5ad(5.5 GB)、与 KPMP 联合整合的 h5ad(9.0 GB)、counts .rds(1.7 GB)、细胞 metadata(9.1 MB)、CosMx h5ad(620 MB)、Visium counts .rds(135 MB)以及 Visium tif/json(RAW.tar 1.2 GB 也只装着 7 个 Visium 样本的 tif/json)。没有找到明确的许可声明。交互网站:susztaklab.com/hk_genemap 和 susztaklab.com/samui。bulk 数据见 GSE115098 和 GSE173343。
- **模型:** 无预训练权重;PostSCVI h5ad 里可能带有 SCVI latent(未下载核实)。

## 待读
- 下载 PreSCVI h5ad,核实三点:`X` 和 layers 里是原始整数 counts 还是 SoupX 校正后的计数;是否保留了每个样本的 batch/HK ID;sc 与 sn 是否用同一套基因。
- 核对 GSE211785 关联的其他 4 个 PMID(38217002、38514613、40796935、41376591),确认这些同实验室数据与本数据有没有供体重叠。
- 与 Lake 2023(KPMP)的对照组对比:取材方式(肾切除、活检、死亡供体)作为 benchmark 的 procurement 轴。

## 引用
```bibtex
@article{Abedini_2024, title={Single-cell multi-omic and spatial profiling of human kidneys implicates the fibrotic microenvironment in kidney disease progression}, volume={56}, ISSN={1546-1718}, url={http://dx.doi.org/10.1038/s41588-024-01802-x}, DOI={10.1038/s41588-024-01802-x}, number={8}, journal={Nature Genetics}, publisher={Springer Science and Business Media LLC}, author={Abedini, Amin and Levinsohn, Jonathan and Klötzer, Konstantin A. and Dumoulin, Bernhard and Ma, Ziyuan and Frederick, Julia and Dhillon, Poonam and Balzer, Michael S. and Shrestha, Rojesh and Liu, Hongbo and Vitale, Steven and Bergeson, Andi M. and Devalaraja-Narashimha, Kishor and Grandi, Paola and Bhattacharyya, Tanmoy and Hu, Erding and Pullen, Steven S. and Boustany-Kari, Carine M. and Guarnieri, Paolo and Karihaloo, Anil and Traum, Daniel and Yan, Hanying and Coleman, Kyle and Palmer, Matthew and Sarov-Blat, Lea and Morton, Lori and Hunter, Christopher A. and Kaestner, Klaus H. and Li, Mingyao and Susztak, Katalin}, year={2024}, month=July, pages={1712–1724} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
