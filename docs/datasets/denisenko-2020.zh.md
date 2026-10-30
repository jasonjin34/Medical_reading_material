# Denisenko 2020 · 小鼠肾解离与保存

> 小鼠肾用 37 °C 和冰上冷解离、新鲜 / 冻存 / 甲醇固定、三种单核方法对比。人肾没有这样的对照实验。

**物种** 小鼠 · **测法** 单细胞 RNA · 单核 RNA · **获取** 公开

## 一眼看完

| | |
|---|---|
| 规模 | 77,656 细胞 + 98,303 核 |
| 人 / 样本 | 每组 3 只小鼠 |
| 标签 | 每个样本的解离 / 保存方式 |
| 许可 | CC BY 4.0 |
| 论文 | Denisenko E et al. Genome Biol 2020;21:130. doi:10.1186/s13059-020-02048-6 · [精读](../papers/denisenko-dissociation-bias-genomebiol-2020/index.md) |

![Denisenko 2020 · 小鼠肾解离与保存](img/denisenko2020_fig1.jpg)

*原图: Denisenko 2020 Fig. 1。A：37 °C 解离，B：冰上冷解离，各自再分新鲜 / 甲醇固定 / 冻存做单细胞，并做 bulk；C–E：三种提取细胞核的方法；F：整块组织 bulk 当参照。Genome Biol 2020，CC BY 4.0。*

## 测了什么

单细胞和单核 RNA（10x）。

## 人和样本

健康小鼠，每组 3 只。

## 标签

17 个应激基因（Fos、Jun、Atf3、Egr1、热休克蛋白等）；14 种细胞里 8 种只在 37 °C 解离时应激升高。37 °C 解离后足细胞只剩 0.03%（冷解离 2.78%）；冻存后近端小管从约 63% 掉到 < 1%。

## 已知问题

- 小鼠基因要换成人的同源基因；批次和品系、性别、试剂版本混在一起；处理方式只标到样本。

## 下载

| 格式 | 文件 | 大小 | 链接 |
|---|---|---|---|
| `TXT` | GEO GSE141115：54 个文库各一个“基因 × 细胞”计数表（QC 后） | 250 MB | [↗](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE141115) |
| `FASTQ` | SRA SRP233496（336 个 run） | ≈ 400 GB (SRA) | — |

细胞类型标签在论文附件 Additional file 3。

## 怎么准备

*2026-10-26 实测，只用 Python（anndata、scanpy、h5py、scipy、pandas、rdata），不需要 R。数据不要放进这个仓库。*

1. 计数是每个样本一个文本文件，基因 × 细胞（例如 BG30：13,347 基因 × 897 细胞）；细胞 ID 里带着样本和处理组（`BG30_BG20C_CRYO_<barcode>`）。
2. 每个样本的处理组（冷 / 热解离；新鲜 / 冻存 / 甲醇；测序方案）在 series matrix 里的 `workflow` 和 `sequencing protocol` 两项。

```python
import pandas as pd
bg30 = pd.read_csv("GSM4195108_BG30.txt.gz", sep="\t", index_col=0)  # genes x cells
```

## 在我们的研究课题里

- **[用伪影注入增强肾脏单细胞异常检测](../research/anomaly-benchmark.md)**: 说明“解离应激会被当成损伤”有实验证据，和 Lake 2023 degenerative 的 FOS / JUN 特征是同一类基因。以后再用，或做校准。
