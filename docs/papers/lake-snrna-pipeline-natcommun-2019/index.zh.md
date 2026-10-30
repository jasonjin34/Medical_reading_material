# A single-nucleus RNA-sequencing pipeline to decipher the molecular anatomy and pathophysiology of human kidneys

> **文献键** `Lake_2019` · **来源** Nature Communications(2019) · **类别** single-cell · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1038/s41467-019-10861-2> · `status: complete`

---

## 一句话
KPMP 早期的方法学论文:比较 7 种肾组织保存/处理方式后,用 snDrop-seq 对 15 人、27 次实验、47 个文库的成人肾做单核转录组,QC 后 17,659 个细胞核聚成 30 个群;结论是 **O.C.T. 冷冻切片 + RNAlater 保存(cryoR)** 的 MT 转录本与应激伪影最少、成功率 >90%,而酶解离(dissocPC/TC)诱导 FOS/FOSB/DNAJB1 应激签名并产生一个伪影簇(PC-2)。

## 研究问题
肾这类上皮丰富、ECM 多的实体组织做单细胞时,酶解离会"激活基因表达伪影、降低活力、造成细胞类型回收不均"。作者想建立一个可复现、适用于活检量级组织、可与组织学并行的单核流程,并系统记录**取材与处理的 preanalytical 参数**,以便在数据中区分生物学变异与技术伪影,进而构建成人肾的分子"蓝图"并定位 CKD / 高血压相关基因的细胞类型。

## 方法
**取材**:Washington University(KTRC)的部分/全肾切除活体患者与弃用的死亡供体肾,以及 University of Michigan(KPMP)的肿瘤肾切除;均取自无瘤区,经组织学确认。**处理方式**(Fig. 1a):整块组织冷冻;O.C.T. 包埋冷冻切片(约 40 µm,7 张)后分别直接冷冻(cryoF)、Wisconsin 冷保存液(cryoW)或 RNAlater(cryoR);新鲜组织酶部分解离:papain/collagenase(dissocPC)或 trypsin/collagenase(dissocTC),解离后存于 RNAlater。GEO 另有"RNAlater 6 Hours"整块组织标签。荧光流式分选核会降低肾核的 snDrop-seq 成功率(Supp. Fig. 1a)。**测序**:snDrop-seq(Drop-seq 改造,HiSeq 2500;流程代码 github.com/chensong611/Dropseq_pipeline)。**QC**:>400 非 MT 转录本、>400 且 <5000 基因,MT 基因剔除;PAGODA2 中 gene/UMI 比值离群过滤、按批次缩放校正;top 2000 overdispersed 基因 → PCA → kNN(k=30,150 PCs)→ infomap,两轮去除 <30 核的簇,另去除一个 120 核无 marker 簇;UMAP 用 Seurat 2.3.4。**分析**:Wilcoxon DE、SWNE、Monocle2 轨迹、CKD eQTL/血压 GWAS 基因的簇特异性评分;按处理方法、个体、来源、性别做平均表达相关性比较(Supp. Fig. 6)。

## 数据
15 名个体(WashU 10 人:PPID 3351, 3395, 3411, 3412, 3414, 3431, 3432, 3434, 3435, 3444;UMich 5 人:17-1606, 18-139, 18-142, 18-162, 18-312),27 次实验 / 47 个文库(GEO GSM3448110–GSM3448156),皮质与髓质。QC 后 17,659 个细胞核,平均每核 1,082 个 UMI(原文 "1082 unique transcripts")。GEO 每个文库有 experiment、barcode、ppid、region、tissue collection(radical / lap / robotic partial / partial nephrectomy、"donor kidney from MAT"、Nephrectomy)、tissue processing、Sex、source。公开文件:带簇注释的 raw UMI 矩阵(列名形如 `C{cluster}_NK{library}_{barcode}`,17,659 列,MT 基因已剔除)和 30 簇注释表;原始 reads 在 SRA SRP166966。**本研究没有活检样本**:"biopsy" 只出现在"兼容活检量级"(平均用 6 mm³ 组织)和与外部数据 GSE114156 的比较中。

## 主要结果
- **处理方式**:只有 O.C.T. 冷冻切片和新鲜解离组织的核与 snDrop-seq 兼容;cryoR 优于 cryoW 与 cryoF;cryoR "showed the fewest expression artifacts while also exhibiting higher experimental success rates (>90%)"。
- **MT 转录本作为质量指标**:"we observed the fewest MTs and stress-induced artifacts in cryoR samples compared to cryosections processed differently (cryoW, cryoF) or fresh dissociated samples (dissocPC, dissocTC), while global gene and transcript levels appeared unaffected"。
- **热缺血**:TAL-1(簇 12,注释为"Thick ascending limb—surgery")和 PT-5(S3,簇 7)出现 MT 富集,"consistent with the nephrectomy procedure-related warm ischemia"。
- **解离应激**:方法间 DE 显示"a stress response signature (including FOS, FOSB, DNAJB1)",只与整细胞解离方法相关、见于多数细胞类型;PC-2(簇 17)主要来自 dissocP/T,"likely represented a dissociation artifact"。
- **一致性**:方法间平均表达相关性高,"cryoW showing the lowest correlation";个体内相关略高于个体间;PT-3(簇 5,炎症基因)主要来自单个个体,可能反映疾病或手术。作者把簇 5、12、17 视为可能的处理、取材或患者来源伪影。
- **生物学**:30 个簇;111/674 个 CKD eQTL 基因、56/220 个高血压基因在簇间差异表达;POD 富集 CKD 位点,MC 富集高血压位点;MC 特异表达 PIEZO2;S2 PT 的 CFH+ 群和 S3 PT 的 FGA/FGB+ 群;髓质 IC-A2 表达 KIT 和 CALCA。

### GEO 复核:同一患者多种处理方式
由公开矩阵列名中的文库号与 GEO 样本注释联结统计(本笔记自算,非论文报告):

| PPID | 来源 | 区域 | 处理 → 核数 |
|---|---|---|---|
| 3351 | radical nephrectomy | Cortex | Fresh Frozen (Dry Ice) 23; RNAlater 6 Hours 72 |
| 3395 | radical nephrectomy | Cortex-Medulla | Flash Frozen OCT cryosection 1,193; RNAlater 6 Hours 375; cryosection + RNAlater 314 |
| 3411 | partial nephrectomy | Cortex | cryosection (dry-ice) 383; cryosection + RNAlater 328 |
| 3414 | donor kidney from MAT | Medulla (+ Cortex) | cryosection 1,401; + Wisc 1,533; + RNAlater 3,102 (medulla) / 481 (cortex) |
| 3435 | robotic partial nephrectomy | Medulla | cryosection + Wisc 342; + RNAlater 338; Papain-Collagenase + RNAlater 223 |
| 3431 | lap nephrectomy | Cortex / Medulla | Papain-Collagenase 781 (cortex); cryosection 834 (medulla) — method confounded with region |
| 18-162 | UMich nephrectomy | Cortex | cryosection 386; + RNAlater 604 |
| 18-312 | UMich nephrectomy | Cortex | cryosection 674; + RNAlater 940 |

单一处理的个体:3432(Trypsin-Collagenase 1,086)、3434(Papain-Collagenase + RNAlater 353)、3412(donor,cryoR 404)、3444(cryoR 50)、17-1606(cryoR 886)、18-139(cryoR 447)、18-142(cryoR 106)。死亡供体只有 3414 和 3412。GEO 用 13 种处理字符串,按切片张数(5/7/10)细分;归并到论文的 7 类方法是本笔记的推断,未与 Supplementary Data 2 核对。

## 创新点
- 第一批系统比较人肾保存/处理方式对单核数据影响的研究之一,确立 cryoR 作为 KPMP 的标准流程。
- 把 preanalytical 参数、组织学和 QC 指标(MT 比例、应激基因)联动起来解释伪影簇。
- 成人肾 30 个细胞群的早期 snRNA 图谱,含 CKD / 高血压基因的细胞类型定位。

## 局限
- 规模小(17,659 核),snDrop-seq 灵敏度低(平均约 1,082 UMI/核),免疫细胞覆盖少;髓质只来自约 3 人。
- 方法比较不是平衡设计:多数方法只在 1–3 人身上做,且常与区域、个体、实验日期(批次)混杂;作者的方法间比较主要是平均表达相关性和 DE,没有给出每种方法的效应量表格(正文中)。
- MT 基因已从公开矩阵剔除,复算 MT 比例需从 SRA 原始 reads 重新比对。
- 作为"正常"参照受限于供体的合并症(作者自述)。

## 与本研究方向的关系
处在 **detect** 一环的**负对照/干扰源**位置。课题 1 的 benchmark 要检验 anomaly detector 能否把疾病与测量/取材伪影分开;这个数据集提供了**同一患者、同一区域、不同保存/处理方式**的真实配对:18-162、18-312、3411(皮质 cryoF vs cryoR)、3414(髓质 cryoF / cryoW / cryoR)、3435(髓质 cryoW / cryoR / dissocPC)、3395、3351。每个细胞核的处理方式可以从公开文件中确定(矩阵列名含文库号 NK#,GEO 每个文库带 tissue processing、ppid、region),因此可以做"伪影标签"的 ground truth:例如在 cryoR 上训练、看 detector 给 dissoc 核(FOS/FOSB/DNAJB1 应激、PC-2 簇)和 cryoW 核打多高的异常分。热缺血(TAL-1、PT-5)给出一个取材相关、但无逐核标签的伪影轴。注意:不同处理通常在不同日期/批次上跑,处理效应与批次部分混杂;样本无疾病标签(只有组织学报告在 Supp. Data 1),所以它只能做伪影侧,疾病侧要靠 KPMP AKI/CKD(如 Lake 2023)。平台是 snDrop-seq,与 10x 数据存在平台差异,也要当作一个伪影轴。

## 可复用资产
- **代码:** snDrop-seq 比对/计数流程 https://github.com/chensong611/Dropseq_pipeline;分步实验流程见 https://kpmp.org/resources/
- **数据:** GEO GSE121862(47 个 GSM,逐文库元数据;带簇注释的 raw UMI 矩阵约 20 MB + 30 簇注释表);SRA SRP166966 原始 reads。
- **模型:** 无。

## 待读
- 获取 Supplementary Data 1–3(preanalytical 参数、病理、每次实验方法与成功率)和 Supp. Fig. 5/6(各方法 MT 比例、相关性),核对 13 种 GEO 处理字符串 → 7 类方法的映射。
- 从 SRA 重比对以恢复 MT 比例,作为逐核质量协变量。
- 对照 Lake 2023 KPMP 图谱(`lake-kidney-atlas-nature-2023`)中参照组织里的 altered states 与缺血应激。

## 引用
```bibtex
@article{Lake_2019, title={A single-nucleus RNA-sequencing pipeline to decipher the molecular anatomy and pathophysiology of human kidneys}, volume={10}, ISSN={2041-1723}, url={http://dx.doi.org/10.1038/s41467-019-10861-2}, DOI={10.1038/s41467-019-10861-2}, number={1}, journal={Nature Communications}, publisher={Springer Science and Business Media LLC}, author={Lake, Blue B. and Chen, Song and Hoshi, Masato and Plongthongkum, Nongluk and Salamon, Diane and Knoten, Amanda and Vijayan, Anitha and Venkatesh, Ramakrishna and Kim, Eric H. and Gao, Derek and Gaut, Joseph and Zhang, Kun and Jain, Sanjay}, year={2019}, month=June }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
