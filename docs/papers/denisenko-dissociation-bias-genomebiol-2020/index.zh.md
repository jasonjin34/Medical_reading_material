# Systematic assessment of tissue dissociation and storage biases in single-cell and single-nucleus RNA-seq workflows

> **文献键** `Denisenko_2020` · **来源** Genome Biology(2020) · **类别** single-cell · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1186/s13059-020-02048-6> · `status: complete`

---

## 一句话
在同一系统(健康成年小鼠肾,10x Chromium)里、三生物学重复地系统比较 37 °C vs 冰上冷蛋白酶解离、新鲜 vs 冻存 vs 甲醇固定、scRNA-seq vs 三种 snRNA-seq 核提取流程(加 bulk RNA-seq 对照),量化每种流程带来的表达伪影(应激基因)和细胞组成偏差;全部数据公开于 GSE141115。

## 研究问题
实体组织必须解离/保存/提核后才能上 10x;每一步都可能改变转录谱(如 37 °C 酶解诱导即刻早期基因)或改变细胞类型代表性。此前的评估分散在不同组织、不同条件下,且缺少与 bulk 的系统对照。本文在同一器官里把这些偏差并排量化,帮助实验设计与数据解读。

## 方法
**实验臂(均 n=3 生物学重复,每只小鼠一个肾):**

- **批次 1(C57BL/6J 雄性,19 周,10x v2):** 37 °C 解离(Miltenyi Multi Tissue Dissociation Kit 2,gentleMACS `37C_Multi_E`)vs 冷解离(冰上 *B. licheniformis* 冷活性蛋白酶,改自 Adam et al.);每种解离后的悬液分为 新鲜 / 冻存(50% FBS + 40% RPMI-1640 + 10% DMSO,梯度降温→液氮,存 6 周)/ 甲醇固定(80% MeOH,−20 °C→−80 °C,存 3 个月)三臂;另做两种解离悬液的 bulk RNA-seq。
- **批次 2(Balb/c 雄性,18 周,10x v2):** 冷解离 scRNA-seq vs SN_FANS_3x500g snRNA-seq(闪冻全肾),加全肾 bulk。
- **批次 3(Balb/c 雌性,15 周,10x v3):** 冷解离 scRNA-seq 新鲜 vs 冻存重复实验(存 2 周,1200g 离心);三种 snRNA-seq:SN_FANS_3x500g(洗 3 次、500g、FANS 分选)、SN_FANS_1x2000g(洗 1 次、2000g、FANS)、SN_sucrose(500g 后蔗糖垫、无需分选);加全肾 bulk 与冷解离悬液 bulk。

**分析:** Cell Ranger 2.1.1(mm10;snRNA 用 pre-mRNA 参考计入内含子)→ EmptyDrops → 过滤(基因 ≥10 个细胞;每细胞 200–3000 基因、线粒体 <50%;细胞核另需 UMI ≥450 (v2)/≥900 (v3) 且去除线粒体基因;Scater 去 UMI/基因比离群)→ Seurat v2 CCA 整合、Wilcoxon 差异表达。细胞注释:scMatch 对三套公开小鼠肾参考 + 基因签名打分两轮细化,CNT 另行亚聚类(15 种细胞类型)。应激评分:从 warm 诱导基因中人工挑选 17 个文献已知应激基因,用 AddModuleScore 计算,1000 次随机基因集 Monte-Carlo 检验。组成差异用卡方检验;bulk 用 edgeR exact test 和 BSEQ-sc 反卷积。

## 数据
共 77,656 个单细胞、98,303 个单核、15 个 bulk 文库(GEO GSE141115:27 个 scRNA、12 个 snRNA、15 个 bulk 样本;Illumina NovaSeq 6000)。批次 1 新鲜 scRNA:23,108 细胞(冷 11,851 / 热 11,257);甲醇固定 11,627(冷)/ 5,545(热);冻存 3,519(冷)/ 3,483(热)。snRNA 各臂具体核数见 Additional file 14(未逐一核对)。

**GEO 内容(已核对):** 每个样本一个 `GSM*_<lib>.txt.gz`,制表符分隔的原始 UMI counts,基因 × 细胞(列名形如 `BG1_BG20C_<barcode>`)。这些矩阵已是 QC 后的细胞:批次 1 冷解离新鲜三个文库列数 2,356 + 4,084 + 5,411 = 11,851,与论文完全一致;冷解离冻存 897 + 1,629 + 993 = 3,519 亦一致。批次内基因集统一(批次 1 新鲜 13,392 基因,冻存 13,347)。实验臂标签在样本层面(GSM 标题/characteristics:strain、sex、workflow、10x 化学版本);逐细胞的细胞类型标签在论文 Additional file 3(Table S2),不在 GEO。没有原始 Cell Ranger 未过滤矩阵;FASTQ 在 SRA(SRP233496)。

## 主要结果
- **37 °C 解离诱导应激:** bulk 中 71 个基因在 warm 中更高、5 个在 cold 中更高(logFC>2,FDR<0.05);logFC>4 的包括 *Fosb, Fos, Jun, Junb, Atf3, Egr1, Hspa1a, Hspa1b*;GO 首位 "regulation of cell death"。scRNA 中 64 个基因至少在一个细胞类型中 warm 更高;*Junb/Jund* 在 7 种细胞类型中差异,*Jun/Fos* 在 5 种。
- **17 基因应激签名:** *Fosb, Fos, Jun, Junb, Jund, Atf3, Egr1, Hspa1a, Hspa1b, Hsp90ab1, Hspa8, Hspb1, Ier3, Ier2, Btg1, Btg2, Dusp1*;"significantly high stress scores were detected only in warm-dissociated samples in eight out of 14 cell types",其中 "immune and endothelial cells are particularly sensitive"。
- **解离造成的组成偏差:** 8 个细胞群在 warm 中更少(含足细胞、系膜细胞、内皮细胞;卡方 p<0.001),且与高应激评分重合;足细胞 warm 仅 3 个(0.03%)vs cold 330 个(2.78%)。aLOH(4.99% vs 2.52%)和 PT(71.36% vs 63.34%)在 warm 中更多。cold 样本血红蛋白转录本更高(红细胞污染)。
- **冻存丢失上皮:** PT 从新鲜 63.12%/70.86%(cold/warm)降到冻存 0.31%/0.57%;可用细胞约为新鲜的 ~30%;冻存还诱导应激基因(即刻早期基因、热休克蛋白)。重复实验(Balb/c 雌性、v3、2 周、1200g)PT 55.55% → 7.65%。
- **甲醇固定保组成但有 ambient RNA:** 组成接近新鲜,巨噬细胞中度下降(5.36%→3.2% cold;4.28%→2.54% warm);多种细胞类型中出现相同的管状上皮高表达转录本与血红蛋白基因,提示细胞损伤导致的环境 RNA 污染。
- **sc vs sn:** 三种核提取流程结果相近,SN_FANS_1x2000g 线粒体污染更高;snRNA 每核基因中位数 1,819 vs scRNA 981。免疫细胞 snRNA 平均 0.73% vs scRNA 6.03%(BSEQ-sc 估计 Balb/c 雌 1.51%、雄 4.84%);snRNA 只回收巨噬细胞,无 T(scRNA 1.38%)、B(0.77%)、NK(0.65%);足细胞 0.7% vs 3.28%;LoH 与系膜细胞在 snRNA 中更多。snRNA 中 lncRNA 更高,scRNA 中线粒体/核糖体基因更高。

## 创新点
- 同一器官、同一实验室、三重复下并排比较 2 种解离 × 3 种保存 + 3 种核提取 + bulk,偏差可以直接对照。
- 给出一个可复用的 17 基因解离应激签名,并显示应激敏感与细胞类型丢失相耦合。
- 揭示肾组织冻存悬液严重丢失 PT 上皮(跨品系、性别、10x 版本可重复),以及 snRNA-seq 丢失淋巴细胞。

## 局限
- 仅健康小鼠肾;无疾病样本,也无人类组织。
- 批次与品系/性别/化学版本混杂(批次 1 C57 雄 v2;批次 3 Balb/c 雌 v3),sc-vs-sn 比较与冻存重复实验无法完全区分这些因素。
- 没有组成"真值":BSEQ-sc 反卷积与 Clark et al. 解剖估计相互矛盾,作者自承需继续寻找 ground truth。
- 应激签名是从 warm 诱导基因中人工挑选的文献基因,并非独立推导;Seurat v2、Cell Ranger 2.1.1 等工具已较旧。
- 冷解离与 37 °C 解离还在机械步骤、离心速度等方面不同,温度不是唯一变量。

## 与本研究方向的关系
处在 **detect** 一环的"负对照/干扰因素"位置。伪影注入课题要构建人肾单细胞 benchmark,检验异常检测器能否把**疾病信号**与**测量/取材伪影**分开。本数据集提供了已知、受控的技术扰动:(1) 37 °C vs 冷解离 → 解离应激(17 基因签名,免疫与内皮细胞最敏感,足细胞丢失);(2) 新鲜 vs 冻存 vs 甲醇 → 保存伪影(上皮丢失、应激、ambient RNA);(3) sc vs sn → 平台/组分偏差。由于样本均为健康组织,任何被检测器打高分的细胞都是"技术异常"而非疾病,可作为假阳性标定集。但它是**小鼠**数据,只能作为后期的校准/迁移检验,不能作为主 benchmark;17 基因签名需映射到人类同源基因(FOS、JUN、HSPA1A 等)后再用于人肾数据的伪影标注。注意 GEO 中臂标签仅在样本层面,且批次与品系/性别/化学版本混杂。

## 可复用资产
- **代码:** 文中未给出代码仓库。
- **数据:** GEO GSE141115(54 个样本,QC 后 UMI counts 矩阵,样本级臂标签);SRA SRP233496(FASTQ);逐细胞类型标签见 Additional file 3,各臂细胞计数见 Additional file 14,DE 表见 Additional files 1/4/5/7–10。
- **模型:** 无;可复用的是 17 基因应激签名与 scMatch 小鼠肾参考(Additional files 19/21)。

## 待读
- Adam et al. 2017(冷活性蛋白酶解离,Development)— 冷解离原始方法。
- van den Brink et al. 2017 Nat Methods(解离诱导的转录变化)。
- Wu et al. 2019 JASN(肾 sc vs sn)与 Slyper et al.(文中引 bioRxiv 2019 版;人肿瘤新鲜/冷冻 sc/sn 工具箱)。
- 人类组织的对应研究(如人肾活检解离/保存伪影)以及 SoupX / DecontX 去环境 RNA。

## 引用
```bibtex
@article{Denisenko_2020, title={Systematic assessment of tissue dissociation and storage biases in single-cell and single-nucleus RNA-seq workflows}, volume={21}, ISSN={1474-760X}, url={http://dx.doi.org/10.1186/s13059-020-02048-6}, DOI={10.1186/s13059-020-02048-6}, number={1}, journal={Genome Biology}, publisher={Springer Science and Business Media LLC}, author={Denisenko, Elena and Guo, Belinda B. and Jones, Matthew and Hou, Rui and de Kock, Leanne and Lassmann, Timo and Poppe, Daniel and Clément, Olivier and Simmons, Rebecca K. and Lister, Ryan and Forrest, Alistair R. R.}, year={2020}, month=June }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
