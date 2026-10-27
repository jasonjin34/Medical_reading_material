# A visual–omics foundation model to bridge histopathology with spatial transcriptomics

> **Bibkey** `Chen_2025_Loki` · **Venue** Nature Methods (2025) · **Category** spatial · **Relevance** high · **Access** open
> **Link** <https://doi.org/10.1038/s41592-025-02707-1> · `status: complete`

---

## One-liner
OmiCLIP writes each Visium spot's transcriptome as a "sentence" of gene symbols ranked by expression and contrastively aligns it with the matching H&E patch in a CLIP/CoCa setup (ST-bank: 2.2M pairs, 1,007 samples, 32 organs); the Loki platform built on top offers five modules — tissue alignment, tissue annotation, cell-type decomposition, image↔transcriptome retrieval and ST expression prediction from H&E.

## Problem
Pathology vision–language foundation models (PLIP, CONCH) use text captions that lack molecular insight, while methods combining histology with omics are task-specific; there is no unified multimodal model and infrastructure that handles sequencing and pathology images together.

## Method
**Data**: ST-bank — 113 studies, 1,007 10x Visium samples, ~2.2M tissue patches with paired transcriptomes across 32 organs, spanning healthy, cancer, heart failure and Alzheimer's states; QC keeps high-resolution H&E. **Representation**: Ensembl IDs mapped to symbols, housekeeping genes removed, genes ranked high→low into a text sentence (after GenePT / Cell2Sentence; the rank-based idea follows Geneformer / scFoundation to dampen batch effects). **Model**: fine-tuned from CoCa (image encoder + text encoder + multimodal fusion decoder), contrastive loss aligning paired image/transcriptome embeddings (768-d). **Loki modules**: Align (OmiCLIP embeddings + adapted coherent point drift; ST↔ST and H&E↔ST); Annotate (cosine similarity between H&E patches and tissue-specific bulk RNA-seq or marker-gene sentences; can be averaged with PLIP's text similarity); Decompose (Tangram's objective applied to OmiCLIP embeddings rather than raw expression, scRNA-seq as reference, in ST mode or image-only mode, plus NMS-style refinement); Retrieve (image embedding → nearest transcriptomes in ST-bank); PredEx (similarity-weighted sum of reference-spot expression). Most tasks fine-tune on the target slide by default.

## Data
Training: ST-bank (above). Evaluation: against 22 SOTA methods on 5 simulated, 19 public and 4 in-house datasets — 8 adjacent small-intestine sections, 2 adjacent ovarian carcinosarcoma sections, breast-cancer Visium + Xenium, in-house TNBC Xenium, colorectal cancer Visium-HD, mouse brain cortex, CRC7K / WSSS4LUAD / PatchCamelyon / LC25000, 39 normal-heart ST samples, and more.

## Key results
- **Representation**: on 95 expert-annotated ST-bank samples, Calinski–Harabasz scores rise significantly after contrastive learning (P < 0.001); image embeddings cluster better than UNI and GigaPath. Robust to noised images and downsampled depth (11,792 → 4,512 → 615 UMI).
- **Align**: small intestine, median PCC 0.67–0.80 (image→ST) / 0.62–0.83 (ST→ST) vs PASTE −0.25–0.39 and GPSA 0.27–0.56; ovarian carcinosarcoma, median PCC 0.88/0.86 vs PASTE 0.26, GPSA 0.43, CAST 0.71; Xenium↔Visium mean error 0.08 mm. Training from scratch reaches only PCC 0.53. Averaging image + transcriptome embeddings does not beat a single modality.
- **Annotate (zero-shot via marker genes)**: F1 0.59–0.96 on four pathology benchmarks vs OpenAI CLIP 0.03–0.34 and PLIP 0.5–0.93; averaging Loki+PLIP is best on all four (93% recall on CRC7K).
- **Decompose**: on the TNBC Xenium benchmark, ST and image modes score 1.32/1.11 (top two) vs 0.87 to −1.82 for Tangram, CARD, Cell2location, RCTD etc.; swapping in scGPT / scFoundation / Geneformer embeddings ranks 6th/8th/9th.
- **Retrieve**: kidney validation Recall@5% 0.173, Recall@10% 0.297 (~3.2× CLIP/PLIP); independent test Recall@5% 0.117, @10% 0.208.
- **PredEx**: on 39 normal-heart samples, best MSE in 28/39 and best PCC in 16/39 vs Hist2ST, HisToGene, BLEEP, mclSTExp — without retraining.

## Contributions
- Plugs "transcriptome-as-text" into a CLIP-style pathology foundation model — the first large-scale vision–omics pretraining from public ST.
- One shared embedding space powers five downstream tasks, letting bulk RNA-seq, scRNA-seq or even marker lists interpret H&E.
- Releases ST-bank, weights and code.

## Limitations
- Million-scale pretraining is far below general CLIP; rare conditions are underrepresented, so alignment/decomposition default to fine-tuning on the target slide.
- Contrastive, not generative: PredEx is similarity-weighted retrieval over reference spots, not true expression generation.
- Uses only top-ranked gene names, losing absolute magnitude; Visium-only (spot level, ~55 μm), not single-cell resolution.
- Some evaluations (e.g. Retrieve) lack transcriptomic ground truth and use image similarity as proxy; if one modality dominates, fusion gains vanish.

## Relation to our direction
For detect → model → revert, OmiCLIP offers a **shared H&E–expression embedding space**, which matters most for Topic 1's cross-modal agreement: if a tissue region's H&E embedding and transcriptome embedding fail to retrieve each other in the shared space, that is a natural cross-modal disagreement signal; when both deviate from the healthy reference, a real lesion is more likely. Given paired H&E and single-cell-resolution spatial-omics data, so Loki Align (the paper already demonstrates Xenium→pseudo-Visium) could register them, and each modality's distance to its healthy distribution could be scored and compared for agreement. Loki Annotate's zero-shot "marker-gene sentence" labelling could take kidney-injury markers (e.g. HAVCR1, LCN2, VCAM1) as prompts to produce weak labels that assist expert annotation for KidneyAnomalyBench. Caveats: kidney validation is thin (kidney Recall@10% 0.297) and resolution is spot-level, not single-cell. For Topic 2, Retrieve's evaluation — image similarity standing in for transcriptomic ground truth — is exactly the weak proxy agents tend to report as evidence, a type the claim-to-evidence verifier should flag.

## Reusable assets
- **Code:**
<https://github.com/GuangyuWangLab2021/Loki>
- **Weights and ST-bank:**
<https://huggingface.co/WangGuangyuLab/Loki>
- **Baselines**: PASTE, GPSA, CAST (alignment); Tangram, CARD, Cell2location, RCTD etc. (decomposition); Hist2ST, HisToGene, BLEEP, mclSTExp (expression prediction).

## Follow-ups
- HEST-1k (`hest1k-2024`) and the H&E→expression benchmark (`he2expr-bench-natcommun-2025`) to compare against PredEx's evaluation protocol.
- CONCH, PLIP and UNI (`uni2-h-model`) as alternative pathology encoders.
- GenePT / Cell2Sentence — origins of the expression-as-text idea.

## Cite
```bibtex
@article{Chen_2025_Loki, title={A visual–omics foundation model to bridge histopathology with spatial transcriptomics}, volume={22}, ISSN={1548-7105}, url={http://dx.doi.org/10.1038/s41592-025-02707-1}, DOI={10.1038/s41592-025-02707-1}, number={7}, journal={Nature Methods}, publisher={Springer Science and Business Media LLC}, author={Chen, Weiqing and Zhang, Pengzhi and Tran, Tu N and Xiao, Yiwei and Li, Shengyu and Shah, Vrutant V. and Cheng, Hao and Brannan, Kristopher W. and Youker, Keith and Lai, Li and Fang, Longhou and Yang, Yu and Le, Nhat-Tu and Abe, Jun-ichi and Chen, Shu-Hsia and Ma, Qin and Chen, Ken and Song, Qianqian and Cooke, John P. and Wang, Guangyu}, year={2025}, month=May, pages={1568–1582} }
```


---

📄 **[AI-ready full-text extract →](ai-ready.md)**
