# Cassie07/PathOmics

> **Bibkey** `Ding2023_PathOmics` · **Venue** GitHub (2023) · **Category** pathology · **Relevance** medium · **Access** open
> **Link** <https://github.com/Cassie07/PathOmics>
> `status: complete` — 基于 GitHub README(2026-10-27 读取)、README 中的流程图、仓库代码(`PathOmics/bash_main.py`、`bash_main_read.py` 等)和论文开放预印本 arXiv:2307.11952v1(方法、数据、实验设置和 Table 1 已对照;附录未读)。/ Based on the GitHub README (read 2026-10-27), its workflow figure, the repo code (`PathOmics/bash_main.py`, `bash_main_read.py`, …) and the open preprint arXiv:2307.11952v1 (methods, data, settings and Table 1 checked; appendix not read).

---

## 一句话 / One-liner
<!-- ZH --> PathOmics 是 MICCAI 2023(Oral,README 称 top 9%)论文 "Pathology-and-genomics Multimodal Transformer for Survival Outcome Prediction" 的官方代码:先用无监督预训练把病理切片和基因组学(mRNA 表达、拷贝数变异 CNA 或甲基化)的嵌入融合对齐,再有监督微调做癌症生存预测,微调时可以用双模态,也可以只用单一模态。
<!-- EN --> PathOmics is the official code of the MICCAI 2023 paper (Oral; "top 9%" per the README) "Pathology-and-genomics Multimodal Transformer for Survival Outcome Prediction": unsupervised pretraining fuses pathology-slide and genomics (mRNA expression, copy-number alteration (CNA) or methylation) embeddings, then supervised finetuning predicts cancer survival with either both modalities or a single one.

## 要点 / Takeaways
- <!-- ZH --> 两阶段:(a) 无监督多模态预训练得到图像嵌入和组学嵌入;(b) 多模态微调或 (c) 单模态微调,接风险分类器做生存预测(README Figure 1)。 <!-- EN --> Two stages: (a) unsupervised multimodal pretraining yields image and omics embeddings; (b) multimodal or (c) single-modal finetuning with a risk classifier for survival (README Figure 1).
- <!-- ZH --> 数据只涉及 TCGA-COAD 和 TCGA-READ(结肠癌、直肠癌);组学来自 cBioPortal 的 `coadread_tcga_pan_can_atlas_2018`。示例命令用 `--omic_modal 'miRNA'`(README "Usage"),但这个选项名有误导性:代码里它读取的是 mRNA 表达 z-score 文件 `data_mrna_seq_v2_rsem_zscores_ref_all_samples.txt`(`bash_main.py`);另两个选项是 `CNA` 和 `Methylation`。论文用的也是 mRNA、CNA、甲基化三种组学,没有 miRNA(论文摘要、Sec. 3)。 <!-- EN --> Data: TCGA-COAD and TCGA-READ only; omics from cBioPortal `coadread_tcga_pan_can_atlas_2018`. The example commands use `--omic_modal 'miRNA'` (README "Usage"), but the name is misleading: in the code this option loads the mRNA-expression z-score file `data_mrna_seq_v2_rsem_zscores_ref_all_samples.txt` (`bash_main.py`); the other options are `CNA` and `Methylation`. The paper also uses mRNA, CNA and methylation, not miRNA (paper abstract, Sec. 3).
- <!-- ZH --> 图像特征由用户自行提取:切前景 patch,用 ImageNet 预训练 ResNet50/101 等提特征,每张切片存一个 .npz(README "Data preprocessing")。 <!-- EN --> Image features are extracted by the user: foreground patches, ImageNet-pretrained ResNet50/101 etc., one .npz per slide (README "Data preprocessing").
- <!-- ZH --> README 不含任何数值结果,也不提供预训练权重;数值在论文 Table 1(见下文主要结果)。 <!-- EN --> The README has no numeric results and no released weights; numbers are in the paper's Table 1 (see Key results below).
- <!-- ZH --> 额外价值:README 末尾维护了一张病理–基因组多模态方法文献表(读取时 48 条,2019–2025.12),带论文和代码链接。 <!-- EN --> Extra value: the README keeps a table of pathology–genomics multimodal methods (48 entries, 2019–2025.12 at reading time) with paper and code links.

## 研究问题 / Problem
<!-- ZH --> README 只简要说明:要把病理图像和基因组数据融合来做预后(生存)预测,并让微调阶段"灵活处理多种数据",即有多模态预训练 backbone 后,多模态或单模态数据都能用于微调(README "Workflow overview")。我们的理解:后者对应临床上常见的缺模态情况(只有切片、没有测序)。
<!-- EN --> The README states briefly that the goal is to fuse pathology images and genomics for prognostic (survival) prediction, with a finetuning scheme that "flexibly handles multiple types of data": given the multimodal pretrained backbones, either multi- or single-modal data can be used for finetuning (README "Workflow overview"). Our reading: the latter addresses the common missing-modality case (slides without sequencing).

## 方法 / Method
<!-- ZH --> (根据 README 文字、命令行参数、Figure 1、代码和论文 arXiv:2307.11952)
<!-- ZH --> 1. **图像预处理**:从 TCGA 下载 WSI,切成 patch 并只保留前景,用 ImageNet 预训练 ResNet50 / ResNet101 等提 patch 特征,每张切片一个 .npz(README;细节见 Issue 1 与 `split_tiles_utils/helper.py`)。
<!-- ZH --> 2. **组学数据**:从 cBioPortal 下载 `coadread_tcga_pan_can_atlas_2018` 文件夹;示例用 mRNA 表达(选项名写作 `miRNA`),也可选 CNA 或甲基化。基因按论文引用的 N = 8 个功能类别分组(如转录因子、抑癌基因、蛋白激酶;论文 Sec. 2;仓库 `PathOmics/gene_family/`)。
<!-- ZH --> 3. **预训练(Figure 1a)**:patch 分成 N 组,每组经 Feature Extractor → Attention Refiner → Image-wise Transformer → Image-wise GAP 得到图像嵌入;组学表格数据分成 N 组,每组经 SNN → Omics-wise Transformer → Omics-wise GAP 得到组学嵌入;两个嵌入在预训练中对齐融合。图中 GAP 指 Global attention pooling。预训练损失为 MSE,把同一病人的图像嵌入和组学嵌入拉近(论文 Eq. 4;示例命令 `--pretrain_loss 'MSE'`,代码也支持 `Cosine`),融合方式 `concat`。
<!-- ZH --> 4. **微调(Figure 1b–c)**:多模态时,图像嵌入 + 组学嵌入 → Multimodal Embedding Fusion → Risk Classifier → 生存预测;单模态时,只用一个嵌入 → Risk Classifier → 生存预测。
<!-- ZH --> 5. **实验设置**:TCGA-COAD 上 4 折交叉验证预训练和微调,在 COAD 留出集评估;或在 COAD 上预训练(5 折),在 TCGA-READ 上微调、验证和评估;`--less_data` + `--less_data_ratio`(保留的微调数据比例)做少数据微调——README 写的是 `--finetune_test_ratio`,但代码里它是 READ 测试集的划分比例(`bash_main_read.py`);示例中预训练和微调各 25 epoch(论文同)。生存预测用 C-index 评估(代码用 scikit-survival 的 `concordance_index_censored`)。
<!-- EN --> (From README text, command-line flags, Figure 1, the code and the paper arXiv:2307.11952.)
<!-- EN --> 1. **Image preprocessing**: download TCGA WSIs, tile into foreground patches, extract features with ImageNet-pretrained ResNet50 / ResNet101 etc., one .npz per slide (README; see Issue 1 and `split_tiles_utils/helper.py`).
<!-- EN --> 2. **Omics**: download `coadread_tcga_pan_can_atlas_2018` from cBioPortal; mRNA expression in the example (option named `miRNA`), or CNA or methylation. Genes are grouped into N = 8 functional families taken from the paper's reference (e.g. transcription factors, tumour suppressors, protein kinases; paper Sec. 2; repo `PathOmics/gene_family/`).
<!-- EN --> 3. **Pretraining (Figure 1a)**: N patch groups → Feature Extractor → Attention Refiner → Image-wise Transformer → Image-wise GAP → image embedding; N groups of omics tabular data → SNN → Omics-wise Transformer → Omics-wise GAP → omics embedding; the two embeddings are aligned/fused. GAP = Global attention pooling in the figure. The pretraining loss is MSE, pulling the image and omics embeddings of the same patient together (paper Eq. 4; example flag `--pretrain_loss 'MSE'`, the code also offers `Cosine`); fusion `concat`.
<!-- EN --> 4. **Finetuning (Figure 1b–c)**: multimodal — image + omics embeddings → Multimodal Embedding Fusion → Risk Classifier → survival; single-modal — one embedding → Risk Classifier → survival.
<!-- EN --> 5. **Settings**: TCGA-COAD with 4-fold CV and evaluation on a COAD hold-out set; or pretrain on COAD (5-fold) and finetune/validate/evaluate on TCGA-READ; `--less_data` + `--less_data_ratio` (fraction of finetuning data kept) for data-efficient finetuning — the README names `--finetune_test_ratio`, but in the code that is the READ test-split fraction (`bash_main_read.py`); 25 pretraining and 25 finetuning epochs in the examples (same in the paper). Survival is scored with the C-index (scikit-survival `concordance_index_censored` in the code).

## 方法图 / Method diagram
```mermaid
flowchart LR
  A["TCGA WSI patches<br/>ResNet features"] --> B["Attention refiner +<br/>image-wise transformer + GAP"]
  C["Omics table<br/>mRNA, CNA or methylation<br/>8 gene groups"] --> D["SNN +<br/>omics-wise transformer + GAP"]
  B --> E["Unsupervised alignment<br/>pretrain loss MSE"]
  D --> E
  E --> F["Finetune multimodal<br/>or single-modal"]
  F --> G["Risk classifier<br/>survival prediction"]
```

## 数据 / Data
<!-- ZH --> TCGA-COAD(结肠腺癌)和 TCGA-READ(直肠腺癌)的 WSI(用户自行下载);组学来自 cBioPortal `coadread_tcga_pan_can_atlas_2018`,示例用 mRNA 表达(选项名 `miRNA`)。仓库不含原始数据或提取好的特征。README 没有给出病例数;论文:去掉缺组学或缺生存标签的样本后,纳入 TCGA-COAD 426 人、TCGA-READ 145 人;WSI 切成 512×512 不重叠 patch(论文 Sec. 3)。
<!-- EN --> TCGA-COAD and TCGA-READ WSIs (downloaded by the user); omics from cBioPortal `coadread_tcga_pan_can_atlas_2018`, mRNA expression in the example (option named `miRNA`). No raw data or features are shipped, and the README gives no case counts; the paper keeps 426 TCGA-COAD and 145 TCGA-READ patients after removing samples without genomics or survival labels, and tiles WSIs into 512×512 non-overlapping patches (paper Sec. 3).

## 主要结果 / Key results
<!-- ZH --> README 没有列出任何数值结果,只说明论文被 MICCAI 2023 接收为 Oral,并标注 "top 9%"(仓库描述与 README 开头)。以下数值来自论文 arXiv:2307.11952 的 Table 1 和正文(C-index %;论文报告 3 次重复实验的平均值,± 为论文所列的离散度,论文未说明是标准差还是标准误):
<!-- EN --> The README lists no numeric results; it only states that the paper was accepted to MICCAI 2023 as an Oral, "top 9%" (repo description and README header). The numbers below are from Table 1 and the text of the paper arXiv:2307.11952 (C-index %; the paper reports the average of three repeated runs, and the ± spread is as printed — the paper does not say whether it is s.d. or s.e.):
- <!-- ZH --> **总体**:论文称在 TCGA-COAD 上比最好的已有方法高约 2%,在 TCGA-READ 上高约 4%;基线为 DeepSets、AB-MIL、TransMIL、MCAT、PORPOISE(论文 Sec. 3 Results)。 <!-- EN --> **Overall**: the paper reports about 2% higher C-index than the best prior methods on TCGA-COAD and about 4% on TCGA-READ; baselines are DeepSets, AB-MIL, TransMIL, MCAT and PORPOISE (paper Sec. 3, Results).
- <!-- ZH --> **TCGA-COAD**:图像 + mRNA 预训练与微调 67.32 ± 1.69(只用图像微调 63.78,只用 mRNA 微调 60.76);基线中最高为 DeepSets 图像 + 甲基化 65.61 和 PORPOISE 图像 + mRNA 65.31(Table 1)。 <!-- EN --> **TCGA-COAD**: image + mRNA pretraining and finetuning 67.32 ± 1.69 (image-only finetuning 63.78, mRNA-only 60.76); the highest baselines are DeepSets image + methylation 65.61 and PORPOISE image + mRNA 65.31 (Table 1).
- <!-- ZH --> **TCGA-READ**:图像 + mRNA 74.35 ± 1.15;最高基线 MCAT 图像 + mRNA 70.27(Table 1)。单模态微调:正文说"用图像 + 甲基化预训练、只用图像微调"得到 74.85%,比最好的基线高约 4%;但 Table 1 中 74.85 ± 0.37 列在"图像 + mRNA 预训练、只用图像微调"一行,而图像 + 甲基化预训练、只用图像微调为 64.42——论文正文与表格不一致。 <!-- EN --> **TCGA-READ**: image + mRNA 74.35 ± 1.15; highest baseline MCAT image + mRNA 70.27 (Table 1). Single-modal finetuning: the text says pretraining on image + methylation and finetuning on image only gives 74.85%, about 4% above the best baseline; but Table 1 lists 74.85 ± 0.37 in the "image + mRNA pretraining, image-only finetuning" row, and image + methylation pretraining with image-only finetuning is 64.42 — the paper's text and table disagree.
- <!-- ZH --> **少数据**:只用 50% 的 COAD 微调数据时 C-index 64.80%;在 READ 上用 50% 或 75% 微调数据时仍高于基线平均(例如 72.32% 对 64.23%)(论文 Ablation Analysis,Fig. 3)。 <!-- EN --> **Less data**: with 50% of the COAD finetuning data the C-index is 64.80%; on READ with 50% or 75% of the finetuning data it stays above the baseline average (e.g. 72.32% vs 64.23%) (paper Ablation Analysis, Fig. 3).
- <!-- ZH --> **去掉无监督预训练**:多模态和单模态结果都低 2%–10%(论文 Ablation Analysis)。 <!-- EN --> **Without unsupervised pretraining**: results are 2%–10% lower for both multi- and single-modal data (paper Ablation Analysis).

## 创新点 / Contributions
- <!-- ZH --> (按 README)用无监督预训练融合病理和基因组嵌入,得到可复用的多模态 backbone。 <!-- EN --> (Per README) Unsupervised pretraining fuses pathology and genomics embeddings into a reusable multimodal backbone.
- <!-- ZH --> (按 README)微调阶段可用双模态或单模态,支持缺模态。 <!-- EN --> (Per README) Finetuning works with multi- or single-modal data, supporting missing modalities.
- <!-- ZH --> (按 README)提供跨数据集(COAD 预训练 → READ 微调)和少数据微调选项。 <!-- EN --> (Per README) Cross-dataset (COAD pretrain → READ finetune) and data-efficient finetuning options.
- <!-- ZH --> 持续更新的病理–基因组多模态方法文献表(48 条)。 <!-- EN --> A maintained literature table of pathology–genomics multimodal methods (48 entries).

## 局限 / Limitations
- <!-- ZH --> README 的示例只覆盖 TCGA 结直肠癌 + mRNA 表达(选项名 `miRNA`);代码和论文还支持 CNA 和甲基化,但只有结直肠癌这一种癌(README;`bash_main.py`;论文 Sec. 3)。 <!-- EN --> The README examples cover only TCGA colorectal cancer + mRNA expression (option named `miRNA`); the code and paper also cover CNA and methylation, but only colorectal cancer (README; `bash_main.py`; paper Sec. 3).
- <!-- ZH --> 我们的理解:推荐用 ImageNet 预训练的 ResNet 提特征,而不是病理基础模型(如 UNI、CONCH);换成更强的编码器可能有提升,但未经验证。 <!-- EN --> Our reading: it suggests ImageNet-pretrained ResNets rather than pathology foundation models (e.g. UNI, CONCH); stronger encoders might help but this is untested.
- <!-- ZH --> 我们的理解:README 无数值结果、无预训练权重(`--load_model_finetune` 需要你自己先训好保存),复现要从下载 TCGA、切片、提特征开始。 <!-- EN --> Our reading: no numeric results and no released weights (`--load_model_finetune` assumes your own saved weights), so reproduction starts from downloading TCGA, tiling and feature extraction.
- <!-- ZH --> 我们的理解:任务是 slide/患者级生存预测,不做空间定位,也不做异常检测或扰动。 <!-- EN --> Our reading: the task is slide/patient-level survival prediction, with no spatial localisation, anomaly detection or perturbation.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 处在"组织表征 / 多模态建模"这一环,与检测和回复环关系不大。
- 我们的理解:它提供了"病理图像嵌入 ⟷ 组学嵌入"预训练对齐、再允许单模态推理的工程范式。肾脏多模态数据(如 H&E 与单细胞 / 空间组学)常常不是每个样本都具备全部模态;这种"多模态预训练 + 单模态可用"的思路可以借来,让只有 H&E 的样本也能用上多模态学到的表示。
- 我们的理解:如果要用于"模态之间不一致即异常"的检测思路,需要把它从 slide 级生存预测改成空间分辨(spot / 细胞级)的对齐,并设计不一致分数——仓库本身不提供这些。
- 我们的理解:README 的文献表是快速了解病理–基因组融合方法(PORPOISE、MCAT、SurvPath、TANGLE、POMP 等)的入口。
- 相关性 medium:结直肠癌 TCGA,不涉及肾脏和空间组学。
<!-- EN --> It sits at the tissue-representation / multimodal-modelling stage, with little bearing on detect or revert.
- Our reading: it gives an engineering template for pretraining-time alignment of pathology and omics embeddings that still allows single-modal inference. Kidney multimodal data (e.g. H&E plus single-cell / spatial omics) often lack some modalities for some samples; "multimodal pretraining, single-modal use" could let H&E-only samples benefit from multimodal representations.
- Our reading: to support "cross-modal disagreement = anomaly", it would have to move from slide-level survival to spatially resolved (spot / cell-level) alignment with a disagreement score — none of which the repo provides.
- Our reading: the README literature table is a quick entry point to pathology–genomics fusion methods (PORPOISE, MCAT, SurvPath, TANGLE, POMP, …).
- Relevance medium: TCGA colorectal cancer; no kidney, no spatial omics.

## 可复用资产 / Reusable assets
- <!-- ZH --> **代码**:`bash_main.py`(TCGA-COAD)、`bash_main_read.py`(COAD → READ)、`split_tiles_utils/helper.py`(切 patch 与提特征);环境 Python 3.8.18、PyTorch 2.0.1、scikit-survival 0.21.0 等。 <!-- EN --> **Code**: `bash_main.py` (TCGA-COAD), `bash_main_read.py` (COAD → READ), `split_tiles_utils/helper.py` (tiling and features); Python 3.8.18, PyTorch 2.0.1, scikit-survival 0.21.0, etc.
<!-- ZH/EN --> <https://github.com/Cassie07/PathOmics>
- <!-- ZH --> **数据**:TCGA-COAD / READ WSI;cBioPortal `coadread_tcga_pan_can_atlas_2018`。 <!-- EN --> **Data**: TCGA-COAD / READ WSIs; cBioPortal `coadread_tcga_pan_can_atlas_2018`.
<!-- ZH/EN --> <https://www.cbioportal.org/>
- <!-- ZH --> **权重**:README 未提供。 <!-- EN --> **Weights**: none provided in the README.
- <!-- ZH --> **文献表**:README 末尾 48 条病理–基因组多模态方法,带论文和代码链接。 <!-- EN --> **Literature table**: 48 pathology–genomics multimodal methods at the end of the README, with paper and code links.

## 待读 / Follow-ups
- <!-- ZH --> 读论文附录(arXiv:2307.11952),看单模态结果的完整表和基因分组消融的细节。 <!-- EN --> Read the paper's appendix (arXiv:2307.11952) for the full single-modal results and the gene-grouping ablation details.
- <!-- ZH --> 从文献表挑 SurvPath、TANGLE(均 CVPR 2024,mahmoodlab)对照,看通路/转录组引导的表示是否更适合与空间组学对接。 <!-- EN --> From the table, compare SurvPath and TANGLE (both CVPR 2024, mahmoodlab) to see whether pathway/transcriptome-guided representations suit spatial omics better.

## 图表 / Figures & tables

![PathOmics two-stage pipeline](figures/fig1.png)
<!-- ZH --> **图1.** PathOmics 两阶段流程总览。(a) 无监督多模态预训练:WSI 切成 N 组 patch → Feature Extractor 提特征 → Attention Refiner + Image-wise Transformer + GAP 得到图像嵌入(蓝色三角);基因组学 omics 表格数据分组经 SNN + Omics-wise Transformer + GAP 得到组学嵌入(绿色圆),两嵌入在预训练中对齐融合(GAP = Global attention pooling)。(b) 有监督多模态微调:图像+组学嵌入经 Multimodal Embedding Fusion → Risk Classifier → 生存预测。(c) 有监督单模态微调:仅图像或仅组学嵌入 → Risk Classifier → 生存预测,支持推断时缺模态。
<!-- EN --> **Fig 1.** Overview of the two-stage PathOmics pipeline. (a) Unsupervised multimodal pretraining: WSIs are tiled into N groups of patches → Feature Extractor → Attention Refiner + Image-wise Transformer + GAP yields the image embedding (blue triangle); grouped omics tabular data pass through SNN + Omics-wise Transformer + GAP to yield the omics embedding (green circle); the two are aligned/fused during pretraining (GAP = Global attention pooling). (b) Supervised multimodal finetuning: fused image+omics embeddings → Multimodal Embedding Fusion → Risk Classifier → survival prediction. (c) Supervised single-modal finetuning: image-only or omics-only embedding → Risk Classifier → survival prediction, enabling missing-modality inference.
<!-- ZH/EN --> _Source: https://github.com/Cassie07/PathOmics/raw/main/Figures/Figure1.png  ·  License: GitHub README figure (MICCAI 2023, Ding et al.)_

### 结果表 / Results

<!-- ZH --> **表1.** PathOmics 的 C-index(%),摘自论文 Table 1 "Ours" 各行(README 本身没有数值)。
<!-- EN --> **Table 1.** PathOmics C-index (%), from the "Ours" rows of the paper's Table 1 (the README itself has no numbers).

| Pretrain data / 预训练数据 | Finetune data / 微调数据 | TCGA-COAD | TCGA-READ |
|---|---|:---:|:---:|
| image+mRNA / 图像+mRNA | image+mRNA / 图像+mRNA | 67.32 ± 1.69 | 74.35 ± 1.15 |
| image+mRNA / 图像+mRNA | image / 图像 | 63.78 ± 1.22 | 74.85 ± 0.37 |
| image+mRNA / 图像+mRNA | mRNA | 60.76 ± 0.88 | 59.61 ± 1.37 |
| image+CNA / 图像+CNA | image+CNA / 图像+CNA | 61.19 ± 1.03 | 73.95 ± 1.05 |
| image+CNA / 图像+CNA | image / 图像 | 58.06 ± 1.54 | 71.18 ± 1.39 |
| image+CNA / 图像+CNA | CNA | 56.43 ± 1.02 | 63.95 ± 0.55 |
| image+Methy / 图像+甲基化 | image+Methy / 图像+甲基化 | 67.22 ± 1.67 | 71.80 ± 2.03 |
| image+Methy / 图像+甲基化 | image / 图像 | 60.43 ± 0.72 | 64.42 ± 0.72 |
| image+Methy / 图像+甲基化 | Methy / 甲基化 | 61.06 ± 1.34 | 65.42 ± 0.91 |

<!-- ZH/EN --> _Source: Ding et al., arXiv:2307.11952v1, Table 1 (MICCAI 2023, pp. 622–631, DOI 10.1007/978-3-031-43987-2_60)._

## 引用 / Cite
```bibtex
@inproceedings{Ding2023_PathOmics,
  title = {Pathology-and-genomics Multimodal Transformer for Survival Outcome Prediction},
  author = {Ding, Kexin and Zhou, Mu and Metaxas, Dimitris N. and Zhang, Shaoting},
  booktitle = {Medical Image Computing and Computer Assisted Intervention (MICCAI)},
  pages = {622--631},
  year = {2023},
  doi = {10.1007/978-3-031-43987-2_60},
  eprint = {2307.11952},
  archivePrefix = {arXiv},
  note = {Code: https://github.com/Cassie07/PathOmics},
  url = {https://github.com/Cassie07/PathOmics}
}
```
