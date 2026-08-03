# An ECG biomarker for sudden cardiac death discovered with deep learning

> **Bibkey** `Obermeyer_2026` · **Venue** Nature (2026) · **Category** imaging · **Relevance** high · **Access** paywall
> **Link** <https://doi.org/10.1038/s41586-026-10674-6>
> `status: complete` — 若为 abstract-only,把 PDF 放到本文件夹的 `source.pdf` 后可补全全文精读。

---

## 一句话 / One-liner
<!-- ZH --> 用深度学习从心电图(ECG)波形中“发现”了一个此前未被描述、肉眼可见且能稳健预测心脏性猝死(SCD)的新生物标志物,并结合生成模型把模型学到的异常波形形态可视化。
<!-- EN --> Deep learning discovers a previously undescribed, visually identifiable ECG biomarker that robustly predicts sudden cardiac death (SCD), and a paired generative model renders the learned waveform morphology visible.

## 研究问题 / Problem
<!-- 这篇论文要解决什么问题?为什么重要? / What problem, and why it matters. -->
<!-- ZH --> 心脏性猝死原则上可用除颤器(ICD)预防,但现有唯一广泛使用的预测指标——左心室射血分数(LVEF)——漏掉了大多数猝死者,同时又把许多低风险患者标记为需要植入除颤器(这些除颤器往往从不放电)。因此临床急需更敏感、更特异的猝死风险生物标志物。
<!-- EN --> SCD is preventable with defibrillators, yet the only widely used predictor, left ventricular ejection fraction (LVEF), misses most SCDs while flagging many low-risk patients for futile ICDs that never fire. A better, more sensitive and specific risk biomarker is urgently needed.

## 方法 / Method
<!-- 核心方法、模型、数据流。关键公式/架构。 / Core method, model, data pipeline, key architecture. -->
<!-- ZH --> 在把某瑞典地区的全部 ECG 与死亡证明相链接的数据集上训练一个深度学习模型,用于从原始 ECG 波形预测猝死风险。为解释模型,作者将该判别模型与一个 ECG 波形的生成模型配对(discriminative + generative pairing),从而合成/可视化模型据以判定高风险的波形形态,把黑箱学到的“异常形态”还原为可肉眼识别的生物标志物;再把该标志物的形状与心脏电生理第一性原理相联系,提出并初步检验关于猝死机制的新假设。具体网络结构、训练细节仅在付费正文中(仅摘要可得 / abstract-only)。
<!-- EN --> A deep-learning model is trained on raw ECG waveforms to predict SCD risk. For interpretability, the discriminative model is paired with a generative model of the ECG waveform, so the morphology the predictor relies on can be synthesized and visualized — turning a black-box signal into an eye-readable biomarker. Its shape is then tied to electrophysiological first principles to form and preliminarily test a mechanistic hypothesis. Exact architecture/training details are behind the paywall (abstract-only).

## 数据 / Data
<!-- 数据集、模态、规模、来源。 / Datasets, modalities, scale, source. -->
<!-- ZH --> 训练/发现队列:某瑞典地区所有 ECG 与死亡证明的链接数据(总体中 2.2% 被划为高风险组;LVEF 降低者占 1.9%)。外部验证两处:(1) 一个美国医疗系统,标签为导致猝死的室性心律失常;(2) 一个台湾医院登记库,标签为未来的心律失常性心脏骤停。模态为 12 导联/标准 ECG 波形(具体导联数正文可得,仅摘要可得 / abstract-only)。
<!-- EN --> Discovery cohort: all ECGs in a Swedish region linked to death certificates (high-risk group = 2.2% of sample; reduced-LVEF group = 1.9%). External validation: (1) a US health system (labels = ventricular arrhythmias causing sudden death), and (2) a Taiwanese hospital registry (labels = future arrhythmic cardiac arrests). Modality: standard ECG waveforms.

## 主要结果 / Key results
<!-- 关键指标与结论,尽量带数字。 / Headline metrics and conclusions, with numbers where possible. -->
<!-- ZH -->
- 模型划出的高风险组(占样本 2.2%)年猝死率 7.0%,高于 LVEF 降低组(占样本 1.9%)的年猝死率 4.6%。
- 该模型标记的高风险患者中 86.1% 未被 LVEF 识别 —— 与现有指标高度互补。
- 高风险且植入除颤器的患者比预期死亡概率低 54.4%,提示存在死亡率获益(观察性证据)。
- 在美国队列外部验证可预测导致猝死的室性心律失常;在台湾登记库可特异性预测未来心律失常性心脏骤停。
- 生成模型揭示出一个此前(据作者所知)未被描述、肉眼可见且稳健的波形生物标志物。
<!-- EN -->
- The model's high-risk group (2.2% of sample) has a 7.0% annual SCD rate, exceeding the reduced-LVEF group (1.9% of sample; 4.6% annual rate).
- 86.1% of the model's high-risk patients were NOT flagged by LVEF — highly complementary to the current standard.
- High-risk patients who received ICDs were 54.4% less likely to die than expected, suggesting a mortality benefit (observational).
- External validation predicts ventricular arrhythmias (US) and future arrhythmic cardiac arrests (Taiwan).
- The generative pairing reveals a previously undescribed, visually identifiable, robust waveform biomarker.

## 创新点 / Contributions
- <!-- ZH --> 用“判别模型 + 生成模型”配对,把深度学习从信号中“发现”的隐含形态还原为可肉眼识别、可临床沟通的新生物标志物(而非停留在不可解释的风险分数)。 <!-- EN --> A discriminative+generative pairing that turns a learned latent morphology into an eye-readable, clinically communicable new biomarker rather than an opaque risk score.
- <!-- ZH --> 发现的标志物与 LVEF 高度互补(86.1% 不重叠),填补现有筛查的空白。 <!-- EN --> The discovered biomarker is highly complementary to LVEF (86.1% non-overlap), filling a screening gap.
- <!-- ZH --> 跨三国(瑞典、美国、台湾)、多终点(猝死/室性心律失常/心脏骤停)外部验证,泛化性强。 <!-- EN --> Cross-country (Sweden, US, Taiwan), multi-endpoint external validation.
- <!-- ZH --> 从数据驱动发现回到电生理第一性原理,提出可检验的猝死机制假设。 <!-- EN --> Moves from data-driven discovery back to electrophysiological first principles, proposing a testable mechanistic hypothesis.

## 局限 / Limitations
- <!-- ZH --> 除颤器获益(-54.4%)来自观察性数据,存在混杂/选择偏倚,非随机对照证据。 <!-- EN --> The ICD mortality benefit is observational and subject to confounding/selection bias, not RCT evidence.
- <!-- ZH --> 机制假设仅“初步检验”,尚需前瞻验证。 <!-- EN --> The mechanistic hypothesis is only preliminarily tested.
- <!-- ZH --> 模型架构、训练与消融、完整评测指标(AUC/校准等)在付费正文中,此处不可得(仅摘要可得 / abstract-only)。 <!-- EN --> Architecture, training/ablations, and full metrics (AUC/calibration) are paywalled (abstract-only).

## 与本研究方向的关系 / Relation to our direction
<!-- anomaly detection → virtual tissue → revert via gene prediction 这条线上,这篇处在哪一环?能复用什么? -->
<!-- ZH --> PI 标注“super relevant”,方法学连接点在 **异常检测(anomaly detection)这一环**:本文正是“从医学信号中用深度学习发现一个此前未知的疾病相关异常模式(biomarker discovery),并用生成模型把该异常显式合成/可视化”的范式。这与我们 pipeline 第一阶段“检测因疾病/药物扰动而改变的生物医学图像或空间组学区域”高度同构 —— 只是把 1D ECG 波形换成 2D/空间组学张量。可迁移的思想:(1) **判别+生成配对**——用生成模型反演判别模型所依赖的形态,得到可解释的“异常原型/counterfactual”,直接对应我们“virtual tissue”的反事实合成需求;(2) **与已知指标的互补性度量**(86.1% 不重叠)可作为评估“新发现异常是否超越已知标志物”的评测协议;(3) **从异常形态回到机制假设**呼应我们“预测若被药物调控可 revert 异常的关键基因”的下游目标——即从发现的异常出发提出可干预机制并交由湿实验验证。本文不涉及 virtual tissue 或 gene-revert 环节,但为“异常检测 + 生成式反事实解释”提供了跨模态可借鉴的高质量范例。
<!-- EN --> PI flags this as super relevant; the methodological link is the **anomaly-detection stage**. The paper is a clean template for "use deep learning to discover a previously unknown disease-associated anomaly in a medical signal, then make it explicit/visible with a generative model" — structurally the same as our stage-1 goal of detecting disease/drug-perturbed regions in biomedical images or spatial-omics, just swapping a 1D ECG waveform for 2D/spatial-omics tensors. Transferable ideas: (1) **discriminative+generative pairing** to invert what the predictor relies on into an interpretable anomaly prototype / counterfactual — directly relevant to our virtual-tissue counterfactual synthesis; (2) a **complementarity metric vs. an existing marker** (86.1% non-overlap) as an eval protocol for whether a discovered anomaly adds signal beyond known biomarkers; (3) **discovery → mechanistic hypothesis** mirrors our "predict the key genes whose modulation would revert the anomaly (wet-lab validated)" downstream. It does not touch the virtual-tissue or gene-revert stages, but is a strong cross-modality exemplar of anomaly detection plus generative counterfactual explanation.

## 可复用资产 / Reusable assets
<!-- 代码、预训练模型、数据集、评测协议。 / Code, checkpoints, datasets, eval protocols. -->
<!-- ZH --> 概念性可复用:判别+生成配对的可解释性框架、"与既有标志物互补性"作为发现价值的评测协议、跨国多终点外部验证设计。代码/权重/数据是否公开需查正文的 Data/Code Availability 段(仅摘要可得 / abstract-only)。数据集为受限的医院/登记库链接数据(瑞典 ECG-死亡证明链接、美国医疗系统、台湾医院登记库),通常不公开。DOI: 10.1038/s41586-026-10674-6。
<!-- EN --> Reusable at the concept level: the discriminative+generative interpretability framework, the "complementarity-to-existing-marker" eval protocol, and the cross-country multi-endpoint validation design. Code/checkpoint/data availability must be checked in the paper's availability statements (abstract-only). Datasets are restricted linked health records (Swedish ECG–death-certificate linkage, US health system, Taiwanese registry) and are typically not public. DOI: 10.1038/s41586-026-10674-6.

## 待读 / Follow-ups
- <!-- ZH/EN --> 取全文正文与 Methods/Extended Data:确认判别模型架构、生成模型类型(VAE/diffusion/GAN?)与配对反演的具体做法。 / Get full text + Methods for the discriminative architecture and the generative model type (VAE/diffusion/GAN?) and the inversion procedure.
- <!-- ZH/EN --> 查 Data/Code Availability,评估能否复用其可解释性/反事实合成代码。 / Check availability statements for reusable interpretability/counterfactual code.
- <!-- ZH/EN --> 精读完整评测(AUC、校准、竞争风险模型)与除颤器获益的因果分析方法。 / Read full metrics (AUC, calibration, competing-risks) and the causal analysis of ICD benefit.

## 引用 / Cite
```bibtex
@article{Obermeyer_2026, title={An ECG biomarker for sudden cardiac death discovered with deep learning}, volume={655}, ISSN={1476-4687}, url={http://dx.doi.org/10.1038/s41586-026-10674-6}, DOI={10.1038/s41586-026-10674-6}, number={8121}, journal={Nature}, publisher={Springer Science and Business Media LLC}, author={Obermeyer, Ziad and Schubert, Alexander and Ross, James and Mullainathan, Sendhil and Lingman, Markus}, year={2026}, month=June, pages={210–218} }
```
