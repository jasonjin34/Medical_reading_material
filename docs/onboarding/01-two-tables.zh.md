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
<ul class="xo-key"><li><span class="xo-ic">行</span><span>一个细胞（核）。左边的 barcode 是它的 ID：一段 16 个字母的 DNA 序列，实验时贴在这个核的每条 RNA 上（模块 5）；前缀 L1、L2 是批次（library），防止不同批次的 barcode 撞号</span></li><li><span class="xo-ic">列</span><span>一个基因；下方色条表示它是哪类细胞的标志基因：青色 PT，蓝色 TAL，紫色足细胞，橙色应激，灰色线粒体</span></li><li><span class="xo-ic">数</span><span>数到的 RNA 分子数，颜色越深越多；灰点是 0</span></li></ul>
<figcaption>数字、barcode 和病人编号都是示意，只画了 7 个基因；把鼠标放在一行上，左右两边一起高亮。nCount 是这一行所有数字之和，nFeature 是这一行非零格子的个数，所以本图里两者只按这 7 个基因计算。第 3 行和第 1 行都是 PT，但第 3 行的应激基因 FOS 很高，被标为 altered：这种差别就是我们要检测的异常。</figcaption></figure>

## 第 1 步 · 计数矩阵 X

**X** 是一张很大的稀疏整数矩阵：

- **一行 = 一个细胞**（或一个细胞核，模块 5 会讲两者的区别）；
- **一列 = 一个基因**；
- **一个数字 = 在这个细胞里测到这个基因的 RNA 分子有几条。**

图里的数字是编的，只是示意。真实的规模来自 Lake 2023 的单核数据（我们从 GEO 标签表数出来的）：**203,702 个细胞核**；每个核中位测到 **2,694 个 RNA 分子**，分布在 **1,638 个基因**上。基因总数是几万个，所以每一行里绝大多数位置是 0。这就是为什么 X 要用稀疏矩阵存。

!!! tip "计算机类比"
    把 X 想成一个 `scipy.sparse` 矩阵，行索引是细胞条形码（一串像 `AAACCCAAGCCGATAG` 的 DNA 序列，模块 5 讲它从哪来），列索引是基因名。每一行可以看成这个细胞的"特征向量"，只不过维度有几万、而且几乎全是 0。

!!! info "生物学提示：LRP2、UMOD 是什么？"
    列名是**基因名**。举两个例子：

    - [`LRP2`](https://www.ncbi.nlm.nih.gov/gene/4036)：编码 megalin，从滤液里回收蛋白，主要在**近端小管**（PT）表达。
    - [`UMOD`](https://www.ncbi.nlm.nih.gov/gene/7369)：编码 uromodulin，几乎只在**髓袢升支粗段**（TAL）产生。

    想查其他基因，在 [NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/) 里搜基因名即可。

## 第 2 步 · 标签表 obs

**obs** 是和 X 行对行对齐的一张表：每个细胞一行，记录这个细胞**来自哪里、质量如何、是什么**。下面是 Lake 2023 单核标签表里真实的第一行（挑了部分列）：

| 列 | 值 | 含义 |
|---|---|---|
| `library` | `KB1` | 哪一次上机 |
| `patient` | `31-10001` | 哪个人 |
| `condition.l2` | `DKD` | 糖尿病肾病 |
| `nCount_RNA` | `5463` | 这个核里的 RNA 分子数（UMI） |
| `nFeature_RNA` | `2996` | 测到的基因数 |
| `percent.mt` | `9.37` | 线粒体 RNA 占比（%） |
| `subclass.l1` | `PT` | 细胞类型：近端小管 |
| `state.l1` | `altered` | 正常 vs 改变 |

三个质量列都是直接从 X 的这一行算出来的：

- **`nCount_RNA`** = 这一行所有数字加起来，也就是这个核里一共测到多少个 RNA 分子。这里是 5,463。
- **`nFeature_RNA`** = 这一行里**不是 0 的格子有几个**，也就是测到了多少个不同的基因。这里是 2,996：几万个基因里，只有约 3,000 个至少测到 1 个分子。它总是 ≤ `nCount_RNA`，因为每个非零格子至少贡献 1 个分子。
- **`percent.mt`** = 线粒体基因（`MT-` 开头）的分子数占 `nCount_RNA` 的百分比。

这三个数太低或太高，常常说明这一行不是一个完好的细胞，比如空液滴、破损的细胞或两个细胞粘在一起。模块 6 会讲怎么用它们做质控。

obs 里的列可以分成四组，后面的模块会逐个解释它们背后的生物学：

| 组 | 列 | 后面在哪讲 |
|---|---|---|
| 标识 | `library` · `patient` · `specimen` | 模块 4、6 |
| 来源 | `condition` · `tissue_type` · `region` · `sex` | 模块 3、4 |
| 质量 | `nCount_RNA` · `nFeature_RNA` · `percent.mt` | 模块 5、6 |
| 答案 | `subclass.l1/l2` · `state.l1/l2` | 模块 2、3 |

还有第三张小表 **var**：每个基因一行，记录基因名等信息。三者装在一起叫 **AnnData**，存成 `.h5ad` 文件。

```python
import scanpy as sc
adata = sc.read_h5ad("lake2023_sn.h5ad")   # any h5ad from cellxgene
adata.X          # sparse count matrix, cells x genes
adata.obs        # pandas DataFrame, one row per cell
adata.var        # pandas DataFrame, one row per gene
adata.obs["state.l1"].value_counts()
```

## 第 3 步 · 用机器学习的话说

- **特征**：X 的一行。
- **标签**：obs 里的 `subclass`（细胞类型）和 `state`（正常 / 改变）。注意这些标签是作者先聚类、再人工判读出来的，**不是实验直接测到的真值**（模块 2 和模块 8 会讲为什么这很重要）。
- **分组 ID**：`patient` 和 `library`。同一个人、同一次上机的细胞共享很多东西：同一个人的基因背景、同一批试剂和操作带来的偏差。

!!! warning "最常见的坑：按细胞随机切分"
    一个人贡献几千个细胞。如果把细胞随机分到训练集和测试集，同一个人的细胞两边都有，模型可以靠"认人"或"认批次"拿高分，换一个新病人就不灵了。**训练和测试要按 `patient` 分开**（必要时也按 `library` 分开）。这和推荐系统里按用户切分、避免同一用户的数据泄漏，是同一个道理。

## 自测

??? question "1. X 的一行、一列、一个数字分别是什么？"
    一行是一个细胞（或细胞核），一列是一个基因，一个数字是这个细胞里测到的这个基因的 RNA 分子数。

??? question "2. `nCount_RNA` 和 `nFeature_RNA` 有什么不同？"
    `nCount_RNA` 是这一行所有数字的和（一共测到多少个 RNA 分子）；`nFeature_RNA` 是这一行里非零的个数（测到了多少个不同的基因）。

??? question "3. 为什么不能把细胞随机分成训练集和测试集？"
    同一个人和同一次上机的细胞高度相关，随机切分会让测试集里出现训练时见过的人和批次，结果虚高。应该按 `patient`（必要时按 `library`）切分。

## 本模块名词

| 中文 | English | 一句话 |
|---|---|---|
| [计数矩阵](glossary.md#count-matrix) | Count matrix | 单细胞数据的主表：每行一个细胞（或细胞核），每列一个基因，数值是该细胞里测到的该基因 RNA 分子数（UMI 数）；非常稀疏。 |
| [AnnData / h5ad 文件](glossary.md#anndata-h5ad) | AnnData / h5ad | Python（scanpy）里存单细胞数据的容器，存成 .h5ad（HDF5）文件：计数矩阵 X，加每个细胞的标签表 obs 和每个基因的信息 var。 |
| [obs / var（细胞和基因的信息表）](glossary.md#obs-var) | obs / var (cell and gene metadata) | 和计数矩阵对齐的两张表：obs 每个细胞一行（病人、批次、质量指标、细胞类型和状态标签），var 每个基因一行（基因名等信息）。 |
| [基因符号（HGNC）](glossary.md#gene-symbol) | Gene symbol (HGNC) | 由 HGNC 定的人类基因官方简称，比如 LRP2、UMOD；计数矩阵的列名就是它。MT- 开头的是线粒体 DNA 编码的基因。 |
| [按病人切分（数据泄漏）](glossary.md#patient-level-split) | Patient-level split (data leakage) | 把同一个病人（必要时同一次上机）的所有细胞放在训练集或测试集的同一边；按细胞随机切分会把病人和批次信息泄漏到测试集，分数虚高。 |
