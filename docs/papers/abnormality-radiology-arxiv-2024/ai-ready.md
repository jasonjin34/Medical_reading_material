<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# Abnormality-Driven Representation Learning for Radiology Imaging

- **Authors:** Marta Ligero; Tim Lenz; Georg Wölflein; Omar S. M. El Nahhas; Daniel Truhn; Jakob Nikolas Kather
- **Venue / Year:** arXiv preprint · 2024
- **DOI:** 
- **URL:** https://arxiv.org/abs/2411.16803
- **Bibkey:** Ligero2024_241116803
- **Status:** complete

## Abstract
To date, the most common approach for radiology deep learning pipelines is the use of end-to-end 3D networks based on models pre-trained on other tasks, followed by fine-tuning on the task at hand. In contrast, adjacent medical fields such as pathology, which focus on 2D images, have effectively adopted task-agnostic foundational models based on self-supervised learning (SSL), combined with weakly-supervised deep learning (DL). However, the field of radiology still lacks task-agnostic representation models due to the computational and data demands of 3D imaging and the anatomical complexity inherent to radiology scans. To address this gap, we propose CLEAR, a framework for radiology images that uses extracted embeddings from 2D slices along with attention-based aggregation for efficiently predicting clinical endpoints. As part of this framework, we introduce lesion-enhanced contrastive learning (LeCL), a novel approach to obtain visual representations driven by abnormalities in 2D axial slices across different locations of the CT scans. Specifically, we trained single-domain contrastive learning approaches using three different architectures: Vision Transformers, Vision State Space Models and Gated Convolutional Neural Networks. We evaluate our approach across three clinical tasks: tumor lesion location, lung disease detection, and patient staging, benchmarking against four state-of-the-art foundation models, including BiomedCLIP. Our findings demonstrate that CLEAR using representations learned through LeCL, outperforms existing foundation models, while being substantially more compute- and data-efficient.

## Full text / Extract
<!-- Full cleaned text for open-access; for paywalled leave the note below. -->
> Open access: the full text is the arXiv PDF (https://arxiv.org/abs/2411.16803; local copy `source.pdf`). The close reading is in `deep-read.md`.
