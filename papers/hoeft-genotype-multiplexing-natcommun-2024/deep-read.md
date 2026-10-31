# Label-free single-cell RNA multiplexing leveraging genetic variability

> **Bibkey** `Hoeft_2024` · **Venue** Nature Communications (2024) · **Category** single-cell · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1038/s41467-024-54270-6>
> `status: complete` — 基于开放全文 (PMC11621319)、Supplementary Information、Supplementary Data 1–2 与 Source Data,以及 GEO GSE247708 / SRA PRJNA1040187 元数据 (2026-10-26 核对)。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> Hayat/Kramann 组提出 **SoupLadle**:先用 Souporcell 按 SNP 对 pooled sc/snRNA-seq 做无参考 deconvolution,再用每位患者的 bulkRNA-seq SNP 通过 Hamming 距离 + Kuhn-Munkres 匹配把 genotype cluster 还原到患者;在 PBMC、两个心脏 snRNA 队列和 **4 例冷冻人肾活检 snRNA**(11,490 nuclei)上召回率最高、cell-type bias 最小。
<!-- EN --> Hayat/Kramann lab present **SoupLadle**: reference-free SNP deconvolution of pooled sc/snRNA-seq with Souporcell, then re-assignment of each genotype cluster to a patient by Hamming distance + Kuhn-Munkres matching against per-patient bulkRNA-seq SNPs; it gives the highest recall and least cell-type bias on PBMC, two heart snRNA cohorts and **4 frozen human kidney biopsies (snRNA, 11,490 nuclei)**.

## 研究问题 / Problem
<!-- ZH --> 大规模人类单细胞队列受限于成本和批次效应。Multiplexing 能同时降本、减批次,但 cell-labeling(CellPlex/Hashtag)需要额外染色和洗涤,对细胞核损失很大("~20–30% of nuclei are lost with each washing step");而纯 SNP 方法(Vireo、Souporcell)不带参考基因型时只能 "discriminate (…deconvolute), but do not re-assign cells to patients"。Vireo 可用 bulkRNA/WES 先验做 demultiplexing,但只使用参考里也测到的 SNP,召回下降,对稀有细胞类型尤甚。问题:如何在冷冻组织 snRNA 上做简单、高召回、且能回到具体患者的 genetic multiplexing?
<!-- EN --> Large human single-cell cohorts are limited by cost and batch effects. Multiplexing reduces both, but cell labeling (CellPlex/Hashtag) needs extra staining and washes that destroy nuclei ("~20–30% of nuclei are lost with each washing step"), while SNP methods without a reference genotype only "discriminate (…deconvolute), but do not re-assign cells to patients". Vireo can use bulkRNA/WES genotypes as a prior, but then only uses SNPs also covered by the reference, losing recall, especially for rare cell types. The question: how to multiplex frozen-tissue snRNA simply, with high recall, and still map every cell back to a named patient?

## 方法 / Method
<!-- ZH -->
SoupLadle 四步 (Fig. 1h):(1) 每位患者做 bulkRNA-seq(STAR 比对,freebayes `-iXu --min-mapping-quality 30 --min-base-quality 10 --min-coverage 5` 调 SNP),**事先**评估 SNP 异质性以挑选可 pool 的样本;(2) pooled 10x 3′ v3.1 sc/snRNA-seq;(3) 在 pooled BAM 上 freebayes 调候选 SNP → Vartrix 计 allele → Souporcell 2.4 聚类(`--num_clusters` = 供体数)+ troublet 识别 doublet;(4) 把 Souporcell 各 genotype cluster 与 bulk SNP profile 求 normalized Hamming 距离矩阵,用 Kuhn-Munkres(Hungarian)做一对一指派。关键论点:deconvolution 阶段可用 scRNA 中**所有** SNP,而不是只用参考里也有的 SNP,所以稀有细胞类型也能被分配。对照方法:CellPlex、Hashtag(TotalSeq-A anti-nuclear-pore)、Souporcell(Vartrix 或 minimap2)、Vireo 0.5.7(cellSNP-lite 或 Vartrix SNP;有/无 bulkRNA 或 WES 先验)。doublet 参考:scDblFinder(top 4000 genes,score > 3)。CellRanger 7.1.0 + GRCh38-2020-A,demultiplexing 前不设 QC cutoff;Seurat 聚类(4000 HVG,res 0.1)作为 PBMC 的 ground truth。
<!-- EN -->
SoupLadle has four steps (Fig. 1h): (1) bulkRNA-seq per patient (STAR, freebayes `-iXu --min-mapping-quality 30 --min-base-quality 10 --min-coverage 5`), used **a priori** to check SNP heterogeneity and choose which samples to pool; (2) pooled 10x 3′ v3.1 sc/snRNA-seq; (3) freebayes candidate SNPs on the pooled BAM → Vartrix allele counts → Souporcell 2.4 clustering (`--num_clusters` = number of donors) + troublet doublet calls; (4) a normalized Hamming-distance matrix between Souporcell genotype clusters and bulk SNP profiles, solved one-to-one with Kuhn-Munkres (Hungarian). The key argument is that deconvolution can use **all** SNPs called in the single-cell data, not just those also in the reference, so rare cell types still get assigned. Comparators: CellPlex, Hashtag (TotalSeq-A anti-nuclear-pore), Souporcell (Vartrix or minimap2), Vireo 0.5.7 (cellSNP-lite or Vartrix SNPs; with/without bulkRNA or WES prior). Doublet reference: scDblFinder (top 4000 genes, score > 3). CellRanger 7.1.0 + GRCh38-2020-A, no QC cutoff before demultiplexing; Seurat clusters (4000 HVG, res 0.1) serve as PBMC ground truth.

## 数据 / Data
<!-- ZH -->
| 数据集 | 设计 | 平台 | 细胞/核数 | 真值 |
|---|---|---|---|---|
| PBMC (P1–5) | 每人 FACS 分选一种 PBMC 亚群 (CD14 Mono / CD16 Mono / CD4 T / CD8 T / CD19 B),各 100,000,pool;CellPlex 标记;bulkRNA + WES | 10x 3′ v3.1, Chip G | 17,892 | 细胞类型 = 患者 (FACS 设计) + CellPlex |
| Heart 1 (P6–10) | 冷冻心肌 snRNA,CellPlex + Hashtag 双标记;bulkRNA + WES | 10x 3′ v3.1, Chip G | 1,563 | CellPlex / HTO |
| Heart 2 (P11–18) | 冷冻心肌 snRNA,每人 ~50,000 nuclei 分选后 pool,无标记;bulkRNA | 10x 3′ HT v3.1, Chip M | 11,501 | 仅方法间一致性 |
| **Kidney (P19–22)** | **4 例冷冻人肾活检**(3 男 1 女),"total processed biopsies were pooled prior to sorting",DAPI⁺ nuclei 分选,无标记;bulkRNA(**无 rRNA depletion**),无 WES | **10x 3′ v3.1 (Dual Index), Chip G, snRNA** | **11,490** | 仅方法间一致性 |

另有一个已发表的 5′ scRNA 心脏数据 (Koenig 2022) 只用于 SNP 分布分析。肾样本的**疾病/临床诊断在论文、补充材料、GEO 与 BioSample 中均未给出**(伦理批号 Erasmus MC MEC-2021-0840)。
<!-- EN -->
| Dataset | Design | Platform | Cells/nuclei | Ground truth |
|---|---|---|---|---|
| PBMC (P1–5) | one FACS-sorted PBMC subset per patient (CD14 Mono / CD16 Mono / CD4 T / CD8 T / CD19 B), 100,000 each, pooled; CellPlex; bulkRNA + WES | 10x 3′ v3.1, Chip G | 17,892 | cell type = patient (by design) + CellPlex |
| Heart 1 (P6–10) | frozen myocardium snRNA, CellPlex + Hashtag; bulkRNA + WES | 10x 3′ v3.1, Chip G | 1,563 | CellPlex / HTO |
| Heart 2 (P11–18) | frozen myocardium snRNA, ~50,000 nuclei/patient sorted and pooled, unlabeled; bulkRNA | 10x 3′ HT v3.1, Chip M | 11,501 | cross-method agreement only |
| **Kidney (P19–22)** | **4 frozen human kidney biopsies** (3 M / 1 F), "total processed biopsies were pooled prior to sorting", DAPI⁺ nuclei sorted, unlabeled; bulkRNA (**no rRNA depletion**), no WES | **10x 3′ v3.1 (Dual Index), Chip G, snRNA** | **11,490** | cross-method agreement only |

A published 5′ heart scRNA dataset (Koenig 2022) is used only for SNP-distribution analysis. **Kidney disease / clinical diagnosis is not reported** in the paper, supplement, GEO or BioSample (ethics: Erasmus MC MEC-2021-0840).

## 主要结果 / Key results
<!-- ZH -->
- **PBMC**:Souporcell 精度/召回最高;Vireo 加 bulkRNA/WES 先验"marginal improvement in precision, but a distinct loss in cell recall";排除 doublet 后所有方法精度 ≈ 98.5%。CellPlex 精度较低源于 doublet 高估(CellPlex 3,947 doublets + 3,524 unassigned vs Souporcell 2,373 + 34,共 17,892 cells)。bulkRNA 比 WES 回收更多 scRNA SNP(尤其 3′UTR)。随机下采样 bulk SNP(1.0→0.2,n = 10)时 SoupLadle 显著优于 Vireo(Wilcoxon, p < 0.0001)。
- **Heart 1**:SoupLadle 几乎全部分配;CellPlex/Hashtag/Vireo CellSNP bulkRNA 约 75%;Vireo CellSNP WES 仅 ~12.5%。方法间重叠 > 95%(WES 除外)。
- **Heart 2 (n = 8)**:SoupLadle 分配 99%,Vireo Vartrix bulkRNA 81%,Vireo CellSNP bulkRNA 45%。
- **Kidney (n = 4, 11,490 nuclei)**:SoupLadle 分配 96%(singlets 10,781;**doublets 250 = 2.2%**;unassigned 459 = 4.0%);Vireo Vartrix bulkRNA 21%;Vireo CellSNP bulkRNA < 1%。SoupLadle 与 Vireo Vartrix 重叠 ~93%。Vireo 对 podocytes、fibroblasts、intercalated cells 等稀有类型分配差,SoupLadle "no apparent cell-type bias"。
- **(我们从 Source Data Fig2j 自行汇总的数字)** 肾表达聚类中 "Mixed/Doublets" 簇有 4,488 nuclei(39%),但 SoupLadle 只把其中 123 个判为跨供体 doublet,308 个 unassigned,其余 4,057 个归给单一供体;"Low Quality" 簇 434 个。即:表达上的"doublet/mixed"簇大部分在基因型上是单一供体。
- 成本:8 样本 multiplexing 约 4 倍降本(Supplementary Data 1)。
- 环境 RNA:**未定量**。原文:"while we do not provide a tool for ambient RNA correction, ambient RNA can be imputed with standard packages (CellBender, SoupX) or Souporcell"。
<!-- EN -->
- **PBMC**: Souporcell has the best precision/recall; adding bulkRNA/WES priors to Vireo gives "marginal improvement in precision, but a distinct loss in cell recall"; excluding doublets, all methods reach ≈ 98.5% precision. CellPlex's lower precision comes from over-calling doublets (CellPlex 3,947 doublets + 3,524 unassigned vs Souporcell 2,373 + 34, of 17,892 cells). bulkRNA recovers more scRNA SNPs than WES (especially 3′UTR). With bulk SNPs randomly downsampled (1.0→0.2, n = 10), SoupLadle beats Vireo significantly (Wilcoxon, p < 0.0001).
- **Heart 1**: SoupLadle assigns nearly all cells; CellPlex/Hashtag/Vireo CellSNP bulkRNA ~75%; Vireo CellSNP WES only ~12.5%. Cross-method overlap > 95% (except WES).
- **Heart 2 (n = 8)**: SoupLadle 99% assigned, Vireo Vartrix bulkRNA 81%, Vireo CellSNP bulkRNA 45%.
- **Kidney (n = 4, 11,490 nuclei)**: SoupLadle assigns 96% (10,781 singlets; **250 doublets = 2.2%**; 459 unassigned = 4.0%); Vireo Vartrix bulkRNA 21%; Vireo CellSNP bulkRNA < 1%. SoupLadle/Vireo Vartrix overlap ~93%. Vireo under-assigns rare types (podocytes, fibroblasts, intercalated cells); SoupLadle shows "no apparent cell-type bias".
- **(Our own tally from Source Data Fig2j.)** The kidney "Mixed/Doublets" expression cluster holds 4,488 nuclei (39%), yet SoupLadle calls only 123 of them cross-donor doublets and 308 unassigned; the other 4,057 go to a single donor. There is also a 434-nucleus "Low Quality" cluster. So most of the expression-defined "doublet/mixed" cluster is genotypically single-donor.
- Cost: ~4-fold cheaper when multiplexing 8 samples (Supplementary Data 1).
- Ambient RNA: **not quantified**. Quote: "while we do not provide a tool for ambient RNA correction, ambient RNA can be imputed with standard packages (CellBender, SoupX) or Souporcell".

## 创新点 / Contributions
- <!-- ZH --> 系统对比 CellPlex、Hashtag、Souporcell、Vireo(± bulkRNA/WES)在 PBMC、心脏、肾三类样本上的表现,其中 PBMC 用 FACS 设计提供"细胞类型 = 患者"真值。 <!-- EN --> A head-to-head benchmark of CellPlex, Hashtag, Souporcell and Vireo (± bulkRNA/WES) on PBMC, heart and kidney, with a FACS design in PBMC that makes "cell type = patient" a ground truth.
- <!-- ZH --> SoupLadle:先 deconvolute 后匹配,两步解耦,在 SNP 稀少和稀有细胞类型上更稳健;提供 R 包和样本 pool 前的 SNP 异质性评估。 <!-- EN --> SoupLadle: deconvolve first, then match, which is more robust when SNPs are scarce and for rare cell types; ships as an R package with a pre-pooling SNP-heterogeneity check.
- <!-- ZH --> 实证:snRNA 的 SNP 主要落在 intron 与 3′UTR,所以 bulkRNA-seq 比 WES 更适合作为参考基因型。 <!-- EN --> Evidence that snRNA SNPs fall mostly in introns and 3′UTRs, so bulkRNA-seq is a better genotype reference than WES.

## 局限 / Limitations
- <!-- ZH --> 心脏 2 与肾数据集没有独立的标签真值(没做 CellPlex/HTO),只能看方法间一致性;作者自称 "proof of concept"。 <!-- EN --> Heart 2 and kidney have no independent label ground truth (no CellPlex/HTO), only cross-method agreement; the authors call it a "proof of concept".
- <!-- ZH --> 肾仅 4 例,未报告疾病、年龄或活检指征;bulkRNA 未做 rRNA depletion。 <!-- EN --> Kidney has only 4 donors, with no reported disease, age or biopsy indication; its bulkRNA was not rRNA-depleted.
- <!-- ZH --> SNP 方法只能检出**跨供体**(heterotypic)doublet;同供体 doublet 不可见。论文未讨论这一点。 <!-- EN --> SNP methods only see **cross-donor** (heterotypic) doublets; same-donor doublets are invisible. The paper does not discuss this.
- <!-- ZH --> 没有量化 ambient RNA 或 contamination。 <!-- EN --> Ambient RNA and contamination are not quantified.
- <!-- ZH --> 公开数据的小问题:GEO 中 Heart_2 的 SRA run (SRR29832268) 显示 0 spots;Heart_2 Patient 18 的 bulk run (SRR29830135) 与 Heart Patient 10 (SRR26826519) 的 spots/bases 完全相同,疑似重复上传(**未核实**)。 <!-- EN --> Deposition issues: the Heart_2 pooled SRA run (SRR29832268) shows 0 spots, and Heart_2 Patient 18's bulk run (SRR29830135) has exactly the same spots/bases as Heart Patient 10 (SRR26826519), which looks like a duplicate upload (**unverified**).

## 与本研究方向的关系 / Relation to our direction
<!-- ZH -->
属于 **detect** 阶段的数据/真值来源,而非方法。伪影注入课题要建立一个人肾单细胞 benchmark,检验 anomaly detector 能否把疾病信号与测量伪影(ambient RNA、doublet、protocol)区分开,并在供体层面用 conformal 控制误报。这个数据集是少见的**真实人肾、多供体 pooled、带每供体 bulk 基因型**的 snRNA:
1. **跨供体 doublet 真值**:基因型 doublet 是独立于表达的标签。在 4 个供体、比例不等时,只有部分 doublet 是跨供体的。这是 lower bound,不是完整 doublet 集合,但足以评估"表达型 doublet 检测器 / anomaly score 是否误把稀有细胞或疾病状态当 doublet"。Source Data 显示表达上的 "Mixed/Doublets" 簇大多是单一供体,是现成的反例池。
2. **Ambient RNA 真值**:pooled 多供体时,每个核里"错误供体等位基因"的比例就是对 ambient/contamination 的基因型估计(Souporcell 本身就估计 ambient 比例;思路同 Janssen 2023 的 genotype-based ground truth)。论文没做,需要我们从 FASTQ 重算。
3. **Donor 层面 conformal**:4 个供体可做 leave-one-donor-out 的小规模校准实验,但 n = 4 太小,只能做 sanity check,不能作为主结果。
4. 局限:疾病状态未知,故无法作为"疾病 vs 伪影"中的疾病一侧;只能做伪影一侧的真值。
<!-- EN -->
This is a data / ground-truth source for the **detect** stage, not a method. The artifact-injection topic builds a human-kidney single-cell benchmark that tests whether anomaly detectors separate disease from measurement artifacts (ambient RNA, doublets, protocol), with donor-level conformal false-alarm control. This dataset is a rare **real human-kidney, multi-donor pooled snRNA with per-donor bulk genotypes**:
1. **Cross-donor doublet ground truth**: genotype doublets are labels independent of expression. With 4 donors in unequal proportions only part of all doublets are cross-donor, so this is a lower bound, not the full doublet set. It is still enough to test whether expression-based doublet detectors or anomaly scores mistake rare cells or disease states for doublets. Source Data shows the expression "Mixed/Doublets" cluster is mostly single-donor, a ready pool of counter-examples.
2. **Ambient RNA ground truth**: in a multi-donor pool, the fraction of "wrong-donor alleles" in each nucleus is a genotype-based estimate of ambient/contamination (Souporcell itself estimates an ambient fraction; same idea as Janssen 2023's genotype-based ground truth). The paper does not do this, so we must recompute it from FASTQ.
3. **Donor-level conformal**: 4 donors allow a small leave-one-donor-out calibration check, but n = 4 is a sanity check, not a headline result.
4. Limitation: disease status is unknown, so the dataset cannot serve as the "disease" side of disease-vs-artifact; it only gives artifact-side ground truth.

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码:** SoupLadle R 包 https://github.com/ToreBle/SoupLadle(Zenodo 10.5281/zenodo.13711299);含 souporcell/vireo shell 脚本与 PBMC/Heart 分析脚本,**仓库中没有肾的分析脚本或每细胞分配表**。 <!-- EN --> **Code:** SoupLadle R package https://github.com/ToreBle/SoupLadle (Zenodo 10.5281/zenodo.13711299); includes souporcell/vireo shell scripts and PBMC/heart analysis scripts, but **no kidney script and no per-cell assignment table**.
- <!-- ZH --> **数据:** GEO GSE247708(SuperSeries:GSE247706 bulk VCF,GSE247707 pooled 10x);肾 pooled snRNA = GSM8397034,只有 `barcodes/features/matrix`(11,490 barcodes × 36,601 genes,cellranger-7.1.0)。GEO 标注为 "raw_feature_bc_matrix",但条形码数等于 cell-called 数,实为**过滤后矩阵**,没有 empty droplets,也没有分配表;肾 bulk VCF = GSM8397029–32 (TS116/120/121/126)。FASTQ 公开:BioProject PRJNA1040187;肾 snRNA run SRR29832267(809M spots, ENA R1 16.5 GB + R2 32.8 GB);肾 bulk SRR29830128–31(约 1.5–1.7 GB/例)。WES(仅 PBMC/心脏)在 EGA EGAD50000000928,受控访问。Source Data 提供肾每细胞类型 × 供体计数(Fig2j)。PBMC (GSM7899153, 2,739,993 barcodes) 和 Heart 1 (GSM7899155, 1,080,502) 是真正的 raw 矩阵,并附 CMO/HTO assignment tables。 <!-- EN --> **Data:** GEO GSE247708 (SuperSeries: GSE247706 bulk VCFs, GSE247707 pooled 10x). Kidney pooled snRNA = GSM8397034, with only `barcodes/features/matrix` (11,490 barcodes × 36,601 genes, cellranger-7.1.0). GEO labels it "raw_feature_bc_matrix", but the barcode count equals the cell-called count, so it is in fact a **filtered matrix**: no empty droplets and no assignment table. Kidney bulk VCFs = GSM8397029–32 (TS116/120/121/126). FASTQs are public under BioProject PRJNA1040187: kidney snRNA run SRR29832267 (809M spots; ENA R1 16.5 GB + R2 32.8 GB) and kidney bulk SRR29830128–31 (~1.5–1.7 GB each). WES (PBMC/heart only) is at EGA EGAD50000000928, controlled access. Source Data gives kidney cell-type × donor counts (Fig2j). PBMC (GSM7899153, 2,739,993 barcodes) and Heart 1 (GSM7899155, 1,080,502) are true raw matrices, with CMO/HTO assignment tables.
- <!-- ZH --> **模型:** 无(非学习模型)。 <!-- EN --> **Checkpoints:** none (not a learned model).

## 待读 / Follow-ups
- <!-- ZH --> 从 SRR29832267 重跑 CellRanger(得到真 raw 矩阵 + BAM)→ Souporcell(k = 4,含 ambient 估计)→ SoupLadle 匹配 GEO 肾 VCF,复现 250 doublets / 459 unassigned,然后再算每核的跨供体等位基因比例。 <!-- EN --> Re-run CellRanger on SRR29832267 (true raw matrix + BAM) → Souporcell (k = 4, with ambient estimate) → SoupLadle matching to the GEO kidney VCFs; reproduce 250 doublets / 459 unassigned, then compute per-nucleus cross-donor allele fractions.
- <!-- ZH --> 向作者 (Hayat/Bleckwehl) 询问肾样本的疾病/临床信息和每细胞分配表。 <!-- EN --> Ask the authors (Hayat/Bleckwehl) for kidney clinical/disease metadata and the per-cell assignment table.
- <!-- ZH --> 对照 Janssen 2023(基因型 ambient 真值)与 Heaton 2020 Souporcell 的 ambient 估计。 <!-- EN --> Compare with Janssen 2023 (genotype-based ambient ground truth) and Heaton 2020 Souporcell ambient estimation.

## 引用 / Cite
```bibtex
@article{Hoeft_2024, title={Label-free single-cell RNA multiplexing leveraging genetic variability}, volume={15}, ISSN={2041-1723}, url={http://dx.doi.org/10.1038/s41467-024-54270-6}, DOI={10.1038/s41467-024-54270-6}, number={1}, journal={Nature Communications}, publisher={Springer Science and Business Media LLC}, author={Hoeft, Konrad and Bleckwehl, Tore and Schumacher, David and Kim, Hyojin and Meyer, Robert and Long, Qingqing and Zhang, Ling and Möller, Christian and Clahsen-van Groningen, Marian C. and Babler, Anne and Saritas, Turgay and Kurth, Ingo and Milting, Hendrik and Hayat, Sikander and Kramann, Rafael}, year={2024}, month=Dec }
```
