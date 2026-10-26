# Hoeft 2024 · 4 个病人混在一个通道

> 4 名病人的冷冻肾活检混在一个 10x 单核通道里测，按 SNP 分出每个核来自谁。这是人肾上唯一能算出真实 ambient 和 doublet 的数据。

**物种** 人 · **测法** 单核 RNA · 基因型 · **获取** 公开

## 一眼看完

| | |
|---|---|
| 规模 | 11,490 核 |
| 人 / 样本 | 4 名病人（冷冻肾活检） |
| 标签 | 按 SNP 分出的供体；250 个基因型 doublet（2.2%） |
| 许可 | CC BY 4.0 (paper) |
| 论文 | Hoeft K et al. Nat Commun 2024;15:10612. doi:10.1038/s41467-024-54270-6 · [精读](../papers/hoeft-genotype-multiplexing-natcommun-2024/index.md) |

![Hoeft 2024 · 4 个病人混在一个通道](img/hoeft2024_fig2ij.jpg)

*原图: Hoeft 2024 Fig. 2 i–j（肾部分，已截取）。i：混合肾样本的表达聚类，和三种按 SNP 分人的结果对照；j：每个簇里各病人、doublet 和未分配核的比例。注意“Low Quality”和“Mixed/Doublets”簇里大部分核其实只属于一个病人。Nat Commun 2024，CC BY 4.0。*

## 测了什么

单核 RNA（10x 3′ v3.1）；每个病人另有 bulk RNA-seq，做成了基因型文件（VCF）。

## 人和样本

4 名病人；论文没有写诊断。

## 标签

核里出现别人的等位基因 = 外来污染（ambient）；一个液滴里有两种基因型 = doublet。每个核的供体分配没有公开，要从原始数据重算。

## 已知问题

- GEO 上写“raw”的矩阵其实已经过滤，没有空液滴；论文没有量化 ambient。
- 只有 4 人，只够做验证，不能当主结果。
- 有用的发现：按表达聚出的“Mixed/Doublets”簇有 4,488 个核（39%），其中按基因型确认是 doublet 的只有 123 个（我们从 Source Data 算的）。只看表达，判断异常原因很不可靠。

## 下载

| 格式 | 文件 | 大小 | 链接 |
|---|---|---|---|
| `MTX` | GEO GSE247708：肾样本 10x 矩阵（已过滤，11,490 核） | 65 MB | [↗](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE247708) |
| `VCF` | 4 个肾病人的基因型（来自 bulk RNA-seq） | ≈ 0.4 MB each | [↗](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE247708) |
| `FASTQ` | SRA PRJNA1040187，肾样本 SRR29832267 | ≈ 50 GB | [↗](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA1040187) |

要得到 ambient / doublet 真值，得用 FASTQ + VCF 重跑 CellRanger 和 souporcell。

## 怎么准备

*2026-10-26 实测，只用 Python（anndata、scanpy、h5py、scipy、pandas、rdata），不需要 R。数据不要放进这个仓库。*

1. 只下载肾样本 GSM8397034（矩阵 + 条形码 + 基因表，68 MB），不用下 611 MB 的整包：36,601 基因 × 11,490 核，每个核中位 1,055 个 UMI。
2. 肾样本的基因型是四个小 VCF（TS116、TS120、TS121、TS126；来自 bulk RNA-seq，每个只有一千多个位点，例如 TS116 有 1,260 个）。用之前在 GEO 样本页确认它们就是这 4 个肾病人。
3. 矩阵已经过滤，每个核属于谁也没公开。所以要得到 doublet 和 ambient 真值，得从 FASTQ（SRR29832267，约 50 GB）重跑：先 CellRanger，再用 VCF 跑 souporcell 或 vireo。

```python
import scanpy as sc, pandas as pd
k = sc.read_mtx("GSM8397034_Kidney_Pooled_matrix.mtx.gz").T      # -> nuclei x genes
k.obs_names = pd.read_csv("GSM8397034_Kidney_Pooled_barcodes.tsv.gz", header=None)[0].values
k.var_names = pd.read_csv("GSM8397034_Kidney_Pooled_features.tsv.gz", header=None, sep="\t")[1].values
k.var_names_make_unique()
```

## 在我们的研究课题里

- **[肾脏单细胞组学异常检测基准](../research/anomaly-benchmark.md)**: 讨论中：人肾真实的 ambient 和 doublet 答案，用来检验我们注入的伪影像不像真的。
