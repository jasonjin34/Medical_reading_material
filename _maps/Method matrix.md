---
title: Method map — anomaly detection from general to kidney
tags:
- moc
- matrix
---

# Method map — anomaly detection from general to kidney

Rows are anomaly-detection paradigms, columns go from general data to kidney omics. Arrows show where a method was carried over; dashed cells are what Topic 1 adds.

行是异常检测的方法范式，列从通用数据一直到肾脏组学。箭头表示方法被迁移到哪里；虚线格是课题 1 要补的空白。

| Paradigm / 范式 | General / industrial<br>通用 / 工业图像 | Medical imaging<br>医学影像 | Histopathology (H&E)<br>病理切片 (H&E) | Single-cell omics<br>单细胞组学 | Spatial omics<br>空间组学 | Kidney (omics + histology)<br>肾脏（组学 + 病理） |
| --- | --- | --- | --- | --- | --- | --- |
| **Reconstruction / generative**<br>重建 / 生成式 | · | [[_maps/papers/f-anogan-media-2019|f-AnoGAN]]<br>[[_maps/papers/anogan-ipmi-2017|AnoGAN]]<br>[[_maps/papers/diffusion-medical-ad-miccai-2022|Diffusion AD (medical)]] | [[_maps/papers/histo-miccai-2025|Latent-diffusion AD]]<br>[[_maps/papers/counterfactual-diffusion-cancerres-2026|Counterfactual diffusion]] | · | [[_maps/papers/meatrd-aaai-2025|MEATRD]]<br>[[_maps/papers/spatial-natcommun-2024|STANDS]] | · |
| **Feature embedding + memory bank / kNN**<br>特征嵌入 + 记忆库 / kNN | [[_maps/papers/patchcore-cvpr-2022|PatchCore]]<br>[[_maps/papers/padim-icpr-2020|PaDiM]] | [[_maps/papers/abnormality-radiology-arxiv-2024|Abnormality radiology (Ligero 2024)]] | [[_maps/papers/histo-nejmai-2024|Clinical-grade histo AD]] | · | · | *Topic 1 gap* |
| **Density / one-class**<br>密度估计 / 单类 | [[_maps/papers/deep-svdd-icml-2018|Deep SVDD]]<br>[[_maps/papers/cflow-ad-wacv-2022|CFLOW-AD]] | · | [[_maps/papers/histo-anomaly-bi-repo|BI histo-AD code]] | · | [[_maps/papers/sardine-bioinformatics-2025|Sardine]] | *Topic 1 gap* |
| **Synthetic anomalies / outlier exposure**<br>合成异常 / 异常暴露 | [[_maps/papers/draem-iccv-2021|DRAEM]] | · | [[_maps/papers/histo-nejmai-2024|Clinical-grade histo AD]] | · | · | · |
| **Classifier OOD & reference mapping**<br>分类器 OOD 与参考映射 | [[_maps/papers/mahalanobis-ood-neurips-2018|Mahalanobis OOD]]<br>[[_maps/papers/msp-ood-iclr-2017|MSP baseline]]<br>[[_maps/papers/energy-ood-neurips-2020|Energy OOD]] | · | · | [[_maps/papers/refmap-eval-biorxiv-2025|Reference-mapping QC]]<br>[[_maps/papers/scatac-novel-genomeres-2026|Novel types in scATAC]] | · | [[_maps/papers/dkd-spatial-atlas-nature-2026|DKD spatial atlas]] |
| **Conformal / calibrated**<br>保形 / 校准 | [[_maps/papers/conformal-outliers-annstat-2023|Conformal p-values]] | · | · | [[_maps/papers/conformal-scrna-bioinformatics-2025|Conformal annotation]] | · | *Topic 1 gap* |
| **Healthy-reference comparison & disease scores**<br>健康参考对比与疾病评分 | · | · | · | [[_maps/papers/healthy-ref-natgenet-2023|Healthy-reference design]]<br>[[_maps/papers/mrvi-natmethods-2025|MrVI]] | · | [[_maps/papers/abedini-kidney-atlas-natgenet-2024|Kidney atlas (Abedini 2024)]]<br>[[_maps/papers/cellspectra-natgenet-2025|CellSpectra]]<br>[[_maps/papers/damage-scores-cellgenomics-2026|Damage scores]] |
| **Cross-modal consistency**<br>跨模态一致性 | · | · | [[_maps/papers/he2expr-bench-natcommun-2025|H&E→expression benchmark]] | · | [[_maps/papers/loki-omiclip-natmethods-2025|Loki / OmiCLIP]] | [[_maps/papers/kidney-multimodal-genomebiol-2026|Kidney multiome (mBDRC)]]<br>*Topic 1 gap* |
| **Technical artifacts (nuisance anomalies)**<br>技术伪影（干扰性异常） | · | · | · | [[_maps/papers/ambient-rna-bench-biorxiv-2026|Ambient-RNA benchmark]] | [[_maps/papers/xenium-split-natmethods-2026|Xenium contamination (SPLIT)]]<br>[[_maps/papers/ovrlpy-natbiotech-2026|ovrlpy]]<br>[[_maps/papers/resolvi-natmethods-2026|ResolVI]] | [[_maps/papers/lake-snrna-pipeline-natcommun-2019|Kidney snRNA processing (Lake 2019)]]<br>[[_maps/papers/malone-transplant-chimerism-jasn-2020|Transplant chimerism (Malone)]]<br>[[_maps/papers/denisenko-dissociation-bias-genomebiol-2020|Dissociation bias, mouse kidney]]<br>[[_maps/papers/janssen-ambient-noise-genomebiol-2023|Ambient truth, mouse kidney (Janssen)]]<br>[[_maps/papers/hoeft-genotype-multiplexing-natcommun-2024|SNP multiplexing (Hoeft)]]<br>*Topic 1 gap* |
| **Benchmarks, datasets & surveys**<br>基准、数据集与综述 | [[_maps/papers/ad-unifying-review-procieee-2021|Unifying AD review]]<br>[[_maps/papers/generalized-ood-survey-ijcv-2024|Generalized OOD survey]]<br>[[_maps/papers/mvtec-ad-cvpr-2019|MVTec AD]] | [[_maps/papers/medianomaly-media-2025|MedIAnomaly]] | [[_maps/papers/pathology-ad-bench-mlhealth-2025|Pathology AD benchmark]] | · | · | [[_maps/papers/nih-kidney-ai-challenge-2026|NIH Kidney AI Challenge]]<br>*Topic 1 gap* |

## Paradigms / 范式

- **Reconstruction / generative / 重建 / 生成式** — Learn to regenerate normal data; a high reconstruction error is anomalous. 学会重建正常数据，重建误差大的就是异常。
  - Kidney omics / 肾脏组学: Autoencoders / VAEs on expression (+ histology); error per cell or spot. 在表达谱（加病理图像）上训练 AE / VAE，按细胞或 spot 计算误差。
- **Feature embedding + memory bank / kNN / 特征嵌入 + 记忆库 / kNN** — Embed with a pretrained network, store normal features, score by distance to the nearest normal ones. 用预训练网络提特征，存下正常样本的特征，用到最近正常特征的距离打分。
  - Kidney omics / 肾脏组学: kNN distance in a scVI / foundation-model latent space built from healthy donors. 在健康供体构建的 scVI / 基础模型潜空间里算 kNN 距离。
- **Density / one-class / 密度估计 / 单类** — Model the density or a tight boundary of normal data (one-class SVM, Deep SVDD, normalizing flows). 对正常数据建模密度或紧致边界（单类 SVM、Deep SVDD、标准化流）。
  - Kidney omics / 肾脏组学: Density of healthy cell states; low likelihood = unexplained state. 估计健康细胞状态的密度，似然低就是解释不了的状态。
- **Synthetic anomalies / outlier exposure / 合成异常 / 异常暴露** — Train a classifier against fake or auxiliary anomalies. 用人造的或外部的异常样本训练分类器。
  - Kidney omics / 肾脏组学: Simulated doublets, ambient RNA or perturbed profiles as negatives. 用模拟的 doublet、ambient RNA 或扰动后的表达谱作为负样本。
- **Classifier OOD & reference mapping / 分类器 OOD 与参考映射** — Use a supervised model's confidence, logits or feature statistics to spot inputs unlike its training data. 利用监督模型的置信度、logits 或特征统计，找出和训练数据不同的输入。
  - Kidney omics / 肾脏组学: Label-transfer confidence and latent distance to a reference atlas; novel cell types. 标签迁移的置信度、到参考图谱的潜空间距离；新细胞类型。
- **Conformal / calibrated / 保形 / 校准** — Turn any score into a p-value with finite-sample error control. 把任意异常分数转成有限样本下误差可控的 p 值。
  - Kidney omics / 肾脏组学: Per-cell anomaly p-values with FDR control across thousands of cells. 给每个细胞一个异常 p 值，并在成千上万个细胞上控制 FDR。
- **Healthy-reference comparison & disease scores / 健康参考对比与疾病评分** — Compare samples or neighbourhoods with a healthy reference; score known disease programmes. 把样本或邻域和健康参考对比，给已知的疾病程序打分。
  - Kidney omics / 肾脏组学: Differential abundance, sample-level distances, damage / injury scores. 差异丰度、样本层面的距离、损伤评分。
- **Cross-modal consistency / 跨模态一致性** — Predict one modality from another; disagreement flags artefacts or biology. 用一个模态预测另一个模态，对不上的地方提示伪影或真实生物学变化。
  - Kidney omics / 肾脏组学: RNA ↔ ATAC ↔ Xenium ↔ H&E agreement per cell or region. 在每个细胞或区域上检查 RNA ↔ ATAC ↔ Xenium ↔ H&E 是否一致。
- **Technical artifacts (nuisance anomalies) / 技术伪影（干扰性异常）** — Anomalies that are technical, not biological, and must be removed or modelled first. 来自技术而不是生物学的异常，要先去除或建模。
  - Kidney omics / 肾脏组学: Doublets, ambient RNA, segmentation spillover, z-overlap in Xenium. doublet、ambient RNA、细胞分割溢出、Xenium 的 z 向重叠。
- **Benchmarks, datasets & surveys / 基准、数据集与综述** — Where methods are compared. 方法在哪里被横向比较。
  - Kidney omics / 肾脏组学: An expert-validated kidney anomaly benchmark (Topic 1 deliverable). 经专家验证的肾脏异常基准（课题 1 的产出）。

## Topic 1 gaps / 课题 1 的空白

- feature × kidney: Topic 1 baseline: kNN distance to healthy KPMP / Lake cells in a shared latent space. 课题 1 基线：在共享潜空间里算到健康 KPMP / Lake 细胞的 kNN 距离。
- density × kidney: Density of healthy kidney cell states per cell type. 按细胞类型估计健康肾脏细胞状态的密度。
- conformal × kidney: Calibrated per-cell anomaly p-values with FDR control. 给每个细胞校准过的异常 p 值，并控制 FDR。
- crossmodal × kidney: Core idea of Topic 1: RNA / ATAC / Xenium / H&E disagreement separates artifacts from disease. 课题 1 的核心：用 RNA / ATAC / Xenium / H&E 之间的不一致，把伪影和疾病分开。
- artifact × kidney: Artifact audit of the 95-biopsy Xenium + snRNA data. 对 95 例活检的 Xenium + snRNA 数据做伪影审计。
- bench × kidney: KidneyAnomalyBench: expert-validated anomalies. KidneyAnomalyBench：经专家验证的异常。

## Method lineage / 方法迁移

- [[_maps/papers/anogan-ipmi-2017|AnoGAN]] → [[_maps/papers/f-anogan-media-2019|f-AnoGAN]] — adds an encoder + WGAN to AnoGAN
- [[_maps/papers/anogan-ipmi-2017|AnoGAN]] → [[_maps/papers/deep-svdd-icml-2018|Deep SVDD]] — AnoGAN as deep baseline
- [[_maps/papers/anogan-ipmi-2017|AnoGAN]] → [[_maps/papers/ad-unifying-review-procieee-2021|Unifying AD review]] — reviewed: GAN reconstruction
- [[_maps/papers/f-anogan-media-2019|f-AnoGAN]] → [[_maps/papers/ad-unifying-review-procieee-2021|Unifying AD review]] — reviewed: GAN + explicit encoder
- [[_maps/papers/deep-svdd-icml-2018|Deep SVDD]] → [[_maps/papers/ad-unifying-review-procieee-2021|Unifying AD review]] — hypersphere model, shallow ↔ deep
- [[_maps/papers/deep-svdd-icml-2018|Deep SVDD]] → [[_maps/papers/meatrd-aaai-2025|MEATRD]] — Deep-SVDD-style one-class scoring
- [[_maps/papers/f-anogan-media-2019|f-AnoGAN]] → [[_maps/papers/meatrd-aaai-2025|MEATRD]] — image baseline
- [[_maps/papers/f-anogan-media-2019|f-AnoGAN]] → [[_maps/papers/histo-miccai-2025|Latent-diffusion AD]] — baseline vs latent diffusion
- [[_maps/papers/f-anogan-media-2019|f-AnoGAN]] → [[_maps/papers/medianomaly-media-2025|MedIAnomaly]] — benchmarked (reconstruction family)
- [[_maps/papers/mvtec-ad-cvpr-2019|MVTec AD]] → [[_maps/papers/ad-unifying-review-procieee-2021|Unifying AD review]] — benchmarks on MVTec AD
- [[_maps/papers/padim-icpr-2020|PaDiM]] → [[_maps/papers/patchcore-cvpr-2022|PatchCore]] — memory bank generalises per-position Gaussians
- [[_maps/papers/padim-icpr-2020|PaDiM]] → [[_maps/papers/cflow-ad-wacv-2022|CFLOW-AD]] — flow likelihood generalises PaDiM's Gaussian
- [[_maps/papers/mahalanobis-ood-neurips-2018|Mahalanobis OOD]] → [[_maps/papers/padim-icpr-2020|PaDiM]] — Mahalanobis scoring on pretrained features
- [[_maps/papers/mahalanobis-ood-neurips-2018|Mahalanobis OOD]] → [[_maps/papers/cflow-ad-wacv-2022|CFLOW-AD]] — Gaussian prior as special case
- [[_maps/papers/mvtec-ad-cvpr-2019|MVTec AD]] → [[_maps/papers/padim-icpr-2020|PaDiM]] — main benchmark
- [[_maps/papers/mvtec-ad-cvpr-2019|MVTec AD]] → [[_maps/papers/patchcore-cvpr-2022|PatchCore]] — main benchmark
- [[_maps/papers/mvtec-ad-cvpr-2019|MVTec AD]] → [[_maps/papers/draem-iccv-2021|DRAEM]] — main benchmark
- [[_maps/papers/mvtec-ad-cvpr-2019|MVTec AD]] → [[_maps/papers/cflow-ad-wacv-2022|CFLOW-AD]] — main benchmark
- [[_maps/papers/anogan-ipmi-2017|AnoGAN]] → [[_maps/papers/mvtec-ad-cvpr-2019|MVTec AD]] — GAN baseline
- [[_maps/papers/patchcore-cvpr-2022|PatchCore]] → [[_maps/papers/pathology-ad-bench-mlhealth-2025|Pathology AD benchmark]] — benchmarked on pathology
- [[_maps/papers/padim-icpr-2020|PaDiM]] → [[_maps/papers/pathology-ad-bench-mlhealth-2025|Pathology AD benchmark]] — benchmarked on pathology
- [[_maps/papers/draem-iccv-2021|DRAEM]] → [[_maps/papers/pathology-ad-bench-mlhealth-2025|Pathology AD benchmark]] — benchmarked on pathology
- [[_maps/papers/cflow-ad-wacv-2022|CFLOW-AD]] → [[_maps/papers/pathology-ad-bench-mlhealth-2025|Pathology AD benchmark]] — benchmarked on pathology
- [[_maps/papers/mvtec-ad-cvpr-2019|MVTec AD]] → [[_maps/papers/pathology-ad-bench-mlhealth-2025|Pathology AD benchmark]] — industrial reference datasets
- [[_maps/papers/msp-ood-iclr-2017|MSP baseline]] → [[_maps/papers/mahalanobis-ood-neurips-2018|Mahalanobis OOD]] — MSP as baseline
- [[_maps/papers/msp-ood-iclr-2017|MSP baseline]] → [[_maps/papers/energy-ood-neurips-2020|Energy OOD]] — energy replaces softmax score
- [[_maps/papers/mahalanobis-ood-neurips-2018|Mahalanobis OOD]] → [[_maps/papers/energy-ood-neurips-2020|Energy OOD]] — benchmarked baseline
- [[_maps/papers/conformal-outliers-annstat-2023|Conformal p-values]] → [[_maps/papers/conformal-scrna-bioinformatics-2025|Conformal annotation]] — calibration-conditional conformal p-values
- [[_maps/papers/msp-ood-iclr-2017|MSP baseline]] → [[_maps/papers/generalized-ood-survey-ijcv-2024|Generalized OOD survey]] — baseline in OpenOOD
- [[_maps/papers/mahalanobis-ood-neurips-2018|Mahalanobis OOD]] → [[_maps/papers/generalized-ood-survey-ijcv-2024|Generalized OOD survey]] — distance-based OOD
- [[_maps/papers/energy-ood-neurips-2020|Energy OOD]] → [[_maps/papers/generalized-ood-survey-ijcv-2024|Generalized OOD survey]] — post-hoc output-based OOD
- [[_maps/papers/ad-unifying-review-procieee-2021|Unifying AD review]] → [[_maps/papers/generalized-ood-survey-ijcv-2024|Generalized OOD survey]] — sensory / semantic anomaly split
- [[_maps/papers/deep-svdd-icml-2018|Deep SVDD]] → [[_maps/papers/generalized-ood-survey-ijcv-2024|Generalized OOD survey]] — one-class AD reviewed
- [[_maps/papers/draem-iccv-2021|DRAEM]] → [[_maps/papers/generalized-ood-survey-ijcv-2024|Generalized OOD survey]] — AD method on far-OOD
- [[_maps/papers/mvtec-ad-cvpr-2019|MVTec AD]] → [[_maps/papers/generalized-ood-survey-ijcv-2024|Generalized OOD survey]] — sensory-AD benchmark
