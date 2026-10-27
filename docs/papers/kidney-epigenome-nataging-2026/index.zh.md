# A cross-species single-cell kidney epigenome atlas reveals epithelial-dominant aging-like states in disease

> **文献键** `Jeong_2026` · **来源** Nature Aging(2026) · **类别** single-cell · **相关度** medium · **获取** open
> **链接** <https://doi.org/10.1038/s43587-026-01221-z> · `status: complete`

---

## 一句话
作者构建了一个跨物种(人 + 小鼠)的单细胞肾脏表观基因组图谱 —— 单细胞 DNA 甲基化(sciMET)+ 匹配的 10x Multiome(RNA+ATAC)+ Xenium 5K 空间转录组 + scMethyl-Hi-C —— 发现肾病中的**表观遗传年龄加速主要发生在小管上皮细胞**(平均快 4.8 年),病变 PT 细胞的甲基化与表达改变和正常衰老的转录轨迹重叠,集中于缺少 CpG 岛的谱系基因,并定位到未完成修复的空间 niche。

## 研究问题
表观遗传衰老是慢性病(包括 CKD)的标志,但 bulk 分析看不出是哪些细胞类型在「加速衰老」;已有单细胞肾脏研究覆盖了转录组和染色质可及性,却缺少更深层、更稳定的表观层 —— DNA 甲基化(长期记录细胞状态)和 3D 基因组结构(调控所需的物理拓扑)。同时,正常的年龄相关表观漂移与疾病特异改变之间的关系也不清楚。

## 方法
**单细胞甲基化**:组合索引 sciMET;人类样本混池同批处理,再用 SNP 反卷积(全基因组测序验证,99.2% 核正确分配)。**多模态整合**:匹配 10x Multiome、Xenium 5K、以及在一位健康供者上做 scMethyl-Hi-C(同一细胞同时测 3D 构象与甲基组)。**甲基化分区**:UMR(<10% 甲基化、CpG 富集、类启动子)与 LMR(10–50%、CpG 贫乏、类增强子)。**跨物种**:每个细胞与 50 个近邻聚成 metacell,在 40,284 个一对一同源 5 kb bin 上用 Harmony 整合。**衰老时钟**:小鼠用基于全局甲基化的时钟;人类用低覆盖鲁棒的 PC 版 Horvath 多组织时钟(下采样到约 3× 仍准确),年龄加速 = 预测年龄 − 实际年龄的残差。**验证**:用单细胞图谱对 KPMP 激光显微切割的肾小管间质/肾小球 bulk WGBS 做反卷积;S-LDSC 做遗传力富集;72 例 20–90 岁非疾病肾的 snRNA 定义年龄相关基因;单分子共甲基化/甲基化熵;Xenium niche 与 TF 活性;Hi-C A/B compartment;UK Biobank Olink 血浆蛋白与 eGFR 关联。

## 数据
sciMET:57,619 个高质量核 —— 人 12 位供者(7 例肾病 + 5 例年龄匹配参照,33,835 核),小鼠 6 只(3 只 4 月龄 + 3 只 20 月龄,均为雄性,23,784 核);每细胞中位 0.91M CpG(约 3.1% 覆盖)。Multiome:人 142,459 核(9 样本)、小鼠 36,563 核(6 样本)。Xenium 5K:健康、AKI、CKD 共 4 个样本 383,771 个细胞。scMethyl-Hi-C:1 位健康供者 3,072 个细胞、>3 亿长程接触。外部:KPMP WGBS(各 15 例)、小鼠 IRI snATAC(GSE209610)、HKA 图谱。甲基化数据存 BioStudies(S-BSST2657 人 / S-BSST2647 鼠),Multiome 在 HuBMAP。

## 主要结果
- **图谱质量**:甲基化与 Multiome 推断的细胞组成 Spearman ρ = 0.72(sciMET 检出更多髓系免疫细胞,可能因 snRNA 漏检低核 RNA 细胞);92.6% 的 UMR 与 ATAC 峰重叠,LMR 只有 54.8%。人类细胞类型 DMR 共 208,049 个,**只有 16.4% 与 Illumina 850K 芯片位点重叠** —— 芯片研究会漏掉大部分调控元件。
- **跨物种**:34% 的人类 DMR 在小鼠中保持同一状态,但**上皮细胞的跨物种甲基化分化显著大于非上皮细胞**,与较低的序列保守性相关;保守 DMR 富集于 TSS 与 Polycomb 抑制区,物种特异 DMR 多在远端增强子;PT 中 AP-1 与 MYC motif 只富集于物种分化 DMR。
- **小鼠衰老**:细胞类型特异的 UMR/LMR 比共享元件更易发生年龄相关甲基化变化;越相近的细胞类型,其特异调控区越易受年龄影响(仅 LMR);年龄 DMR 在小鼠 IRI 损伤相关可及区显著富集(fold enrichment = 2.95,P < 0.01)。
- **人类疾病**:样本级伪 bulk 显示疾病组年龄加速(P = 0.01);细胞类型级别,**上皮细胞平均加速 4.8 年(P = 2.3 × 10⁻⁴),非上皮细胞无显著差异**,且疾病样本上皮比例相近 —— 加速是细胞内在的,而非组成变化。KPMP bulk WGBS 反卷积验证:富含小管上皮的肾小管间质区年龄加速显著。PT 特异 DMR 富集 eGFR 遗传力,健康→病变态 DMR 亦然(FDR = 0.004)。
- **病变 PT**:同一供者内比较病变(adaptive/maladaptive/degenerative 合并)与健康 PT,得到 8,996 个 DMR,其中 63.1% 为高甲基化;病变 PT 局部甲基化协调性下降、熵升高,尤以 PT 特异调控区为甚;HNF、RXR、PPAR motif 可及性降低、甲基化升高;DMR 甲基化与邻近基因表达 ρ = −0.49;病变 vs 健康的表达改变与 72 例正常肾的年龄相关得分正相关(如 CXCL1、IGFBP6、KCNB2);同时差异甲基化+差异表达的基因富集于**无 CpG 岛**基因。
- **空间与 3D**:Xenium 5K 中病变 PT 甲基化相关基因签名富集在早期修复 niche(AKI 富集;ATF4、JUN、BACH2、E2F)与失败修复 niche(CKD 富集;BHLHE40、MYC、MITF、WNT);PCK1 高甲基化且下调,PLAU、MYO1C、CYTH2 低甲基化且上调。Hi-C 显示上皮细胞短程/长程接触比更高;病变上调基因富集于 PT 特异 B compartment,下调基因富集于 A compartment;找到 107 个「去抑制」区与 64 个「增抑制」区,去抑制区含 CXCL1/2/3/6、ITGA2、ANTXR1、HMGA2、ETS1、BACH2;其中 DSC2、DSG2、TIMP2 编码蛋白的血浆水平在 UK Biobank(54,219 人)中与 eGFR 负相关。

## 创新点
- 首个跨物种、单细胞分辨率的肾脏 DNA 甲基化图谱,并与 RNA/ATAC、空间与 3D 基因组整合。
- 把 bulk 层面的「疾病加速衰老」定位到**小管上皮**,并用独立 bulk WGBS 反卷积验证。
- 提出「谱系特异调控元件更易受衰老和疾病侵蚀」与「缺 CpG 岛基因去抑制」的机制框架。
- 用遗传力(S-LDSC)与人群血浆蛋白组把单细胞表观改变连到临床肾功能。

## 局限
- 作者自陈:小鼠衰老/损伤模型不能完全代表人类慢性病;需纵向研究建立因果;小鼠全为雄性;人类疾病队列小且病因异质,无法分病因分析;scMethyl-Hi-C 只有一位健康供者、分辨率稀疏。
- 「衰老样」状态的解释被作者主动限定:损伤、炎症、应激与去分化会产生重叠的分子签名,**无法确定归因于加速的生物学衰老或细胞衰老**。
- 病变 PT 合并了 adaptive/maladaptive/degenerative 三种状态;Xenium 只有 4 个样本;部分检验未做多重校正(作者称为预设的两组比较)。

## 与本研究方向的关系
对 **课题 1** 的最大提醒是**年龄是一个混杂轴**:疾病中的病变 PT 在表观与转录上都「像变老了」,而正常老年肾本身就带有部分同样的签名(CXCL1 等)。如果异常检测器用年轻或年龄不匹配的健康参照(例如部分公开图谱),它很可能把正常衰老当成异常;反之,若参照偏老,早期疾病信号可能被吸收。因此 KidneyAnomalyBench 应**按年龄匹配参照、或把年龄作为协变量**,并报告异常分数与供者年龄的相关性。第二,本文提供了一个**多层「正交模态」**的范本:甲基化(稳定、长期)、ATAC(可及性)、RNA(瞬时)、空间(niche)在同一状态上一致 —— 这正是「跨模态一致性区分伪影与疾病」的思路:一个只在 RNA 上出现、在甲基化/ATAC 上毫无痕迹的「异常」更可能是技术性的(如 ambient RNA);反过来,甲基化熵升高本身也可作为细胞级的「身份侵蚀」异常分数。第三,Xenium 5K 上的早期修复 / 失败修复 niche 与 `inflammatory-pt-natcommun-2025`、`lake-kidney-atlas-nature-2023` 的 PT 状态对应,可作为空间异常的专家标签候选。对 **revert**:「去抑制」区的基因(CXCL 家族、HMGA2、ETS1、BACH2)与 HNF4A/RXR/PPAR 程序是天然的逆转靶点候选,但作者没有做扰动验证。对 **课题 2**:作者对「衰老」结论的主动限定,以及「未做多重校正」的明示,是 claim-to-evidence 校验中「结论措辞是否与证据强度匹配」的好样例。

## 可复用资产
- **代码:** 处理流程与作图代码。
<https://github.com/hrrsjeong/sckidney_methylome_processing>
<https://github.com/hrrsjeong/sc-kidney-methylome-figures-v0.1>
- **数据:** 单核甲基化(BioStudies S-BSST2657 / S-BSST2647);Multiome(HuBMAP HBM233.KJSR.676;HKAv2 为 HBM787.TZJP.273);KPMP WGBS。
<https://atlas.kpmp.org>
- **方法:** 单细胞甲基化图谱作为 bulk 甲基化的反卷积参照;低覆盖鲁棒的 PC-Horvath 时钟做细胞类型级年龄加速。

## 待读
- Human Kidney Atlas(HKA,Lake 等,`lake-kidney-atlas-nature-2023`)中 adaptive / maladaptive / degenerative 状态的定义。
- 72 例正常肾年龄数据的来源,看能否用于构建年龄匹配的健康参照。

## 引用
```bibtex
@article{Jeong_2026, title={A cross-species single-cell kidney epigenome atlas reveals epithelial-dominant aging-like states in disease}, volume={6}, ISSN={2662-8465}, url={http://dx.doi.org/10.1038/s43587-026-01221-z}, DOI={10.1038/s43587-026-01221-z}, number={10}, journal={Nature Aging}, publisher={Springer Science and Business Media LLC}, author={Jeong, Hyeonsoo and Lake, Blue B. and Diep, Dinh and Li, Xuwen and Yan, Qi and Gisch, Debora L. and Kaushal, Madhurima and Reinert, Stephanie and Eadon, Michael T. and Gaut, Joseph P. and Jain, Sanjay and Zhang, Kun}, year={2026}, month=Sept, pages={2218–2233} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
