# Abedini 2024 · 第二队列

> 换一个实验室、换一批人，检验方法在健康人身上的误报率能不能控住。

**物种** 人 · **测法** 单细胞 RNA · 单核 RNA · ATAC · 空间 · **获取** 公开

## 一眼看完

| | |
|---|---|
| 规模 | 338,565 细胞 / 核 |
| 人 / 样本 | 36 份对照 + 45 份 CKD（20 糖尿病肾病、25 高血压肾病） |
| 标签 | 细胞类型；每个样本的疾病组 |
| 许可 | not stated |
| 论文 | Abedini A et al. Nat Genet 2024. doi:10.1038/s41588-024-01802-x · [精读](../papers/abedini-kidney-atlas-natgenet-2024/index.md) |

## 测了什么

单细胞 RNA、单核 RNA、snATAC（分开测，不是同核），还有 Visium 和 CosMx。

## 人和样本

肿瘤肾切除的未受累组织。对照：eGFR > 60 且纤维化 < 10%。按人数：单细胞对照 14 人、单核对照 7 人；单细胞和单核只有 8 人重叠。

## 标签

细胞类型和每个样本的疾病组；没有逐个细胞的改变态标签。

## 已知问题

- 已经用 SoupX 去过 ambient、用 DoubletFinder 去过 doublet，伪影被提前洗掉了一部分；计数是 SoupX 校正后的（非整数）。
- 对照组的数据质量反而更差（单细胞每细胞基因数中位约 358，疾病组约 598）；部分对照有高血压。
- 单细胞是 37 °C 酶解，会有解离应激。没有原始数据（原文：“due to privacy concerns”）。

## 下载

| 格式 | 文件 | 大小 | 链接 |
|---|---|---|---|
| `H5AD` | GEO GSE211785：sc + sn + ATAC 合并，scVI 前 / 后 | 4.7 / 5.5 GB | [↗](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE211785) |
| `H5AD` | 同上，加上 KPMP 数据的版本 | 9.0 GB | [↗](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE211785) |
| `RDS` | 计数矩阵（sc + sn + ATAC） | 1.7 GB | [↗](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE211785) |
| `TXT` | 每个细胞的标签表 + UMAP | 15 MB | [↗](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE211785) |

论文不是 CC 授权，这里不放原图。发布派生标签前要先确认数据许可。

## 怎么准备

*2026-10-26 实测，只用 Python（anndata、scanpy、h5py、scipy、pandas、rdata），不需要 R。数据不要放进这个仓库。*

1. 每个细胞的标签**只在 h5ad 里**（压缩 5.0 GB，**解压后 18 GB**）；那个小的 `EXPORT_..._umap.txt.gz` 只有细胞 ID 和 UMAP。用 backed 模式打开 h5ad。
2. 338,565 细胞 × 34,733 基因。`X` 是归一化后的值，整数计数在 `layers["counts"]`。`tech` = SC_RNA / SN_RNA / SN_ATAC；`group` = Control / DKD / HKD；`sample` = 44 人。
3. obs 里的数值列存成了文本，用之前要先转类型。`nCount_RNA` 不是整数（做过 SoupX 校正）；`layers["counts"]` 是校正前还是后，还没确认。
4. 对照组人数：单细胞 14、单核 7、ATAC 7。

```python
import anndata as ad
a = ad.read_h5ad("GSE211785_Susztak_SC_SN_ATAC_merged_PreSCVI_final.h5ad", backed="r")
rna = a[a.obs["tech"].astype(str) != "SN_ATAC"].to_memory()
rna.X = rna.layers["counts"]
```

## 在我们的研究课题里

- **[肾脏单细胞组学异常检测基准](../research/anomaly-benchmark.md)**: 任务 T4：健康人身上报出的“异常”都算误报，看实际误报率是否低于设定值。
