# 入门模块 4、5.1、5.2 写作计划 / Onboarding modules 4–5 plan

> 状态：已完成（模块 4、5 已写入 onboarding/）· 归档 2026-10-31
> 目标：写完模块 4（病人和取材）和模块 5（测法）。写法和模块 1–3 一样：一步一步讲，
> 每个概念说明它落在数据的哪里，配计算机类比、真实图片和自测题。
> **最重要的要求：每一句事实性的话都有出处，不能误人子弟。**

---

## 1. 引用规则（模块 4、5 先用，之后补到模块 1–3）

1. **每条事实都有出处。** 定义、数字、"X 会导致 Y"这类因果说法，句末都要标引用。
   类比和"我们为什么关心这一点"是我们自己的解释，不用标引用，但不能写成事实的样子。
2. **出处要真的读过。** 只核对 DOI 还不够：要找到原文里支持这句话的那一段，
   把位置（章节、页码、图号）记在下面第 4 节的核对表里。没找到原文段落的，不写进页面。
3. **优先用一手来源。** 临床定义用指南原文（KDIGO），方法用提出它的那篇论文，
   数据集的事实用数据集论文或我们自己从下载数据里数出来的数（注明"我们数的"）。
4. **数字只有两种来源**：论文原文，或者我们自己从公开数据里数的。不凭记忆写。
   已经核对过的数据集事实在 `datasets/datasets.yaml`，页面里直接链接过去，不重复抄。
5. **页面格式。** 正文里用 `[1]`、`[2]` 标号，页面末尾放"参考文献 / References"一节：
   作者、年份、标题、期刊、DOI 链接。论文库里已经有的，同时链接到它的精读页。
6. **库外文献**（KDIGO、10x 等）的 BibTeX 放进 `onboarding/refs.bib`（新建），
   通过 DOI 从 Crossref 取，不手写。
7. **讲不准的地方就说不准。** 文献之间有分歧或者证据不足时，写"目前的证据是……"，不下结论。

---

## 2. 模块 4 · 病人和取材（30 分钟）

主线：obs 里 `condition` 和 `tissue_type` 是怎么来的，以及它们为什么会**骗**模型。

| 步骤 | 要写的说法 | 出处 | 落在数据哪里 |
|---|---|---|---|
| 1 · 两种肾病 | AKI 的定义：短时间内（小时到天）肾功能下降，按血肌酐上升或尿量减少判定 | KDIGO 2012 AKI 指南（**DOI 待查**，见第 4 节） | `condition.l1` |
| | CKD 的定义：肾脏结构或功能异常持续 **> 3 个月** | KDIGO 2024 CKD 指南 [Stevens 2024] | `condition.l1` |
| | DKD：糖尿病引起的 CKD | KDIGO 2022 糖尿病 CKD 指南 [Rossing 2022] | `condition.l2` |
| 2 · 病有多重 | eGFR 是由血肌酐（和/或胱抑素 C）估算的肾功能；CKD 按 eGFR 分期 G1–G5 | Inker 2021（公式）；KDIGO 2024（分期表） | 先查 Lake 标签表有没有 eGFR 列；没有就只讲概念 |
| 3 · 三种取材 | 活检、肿瘤肾切除、死亡供体，各自提供谁的组织 | Lake 2023 方法部分；KPMP 设计 [de Boer 2021] | `tissue_type` |
| | 每种取材带来的偏差（组织量、取到皮质还是髓质、病人年龄、缺血时间） | **需要找来源**：先查 Lake 2023 和 KPMP 设计论文里有没有写；没有的不写 | `tissue_type`、`region` |
| 4 · 健康人也有 altered 细胞 | 单核数据里健康人的核有 26% 是 altered | `datasets.yaml`（我们数的） | `state.l1` × `condition` |
| | 作者给出的可能原因：取材时缺血、正常衰老 | Lake 2023（**要找到原文那一句**） | |
| 5 · 混杂 | Lake 里病人组织来自 KPMP 活检，健康组织来自肾切除、死亡供体和活体供体活检 | `datasets.yaml` + Lake 2023 | `condition` 和 `tissue_type` 相关 |
| | 所以区分病人和健康人的模型可能只学会了区分取材方式 | 我们的推论，写成推论；可以用 `condition` × `tissue_type` 交叉表（我们数的）支持 | |

**图：** 优先复用 Lake 2023 Fig. 1a（CC BY 4.0，已在 `datasets/img/`）；
活检示意图到 Wikimedia Commons 找 CC 授权的。

**自测：** AKI 和 CKD 的区别；为什么健康人也有 altered 细胞；为什么模型可能只学会了认取材方式。

---

## 3. 模块 5 · 测法（拆成两页，各 45 分钟）

主线：一块组织是怎么变成模块 1 里的 X 的，以及每种测法在 X 里留下了什么偏差。

- **5.1 · 从组织到计数矩阵**（`05-1-assays-rna.md`）：下表第 1–3 步。
- **5.2 · ATAC、多模态、空间、混样**（`05-2-assays-more.md`）：下表第 4–7 步。
- 两页结构已拆好（2026-10-26），目前是占位页；名词也按这个分到两页（见 `modules.yaml`）。

| 步骤 | 要写的说法 | 出处 | 落在数据哪里 |
|---|---|---|---|
| 1 · 整个细胞还是只测核 | 单细胞要先用酶把组织解离；解离本身会诱导应激基因（FOS、JUN 等） | van den Brink 2017；Denisenko 2020（库内） | `nCount`、应激基因 |
| | 单核可以用冻存组织，只拿到核里的 RNA；在成人肾脏上单核能拿到更多稀有细胞类型 | Wu 2019（JASN）；Lake 2019（库内） | 哪个矩阵 |
| 2 · 液滴、barcode、UMI | 一个油滴里装一个细胞（核）和一颗带 barcode 的珠子，barcode 标明细胞 | Macosko 2015（Drop-seq）；Zheng 2017（10x） | X 的行 |
| | UMI 给每条原始分子编号，用来去掉 PCR 扩增出的重复 | Kivioja 2012；Islam 2014 | X 里的数字 |
| | barcode 长度（16 nt）、UMI 长度 | **10x 官方技术文档**，要找到具体版本（v3） | |
| 3 · 液滴出错 | 空液滴、doublet，只预告 | EmptyDrops [Lun 2019]；模块 6 细讲 | |
| 4 · ATAC | Tn5 转座酶优先切入开放染色质，测序片段堆积成 peak | Buenrostro 2013；单细胞版 Buenrostro 2015 | 核 × peak 矩阵 |
| 5 · 同一个核测两样 | SNARE-seq2 在同一个核里同时测 RNA 和 ATAC | Plongthongkum 2021 | 两个矩阵共用行 |
| | Lake 的 SNARE2：104,809 个核，只来自 7 名健康人 | `datasets.yaml` | |
| 6 · 空间 | Visium：组织切片上的点阵，一个点可能包含多个细胞 | Ståhl 2016（原始方法）；10x 文档（点的大小） | 多一张坐标表 |
| | Xenium：成像法，单细胞分辨率，但只测预选的几百个基因 | Janesick 2023 | |
| 7 · 多人混在一次上机 | 用 SNP 基因型把细胞分回各自的人，同时能发现跨人的 doublet | Kang 2018（demuxlet）；Heaton 2020（souporcell） | `patient` 是怎么来的 |

**5.2 的 ATAC 和 SNARE 要讲到初学者能懂（用户要求，2026-10-26）。** 不能一句"Tn5 切开放染色质"带过，要分步：
1. DNA 在核里绕在组蛋白上，缠紧的区域（关）基因用不了，松开的区域（开）才能被读——先回到模块 2 的"源代码"类比；
2. Tn5 只能钻进松开的区域，插进去的地方带着测序接头，所以测到的片段 = 开放区域的位置；
3. 很多核在同一位置都有片段，堆起来就是 peak；矩阵 = 核 × peak，数字多是 0/1/2；
4. 为什么要 ATAC：它告诉你"哪些基因准备好可以开"，RNA 告诉你"哪些正在开"，两者不完全一致；
5. SNARE2：如果 RNA 和 ATAC 来自不同的核，只能靠算法把两边配对；同一个核测两样就不用猜。
每一步配图（自己画或 CC 授权），每条事实有出处。

**最后一张总表**（放在 5.2 末尾，覆盖两页）：测法 / 一行是什么 / 一列是什么 / 主要偏差。表里每一格都要能对上上面某条出处。

**图：** 第 1 步复用 Lake 2023 Fig. 1a；第 2 步自己画交互图（读段 → (barcode, UMI, 基因) → 去重 → 计数），
沿用模块 1 那张 X/obs 图的风格；ATAC、空间到 Wikimedia Commons 找 CC 授权的图。


---

## 4. 文献核对表

DOI 一栏已经用 Crossref 核对过（2026-10-26），标题和期刊都对得上。
"原文段落"一栏是写作时要填的：支持页面上那句话的原文位置。

| 简称 | 文献 | DOI | DOI 核对 | 原文段落 |
|---|---|---|---|---|
| KDIGO AKI 2012 | KDIGO AKI guideline, Section 2: AKI Definition. Kidney Int Suppl 2012;2(1):19–36 | 10.1038/kisup.2011.32 | ✓（`10.1038/kisup.2012.1` 是 "Notice"，弃用） | Rec 2.1.1（AKI 三条标准，p.19）；Figure 2（AKI 可叠加在 CKD 上） |
| Stevens 2024 | KDIGO 2024 CKD guideline. Kidney Int 2024 | 10.1016/j.kint.2023.10.018 | ✓ | CKD 定义（"present for a minimum of 3 months, with implications for health"）；Table 2（G1–G5 及脚注）；Practice Point 1.2.2.1（SCr + 公式做初步评估）；肌酐生成与肌肉量（Fig./表注） |
| Rossing 2022 | KDIGO 2022 Diabetes in CKD guideline. Kidney Int 2022 | 10.1016/j.kint.2022.06.008 | ✓ | 模块 4 最终没用（DKD 改用 KPMP 摘要 + Lake 标签表） |
| Inker 2021 | New creatinine- and cystatin C–based equations to estimate GFR without race. NEJM 385:1737–1749 | 10.1056/NEJMoa2102953 | ✓ | 标题与摘要：eGFR 由肌酐和/或胱抑素 C 估算 |
| de Boer 2021 | Rationale and design of the Kidney Precision Medicine Project. Kidney Int 99:498–510 | 10.1016/j.kint.2020.08.039 | ✓ | 摘要：研究用活检；CKD 来自糖尿病或高血压，AKI 来自缺血或毒性损伤 |
| Lake 2023 | 库内 `lake-kidney-atlas-nature-2023` | 10.1038/s41586-023-05769-3 | 库内 | Fig. 1a（取材）；Methods "Ethical compliance"（KPMP 活检、KTRC 肾切除和死亡供体、HCA 活体供体活检）；正文 "might arise from ischaemic stress during sample acquisition or normal ageing"。**原文没有**写健康参考的判定标准、缺血时间、肾切除是否因肿瘤 |
| Lake 2019 | 库内 `lake-snrna-pipeline-natcommun-2019` | — | 库内 | |
| Denisenko 2020 | 库内 `denisenko-dissociation-bias-genomebiol-2020` | — | 库内 | |
| van den Brink 2017 | Single-cell sequencing reveals dissociation-induced gene expression… Nat Methods | 10.1038/nmeth.4437 | ✓ | |
| Wu 2019 | Advantages of single-nucleus over single-cell RNA sequencing of adult kidney. JASN | 10.1681/ASN.2018090912 | ✓ | |
| Macosko 2015 | Drop-seq. Cell | 10.1016/j.cell.2015.05.002 | ✓ | |
| Zheng 2017 | Massively parallel digital transcriptional profiling of single cells. Nat Commun | 10.1038/ncomms14049 | ✓ | |
| Kivioja 2012 | Counting absolute numbers of molecules using UMIs. Nat Methods | 10.1038/nmeth.1778 | ✓ | |
| Islam 2014 | Quantitative single-cell RNA-seq with UMIs. Nat Methods | 10.1038/nmeth.2772 | ✓ | |
| Lun 2019 | EmptyDrops. Genome Biol | 10.1186/s13059-019-1662-y | ✓ | |
| Buenrostro 2013 | ATAC-seq. Nat Methods | 10.1038/nmeth.2688 | ✓ | |
| Buenrostro 2015 | Single-cell chromatin accessibility… Nature | 10.1038/nature14590 | ✓ | |
| Plongthongkum 2021 | SNARE-seq2. Nat Protoc | 10.1038/s41596-021-00507-3 | ✓ | |
| Ståhl 2016 | Spatial transcriptomics. Science | 10.1126/science.aaf2403 | ✓ | |
| Janesick 2023 | Xenium. Nat Commun | 10.1038/s41467-023-43458-x | ✓ | |
| Kang 2018 | demuxlet. Nat Biotechnol | 10.1038/nbt.4042 | ✓ | |
| Heaton 2020 | souporcell. Nat Methods | 10.1038/s41592-020-0820-1 | ✓ | |

注：Crossref 的年份是在线发表年份，有几篇和印刷年份差一年（Kivioja 2011 在线 / 2012 印刷，
Islam 2013 / 2014，Wu 2018 / 2019，Kang 2017 / 2018）。页面上统一用印刷年份。

---

## 5. 执行顺序

| 步 | 做什么 | 产出 |
|---|---|---|
| M0 | 找到 KDIGO AKI 指南的正确 DOI；补齐 10x 技术文档出处 | 核对表无"待查" |
| M1 | 模块 4：逐条读原文、填"原文段落"栏；数 `condition` × `tissue_type` 交叉表 | 核对表模块 4 部分填满 |
| M2 | 写模块 4 页面 + 参考文献节；你审读 | `onboarding/04-patients-tissue.md` |
| M3 | 模块 5.1：同 M1，再写页面（含交互图）；你审读 | `onboarding/05-1-assays-rna.md` |
| M4 | 模块 5.2：同 M1，再写页面和总表；你审读 | `onboarding/05-2-assays-more.md` |
| M5 | 把同样的引用规则补到模块 1–3 | 模块 1–3 加参考文献节 |

每一步完成后 `mkdocs build --strict` 通过再进行下一步。

---

## 6. 进度记录

**2026-10-26 · M0、M1、M2 完成（模块 4 已写，待审读）。**
自己数的数字来自 GEO `GSE183277_..._snCv3_Metadata_03282022.txt.gz`：
condition × tissue_type、region、altered 占比、`condition.l2` 人数。

核对中发现的问题：
- `datasets/datasets.yaml` 中 Lake 2023 `samples` 写"病人组织来自 KPMP 穿刺活检"——单核数据里有 **3 名 CKD 病人来自肾切除**；
  还写"健康组织来自**肿瘤**肾切除"——Lake 2023 原文（Methods）只说"partial or total nephrectomy"，没有提肿瘤。待用户确认后修正。
- 计划里原写"每种取法的偏差（组织量、年龄、缺血时间）"找不到文献支持，模块 4 改为只写数据里能数出来的事实（取材部位分布、altered 占比）。
- 标签表里没有 eGFR 和年龄列，第 2 步只讲概念。
