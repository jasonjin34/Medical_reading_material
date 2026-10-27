# 5.1 · 测法：从组织到计数矩阵

> ⏱ 约 45 分钟 · 第 1 天 · 读懂

!!! abstract "读完能回答"
    - 单细胞测序（single-cell sequencing）和单个细胞核测序（single-nucleus sequencing）各测到什么、各有什么代价？
    - 条形码（barcode）和 UMI（unique molecular identifier，分子唯一标识）怎么把测序读段（reads）变成计数矩阵（count matrix）？

模块 1 讲了终点：计数矩阵 X。这一页讲 X 是怎么来的，一共三段：

1. 把组织拆成一个个**细胞**或**细胞核**；
2. 每个细胞（核）和一颗带 **barcode** 的珠子（bead）一起被包进一个小油滴（droplet），它的 RNA 都被贴上这个 barcode 和一个 **UMI**；
3. 测序后，按 barcode 和 UMI **数**出每个细胞里每个基因有几条分子。

每一段都会在 X 里留下痕迹。本页标 [n] 的来自文献；标"我们数的"来自 Lake 2023 在 GEO 上公开的标签表。

## 第 1 步 · 测整个细胞，还是只测细胞核

<div class="grid" markdown>

![Lake 2023 Fig. 1a: tissue processed into cells or nuclei before droplet sequencing (Cv3) / 组织先处理成细胞或细胞核，再进液滴测序（Cv3）](img/lake2023_fig1a_crop.jpg)

<div markdown>

Lake 2023 两种都做了：**scCv3** 测整个细胞，**snCv3** 只测细胞核 [1]。两条路的第一步不一样：

- **单细胞**：要用酶（enzyme）把组织**消化**（digestion，即组织解离 tissue dissociation）成单个活细胞，例如在 37 °C 下消化 [2]。
- **单核**：把组织（可以是**冻存**（frozen）的）弄碎，直接把细胞核提出来，不需要活细胞 [2, 3]。

</div>

</div>

图：Lake et al. 2023 Fig. 1a（截取），Nature，CC BY 4.0。

**代价 1：消化本身会改变细胞。** 在小鼠肾脏上，37 °C 消化会让一批应激基因（stress genes）明显升高，包括 *Fos*、*Jun*、*Atf3*、*Egr1* 和热休克蛋白（heat-shock proteins）；在冰上消化可以避免 [2]。在人肾脏上，整细胞方法同样带出了应激特征（*FOS*、*FOSB*、*DNAJB1*），单核方法没有 [3]。这就是模块 1 示意图里给 FOS 单独一列的原因：它高，可能是病，也可能只是消化造成的（模块 6）。

**代价 2：只测核就少了胞质里的 RNA。** 回忆模块 2：RNA 在核里产生，再送到胞质。Lake 2023 提到，整细胞数据的好处之一就是多了**胞质里的转录本**（cytosolic transcripts）[1]。线粒体在胞质里，它的 RNA 在细胞核里基本没有 [3]。

**代价 3：两条路抓到的细胞类型比例不一样。** 小鼠肾脏上，单细胞数据里缺少肾小球的细胞（足细胞等），单核数据里有 [4]；反过来，单核数据里 T、B、NK 淋巴细胞（lymphocytes）偏少 [2]。

这些差别直接体现在 Lake 2023 的两张标签表里（我们数的，中位数）：

| | 单核) | 单细胞) |
|---|---|---|
| 核数或细胞数 | 203,702 | 109,741 |
| 人数 | 36 | 45 |
| 中位) | 0.81% | 22.99% |
| 中位) | 1,638 | 1,276 |
| 中位) | 2,694 | ≈ 3,076 |

`percent.mt` 差了近 30 倍，正是"线粒体 RNA 在胞质里"的结果。基因数和分子数差得不多，这和小鼠肾脏上"单细胞和单核检测到的基因数相当"的结果一致 [4]。注意这两份数据来自不同的人和组织（scCv3 全部是活检），所以这只是描述，不是严格的对照比较。

!!! tip "计算机类比"
    单细胞像把一台正在运行的机器从机架上整台拔下来再检查：拔的过程本身会触发告警（应激基因）。单核像只把硬盘拆下来读：不受拔机器的影响，但内存里的东西（胞质 RNA）就看不到了。

## 第 2 步 · 液滴和 barcode：分清哪条 RNA 属于哪个细胞

几万个细胞的 RNA 最后要混在一起测序。为了事后还能分开，思路是：**先给每个细胞发一个独一无二的编号，让它的每条 RNA 都带上这个编号，再混在一起测，最后按编号分回去。**

发编号靠的是**珠子**（bead）：一颗比细胞略大的微小凝胶珠，是厂家批量做好的试剂。每颗珠子表面挂着大量很短的 DNA，叫**引物**（primer）。

- **同一颗珠子上的所有引物，带的是同一个 barcode**；
- **不同珠子的 barcode 各不相同**。

所以"一颗珠子 = 一个编号"。只要一个细胞配一颗珠子，这个细胞就有了自己的编号。以 Drop-seq 为例，流程是 [5]：

1. 准备细胞悬液（cell suspension）；
2. 仪器把每个细胞和一颗珠子一起包进一个纳升（nanolitre）大小的油滴；
3. 在油滴里把细胞裂解（lyse）；
4. 细胞的 mRNA 被这颗珠子上的引物抓住，从此带上了这颗珠子的 barcode；
5. 把所有油滴打破，几千个细胞的 RNA 混在一起反转录（reverse transcription）、扩增（amplification）、测序；
6. 按 barcode 把读到的序列分回各个细胞，一个 barcode 就是 X 的一行。

10x Chromium（Lake 2023 用的 Cv3 就是它）原理相同，油滴叫 GEM（Gel bead in EMulsion）[6]。

每条引物由几段拼成 [5]：

- **cell barcode**（细胞条形码）：同一颗珠子上都一样，用来区分**细胞**；
- **UMI**：每条引物都不同，用来区分**分子**，识别 PCR（polymerase chain reaction，聚合酶链式反应）复制出来的重复（第 3 步）；
- **oligo-dT**（寡聚 dT）：一串 T，能和 mRNA 尾巴上的一串 A 配对，把 mRNA 抓住。

Lake 2023 用的 10x 3′ v3 试剂（chemistry）里，barcode 是 **16 个碱基**（bases），可选的 barcode 约 **350 万**种；UMI 是 **12 个碱基** [7]。

注意：**barcode 是每个细胞一个，不是每批一个。**模块 1 里 `KB1_AAACCCAAGCCGATAG` 后面 16 个字母是这个细胞的 barcode，前面的 `KB1` 才是批次（哪一次上机）。不同批次可能用到同一个 barcode，所以要加上批次前缀，ID 才不会重复。

!!! tip "计算机类比"
    barcode 就是**外键**（foreign key）：每条 RNA 记录都带着它所属细胞的 ID，最后按这个键 `GROUP BY`，就把混在一起的记录分回每个细胞。不同批次可能重复使用同一个 barcode，所以要加上批次前缀（`KB1_`），就像合并两张表前给主键（primary key）加命名空间（namespace）。

## 第 3 步 · UMI：数分子，不数读段

**UMI 是什么：**引物上一小段**随机**的碱基序列（10x v3 里是 12 个碱基）。每条引物的 UMI 都不一样，所以每抓住一条 mRNA，这条分子就得到一个自己的随机编号 [5, 9]。

**为什么需要它：因为测序前要先复制。**一个细胞里的 RNA 太少，直接测不出来，要先用 PCR 复制成千上万份。但复制**不均匀**，有的分子复制得多，有的复制得少 [8]。

举个例子：一个细胞里其实只有 **2 条** `LRP2` 的 mRNA。分子①被复制了 10 份，分子②被复制了 30 份，测序一共读到 40 条读段（reads）。

| | 怎么数 | 结果 |
|---|---|---|
| 不用 UMI | 数读段 | **40**，复制了多少次 |
| 用 UMI | 数不同的 UMI | **2**，真实有几条分子 |

所以 UMI 就是用来**去重**的：同一个 UMI 的读段都是同一条原始分子的拷贝，只算一次。下图把这个过程画成三步：

<figure class="umi" markdown="0"><div class="um-row">
<div class="um-panel"><p class="um-h">① 测序读段（reads）</p><table><tr><th>barcode</th><th>UMI</th><th>基因</th></tr>
<tr><td class="um-k" style="--c:var(--u1)">AAACCC…</td><td>TTGCATGGACTA</td><td class="um-gene">LRP2</td></tr>
<tr class="um-dup"><td class="um-k" style="--c:var(--u1)">AAACCC…</td><td>TTGCATGGACTA</td><td class="um-gene">LRP2</td></tr>
<tr class="um-dup"><td class="um-k" style="--c:var(--u1)">AAACCC…</td><td>TTGCATGGACTA</td><td class="um-gene">LRP2</td></tr>
<tr><td class="um-k" style="--c:var(--u2)">AAACCC…</td><td>GACTTACCGTAG</td><td class="um-gene">LRP2</td></tr>
<tr><td class="um-k" style="--c:var(--u3)">AAACGA…</td><td>CCATGAGTTACG</td><td class="um-gene">UMOD</td></tr>
<tr class="um-dup"><td class="um-k" style="--c:var(--u3)">AAACGA…</td><td>CCATGAGTTACG</td><td class="um-gene">UMOD</td></tr>
<tr><td class="um-k" style="--c:var(--u4)">AAACGA…</td><td>AGGTCCATTGCA</td><td class="um-gene">UMOD</td></tr>
<tr><td class="um-k" style="--c:var(--u5)">AAACCC…</td><td>CTTAGGCAAGTC</td><td class="um-gene">FOS</td></tr>
</table></div><div class="um-arrow" aria-hidden="true">→</div>
<div class="um-panel"><p class="um-h">② 按 (barcode, UMI, 基因) 去重</p><table><tr><th>barcode</th><th>UMI</th><th>基因</th></tr>
<tr><td class="um-k" style="--c:var(--u1)">AAACCC…</td><td>TTGCATGGACTA</td><td class="um-gene">LRP2</td></tr>
<tr><td class="um-k" style="--c:var(--u2)">AAACCC…</td><td>GACTTACCGTAG</td><td class="um-gene">LRP2</td></tr>
<tr><td class="um-k" style="--c:var(--u3)">AAACGA…</td><td>CCATGAGTTACG</td><td class="um-gene">UMOD</td></tr>
<tr><td class="um-k" style="--c:var(--u4)">AAACGA…</td><td>AGGTCCATTGCA</td><td class="um-gene">UMOD</td></tr>
<tr><td class="um-k" style="--c:var(--u5)">AAACCC…</td><td>CTTAGGCAAGTC</td><td class="um-gene">FOS</td></tr>
</table></div><div class="um-arrow" aria-hidden="true">→</div>
<div class="um-panel"><p class="um-h">③ 计数：X 的两行</p><table><tr><th></th><th>LRP2</th><th>UMOD</th><th>FOS</th></tr>
<tr><td>AAACCC…</td><td class="um-n">2</td><td class="um-n um-z">·</td><td class="um-n">1</td></tr>
<tr><td>AAACGA…</td><td class="um-n um-z">·</td><td class="um-n">2</td><td class="um-n um-z">·</td></tr>
</table></div></div>
<figcaption>示意数据。每条读段带着三样东西：barcode（哪个细胞）、UMI（哪一条原始分子）、基因（读段比对（align）到哪个基因）。同一条原始分子被 PCR 复制了好几份，所以 ① 里有完全相同的行（颜色相同、后面几行变灰）。按三者去重后，每一行才是一条真实的分子；再按 barcode × 基因数一数，就得到 X。如果直接数读段，第一个细胞的 LRP2 会是 4，而不是 2。</figcaption></figure>

X 里的每个数字，以及 obs 里的 `nCount_RNA`，数的都是 **UMI**（模块 1）。

!!! tip "计算机类比"
    UMI 像消息队列（message queue）里的**幂等键**（idempotency key）：同一条消息被重发了好几次，消费端按消息 ID 去重，只算一次。

## 第 4 步 · 液滴会出错（预告）

上面的流程是理想情况。实际上：

- **不是每个细胞都被抓到。** 10x 原始论文报告的细胞捕获效率（cell capture efficiency）约 50% [6]。
- **空液滴（empty droplet）。** 很多油滴里没有细胞，但仍然含有漂在液体里的游离 RNA，叫 **ambient RNA**（游离 RNA 污染）；它可能是细胞主动分泌的，也可能是细胞破裂（例如消化的应激）释放的 [10]。有细胞的油滴里也混着这些 RNA。
- **一个油滴装进两个细胞**，叫 **doublet**（双细胞假象；多于两个叫 multiplet）。装进去的细胞越多，这种情况越多，符合泊松分布（Poisson distribution）的预期 [6]。

这三件事都会让 X 的某一行"看起来不正常"，模块 6 专门讲。

## 自测

??? question "1. 为什么数 UMI，而不直接数测序读段？"
    PCR 扩增不均匀，一条原始分子可能被复制很多份。数读段反映的是复制次数；按 (barcode, UMI, 基因) 去重后数到的才是原始分子数。

??? question "2. 为什么单核数据的 `percent.mt` 很低，单细胞数据的很高？"
    线粒体在胞质里，它的 RNA 在细胞核里基本没有。单核只测核，所以线粒体 RNA 很少（Lake 2023 中位 0.81%）；单细胞包含胞质，所以高得多（中位 22.99%）。

??? question "3. 一个单细胞数据集里 FOS 很高，能直接说明这些细胞受了伤吗？"
    不能。37 °C 消化本身就会诱导 FOS 等应激基因。要看是不是单细胞、怎么消化的，和单核数据或冰上消化的数据比一比（模块 6）。

## 参考文献

1. Lake BB, Menon R, Winfree S, et al. An atlas of healthy and injured cell states and niches in the human kidney. *Nature* 2023;619:585–594. [doi:10.1038/s41586-023-05769-3](https://doi.org/10.1038/s41586-023-05769-3) — Results ("the addition of cytosolic transcripts from scCv3"); Fig. 1a. Deep-read: [Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md).
2. Denisenko E, Guo BB, Jones M, et al. Systematic assessment of tissue dissociation and storage biases in single-cell and single-nucleus RNA-seq workflows. *Genome Biol* 2020;21:130. [doi:10.1186/s13059-020-02048-6](https://doi.org/10.1186/s13059-020-02048-6) — mouse kidney; abstract and Results (stress genes after 37 °C digestion; lymphocytes in snRNA-seq). Deep-read: [Denisenko 2020](../papers/denisenko-dissociation-bias-genomebiol-2020/index.md).
3. Lake BB, Chen S, Hoshi M, et al. A single-nucleus RNA-sequencing pipeline to decipher the molecular anatomy and pathophysiology of human kidneys. *Nat Commun* 2019;10:2832. [doi:10.1038/s41467-019-10861-2](https://doi.org/10.1038/s41467-019-10861-2) — human kidney; Results (stress signature in whole-cell methods; frozen tissue; mitochondrial transcripts "not expressed in nuclei"). Deep-read: [Lake 2019](../papers/lake-snrna-pipeline-natcommun-2019/index.md).
4. Wu H, Kirita Y, Donnelly EL, Humphreys BD. Advantages of single-nucleus over single-cell RNA sequencing of adult kidney: rare cell types and novel cell states revealed in fibrosis. *J Am Soc Nephrol* 2019;30:23–32. [doi:10.1681/ASN.2018090912](https://doi.org/10.1681/ASN.2018090912) — mouse kidney; abstract.
5. Macosko EZ, Basu A, Satija R, et al. Highly parallel genome-wide expression profiling of individual cells using nanoliter droplets. *Cell* 2015;161:1202–1214. [doi:10.1016/j.cell.2015.05.002](https://doi.org/10.1016/j.cell.2015.05.002) — Results (six steps of Drop-seq; four parts of each primer; UMIs avoid double-counting).
6. Zheng GXY, Terry JM, Belgrader P, et al. Massively parallel digital transcriptional profiling of single cells. *Nat Commun* 2017;8:14049. [doi:10.1038/ncomms14049](https://doi.org/10.1038/ncomms14049) — Results (GEMs; ~50% cell capture efficiency; multiplet rate consistent with Poisson loading).
7. 10x Genomics. Technical Note CG000201 Rev A: Chromium Single Cell 3′ v3 reagent, workflow & software updates. [PDF](https://cdn.10xgenomics.com/image/upload/v1660261285/support-documents/CG000201_TechNote_Chromium_Single_Cell_3___v3_Reagent__Workflow___Software_Updates_RevA.pdf) — 16 nt barcode, 3.5 million barcodes, 12 nt UMI.
8. Islam S, Zeisel A, Joost S, et al. Quantitative single-cell RNA-seq with unique molecular identifiers. *Nat Methods* 2014;11:163–166. [doi:10.1038/nmeth.2772](https://doi.org/10.1038/nmeth.2772) — abstract.
9. Kivioja T, Vähärautio A, Karlsson K, et al. Counting absolute numbers of molecules using unique molecular identifiers. *Nat Methods* 2012;9:72–74. [doi:10.1038/nmeth.1778](https://doi.org/10.1038/nmeth.1778) — abstract.
10. Lun ATL, Riesenfeld S, Andrews T, et al. EmptyDrops: distinguishing cells from empty droplets in droplet-based single-cell RNA sequencing data. *Genome Biol* 2019;20:63. [doi:10.1186/s13059-019-1662-y](https://doi.org/10.1186/s13059-019-1662-y) — Background (ambient RNA in empty droplets and its origin).

"我们数的"数字：GEO GSE183277（snCv3）和 GSE183276（scCv3）的 `*_Metadata_03282022.txt.gz`，取 `nCount_RNA`、`nFeature_RNA`、`percent.mt` 的中位数。scCv3 的 `nCount_RNA` 不是整数（中位 3,075.95），说明作者对它做过处理，这里取约数。

## 本模块名词

| 中文 | English | 一句话 |
|---|---|---|
| [单细胞 RNA 测序(scRNA-seq)](glossary.md#single-cell-rna-seq) | Single-cell RNA sequencing (scRNA-seq) | 一种对单个细胞转录组进行测序的技术,可揭示被批量测序平均掉的细胞类型异质性。 |
| [单核 RNA 测序(snRNA-seq)](glossary.md#snrna-seq) | Single-nucleus RNA-seq (snRNA-seq) | 把组织解离成单个细胞核并分别测其 RNA,得到每个核的全基因组表达,代价是彻底丢失细胞原本在组织中的位置。 |
| [组织解离](glossary.md#tissue-dissociation) | Tissue dissociation | 做单细胞 RNA 测序前把组织拆成单个细胞，通常用酶在 37 °C 消化；能得到完整细胞，但会让细胞应激。 |
| [10x Chromium（Cv3 = 第 3 版试剂）](glossary.md#chromium-10x) | 10x Chromium (Cv3) | 最常用的商业单细胞平台：把每个细胞或核和一颗带条形码的珠子一起包进油滴。Cv3 = Chromium 第 3 版试剂（Lake 2023 里的 snCv3 / scCv3）。 |
| [细胞条形码](glossary.md#cell-barcode) | Cell barcode | 贴在同一个油滴（或同一条分池路径）里所有 RNA 上的短 DNA 标签，用来把读段分回各个细胞；它就是计数矩阵的行 ID。 |
| [UMI（分子唯一标识）](glossary.md#umi) | UMI (unique molecular identifier) | 扩增前贴在每条 RNA 分子上的随机标签，用来去掉 PCR 复制出的重复；计数矩阵里的数字就是 UMI 数（nCount_RNA = 一个细胞的 UMI 总数）。 |
