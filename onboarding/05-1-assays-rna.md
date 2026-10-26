# 5.1 · 测法：从组织到计数矩阵 / 5.1 · Assays: from tissue to the count matrix

<!-- ZH -->
!!! abstract "读完能回答"
    - 单细胞和单个细胞核测序各测到什么、各有什么代价？
    - 条形码和 UMI 怎么把测序读段变成计数矩阵？
<!-- EN -->
!!! abstract "After this module you can answer"
    - What do single-cell and single-nucleus sequencing capture, and at what cost?
    - How do barcodes and UMIs turn reads into a count matrix?

<!-- ZH -->
模块 1 讲了终点：计数矩阵 X。这一页讲 X 是怎么来的，一共三段：

1. 把组织拆成一个个**细胞**或**细胞核**；
2. 每个细胞（核）和一颗带 **barcode** 的珠子一起被包进一个小油滴，它的 RNA 都被贴上这个 barcode 和一个 **UMI**；
3. 测序后，按 barcode 和 UMI **数**出每个细胞里每个基因有几条分子。

每一段都会在 X 里留下痕迹。本页标 [n] 的来自文献；标"我们数的"来自 Lake 2023 在 GEO 上公开的标签表。
<!-- EN -->
Module 1 showed the end point, the count matrix X. This page shows how X is made, in three stages:

1. the tissue is broken into single **cells** or **nuclei**;
2. each cell (or nucleus) is packed into a tiny droplet with a bead carrying a **barcode**, and its RNA is tagged with that barcode and a **UMI**;
3. after sequencing, barcodes and UMIs are used to **count** how many molecules of each gene each cell had.

Each stage leaves marks in X. Items marked [n] come from the literature; "our count" means counted from Lake 2023's public label tables on GEO.

## 第 1 步 · 测整个细胞，还是只测细胞核 / Step 1 · Whole cells or nuclei

<!-- ZH/EN --> <div class="grid" markdown>

<!-- ZH/EN --> ![Lake 2023 Fig. 1a: tissue processed into cells or nuclei before droplet sequencing (Cv3) / 组织先处理成细胞或细胞核，再进液滴测序（Cv3）](img/lake2023_fig1a_crop.jpg)

<!-- ZH -->
Lake 2023 两种都做了：**scCv3** 测整个细胞，**snCv3** 只测细胞核 [1]。两条路的第一步不一样：

- **单细胞**：要用酶把组织**消化**成单个活细胞，例如在 37 °C 下消化 [2]。
- **单核**：把组织（可以是**冻存**的）弄碎，直接把细胞核提出来，不需要活细胞 [2, 3]。
<!-- EN -->
Lake 2023 did both: **scCv3** profiles whole cells and **snCv3** profiles nuclei [1]. The first step differs:

- **Single-cell**: the tissue is **digested** with enzymes into single living cells, for example at 37 °C [2].
- **Single-nucleus**: the tissue (which can be **frozen**) is broken up and the nuclei are pulled out directly; no living cells are needed [2, 3].

<!-- ZH/EN --> </div>

<!-- ZH -->
图：Lake et al. 2023 Fig. 1a（截取），Nature，CC BY 4.0。

**代价 1：消化本身会改变细胞。** 在小鼠肾脏上，37 °C 消化会让一批应激基因明显升高，包括 *Fos*、*Jun*、*Atf3*、*Egr1* 和热休克蛋白；在冰上消化可以避免 [2]。在人肾脏上，整细胞方法同样带出了应激特征（*FOS*、*FOSB*、*DNAJB1*），单核方法没有 [3]。这就是模块 1 示意图里给 FOS 单独一列的原因：它高，可能是病，也可能只是消化造成的（模块 6）。

**代价 2：只测核就少了胞质里的 RNA。** 回忆模块 2：RNA 在核里产生，再送到胞质。Lake 2023 提到，整细胞数据的好处之一就是多了**胞质里的转录本** [1]。线粒体在胞质里，它的 RNA 在细胞核里基本没有 [3]。

**代价 3：两条路抓到的细胞类型比例不一样。** 小鼠肾脏上，单细胞数据里缺少肾小球的细胞（足细胞等），单核数据里有 [4]；反过来，单核数据里 T、B、NK 淋巴细胞偏少 [2]。

这些差别直接体现在 Lake 2023 的两张标签表里（我们数的，中位数）：
<!-- EN -->
Figure: Lake et al. 2023, Fig. 1a (cropped), Nature, CC BY 4.0.

**Cost 1: digestion changes the cells.** In mouse kidney, digestion at 37 °C strongly induces stress genes, including *Fos*, *Jun*, *Atf3*, *Egr1* and heat-shock proteins; digesting on ice avoids this [2]. In human kidney, whole-cell methods likewise showed a stress signature (*FOS*, *FOSB*, *DNAJB1*) that single-nucleus methods did not [3]. This is why module 1's figure gives FOS its own column: a high value might be disease, or might just be digestion (module 6).

**Cost 2: nuclei lack the cytoplasmic RNA.** Recall module 2: RNA is made in the nucleus and then shipped to the cytoplasm. Lake 2023 names the **cytosolic transcripts** as one advantage of whole-cell data [1]. Mitochondria sit in the cytoplasm, and their RNA is essentially absent from nuclei [3].

**Cost 3: the two routes recover different cell-type mixes.** In mouse kidney, single-cell data lacked glomerular cells such as podocytes, which single-nucleus data recovered [4]; conversely, single-nucleus data under-represented T, B and NK lymphocytes [2].

These differences show up directly in Lake 2023's two label tables (our count, medians):

| | snCv3 (nuclei / 单核) | scCv3 (cells / 单细胞) |
|---|---|---|
| Nuclei or cells / 核数或细胞数 | 203,702 | 109,741 |
| People / 人数 | 36 | 45 |
| `percent.mt` (median / 中位) | 0.81% | 22.99% |
| `nFeature_RNA` (median / 中位) | 1,638 | 1,276 |
| `nCount_RNA` (median / 中位) | 2,694 | ≈ 3,076 |

<!-- ZH -->
`percent.mt` 差了近 30 倍，正是"线粒体 RNA 在胞质里"的结果。基因数和分子数差得不多，这和小鼠肾脏上"单细胞和单核检测到的基因数相当"的结果一致 [4]。注意这两份数据来自不同的人和组织（scCv3 全部是活检），所以这只是描述，不是严格的对照比较。
<!-- EN -->
`percent.mt` differs by a factor of almost thirty, which is what you expect if mitochondrial RNA sits in the cytoplasm. Gene and molecule counts are close, consistent with the mouse-kidney finding that single-cell and single-nucleus methods detect similar numbers of genes [4]. The two datasets come from different people and tissue (scCv3 is all biopsies), so this is a description, not a controlled comparison.

<!-- ZH -->
!!! tip "计算机类比"
    单细胞像把一台正在运行的机器从机架上整台拔下来再检查：拔的过程本身会触发告警（应激基因）。单核像只把硬盘拆下来读：不受拔机器的影响，但内存里的东西（胞质 RNA）就看不到了。
<!-- EN -->
!!! tip "Computer analogy"
    Single-cell is like pulling a running machine out of the rack to inspect it: the pulling itself fires alarms (stress genes). Single-nucleus is like reading only the disk: unaffected by the pulling, but you lose what was in memory (cytoplasmic RNA).

## 第 2 步 · 液滴和 barcode：分清哪条 RNA 属于哪个细胞 / Step 2 · Droplets and barcodes: which RNA came from which cell

<!-- ZH -->
几万个细胞的 RNA 最后要混在一起测序。为了事后还能分开，每个细胞先被单独"贴标签"。以 Drop-seq 为例，流程是 [5]：

1. 准备细胞悬液；
2. 每个细胞和一颗带 barcode 的珠子一起被包进一个纳升大小的油滴；
3. 在油滴里把细胞裂解；
4. 细胞的 mRNA 被珠子上的引物抓住；
5. 把所有油滴打破，几千个细胞一起反转录、扩增、测序；
6. 靠 barcode 推断每条转录本来自哪个细胞。

10x Chromium（Lake 2023 用的 Cv3 就是它）原理相同，油滴叫 GEM（Gel bead in EMulsion）[6]。

珠子上的每条引物由几段组成 [5]：

- **cell barcode**：**同一颗珠子上的所有引物都一样，不同珠子之间不同**。所以同一个油滴里的 RNA 都带着同一个 barcode。
- **UMI**：**每条引物都不同**，用来识别 PCR 复制出来的重复（第 3 步）。
- **oligo-dT**：一串 T，能和 mRNA 尾巴上的一串 A 配对，把 mRNA 抓住。

Lake 2023 用的 10x 3′ v3 试剂里，barcode 是 **16 个碱基**，可选的 barcode 约 **350 万**种；UMI 是 **12 个碱基** [7]。模块 1 里 `KB1_AAACCCAAGCCGATAG` 后面那 16 个字母就是它。
<!-- EN -->
The RNA of tens of thousands of cells is eventually sequenced together. To separate it again afterwards, each cell is labelled on its own first. Taking Drop-seq as the example, the steps are [5]:

1. prepare a cell suspension;
2. pack each cell with a barcoded bead into a nanolitre droplet;
3. lyse the cell inside the droplet;
4. let the bead's primers capture the cell's mRNA;
5. break all droplets and reverse-transcribe, amplify and sequence thousands of cells in one reaction;
6. use the barcodes to infer which cell each transcript came from.

10x Chromium, which Lake 2023 used (Cv3), works the same way; its droplets are called GEMs (Gel bead in EMulsion) [6].

Each primer on a bead has several parts [5]:

- **cell barcode**: **identical on all primers of one bead, different between beads**, so all RNA from one droplet carries the same barcode;
- **UMI**: **different on every primer**, used to recognise PCR duplicates (step 3);
- **oligo-dT**: a run of T that pairs with the run of A at the tail of an mRNA and captures it.

In the 10x 3′ v3 chemistry used by Lake 2023, the barcode is **16 bases** long, drawn from about **3.5 million** barcodes, and the UMI is **12 bases** [7]. Those are the 16 letters after `KB1_` in module 1's `KB1_AAACCCAAGCCGATAG`.

<!-- ZH -->
!!! tip "计算机类比"
    barcode 就是**外键**：每条 RNA 记录都带着它所属细胞的 ID，最后按这个键 `GROUP BY`，就把混在一起的记录分回每个细胞。不同批次可能重复使用同一个 barcode，所以要加上批次前缀（`KB1_`），就像合并两张表前给主键加命名空间。
<!-- EN -->
!!! tip "Computer analogy"
    The barcode is a **foreign key**: every RNA record carries the ID of its cell, and a final `GROUP BY` on that key splits the pooled records back into cells. Different runs can reuse the same barcodes, which is why a run prefix (`KB1_`) is added, like namespacing primary keys before merging two tables.

## 第 3 步 · UMI：数分子，不数读段 / Step 3 · UMIs: count molecules, not reads

<!-- ZH -->
测序前要用 PCR 把 DNA 扩增很多倍，否则量太少测不出来。但扩增不均匀：不同的原始分子被复制的份数各不相同。如果直接数**读段**（reads），数字反映的是"复制了多少次"，不是"有几条分子"。单细胞数据里起始量极少，这个误差尤其严重 [8]。

UMI 的作用就是给每条**原始分子**一个随机编号。复制出来的拷贝编号都一样，所以按 (barcode, UMI, 基因) 去重，剩下的才是真实的分子数 [5, 8, 9]。
<!-- EN -->
Before sequencing, PCR amplifies the DNA many times over; otherwise there is too little to read. But amplification is uneven: different original molecules end up with different numbers of copies. Counting **reads** directly would measure how often things were copied, not how many molecules there were. With the tiny starting amounts in single-cell data this error is severe [8].

A UMI gives each **original molecule** a random tag. All copies share that tag, so de-duplicating on (barcode, UMI, gene) leaves the real number of molecules [5, 8, 9].

<!-- ZH -->
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
<figcaption>示意数据。每条读段带着三样东西：barcode（哪个细胞）、UMI（哪一条原始分子）、基因（读段比对到哪个基因）。同一条原始分子被 PCR 复制了好几份，所以 ① 里有完全相同的行（颜色相同、后面几行变灰）。按三者去重后，每一行才是一条真实的分子；再按 barcode × 基因数一数，就得到 X。如果直接数读段，第一个细胞的 LRP2 会是 4，而不是 2。</figcaption></figure>
<!-- EN -->
<figure class="umi" markdown="0"><div class="um-row">
<div class="um-panel"><p class="um-h">① Sequencing reads</p><table><tr><th>barcode</th><th>UMI</th><th>gene</th></tr>
<tr><td class="um-k" style="--c:var(--u1)">AAACCC…</td><td>TTGCATGGACTA</td><td class="um-gene">LRP2</td></tr>
<tr class="um-dup"><td class="um-k" style="--c:var(--u1)">AAACCC…</td><td>TTGCATGGACTA</td><td class="um-gene">LRP2</td></tr>
<tr class="um-dup"><td class="um-k" style="--c:var(--u1)">AAACCC…</td><td>TTGCATGGACTA</td><td class="um-gene">LRP2</td></tr>
<tr><td class="um-k" style="--c:var(--u2)">AAACCC…</td><td>GACTTACCGTAG</td><td class="um-gene">LRP2</td></tr>
<tr><td class="um-k" style="--c:var(--u3)">AAACGA…</td><td>CCATGAGTTACG</td><td class="um-gene">UMOD</td></tr>
<tr class="um-dup"><td class="um-k" style="--c:var(--u3)">AAACGA…</td><td>CCATGAGTTACG</td><td class="um-gene">UMOD</td></tr>
<tr><td class="um-k" style="--c:var(--u4)">AAACGA…</td><td>AGGTCCATTGCA</td><td class="um-gene">UMOD</td></tr>
<tr><td class="um-k" style="--c:var(--u5)">AAACCC…</td><td>CTTAGGCAAGTC</td><td class="um-gene">FOS</td></tr>
</table></div><div class="um-arrow" aria-hidden="true">→</div>
<div class="um-panel"><p class="um-h">② De-duplicate on (barcode, UMI, gene)</p><table><tr><th>barcode</th><th>UMI</th><th>gene</th></tr>
<tr><td class="um-k" style="--c:var(--u1)">AAACCC…</td><td>TTGCATGGACTA</td><td class="um-gene">LRP2</td></tr>
<tr><td class="um-k" style="--c:var(--u2)">AAACCC…</td><td>GACTTACCGTAG</td><td class="um-gene">LRP2</td></tr>
<tr><td class="um-k" style="--c:var(--u3)">AAACGA…</td><td>CCATGAGTTACG</td><td class="um-gene">UMOD</td></tr>
<tr><td class="um-k" style="--c:var(--u4)">AAACGA…</td><td>AGGTCCATTGCA</td><td class="um-gene">UMOD</td></tr>
<tr><td class="um-k" style="--c:var(--u5)">AAACCC…</td><td>CTTAGGCAAGTC</td><td class="um-gene">FOS</td></tr>
</table></div><div class="um-arrow" aria-hidden="true">→</div>
<div class="um-panel"><p class="um-h">③ Count: two rows of X</p><table><tr><th></th><th>LRP2</th><th>UMOD</th><th>FOS</th></tr>
<tr><td>AAACCC…</td><td class="um-n">2</td><td class="um-n um-z">·</td><td class="um-n">1</td></tr>
<tr><td>AAACGA…</td><td class="um-n um-z">·</td><td class="um-n">2</td><td class="um-n um-z">·</td></tr>
</table></div></div>
<figcaption>Illustrative data. Each read carries three things: a barcode (which cell), a UMI (which original molecule) and a gene (where the read aligns). One original molecule is copied several times by PCR, so ① has identical rows (same colour, repeats greyed). After de-duplicating on all three, each row is one real molecule; counting per barcode × gene gives X. Counting reads instead would give the first cell 4 LRP2, not 2.</figcaption></figure>


<!-- ZH -->
X 里的每个数字，以及 obs 里的 `nCount_RNA`，数的都是 **UMI**（模块 1）。

!!! tip "计算机类比"
    UMI 像消息队列里的**幂等键**：同一条消息被重发了好几次，消费端按消息 ID 去重，只算一次。
<!-- EN -->
Every number in X, and `nCount_RNA` in obs, counts **UMIs** (module 1).

!!! tip "Computer analogy"
    A UMI is like an **idempotency key** in a message queue: the same message is delivered several times, and the consumer de-duplicates on the message ID so it counts once.

## 第 4 步 · 液滴会出错（预告） / Step 4 · Droplets go wrong (preview)

<!-- ZH -->
上面的流程是理想情况。实际上：

- **不是每个细胞都被抓到。** 10x 原始论文报告的细胞捕获效率约 50% [6]。
- **空液滴。** 很多油滴里没有细胞，但仍然含有漂在液体里的游离 RNA，叫 **ambient RNA**；它可能是细胞主动分泌的，也可能是细胞破裂（例如消化的应激）释放的 [10]。有细胞的油滴里也混着这些 RNA。
- **一个油滴装进两个细胞**，叫 **doublet**（多于两个叫 multiplet）。装进去的细胞越多，这种情况越多，符合泊松分布的预期 [6]。

这三件事都会让 X 的某一行"看起来不正常"，模块 6 专门讲。
<!-- EN -->
The steps above are the ideal case. In practice:

- **Not every cell is captured.** The original 10x paper reports about 50% cell capture efficiency [6].
- **Empty droplets.** Many droplets hold no cell but still contain free-floating RNA from the solution, called **ambient RNA**; it can be secreted by cells or released when cells burst (for example under the stress of dissociation) [10]. Droplets with a cell contain some of it too.
- **Two cells in one droplet**, a **doublet** (more than two: multiplet). The more cells are loaded, the more often this happens, as expected from Poisson loading [6].

All three can make a row of X look abnormal; module 6 covers them.

## 自测 / Self-check

<!-- ZH -->
??? question "1. 为什么数 UMI，而不直接数测序读段？"
    PCR 扩增不均匀，一条原始分子可能被复制很多份。数读段反映的是复制次数；按 (barcode, UMI, 基因) 去重后数到的才是原始分子数。

??? question "2. 为什么单核数据的 `percent.mt` 很低，单细胞数据的很高？"
    线粒体在胞质里，它的 RNA 在细胞核里基本没有。单核只测核，所以线粒体 RNA 很少（Lake 2023 中位 0.81%）；单细胞包含胞质，所以高得多（中位 22.99%）。

??? question "3. 一个单细胞数据集里 FOS 很高，能直接说明这些细胞受了伤吗？"
    不能。37 °C 消化本身就会诱导 FOS 等应激基因。要看是不是单细胞、怎么消化的，和单核数据或冰上消化的数据比一比（模块 6）。
<!-- EN -->
??? question "1. Why count UMIs instead of reads?"
    PCR amplification is uneven, so one original molecule may be copied many times. Reads measure copying; counting after de-duplicating on (barcode, UMI, gene) gives the number of original molecules.

??? question "2. Why is `percent.mt` low in single-nucleus data and high in single-cell data?"
    Mitochondria sit in the cytoplasm and their RNA is essentially absent from nuclei. Nuclei-only data has little of it (Lake 2023 median 0.81%); whole cells include the cytoplasm, so it is much higher (median 22.99%).

??? question "3. FOS is high in a single-cell dataset. Does that show the cells were injured?"
    No. Digestion at 37 °C itself induces FOS and other stress genes. Check whether the data is single-cell and how it was digested, and compare with single-nucleus or cold-digested data (module 6).

## 参考文献 / References

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

<!-- ZH -->
"我们数的"数字：GEO GSE183277（snCv3）和 GSE183276（scCv3）的 `*_Metadata_03282022.txt.gz`，取 `nCount_RNA`、`nFeature_RNA`、`percent.mt` 的中位数。scCv3 的 `nCount_RNA` 不是整数（中位 3,075.95），说明作者对它做过处理，这里取约数。
<!-- EN -->
"Our count" numbers: the `*_Metadata_03282022.txt.gz` files of GEO GSE183277 (snCv3) and GSE183276 (scCv3), medians of `nCount_RNA`, `nFeature_RNA` and `percent.mt`. scCv3's `nCount_RNA` is not an integer (median 3,075.95), so the authors processed it; we give a rounded value.
