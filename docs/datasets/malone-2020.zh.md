# Malone 2020 · 移植肾供体 / 受者

> 移植肾活检，按供体和受者的基因型分出每个细胞来自谁。

**物种** 人 · **测法** 单细胞 RNA · 基因型 · **获取** 公开

## 一眼看完

| | |
|---|---|
| 规模 | 81,139 细胞 |
| 人 / 样本 | 5 份移植肾活检 |
| 标签 | 每个细胞来自供体还是受者（公开文件和论文对不上） |
| 许可 | not CC |
| 论文 | Malone AF et al. JASN 2020;31(9):1977–1986. doi:10.1681/ASN.2020030326 · [精读](../papers/malone-transplant-chimerism-jasn-2020/index.md) |

## 测了什么

单细胞 RNA（10x 5′）；供体和受者都做了全外显子测序。

## 人和样本

5 份移植肾活检：3 份抗体介导的排斥，2 份非排斥原因的 AKI；不是自体肾的 AKI / CKD。

## 标签

每个细胞的供体 / 受者标签。公开文件里的标签和论文对不上（巨噬细胞：文件 4,715 / 312，论文 1,229 / 3,798），原因未知。

## 已知问题

- doublet 已被手工删掉，也按 Demuxlet 的基因型判定删过（占 3–10.5%）；公开文件里没有 doublet 标签，没有空液滴；全文没提 ambient。

## 下载

| 格式 | 文件 | 大小 | 链接 |
|---|---|---|---|
| `CSV` | GEO GSE145927：7 个活检的计数表（QC 后） | 247 MB | [↗](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE145927) |
| `CSV` | 每个细胞的标签表（供体 / 受者、细胞类型、排斥） | 2.1 MB | [↗](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE145927) |
| `FASTQ` | SRA SRP250734（36 个 run，含全外显子） | ≈ 693 GB (SRA) | — |

JASN 不是 CC 授权，不放原图。要用就得从每个单细胞样本约 75–120 GB 的原始数据（SRA）重跑。

## 怎么准备

*2026-10-26 实测，只用 Python（anndata、scanpy、h5py、scipy、pandas、rdata），不需要 R。数据不要放进这个仓库。*

1. 标签表：5 份活检（`orig.ident` biopsy62/64/65/67/68）共 81,139 个细胞，`SNV_GT` 供体 75,741 / 受者 5,398。
2. 计数文件每个样本一个，基因 × 细胞，条形码写法不同：biopsy65（`day11rawcounts`）要把 `AAACCTGAGAGCTTCT.1` 改成 `AAACCTGAGAGCTTCT-1_3`，改完 5,395 个全部对上。计数文件有 7 个，但标签表里只有 5 份活检。
3. 暂时不用：公开的供体 / 受者标签和论文对不上。

```python
import pandas as pd
md = pd.read_csv("GSE145927_MGI.metadata.csv.gz", index_col=0)
c = pd.read_csv("GSM4339777_day11rawcounts.csv.gz", index_col=0)  # biopsy65, genes x cells
c.columns = c.columns.str.replace(r"\.(\d+)$", r"-\1", regex=True) + "_3"
```

## 在我们的研究课题里

- **[用伪影注入增强肾脏单细胞异常检测](../research/anomaly-benchmark.md)**: 暂不用；人肾伪影真值主要靠 Hoeft 2024。
