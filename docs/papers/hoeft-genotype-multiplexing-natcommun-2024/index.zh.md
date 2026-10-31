# Label-free single-cell RNA multiplexing leveraging genetic variability

> **文献键** `Hoeft_2024` · **来源** Nature Communications(2024) · **类别** single-cell · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1038/s41467-024-54270-6> · `status: complete`

---

## 一句话
Hayat/Kramann 组提出 **SoupLadle**:先用 Souporcell 按 SNP 对 pooled sc/snRNA-seq 做无参考 deconvolution,再用每位患者的 bulkRNA-seq SNP 通过 Hamming 距离 + Kuhn-Munkres 匹配把 genotype cluster 还原到患者;在 PBMC、两个心脏 snRNA 队列和 **4 例冷冻人肾活检 snRNA**(11,490 nuclei)上召回率最高、cell-type bias 最小。

## 研究问题
大规模人类单细胞队列受限于成本和批次效应。Multiplexing 能同时降本、减批次,但 cell-labeling(CellPlex/Hashtag)需要额外染色和洗涤,对细胞核损失很大("~20–30% of nuclei are lost with each washing step");而纯 SNP 方法(Vireo、Souporcell)不带参考基因型时只能 "discriminate (…deconvolute), but do not re-assign cells to patients"。Vireo 可用 bulkRNA/WES 先验做 demultiplexing,但只使用参考里也测到的 SNP,召回下降,对稀有细胞类型尤甚。问题:如何在冷冻组织 snRNA 上做简单、高召回、且能回到具体患者的 genetic multiplexing?

## 方法

SoupLadle 四步 (Fig. 1h):(1) 每位患者做 bulkRNA-seq(STAR 比对,freebayes `-iXu --min-mapping-quality 30 --min-base-quality 10 --min-coverage 5` 调 SNP),**事先**评估 SNP 异质性以挑选可 pool 的样本;(2) pooled 10x 3′ v3.1 sc/snRNA-seq;(3) 在 pooled BAM 上 freebayes 调候选 SNP → Vartrix 计 allele → Souporcell 2.4 聚类(`--num_clusters` = 供体数)+ troublet 识别 doublet;(4) 把 Souporcell 各 genotype cluster 与 bulk SNP profile 求 normalized Hamming 距离矩阵,用 Kuhn-Munkres(Hungarian)做一对一指派。关键论点:deconvolution 阶段可用 scRNA 中**所有** SNP,而不是只用参考里也有的 SNP,所以稀有细胞类型也能被分配。对照方法:CellPlex、Hashtag(TotalSeq-A anti-nuclear-pore)、Souporcell(Vartrix 或 minimap2)、Vireo 0.5.7(cellSNP-lite 或 Vartrix SNP;有/无 bulkRNA 或 WES 先验)。doublet 参考:scDblFinder(top 4000 genes,score > 3)。CellRanger 7.1.0 + GRCh38-2020-A,demultiplexing 前不设 QC cutoff;Seurat 聚类(4000 HVG,res 0.1)作为 PBMC 的 ground truth。

## 数据

| 数据集 | 设计 | 平台 | 细胞/核数 | 真值 |
|---|---|---|---|---|
| PBMC (P1–5) | 每人 FACS 分选一种 PBMC 亚群 (CD14 Mono / CD16 Mono / CD4 T / CD8 T / CD19 B),各 100,000,pool;CellPlex 标记;bulkRNA + WES | 10x 3′ v3.1, Chip G | 17,892 | 细胞类型 = 患者 (FACS 设计) + CellPlex |
| Heart 1 (P6–10) | 冷冻心肌 snRNA,CellPlex + Hashtag 双标记;bulkRNA + WES | 10x 3′ v3.1, Chip G | 1,563 | CellPlex / HTO |
| Heart 2 (P11–18) | 冷冻心肌 snRNA,每人 ~50,000 nuclei 分选后 pool,无标记;bulkRNA | 10x 3′ HT v3.1, Chip M | 11,501 | 仅方法间一致性 |
| **Kidney (P19–22)** | **4 例冷冻人肾活检**(3 男 1 女),"total processed biopsies were pooled prior to sorting",DAPI⁺ nuclei 分选,无标记;bulkRNA(**无 rRNA depletion**),无 WES | **10x 3′ v3.1 (Dual Index), Chip G, snRNA** | **11,490** | 仅方法间一致性 |

另有一个已发表的 5′ scRNA 心脏数据 (Koenig 2022) 只用于 SNP 分布分析。肾样本的**疾病/临床诊断在论文、补充材料、GEO 与 BioSample 中均未给出**(伦理批号 Erasmus MC MEC-2021-0840)。

## 主要结果

- **PBMC**:Souporcell 精度/召回最高;Vireo 加 bulkRNA/WES 先验"marginal improvement in precision, but a distinct loss in cell recall";排除 doublet 后所有方法精度 ≈ 98.5%。CellPlex 精度较低源于 doublet 高估(CellPlex 3,947 doublets + 3,524 unassigned vs Souporcell 2,373 + 34,共 17,892 cells)。bulkRNA 比 WES 回收更多 scRNA SNP(尤其 3′UTR)。随机下采样 bulk SNP(1.0→0.2,n = 10)时 SoupLadle 显著优于 Vireo(Wilcoxon, p < 0.0001)。
- **Heart 1**:SoupLadle 几乎全部分配;CellPlex/Hashtag/Vireo CellSNP bulkRNA 约 75%;Vireo CellSNP WES 仅 ~12.5%。方法间重叠 > 95%(WES 除外)。
- **Heart 2 (n = 8)**:SoupLadle 分配 99%,Vireo Vartrix bulkRNA 81%,Vireo CellSNP bulkRNA 45%。
- **Kidney (n = 4, 11,490 nuclei)**:SoupLadle 分配 96%(singlets 10,781;**doublets 250 = 2.2%**;unassigned 459 = 4.0%);Vireo Vartrix bulkRNA 21%;Vireo CellSNP bulkRNA < 1%。SoupLadle 与 Vireo Vartrix 重叠 ~93%。Vireo 对 podocytes、fibroblasts、intercalated cells 等稀有类型分配差,SoupLadle "no apparent cell-type bias"。
- **(我们从 Source Data Fig2j 自行汇总的数字)** 肾表达聚类中 "Mixed/Doublets" 簇有 4,488 nuclei(39%),但 SoupLadle 只把其中 123 个判为跨供体 doublet,308 个 unassigned,其余 4,057 个归给单一供体;"Low Quality" 簇 434 个。即:表达上的"doublet/mixed"簇大部分在基因型上是单一供体。
- 成本:8 样本 multiplexing 约 4 倍降本(Supplementary Data 1)。
- 环境 RNA:**未定量**。原文:"while we do not provide a tool for ambient RNA correction, ambient RNA can be imputed with standard packages (CellBender, SoupX) or Souporcell"。

## 创新点
- 系统对比 CellPlex、Hashtag、Souporcell、Vireo(± bulkRNA/WES)在 PBMC、心脏、肾三类样本上的表现,其中 PBMC 用 FACS 设计提供"细胞类型 = 患者"真值。
- SoupLadle:先 deconvolute 后匹配,两步解耦,在 SNP 稀少和稀有细胞类型上更稳健;提供 R 包和样本 pool 前的 SNP 异质性评估。
- 实证:snRNA 的 SNP 主要落在 intron 与 3′UTR,所以 bulkRNA-seq 比 WES 更适合作为参考基因型。

## 局限
- 心脏 2 与肾数据集没有独立的标签真值(没做 CellPlex/HTO),只能看方法间一致性;作者自称 "proof of concept"。
- 肾仅 4 例,未报告疾病、年龄或活检指征;bulkRNA 未做 rRNA depletion。
- SNP 方法只能检出**跨供体**(heterotypic)doublet;同供体 doublet 不可见。论文未讨论这一点。
- 没有量化 ambient RNA 或 contamination。
- 公开数据的小问题:GEO 中 Heart_2 的 SRA run (SRR29832268) 显示 0 spots;Heart_2 Patient 18 的 bulk run (SRR29830135) 与 Heart Patient 10 (SRR26826519) 的 spots/bases 完全相同,疑似重复上传(**未核实**)。

## 与本研究方向的关系

属于 **detect** 阶段的数据/真值来源,而非方法。伪影注入课题要建立一个人肾单细胞 benchmark,检验 anomaly detector 能否把疾病信号与测量伪影(ambient RNA、doublet、protocol)区分开,并在供体层面用 conformal 控制误报。这个数据集是少见的**真实人肾、多供体 pooled、带每供体 bulk 基因型**的 snRNA:
1. **跨供体 doublet 真值**:基因型 doublet 是独立于表达的标签。在 4 个供体、比例不等时,只有部分 doublet 是跨供体的。这是 lower bound,不是完整 doublet 集合,但足以评估"表达型 doublet 检测器 / anomaly score 是否误把稀有细胞或疾病状态当 doublet"。Source Data 显示表达上的 "Mixed/Doublets" 簇大多是单一供体,是现成的反例池。
2. **Ambient RNA 真值**:pooled 多供体时,每个核里"错误供体等位基因"的比例就是对 ambient/contamination 的基因型估计(Souporcell 本身就估计 ambient 比例;思路同 Janssen 2023 的 genotype-based ground truth)。论文没做,需要我们从 FASTQ 重算。
3. **Donor 层面 conformal**:4 个供体可做 leave-one-donor-out 的小规模校准实验,但 n = 4 太小,只能做 sanity check,不能作为主结果。
4. 局限:疾病状态未知,故无法作为"疾病 vs 伪影"中的疾病一侧;只能做伪影一侧的真值。

## 可复用资产
- **代码:** SoupLadle R 包 https://github.com/ToreBle/SoupLadle(Zenodo 10.5281/zenodo.13711299);含 souporcell/vireo shell 脚本与 PBMC/Heart 分析脚本,**仓库中没有肾的分析脚本或每细胞分配表**。
- **数据:** GEO GSE247708(SuperSeries:GSE247706 bulk VCF,GSE247707 pooled 10x);肾 pooled snRNA = GSM8397034,只有 `barcodes/features/matrix`(11,490 barcodes × 36,601 genes,cellranger-7.1.0)。GEO 标注为 "raw_feature_bc_matrix",但条形码数等于 cell-called 数,实为**过滤后矩阵**,没有 empty droplets,也没有分配表;肾 bulk VCF = GSM8397029–32 (TS116/120/121/126)。FASTQ 公开:BioProject PRJNA1040187;肾 snRNA run SRR29832267(809M spots, ENA R1 16.5 GB + R2 32.8 GB);肾 bulk SRR29830128–31(约 1.5–1.7 GB/例)。WES(仅 PBMC/心脏)在 EGA EGAD50000000928,受控访问。Source Data 提供肾每细胞类型 × 供体计数(Fig2j)。PBMC (GSM7899153, 2,739,993 barcodes) 和 Heart 1 (GSM7899155, 1,080,502) 是真正的 raw 矩阵,并附 CMO/HTO assignment tables。
- **模型:** 无(非学习模型)。

## 待读
- 从 SRR29832267 重跑 CellRanger(得到真 raw 矩阵 + BAM)→ Souporcell(k = 4,含 ambient 估计)→ SoupLadle 匹配 GEO 肾 VCF,复现 250 doublets / 459 unassigned,然后再算每核的跨供体等位基因比例。
- 向作者 (Hayat/Bleckwehl) 询问肾样本的疾病/临床信息和每细胞分配表。
- 对照 Janssen 2023(基因型 ambient 真值)与 Heaton 2020 Souporcell 的 ambient 估计。

## 引用
```bibtex
@article{Hoeft_2024, title={Label-free single-cell RNA multiplexing leveraging genetic variability}, volume={15}, ISSN={2041-1723}, url={http://dx.doi.org/10.1038/s41467-024-54270-6}, DOI={10.1038/s41467-024-54270-6}, number={1}, journal={Nature Communications}, publisher={Springer Science and Business Media LLC}, author={Hoeft, Konrad and Bleckwehl, Tore and Schumacher, David and Kim, Hyojin and Meyer, Robert and Long, Qingqing and Zhang, Ling and Möller, Christian and Clahsen-van Groningen, Marian C. and Babler, Anne and Saritas, Turgay and Kurth, Ingo and Milting, Hendrik and Hayat, Sikander and Kramann, Rafael}, year={2024}, month=Dec }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
