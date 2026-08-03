# Pathology-Informed Latent Diffusion Model for Anomaly Detection in Lymph Node Metastasis

> **Bibkey** `histo-miccai-2025` · **Venue** MICCAI 2025 (2025) · **Category** histopath · **Relevance** medium · **Access** open
> **Link** <https://papers.miccai.org/miccai-2025/0675-Paper2270.html>
> `status: complete` — 若为 abstract-only,把 PDF 放到本文件夹的 `source.pdf` 后可补全全文精读。

---

## 一句话 / One-liner
AnoPILaD is a pathology-informed latent diffusion model: a VLM (CONCH) selects normal-tissue keywords that condition an LDM's reconstruction toward normal morphology, and the input-vs-reconstruction discrepancy serves as an unsupervised anomaly score for lymph-node metastasis.

## 研究问题 / Problem
Supervised metastasis detection needs exhaustive annotation, which is scarce in digital pathology. Unsupervised reconstruction-based methods (e.g. AnoDDPM) train only on normal tissue but reconstruct poorly, yielding many false positives and weak normal/abnormal separation. The paper aims to sharpen this separation and improve cross-organ robustness.

## 方法 / Method
AnoPILaD fine-tunes a Stable Diffusion v1.5 LDM with LoRA (rank 4, lr 1e-5, batch 64) on normal patches only, with a text-conditioned denoising loss. A "weighted prompt" module takes 74 pathologist-validated normal-lymph-node keywords, uses CONCH (VLM pretrained on 1.17M pathology image-caption pairs) to pick the top-5 by cosine similarity, normalizes scores by their median for weighting, and encodes them via Compel into the LDM condition. Following AnoDDPM, an input is partially noised to timestep t (674 here) and reverse-denoised under the prompt to a "normal-like" reconstruction; input-vs-reconstruction discrepancy is the anomaly score. Inference uses a PLMS sampler with 100 steps.

## 数据 / Data
Two lymph-node WSI datasets at 20× (256×256 patches). LH (local hospital gastric): 808 WSIs (751 normal / 57 metastasis); train 643 normal WSIs = 1.37M patches, val 50, in-dist test 58, OOD test 57. C16 (Camelyon16 breast, public) for domain-shift testing: 32 val / 80 in-dist / 49 metastasis WSIs (22 with tumor clusters >2mm = "C16 Macro"); 55,659 OOD patches.

## 主要结果 / Key results
Patch-level (Table 2): AnoPILaD LH AUC 0.9587 / AUPR 0.9499; C16 AUC 0.8884 / AUPR 0.6987, ~0.22 AUC above AE/MemAE under domain shift. WSI-level (Table 3): LH classification AUC up to 0.9943 (Z99); C16 Macro AUC ~0.806 vs ~0.5-0.6 for others. Segmentation: AnoPILaD best DICE/IoU/TNR everywhere (C16 Macro DICE 0.5420 vs AnoDDPM 0.3131); AE/MemAE classify okay but localize poorly (near-uniform heatmaps).

## 创新点 / Contributions
- Couples a pathology VLM (CONCH) with an LDM, using normal-tissue keyword prompts as an inductive bias for reconstruction-based anomaly detection.
- A weighted-prompt module: 74 validated keywords, CONCH top-5 selection, median-normalized weights, Compel encoding.
- Demonstrates cross-organ (gastric→breast) robustness and argues segmentation/localization, not just classification, is the meaningful anomaly-detection metric.

## 局限 / Limitations
- Large cross-domain drop remains (C16 WSI AUC ~0.67 vs LH ~0.99); absolute segmentation DICE still modest (0.54 on C16 Macro).
- Keyword pool is hand-curated and lymph-node-specific; no ablation on prompt count/source; new organs need a new vocabulary.
- Only two organs / partly-private data; reconstruction timestep t=674 tuned on LH may not transfer.

## 与本研究方向的关系 / Relation to our direction
Squarely at stage 1 (anomaly detection) of our pipeline, and a near-ideal template: model only normal tissue generatively, treat disease/metastasis as OOD, and both detect and localize it via z-score heatmaps + segmentation. Its "reconstruct-to-normal, discrepancy = anomaly" scheme is an image-domain prototype of a virtual (normal) tissue that reverts an abnormal sample to normal morphology, structurally analogous to our "revert the anomaly" goal but in pixels rather than genes. Reusable ideas: (1) conditioning a generative normal-tissue model on foundation-model priors/text; (2) the CONCH weighted-keyword prompting could map onto spatial-omics by conditioning on marker/pathway vocabularies. It does not do gene-level revert prediction (stage 3) but offers a concrete localization/eval protocol.

## 可复用资产 / Reusable assets

- Code: <https://github.com/QuIIL/AnoPILaD> (MIT). Scripts for CONCH captioning, LoRA fine-tuning of SD v1.5, and reconstruction/anomaly scoring; deps: diffusers, CONCH, compel, CFG++ solver, python 3.11. No released checkpoints. C16 (Camelyon16) is public for reproducing the cross-domain test; LH data is private. Reusable eval protocol: patch AUC/AUPR from z-scores; WSI Zmax & Z99 scoring with 2×2 erosion; DICE/IoU + TNR for localization at threshold 0; FID for checkpoint selection. Plus the 74-keyword normal-lymph-node vocabulary and weighted-prompt recipe.

## 待读 / Follow-ups
- AnoDDPM (Wyatt 2022) and Linmans 2024 (Med Image Anal 93:103088), the direct baselines.
- CONCH (Lu 2023, arXiv:2307.12914) as a pathology VLM to probe for omics conditioning.
- Compel weighted-embedding internals; whether keyword weights can be swapped for gene/marker expression weights.

## 引用 / Cite
```bibtex
% no BibTeX fetched
```


---

📄 **[AI-ready 全文 / full-text extract →](ai-ready.md)**
