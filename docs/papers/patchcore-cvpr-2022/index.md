# Towards Total Recall in Industrial Anomaly Detection (PatchCore)

> **Bibkey** `Roth2021_210608265` · **Venue** 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) (2022) · **Category** anomaly · **Relevance** high · **Access** open
> **Link** <https://arxiv.org/abs/2106.08265> · `status: complete`

---

## One-liner
PatchCore stores **mid-level, neighbourhood-aggregated patch features** of all normal training images in a memory bank, shrinks it to 1–25% with **greedy coreset subsampling** at almost no loss, and scores a test image by the distance of its most anomalous patch to that patch's nearest normal neighbour — 99.1% image AUROC on MVTec AD (up to 99.6% with an ensemble), more than halving PaDiM's error.

## Problem
The **cold-start** problem in industrial inspection: fit using nominal images only, while working well across many product categories automatically. The best methods (SPADE, PaDiM) combined ImageNet features with an outlier detector but had two flaws: (1) deep features are biased toward ImageNet classification and overlap little with industrial defects; (2) the nominal context usable at test time is limited — SPADE relies on an image-level kNN preselection, and PaDiM compares each patch only with same-position statistics, requiring alignment. PatchCore aims to maximize nominal information at test time, reduce ImageNet bias, and keep inference fast.

## Method
**(1) Locally aware patch features**: take **mid-level** features from an ImageNet-pretrained WideResNet-50 (blocks 2 and 3, j ∈ [2,3]) — avoiding both too-generic shallow and too-ImageNet-biased deep features. Each position's feature is aggregated over a p×p neighbourhood (default p = 3) by adaptive average pooling, enlarging the receptive field and adding robustness to small shifts without losing resolution; block-3 features are bilinearly upsampled and concatenated with block 2. The union of all patch features of all nominal images is the memory bank M. **(2) Coreset subsampling**: M is huge and random subsampling loses feature-space coverage, so a minimax facility-location coreset is used — the subset M_C minimizing the maximum distance from any point in M to M_C — approximated greedily (add the point farthest from the current coreset each step), with Johnson–Lindenstrauss random projections to speed up selection. PatchCore-n% keeps n% of the bank. **(3) Scoring**: each test patch finds its nearest neighbour in M; the image score uses the largest such distance s*, reweighted by how rare that neighbour m* is within the bank (if m* is far from its own b nearest neighbours, it is itself a rare nominal sample, so the score is raised). The anomaly map places patch scores back spatially, upsamples bilinearly and smooths with σ = 4. Images need not share a shape, need no alignment, and no training on the target data is required.

## Method lineage
**Paradigm: feature-embedding & memory bank** (the non-parametric kNN version, and the paradigm's flagship). **Builds on**: Bergman et al. 2020 (DN2, kNN on pretrained features), SPADE (multi-layer feature memory bank + kNN segmentation), PaDiM (per-position Gaussian + Mahalanobis); the authors state its components are "most related to SPADE and PaDiM" and replace PaDiM's same-position-only statistics with one bank shared by all patches. The coreset idea comes from active learning (Sener & Savarese) and coreset selection in GAN training. **Led to**: the de-facto standard industrial AD baseline, widely ported to medicine/pathology — pathology-ad-bench-mlhealth-2025 benchmarks it within the feature-distribution family, and virchow-2024's follow-ups propose PatchCore on frozen Virchow embeddings. With CFLOW-AD (same era, same pretrained features, flow density instead) it forms the "non-parametric kNN vs parametric density" contrast.

## Data
**MVTec AD**: 15 sub-datasets, 5354 images, 1725 of them test; resized to 256×256 and centre-cropped to 224×224 with no augmentation (augmentation would need prior knowledge of class-preserving transforms). **Magnetic Tile Defects (MTD)**: 925 defect-free + 392 defective tiles with varied illumination and size; 20% of defect-free images held out for test. **mini ShanghaiTech Campus (mSTC)**: every fifth STC frame, 12 scenes, 256×256.

## Key results
- **Image detection (MVTec AUROC)**: PatchCore-25% **99.1%**, -10% 99.0%, -1% 99.0%, vs PaDiM (task-specific backbone) 97.9%, MahalanobisAD 95.8%, PaDiM 95.3%, DifferNet 94.9%, Patch SVDD 92.1%, SPADE 85.5%. Error drops from 2.1% to 0.9% (−57%); at the F1-optimal threshold only 42 of 1725 images are misclassified and a third of the classes are solved perfectly.
- **Segmentation**: pixel AUROC 98.1% (PaDiM 97.5%, SPADE 96.0%); PRO 93.5% (PaDiM 92.1%, SPADE 91.7%).
- **Larger setups**: PatchCore-1% with a DenseNet-201 & ResNeXt-101 & WRN-101 ensemble at 320 px reaches **99.6%** image AUROC, 98.2% pixel AUROC, 94.9% PRO.
- **Inference time (per image, GPU)**: PatchCore-100% 0.6 s (99.1/98.0/93.3), -10% 0.22 s, -1% 0.17 s (99.0/98.0/93.1); SPADE 0.66 s (85.3/96.6/91.5), PaDiM 0.19 s (95.4/97.3/91.8); PatchCore-100% + IVFPQ approximate NN 0.2 s but image AUROC falls to 98.0.
- **Ablations**: neighbourhood p = 3 is the optimum between locality and global context; blocks 2+3 are best; coreset clearly beats random subsampling and learned proxies; without subsampling <30% of bank entries are ever used at test time, rising to ~95% after a 1% coreset; shrinking the bank via stride 2 / 3 drops image AUROC to 97.6% / 96.8%.
- **Other benchmarks & low-shot**: mSTC pixel AUROC 91.8% (PaDiM 91.2%); MTD image AUROC 97.9% (DifferNet 97.7%); one fifth of the nominal training data already matches the previous state of the art.

## Contributions
- **Mid-level, neighbourhood-aggregated** patch features balancing resolution, context and ImageNet bias.
- **One memory bank shared by all patches**: removes PaDiM's positional binding — no alignment, no fixed input shape.
- **Greedy coreset subsampling**: shrinks the bank by two orders of magnitude at near-constant performance — the key to scaling kNN methods, and the most transferable idea for us.
- Neighbour-rarity score reweighting; high sample efficiency.

## Limitations
- Self-stated: applicability is bounded by the transferability of the pretrained features; combining with feature adaptation is left to future work.
- **Bank contamination**: kNN implicitly assumes the bank is clean; a few anomalies in the training set give anomalous test patches "nominal" neighbours — not discussed in the paper.
- The max-patch image score is sensitive to a single noisy patch; no calibrated threshold or FPR guarantee.
- Evaluation is almost entirely MVTec, which is near-saturated (99%+) and discriminates little for real-world settings.

## Relation to our direction
PatchCore is **the classic AD method most worth porting directly** in Topic 1, because each of its three components has a clean omics analogue. **Mapping**: memory bank = embeddings of all cells/spots in the healthy reference (scVI, scGPT/Geneformer-style foundation models, or spatially aware embeddings like Nicheformer); "local neighbourhood aggregation" of patches = pooling over spatial neighbours in Xenium/Visium (i.e., niche features); test score = distance of a cell to its nearest healthy neighbour; image-level score = the score of the most anomalous cell (or top-k mean) in a biopsy or anatomical region. On the H&E side it ports unchanged: UNI2-h / Virchow patch embeddings + PatchCore, exactly what virchow-2024's follow-ups propose. **The coreset is the key piece**: healthy atlases hold hundreds of thousands to millions of cells; a coreset fixes kNN's scaling problem while guaranteeing that rare healthy cell types (podocytes, juxtaglomerular cells) are not dropped as they would be under random subsampling — i.e., coverage-first compression of the healthy reference. **What breaks**: (1) **bank contamination** — healthy donors carry age-related focal injury, ambient-RNA contamination and doublets, which enter the bank and "cover" similar anomalies in the test set; (2) **batch effects** — if a new biopsy comes from a different batch/platform than the reference, nearest-neighbour distances rise globally and everything looks anomalous, so scArches-style mapping or multi-batch normals in the bank are needed first; (3) **continuous disease states** — kNN distance says "how far from healthy" but not in which direction, so an injured PT cell and a doublet can score alike; (4) **no pixel masks** — the pixel AUROC / PRO PatchCore reports must become per-cell expert labels or synthetic perturbations with known ground truth. Topic 1's cross-modal agreement directly addresses (2) and (3): a cell/region that is far from healthy neighbours in **all** of the RNA, ATAC, Xenium and H&E banks is more likely disease than technical artifact. **Existing repo papers with the same idea**: pathology-ad-bench-mlhealth-2025 benchmarks PatchCore on pathology data including mouse glomeruli; histo-nejmai-2024 scores CTransPath foundation-model features with a modified kNN — a close pathology relative of PatchCore; spatial-natcommun-2024 (STANDS) also has a memory bank, but to curb mode collapse inside GAN reconstruction, not as PatchCore's normal-feature bank for kNN. For Topic 2: kNN distances are uncalibrated, so a verifier should require the agent to state where its threshold comes from (e.g., conformal p-values as in conformal-scrna-bioinformatics-2025).

## Reusable assets
- **Code:** official implementation (Amazon Science) with coreset selection and faiss nearest-neighbour search.
<https://github.com/amazon-science/patchcore-inspection>
- **Library:** the PatchCore implementation in anomalib (used by pathology-ad-bench-mlhealth-2025).
<https://github.com/open-edge-platform/anomalib>
- **Directly reusable piece:** greedy minimax coreset (+ JL random projection) — usable on its own to compress a healthy single-cell reference while keeping rare cell types covered.

## Follow-ups
- SPADE (Cohen & Hoshen 2020) and DN2 (Bergman et al. 2020), PatchCore's direct predecessors.
- Follow-ups on bank contamination / PatchCore robustness when the training set contains anomalies (e.g., SoftPatch-type work) — crucial because "healthy donors are not fully healthy".
- Run PatchCore on UNI2-h embeddings of H&E from the kidney samples to be tested (or public KPMP WSIs) and compare against cell-level kNN scores on the Xenium side as a cross-modal agreement test.

## Cite
```bibtex
@inproceedings{Roth2021_210608265,
  title = {Towards Total Recall in Industrial Anomaly Detection},
  author = {Roth, Karsten and Pemula, Latha and Zepeda, Joaquin and Sch{\"o}lkopf, Bernhard and Brox, Thomas and Gehler, Peter},
  booktitle = {2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages = {14298--14308},
  publisher = {IEEE},
  year = {2022},
  doi = {10.1109/CVPR52688.2022.01392},
  eprint = {2106.08265},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2106.08265}
}
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
