# 1 · 两张表：X 和 obs / 1 · Two tables: X and obs

<!-- ZH -->
!!! abstract "读完能回答"
    - 单细胞数据最后变成哪两张表？
    - 矩阵的一行、一列、一个数字分别代表什么？
    - 哪个字段是标签，哪个字段是分组 ID？为什么不能随机切分训练集和测试集？
<!-- EN -->
!!! abstract "After this module you can answer"
    - Which two tables does single-cell data end up as?
    - What do a row, a column and a number in the matrix mean?
    - Which field is the label and which is the group ID, and why can't you split train and test at random?

<!-- ZH -->
先从终点讲起。后面几个模块讲的生物和实验，最后都会落到这两张表里。先知道终点长什么样，读后面的内容时就知道每个概念最后变成了表里的什么。
<!-- EN -->
We start at the end. All the biology and lab work in the next modules ends up in these two tables. Knowing the destination first tells you, for every later concept, what it becomes in the data.

<!-- ZH -->
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

<!-- EN -->
The figure below draws the two tables side by side: X on the left, obs on the right, and **the same row is the same cell**. Take it in as a whole first; the steps below go through each table.

<figure class="xobs" markdown="0"><div class="xo-scroll"><table aria-label="Count matrix X aligned row by row with label table obs">
<thead><tr class="xo-cap"><th></th><th colspan="8"><span class="xo-tag">X</span>count matrix <span class="xo-sub">· cells × genes</span></th><th></th><th colspan="5"><span class="xo-tag">obs</span>label table <span class="xo-sub">· one row per cell</span></th></tr>
<tr class="xo-genes"><th></th><th>LRP2<i style="background:var(--xo-pt)"></i></th><th>CUBN<i style="background:var(--xo-pt)"></i></th><th>UMOD<i style="background:var(--xo-tal)"></i></th><th>SLC12A1<i style="background:var(--xo-tal)"></i></th><th>NPHS2<i style="background:var(--xo-pod)"></i></th><th>FOS<i style="background:var(--xo-stress)"></i></th><th>MT-CO1<i style="background:var(--xo-mito)"></i></th><th></th><th></th><th class="xo-o">patient</th><th class="xo-o xo-n">nCount</th><th class="xo-o xo-n">nFeature</th><th class="xo-o">subclass</th><th class="xo-o">state</th></tr></thead>
<tbody>
<tr tabindex="0"><td class="xo-bc">L1_AAACCCAAGC…</td><td class="xo-x"><b style="--c:var(--xo-pt);--a:61%">12</b></td><td class="xo-x"><b style="--c:var(--xo-pt);--a:46%">5</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-mito);--a:30%">1</b></td><td class="xo-more">…</td><td class="xo-seam"><div></div></td><td class="xo-o">P1</td><td class="xo-o xo-n">18</td><td class="xo-o xo-n">3</td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-pt)">PT</span></td><td class="xo-o"><span class="xo-pill">reference</span></td></tr>
<tr tabindex="0"><td class="xo-bc">L1_AAACGAATCA…</td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-tal);--a:80%">25</b></td><td class="xo-x"><b style="--c:var(--xo-tal);--a:51%">7</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-more">…</td><td class="xo-seam"><div></div></td><td class="xo-o">P1</td><td class="xo-o xo-n">32</td><td class="xo-o xo-n">2</td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-tal)">TAL</span></td><td class="xo-o"><span class="xo-pill">reference</span></td></tr>
<tr tabindex="0"><td class="xo-bc">L2_AAAGGATGTC…</td><td class="xo-x"><b style="--c:var(--xo-pt);--a:53%">8</b></td><td class="xo-x"><b style="--c:var(--xo-pt);--a:36%">2</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-stress);--a:55%">9</b></td><td class="xo-x"><b style="--c:var(--xo-mito);--a:39%">3</b></td><td class="xo-more">…</td><td class="xo-seam"><div></div></td><td class="xo-o">P2</td><td class="xo-o xo-n">22</td><td class="xo-o xo-n">4</td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-pt)">PT</span></td><td class="xo-o"><span class="xo-pill xo-alt">altered</span></td></tr>
<tr tabindex="0"><td class="xo-bc">L2_AACAACCTCG…</td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-pod);--a:48%">6</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-more">…</td><td class="xo-seam"><div></div></td><td class="xo-o">P2</td><td class="xo-o xo-n">6</td><td class="xo-o xo-n">1</td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-pod)">POD</span></td><td class="xo-o"><span class="xo-pill">reference</span></td></tr>
<tr tabindex="0"><td class="xo-bc">L3_AACCTGAAGT…</td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-tal);--a:43%">4</b></td><td class="xo-x"><b style="--c:var(--xo-tal);--a:30%">1</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-stress);--a:48%">6</b></td><td class="xo-x"><b style="--c:var(--xo-mito);--a:36%">2</b></td><td class="xo-more">…</td><td class="xo-seam"><div></div></td><td class="xo-o">P3</td><td class="xo-o xo-n">13</td><td class="xo-o xo-n">4</td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-tal)">TAL</span></td><td class="xo-o"><span class="xo-pill xo-alt">altered</span></td></tr>
<tr tabindex="0"><td class="xo-bc">L3_AACGTCAGTA…</td><td class="xo-x"><b style="--c:var(--xo-pt);--a:66%">15</b></td><td class="xo-x"><b style="--c:var(--xo-pt);--a:48%">6</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-more">…</td><td class="xo-seam"><div></div></td><td class="xo-o">P3</td><td class="xo-o xo-n">21</td><td class="xo-o xo-n">2</td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-pt)">PT</span></td><td class="xo-o"><span class="xo-pill">reference</span></td></tr>
</tbody>
<tfoot><tr class="xo-under"><td></td><td colspan="8"><div>features · tens of thousands of columns, mostly 0</div></td><td></td><td><div>group ID</div></td><td colspan="2"><div>quality · computed from the X row</div></td><td colspan="2"><div>labels · assigned by experts</div></td></tr></tfoot></table></div>
<p class="xo-hint">Click the figure to enlarge; click again or press Esc to close</p>
<ul class="xo-key"><li><span class="xo-ic">row</span><span>one cell (nucleus). The barcode on the left is its ID: a 16-letter DNA sequence attached to every RNA of this nucleus during the experiment (module 5); the prefix L1, L2 is the library (batch), so barcodes from different batches do not collide</span></li><li><span class="xo-ic">column</span><span>one gene; the bar under its name shows which cell type it marks: teal PT, blue TAL, purple podocyte, orange stress, grey mitochondrial</span></li><li><span class="xo-ic">number</span><span>RNA molecules counted; darker means more, a grey dot is 0</span></li></ul>
<figcaption>Numbers, barcodes and patient IDs are illustrative, and only 7 genes are drawn; hover over a row to highlight it on both sides. nCount is the sum of the row and nFeature the number of non-zero entries, so here both count only these 7 genes. Rows 3 and 1 are both PT, but row 3 has high FOS, a stress gene, and is labelled altered: that difference is the anomaly we want to detect.</figcaption></figure>

## 第 1 步 · 计数矩阵 X / Step 1 · The count matrix X

<!-- ZH -->
**X** 是一张很大的稀疏整数矩阵：

- **一行 = 一个细胞**（或一个细胞核，模块 5 会讲两者的区别）；
- **一列 = 一个基因**；
- **一个数字 = 在这个细胞里测到这个基因的 RNA 分子有几条。**
<!-- EN -->
**X** is a large, sparse integer matrix:

- **one row = one cell** (or one nucleus; module 5 explains the difference);
- **one column = one gene**;
- **one number = how many RNA molecules of that gene were detected in that cell.**


<!-- ZH -->
图里的数字是编的，只是示意。真实的规模来自 Lake 2023 的单核数据（我们从 GEO 标签表数出来的）：**203,702 个细胞核**；每个核中位测到 **2,694 个 RNA 分子**，分布在 **1,638 个基因**上。基因总数是几万个，所以每一行里绝大多数位置是 0。这就是为什么 X 要用稀疏矩阵存。
<!-- EN -->
The numbers in the figure are made up for illustration. The real scale, from Lake 2023's single-nucleus data (counted by us from the GEO label table): **203,702 nuclei**; each nucleus has a median of **2,694 RNA molecules** spread over **1,638 genes**. With tens of thousands of genes, almost every entry in a row is 0, which is why X is stored as a sparse matrix.

<!-- ZH -->
!!! tip "计算机类比"
    把 X 想成一个 `scipy.sparse` 矩阵，行索引是细胞条形码（一串像 `AAACCCAAGCCGATAG` 的 DNA 序列，模块 5 讲它从哪来），列索引是基因名。每一行可以看成这个细胞的"特征向量"，只不过维度有几万、而且几乎全是 0。
<!-- EN -->
!!! tip "Computer analogy"
    Think of X as a `scipy.sparse` matrix whose row index is the cell barcode (a DNA string like `AAACCCAAGCCGATAG`; module 5 explains where it comes from) and whose column index is the gene name. Each row is that cell's feature vector, just with tens of thousands of dimensions, nearly all zero.

<!-- ZH -->
!!! info "生物学提示：LRP2、UMOD 是什么？"
    列名是**基因名**。举两个例子：

    - [`LRP2`](https://www.ncbi.nlm.nih.gov/gene/4036)：编码 megalin，从滤液里回收蛋白，主要在**近端小管**（PT）表达。
    - [`UMOD`](https://www.ncbi.nlm.nih.gov/gene/7369)：编码 uromodulin，几乎只在**髓袢升支粗段**（TAL）产生。

    想查其他基因，在 [NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/) 里搜基因名即可。
<!-- EN -->
!!! info "Biology note: what are LRP2 and UMOD?"
    The column names are **gene names**. Two examples:

    - [`LRP2`](https://www.ncbi.nlm.nih.gov/gene/4036): encodes megalin, which takes proteins back from the filtered fluid; mainly in the **proximal tubule** (PT).
    - [`UMOD`](https://www.ncbi.nlm.nih.gov/gene/7369): encodes uromodulin, made almost only in the **thick ascending limb** (TAL).

    To look up any other gene, search its name in [NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/).

## 第 2 步 · 标签表 obs / Step 2 · The label table obs

<!-- ZH -->
**obs** 是和 X 行对行对齐的一张表：每个细胞一行，记录这个细胞**来自哪里、质量如何、是什么**。下面是 Lake 2023 单核标签表里真实的第一行（挑了部分列）：
<!-- EN -->
**obs** is a table aligned row-for-row with X: one row per cell, recording **where the cell came from, how good its measurement is, and what it is**. Below is the real first row of Lake 2023's single-nucleus label table (selected columns):

| Column / 列 | Value / 值 | Meaning / 含义 |
|---|---|---|
| `library` | `KB1` | which sequencing run / 哪一次上机 |
| `patient` | `31-10001` | which person / 哪个人 |
| `condition.l2` | `DKD` | diabetic kidney disease / 糖尿病肾病 |
| `nCount_RNA` | `5463` | RNA molecules (UMIs) in this nucleus / 这个核里的 RNA 分子数（UMI） |
| `nFeature_RNA` | `2996` | genes detected / 测到的基因数 |
| `percent.mt` | `9.37` | % mitochondrial RNA / 线粒体 RNA 占比（%） |
| `subclass.l1` | `PT` | cell type: proximal tubule / 细胞类型：近端小管 |
| `state.l1` | `altered` | reference (normal) vs altered / 正常 vs 改变 |

<!-- ZH -->
三个质量列都是直接从 X 的这一行算出来的：

- **`nCount_RNA`** = 这一行所有数字加起来，也就是这个核里一共测到多少个 RNA 分子。这里是 5,463。
- **`nFeature_RNA`** = 这一行里**不是 0 的格子有几个**，也就是测到了多少个不同的基因。这里是 2,996：几万个基因里，只有约 3,000 个至少测到 1 个分子。它总是 ≤ `nCount_RNA`，因为每个非零格子至少贡献 1 个分子。
- **`percent.mt`** = 线粒体基因（`MT-` 开头）的分子数占 `nCount_RNA` 的百分比。

这三个数太低或太高，常常说明这一行不是一个完好的细胞，比如空液滴、破损的细胞或两个细胞粘在一起。模块 6 会讲怎么用它们做质控。
<!-- EN -->
The three quality columns are computed straight from this row of X:

- **`nCount_RNA`** = the sum of the row: how many RNA molecules were detected in this nucleus. Here 5,463.
- **`nFeature_RNA`** = **how many entries in the row are not 0**: how many different genes were detected. Here 2,996: out of tens of thousands of genes, only about 3,000 have at least one molecule. It is always ≤ `nCount_RNA`, since every non-zero entry contributes at least one molecule.
- **`percent.mt`** = the share of `nCount_RNA` that comes from mitochondrial genes (names starting with `MT-`), in percent.

Values that are too low or too high often mean the row is not one intact cell: an empty droplet, a broken cell, or two cells stuck together. Module 6 shows how they are used for quality control.

<!-- ZH -->
obs 里的列可以分成四组，后面的模块会逐个解释它们背后的生物学：
<!-- EN -->
The obs columns fall into four groups; later modules explain the biology behind each:

| Group / 组 | Columns / 列 | Explained in / 后面在哪讲 |
|---|---|---|
| IDs / 标识 | `library` · `patient` · `specimen` | modules 4, 6 / 模块 4、6 |
| Origin / 来源 | `condition` · `tissue_type` · `region` · `sex` | modules 3, 4 / 模块 3、4 |
| Quality / 质量 | `nCount_RNA` · `nFeature_RNA` · `percent.mt` | modules 5, 6 / 模块 5、6 |
| Answers / 答案 | `subclass.l1/l2` · `state.l1/l2` | modules 2, 3 / 模块 2、3 |

<!-- ZH -->
还有第三张小表 **var**：每个基因一行，记录基因名等信息。三者装在一起叫 **AnnData**，存成 `.h5ad` 文件。
<!-- EN -->
A third, small table, **var**, has one row per gene (names and other gene information). The three together form an **AnnData** object, saved as an `.h5ad` file.

```python
import scanpy as sc
adata = sc.read_h5ad("lake2023_sn.h5ad")   # any h5ad from cellxgene
adata.X          # sparse count matrix, cells x genes
adata.obs        # pandas DataFrame, one row per cell
adata.var        # pandas DataFrame, one row per gene
adata.obs["state.l1"].value_counts()
```

## 第 3 步 · 用机器学习的话说 / Step 3 · In machine-learning terms

<!-- ZH -->
- **特征**：X 的一行。
- **标签**：obs 里的 `subclass`（细胞类型）和 `state`（正常 / 改变）。注意这些标签是作者先聚类、再人工判读出来的，**不是实验直接测到的真值**（模块 2 和模块 8 会讲为什么这很重要）。
- **分组 ID**：`patient` 和 `library`。同一个人、同一次上机的细胞共享很多东西：同一个人的基因背景、同一批试剂和操作带来的偏差。
<!-- EN -->
- **Features**: a row of X.
- **Labels**: `subclass` (cell type) and `state` (reference / altered) in obs. These labels were assigned by the authors after clustering and manual review; **they are not measured ground truth** (modules 2 and 8 explain why that matters).
- **Group IDs**: `patient` and `library`. Cells from the same person or the same sequencing run share a lot: the person's genetic background, and the bias of one batch of reagents and handling.

<!-- ZH -->
!!! warning "最常见的坑：按细胞随机切分"
    一个人贡献几千个细胞。如果把细胞随机分到训练集和测试集，同一个人的细胞两边都有，模型可以靠"认人"或"认批次"拿高分，换一个新病人就不灵了。**训练和测试要按 `patient` 分开**（必要时也按 `library` 分开）。这和推荐系统里按用户切分、避免同一用户的数据泄漏，是同一个道理。
<!-- EN -->
!!! warning "The most common trap: splitting by cell at random"
    One person contributes thousands of cells. If cells are split at random, the same person ends up on both sides, and a model can score well by recognising the person or the batch, then fail on a new patient. **Split train and test by `patient`** (and by `library` where needed). It is the same reason recommender systems split by user to avoid leakage.

## 自测 / Self-check

<!-- ZH -->
??? question "1. X 的一行、一列、一个数字分别是什么？"
    一行是一个细胞（或细胞核），一列是一个基因，一个数字是这个细胞里测到的这个基因的 RNA 分子数。

??? question "2. `nCount_RNA` 和 `nFeature_RNA` 有什么不同？"
    `nCount_RNA` 是这一行所有数字的和（一共测到多少个 RNA 分子）；`nFeature_RNA` 是这一行里非零的个数（测到了多少个不同的基因）。

??? question "3. 为什么不能把细胞随机分成训练集和测试集？"
    同一个人和同一次上机的细胞高度相关，随机切分会让测试集里出现训练时见过的人和批次，结果虚高。应该按 `patient`（必要时按 `library`）切分。
<!-- EN -->
??? question "1. What are a row, a column and a number of X?"
    A row is a cell (or nucleus), a column is a gene, and a number is how many RNA molecules of that gene were detected in that cell.

??? question "2. How do `nCount_RNA` and `nFeature_RNA` differ?"
    `nCount_RNA` is the sum of the row (total RNA molecules detected); `nFeature_RNA` is the number of non-zero entries in the row (how many different genes were detected).

??? question "3. Why not split cells into train and test at random?"
    Cells from the same person and the same run are strongly correlated, so a random split puts people and batches seen in training into the test set and inflates the score. Split by `patient` (and by `library` where needed).
