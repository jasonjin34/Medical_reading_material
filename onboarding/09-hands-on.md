# 9 · 动手 / 9 · Hands-on

<!-- ZH -->
!!! abstract "读完能回答"
    - 怎么下载并读入 Lake 2023 的标签表和 h5ad？
    - 怎么复现"退化细胞在单核里基因少、线粒体高"这个结果？
    - 怎么跑一个最简单的异常打分、算 AUROC，以及为什么这还不够？
<!-- EN -->
!!! abstract "After this module you can answer"
    - How do you download and load Lake 2023's label table and h5ad?
    - How do you reproduce 'degenerative nuclei have fewer genes and more mitochondrial RNA'?
    - How do you run the simplest anomaly score, compute AUROC, and see why that is not enough?

<!-- ZH -->
这是第 2 天的内容，可选。分两段：

- **A 段**（约 1 小时）：只下载 19 MB 的标签表，复现模块 2、模块 8 里的数字，笔记本电脑就够。
- **B 段**（约 2 小时）：再下载 1.6 GB 的计数矩阵，跑一个健康参考 kNN 异常打分，复现模块 8 的结果。内存需求和机器有关：我们在一台 macOS 电脑上实测最大常驻内存 3.6 GB、峰值内存占用 9.7 GB，建议用 16 GB 内存的电脑（8 GB 的可能会用到交换空间）。运行不到 1 分钟。

下面的代码我们在 2026-10-27 原样跑过（Python 3，scanpy 1.12.4、anndata 0.13.4、scikit-learn 1.9.1），页面上的输出就是那次的结果。每份数据的下载方式和已知问题见 [Lake 2023 数据页](../datasets/lake-2023.md)。
<!-- EN -->
This is day 2 and optional. Two parts:

- **Part A** (about 1 hour): download only the 19 MB label table and reproduce the numbers in modules 2 and 8. A laptop is enough.
- **Part B** (about 2 hours): also download the 1.6 GB count matrix, run a healthy-reference kNN anomaly score and reproduce module 8's results. Memory use depends on the machine: on one macOS computer we measured 3.6 GB maximum resident memory and a 9.7 GB peak memory footprint, so 16 GB is recommended (an 8 GB machine may swap). It runs in under a minute.

We ran the code below verbatim on 2026-10-27 (Python 3, scanpy 1.12.4, anndata 0.13.4, scikit-learn 1.9.1); the outputs shown are from that run. Download routes and known issues are on the [Lake 2023 dataset page](../datasets/lake-2023.md).

<!-- ZH -->
!!! warning "数据放在仓库外面"
    这个仓库是公开的。数据放在自己的目录里，比如 `~/data/kidney/`，不要放进仓库。
<!-- EN -->
!!! warning "Keep data outside the repository"
    This repository is public. Put data in your own folder, such as `~/data/kidney/`, never inside the repository.

## 第 0 步 · 准备环境 / Step 0 · Set up

```bash
mkdir -p ~/data/kidney/lake-2023 && cd ~/data/kidney/lake-2023
python -m venv venv && source venv/bin/activate
pip install scanpy scikit-learn
curl -O https://ftp.ncbi.nlm.nih.gov/geo/series/GSE183nnn/GSE183277/suppl/GSE183277_Kidney_Healthy-Injury_Cell_Atlas_snCv3_Metadata_03282022.txt.gz
```

## A 段 · 只用标签表 / Part A · The label table only

### 第 1 步 · 读入并数一数 / Step 1 · Load and count

<!-- ZH -->
标签表就是模块 1 里的 obs：每行一个核，每列一个字段。下面这段代码读入它，数每种状态有多少核，比较各状态的三个 QC 指标，最后算两个"只看 QC"打分器的 AUROC。
<!-- EN -->
The label table is module 1's obs: one row per nucleus, one column per field. The code reads it, counts the nuclei in each state, compares the three QC metrics across states, and finally computes the AUROC of two QC-only scorers.

```python
import pandas as pd
meta = pd.read_csv("GSE183277_Kidney_Healthy-Injury_Cell_Atlas_snCv3_Metadata_03282022.txt.gz",
                   sep="\t", index_col=0, low_memory=False, dtype={"patient": str})
print(meta.shape)                              # rows = nuclei, columns = obs fields
print(meta["state.l2"].value_counts(dropna=False))

qc = ["nFeature_RNA", "nCount_RNA", "percent.mt"]
print(meta.groupby("state.l2")[qc].median().round(2))

from sklearn.metrics import roc_auc_score
s = meta.dropna(subset=["state.l1"])
y = s["state.l1"] == "altered"                 # 1 = altered, 0 = reference
print("genes (fewer = more anomalous):", roc_auc_score(y, -s["nFeature_RNA"]))
print("percent.mt:", roc_auc_score(y, s["percent.mt"]))

d = s[s["state.l2"].isin(["degenerative", "reference"])]
yd = d["state.l2"] == "degenerative"
print("degenerative only, genes:", roc_auc_score(yd, -d["nFeature_RNA"]))
print("degenerative only, percent.mt:", roc_auc_score(yd, d["percent.mt"]))
```

### 第 2 步 · 看输出 / Step 2 · Read the output

<!-- ZH -->
- 表的大小是 **203,702 × 49**；状态的计数和模块 2 的表一致（reference 128,090，degenerative 42,316……）。
- 各状态的中位数：
<!-- EN -->
- The table is **203,702 × 49**; the state counts match the table in module 2 (reference 128,090, degenerative 42,316…).
- Medians per state:

| state.l2 | nFeature_RNA | nCount_RNA | percent.mt |
|---|---|---|---|
| reference | 1,736 | 2,960 | 0.63 |
| degenerative | 791 | 990 | 2.95 |
| adaptive – epi | 2,426 | 4,612.5 | 0.49 |
| adaptive – str | 1,657 | 2,706 | 0.41 |
| cycling | 1,873 | 3,157 | 0.57 |
| transitioning | 3,420.5 | 7,400 | 1.00 |

<!-- ZH -->
- 只看 QC 的打分器：
<!-- EN -->
- QC-only scorers:

| Score / 打分 | All altered vs reference / 全部 altered | Degenerative vs reference / 只看 degenerative |
|---|---|---|
| fewer genes / 基因越少分越高 | 0.56 | 0.69 |
| higher `percent.mt` / 线粒体越高分越高 | 0.63 | 0.75 |

<!-- ZH -->
degenerative 的基因数不到 reference 的一半，所以"只看 QC"在它身上分数不低；adaptive 的基因反而更多，所以把所有 altered 混在一起时分数就掉下来了。这就是模块 8 说的：**结果要按状态分开报**。

这不全是巧合：Lake 2023 当初就是把"测到的基因少、线粒体转录本多、内质网相关转录本多、损伤标记基因升高、或者在 AKI / CKD 样本里富集"的簇先标成可能的改变态（Methods）。也就是说，"基因少、线粒体高"有一部分是标签定义本身带进来的（模块 2、模块 6）。
<!-- EN -->
Degenerative nuclei have less than half the genes of reference nuclei, so QC alone scores well on them; adaptive nuclei have more genes, so mixing all altered states together drags the score down. As module 8 said: **report results per state**.

This is not a coincidence: Lake 2023 first flagged as possible altered states the clusters with "low genes detected, a high number of mitochondrial transcripts, a high number of endoplasmic-reticulum-associated transcripts, upregulation of injury markers… or enrichment in AKI or CKD samples" (Methods). Part of "few genes, high mito" was built into the labels themselves (modules 2 and 6).

<!-- ZH -->
!!! note "这里的数字和 B 段不同"
    A 段用的是全部细胞类型、全部供体，没有划分训练和测试；B 段只看近端小管（PT），只在没见过的供体上评估。两者回答的问题不一样，数字不能直接比。
<!-- EN -->
!!! note "These numbers differ from Part B"
    Part A uses every cell type and every donor, with no train/test split; Part B looks only at proximal tubule (PT) and evaluates only on unseen donors. They answer different questions, so the numbers are not directly comparable.

## B 段 · 健康参考 kNN 打分 / Part B · A healthy-reference kNN score

### 第 3 步 · 下载计数矩阵 / Step 3 · Download the count matrix

<!-- ZH -->
cellxgene 上的单核文件，1.57 GB：172,847 核 × 28,813 基因。它没有 `state` 标签，要和第 1 步的标签表按细胞 ID 合并（模块 1）。
<!-- EN -->
The single-nucleus file on cellxgene, 1.57 GB: 172,847 nuclei × 28,813 genes. It has no `state` labels, so it is joined to the step 1 label table by cell ID (module 1).

```bash
curl -o lake2023_sn.h5ad https://datasets.cellxgene.cziscience.com/5dc03d39-ac5f-49e1-8630-a64d2e6e293b.h5ad
```

### 第 4 步 · 打分 / Step 4 · Score

<!-- ZH -->
方法是最朴素的一种，正好对应模块 8 第 2 步的那张表：

1. 只看一种细胞类型（PT），这样"异常"指的是状态，而不是细胞类型（模块 2）；
2. 把 13 个健康供体**按人**分成三份：一半做健康参考，四分之一定阈值，四分之一留作测试（模块 1）；
3. 基因选择、标准化和 PCA 都只在参考上拟合，测试数据照着同样的变换投影，防止信息泄漏；
4. 异常分 = 到最近的 10 个健康参考细胞的平均距离；
5. 阈值取定阈值那份供体分数的 95% 分位数，希望误报是 5%。
<!-- EN -->
The method is the plainest possible one, matching the table in module 8, step 2:

1. look at one cell type only (PT), so "anomalous" means a state, not a cell type (module 2);
2. split the 13 healthy donors **by person** into three parts: half as the healthy reference, a quarter to set the threshold, a quarter held out for testing (module 1);
3. fit gene selection, scaling and PCA on the reference only, and project test data with the same transform, so nothing leaks;
4. anomaly score = mean distance to the 10 nearest healthy reference cells;
5. threshold = the 95th percentile of scores on the threshold donors, aiming at 5% false alarms.

```python
import numpy as np, pandas as pd, scanpy as sc
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import roc_auc_score

# 1. counts from cellxgene + state labels from GEO (module 1)
adata = sc.read_h5ad("lake2023_sn.h5ad")
adata.X = adata.raw.X
meta = pd.read_csv("GSE183277_Kidney_Healthy-Injury_Cell_Atlas_snCv3_Metadata_03282022.txt.gz",
                   sep="\t", index_col=0, low_memory=False, dtype={"patient": str})
adata.obs = adata.obs.join(meta[["state.l1", "state.l2", "condition.l1", "patient"]])

# 2. one cell type only, so "anomalous" means a state, not a type (module 2)
pt = adata[adata.obs["subclass.l1"] == "PT"].copy()
sc.pp.normalize_total(pt, target_sum=1e4)
sc.pp.log1p(pt)

# 3. split healthy DONORS, not cells: reference / calibration / test (module 1)
healthy = sorted(pt.obs.loc[pt.obs["condition.l1"] == "Ref", "patient"].unique())
rng = np.random.default_rng(0)
rng.shuffle(healthy)
n = len(healthy)
ref_donors, cal_donors, test_donors = healthy[: n // 2], healthy[n // 2 : 3 * n // 4], healthy[3 * n // 4 :]
reference = pt.obs["state.l1"] == "reference"
is_ref = pt.obs["patient"].isin(ref_donors) & reference
is_cal = pt.obs["patient"].isin(cal_donors) & reference
is_test = (pt.obs["patient"].isin(test_donors) | (pt.obs["condition.l1"] != "Ref")) & pt.obs["state.l1"].notna()

# 4. fit genes, scaling and PCA on the reference only
ref = pt[is_ref].copy()
sc.pp.highly_variable_genes(ref, n_top_genes=2000)
genes = ref.var_names[ref.var["highly_variable"]]
sc.pp.scale(ref, max_value=10)
sc.tl.pca(ref, n_comps=50)
mean, std = ref.var.loc[genes, "mean"].values, ref.var.loc[genes, "std"].values
pcs = ref.varm["PCs"][ref.var_names.get_indexer(genes)]

def embed(a):
    x = np.clip((a[:, genes].X.toarray() - mean) / std, -10, 10)
    return x @ pcs

# 5. anomaly score = mean distance to the 10 nearest healthy reference cells
nn = NearestNeighbors(n_neighbors=10).fit(ref.obsm["X_pca"])
def score(a):
    dist, _ = nn.kneighbors(embed(a))
    return dist.mean(axis=1)

threshold = np.quantile(score(pt[is_cal]), 0.95)   # target: 5% false alarms

# 6. evaluate on held-out donors
test = pt[is_test]
s = score(test)
obs = test.obs
y = (obs["state.l1"] == "altered").values
print("all altered   kNN", roc_auc_score(y, s), " genes", roc_auc_score(y, -obs["nFeature_RNA"]))
for state in ["degenerative", "adaptive - epi"]:
    m = obs["state.l2"].isin([state, "reference"]).values
    yy = (obs["state.l2"][m] == state).values
    print(state, " kNN", roc_auc_score(yy, s[m]), " genes", roc_auc_score(yy, -obs["nFeature_RNA"].values[m]))
healthy_test = (obs["patient"].isin(test_donors) & (obs["state.l1"] == "reference")).values
print("false alarms on held-out healthy donors:", (s[healthy_test] > threshold).mean())
```

### 第 5 步 · 看输出 / Step 5 · Read the output

<!-- ZH -->
用 `default_rng(0)` 的那次划分，测试集有 28,380 个 PT 核，其中 20,477 个是 altered。再把 `0` 换成 1–4，又跑了 4 种划分。结果：
<!-- EN -->
With the `default_rng(0)` split, the test set has 28,380 PT nuclei, 20,477 of them altered. Changing `0` to 1–4 gives 4 more splits. Results:

| Held-out donors / 没见过的供体 | Seed 0 / 种子 0 | Seeds 0–4 / 种子 0–4 |
|---|---|---|
| all altered, kNN / 全部 altered，kNN | 0.67 | 0.67 – 0.76 |
| all altered, gene count / 全部 altered，只数基因 | 0.56 | 0.56 – 0.61 |
| degenerative, kNN / degenerative，kNN | 0.76 | 0.76 – 0.81 |
| degenerative, gene count / degenerative，只数基因 | 0.76 | 0.76 – 0.85 |
| adaptive – epi, kNN / adaptive – epi，kNN | 0.56 | 0.53 – 0.71 |
| adaptive – epi, gene count / adaptive – epi，只数基因 | 0.30 | 0.30 – 0.34 |
| false alarms on healthy test donors (target 5%) / 健康测试供体上的误报（目标 5%） | 0.9% | 0.9% – 6.3% |

<!-- ZH -->
三条读法，对应模块 8 的三个难点：

1. **degenerative 上，kNN 和只数基因差不多**，5 次里有 4 次还更差。漂亮的 AUROC 不说明方法学会了"病"。
2. **我们不知道 kNN 报出来的细胞里有多少是伪影**：Lake 没有伪影标签，这段代码答不了。[课题 1](../research/anomaly-benchmark.md) 的思路就是往数据里注入已知的伪影，再用真实答案检验；第 6 步的练习 6 是一个最小的版本。
3. **误报不稳**：阈值定在 5%，在没见过的健康人身上是 0.9% 到 6.3%。13 个健康人按 6 / 3 / 4 分，测试供体只有 4 个，有的人 PT 核很少（种子 0 里有一个人只有 4 个，种子 1–4 里有一个人只有 3 个），单人的误报率波动很大。
<!-- EN -->
Three readings, matching module 8's three difficulties:

1. **On degenerative cells, kNN is about as good as counting genes**, and worse in 4 of 5 splits. A good AUROC does not show the method learned disease.
2. **We do not know how many kNN-flagged cells are artifacts**: Lake has no artifact labels, so this code cannot answer that. [Topic 1](../research/anomaly-benchmark.md) does exactly this: inject known artifacts into the data, then test on real answers; exercise 6 in step 6 is a minimal version.
3. **False alarms are unstable**: set at 5%, they land between 0.9% and 6.3% on unseen healthy donors. The 13 healthy donors split 6 / 3 / 4, so there are only 4 test donors, and some have very few PT nuclei (one has 4 in seed 0, one has 3 in seeds 1–4), so per-person rates swing widely.

## 第 6 步 · 练习 / Step 6 · Exercises

<!-- ZH -->
这些没有标准答案，结果请自己跑出来再下结论。

1. 把第 4 步代码里第 3 段的按人划分改成**按细胞随机划分**，再算一次误报率。和按人划分比，有什么不同？为什么？
2. 把 `"PT"` 换成 `"TAL"`，结论还成立吗？
3. 把"只数基因"换成 `percent.mt`，或者两者结合，能不能在 degenerative 上追平 kNN？
4. 把 `n_neighbors` 从 10 改成 1 或 50，AUROC 和误报率怎么变？
5. 把标签表里的 `tissue_type`（模块 4）也合并进来：在第 4 步代码第 1 段的 `join` 后面加一行 `adata.obs = adata.obs.join(meta[["tissue_type"]], rsuffix="_geo")`（h5ad 自己也有一列 `tissue_type`，但值全是 "tissue"），再用 `tissue_type_geo` 按活检、肾切除、死亡供体分别报误报率。这一行我们跑过，其余结果不变。
6. **自己造 doublet**（课题 1 的最小版本）：在第 4 步代码第 2 段 `normalize_total` 之前，从测试供体的 reference PT 核里随机取 500 对，把两行**原始计数相加**，当作 500 个新细胞加进去，标成"伪影"（Scrublet 就是这样造 doublet 的）。用同样的流程打分：它们有多少超过阈值？再换成"PT + TAL"两种细胞相加，结果有什么不同？想一想为什么同一类细胞组成的 doublet 很难被发现。
<!-- EN -->
None of these has a fixed answer; run them before drawing conclusions.

1. Replace the by-person split (part 3 of the step 4 code) with a **random split by cell** and compute the false-alarm rate again. How does it differ from the by-person split, and why?
2. Replace `"PT"` with `"TAL"`. Do the conclusions still hold?
3. Replace "gene count" with `percent.mt`, or combine the two. Can it match kNN on degenerative cells?
4. Change `n_neighbors` from 10 to 1 or 50. How do AUROC and the false-alarm rate change?
5. Also join `tissue_type` from the label table (module 4): after the `join` in part 1 of the step 4 code, add `adata.obs = adata.obs.join(meta[["tissue_type"]], rsuffix="_geo")` (the h5ad has its own `tissue_type` column, but every value is "tissue"), then report the false-alarm rate separately for biopsy, nephrectomy and deceased donor using `tissue_type_geo`. We ran this line; the other results do not change.
6. **Make your own doublets** (a minimal version of Topic 1): before `normalize_total` in part 2 of the step 4 code, take 500 random pairs of reference PT nuclei from the test donors, **add the two rows' raw counts**, append them as 500 new cells and label them "artifact" (this is how Scrublet simulates doublets). Score them with the same pipeline: how many exceed the threshold? Then add PT + TAL pairs instead. What changes? Think about why doublets of two cells of the same type are hard to detect.

## 第 7 步 · 收尾 / Step 7 · Clean up

<!-- ZH -->
做完可以删掉 h5ad（1.6 GB）。需要时按第 3 步重新下载即可。
<!-- EN -->
When done you can delete the h5ad (1.6 GB) and download it again with step 3 when needed.

## 自测 / Self-check

<!-- ZH -->
??? question "1. 为什么基因选择、标准化和 PCA 只在参考上拟合？"
    测试数据参与拟合，就相当于提前看到了测试集，结果会偏乐观。和机器学习里只在训练集上拟合 scaler 是同一回事。

??? question "2. 为什么阈值要在另一批供体上定，而不是直接在参考上定？"
    参考细胞是 kNN 的"训练集"，它们离自己的邻居天然更近，在它们身上定的阈值会偏低，换到新人身上误报就会偏高。

??? question "3. adaptive – epi 上「只数基因」的 AUROC 是 0.30，低于 0.5，说明什么？"
    adaptive 细胞的基因比 reference 更多，"基因越少越异常"的方向在它身上正好反了。反过来用这个分数也能到 0.70 左右，但那同样只是在学 QC 指标。
<!-- EN -->
??? question "1. Why are gene selection, scaling and PCA fitted on the reference only?"
    Fitting on test data means peeking at the test set, which makes results look better than they are. It is the same as fitting a scaler on the training set only in machine learning.

??? question "2. Why set the threshold on separate donors instead of on the reference itself?"
    Reference cells are the kNN's "training set" and sit naturally close to their own neighbours. A threshold set on them is too low, so false alarms rise on new people.

??? question "3. The gene-count AUROC on adaptive – epi is 0.30, below 0.5. What does that say?"
    Adaptive cells have more genes than reference cells, so "fewer genes = more anomalous" points the wrong way for them. Flipping the score gives about 0.70, but that too is only learning a QC metric.
