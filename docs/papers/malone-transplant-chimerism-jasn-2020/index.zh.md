# Harnessing Expressed Single Nucleotide Variation and Single Cell RNA Sequencing To Define Immune Cell Chimerism in the Rejecting Kidney Transplant

> **文献键** `Malone_2020` · **来源** Journal of the American Society of Nephrology(2020) · **类别** single-cell · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1681/asn.2020030326> · `status: complete`

---

## 一句话
用 donor/recipient 配对 WES 生成 SNV 参考(.vcf),对 5 个肾移植活检的 10x 5′ scRNA-seq(81,139 个细胞)跑 Demuxlet,逐细胞判定供体/受体来源,发现供体巨噬细胞在非排斥移植肾中可持续存在、且与受体巨噬细胞转录程序不同。

## 研究问题
实体器官移植中通常假设供体来源免疫细胞术后逐渐消失,但它们是否在肾移植物中持续存在、是否参与排斥一直未知,原因之一是缺乏区分供/受体细胞的手段(以往只能靠性别错配时的 Y 染色体)。本文提出用表达的 SNV + scRNA-seq 在单细胞分辨率上界定白细胞嵌合(leukocyte chimerism)。

## 方法
(1) 活检新鲜解离(0.25% trypsin + DNase I,约 30 min,活率约 90%);每个活检 2 条 10x Chromium lane(目标 10,000 细胞/lane),**5′ 试剂盒** + T 细胞 VDJ 文库;测序深度 50,000 reads/cell(GEX)。(2) Cell Ranger 3.0 → Seurat v3;QC:200–2500 genes/cell、<25% 线粒体;高分辨率过聚类后,"含两种及以上 cell-type 标志基因的 cluster 作为 doublet cluster 删除",低基因数 cluster 作为 debris 删除;Seurat v3 integration。(3) 外周血 germline DNA 做 WES(目标 50×),BWA-MEM → Picard MarkDuplicates → GATK BQSR → GATK best-practice 过滤常见变异(AF>0.05);每对 donor+recipient 合并 .vcf(平均 120,896 个编码 SNV)。(4) Demuxlet(默认参数,α=0、0.5、1)输入合并 .vcf + Cell Ranger BAM,以 BEST 列标注每个细胞 donor/recipient。(5) 差异表达(Seurat FindMarkers)+ ToppFun 通路;Spearman 相关;VDJ Loupe 做 T 细胞克隆。

## 数据
5 个肾移植指征活检(Washington University):3 例急性抗体介导排斥(ABMR,均有 DSA)+ 2 例非排斥 AKI;移植后 5 天至 7 年。另有一个"独立数据集":同一 ABMR 患者治疗前/治疗后 1 个月的连续活检(Fig 3G,GEO 中标为 **3′** 试剂盒,不在 81,139 细胞主数据集里)。GEO **GSE145927**:7 个 scRNA 样本(Biopsy1_Day28、Biopsy2_Day2542、Biopsy3_Day11、Biopsy4_Day5、Biopsy5_Day232 为 5′;Biopsy6_Pre-treatment、Biopsy7_Post-treatment 为 3′)+ 10 个 WES 样本(5 对 donor/recipient,PBMC,IDT xGen Exome v1,NovaSeq6000)。处理后文件:每个样本一个 `*rawcounts.csv.gz`(基因 × 细胞 UMI 计数,**只含 QC 后细胞**,如 Day11 文件 = 5,395 个细胞 = metadata 中 biopsy65)+ `GSE145927_MGI.metadata.csv.gz`(81,139 个细胞:biopsy、nCount/nFeature、percent.mt、cluster、`SNV_GT`(donor/recipient)、`stim`(rejn/no_rejn)、细胞类型)。原始 FASTQ(scRNA 与 WES)在 SRA **SRP250734 / PRJNA608747**,runinfo 显示为公开下载(非 dbGaP);GEO 上 WES 样本无处理后文件(无 VCF)。

## 主要结果
- 81,139 个细胞通过 QC(平均 1,124 genes / 2,497 transcripts);8 个肾细胞 cluster + 2 个免疫 cluster;巨噬细胞 5,027、淋巴细胞 3,647(T 3,067、B 190、浆细胞 231;另亚聚类出肥大细胞 111)。
- 每个细胞用到的 SNV 中位数 71–231,最少 17;作者称整体约 90% 准确、下四分位以上细胞接近 100%。
- "Despite manual filtering and removal of doublet cells … the Demuxlet tool identified 3%–10.5% of cells as doublets"(手工去 doublet 之后 Demuxlet 仍判出 3–10.5% doublet)。
- 巨噬细胞:受体 3,798 / 供体 1,229;淋巴细胞:受体 1,528 / 供体 2,119。非排斥样本供/受体巨噬细胞约各半,排斥样本受体主导(如 Day 11 排斥活检受体 97%;Day 28 非排斥活检供体 35.8%)。淋巴细胞的供体比例随时间下降(Day 232 时很少)。
- 受体巨噬细胞:IL-6、IFN、FCγR 通路,CD16/CD68;供体巨噬细胞:补体(C1QA/B/C)、抗原呈递、F13A1、CD14。受体 T 细胞与排斥 T 细胞相关(Spearman 0.8),表达 NKG7/GNLY/GZMB/PRF1;供体 T 细胞与非排斥 T 细胞相关(1.0),富集氧化磷酸化(静息)。
- VDJ:仅 120/3,115 个 T 细胞有完整 VDJ(供体 34,全部来自 Day 11 排斥样本;受体 86)。

## 创新点
- 首次把 donor/recipient 配对 WES + Demuxlet 用于人肾移植活检 scRNA-seq,逐细胞界定白细胞嵌合。
- 发现供体巨噬细胞可在非排斥移植肾持续存在,且与受体巨噬细胞功能程序不同(补体/抗原呈递 vs. 炎症激活)。
- 公开了 5′ scRNA + 配对 WES 原始数据,构成一个带"遗传身份"标签的人肾组织数据集。

## 局限
- 样本极小(5 个活检、3 vs 2),作者自称 proof-of-concept;排斥与时间点混杂。
- 正文没有给出 Demuxlet 对上皮/内皮/基质细胞的来源比例,也没有讨论 ambient RNA 或 soup 污染;"所有肾实质细胞均为供体来源"只是生物学预期,文中未逐项报告(补充材料未能获取,未核实)。
- Demuxlet 判定的 doublet 未在 GEO metadata 中提供(最终数据集只有 donor/recipient 标签);doublet 在 QC 中已被部分人工删除,因此公开矩阵不是"原始 doublet 分布"。
- **公开 metadata 中的 `SNV_GT` 与正文不符**(我们自行统计):巨噬细胞 donor 4,715 / recipient 312(正文为 donor 1,229 / recipient 3,798),且每个活检内各细胞类型的 recipient 比例几乎相同(biopsy65:22.6–29.3%;biopsy62:3.6–5.6%),不像真实的细胞类型特异嵌合。可能是标签与条形码错配或含义不同——使用前必须从 SRA 重跑 demuxlet/vireo。
- 正文称测序平台为 HiSeq,但 SRA runinfo 记为 NovaSeq 6000;小细节,但说明公开记录与正文不完全一致。

## 与本研究方向的关系
属于伪影注入课题的 **detect** 环节中的"伪影 ground truth"数据源。我们的 benchmark 要检验 anomaly detector 能否把疾病(排斥/AKI)与测量伪影(ambient RNA、doublet)分开,并在 donor 层面控制误报。本数据集的价值:(1) **doublet 真值**:同一 lane 混有供体与受体两种基因型,demuxlet 能识别异基因型 doublet(donor+recipient),论文报告 3–10.5%;但同基因型 doublet(donor+donor,在以供体上皮为主的组织里应占多数)无法被基因型识别,所以只是部分真值,需要用异基因型比例按 Demuxlet 原文的公式外推。(2) **ambient 真值(我们自己的推断,论文未提及)**:肾实质上皮细胞理论上全为供体来源,其中检出的受体特异等位基因 reads 可以作为来自受体浸润免疫细胞的 ambient/soup 污染的直接估计——与 Janssen 2023(Genome Biology)用小鼠品系混合估计 background noise 的逻辑相同。论文没有提出或验证这一点。(3) 有排斥 vs 非排斥 = 真实"疾病"信号,可作为对照。限制:只有 5 个 donor 对,donor 层面误报控制统计功效很弱;要做 (1)(2) 必须从 SRA 下载 BAM/FASTQ(单个 scRNA run 约 30–65 GB)+ WES 自行 call 变异,GEO 处理后文件不够。

## 可复用资产
- **代码:** 未公开代码;流程为标准工具(Cell Ranger 3.0、Seurat v3、GATK、Demuxlet)。
- **数据:** GEO GSE145927(QC 后计数矩阵 + 81,139 细胞 metadata,含 `SNV_GT`,但见局限);SRA SRP250734(scRNA FASTQ 17 个 run + WES FASTQ 10 个 run,公开)。无 VCF、无 raw droplet 矩阵、无 doublet 标签。
- **模型:** 无。

## 待读
- 补充材料(Supplemental Methods 的 doublet 去除细节、Supp Table 1 临床信息、Supp Fig 1 每样本 droplet 直方图)——未能获取,需手动下载。
- Kang et al. 2018(Demuxlet,Nat Biotechnol)——异基因型 doublet 外推公式。
- 与 janssen-ambient-noise-genomebiol-2023 对照:基因型法估计 ambient 的方法学可直接迁移。
- 核实 `SNV_GT` 与正文不符的原因(联系作者或从 SRA 重跑)。

## 引用
```bibtex
@article{Malone_2020, title={Harnessing Expressed Single Nucleotide Variation and Single Cell RNA Sequencing To Define Immune Cell Chimerism in the Rejecting Kidney Transplant}, volume={31}, ISSN={1533-3450}, url={http://dx.doi.org/10.1681/ASN.2020030326}, DOI={10.1681/asn.2020030326}, number={9}, journal={Journal of the American Society of Nephrology}, publisher={Ovid Technologies (Wolters Kluwer Health)}, author={Malone, Andrew F. and Wu, Haojia and Fronick, Catrina and Fulton, Robert and Gaut, Joseph P. and Humphreys, Benjamin D.}, year={2020}, month=July, pages={1977–1986} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
