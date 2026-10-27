# Deep-learning-based gene perturbation effect prediction does not yet outperform simple linear baselines

> **Bibkey** `Ahlmann_Eltze_2025` · **Venue** Nature Methods (2025) · **Category** foundation · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1038/s41592-025-02772-6>
> `status: complete` — 基于 Europe PMC 开放全文(PMC12328236)精读(Brief Communication)。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> 在双扰动与未见单扰动的转录组效应预测上,scGPT、scFoundation、GEARS、CPA 以及接线性解码器的 scBERT / Geneformer / UCE,没有一个稳定超过「加性」「不变」「均值」或一个简单的双线性模型;唯一稳定最好的是在**另一细胞系的扰动数据**上预训练扰动嵌入的线性模型。
<!-- EN --> For predicting transcriptomic effects of double perturbations and of unseen single perturbations, none of scGPT, scFoundation, GEARS, CPA, or scBERT / Geneformer / UCE with a linear decoder consistently beats "additive", "no change", "mean" or a simple bilinear model; the only consistent winner is a linear model whose perturbation embedding is pretrained on **perturbation data from another cell line**.

## 研究问题 / Problem
<!-- ZH --> scGPT 与 scFoundation 等单细胞基础模型宣称能预测基因扰动引起的表达变化(包括未做过的扰动),这是「虚拟细胞」叙事的核心卖点。但它们原文中的对照可能过于「容易」(例如 CPA 本不为未见扰动设计;scGPT 基准中的线性模型对未见扰动退化为「不变」)。问题是:在公平设置下,它们是否真的比刻意简单的基线更好?
<!-- EN --> Single-cell foundation models such as scGPT and scFoundation claim to predict expression changes caused by genetic perturbations, including unseen ones — the core selling point of the "virtual cell" narrative. But their original comparisons may have been "easy" (CPA was never designed for unseen perturbations; the linear model in scGPT's benchmark effectively reverted to "no change"). Under a fair setup, do they actually beat deliberately simple baselines?

## 方法 / Method
<!-- ZH --> **任务 1:双扰动**。Norman et al. K562 CRISPRa 数据(100 个单基因、124 对基因,19,264 个基因的 log 表达);用全部单扰动 + 62 个双扰动微调,在其余 62 个双扰动上测试,5 次随机划分。基线:「no change」(预测对照)与「additive」(单扰动 LFC 之和,不使用任何双扰动数据)。误差 = 前 1,000 高表达基因的 L2 距离;另看 Pearson delta 等。**遗传互作**:在 null(正态)下偏离加性期望显著者定义为互作(FDR 5% 共 5,035 个/约 124,000),分为 buffering、synergistic、opposite;对模型 310,000 个预测按阈值 D 计算 TPR–FDP 曲线。**任务 2:未见单扰动**。Replogle K562、Replogle RPE1(CRISPRi)与 Adamson K562。基线:训练集扰动均值 b;以及双线性模型 Y ≈ G W Pᵀ + b(G 为基因嵌入、P 为扰动嵌入,可来自训练数据的降维,或外部来源 —— scGPT/scFoundation 的基因嵌入、GEARS 的扰动嵌入、或另一细胞系 Replogle 数据的扰动嵌入)。各模型尽量用默认参数,微调限时 3 天(scFoundation 训练 5 个 epoch)。
<!-- EN --> **Task 1: double perturbations.** Norman et al. K562 CRISPRa (100 single genes, 124 pairs; log expression for 19,264 genes); fine-tune on all singles + 62 doubles, test on the other 62 doubles, five random splits. Baselines: "no change" (predict control) and "additive" (sum of single-perturbation LFCs, using no double data). Error = L2 distance over the top 1,000 expressed genes; also Pearson delta etc. **Genetic interactions**: doubles deviating from the additive expectation beyond a Normal null (5,035 at 5% FDR out of ~124,000), classed as buffering, synergistic or opposite; TPR–FDP curves over thresholds D on each model's 310,000 predictions. **Task 2: unseen single perturbations.** Replogle K562, Replogle RPE1 (CRISPRi) and Adamson K562. Baselines: training-set mean b, and a bilinear model Y ≈ G W Pᵀ + b (G gene embedding, P perturbation embedding — from dimensionality reduction of training data or external sources: scGPT/scFoundation gene embeddings, GEARS perturbation embedding, or a perturbation embedding from the other cell line's Replogle data). Default parameters where possible; fine-tuning capped at 3 days (scFoundation trained for five epochs).

## 数据 / Data
<!-- ZH --> Norman et al.(K562 CRISPRa,双扰动)、Replogle et al.(K562 与 RPE1 CRISPRi)、Adamson et al.(K562 CRISPRi)—— 即 GEARS / scGPT / scFoundation 原文使用的数据;全部是癌细胞系。
<!-- EN --> Norman et al. (K562 CRISPRa, doubles), Replogle et al. (K562 and RPE1 CRISPRi), Adamson et al. (K562 CRISPRi) — the datasets used in the GEARS / scGPT / scFoundation papers; all cancer cell lines.

## 主要结果 / Key results
- <!-- ZH --> **双扰动**:所有深度模型的预测误差都**显著高于 additive 基线**;换 Pearson delta、不同基因子集结论不变。 <!-- EN --> **Doubles**: every deep model has prediction error **substantially higher than the additive baseline**; same conclusion under Pearson delta and other gene subsets.
- <!-- ZH --> **遗传互作**:没有任何模型优于「no change」基线;模型几乎只预测 buffering,很少预测 synergistic,而预测对的更少。HBG2/HBZ 这对强单效应基因,除 Geneformer、scFoundation 外的模型都预测 LFC ≈ 0。scGPT、UCE、scBERT 对多数基因的预测几乎不随扰动变化;GEARS、scFoundation 的变化幅度也远小于真实值。 <!-- EN --> **Genetic interactions**: no model beats "no change"; models predict mostly buffering, rarely synergy, and correct synergy even more rarely. For HBG2/HBZ — strong individual effects — all models except Geneformer and scFoundation predict LFC ≈ 0. scGPT, UCE and scBERT predictions barely vary across perturbations for most genes; GEARS and scFoundation vary far less than ground truth.
- <!-- ZH --> **未见单扰动**:没有深度模型稳定超过均值基线或线性模型(scFoundation 因基因集必须完全匹配其预训练而无法在 Adamson/Replogle 上运行;CPA 不适用)。把 scGPT/scFoundation 的基因嵌入或 GEARS 的扰动嵌入放进线性模型,表现与原模型自带解码器相当或更好,但并不稳定优于用训练数据自身得到 G、P 的线性模型。 <!-- EN --> **Unseen singles**: no deep model consistently beats the mean baseline or the linear model (scFoundation could not run on Adamson/Replogle because its gene set must match pretraining exactly; CPA not applicable). Plugging scGPT/scFoundation gene embeddings or GEARS perturbation embeddings into the linear model matches or beats their own decoders, but does not consistently beat the linear model with G, P from the training data.
- <!-- ZH --> **唯一稳定赢家**:用另一细胞系(K562↔RPE1)Replogle 数据预训练 P 的线性模型;且两细胞系间越相似的基因预测越准 —— 说明在**扰动数据**上预训练有用,而在单细胞图谱上预训练只比随机嵌入略好。深度模型的微调计算开销远高于这些基线。 <!-- EN --> **The only consistent winner**: a linear model with P pretrained on the other cell line's Replogle data (K562↔RPE1), more accurate for genes more similar between the lines — pretraining on **perturbation data** helps, while pretraining on single-cell atlases gives only a small benefit over random embeddings. Deep models cost far more compute to fine-tune.

## 创新点 / Contributions
- <!-- ZH --> 在原作者自己的数据上,用刻意简单的基线做公平对照,揭示扰动预测的进展被高估。 <!-- EN --> A fair comparison against deliberately simple baselines, on the original authors' own datasets, showing progress in perturbation prediction has been overstated.
- <!-- ZH --> 双线性 G W Pᵀ 框架可插拔任意基因/扰动嵌入,用来单独检验「预训练表示」本身是否有用。 <!-- EN --> The bilinear G W Pᵀ framework accepts any gene/perturbation embedding, isolating whether the pretrained representation itself is useful.
- <!-- ZH --> 遗传互作的操作化定义与 buffering / synergistic / opposite 分类,成为后续基准的常用口径。 <!-- EN --> An operational definition of genetic interaction with buffering / synergistic / opposite classes, now a common benchmark lens.

## 局限 / Limitations
- <!-- ZH --> 只有 4 个数据集,全部是癌细胞系(K562、RPE1);没有组织或原代细胞。 <!-- EN --> Only four datasets, all cancer cell lines (K562, RPE1); no tissue or primary cells.
- <!-- ZH --> 未改进原始 QC(例如没有剔除未能下调靶基因、可能无效的扰动)。 <!-- EN --> Original QC not improved (e.g. perturbations that failed to change their own target were not removed).
- <!-- ZH --> 微调限时 3 天、尽量默认参数 —— 更充分调参可能缩小差距(作者未声称深度模型永远不行)。 <!-- EN --> 3-day fine-tuning cap and default parameters — more tuning might narrow the gap (the authors do not claim deep models can never work).
- <!-- ZH --> 评测聚焦 pseudobulk 平均表达,未评估单细胞层面的分布变化。 <!-- EN --> Evaluation focuses on pseudobulk mean expression, not single-cell distributional shifts.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 这是 **revert** 阶段最重要的「冷水」:我们设想在虚拟组织里预测「哪些基因扰动能把异常拉回正常」,而本文表明,即使在最干净的细胞系 Perturb-seq 上,基础模型连加性/均值基线都打不过。直接的工程启示:**(1) 任何回逆(reversion)预测都必须报告 additive / no-change / mean / 线性基线**,否则无法区分模型贡献;**(2) 若要预训练,应优先用扰动数据(如 Replogle、Virtual Cell Challenge 数据)而非单纯图谱**;**(3) 「回逆」本质是预测反向的 LFC,而模型系统性低估效应幅度(预测几乎不随扰动变化),这会让「哪个扰动最能回逆」的排序退化为噪声** —— 评测时要看效应幅度与排序,不能只看相关。对课题 1,它提醒异常检测的下游价值不能靠「接一个基础模型做回逆」来自证。对课题 2,这是 agent 最常见的不可信 claim 之一(「scGPT 预测敲除 X 可逆转表型」),本文给出了可执行的校验方式:让 verifier 自动对照线性/加性基线,这可以成为组学特异失败分类中的一条「缺失基线」类别。
<!-- EN --> This is the key "cold water" for the **revert** stage: we envision predicting, inside a virtual tissue, which gene perturbations would pull an anomaly back to normal — and this paper shows that even on the cleanest cell-line Perturb-seq, foundation models fail to beat additive/mean baselines. Concrete implications: **(1) any reversion prediction must report additive / no-change / mean / linear baselines**, or model contribution is unidentifiable; **(2) if pretraining, prefer perturbation data (e.g. Replogle, Virtual Cell Challenge data) over atlases alone**; **(3) reversion is essentially predicting the reverse LFC, and models systematically underestimate effect magnitude (predictions barely vary across perturbations), which would reduce a "which perturbation best reverts" ranking to noise** — evaluate magnitude and ranking, not just correlation. For Topic 1, it warns that the downstream value of anomaly detection cannot be self-certified by "bolting on a foundation model for reversion." For Topic 2, it addresses one of the most common untrustworthy agent claims ("scGPT predicts knocking out X reverses the phenotype") with an executable check: have the verifier automatically compare against linear/additive baselines — a "missing baseline" category for the omics-specific failure taxonomy.

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码与中间结果**(含各模型运行脚本、Zenodo 归档): <!-- EN --> **Code and intermediate results** (model run scripts, Zenodo archive):
<!-- ZH/EN --> <https://github.com/const-ae/linear_perturbation_prediction-Paper>
- <!-- ZH --> **基线集合**:no change、additive、mean、双线性 G W Pᵀ(可插外部嵌入)。 <!-- EN --> **Baseline suite**: no change, additive, mean, bilinear G W Pᵀ (pluggable external embeddings).
- <!-- ZH --> **数据**:Norman 2019、Replogle 2022、Adamson 2016(公开)。 <!-- EN --> **Data**: Norman 2019, Replogle 2022, Adamson 2016 (public).

## 待读 / Follow-ups
- <!-- ZH --> Kernfeld et al. 与 Csendes et al. 的「均值基线」预印本,以及后续多个扰动基准。 <!-- EN --> The Kernfeld et al. and Csendes et al. "mean baseline" preprints and the subsequent perturbation benchmarks.
- <!-- ZH --> Virtual Cell Challenge(`virtual-cell-challenge`)的评测设计是否吸收了这些基线。 <!-- EN --> Whether the Virtual Cell Challenge (`virtual-cell-challenge`) evaluation absorbs these baselines.
- <!-- ZH --> 零样本评测(`scfm-zeroshot-genomebiol-2025`)—— 同一类「基础模型不如简单方法」的证据。 <!-- EN --> Zero-shot evaluation (`scfm-zeroshot-genomebiol-2025`) — the same "foundation models vs simple methods" evidence.

## 引用 / Cite
```bibtex
@article{Ahlmann_Eltze_2025, title={Deep-learning-based gene perturbation effect prediction does not yet outperform simple linear baselines}, volume={22}, ISSN={1548-7105}, url={http://dx.doi.org/10.1038/s41592-025-02772-6}, DOI={10.1038/s41592-025-02772-6}, number={8}, journal={Nature Methods}, publisher={Springer Science and Business Media LLC}, author={Ahlmann-Eltze, Constantin and Huber, Wolfgang and Anders, Simon}, year={2025}, month=Aug, pages={1657–1661} }
```
