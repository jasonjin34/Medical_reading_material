<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# Nephrobase Cell+: Multimodal Single-Cell Foundation Model for Decoding Kidney Biology

- **Authors:** Li, Chenyu; Ziyadeh, Elias; Sharma, Yash; Dumoulin, Bernhard; Levinsohn, Jonathan; Ha, Eunji; Pan, Siyu; Rao, Vishwanatha; Subramaniyam, Madhav; Szegedy, Mario; Zhang, Nancy; Susztak, Katalin
- **Venue / Year:** bioRxiv (preprint, v1 posted 2025-10-01) · 2025
- **DOI:** 10.1101/2025.09.30.679471
- **URL:** https://doi.org/10.1101/2025.09.30.679471
- **Bibkey:** Li_2025_Nephrobase
- **Status:** complete

## Abstract
Abstract
                
                  Background
                  Large foundation models have revolutionized single-cell analysis, yet no kidney-specific model currently exists, and it remains unclear whether organ-focused models can outperform generalized models. The kidney’s complex cellular architecture and dynamic microenvironments further complicate integration of large-scale single-cell and spatial omics data, where current frameworks trained on limited datasets struggle to correct batch effects, capture cross-modality variation, and generalize across species.
                
                
                  Methods
                  We developed Nephrobase Cell+, the first kidney-focused large foundation model, pretrained on ~100 billion tokens from ~39.5 million single-cell and single-nucleus profiles across 4,319 samples, four mammalian species (human, mouse, rat, pig), and multiple assay modalities (scRNA-seq, snRNA-seq, snATAC-seq, spatial transcriptomics). Nephrobase Cell+ uses a transformer-based encoder-decoder architecture with gene-token cross-attention and a mixture-of-experts module for scalable representation learning.
                
                
                  Results
                  Nephrobase Cell+ sets a new benchmark for kidney single-cell analysis. It produces tightly clustered, biologically coherent embeddings in human and mouse kidneys, far surpassing previous foundation models such as Geneformer, scGPT, and UCE, as well as traditional methods such as PCA and autoencoders. It achieves the highest cluster concordance and batch-mixing scores, effectively removing donor/assay batch effects while preserving cell-type structure. Cross-species evaluation shows superior alignment of homologous cell types and &gt;90% zero-shot annotation accuracy for major kidney lineages in both human and mouse. Even its 1B-parameter and 500M variants consistently outperform all existing models.
                
                
                  Conclusions
                  With organ-scale multimodal pretraining and a specialized transformer architecture, Nephrobase Cell+ delivers a unified, high-fidelity representation of kidney biology that is robust, cross-species transferable, and unmatched by current single-cell foundation models, offering a powerful resource for kidney genomics and disease research.

## Full text / Extract
<!-- bioRxiv license for this preprint is "no CC" (all rights reserved), so the full text is NOT reproduced here. Below: factual key points extracted from the v1 full text (JATS), with numbers as reported by the authors. -->

**Corpus.** 4,319 samples, ~39.5M single-cell/single-nucleus profiles, ~100B tokens. Species: human 25.2M, mouse 12.5M, rat 1.4M, pig 0.293M. ~30M from kidney tissue, ~10M immune/peripheral (incl. PBMCs from healthy and CKD donors); also fetal kidney and organoids. Assays: scRNA-seq ~48.7%, snRNA-seq ~25.4%, CosMx ~7.7%, snATAC-seq ~6.2%, Xenium ~5.5%. Top cell types: PT 27.4%, T cells 19.1%, EC 8.8%. Sources: GEO, SRA, HCA, CELLxGENE, KPMP + in-house (CosMx ~3M, Xenium ~2M, sn/sc/snATAC ~3M cells). Fixed feature space of 32,768 orthologous genes.

**Architecture/objectives.** Transformer encoder-decoder; gene tokens = identity + normalised expression (+ optional metadata/perturbation) embedded via cross-attention; encoder self-attention, decoder cross-attention; RMSNorm; sparse top-k Mixture-of-Experts with shared expert and load-balancing loss. Losses: ZINB reconstruction (masked + unmasked genes), focal-loss cell-type classification (effective-number class weights, beta = 0.9, gamma = 2.0), Elastic Cell Similarity regulariser (target cosine threshold e.g. 0.5), supervised contrastive loss (temperature e.g. 0.07), domain and assay adversarial discriminators with gradient reversal (assay weight ramped over epochs). Two models: ~1B and ~500M parameters.

**Evaluation (held-out).** Human: KPMP 2025 Q2 data; mouse: a developmental model; plus a mixed human-mouse kidney dataset. Baselines: Geneformer, scGPT, UCE, PCA, autoencoder.
- Human: KMeans ARI 0.82 (1B) vs scGPT 0.40, autoencoder 0.55, Geneformer 0.22; NMI 0.78 vs scGPT 0.48; silhouette ~0.68; cLISI 1.00; iLISI ~0.17-0.18; kBET 0.25-0.28 (scGPT 0.09; authors state lower is better); total integration score 0.71 (1B), 0.70 (500M).
- Mouse: ARI ~0.70, cLISI 1.0, total 0.69-0.68.
- Cross-species: 500M NMI 0.75 / ARI 0.72 (Geneformer 0.44/0.22, scGPT 0.62/0.43); 1B NMI 0.73 / ARI 0.57; cLISI 1.00, iLISI 0.01, graph connectivity ~0.94, PCR ~0.94; total 0.63 (500M), 0.61 (1B), Geneformer 0.50, UCE 0.51.
- "Zero-shot" annotation (trained classification head applied to held-out data without fine-tuning): >90% of PT cells correct, high agreement for TAL, DCT, CNT, IC, podocytes; errors mainly between related subtypes (distal vs connecting tubule). Comparison with simpler methods reported as "not shown".

**In silico perturbation.** 5,000 randomly sampled cells, target gene expression doubled, predicted DE genes ranked and GSEA run. CCL2 and VCAM1: immune adhesion/chemotaxis terms; GDF15: growth regulation, MAPK; SOX4: kidney morphogenesis, oxidative phosphorylation. Qualitative only; no baseline or wet-lab validation.

**Stated limitations.** Not every kidney condition/assay covered; rare cell types and extreme pathologies may be underrepresented; fixed gene space; heavy compute; RNA and ATAC only (no proteomics/metabolomics/imaging); correlational, requires experimental validation.

**Data availability.** Previously published data: GSE107585, GSE182256, GSE183842, GSE173343, GSE211785, GSE209821, GSE183839, GSE291551. New scRNA-seq and CosMx data: GEO accession placeholder ("***") in v1. No code/weights link found in v1.
