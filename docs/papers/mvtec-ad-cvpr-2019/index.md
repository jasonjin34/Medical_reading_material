# MVTec AD — A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection

> **Bibkey** `Bergmann_2019` · **Venue** 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) (2019) · **Category** anomaly · **Relevance** medium · **Access** open
> **Link** <https://doi.org/10.1109/cvpr.2019.00982> · `status: complete`

---

## One-liner
MVTec AD is the first unsupervised anomaly-detection dataset aimed at real industrial inspection with multiple objects, multiple defect types and **pixel-precise ground truth**: 15 categories (5 textures + 10 objects), 5,354 high-resolution images, 73 defect types and 1,888 hand-annotated anomalous regions, with defect-free images only in training. The paper also benchmarks AnoGAN, L2/SSIM autoencoders, a CNN feature dictionary, a GMM texture model and a variation model, concluding that no method works well on every category. It became the standard benchmark for virtually all visual AD methods since, including PaDiM, PatchCore, DRÆM and CFLOW-AD.

## Problem
Evaluation of anomaly/novelty detection mostly relabelled arbitrary classes of MNIST, CIFAR-10 or ImageNet as outliers — outliers far from the training distribution — which says nothing about real anomalies that are **very close to the training data and differ only subtly in small regions**; the few datasets supporting segmentation (NanoTWICE: 45 images of one texture; DAGM 2007: synthetic textures with coarse ellipse labels) were small and low in diversity. The authors argue AD lacked a dataset playing the role ImageNet plays for classification.

## Method
**Acquisition**: a 2048×2048 industrial RGB sensor with two bilateral telecentric lenses (1:5 and 1:1 magnification) under highly controlled illumination (deliberately varied for some classes), cropped to 700²–1024²; grid, screw and zipper are grey-scale only. Some objects are roughly aligned (toothbrush, capsule, pill), others randomly rotated (metal nut, screw, hazelnut). Defects were **manually produced** to realistically mimic production defects: surface defects (scratches, dents), structural defects (distorted parts), missing parts, etc. **Benchmark protocol**: every method outputs a one-channel anomaly map; the authors propose setting the threshold **from anomaly-free validation images only** — per category, a minimum defect area is defined and the threshold raised on the validation set until the largest connected "anomalous" region falls just below that area. **Metrics**: per-image classification accuracy for defect-free and defective images separately; for segmentation, per-region overlap (PRO) at that threshold plus threshold-free pixel ROC AUC. **Baselines**: AnoGAN (300 iterations of latent search), L2 and SSIM convolutional autoencoders (128×128 texture patches; 256×256 objects), a CNN feature dictionary (ResNet-18 avgpool + PCA + k-means, after Napoletano et al.), a GMM-based texture inspection model (HALCON implementation) and a variation model (per-pixel mean/variance, needs shape-based alignment). Deep methods are augmented to 10,000 training patches per category.

## Method lineage
A **dataset/benchmark**, not a method; its baselines span the two main 2019 paradigms — **reconstruction/generative** (AnoGAN, L2/SSIM-AE) and **feature-embedding** (pretrained CNN features + clustering) — plus classical **density / one-class** models (GMM texture model, per-pixel Gaussian variation model). **Builds on**: Schlegl et al.'s AnoGAN (explicitly the GAN baseline), Bergmann et al.'s SSIM-AE, Napoletano et al.'s CNN feature dictionary. **Led to**: it is the main benchmark of every mainstream visual AD paper since — PaDiM, PatchCore, DRÆM and CFLOW-AD all report headline results on it; PaDiM derives a misaligned variant (Rd-MVTec AD) from it; by PatchCore image AUROC exceeds 99%, i.e. the benchmark is essentially saturated. The PRO metric also became the standard localization metric.

## Data
**Scale**: 3,629 training/validation images (all defect-free) + 1,725 test images (467 defect-free + 1,258 defective); 60–391 training images per category (toothbrush fewest at 60, hazelnut most at 391); 1–8 defect groups per category, 73 in total; 1,888 defect regions overall. **Textures**: carpet, grid (regular), leather, tile, wood (random). **Objects**: bottle, cable, capsule, hazelnut, metal nut, pill, screw, toothbrush, transistor, zipper. **License**: CC BY-NC-SA 4.0 (non-commercial; per the MVTec website).

## Key results
- **No winner**: no method performs consistently well across all object and texture classes. On textures there is no clear winner, with the CNN feature dictionary most consistent by ROC AUC; on objects the L2 / SSIM autoencoders are best, which one depending on the object.
- **High AUC ≠ good segmentation**: even with high pixel ROC AUC, PRO at the threshold estimated from defect-free validation images can be very low (e.g., on bottle the four deep methods reach PRO of only 0.05–0.22 while ROC AUC is 0.78–0.93) — showing that **setting thresholds from normal samples alone** is itself a hard problem.
- **Failure modes**: AnoGAN suffers mode collapse, barely reconstructing objects with variable shape/orientation and failing completely on carpet; autoencoders blur high-frequency textures (tile, zipper) with many false positives; the CNN feature dictionary lacks spatial information and degrades on objects; the GMM texture model is grey-scale only and misses colour defects; the variation model needs exact alignment, so the randomly placed imprint on capsule is always flagged as a defect.

## Contributions
- The first multi-category, multi-defect, pixel-annotated, application-oriented unsupervised AD dataset.
- A thresholding protocol **using defect-free validation images only**, and use of the PRO metric — which became the standard localization metric.
- A cross-paradigm initial benchmark that exposes concrete failure modes of each method family.

## Limitations
- Defects are manually produced and acquisition is highly controlled (telecentric lenses, controlled light), unlike real production variability; few training images per class (60–391).
- Only local appearance/structural defects; no "logical anomalies" (wrong count/arrangement of parts) — addressed later by MVTec LOCO (not part of this paper).
- Later methods push image AUROC beyond 99%, so the benchmark is near-saturated and discriminates less; and pathology-ad-bench-mlhealth-2025 shows MVTec success does not transfer to pathology (industrial mean ROC-AUC 0.888 vs real pathology 0.645).
- Non-commercial license limits industrial use.

## Relation to our direction
For the artifact-injection topic, MVTec AD is **both the design template and a cautionary tale for KidneyAnomalyBench**. **What to borrow**: (1) the structure "normal-only training, normal + anomalous test, region-level ground truth for anomalies" — i.e., healthy-reference training, the kidney samples to be tested as the test set, expert-annotated lesions (glomerulosclerosis, interstitial fibrosis, tubular atrophy, inflammatory infiltrate) as region-level truth; (2) the **threshold-from-normal-validation-only** protocol — kidney data also lack known anomalies for tuning, and the paper's "high AUC but poor thresholded segmentation" will be worse in omics, so KidneyAnomalyBench should report both threshold-free metrics (AUROC/AP) and region overlap at a fixed-protocol threshold; (3) **per-category reporting** — MVTec's "no method wins every category" translates into reporting per anatomical unit / cell type / lesion type rather than one global AUC. **What breaks**: (1) MVTec's "normal" is a tightly controlled single product, whereas healthy kidney is itself heterogeneous (cortex/medulla, tubular segments, age-related change) and "healthy donors" are not fully healthy; (2) MVTec anomalies are **discrete, local** defects, while kidney disease is a **continuous, diffuse** spectrum that binary pixel masks cannot express — graded labels (e.g., IFTA severity) or continuous damage scores are needed (the PDS/HDS of damage-scores-cellgenomics-2026 could serve as continuous pseudo-truth); (3) MVTec has almost no "technical artifact vs true anomaly" confusion, whereas in omics ambient RNA, doublets, segmentation errors and batch effects all register as "anomalies" — KidneyAnomalyBench should include an explicit **artifact-type anomaly** class and require methods to separate it from disease, which is precisely where the artifact-injection topic's cross-modal agreement gets evaluated; (4) pixel masks do not exist for snRNA/snATAC and can only be approximated on Xenium/H&E spatial data. **Existing repo papers with the same idea**: pathology-ad-bench-mlhealth-2025 uses MVTec Hazelnut and Tile as industrial references against Camelyon16, Crohn's colon and mouse glomeruli and directly quantifies the industrial→pathology performance cliff; medianomaly-media-2025 is the medical-imaging counterpart unified AD benchmark (7 datasets, 30 methods); nih-kidney-ai-challenge-2026 is a possible external benchmark outlet on the kidney side.

## Reusable assets
- **Data:** MVTec AD download and evaluation code (CC BY-NC-SA 4.0).
<https://www.mvtec.com/research-teaching/datasets/mvtec-ad>
- **Eval protocol:** threshold estimation from defect-free validation images and a minimum defect area; the PRO (per-region overlap) metric — adaptable to per-cell / per-region metrics in KidneyAnomalyBench.
- **Library:** anomalib ships MVTec AD loaders and PRO computation.
<https://github.com/open-edge-platform/anomalib>

## Follow-ups
- The IJCV 2021 journal extension of MVTec AD (fuller baselines and metric discussion) and MVTec LOCO (logical anomalies).
- anogan-ipmi-2017 (this paper's GAN baseline) and Bergmann et al.'s SSIM-AE (VISAPP 2019).
- Draft an "MVTec-style" data card for KidneyAnomalyBench: normal-reference sources, test composition, region-truth types, artifact class, thresholding protocol.

## Cite
```bibtex
@inproceedings{Bergmann_2019, title={MVTec AD — A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection}, url={http://dx.doi.org/10.1109/CVPR.2019.00982}, DOI={10.1109/cvpr.2019.00982}, booktitle={2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)}, publisher={IEEE}, author={Bergmann, Paul and Fauser, Michael and Sattlegger, David and Steger, Carsten}, year={2019}, month=June, pages={9584–9592} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
