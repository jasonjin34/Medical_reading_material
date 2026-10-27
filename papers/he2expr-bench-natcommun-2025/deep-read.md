# Benchmarking the translational potential of spatial gene expression prediction from histology

> **Bibkey** `Wang_2025_HE2Expr` · **Venue** Nature Communications (2025) · **Category** histopath · **Relevance** medium · **Access** open
> **Link** <https://doi.org/10.1038/s41467-025-56618-y>
> `status: complete` — 基于 Europe PMC 开放全文(PMC11814321)精读。
> Bilingual convention (drives the site's EN⇄中文 switcher): put `<!-- ZH -->` 中文 and `<!-- EN -->` English on their own lines (or inline `- <!-- ZH --> 中文 <!-- EN --> English`). Use `<!-- ZH/EN -->` ONLY for a purely language-neutral line (a bare URL or code token) — never for bilingual prose or labels.

---

## 一句话 / One-liner
<!-- ZH --> 对 11 个「从 H&E 预测空间基因表达(SGE)」的方法做独立复现与评测:5 个 SRT 数据集 + TCGA-BRCA 外部验证,28 个指标覆盖预测精度、泛化、临床转化(生存)、可用性与计算效率;结论是没有一个方法全面最优,全基因平均相关性普遍 < 0.25,复杂架构并不更好,且在交叉验证下生存分层基本不显著。
<!-- EN --> An independent reproduction and evaluation of 11 methods that predict spatial gene expression (SGE) from H&E: 5 SRT datasets plus TCGA-BRCA external validation, 28 metrics spanning accuracy, generalisability, clinical translation (survival), usability and compute. No method wins everywhere; all-gene mean correlation is typically < 0.25, more complex architectures are not better, and survival stratification is mostly non-significant under cross-validation.

## 研究问题 / Problem
<!-- ZH --> 从常规 H&E 推断空间表达若可行,将大幅放大现有病理档案的分子信息。但这些方法近 3 年才出现,几乎都只由开发者自评,评测框架各不相同(有的测 TCGA、有的做消融、有的比 backbone),缺乏统一、独立的比较,也缺少对图像质量、分辨率、转化价值的批判性评估。
<!-- EN --> If spatial expression could be inferred from routine H&E, existing pathology archives would gain huge molecular value. But these methods appeared only in the last ~3 years and are almost always self-evaluated with inconsistent protocols (TCGA tests, ablations, backbone comparisons); there was no unified independent comparison and no critical assessment of image quality, resolution or translational value.

## 方法 / Method
<!-- ZH --> **被测方法(11 个)**:ST-Net(DenseNet121)、HisToGene(ViT + super-resolution)、DeepPT(ResNet50 + AE + MLP)、Hist2ST(ConvMixer + GraphSAGE + Transformer)、DeepSpaCE(VGG16)、GeneCodeR(非深度学习)、EGNv1(ViT + exemplar)、EGNv2(exemplar + GCN)、TCGN(CNN + ViT + GNN)、THItoGene(动态卷积 + capsule + GAT + ViT)、iStar(HViT,近单细胞超分辨)。**五类评测**:(1) 同一研究内的 SGE 预测(ST 与 Visium,4 折 CV;PCC、MI、SSIM、AUC、JS 散度、NRMSE 等,并区分全基因、HVG、SVG、高稀疏基因 HSG);(2) 跨研究泛化(ST→Visium、跨乳腺癌亚型、ST 训练模型→TCGA 图像 pseudobulk 与 bulk RNA-seq 的患者级相关);(3) 临床转化(HistoQC 图像质量对性能的依赖;用预测 pseudobulk 做 Cox 生存模型,C-index 与 log-rank,3 折 CV × 100 次重复);(4) 可用性评分(8 个方面加权,满分 31);(5) 计算效率。
<!-- EN --> **Methods (11)**: ST-Net (DenseNet121), HisToGene (ViT + super-resolution), DeepPT (ResNet50 + AE + MLP), Hist2ST (ConvMixer + GraphSAGE + Transformer), DeepSpaCE (VGG16), GeneCodeR (non-deep), EGNv1 (ViT + exemplar), EGNv2 (exemplar + GCN), TCGN (CNN + ViT + GNN), THItoGene (dynamic conv + capsule + GAT + ViT), iStar (HViT, near-single-cell super-resolution). **Five categories**: (1) within-study SGE prediction (ST and Visium, 4-fold CV; PCC, MI, SSIM, AUC, JS divergence, NRMSE etc., stratified into all genes, HVGs, SVGs and high-sparsity genes HSGs); (2) cross-study generalisation (ST→Visium, across breast-cancer subtypes, ST-trained models → TCGA images via patient-level pseudobulk vs bulk RNA-seq correlation); (3) clinical translation (dependence on HistoQC image quality; Cox survival from predicted pseudobulk, C-index and log-rank, 3-fold CV × 100 repeats); (4) usability score (8 weighted aspects, max 31); (5) compute efficiency.

## 数据 / Data
<!-- ZH --> HER2+ 乳腺癌 ST(Andersson et al.)、皮肤 cSCC ST(GSE144240)、10x Visium:Visium-HER2+(Block A 两切片)、Visium-Hercep-Test2+、**Visium-Kidney(10x 健康人肾 FFPE)**;外部:TCGA-BRCA(671 张图像;HER2+ 92、luminal 463、TNBC 79 例用于生存)。
<!-- EN --> HER2+ breast-cancer ST (Andersson et al.), cutaneous SCC ST (GSE144240), 10x Visium: Visium-HER2+ (two Block A sections), Visium-Hercep-Test2+, **Visium-Kidney (10x healthy human kidney FFPE)**; external: TCGA-BRCA (671 images; HER2+ 92, luminal 463, TNBC 79 patients for survival).

## 主要结果 / Key results
- <!-- ZH --> **ST 数据整体最佳 EGNv2**:PCC 0.28、MI 0.06、SSIM 0.22、AUC 0.65;所有方法的全基因平均相关 < 0.25。HVG/SVG 上相关性和 SSIM 显著高于全基因,作者主张以 HVG/SVG 为主要评测口径。预测值对「>10 vs <10 counts」的区分 AUC 0.65,对「零 vs 非零」仅 0.57;基因零比例越高相关性越低。 <!-- EN --> **Best on ST: EGNv2** — PCC 0.28, MI 0.06, SSIM 0.22, AUC 0.65; all methods' all-gene mean correlation < 0.25. Correlation and SSIM are significantly higher on HVGs/SVGs, which the authors advocate as the primary evaluation. Predictions separate >10 vs <10 counts at AUC 0.65 but zero vs non-zero only at 0.57; higher zero fraction → lower correlation.
- <!-- ZH --> **架构**:只看单 spot patch 的 CNN 类(EGNv2、ST-Net、DeepPT)聚为一类且表现最好;引入邻域/全片全局信息的方法并不更优(spot 间距 ST 150–200 μm、Visium 100 μm,邻域相关不强)。 <!-- EN --> **Architecture**: patch-only CNN methods (EGNv2, ST-Net, DeepPT) cluster together and perform best; adding neighbourhood/whole-slide global context does not help (spot spacing 150–200 μm ST, 100 μm Visium; neighbouring spots are weakly correlated).
- <!-- ZH --> **健康肾 Visium**:DeepPT 最好(HVG 平均相关 0.45、SVG 0.47),其次 ST-Net(0.31/0.36)、EGNv1(0.25/0.24);作者归因于低异质性组织中单 patch 信息已足够。多种方法在 Visium 上预测几乎无空间变化(与 Visium 表达更稠密有关)。 <!-- EN --> **Healthy-kidney Visium**: DeepPT best (HVG mean r 0.45, SVG 0.47), then ST-Net (0.31/0.36) and EGNv1 (0.25/0.24) — attributed to low heterogeneity, where a single patch suffices. Several methods produce near-constant predictions on Visium (linked to denser Visium expression).
- <!-- ZH --> **泛化**:跨亚型、跨分辨率迁移普遍明显变差;ST→Visium 只有 HisToGene 有效。TCGA 患者级相关:HisToGene、EGNv2 均值 0.53、DeepSpaCE 0.52 … ST-Net 0.33。DeepPT 性能与图像质量强相关(r = 0.53),HisToGene(0.05)、Hist2ST(0.19)基本不受影响。 <!-- EN --> **Generalisation**: cross-subtype and cross-resolution transfer degrades markedly; only HisToGene transfers ST→Visium. TCGA patient-level correlation: HisToGene and EGNv2 mean 0.53, DeepSpaCE 0.52 … ST-Net 0.33. DeepPT's performance correlates strongly with image quality (r = 0.53); HisToGene (0.05) and Hist2ST (0.19) barely depend on it.
- <!-- ZH --> **生存**:C-index 与 bulk RNA-seq 接近但都很低(如 HER2+ DeepPT 0.55 vs RNA-seq 0.58;TNBC Hist2ST 0.58 vs 0.57);在训练集上 KM 分离显著,但在 CV 下基本不显著,仅 DeepSpaCE(p = 0.028)及 Hist2ST、ST-Net 边缘显著 —— 作者结论是尚未准备好临床转化。 <!-- EN --> **Survival**: C-indices are close to bulk RNA-seq but low (e.g. HER2+ DeepPT 0.55 vs RNA-seq 0.58; TNBC Hist2ST 0.58 vs 0.57); KM separation is significant on training predictions but largely vanishes under CV — only DeepSpaCE (p = 0.028), with Hist2ST and ST-Net borderline. Not yet ready for clinical translation.
- <!-- ZH --> **可用性**:最高 Hist2ST 18.8/31,均值 15.1(不含 DeepPT,其无公开代码仅得 2);所有方法都没有单元测试。 <!-- EN --> **Usability**: best Hist2ST 18.8/31, mean 15.1 (excluding DeepPT, which had no code and scored 2); no method has unit tests.

## 创新点 / Contributions
- <!-- ZH --> 第一个独立、统一复现 11 个 H&E→SGE 方法的基准,28 个指标、五个维度。 <!-- EN --> The first independent, unified reproduction of 11 H&E→SGE methods: 28 metrics in five dimensions.
- <!-- ZH --> 提出「全基因平均相关」是误导性指标,应聚焦 HVG/SVG。 <!-- EN --> Argues all-gene mean correlation is misleading; evaluation should focus on HVGs/SVGs.
- <!-- ZH --> 把图像质量依赖、跨分辨率泛化、CV 下生存分层纳入评测,揭示「训练集上显著」的转化结论在 CV 下消失。 <!-- EN --> Adds image-quality dependence, cross-resolution transfer and CV-based survival stratification, showing that training-set "significant" translational claims vanish under CV.
- <!-- ZH --> 开源 benchmark 流水线。 <!-- EN --> Open-source benchmark pipeline.

## 局限 / Limitations
- <!-- ZH --> 数据以乳腺癌为主,肾只有一张健康 Visium;未涵盖 Xenium 等亚细胞分辨率平台。 <!-- EN --> Mostly breast cancer; kidney is a single healthy Visium section; subcellular platforms like Xenium are not covered.
- <!-- ZH --> 未纳入基于病理基础模型(UNI、CONCH、OmiCLIP 等)的新一代方法;方法版本截至评测时。 <!-- EN --> Does not include newer pathology-foundation-model approaches (UNI, CONCH, OmiCLIP etc.); methods frozen at assessment time.
- <!-- ZH --> 生存分析只用 pseudobulk,不利用空间信息;可用性评分有一定主观性。 <!-- EN --> Survival uses only pseudobulk, ignoring spatial information; usability scoring is partly subjective.

## 与本研究方向的关系 / Relation to our direction
<!-- ZH --> 对课题 1,这篇是「H&E 能在多大程度上代替/校验分子模态」的冷静基线:若想用 H&E 预测表达,再与 Xenium/snRNA 实测比较来做跨模态一致性检验,就必须先知道「预测本身有多不靠谱」—— 全基因相关 < 0.25,只有 HVG/SVG 上才有意义的信号,且对零膨胀基因几乎无能为力。这意味着 **H&E↔表达不一致的阈值必须按基因可预测性分层**,否则大量不一致只是预测噪声而非伪影或病变。好消息是:健康肾 Visium 上 DeepPT 对 HVG/SVG 的相关达 0.45–0.47,说明肾这种低异质性组织里单 patch 信息较充分,适合做「健康外观 vs 表达」的正常模型。图像质量依赖(DeepPT r = 0.53)提醒我们:H&E 质量本身就是一个需要单独建模的伪影源。对课题 2,「训练集上显著、CV 下不显著」的生存结论是 agent 最容易复述的过度结论,是 claim-to-evidence 校验与 rerun 稳定性测试的现成范例;「用 HVG/SVG 而非全基因评价」也可写入组学特异的评测规范。
<!-- EN --> For Topic 1 this is the sober baseline for "how far can H&E stand in for, or check, molecular modalities." To predict expression from H&E and compare against measured Xenium/snRNA as a cross-modal agreement test, one must first know how unreliable the prediction is — all-gene correlation < 0.25, meaningful signal only on HVGs/SVGs, almost none for zero-inflated genes. So **H&E↔expression disagreement thresholds must be stratified by per-gene predictability**, otherwise most disagreement is prediction noise, not artefact or disease. The good news: on healthy-kidney Visium DeepPT reaches r = 0.45–0.47 on HVG/SVG, suggesting that in low-heterogeneity kidney tissue a single patch carries enough information for a "healthy morphology vs expression" normal model. The image-quality dependence (DeepPT r = 0.53) is a reminder that H&E quality is itself an artefact source to model separately. For Topic 2, the "significant on training, non-significant under CV" survival result is exactly the over-claim agents tend to repeat — a ready example for claim-to-evidence verification and rerun-stability tests; "evaluate on HVG/SVG, not all genes" can go into omics-specific evaluation rules.

## 可复用资产 / Reusable assets
- <!-- ZH --> **Benchmark 代码**(Apache-2.0): <!-- EN --> **Benchmark code** (Apache-2.0):
<!-- ZH/EN --> <https://github.com/SydneyBioX/HEtoSGEBench> · Zenodo 10.5281/zenodo.14602489
- <!-- ZH --> **健康人肾 Visium FFPE**(10x 公共数据集),可作为课题 1 的 H&E↔表达正常参考: <!-- EN --> **Healthy human kidney Visium FFPE** (10x public dataset), usable as a Topic 1 H&E↔expression normal reference:
<!-- ZH/EN --> <https://www.10xgenomics.com/datasets/human-kidney-11-mm-capture-area-ffpe-2-standard>
- <!-- ZH --> **评测规范**:HVG/SVG/HSG 分层、HistoQC 质量依赖、CV×100 生存评估、可用性评分表。 <!-- EN --> **Evaluation recipe**: HVG/SVG/HSG stratification, HistoQC quality dependence, CV×100 survival evaluation, usability rubric.

## 待读 / Follow-ups
- <!-- ZH --> HEST-1k(`hest1k-2024`)与 OmiCLIP/Loki(`loki-omiclip-natmethods-2025`):基础模型时代的 H&E→表达,看是否突破本文的 0.25 天花板。 <!-- EN --> HEST-1k (`hest1k-2024`) and OmiCLIP/Loki (`loki-omiclip-natmethods-2025`) — foundation-model-era H&E→expression; does it break this paper's 0.25 ceiling?
- <!-- ZH --> iStar 与 Xenium 级别的预测方法。 <!-- EN --> iStar and Xenium-resolution prediction methods.

## 引用 / Cite
```bibtex
@article{Wang_2025_HE2Expr, title={Benchmarking the translational potential of spatial gene expression prediction from histology}, volume={16}, ISSN={2041-1723}, url={http://dx.doi.org/10.1038/s41467-025-56618-y}, DOI={10.1038/s41467-025-56618-y}, number={1}, journal={Nature Communications}, publisher={Springer Science and Business Media LLC}, author={Wang, Chuhan and Chan, Adam S. and Fu, Xiaohang and Ghazanfar, Shila and Kim, Jinman and Patrick, Ellis and Yang, Jean Y. H.}, year={2025}, month=Feb }
```
