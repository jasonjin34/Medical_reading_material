# Zero-shot evaluation reveals limitations of single-cell foundation models

> **Bibkey** `Kedzierska_2025` · **Venue** Genome Biology (2025) · **Category** foundation · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1186/s13059-025-03574-x>
> `status: complete` — 基于 Europe PMC 开放全文(PMC12007350)精读(Short report)。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> 不做任何微调、直接用 scGPT 与 Geneformer 的细胞嵌入做细胞类型聚类与批次整合,它们在五个数据集上普遍不如「选 HVG」、Harmony 与 scVI;连预训练任务本身(掩码表达重建)也做得勉强 —— scGPT 不加细胞嵌入时甚至不如「预测均值」。
<!-- EN --> Using scGPT and Geneformer cell embeddings zero-shot — no fine-tuning — for cell-type clustering and batch integration, both generally underperform simply selecting HVGs, Harmony and scVI across five datasets; they even struggle at their own pretraining task (masked expression reconstruction) — scGPT without cell embeddings does worse than predicting the mean.

## 研究问题 / Problem
<!-- ZH --> 单细胞基础模型多以微调后的表现来证明价值,但很多单细胞任务是探索性的、没有预定义标签,只能零样本使用嵌入。蛋白语言模型的经验表明,微调带来的提升可能来自与预训练无关的「平凡机制」。因此需要问:预训练到底学到了可迁移的生物学吗?
<!-- EN --> Single-cell foundation models mostly prove their value through fine-tuned performance, yet many single-cell tasks are exploratory with no predefined labels, so embeddings must be used zero-shot. Protein-LM experience shows fine-tuning gains can stem from trivial mechanisms unrelated to pretraining. So: does pretraining actually learn transferable biology?

## 方法 / Method
<!-- ZH --> 评估 Geneformer 与 scGPT(scGPT 有四个变体:随机初始化、kidney 814k 细胞、blood 10.3M、human 33M)。基线:HVG、Harmony、scVI。**任务**:(1) 细胞类型聚类 —— AvgBIO 分数、ASW;(2) 批次整合 —— scib 的 batch 分数、PCR 等,在全维与降维下分别计算;(3) 预训练任务重建 —— scGPT 的 bin 值预测(GEP,以及以细胞嵌入为条件的 GEPC),Geneformer 的基因排序预测,对比「均值 / 平均排序」朴素基线。核查评测数据与预训练数据的重叠。代码与 Docker 镜像公开。
<!-- EN --> Evaluates Geneformer and scGPT (four scGPT variants: random init, kidney 814k cells, blood 10.3M, human 33M). Baselines: HVG, Harmony, scVI. **Tasks**: (1) cell-type clustering — AvgBIO, ASW; (2) batch integration — scib batch scores, PCR etc., in full and reduced dimensions; (3) pretraining-task reconstruction — scGPT bin-value prediction (GEP, and GEPC conditioned on the cell embedding), Geneformer gene-rank prediction, vs naive mean / average-rank baselines. Overlap between evaluation and pretraining data is checked. Code and Docker image public.

## 数据 / Data
<!-- ZH --> 五个数据集:Pancreas(16k,五个来源,与 Geneformer 预训练部分重叠)、两个 PBMC 数据集(含 PBMC 12k)、跨组织免疫细胞图谱 Immune(330k)、多器官的 Tabula Sapiens;后两者在 scGPT 预训练集中出现过。作者认为这已是对模型「最有利」的设置(组织与技术都接近预训练分布)。
<!-- EN --> Five datasets: Pancreas (16k, five sources, partially overlapping Geneformer pretraining), two PBMC datasets (incl. PBMC 12k), a cross-tissue Immune atlas (330k) and the multi-organ Tabula Sapiens — the last two were in scGPT's pretraining set. The authors regard this as the most favourable setting (tissues and technologies close to pretraining).

## 主要结果 / Key results
- <!-- ZH --> **细胞类型聚类**:按 AvgBIO,Geneformer 与 scGPT 都不如 HVG、Harmony、scVI;scGPT 仅在 PBMC 12k 上胜出;**HVG 在所有指标上都优于两者**。在预训练见过的数据上也没有稳定优势。 <!-- EN --> **Cell-type clustering**: by AvgBIO, Geneformer and scGPT both trail HVG, Harmony and scVI; scGPT wins only on PBMC 12k; **HVG beats both on every metric**. No consistent advantage even on datasets seen in pretraining.
- <!-- ZH --> **预训练数据规模**:预训练相对随机初始化有一定提升(尤其 PBMC),但 scGPT human(33M)反而略逊于 scGPT blood(10.3M),即使在非血液组织上也是如此 —— 更大更多样的数据不一定更好。 <!-- EN --> **Pretraining scale**: pretraining helps over random init (notably PBMC), but scGPT human (33M) slightly underperforms scGPT blood (10.3M), even on non-blood tissues — bigger, more diverse data does not necessarily help.
- <!-- ZH --> **批次整合**:Geneformer 几乎在所有数据集和指标上排最后,其嵌入中批次解释的方差甚至高于原始数据;scGPT 在仅有技术批次的 Pancreas/PBMC 上不如 scVI、Harmony,在含供体差异的 Tabula Sapiens/Immune 上胜出(但二者在预训练中出现过)。全维排名下 HVG 最好。 <!-- EN --> **Batch integration**: Geneformer ranks last on almost every dataset and metric, with more variance explained by batch in its embeddings than in the raw data; scGPT trails scVI/Harmony on technical-batch-only Pancreas/PBMC and wins on Tabula Sapiens/Immune with donor-level variation (both seen in pretraining). HVG ranks best in full dimensions.
- <!-- ZH --> **预训练任务**:scGPT 不加细胞嵌入时只会预测输入 bin 的均值,MSE 不如朴素均值基线,加细胞嵌入后也只是略好;Geneformer 预测排序与真实排序的中位相关 0.56(最好 0.95),并会预测输入中不存在的基因。 <!-- EN --> **Pretraining task**: without cell embeddings scGPT predicts the mean input bin, with MSE worse than a naive mean baseline and only marginally better with embeddings; Geneformer's predicted vs true ranking has median correlation 0.56 (best 0.95), and it sometimes predicts genes absent from the input.

## 创新点 / Contributions
- <!-- ZH --> 把「零样本评测」确立为单细胞基础模型的必要检验,并展示其能暴露微调掩盖的问题。 <!-- EN --> Establishes zero-shot evaluation as a necessary test for single-cell foundation models and shows it exposes problems fine-tuning hides.
- <!-- ZH --> 回到预训练目标本身做诊断,质疑 MLM 是否适合学习细胞嵌入。 <!-- EN --> Diagnoses the pretraining objective itself, questioning MLM's suitability for learning cell embeddings.
- <!-- ZH --> 呼吁建立永不用于预训练的保留评测集(类似 LLM 的做法)。 <!-- EN --> Calls for held-out evaluation sets never used for pretraining (as with LLMs).

## 局限 / Limitations
- <!-- ZH --> 只评估两个模型、五个转录组数据集,未覆盖更新模型(如以蛋白知识增强基因表示的模型)。 <!-- EN --> Only two models and five transcriptomic datasets; newer models (e.g. protein-informed gene representations) not covered.
- <!-- ZH --> 部分评测数据出现在预训练中,难以区分泛化与记忆。 <!-- EN --> Some evaluation data appear in pretraining, confounding generalisation vs memorisation.
- <!-- ZH --> scGPT 不同变体的数据规模与组织组成相互混淆。 <!-- EN --> scGPT variants confound data size with tissue composition.
- <!-- ZH --> 不涉及扰动预测、基因调控等下游任务。 <!-- EN --> Does not cover perturbation prediction, gene regulation or other downstream tasks.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 对 Plan A,异常检测本质上是零样本问题 —— 我们没有异常的标签,只能依赖「健康参考」的嵌入空间去度量偏离。这篇直接说明:**拿现成单细胞基础模型的嵌入当作肾组学的「正常流形」是有风险的**,HVG + scVI/Harmony 往往更好,而且 Geneformer 的嵌入批次方差甚至比原始数据更高 —— 在 95 例活检多中心、多协议的场景里,这意味着基础模型嵌入里的「离群」很可能是批次而不是疾病。实践建议:KidneyAnomalyBench 必须把 HVG-PCA、scVI 作为异常打分的强基线,并像本文一样报告批次分数(batch 是否驱动异常分数)。值得注意的是 scGPT 有一个**仅用 814k 肾细胞预训练的 kidney 变体**,可作为肾特异基础模型的直接对照(另见 Nephrobase Cell+)。对 Plan B,「基础模型嵌入优于传统方法」是 agent 常见的未经验证 claim;本文提供了 verifier 可执行的检验协议(零样本 + HVG 基线 + 预训练重叠检查),并且「评测数据混入预训练」是一条值得写入失败分类的数据泄漏模式。
<!-- EN --> For Plan A, anomaly detection is inherently zero-shot — we have no anomaly labels and must measure deviation in an embedding space defined by healthy references. This paper says directly that **using off-the-shelf single-cell foundation-model embeddings as the "normal manifold" for kidney omics is risky**: HVG + scVI/Harmony are often better, and Geneformer embeddings carry even more batch variance than raw data — in our multicentre, multi-protocol 95-biopsy setting, "outliers" in foundation-model embeddings may well be batch, not disease. Practical rule: KidneyAnomalyBench must include HVG-PCA and scVI as strong anomaly-scoring baselines and, like this paper, report batch scores (does batch drive the anomaly score?). Notably scGPT has a **kidney variant pretrained on only 814k kidney cells**, a direct comparator for kidney-specific foundation models (see also Nephrobase Cell+). For Plan B, "foundation-model embeddings beat traditional methods" is a common unverified agent claim; the paper gives the verifier an executable protocol (zero-shot + HVG baseline + pretraining-overlap check), and "evaluation data leaked into pretraining" is a data-leakage pattern worth adding to the failure taxonomy.

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码**(MIT): <!-- EN --> **Code** (MIT):
<!-- ZH/EN --> <https://github.com/microsoft/zero-shot-scfoundation>
- <!-- ZH --> **Docker 环境**:DockerHub `kzkedzierska/sc_foundation_evals`。 <!-- EN --> **Docker environment**: DockerHub `kzkedzierska/sc_foundation_evals`.
- <!-- ZH --> **评测协议**:scib v1.0.4 指标(AvgBIO、ASW、batch、PCR),全维/降维两种计算;预训练任务重建对比均值基线。 <!-- EN --> **Protocol**: scib v1.0.4 metrics (AvgBIO, ASW, batch, PCR) in full and reduced dimensions; pretraining-task reconstruction vs mean baseline.

## 待读 / Follow-ups
- <!-- ZH --> 扰动预测的线性基线对照(`linear-baselines-natmethods-2025`)。 <!-- EN --> Linear-baseline comparison for perturbation prediction (`linear-baselines-natmethods-2025`).
- <!-- ZH --> 肾特异基础模型 Nephrobase Cell+(`nephrobase-biorxiv-2025`)是否做了零样本 + HVG/scVI 对照。 <!-- EN --> Whether the kidney-specific Nephrobase Cell+ (`nephrobase-biorxiv-2025`) runs zero-shot + HVG/scVI comparisons.
- <!-- ZH --> UCE、scFoundation 等更新模型的零样本评测。 <!-- EN --> Zero-shot evaluation of newer models such as UCE and scFoundation.

## 引用 / Cite
```bibtex
@article{Kedzierska_2025, title={Zero-shot evaluation reveals limitations of single-cell foundation models}, volume={26}, ISSN={1474-760X}, url={http://dx.doi.org/10.1186/s13059-025-03574-x}, DOI={10.1186/s13059-025-03574-x}, number={1}, journal={Genome Biology}, publisher={Springer Science and Business Media LLC}, author={Kedzierska, Kasia Z. and Crawford, Lorin and Amini, Ava P. and Lu, Alex X.}, year={2025}, month=Apr }
```
