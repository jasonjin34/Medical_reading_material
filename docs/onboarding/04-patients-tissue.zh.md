# 4 · 病人和取材

> ⏱ 约 30 分钟 · 第 1 天 · 读懂

!!! abstract "读完能回答"
    - AKI 和 CKD 有什么不同？
    - 活检、肾切除、死亡供体三种取法各有什么问题？
    - 为什么健康人身上也有 altered 细胞？

模块 1 的 obs 里有三列描述"这个细胞从哪来"：`condition`（这个人有什么病）、`tissue_type`（组织是怎么取到的）、`region`（取的是肾的哪一层）。这一模块讲这三列背后的事，以及它们为什么会**骗**模型。

本页的数字有两种来源：文献原文（标 [n]），或者我们自己从 GEO 下载的 Lake 2023 单核标签表里数出来的（标"我们数的"）。

## 第 1 步 · 两种肾病：AKI 和 CKD

肾病按**时间**分成两大类。国际肾脏病指南组织 KDIGO 给了操作性的定义：

- **AKI（急性肾损伤，acute kidney injury）**：肾功能在**几天之内**明显下降。满足下面任意一条就算 [1]：
    - 血肌酐 48 小时内上升 ≥ 0.3 mg/dl（26.5 µmol/l）；
    - 血肌酐在 7 天内升到基线的 1.5 倍以上；
    - 尿量连续 6 小时少于 0.5 ml/kg/h。
- **CKD（慢性肾病，chronic kidney disease）**：肾脏结构或功能异常，**至少持续 3 个月**，并且影响健康 [2]。

**血肌酐**（serum creatinine）是血液里的一种代谢产物，由肾脏滤出；肾脏滤得慢了，它就会在血里积累。KDIGO 建议初步评估肾功能时，就用血肌酐加一个估算公式（第 2 步的 eGFR）。肌酐的产生量和肌肉量有关，所以肌肉特别多或特别少的人，用它估算会有偏差 [2]。

两者不是互斥的：一个已经有 CKD 的人，也可以再发生一次 AKI [1]。

!!! tip "计算机类比"
    AKI 像一次**线上事故**：几小时到几天内突然变差，看的是短时间窗口里的指标跳变。CKD 像**长期退化**：问题持续好几个月，看的是长期状态。一个长期退化的系统，也可能再出一次事故。

### 在数据里

KPMP（Lake 2023 病人样本的来源）重点收集的是最常见的几类：**糖尿病或高血压引起的 CKD**，以及**缺血或毒性损伤引起的 AKI** [3]。这正好对应 Lake 单核标签表里的 `condition.l2`（我们数的，单位是人）：

| `condition.l1` | `condition.l2` | 含义 | 人数 |
|---|---|---|---|
| AKI | AKI | 急性肾损伤 | 6 |
| AKI | COV-AKI | 新冠相关的 AKI | 4 |
| CKD | DKD | 糖尿病肾病 | 7 |
| CKD | H-CKD | 高血压引起的 CKD | 6 |
| Ref | Ref | 健康参考 | 13 |

## 第 2 步 · 病有多重：eGFR

**GFR**（肾小球滤过率）是肾脏每分钟滤出多少血浆，是衡量肾功能的核心指标。直接测很麻烦，临床上通常用血肌酐和 / 或胱抑素 C（cystatin C）加上年龄、性别，用公式**估算**，叫 **eGFR** [4]。KDIGO 按 GFR 把 CKD 分成 6 级 [2]：

| 分级 | GFR (ml/min/1.73 m²) | 含义 |
|---|---|---|
| G1 | ≥ 90 | 正常或偏高 |
| G2 | 60–89 | 轻度下降 |
| G3a | 45–59 | 轻到中度下降 |
| G3b | 30–44 | 中到重度下降 |
| G4 | 15–29 | 重度下降 |
| G5 | < 15 | 肾衰竭 |

G1、G2 本身不算 CKD，要同时有肾损伤的证据才算 [2]。

**在数据里：Lake 2023 公开的单核标签表里没有 eGFR 列，也没有年龄列**（我们查过）。所以我们只知道一个人"有没有病、哪种病"，不知道"病得多重"。

## 第 3 步 · 组织从哪来：三种取材

<div class="grid" markdown>

![Lake 2023 Fig. 1a: kidney tissue from biopsy, nephrectomy (Nx) or deceased donor (DD), processed into cells, nuclei or sections / 肾组织来自活检、肾切除（Nx）或死亡供体（DD），处理成细胞、细胞核或切片](img/lake2023_fig1a_crop.jpg)

Lake 2023 的组织有三种来源 [5]：

- **穿刺活检**（biopsy）：用细针从肾里取一条组织。病人的活检来自 KPMP，是专门为研究做的 [3]；健康参考里也有一部分是**活体捐肾者**的活检 [5]。
- **肾切除**（nephrectomy，图中 Nx）：因病接受部分或全部肾切除的病人，研究用的是切下来的组织 [5]。
- **死亡供体**（deceased donor，图中 DD）：来自已故捐献者、最后没有用于移植的肾 [5]。

</div>

图：Lake et al. 2023 Fig. 1a（截取），Nature，CC BY 4.0。

**取法决定了你看到肾的哪一部分。**下面是 Lake 单核数据里每种取法的细胞核落在哪一层（我们数的）：

| `tissue_type` | 皮质 | 髓质 | 乳头 |
|---|---|---|---|
| 活检 | 81,716 | 42,832 | 8,064 |
| 肾切除 | 43,805 | 7,945 | 0 |
| 死亡供体 | 0 | 7,013 | 12,327 |

在这份数据里，死亡供体的样本**全部**来自髓质和乳头，一个皮质核都没有；肾切除则大部分是皮质。回忆模块 3：皮质和髓质里的细胞类型不一样，所以不同取法的样本，细胞类型的比例本身就不同。

## 第 4 步 · 为什么健康人也有 altered 细胞

按直觉，健康参考（`condition.l1 = Ref`）的细胞应该都是 reference 状态。实际上（我们数的）：

- 健康参考里 **25.7%** 的细胞核被标为 altered（AKI 是 43.2%，CKD 是 42.5%）；
- 按人看，13 个健康人里，altered 占比从 **12% 到 50%** 不等。

Lake 2023 的作者认为，健康参考组织里的 altered 状态**可能来自取样时的缺血应激，或者正常衰老** [5]。这里的"缺血"（ischaemia）指组织离开血液供应、得不到氧气的那段时间。

!!! warning "对我们的工作意味着什么"
    `Ref` 是**按人**打的标签，不是按细胞。如果把"健康人的所有细胞"当作正常样本来训练异常检测模型，训练集里约四分之一的细胞本身就被作者标成了 altered。训练前要想清楚：正常样本是"健康人的细胞"，还是"`state.l1 = reference` 的细胞"？两种选法回答的是不同的问题（模块 8）。

## 第 5 步 · 最大的坑：混杂

把 `condition` 和 `tissue_type` 交叉起来看（我们数的，单位是人 / 细胞核）：

| `condition.l1` | 活检 | 肾切除 | 死亡供体 |
|---|---|---|---|
| AKI | 10 / 51,868 | — | — |
| CKD | 10 / 55,274 | 3 / 8,100 | — |
| Ref | 5 / 25,470 | 5 / 43,650 | 3 / 19,340 |

三件事要注意：

1. **AKI 全部来自活检**，健康参考有一半以上来自肾切除和死亡供体。所以"AKI vs 健康"的差别里，混着"活检 vs 其他取法"的差别。
2. 健康参考里，altered 占比按取法分别是：活检 26.5%、肾切除 29.8%、死亡供体 15.6%（我们数的）。死亡供体反而最低，但它只取了髓质和乳头（第 3 步），而且只有 3 个人。**仅凭这份数据，分不清这个差别来自取法、取材部位，还是这几个人本身。**
3. 每种组合只有 3 到 10 个人。一个人贡献几千个细胞，细胞数看起来很大，但能独立比较的其实只有这几个人（模块 7 的问题 2）。

以上是我们根据计数得出的推论，不是文献结论。

!!! tip "计算机类比"
    像一次 A/B 测试：实验组全部跑在新机房，对照组大多跑在旧机房。看到两组指标不同，你没法知道是新功能的作用，还是机房的作用。训练分类器之前，先把 `condition` × `tissue_type` × `region` 交叉表打出来看一眼。

## 自测

??? question "1. AKI 和 CKD 的根本区别是什么？"
    时间。AKI 是几天之内的急性下降（例如血肌酐 48 小时内上升 ≥ 0.3 mg/dl），CKD 是至少持续 3 个月的异常。两者可以同时存在。

??? question "2. 为什么健康人身上也有 altered 细胞？"
    作者认为可能来自取样时的缺血应激，或者正常衰老。Lake 单核数据里健康参考有 25.7% 的核是 altered，按人从 12% 到 50% 不等。

??? question "3. 一个区分 AKI 和健康人的分类器准确率很高，为什么不能直接相信？"
    AKI 的样本全部来自活检，健康样本大多来自肾切除和死亡供体，取材部位也不一样。模型可能学到的是取法或部位，而不是疾病。要先看交叉表，并按人切分（模块 1）。

## 参考文献

1. Kidney Disease: Improving Global Outcomes (KDIGO) Acute Kidney Injury Work Group. Section 2: AKI definition. *Kidney Int Suppl* 2012;2(1):19–36. [doi:10.1038/kisup.2011.32](https://doi.org/10.1038/kisup.2011.32) — Recommendation 2.1.1; Figure 2.
2. KDIGO CKD Work Group (Stevens PE, Ahmed SB, et al.). KDIGO 2024 clinical practice guideline for the evaluation and management of chronic kidney disease. *Kidney Int* 2024;105(4S):S117–S314. [doi:10.1016/j.kint.2023.10.018](https://doi.org/10.1016/j.kint.2023.10.018) — CKD definition; Table 2; Practice Point 1.2.2.1.
3. de Boer IH, Alpers CE, Azeloglu EU, et al. Rationale and design of the Kidney Precision Medicine Project. *Kidney Int* 2021;99(3):498–510. [doi:10.1016/j.kint.2020.08.039](https://doi.org/10.1016/j.kint.2020.08.039) — abstract.
4. Inker LA, Eneanya ND, Coresh J, et al. New creatinine- and cystatin C–based equations to estimate GFR without race. *N Engl J Med* 2021;385:1737–1749. [doi:10.1056/NEJMoa2102953](https://doi.org/10.1056/NEJMoa2102953)
5. Lake BB, Menon R, Winfree S, et al. An atlas of healthy and injured cell states and niches in the human kidney. *Nature* 2023;619:585–594. [doi:10.1038/s41586-023-05769-3](https://doi.org/10.1038/s41586-023-05769-3) — Fig. 1a; Methods (ethical compliance); Results on altered states. Deep-read: [Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md).

"我们数的"数字：GEO GSE183277，`GSE183277_Kidney_Healthy-Injury_Cell_Atlas_snCv3_Metadata_03282022.txt.gz`，按 `condition.l1`、`condition.l2`、`tissue_type`、`region.l1`、`state.l1`、`patient` 计数。

## 本模块名词

| 中文 | English | 一句话 |
|---|---|---|
| [急性肾损伤](glossary.md#acute-kidney-injury) | Acute kidney injury (AKI) | 几小时到几天内肾功能突然下降（如手术、脓毒症、药物之后）；可能恢复，也可能发展成慢性肾病。 |
| [慢性肾脏病(CKD)](glossary.md#chronic-kidney-disease) | Chronic kidney disease (CKD) | 肾功能在数月至数年间进行性、基本不可逆的丧失;正是在这类非肿瘤疾病场景下,计算病理学的基准明显缺席。 |
| [糖尿病肾病 / 高血压肾病](glossary.md#diabetic-kidney-disease) | Diabetic / hypertensive kidney disease (DKD / H-CKD) | 慢性肾病最常见的两种病因，在肾脏图谱里标作 DKD 和 H-CKD（或 HKD）。 |
| [估算肾小球滤过率(eGFR)](glossary.md#egfr-kidney-function) | Estimated glomerular filtration rate (eGFR) | 由血液指标估算的肾脏每分钟滤过量,是肾功能的标准度量;其多年的变化轨迹,是任何肾脏预后模型最终要对照的临床结局。 |
| [肾活检](glossary.md#kidney-biopsy) | Kidney biopsy | 用穿刺针取出的数毫米长肾组织条,是所有肾脏 modality 共同的原材料——或染色、或解离、或原位测序,各读各的。 |
| [肾切除](glossary.md#nephrectomy) | Nephrectomy (tumour nephrectomy) | 手术切除肾，通常因为肿瘤；离肿瘤远的组织被当作'健康'参考，但它已经缺血了一段时间。 |
| [死亡供体](glossary.md#deceased-donor) | Deceased donor | 器官捐献者的肾最后没被移植、用于研究；缺血时间通常比活检和肾切除更长。 |
| [缺血（取样缺血）](glossary.md#ischaemia) | Ischaemia (procurement ischaemia) | 血流中断；手术中或死后没有血供的组织会启动应激基因，让健康细胞看起来像受了伤。 |
