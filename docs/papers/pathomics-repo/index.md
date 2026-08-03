# Cassie07/PathOmics

> **Bibkey** `pathomics-repo` · **Venue** GitHub (2023) · **Category** pathology · **Relevance** medium · **Access** open
> **Link** <https://github.com/Cassie07/PathOmics>
> `status: complete` — 若为 abstract-only,把 PDF 放到本文件夹的 `source.pdf` 后可补全全文精读。

---

## 一句话 / One-liner
<!-- ZH --> PathOmics 是 MICCAI 2023 Oral 论文的官方开源实现:一个"病理图像 + 基因组学"多模态 Transformer,用无监督多模态预训练学习融合表征,再有监督微调来预测癌症生存结局(survival outcome)。
<!-- EN --> PathOmics is the official code for a MICCAI 2023 Oral paper: a pathology-and-genomics multimodal Transformer that learns fused embeddings via unsupervised multimodal pretraining, then supervised-finetunes to predict cancer survival outcomes.

## 研究问题 / Problem
<!-- ZH --> 癌症预后需要同时利用组织形态(WSI)与分子信息(基因组学),但两种模态尺度/维度差异大,且临床上常缺失某一模态。核心问题:如何在预训练阶段有效融合病理与基因组学,并让下游微调既能用多模态、也能在只剩单模态(如推断时只有病理图)时仍可用,从而提升生存预测的 C-index。
<!-- EN --> Cancer prognosis benefits from both tissue morphology (WSIs) and molecular signals (genomics), but the modalities differ in scale/dimensionality and one is often missing in practice. The problem: fuse pathology and genomics during pretraining so that downstream finetuning works with multimodal data yet remains usable when only a single modality (e.g., image-only at inference) is available, improving survival prediction.

## 方法 / Method
<!-- ZH --> 两阶段流程。(a) 无监督多模态预训练:WSI 切 patch → 用 ImageNet 预训练 ResNet50/101 提 patch 特征存为 .npz;基因组学(miRNA)取对应特征;通过多模态 Transformer 融合两模态生成对齐的图像/基因组嵌入(预训练损失用 MSE,支持在预训练中做 GAP 全局平均池化 `--use_GAP_in_pretrain_flag`)。(b)(c) 有监督微调:用预训练得到的多模态 backbone,对多模态或单模态数据做生存预测微调。融合方式默认 `concat`。支持 data-efficient 微调(`--less_data` + `--finetune_test_ratio`)与跨数据集迁移(COAD 预训练 → READ 微调)。
<!-- EN --> Two-stage pipeline. (a) Unsupervised multimodal pretraining: tile WSIs into foreground patches → extract patch features with an ImageNet-pretrained ResNet50/101 saved as one .npz per slide; take corresponding genomics (miRNA) features; a multimodal Transformer fuses both to produce aligned image/genomics embeddings (pretrain loss = MSE, optional global-average-pooling via `--use_GAP_in_pretrain_flag`). (b)(c) Supervised finetuning: reuse the pretrained multimodal backbone to finetune for survival prediction on multi- or single-modal data (default fusion = `concat`). Supports data-efficient finetuning (`--less_data`, `--finetune_test_ratio`) and cross-dataset transfer (pretrain on COAD → finetune on READ).

## 数据 / Data
<!-- ZH --> TCGA-COAD(结肠腺癌)与 TCGA-READ(直肠腺癌)。影像模态为 WSI(需自行从 TCGA 下载、切 patch、提特征);基因组学为 miRNA,来自 cBioPortal 的 `coadread_tcga_pan_can_atlas_2018`。COAD 内部用 4 折交叉验证 + hold-out;COAD→READ 迁移用 5 折。仓库不含原始数据与切片特征,需按预处理步骤自行生成。
<!-- EN --> TCGA-COAD (colon adenocarcinoma) and TCGA-READ (rectal adenocarcinoma). Imaging modality is WSIs (user downloads from TCGA, tiles, extracts features); genomics is miRNA from cBioPortal (`coadread_tcga_pan_can_atlas_2018`). COAD uses 4-fold CV + hold-out; COAD→READ transfer uses 5-fold. The repo ships no raw data or patch features — these must be generated via the preprocessing steps.

## 主要结果 / Key results
<!-- ZH --> README 未列出具体 C-index 数值(需查论文 https://rdcu.be/dnwKf)。可确认的定性结论:该方法在 MICCAI 2023 被评为 Oral(top 9%),核心卖点是多模态预训练 backbone 使得下游即使单模态输入也能获得可用的生存预测性能,并支持跨癌种迁移(COAD→READ)与 data-efficient 微调。(具体指标以论文为准 / numeric C-index not in README.)
<!-- EN --> The README lists no explicit C-index numbers (see paper https://rdcu.be/dnwKf). Confirmable qualitatively: the method was a MICCAI 2023 Oral (top 9%); its selling point is that the multimodal pretrained backbone yields usable survival-prediction performance even with single-modal input downstream, plus cross-cancer transfer (COAD→READ) and data-efficient finetuning. (Exact metrics live in the paper, not the repo.)

## 创新点 / Contributions
- <!-- ZH --> 用无监督多模态预训练对齐病理与基因组学嵌入,得到可迁移的融合 backbone。 <!-- EN --> Unsupervised multimodal pretraining that aligns pathology and genomics embeddings into a transferable fused backbone.
- <!-- ZH --> 微调阶段"模态灵活":多模态或单模态输入都可用,缓解临床缺模态问题。 <!-- EN --> Modality-flexible finetuning: works with multi- or single-modal input, mitigating missing-modality settings.
- <!-- ZH --> 提供跨数据集迁移(COAD→READ)与 data-efficient 微调选项;附带 45+ 篇病理-基因组学多模态方法的持续更新文献表。 <!-- EN --> Cross-dataset transfer (COAD→READ) and data-efficient finetuning options; ships a continually-updated table of 45+ pathology-genomics multimodal methods.

## 局限 / Limitations
- <!-- ZH --> 仅在结直肠癌(COAD/READ)+ miRNA 上验证,泛化到其它癌种/组学未在仓库展示。 <!-- EN --> Validated only on colorectal (COAD/READ) + miRNA; generalization to other cancers/omics not shown in-repo.
- <!-- ZH --> 特征提取依赖旧的 ImageNet-ResNet(非病理基础模型如 UNI/CONCH),表征上限受限。 <!-- EN --> Feature extraction relies on legacy ImageNet-ResNet rather than pathology foundation models (UNI/CONCH), capping representation quality.
- <!-- ZH --> 任务是生存预测,非异常检测/空间定位;README 无数值结果、无预训练 checkpoint,复现需自行下载 TCGA 并跑完整预处理。 <!-- EN --> Task is survival prediction, not anomaly detection/spatial localization; README has no numeric results and no released checkpoint, so reproduction requires downloading TCGA and running full preprocessing.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 处在"virtual tissue / 多模态表征建模"这一环,而非 anomaly detection 或 gene-revert 环。价值在于它提供了一个"病理图像 ⟷ 基因组学"配对与融合的完整工程范式:如何把 WSI patch 特征与分子特征在同一 Transformer 里对齐,得到可迁移嵌入。对我们的 virtual tissue 建模而言,这套多模态预训练+模态灵活微调的思路可直接借用——尤其"缺模态仍可推断"契合真实空间组学常缺配对基因表达的场景。但它不做扰动/异常建模,也不预测"哪个基因被调控能逆转异常";要对接 gene-revert 环,需把其融合表征改造成对扰动敏感的、可反事实生成的模型。可复用为 baseline / 表征对齐组件,而非现成的 revert 引擎。
<!-- EN --> It sits at the "virtual tissue / multimodal representation modelling" stage, not the anomaly-detection or gene-revert stages. Its value is a complete engineering recipe for pairing and fusing pathology-image with genomics: aligning WSI patch features and molecular features inside one Transformer to yield transferable embeddings. For our virtual-tissue modelling, the multimodal-pretraining + modality-flexible-finetuning idea transfers directly — the "infer even when a modality is missing" property fits real spatial-omics where paired expression is often absent. However, it does no perturbation/anomaly modelling and does not predict which gene, if modulated, reverts an anomaly; connecting it to the gene-revert stage would require reworking its fused representation into a perturbation-sensitive, counterfactually-generative model. Reusable as a baseline / representation-alignment component, not a ready-made revert engine.

## 可复用资产 / Reusable assets
- <!-- ZH --> 代码 / Code: <https://github.com/Cassie07/PathOmics> — `bash_main.py`(COAD)、`bash_main_read.py`(COAD→READ 迁移)、`split_tiles_utils/helper.py`(切 patch + 提特征)。
- <!-- ZH --> 数据 / Data: TCGA-COAD/READ WSIs;基因组学 miRNA 来自 cBioPortal `coadread_tcga_pan_can_atlas_2018`。仓库不含预处理产物。
- <!-- ZH --> 评测协议 / Eval protocol: COAD 4 折 CV + hold-out;COAD→READ 5 折迁移;data-efficient 微调 (`--less_data`,`--finetune_test_ratio`)。生存预测用 scikit-survival(C-index 类指标)。
- <!-- ZH --> 文献表 / Lit table: 仓库末尾 45+ 篇病理-基因组学多模态方法(PORPOISE、MCAT、SurvPath、TANGLE、MOTCat、CMTA、POMP 等)带代码链接,可作调研入口。
- <!-- ZH --> Checkpoint: README 未提供公开预训练权重(`--load_model_finetune` 假定你自己已训练保存)。

## 待读 / Follow-ups
- <!-- ZH --> 读原论文 https://rdcu.be/dnwKf,拿到具体 C-index 与消融(单模态 vs 多模态、GAP、融合方式)。 <!-- EN --> Read the paper for exact C-index and ablations (single- vs multimodal, GAP, fusion type).
- <!-- ZH --> 对比 SurvPath / TANGLE(CVPR 2024)——用 pathway / transcriptomics 引导的更强表征,评估替换 ResNet 特征为病理基础模型(UNI/CONCH)的收益。 <!-- EN --> Compare with SurvPath / TANGLE (CVPR 2024) and assess replacing ResNet features with pathology foundation models (UNI/CONCH).
- <!-- ZH --> 评估把其融合嵌入接入我们的 anomaly-detection / counterfactual gene-revert 流程的可行性。 <!-- EN --> Evaluate wiring its fused embeddings into our anomaly-detection / counterfactual gene-revert pipeline.

## 引用 / Cite
```bibtex
@inproceedings{ding2023pathology,
  title={Pathology-and-genomics multimodal transformer for survival outcome prediction},
  author={Ding, Kexin and Zhou, Mu and Metaxas, Dimitris N and Zhang, Shaoting},
  booktitle={International Conference on Medical Image Computing and Computer-Assisted Intervention},
  pages={622--631},
  year={2023},
  organization={Springer}
}
```


---

📄 **[AI-ready 全文/full-text extract →](ai-ready.md)**
