# MahmoodLab/UNI2-h

> **Bibkey** `uni2-h-model` · **Venue** Hugging Face () · **Category** foundation · **Relevance** medium · **Access** open
> **Link** <https://huggingface.co/MahmoodLab/UNI2-h>
> `status: complete` — 若为 abstract-only,把 PDF 放到本文件夹的 `source.pdf` 后可补全全文精读。

---

## 一句话 / One-liner
UNI2-h is Mahmood Lab's histopathology foundation model: a ViT-H/14 backbone self-supervised with DINOv2 on 200M+ H&E/IHC tiles, turning a 224×224 tissue patch into a 1536-dim embedding usable as a frozen feature extractor for downstream classification, retrieval and MIL.

## 研究问题 / Problem
Computational pathology lacks a general, transferable histology representation — each task/organ/site often needs bespoke training with costly labels and poor generalization. UNI2-h aims to be a universal patch-level encoder across tissue types, stains and tasks, so downstream work needs only lightweight probes or MIL heads.

## 方法 / Method
As a resource, the core is architecture + SSL recipe. A custom ViT-H/14: depth 24, 24 heads, embed_dim 1536, SwiGLU FFN (mlp_ratio≈2.667×2, SiLU act), init_values 1e-5, 8 register tokens, no_embed_class, dynamic_img_size — 681M params. Pretraining uses the DINOv2 recipe = DINO self-distillation + iBOT masked-image modeling + KoLeo regularization, on A100 80GB with bf16 + PyTorch-FSDP. Inference returns the 1536-dim CLS token.

## 数据 / Data
Pretraining corpus: 300k+ H&E and IHC slides from Mass General Brigham, sampled into 200M+ tiles (>200M tiles from >300k slides is the headline figure). Stains include H&E and IHC; exact magnification/organ breakdown is not enumerated on the card. Substantially larger than UNI v1 (~100M tiles / 100k WSIs) and adds IHC.

## 主要结果 / Key results
The card gives no quantitative benchmark table on this page; it is positioned as a general backbone supporting ROI classification (logistic regression, k-NN, nearest-centroid), ROI retrieval by nearest neighbors, MIL-based slide classification, and fine-tuning for segmentation. Quantitative comparisons live in the UNI-series Nature Medicine paper (Chen et al. 2024).

## 创新点 / Contributions
- Scaled DINOv2 pretraining (>200M tiles / >300k slides) with a modern ViT-H (SwiGLU, 8 register tokens, dynamic sizing) producing a strong 1536-dim histology embedding.

## 局限 / Limitations
- Restrictive CC-BY-NC-ND 4.0 (no commercial use, no redistribution, gated); single-institution (MGB) data risks domain shift; patch-level morphology only, no spatial-omics and not tailored to anomaly detection.

## 与本研究方向的关系 / Relation to our direction
It sits at the **feature-extraction / representation** stage — the upstream encoder for anomaly detection. In our chain: tile a WSI into 224×224 patches, extract frozen 1536-dim UNI2-h features to get a morphology embedding space; fit a normal-tissue manifold and score disease/drug-perturbed deviations as anomalies (kNN density, one-class SVM, reconstruction/flow scoring, or MIL aggregation to slide level). The same patch embeddings serve as morphological coordinates for "virtual tissue," registrable to spatial transcriptomics for morphology↔gene joint modeling that conditions downstream gene-revert targets. Plug-and-play and reusable, but academic-only under NC-ND.

## 可复用资产 / Reusable assets
Weights `hf-hub:MahmoodLab/UNI2-h` (gated); load via `timm.create_model(..., **timm_kwargs)` with `resolve_data_config`+`create_transform`, ImageNet norm, 224×224 in → 1536-d CLS out. Downstream recipes (LR/k-NN/nearest-centroid, NN retrieval, MIL) and the UNI/CLAM/Trident ecosystem from Mahmood Lab. Cite Chen et al., Nature Medicine 2024.

## 待读 / Follow-ups

## 引用 / Cite
```bibtex
% no BibTeX fetched
```


---

📄 **[AI-ready 全文 / full-text extract →](ai-ready.md)**
