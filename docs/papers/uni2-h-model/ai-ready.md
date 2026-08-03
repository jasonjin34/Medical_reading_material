<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# MahmoodLab/UNI2-h

- **Authors:** Mahmood Lab (Harvard Medical School / Brigham and Women's Hospital); contact faisalmahmood@bwh.harvard.edu
- **Venue / Year:** Hugging Face · 2024
- **DOI:** 10.1038/s41591-024-02857-3 (associated UNI paper, Chen et al., Nature Medicine 2024)
- **URL:** https://huggingface.co/MahmoodLab/UNI2-h
- **Bibkey:** uni2-h-model
- **Status:** complete

## Abstract
_(model card — no formal abstract; see full extract below)_

## Full text / Extract

### What it is
UNI2-h is a foundational (pretrained) vision model / backbone for computational pathology developed by the Mahmood Lab. It is intended as a general-purpose feature extractor for histopathology (H&E and IHC) images, producing embeddings that transfer across tissue types, tasks and institutions.

### Architecture
- Base: custom ViT-H/14 (Vision Transformer, Huge, patch 14) built with the DINOv2 framework.
- Parameters: 681M.
- Patch size: 14; image size: 224×224.
- Embedding dimension: 1536 (output CLS token dimension).
- Depth: 24 transformer layers; attention heads: 24.
- FFN: SwiGLU (SwiGLUPacked), mlp_ratio ≈ 2.66667×2, activation SiLU.
- init_values: 1e-5.
- Register tokens: 8.
- Extras: no_embed_class (no class token in position embeddings), dynamic image sizing (dynamic_img_size).

### Training data
- Over 200 million image tiles sampled from over 300,000 H&E and IHC whole-slide images.
- Source: Mass General Brigham institutional data.
- Stains: H&E and IHC. (Magnification/organ breakdown not enumerated on the card.)

### Training details
- Objective: DINOv2 self-supervised recipe = DINO self-distillation + iBOT masked-image modeling + KoLeo regularization.
- Infrastructure: Nvidia A100 80GB GPUs, bf16 mixed precision, PyTorch-FSDP.

### How to load and use

Model is gated: you must be logged in to Hugging Face and have been granted access.

```python
import torch
import timm
from timm.data import resolve_data_config
from timm.data.transforms_factory import create_transform
from huggingface_hub import login

login()  # requires HF token with granted access to the gated repo

timm_kwargs = {
    'img_size': 224,
    'patch_size': 14,
    'depth': 24,
    'num_heads': 24,
    'init_values': 1e-5,
    'embed_dim': 1536,
    'mlp_ratio': 2.66667 * 2,
    'num_classes': 0,
    'no_embed_class': True,
    'mlp_layer': timm.layers.SwiGLUPacked,
    'act_layer': torch.nn.SiLU,
    'reg_tokens': 8,
    'dynamic_img_size': True,
}

model = timm.create_model("hf-hub:MahmoodLab/UNI2-h", pretrained=True, **timm_kwargs)
transform = create_transform(**resolve_data_config(model.pretrained_cfg, model=model))
model.eval()
```

- Preprocessing / transform: resize + normalize to ImageNet statistics (mean 0.485/0.456/0.406, std 0.229/0.224/0.225), tensor conversion, 224×224 input.
- Output: 1536-dimensional class-token feature per input tile, used as a frozen embedding for downstream tasks.

### Intended use / downstream applications
- ROI (region-of-interest) classification via logistic regression, k-NN, or nearest-centroid on the embeddings.
- ROI retrieval via nearest neighbors.
- Slide-level classification using multiple-instance learning (MIL) over patch embeddings.
- Fine-tuning recommended for segmentation tasks.

### Access and licensing
- License: CC-BY-NC-ND 4.0.
- Gating: requires institutional email verification and agreement to non-commercial academic research terms; access must be granted before download.
- Restrictions: commercial use prohibited without prior approval; redistribution of the model is forbidden.

### Citation
Chen et al., "Towards a general-purpose foundation model for computational pathology," Nature Medicine (2024), doi:10.1038/s41591-024-02857-3. Contact: faisalmahmood@bwh.harvard.edu.
