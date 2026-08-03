<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# Pathology-Informed Latent Diffusion Model for Anomaly Detection in Lymph Node Metastasis

- **Authors:** Jiamu Wang, Keunho Byeon, Jinsol Song, Anh Nguyen, Sangjeong Ahn, Sung Hak Lee, Jin Tae Kwak
- **Venue / Year:** MICCAI 2025 · 2025
- **DOI:** (not assigned; MICCAI proceedings)
- **URL:** https://papers.miccai.org/miccai-2025/0675-Paper2270.html
- **PDF:** https://papers.miccai.org/miccai-2025/paper/2270_paper.pdf
- **Code:** https://github.com/QuIIL/AnoPILaD (MIT License)
- **Bibkey:** histo-miccai-2025
- **Status:** complete

## Abstract
Anomaly detection is an emerging approach in digital pathology for its ability to efficiently and effectively utilize data for disease diagnosis. While supervised learning approaches deliver high accuracy, they rely on extensively annotated datasets, suffering from data scarcity in digital pathology. Unsupervised anomaly detection, however, offers a viable alternative by identifying deviations from normal tissue distributions without requiring exhaustive annotations. Recently, denoising diffusion probabilistic models have gained popularity in unsupervised anomaly detection, achieving promising performance in both natural and medical imaging datasets. Building on this, we incorporate a vision-language model with a diffusion model for unsupervised anomaly detection in digital pathology, utilizing histopathology prompts during reconstruction. Our approach employs a set of pathology-related keywords associated with normal tissues to guide the reconstruction process, facilitating the differentiation between normal and abnormal tissues. To evaluate the effectiveness of the proposed method, we conduct experiments on a gastric lymph node dataset from a local hospital and assess its generalization ability under domain shift using a public breast lymph node dataset. The experimental results highlight the potential of the proposed method for unsupervised anomaly detection across various organs in digital pathology. Code: https://github.com/QuIIL/AnoPILaD.

Keywords: Unsupervised Anomaly Detection · Diffusion Model · Visual-Language Model · Lymph Node Metastasis.

## Full text / Extract

### 1. Introduction
Lymph node metastasis is a crucial prognostic factor in cancer progression and treatment decisions. With the advent of digital pathology, several artificial intelligence approaches have been proposed to automate the detection of lymph node metastasis within tissues. Many of these methods are based on supervised learning, leveraging convolutional neural networks (CNNs) and transformer-based models to identify metastasis with high accuracy. While effective, these methods heavily depend on exhaustive expert annotations, which are time-consuming and resource-intensive. To address this limitation, unsupervised learning has emerged as a viable alternative, as it does not demand manual annotations. In unsupervised learning, a model is trained solely on normal (in-distribution) samples to learn a representation of in-distribution patterns. The trained model then detects abnormal or out-of-distribution (OOD) samples by identifying deviations from the learned in-distribution patterns, making it particularly well-suited for large-scale applications in digital pathology, where annotated abnormal samples are scarce.

Recently, generative models have been widely used for unsupervised anomaly detection, with two popular approaches: density-based methods and reconstruction-based methods. Density-based methods, such as variational autoencoders (VAEs), learn representations of in-distribution data, assigning higher likelihoods to in-distribution samples and lower likelihoods to OOD samples. In contrast, reconstruction-based methods are trained exclusively on normal data to guarantee poor reconstruction quality for abnormal samples and high reconstruction quality for normal samples. These include autoencoder (AE)-based models, Generative Adversarial Network (GAN)-based models, and denoising diffusion probabilistic model (DDPM)-based models.

In this paper, we introduce AnoPILaD, a Pathology-Informed Latent Diffusion model for anomaly detection in lymph node pathology images. This framework combines a latent diffusion model (LDM) and a vision-language model (VLM) for improved identification of anomalies in pathology images. AnoPILaD utilizes an LDM to learn a compact representation of normal images in a latent space via iterative diffusion and denoising processes while preserving critical histopathological features. AnoPILaD also adopts a VLM to select pathology-specific normal keywords, semantically guiding the reconstruction process towards a specific direction. In this manner, AnoPILaD achieves small deviations for normal samples and large deviations for abnormal samples, enhancing the accuracy and robustness of anomaly detection.

### 2. Methods

#### 2.1 Pathology-Informed Latent Diffusion Model
Recent research often employs DDPMs for reconstruction-based anomaly detection. A trained DDPM p_θ generates samples that match the in-distribution patterns z0 ∼ q(z0) by adding noise in a forward (diffusion) process, which has tractable posteriors at time t−1:

    q(z_{t-1} | z_t, z_0) = N(z_{t-1}; μ̃(z_t(z_0, ε), t), β̃_t I)          (1)

where t ∼ [1, 1000], ε ∼ N(0, I), z_t is a noisy sample, and β̃_t is a predefined constant. The model progressively removes noise in a reverse process:

    p_θ(z_{t-1} | z_t) = N(z_{t-1}; μ_θ(z_t(z_0, ε_θ), t), β̃_t I)          (2)

where ε_θ is an approximator to predict ε from z_t. The model is trained by decreasing the KL divergence between two Gaussians, with a simple objective:

    L = E_{z_t, t, ε∼N(0,1)} [ ‖ε − ε_θ(z_t, t)‖² ]                        (3)

A previous work adopted a DDPM for detecting breast lymph node metastasis, referred to as AnoDDPM, where normal samples are in-distribution data and metastasis samples are OOD data. The pretrained DDPM denoised partially diffused inputs z_t ∼ q(z_t | z_0) while steering the reverse process toward in-distribution patterns to get the reconstruction ẑ_0 ∼ p_θ(z_0 | z_{1:t}). The discrepancy between the input z_0 and its reconstruction ẑ_0 serves as the anomaly score, which is expected to be small for normal samples and large for metastasis samples. Though successful, AnoDDPM exhibited a substantial number of false positives, indicating insufficient ability to differentiate normal and OOD distributions. To address this and improve performance, AnoPILaD integrates an LDM with pathology-specific textual prompts, based on the assumption that these prompts enhance reconstruction quality and magnify the contrast between normal and abnormal samples. The LDM is trained with:

    L = E_{z_t, t, c, ε∼N(0,1)} [ ‖ε − ε_θ(z_t, t, c)‖² ]                  (4)

where c denotes a textual prompt. Pathology-informed reconstruction uses the same procedure as AnoDDPM, except the reverse process is guided by the textual condition: ẑ_0 ∼ p_θ(z_0 | z_{1:t}, c).

#### 2.2 Weighted Prompts Generation
To introduce a stronger inductive bias to the reconstruction, the authors exploit prior pathology knowledge of normal lymph nodes. Specifically, they collect a pool of 74 pathology keywords from the literature, describing characteristics of cells and microenvironments of normal lymph nodes and tissues. These keywords are reviewed and validated by an experienced pathologist to ensure clinical relevance and accuracy.

Given a pathology image, it is aligned with the pathology keywords to identify the most relevant ones and generate a text prompt guiding the reconstruction towards a pathology-informed direction. To align images and keywords, they adopt CONCH, a vision-language foundation model pre-trained on over 1.17 million pathology image-caption pairs. CONCH's image and text encoders produce embeddings for each pair of input image and keywords; cosine similarity scores are computed and the top-five most similar keywords are chosen. The similarity scores of the selected keywords are normalized by dividing by the median score. Using the selected keywords and their normalized scores, a weighted prompt is generated, transformed into an embedding vector, and fed into the LDM following the procedure of the Compel library (https://github.com/damian0815/compel).

### 3. Experiment

#### 3.1 Dataset
A gastric lymph node dataset was obtained from two local hospital (LH) sites, containing 808 Whole Slide Images (WSIs): 751 normal and 57 metastasis WSIs with partial annotation. All metastasis WSIs are used as an OOD test set (D_out^{LH,w}). Normal WSIs are split into training (643 WSIs, D_tr^{LH,w}), validation (50 WSIs, D_val^{LH,w}), and an in-distribution test set (58 WSIs, D_in^{LH,w}). WSIs are divided into patches: D_tr^{LH,p} = 1,373,475; D_val^{LH,p} = 102,240; D_in^{LH,p} = 174,703 patches (138,054 from D_in^{LH,w} and 36,649 from normal annotated regions of D_out^{LH,w}); D_out^{LH,p} = 115,330 with full metastasis annotation.

The Camelyon16 Challenge dataset (C16), a breast lymph node dataset, is used for independent testing: 32 normal WSIs as validation (D_val^{C16,w}), 80 normal WSIs as in-distribution test (D_in^{C16,w}), and 49 metastasis WSIs as OOD test (D_out^{C16,w}). Among the 49, 22 WSIs contain tumor cell clusters larger than 2 mm in diameter, designated as C16 Macro (D_out,m^{C16,w}). All tumor regions in LH are larger than 2 mm. Patch counts: D_val^{C16,p} = 37,056; D_in^{C16,p} = 240,139; D_out^{C16,p} = 55,659 patches with full metastasis annotation.

Base prevalences: 0.3976 (D^{LH,p}); 0.4956 (D^{LH,w}); 0.1882 (D^{C16,p}); 0.3798 (D^{C16,w}); 0.2157 (D^{C16,w,macro}). For patch-level evaluation, WSIs from both LH and C16 are divided into 256×256-pixel patches using pixel-level annotations. All WSIs are processed at 20× magnification.

Label distribution (Table 1):
- WSI-level — LH: D_tr^w 643, D_val^w 50, D_in^w 58, D_out^w 57. C16: D_val^w 32, D_in^w 80, D_out^w 49 (D_out,m^w 22).
- Patch-level — LH: D_tr^p 1,373,475, D_val^p 102,240, D_in^p 174,703, D_out^p 115,330. C16: D_val^p 37,056, D_in^p 240,139, D_out^p 55,659 (D_out,m^p 55,536).

#### 3.2 Experiment Details
AnoPILaD uses Stable Diffusion model v1.5. The diffusion model was fine-tuned with the Adam optimizer, learning rate 1e-5, and batch size 64 using low-rank adaptation (LoRA) with update-matrix dimension 4. FID (Fréchet Inception Distance) was used to measure generated image quality; at 400k steps the model achieved the lowest FID and was chosen for testing. Input image size was 256×256 pixels.

AnoPILaD was compared with density- and reconstruction-based OOD methods. Density-based: negative log-likelihood (NLL) of a VAE backbone and three variants — Regret, LLR, and complexity (latent vector size 100, 64×64 randomly cropped inputs). Reconstruction-based: f-AnoGAN (64×64 random crops), AE, and MemAE (256×256 inputs, architecture following the MemAE work). Both AnoDDPM and AnoPILaD were implemented with the Diffusers library and used a PLMS sampler with 100 timesteps at inference.

For each method, z-scores of anomaly scores were computed for all patches in each test set. Patch-level OOD detection was evaluated by AUC (area under ROC) and AUPR (area under precision-recall curve). For WSI-level evaluation, a z-score heatmap was produced and a morphological erosion (2×2 window) applied, since metastasis areas can be very small. Classification used two strategies: maximum z-score (Z_MAX) and the average of 99th-percentile z-scores (Z_99), yielding WSI-level AUC and AUPR. For segmentation, mean patch-level DICE and IoU on D_out assessed overlap with annotations, and mean patch-level true negative rate (TNR) on D_in was measured (no positive regions). The segmentation prediction threshold was zero. The reconstruction timestep for both diffusion methods was chosen from eight candidate values by best WSI classification on the LH test set: 674 for both methods.

### 4. Results
Models were trained only on D_tr and evaluated separately at patch- and WSI-level on the two datasets (different organs), probing robustness to domain shift.

**Patch-level Anomaly Detection (Table 2), AUC / AUPR:**
- NLL: LH 0.4982 / 0.5552; C16 0.3250 / 0.1600
- Regret: LH 0.6720 / 0.6718; C16 0.6480 / 0.3441
- LLR: LH 0.6078 / 0.6260; C16 0.7065 / 0.4765
- complexity: LH 0.7931 / 0.7139; C16 0.7752 / 0.5140
- f-AnoGAN: LH 0.2289 / 0.3377; C16 0.1735 / 0.1104
- AE: LH 0.9254 / 0.8906; C16 0.6584 / 0.4759
- MemAE: LH 0.9290 / 0.8886; C16 0.6611 / 0.4880
- AnoDDPM: LH 0.8555 / 0.7841; C16 0.6857 / 0.5741
- **AnoPILaD: LH 0.9587 / 0.9499; C16 0.8884 / 0.6987**

AnoPILaD substantially outperformed all methods. Among density-based methods, NLL failed to distinguish OOD patches; variants improved, with complexity the best, but still ~0.16 AUC and ~0.23 AUPR below AnoPILaD. Among reconstruction-based methods, f-AnoGAN was poorest; AE and MemAE were strongest, ~0.03 AUC and ~0.05 AUPR below AnoPILaD on LH, but the gap widened to ~0.22 AUC and ~0.22 AUPR on C16, showing AnoPILaD's superior robustness to organ-type domain shift.

**WSI-level Anomaly Detection (Table 3) — Classification (AUC / AUPR) for the four top patch-level models:**
- AE: LH Z_max 0.9622/0.9612, Z_99 0.9395/0.9381; C16 Z_max 0.6612/0.5961, Z_99 0.5798/0.5217; C16 Macro Z_max 0.6398/0.3677, Z_99 0.5523/0.2918
- MemAE: LH Z_max 0.9504/0.9440, Z_99 0.9365/0.9382; C16 Z_max 0.6505/0.5689, Z_99 0.5686/0.5313; C16 Macro Z_max 0.6381/0.3657, Z_99 0.5597/0.3141
- AnoDDPM: LH Z_max 0.7840/0.6616, Z_99 0.9383/0.8995; C16 Z_max 0.4992/0.3885, Z_99 0.4551/0.3905; C16 Macro Z_max 0.4926/0.2146, Z_99 0.5119/0.2347
- **AnoPILaD: LH Z_max 0.9837/0.9740, Z_99 0.9943/0.9948; C16 Z_max 0.6745/0.6140, Z_99 0.6367/0.5902; C16 Macro Z_max 0.8062/0.5965, Z_99 0.8023/0.5886**

**WSI-level — Segmentation (TNR / DICE / IoU):**
- AE: LH 0.7981/0.3812/0.2902; C16 0.4536/0.1745/0.1317; C16 Macro 0.4536/0.3249/0.2549
- MemAE: LH 0.7957/0.3863/0.2932; C16 0.5593/0.1377/0.1039; C16 Macro 0.5594/0.2173/0.2124
- AnoDDPM: LH 0.7850/0.4319/0.3259; C16 0.7842/0.1765/0.1142; C16 Macro 0.7842/0.3131/0.2075
- **AnoPILaD: LH 0.8097/0.4322/0.3311; C16 0.8312/0.3098/0.2326; C16 Macro 0.8312/0.5420/0.4275**

AnoPILaD was superior across both datasets, metrics, and scoring strategies for classification. Performance varied strongly between LH and C16 (LH AUC 0.7840–0.9943 vs C16 AUC 0.4551–0.6745), but AnoPILaD had the smallest best-performance drop (0.3092–0.3576 AUC, 0.3600–0.4046 AUPR). On large metastatic regions (C16 Macro), all models declined, but AnoPILaD held AUC 0.8023–0.8062, suggesting strong cross-organ potential. In segmentation, AnoPILaD achieved the highest scores in every scenario. Although AE/MemAE reached comparable classification to diffusion methods, their segmentation was substantially poorer — MemAE (and similarly AE) assigned near-uniform scores across a slide, lacking specificity in localizing metastatic regions, underscoring that classification alone does not capture localization ability.

Qualitatively, comparing reconstructions of AnoPILaD and AnoDDPM: for in-distribution samples both generate normal histologic features, preserving small, dense lymphocytic structures. For OOD samples with disrupted architecture, AnoDDPM partially reconstructs metastatic regions and fails to fully suppress pleomorphic nuclei and fibrotic tissue, leaving residual abnormalities that blur the normal/abnormal boundary. With text-prompt guidance, AnoPILaD generates more uniform lymphocytic arrangements while suppressing architectural distortions, yielding a clearer distinction between normal and metastatic regions.

### 5. Conclusion
The authors propose AnoPILaD, a pathology-informed LDM for unsupervised anomaly detection in lymph nodes. By leveraging histological context provided through prompts, AnoPILaD introduces a stronger inductive bias during reconstruction, enhancing sensitivity to abnormal features and improving detection. Evaluating patch- and slide-level performance across two organ types, AnoPILaD substantially outperforms both density- and reconstruction-based anomaly-detection methods. Future work will extend AnoPILaD to further enhance cross-organ performance, improving adaptability and robustness for broader pathological applications.

Acknowledgments: Supported by the National Research Foundation of Korea (NRF) grants (No. RS-2025-0058322 and RS-2024-00397293) and Korea Institute for Advancement of Technology (KIAT) International Cooperative R&D program (No. P0022543). The authors declare no competing interests.

### Code / Repository notes (github.com/QuIIL/AnoPILaD, MIT License)
- Environment: `conda create -n anopilad python=3.11`, dependencies via `requirements.txt`, plus CONCH installed from GitHub.
- Pipeline scripts: `image_caption.py` (CONCH-based captioning / keyword selection), `train_text_to_image_lora.py` (LoRA fine-tuning of Stable Diffusion text-to-image, e.g. `--train_batch_size 16 --num_train_epochs 20`, distributed via `torch.distributed.run`), and `rec_generate.py` (reconstruction + anomaly scoring).
- Data layout: separate directories for train / validation / in-distribution test / OOD test, each with slides containing patch images and a `metadata.csv` mapping image paths to prompts.
- Code adapts training implementations from HuggingFace `diffusers` and the CFG++ (CFGpp) repository. No pretrained checkpoint download links are provided in the README.
