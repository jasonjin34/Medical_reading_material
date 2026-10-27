# 1 · 两张表：X 和 obs

> ⏱ 约 30 分钟 · 第 1 天 · 读懂

!!! abstract "读完能回答"
    - 单细胞数据最后变成哪两张表？
    - 矩阵的一行、一列、一个数字分别代表什么？
    - 哪个字段是标签，哪个字段是分组 ID？为什么不能随机切分训练集和测试集？

先从终点讲起。后面几个模块讲的生物和实验，最后都会落到这两张表里。先知道终点长什么样，读后面的内容时就知道每个概念最后变成了表里的什么。

下面这张图把两张表画在一起：左边是 X，右边是 obs，**同一行就是同一个细胞**。先整体看一眼，下面再一张一张讲。

<figure class="xobs" markdown="0"><div class="xo-scroll"><table aria-label="计数矩阵 X 与标签表 obs 按行对齐">
<thead><tr class="xo-cap"><th></th><th colspan="8"><span class="xo-tag">X</span>计数矩阵 <span class="xo-sub">· 细胞 × 基因</span></th><th></th><th colspan="5"><span class="xo-tag">obs</span>标签表 <span class="xo-sub">· 每个细胞一行</span></th></tr>
<tr class="xo-genes"><th></th><th>LRP2<i style="background:var(--xo-pt)"></i></th><th>CUBN<i style="background:var(--xo-pt)"></i></th><th>UMOD<i style="background:var(--xo-tal)"></i></th><th>SLC12A1<i style="background:var(--xo-tal)"></i></th><th>NPHS2<i style="background:var(--xo-pod)"></i></th><th>FOS<i style="background:var(--xo-stress)"></i></th><th>MT-CO1<i style="background:var(--xo-mito)"></i></th><th></th><th></th><th class="xo-o">patient</th><th class="xo-o xo-n">nCount</th><th class="xo-o xo-n">nFeature</th><th class="xo-o">subclass</th><th class="xo-o">state</th></tr></thead>
<tbody>
<tr tabindex="0"><td class="xo-bc">L1_AAACCCAAGC…</td><td class="xo-x"><b style="--c:var(--xo-pt);--a:61%">12</b></td><td class="xo-x"><b style="--c:var(--xo-pt);--a:46%">5</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-mito);--a:30%">1</b></td><td class="xo-more">…</td><td class="xo-seam"><div></div></td><td class="xo-o">P1</td><td class="xo-o xo-n">18</td><td class="xo-o xo-n">3</td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-pt)">PT</span></td><td class="xo-o"><span class="xo-pill">reference</span></td></tr>
<tr tabindex="0"><td class="xo-bc">L1_AAACGAATCA…</td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-tal);--a:80%">25</b></td><td class="xo-x"><b style="--c:var(--xo-tal);--a:51%">7</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-more">…</td><td class="xo-seam"><div></div></td><td class="xo-o">P1</td><td class="xo-o xo-n">32</td><td class="xo-o xo-n">2</td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-tal)">TAL</span></td><td class="xo-o"><span class="xo-pill">reference</span></td></tr>
<tr tabindex="0"><td class="xo-bc">L2_AAAGGATGTC…</td><td class="xo-x"><b style="--c:var(--xo-pt);--a:53%">8</b></td><td class="xo-x"><b style="--c:var(--xo-pt);--a:36%">2</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-stress);--a:55%">9</b></td><td class="xo-x"><b style="--c:var(--xo-mito);--a:39%">3</b></td><td class="xo-more">…</td><td class="xo-seam"><div></div></td><td class="xo-o">P2</td><td class="xo-o xo-n">22</td><td class="xo-o xo-n">4</td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-pt)">PT</span></td><td class="xo-o"><span class="xo-pill xo-alt">altered</span></td></tr>
<tr tabindex="0"><td class="xo-bc">L2_AACAACCTCG…</td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-pod);--a:48%">6</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-more">…</td><td class="xo-seam"><div></div></td><td class="xo-o">P2</td><td class="xo-o xo-n">6</td><td class="xo-o xo-n">1</td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-pod)">POD</span></td><td class="xo-o"><span class="xo-pill">reference</span></td></tr>
<tr tabindex="0"><td class="xo-bc">L3_AACCTGAAGT…</td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-tal);--a:43%">4</b></td><td class="xo-x"><b style="--c:var(--xo-tal);--a:30%">1</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-stress);--a:48%">6</b></td><td class="xo-x"><b style="--c:var(--xo-mito);--a:36%">2</b></td><td class="xo-more">…</td><td class="xo-seam"><div></div></td><td class="xo-o">P3</td><td class="xo-o xo-n">13</td><td class="xo-o xo-n">4</td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-tal)">TAL</span></td><td class="xo-o"><span class="xo-pill xo-alt">altered</span></td></tr>
<tr tabindex="0"><td class="xo-bc">L3_AACGTCAGTA…</td><td class="xo-x"><b style="--c:var(--xo-pt);--a:66%">15</b></td><td class="xo-x"><b style="--c:var(--xo-pt);--a:48%">6</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-more">…</td><td class="xo-seam"><div></div></td><td class="xo-o">P3</td><td class="xo-o xo-n">21</td><td class="xo-o xo-n">2</td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-pt)">PT</span></td><td class="xo-o"><span class="xo-pill">reference</span></td></tr>
</tbody>
<tfoot><tr class="xo-under"><td></td><td colspan="8"><div>特征 · 几万列，绝大多数是 0</div></td><td></td><td><div>分组 ID</div></td><td colspan="2"><div>质量 · 由 X 这一行算出</div></td><td colspan="2"><div>标签 · 人工判读</div></td></tr></tfoot></table></div>
<p class="xo-hint">点击图片放大，再点一次或按 Esc 关闭</p>
<ul class="xo-key"><li><span class="xo-ic">行</span><span>一个细胞（核）。左边的 barcode 是它的 ID：一段 16 个字母的 DNA 序列，实验时被抄进这个核里每条被抓到的 mRNA 的 cDNA 上（模块 5.1）；前缀 L1、L2 是文库（library，一个样本的一次 10x 反应），防止不同文库的 barcode 撞号</span></li><li><span class="xo-ic">列</span><span>一个基因；下方色条表示它是哪类细胞的标志基因：青色 PT，蓝色 TAL，紫色足细胞，橙色应激，灰色线粒体</span></li><li><span class="xo-ic">数</span><span>数到的 RNA 分子数，颜色越深越多；灰点是 0</span></li></ul>
<figcaption>数字、barcode 和病人编号都是示意，只画了 7 个基因；把鼠标放在一行上，左右两边一起高亮。nCount 是这一行所有数字之和，nFeature 是这一行非零格子的个数，所以本图里两者只按这 7 个基因计算。`MT-CO1` 这一列也只是示意：Lake 公开的矩阵里已经去掉了线粒体基因（见第 2 步）。第 3 行和第 1 行都是 PT，但第 3 行的应激基因 FOS 很高，被标为 altered：这种差别就是我们要检测的异常。</figcaption></figure>

## 第 1 步 · 计数矩阵 X

**X** 是一张很大的稀疏矩阵：

- **一行 = 一个细胞**（或一个细胞核，模块 5.1 会讲两者的区别）；
- **一列 = 一个基因**；
- **一个数字 = 在这个细胞里测到这个基因的 RNA 分子有几条。**

原始的 X 是整数计数。但公开下载的文件里，X 常常已经被处理过：比如 CELLxGENE 文件里的 `X` 是归一化后的小数，原始计数放在 `raw.X` 里 [3]；Lake 2023 的单细胞数据用 SoupX 减过 ambient RNA [1]，GEO 单细胞标签表里 88% 的 `nCount_RNA` 不是整数（我们数的）[2]（模块 6）。

图里的数字是编的，只是示意。真实的规模来自 Lake 2023 的单核数据（我们从 GEO 标签表数出来的）[2]：**203,702 个细胞核**；每个核中位测到 **2,694 个 RNA 分子**，分布在 **1,638 个基因**上。基因总数是几万个（CELLxGENE 单核文件有 28,813 个基因 [3]），所以每一行里绝大多数位置是 0。这就是为什么 X 要用稀疏矩阵存。

!!! tip "计算机类比"
    把 X 想成一个 `scipy.sparse` 矩阵，行索引是细胞条形码（一串像 `AAACCCAAGCCGATAG` 的 16 个字母的 DNA 序列 [4]，模块 5.1 讲它从哪来），列索引是基因。每一行可以看成这个细胞的"特征向量"，只不过维度有几万、而且几乎全是 0。

!!! info "生物学提示：LRP2、UMOD 是什么？"
    列名是**基因名**。举两个例子：

    - [`LRP2`](https://www.ncbi.nlm.nih.gov/gene/4036)：编码 megalin，一种把滤液里的蛋白吞回细胞的受体 [6]，位于**近端小管**（PT）细胞的顶端膜上 [7]。
    - [`UMOD`](https://www.ncbi.nlm.nih.gov/gene/7369)：编码 uromodulin，主要由**髓袢升支粗段**（TAL）产生 [8]。一篇综述估计约 85–90% 来自 TAL、10–15% 来自远曲小管前段 [9]；另一篇则写远曲小管不表达它 [8]。

    想查其他基因，在 [NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/) 里搜基因名即可。

## 第 2 步 · 标签表 obs

**obs** 是和 X 行对行对齐的一张表：每个细胞一行，记录这个细胞**来自哪里、质量如何、是什么**。下面是 Lake 2023 单核标签表（GEO）里真实的第一行（挑了部分列）[2]：

| 列 | 值 | 含义 |
|---|---|---|
| `library` | `KB1` | 哪个 10x 文库（一个样本的一次反应） |
| `patient` | `31-10001` | 哪个人 |
| `condition.l2` | `DKD` | 糖尿病肾病 |
| `nCount_RNA` | `5463` | 这个核里的 RNA 分子数（UMI） |
| `nFeature_RNA` | `2996` | 测到的基因数 |
| `percent.mt` | `9.37` | 线粒体 RNA 占比（%） |
| `subclass.l1` | `PT` | 细胞类型：近端小管 |
| `state.l1` | `altered` | 正常 vs 改变 |

三个质量列，原则上都是从 X 的这一行算出来的：

- **`nCount_RNA`** = 这一行所有数字加起来，也就是这个核里一共测到多少个 RNA 分子。这里是 5,463。
- **`nFeature_RNA`** = 这一行里**不是 0 的格子有几个**，也就是测到了多少个不同的基因。这里是 2,996：几万个基因里，只有约 3,000 个至少测到 1 个分子。对整数计数来说它总是 ≤ `nCount_RNA`，因为每个非零格子至少贡献 1 个分子。
- **`percent.mt`** = 线粒体基因（`MT-` 开头）的分子数占 `nCount_RNA` 的百分比。

但在公开的 Lake 文件里，你没法完全重算它们：作者在单核数据里**去掉了线粒体基因** [1]，CELLxGENE 单核文件里一个 `MT-` 基因都没有 [3]，所以 `percent.mt` 只能直接读标签表；把 CELLxGENE 计数（`raw.X`）里这一行加起来，得到 5,424 个分子、2,974 个基因，比标签表里的数略少 [3]。

这三个数太低或太高，常常说明这一行不是一个完好的细胞，比如空液滴、破损的细胞或两个细胞粘在一起 [5]。模块 6 会讲怎么用它们做质控。

obs 里的列可以分成四组，后面的模块会逐个解释它们背后的生物学：

| 组 | 列 | 后面在哪讲 |
|---|---|---|
| 标识 | `library` · `patient` · `specimen` | 模块 4、6 |
| 来源 | `condition.l1/l2` · `tissue_type` · `region.l1/l2` · `sex` | 模块 3、4 |
| 质量 | `nCount_RNA` · `nFeature_RNA` · `percent.mt` | 模块 5.1、6 |
| 答案 | `subclass.l1/l2` · `state.l1/l2` | 模块 2、3 |

还有第三张小表 **var**：每个基因一行，记录基因名等信息。三者装在一起叫 **AnnData**，存成 `.h5ad` 文件 [10]。

!!! warning "同一份数据，不同文件里的列名不一样"
    上面的列名来自 GEO 上的标签表 [2]。从 CELLxGENE 下载的 Lake 2023 文件 [3]：

    - 单核文件有 172,847 个核（GEO 标签表是 203,702 个），人和文库的列叫 `donor_id`、`library_id`，有 `subclass.l1/l2`，但**没有 `state.l1` / `state.l2`**；
    - 单细胞文件也没有 state 列；整合文件（单核 + 单细胞）有 `state` 和 `state.l2`；
    - `X` 是归一化后的值，原始计数在 `raw.X`；基因名在 `var["feature_name"]`，行索引是 Ensembl ID。

    所以要用 `state` 标签，最简单的是读 GEO 标签表，或者用整合文件。

```python
import pandas as pd
import scanpy as sc

# GEO label table (203,702 nuclei; has state.l1 / state.l2)
labels = pd.read_csv(
    "GSE183277_Kidney_Healthy-Injury_Cell_Atlas_snCv3_Metadata_03282022.txt.gz",
    sep="\t", index_col=0,
    dtype={"patient": str})   # patient IDs mix numbers and text; read as text or one person can split into two groups
labels["state.l1"].value_counts()

# CELLxGENE single-nucleus h5ad (172,847 nuclei; no state columns)
adata = sc.read_h5ad("<downloaded single-nucleus file>.h5ad")
adata.raw.X                  # raw counts, cells x genes (sparse)
adata.X                      # normalised values
adata.obs[["donor_id", "library_id", "subclass.l1"]]
adata.var["feature_name"]    # gene symbols; the index holds Ensembl IDs
```

## 第 3 步 · 用机器学习的话说

- **特征**：X 的一行。
- **标签**：obs 里的 `subclass`（细胞类型）和 `state`（正常 / 改变）。注意这些标签是作者先聚类、再看标记基因人工判读、按簇赋给细胞的 [1][2]，**不是实验直接测到的真值**（模块 2 和模块 6 会讲为什么这很重要）。
- **分组 ID**：`patient` 和 `library`。同一个人、同一个文库的细胞共享很多东西：同一个人的基因背景、同一批试剂和操作带来的偏差。

!!! warning "最常见的坑：按细胞随机切分"
    一个人贡献几千个细胞（Lake 单核数据有 36 人，中位每人约 5,016 个核 [2]）。如果把细胞随机分到训练集和测试集，同一个人的细胞两边都有，模型可以靠"认人"或"认批次"拿高分，换一个新病人就不灵了。**训练和测试要按 `patient` 分开**（必要时也按 `library` 分开）。这和推荐系统里按用户切分、避免同一用户的数据泄漏，是同一个道理。

## 自测

??? question "1. X 的一行、一列、一个数字分别是什么？"
    一行是一个细胞（或细胞核），一列是一个基因，一个数字是这个细胞里测到的这个基因的 RNA 分子数（原始计数；下载的文件里 X 可能已经归一化）。

??? question "2. `nCount_RNA` 和 `nFeature_RNA` 有什么不同？"
    `nCount_RNA` 是这一行所有数字的和（一共测到多少个 RNA 分子）；`nFeature_RNA` 是这一行里非零的个数（测到了多少个不同的基因）。

??? question "3. 为什么不能把细胞随机分成训练集和测试集？"
    同一个人和同一个文库的细胞高度相关，随机切分会让测试集里出现训练时见过的人和批次，结果虚高。应该按 `patient`（必要时按 `library`）切分。

## 参考文献

1. Lake BB, Menon R, Winfree S, et al. An atlas of healthy and injured cell states and niches in the human kidney. *Nature* 2023;619:585–594. [doi:10.1038/s41586-023-05769-3](https://doi.org/10.1038/s41586-023-05769-3) — Methods, "Quality control of sequencing data" ("Mitochondrial transcripts (MT-*) were removed"; scCv3 "corrected using SoupX") and "Clustering snCv3" (cluster decision tree; "Annotations of clusters were based on known positive and negative cell type markers"). Deep-read: [Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md).
2. GEO GSE183277: `GSE183277_Kidney_Healthy-Injury_Cell_Atlas_snCv3_Metadata_03282022.txt.gz` and `…_Metadata_Field_Descriptions.txt.gz` ([GEO files](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE183nnn/GSE183277/suppl/)) — first row; medians; nuclei per patient; field descriptions ("Subclass annotations for clusters", "Injury (altered) or healthy (reference) state for clusters"). Also GSE183276 `GSE183276_Kidney_Healthy-Injury_Cell_Atlas_scCv3_Metadata_03282022.txt.gz` ([GEO files](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE183nnn/GSE183276/suppl/)): non-integer `nCount_RNA`. Counted by us.
3. CZ CELLxGENE, collection "An atlas of healthy and injured cell states and niches in the human kidney" ([link](https://cellxgene.cziscience.com/collections/bcb61471-2a44-4d00-a0af-ff085512674c)) — datasets "Single-nucleus RNA-seq of the Adult Human Kidney (Version 1.0)" (172,847 × 28,813), "Single-cell RNA-seq…" and "Integrated…"; obs and var column names, `X` vs `raw.X`, and row sums checked by us.
4. 10x Genomics. Technical Note CG000201 Rev A: Chromium Single Cell 3′ v3 reagent, workflow & software updates. [PDF](https://cdn.10xgenomics.com/image/upload/v1660261285/support-documents/CG000201_TechNote_Chromium_Single_Cell_3___v3_Reagent__Workflow___Software_Updates_RevA.pdf) — "16 nt 10x Barcode"; "barcoded, full-length cDNA from poly-adenylated mRNA".
5. Luecken MD, Theis FJ. Current best practices in single-cell RNA-seq analysis: a tutorial. *Mol Syst Biol* 2019;15:e8746. [doi:10.15252/msb.20188746](https://doi.org/10.15252/msb.20188746) — section "Quality control" (low counts / few genes / high mitochondrial fraction = broken cell; high counts = possible doublet).
6. NCBI Gene 4036 (LRP2). [link](https://www.ncbi.nlm.nih.gov/gene/4036) — RefSeq summary ("multi-ligand endocytic receptor… primarily in absorptive epithelial tissues such as the kidney"; ligands include albumin).
7. De S, Kuwahara S, Saito A. The endocytic receptor megalin and its associated proteins in proximal tubule epithelial cells. *Membranes* 2014;4:333–355. [doi:10.3390/membranes4030333](https://doi.org/10.3390/membranes4030333) — abstract ("expressed in the apical membrane of PTECs").
8. Mount DB. Thick ascending limb of the loop of Henle. *Clin J Am Soc Nephrol* 2014;9:1974–1986. [doi:10.2215/CJN.04480413](https://doi.org/10.2215/CJN.04480413) — section "Uromodulin" ("not expressed by macula densa cells or the downstream DCT").
9. Karagiannidis AG, Theodorakopoulou MP, Pella E, Sarafidis PA, Ortiz A. Uromodulin biology. *Nephrol Dial Transplant* 2024;39:1073–1087. [doi:10.1093/ndt/gfae008](https://doi.org/10.1093/ndt/gfae008) — Introduction ("TAL (85%–90%) and early distal convoluted tubule (DCT) (10%–15%)").
10. anndata documentation. [link](https://anndata.readthedocs.io/en/stable/) — AnnData object (`X`, `obs`, `var`, `raw`) and the `.h5ad` format.

## 本模块名词

| 中文 | English | 一句话 |
|---|---|---|
| [计数矩阵](glossary.md#count-matrix) | Count matrix | 单细胞数据的主表：每行一个细胞（或细胞核），每列一个基因，数值是该细胞里测到的该基因 RNA 分子数（UMI 数）；非常稀疏。 |
| [AnnData / h5ad 文件](glossary.md#anndata-h5ad) | AnnData / h5ad | Python（scanpy）里存单细胞数据的容器，存成 .h5ad（HDF5）文件：计数矩阵 X，加每个细胞的标签表 obs 和每个基因的信息 var。 |
| [obs / var（细胞和基因的信息表）](glossary.md#obs-var) | obs / var (cell and gene metadata) | 和计数矩阵对齐的两张表：obs 每个细胞一行（病人、文库、质量指标、细胞类型和状态标签），var 每个基因一行（基因名等信息）。 |
| [基因符号（HGNC）](glossary.md#gene-symbol) | Gene symbol (HGNC) | 由 HGNC 定的人类基因官方简称，比如 LRP2、UMOD；计数矩阵的列名就是它。MT- 开头的是线粒体 DNA 编码的基因。 |
| [按病人切分（数据泄漏）](glossary.md#patient-level-split) | Patient-level split (data leakage) | 把同一个病人（必要时同一个文库）的所有细胞放在训练集或测试集的同一边；按细胞随机切分会把病人和批次信息泄漏到测试集，分数虚高。 |
