# Benchmarking the translational potential of spatial gene expression prediction from histology

> **Bibkey** `Wang_2025_HE2Expr` · **Venue** Nature Communications (2025) · **Category** histopath · **Relevance** medium · **Access** open
> **Link** <https://doi.org/10.1038/s41467-025-56618-y> · `status: complete`

---

## One-liner
An independent reproduction and evaluation of 11 methods that predict spatial gene expression (SGE) from H&E: 5 SRT datasets plus TCGA-BRCA external validation, 28 metrics spanning accuracy, generalisability, clinical translation (survival), usability and compute. No method wins everywhere; all-gene mean correlation is typically < 0.25, more complex architectures are not better, and survival stratification is mostly non-significant under cross-validation.

## Problem
If spatial expression could be inferred from routine H&E, existing pathology archives would gain huge molecular value. But these methods appeared only in the last ~3 years and are almost always self-evaluated with inconsistent protocols (TCGA tests, ablations, backbone comparisons); there was no unified independent comparison and no critical assessment of image quality, resolution or translational value.

## Method
**Methods (11)**: ST-Net (DenseNet121), HisToGene (ViT + super-resolution), DeepPT (ResNet50 + AE + MLP), Hist2ST (ConvMixer + GraphSAGE + Transformer), DeepSpaCE (VGG16), GeneCodeR (non-deep), EGNv1 (ViT + exemplar), EGNv2 (exemplar + GCN), TCGN (CNN + ViT + GNN), THItoGene (dynamic conv + capsule + GAT + ViT), iStar (HViT, near-single-cell super-resolution). **Five categories**: (1) within-study SGE prediction (ST and Visium, 4-fold CV; PCC, MI, SSIM, AUC, JS divergence, NRMSE etc., stratified into all genes, HVGs, SVGs and high-sparsity genes HSGs); (2) cross-study generalisation (ST→Visium, across breast-cancer subtypes, ST-trained models → TCGA images via patient-level pseudobulk vs bulk RNA-seq correlation); (3) clinical translation (dependence on HistoQC image quality; Cox survival from predicted pseudobulk, C-index and log-rank, 3-fold CV × 100 repeats); (4) usability score (8 weighted aspects, max 31); (5) compute efficiency.

## Data
HER2+ breast-cancer ST (Andersson et al.), cutaneous SCC ST (GSE144240), 10x Visium: Visium-HER2+ (two Block A sections), Visium-Hercep-Test2+, **Visium-Kidney (10x healthy human kidney FFPE)**; external: TCGA-BRCA (671 images; HER2+ 92, luminal 463, TNBC 79 patients for survival).

## Key results
- **Best on ST: EGNv2** — PCC 0.28, MI 0.06, SSIM 0.22, AUC 0.65; all methods' all-gene mean correlation < 0.25. Correlation and SSIM are significantly higher on HVGs/SVGs, which the authors advocate as the primary evaluation. Predictions separate >10 vs <10 counts at AUC 0.65 but zero vs non-zero only at 0.57; higher zero fraction → lower correlation.
- **Architecture**: patch-only CNN methods (EGNv2, ST-Net, DeepPT) cluster together and perform best; adding neighbourhood/whole-slide global context does not help (spot spacing 150–200 μm ST, 100 μm Visium; neighbouring spots are weakly correlated).
- **Healthy-kidney Visium**: DeepPT best (HVG mean r 0.45, SVG 0.47), then ST-Net (0.31/0.36) and EGNv1 (0.25/0.24) — attributed to low heterogeneity, where a single patch suffices. Several methods produce near-constant predictions on Visium (linked to denser Visium expression).
- **Generalisation**: cross-subtype and cross-resolution transfer degrades markedly; only HisToGene transfers ST→Visium. TCGA patient-level correlation: HisToGene and EGNv2 mean 0.53, DeepSpaCE 0.52 … ST-Net 0.33. DeepPT's performance correlates strongly with image quality (r = 0.53); HisToGene (0.05) and Hist2ST (0.19) barely depend on it.
- **Survival**: C-indices are close to bulk RNA-seq but low (e.g. HER2+ DeepPT 0.55 vs RNA-seq 0.58; TNBC Hist2ST 0.58 vs 0.57); KM separation is significant on training predictions but largely vanishes under CV — only DeepSpaCE (p = 0.028), with Hist2ST and ST-Net borderline. Not yet ready for clinical translation.
- **Usability**: best Hist2ST 18.8/31, mean 15.1 (excluding DeepPT, which had no code and scored 2); no method has unit tests.

## Contributions
- The first independent, unified reproduction of 11 H&E→SGE methods: 28 metrics in five dimensions.
- Argues all-gene mean correlation is misleading; evaluation should focus on HVGs/SVGs.
- Adds image-quality dependence, cross-resolution transfer and CV-based survival stratification, showing that training-set "significant" translational claims vanish under CV.
- Open-source benchmark pipeline.

## Limitations
- Mostly breast cancer; kidney is a single healthy Visium section; subcellular platforms like Xenium are not covered.
- Does not include newer pathology-foundation-model approaches (UNI, CONCH, OmiCLIP etc.); methods frozen at assessment time.
- Survival uses only pseudobulk, ignoring spatial information; usability scoring is partly subjective.

## Relation to our direction
For the artifact-injection topic this is the sober baseline for "how far can H&E stand in for, or check, molecular modalities." To predict expression from H&E and compare against measured Xenium/snRNA as a cross-modal agreement test, one must first know how unreliable the prediction is — all-gene correlation < 0.25, meaningful signal only on HVGs/SVGs, almost none for zero-inflated genes. So **H&E↔expression disagreement thresholds must be stratified by per-gene predictability**, otherwise most disagreement is prediction noise, not artefact or disease. The good news: on healthy-kidney Visium DeepPT reaches r = 0.45–0.47 on HVG/SVG, suggesting that in low-heterogeneity kidney tissue a single patch carries enough information for a "healthy morphology vs expression" normal model. The image-quality dependence (DeepPT r = 0.53) is a reminder that H&E quality is itself an artefact source to model separately. For the agent-trustworthiness topic, the "significant on training, non-significant under CV" survival result is exactly the over-claim agents tend to repeat — a ready example for claim-to-evidence verification and rerun-stability tests; "evaluate on HVG/SVG, not all genes" can go into omics-specific evaluation rules.

## Reusable assets
- **Benchmark code** (Apache-2.0):
<https://github.com/SydneyBioX/HEtoSGEBench> · Zenodo 10.5281/zenodo.14602489
- **Healthy human kidney Visium FFPE** (10x public dataset), usable as an artifact-injection-topic H&E↔expression normal reference:
<https://www.10xgenomics.com/datasets/human-kidney-11-mm-capture-area-ffpe-2-standard>
- **Evaluation recipe**: HVG/SVG/HSG stratification, HistoQC quality dependence, CV×100 survival evaluation, usability rubric.

## Follow-ups
- HEST-1k (`hest1k-2024`) and OmiCLIP/Loki (`loki-omiclip-natmethods-2025`) — foundation-model-era H&E→expression; does it break this paper's 0.25 ceiling?
- iStar and Xenium-resolution prediction methods.

## Cite
```bibtex
@article{Wang_2025_HE2Expr, title={Benchmarking the translational potential of spatial gene expression prediction from histology}, volume={16}, ISSN={2041-1723}, url={http://dx.doi.org/10.1038/s41467-025-56618-y}, DOI={10.1038/s41467-025-56618-y}, number={1}, journal={Nature Communications}, publisher={Springer Science and Business Media LLC}, author={Wang, Chuhan and Chan, Adam S. and Fu, Xiaohang and Ghazanfar, Shila and Kim, Jinman and Patrick, Ellis and Yang, Jean Y. H.}, year={2025}, month=Feb }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
