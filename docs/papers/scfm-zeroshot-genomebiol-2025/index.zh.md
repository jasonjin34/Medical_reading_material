# Zero-shot evaluation reveals limitations of single-cell foundation models

> **文献键** `Kedzierska_2025` · **来源** Genome Biology(2025) · **类别** foundation · **相关度** high · **获取** open
> **链接** <https://doi.org/10.1186/s13059-025-03574-x> · `status: complete`

---

## 一句话
不做任何微调、直接用 scGPT 与 Geneformer 的细胞嵌入做细胞类型聚类与批次整合,它们在五个数据集上普遍不如「选 HVG」、Harmony 与 scVI;连预训练任务本身(掩码表达重建)也做得勉强 —— scGPT 不加细胞嵌入时甚至不如「预测均值」。

## 研究问题
单细胞基础模型多以微调后的表现来证明价值,但很多单细胞任务是探索性的、没有预定义标签,只能零样本使用嵌入。蛋白语言模型的经验表明,微调带来的提升可能来自与预训练无关的「平凡机制」。因此需要问:预训练到底学到了可迁移的生物学吗?

## 方法
评估 Geneformer 与 scGPT(scGPT 有四个变体:随机初始化、kidney 814k 细胞、blood 10.3M、human 33M)。基线:HVG、Harmony、scVI。**任务**:(1) 细胞类型聚类 —— AvgBIO 分数、ASW;(2) 批次整合 —— scib 的 batch 分数、PCR 等,在全维与降维下分别计算;(3) 预训练任务重建 —— scGPT 的 bin 值预测(GEP,以及以细胞嵌入为条件的 GEPC),Geneformer 的基因排序预测,对比「均值 / 平均排序」朴素基线。核查评测数据与预训练数据的重叠。代码与 Docker 镜像公开。

## 数据
五个数据集:Pancreas(16k,五个来源,与 Geneformer 预训练部分重叠)、两个 PBMC 数据集(含 PBMC 12k)、跨组织免疫细胞图谱 Immune(330k)、多器官的 Tabula Sapiens;后两者在 scGPT 预训练集中出现过。作者认为这已是对模型「最有利」的设置(组织与技术都接近预训练分布)。

## 主要结果
- **细胞类型聚类**:按 AvgBIO,Geneformer 与 scGPT 都不如 HVG、Harmony、scVI;scGPT 仅在 PBMC 12k 上胜出;**HVG 在所有指标上都优于两者**。在预训练见过的数据上也没有稳定优势。
- **预训练数据规模**:预训练相对随机初始化有一定提升(尤其 PBMC),但 scGPT human(33M)反而略逊于 scGPT blood(10.3M),即使在非血液组织上也是如此 —— 更大更多样的数据不一定更好。
- **批次整合**:Geneformer 几乎在所有数据集和指标上排最后,其嵌入中批次解释的方差甚至高于原始数据;scGPT 在仅有技术批次的 Pancreas/PBMC 上不如 scVI、Harmony,在含供体差异的 Tabula Sapiens/Immune 上胜出(但二者在预训练中出现过)。全维排名下 HVG 最好。
- **预训练任务**:scGPT 不加细胞嵌入时只会预测输入 bin 的均值,MSE 不如朴素均值基线,加细胞嵌入后也只是略好;Geneformer 预测排序与真实排序的中位相关 0.56(最好 0.95),并会预测输入中不存在的基因。

## 创新点
- 把「零样本评测」确立为单细胞基础模型的必要检验,并展示其能暴露微调掩盖的问题。
- 回到预训练目标本身做诊断,质疑 MLM 是否适合学习细胞嵌入。
- 呼吁建立永不用于预训练的保留评测集(类似 LLM 的做法)。

## 局限
- 只评估两个模型、五个转录组数据集,未覆盖更新模型(如以蛋白知识增强基因表示的模型)。
- 部分评测数据出现在预训练中,难以区分泛化与记忆。
- scGPT 不同变体的数据规模与组织组成相互混淆。
- 不涉及扰动预测、基因调控等下游任务。

## 与本研究方向的关系
对伪影注入课题,异常检测本质上是零样本问题 —— 我们没有异常的标签,只能依赖「健康参考」的嵌入空间去度量偏离。这篇直接说明:**拿现成单细胞基础模型的嵌入当作肾组学的「正常流形」是有风险的**,HVG + scVI/Harmony 往往更好,而且 Geneformer 的嵌入批次方差甚至比原始数据更高 —— 在多中心、多协议的肾活检场景里,这意味着基础模型嵌入里的「离群」很可能是批次而不是疾病。实践建议:KidneyAnomalyBench 必须把 HVG-PCA、scVI 作为异常打分的强基线,并像本文一样报告批次分数(batch 是否驱动异常分数)。值得注意的是 scGPT 有一个**仅用 814k 肾细胞预训练的 kidney 变体**,可作为肾特异基础模型的直接对照(另见 Nephrobase Cell+)。对 Agent 可信度课题,「基础模型嵌入优于传统方法」是 agent 常见的未经验证 claim;本文提供了 verifier 可执行的检验协议(零样本 + HVG 基线 + 预训练重叠检查),并且「评测数据混入预训练」是一条值得写入失败分类的数据泄漏模式。

## 可复用资产
- **代码**(MIT):
<https://github.com/microsoft/zero-shot-scfoundation>
- **Docker 环境**:DockerHub `kzkedzierska/sc_foundation_evals`。
- **评测协议**:scib v1.0.4 指标(AvgBIO、ASW、batch、PCR),全维/降维两种计算;预训练任务重建对比均值基线。

## 待读
- 扰动预测的线性基线对照(`linear-baselines-natmethods-2025`)。
- 肾特异基础模型 Nephrobase Cell+(`nephrobase-biorxiv-2025`)是否做了零样本 + HVG/scVI 对照。
- UCE、scFoundation 等更新模型的零样本评测。

## 引用
```bibtex
@article{Kedzierska_2025, title={Zero-shot evaluation reveals limitations of single-cell foundation models}, volume={26}, ISSN={1474-760X}, url={http://dx.doi.org/10.1186/s13059-025-03574-x}, DOI={10.1186/s13059-025-03574-x}, number={1}, journal={Genome Biology}, publisher={Springer Science and Business Media LLC}, author={Kedzierska, Kasia Z. and Crawford, Lorin and Amini, Ava P. and Lu, Alex X.}, year={2025}, month=Apr }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
