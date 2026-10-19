<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# MedIAnomaly: A comparative study of anomaly detection in medical images

- **Authors:** Cai, Yu; Zhang, Weiwen; Chen, Hao; Cheng, Kwang-Ting
- **Venue / Year:** Medical Image Analysis · 2025
- **DOI:** 10.1016/j.media.2025.103500
- **URL:** https://doi.org/10.1016/j.media.2025.103500
- **Bibkey:** Cai_2025
- **Status:** complete

## Abstract
Anomaly detection (AD) aims at detecting abnormal samples that deviate from the expected normal patterns. Generally, it can be trained merely on normal data, without a requirement for abnormal samples, and thereby plays an important role in rare disease recognition and health screening in the medical domain. Despite the emergence of numerous methods for medical AD, the lack of a fair and comprehensive evaluation causes ambiguous conclusions and hinders the development of this field. To address this problem, this paper builds a benchmark with unified comparison. Seven medical datasets with five image modalities, including chest X-rays, brain MRIs, retinal fundus images, dermatoscopic images, and histopathology images, are curated for extensive evaluation. Thirty typical AD methods, including reconstruction and self-supervised learning-based methods, are involved in comparison of image-level anomaly classification and pixel-level anomaly segmentation. Furthermore, for the first time, we systematically investigate the effect of key components in existing methods, revealing unresolved challenges and potential future directions. The datasets and code are available at https://github.com/caiyu6666/MedIAnomaly.

## Full text / Extract
<!-- Full cleaned text for open-access; for paywalled leave the note below. -->
> Source: legitimate open preprint — arXiv HTML v4 (2404.04518, 2025-02-19), labelled as the Medical Image Analysis version. Section 4.2.1 (network-architecture ablation) and all large numeric tables are omitted; the journal version itself is paywalled.

## Abstract

Anomaly detection (AD) aims at detecting abnormal samples that deviate from the expected normal patterns. Generally, it can be trained merely on normal data, without a requirement for abnormal samples, and thereby plays an important role in rare disease recognition and health screening in the medical domain. Despite the emergence of numerous methods for medical AD, the lack of a fair and comprehensive evaluation causes ambiguous conclusions and hinders the development of this field. To address this problem, this paper builds a benchmark with unified comparison. Seven medical datasets with five image modalities, including chest X-rays, brain MRIs, retinal fundus images, dermatoscopic images, and histopathology images, are curated for extensive evaluation. Thirty typical AD methods, including reconstruction and self-supervised learning-based methods, are involved in comparison of image-level anomaly classification and pixel-level anomaly segmentation. Furthermore, for the first time, we systematically investigate the effect of key components in existing methods, revealing unresolved challenges and potential future directions. The datasets and code are available at https://github.com/caiyu6666/MedIAnomaly.

## 1 Introduction

Anomaly detection (AD) is a fundamental machine learning problem [25, 78], which aims to detect abnormal samples that deviate from expected normal patterns. It works under the assumption that a large number of normal samples with similar patterns are readily available, while abnormal samples, with diverse and unknown patterns, are difficult to collect comprehensively. Therefore, existing AD methods generally train the model merely on normal data. This alleviates the requirement for abnormal samples, facilitating the application of AD in the medical domain, especially in rare disease recognition and health screening where abnormal samples are usually rare and diverse. Take the case of the United States, where over 7,000 rare diseases affect more than 30 million people, though each disease alone affects fewer than 200,000 people (about 0.06% of the population).11
 1

 https://www.fda.gov/patients/rare-diseases-fda Their rarity and diversity make it infeasible to collect enough samples for each disease to train a typical supervised model. This fact makes AD an appropriate solution to assist radiologists in recognizing potential abnormalities from medical images.

Table 1: Performance (AUC) of our implemented AE and prevailing works on Hyper-Kvasir and OCT2017 datasets. The details of AE (Our impl.) are shown in Section 3.2.1. Results∗ are taken from Tian et al. [109], Tian et al. [108], results† are taken from Zhao et al. [125], and results‡ are taken from Zhao et al. [124].

Numerous studies [94, 93, 68, 107, 95, 22] have been dedicated to medical AD. However, the lack of a comprehensive and fair comparison makes some conclusions unclear and hinders the development of this area.
On the one hand, the use of different datasets or partitions in existing studies impedes reproducibility and comparability. As a result, some studies underestimate the baseline and draw biased conclusions.
For instance, several papers [109, 108, 124, 125] performed experiments on datasets such as Hyper-Kvasir [18] or OCT2017 [53]. However, as shown in Table 1, a simple auto-encoder (AE) implemented by us, with default settings described in Section 3.2.1, achieves nearly perfect performance on these datasets. This suggests that these datasets are not challenging for AD, and therefore evaluating AD methods on them is not suitable.
On the other hand, despite many methods belonging to the same paradigm, the absence of a unified implementation leads to different network architectures and training tricks, resulting in unfair comparison. Take the case of reconstruction-based methods, where f-AnoGAN [93] adopts residual blocks [40] with multiple convolutional layers for the encoder and decoder, AE-Flow [125] chooses Wide ResNet-50-2 [120] as the encoder, while AE-U [68] uses plain convolutional layers without any specific designs. These differences could interfere with the comparison of methodologies and make ambiguous results. Overall, the comparisons based on improper datasets or inconsistent implementations are unreasonable. To address these issues, comprehensive datasets and a unified implementation of methodologies for medical AD are in high demand.

Although some surveys and benchmarks have been made for medical AD [35, 7, 57, 5, 23], they do not provide a comprehensive and fair comparison of methods. Fernando et al. [35] provided a systematic review of machine learning–based medical AD techniques with their applications and limitations, while no experiments were conducted. Baur et al. [7] compared a series of medical reconstruction-based AD methods on unified datasets. However, the comparison was limited to reconstruction methods only and the experiments were performed on a single image modality (brain MRI). These could lead to incomplete conclusions. Also, their utilization of private datasets impedes reproducibility.
Cai et al. [23] assessed various medical AD methods on reorganized datasets, but did not dive into a detailed analysis of these methods. Bao et al. [5] evaluated a range of AD methods on reorganized public medical datasets. However, most of these methods were originally designed for industrial applications rather than the medical domain.

It is important to note that Lagogiannis et al. [57] recently offered a detailed analysis of diverse SOTA AD methods across multiple datasets. They extensively investigated the influence of anomaly size and intensity, the effects of limited training data, and the performance of self-supervised pre-training on weight initialization and backbone pre-training.
However, their analysis did not thoroughly encompass some non-latest yet representative methods, such as various variants of AE-based methods and certain self-supervised methods utilizing specialized synthetic anomalies. Additionally, they did not employ unified network architectures for analyzing methods within the same paradigm. As a result, the inherent properties of the components and network architectures in typical methods remain unexplored.
Unlike Lagogiannis et al. [57], we aim to further investigate the effects and inherent properties of key components in typical methods by conducting comparisons across comprehensive datasets and employing as fair as possible network configurations.
The main contribution of this work is summarized as follows:

1. 

We present a taxonomy of common anomaly detection methods, encompassing reconstruction-based methods (image-reconstruction and feature-reconstruction), self-supervised learning-based methods (one-stage and two-stage), and feature reference-based methods (knowledge distillation and feature modeling). A thorough literature review is conducted accordingly.

2. 

We collect seven medical datasets, comprising five image modalities, to facilitate the evaluation of anomaly detection.

3. 

We conduct a comprehensive comparison of thirty representative methods using the collected datasets. Furthermore, the effects of key components employed in these methods are analyzed.

4. 

Through experiments and analysis, we highlight unresolved challenges and potential future directions in the field of medical anomaly detection.

## 3 Benchmark

In this section, we introduce our benchmark from the perspectives of datasets and implementation to facilitate comprehensive and fair comparison of methods for medical AD. Section 3.1 begins by analyzing previous datasets that are particularly easy for AD, and then introduces our curated datasets, followed by an introduction to the evaluation metrics employed. Section 3.2 introduces our unified implementation with default setups for typical reconstruction- and SSL-based AD methods.

## 3.1 Datasets and metrics

Fig. 3: Examples of datasets deemed too simple for AD, including the Hyper-Kvasir and OCT2017 datasets.

## 3.1.1 Datasets not suitable for anomaly detection

As depicted in Table 1, datasets such as Hyper-Kvasir [18] and OCT2017 [53] are remarkably easy for anomaly detection, rendering them unsuitable for evaluation purposes. This realization prompts us to explore the underlying reasons and aid in the selection of more appropriate datasets for evaluating AD.

In Fig. 3, we present examples of these two datasets, from which we identify two key factors. Firstly, the presence of anomaly-unrelated bias in abnormal samples creates an undesirable shortcut for AD. Normal images in the Hyper-Kvasir dataset (following the split from Tian et al. [109]) consistently feature green thumbnails in the lower left corner. In contrast, most abnormal images in the dataset exhibit black thumbnails or no thumbnails in that location. Consequently, these samples can be easily distinguished solely based on the lower left corner, even though this characteristic has no direct correlation with the disease itself. Secondly, distinct low-level differences can make abnormal images conspicuously distinguishable from normal ones. Polyps in the Hyper-Kvasir dataset exhibit clear boundaries and occupies substantial regions within the image, while ophthalmic diseases in OCT2017 dataset display distinct patterns of distorted texture and shape in retinal layers. These abnormal patterns deviate significantly from the corresponding simpler normal patterns, making them easily recognizable.

Therefore, to ensure effective evaluation, it is crucial to select datasets where abnormal samples and normal samples do not exhibit anomaly-unrelated bias, and where abnormal patterns are not excessively different from normal patterns.

Table 2: Summary of the datasets.

## 3.1.2 Image-level anomaly classification datasets

Six datasets are collected for image-level AnoCls: 
RSNA Dataset33
 3

 https://www.kaggle.com/c/rsna-pneumonia-detection-challenge. The dataset contains 8851 normal and 6012 lung opacity chest X-rays (CXRs). In experiments, we use 3851 normal images as the normal training dataset , and 1000 normal and 1000 abnormal (lung opacity) images as the test dataset . 
VinDr-CXR Dataset44
 4

 https://www.kaggle.com/c/vinbigdata-chest-xray-abnormalities-detection [75]. The dataset contains 10606 normal and 4394 abnormal CXRs that include 14 categories of anomalies in total. In experiments, we use 4000 normal images as , and 1000 normal and 1000 abnormal images as . 
Brain Tumor Dataset55
 5

 https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset. The dataset contains 2000 MRI slices with no tumors, 1621 with glioma, and 1645 with meningioma. The glioma and meningioma are regarded as anomalies. The images with no tumor come from Br35H66
 6

 https://www.kaggle.com/datasets/ahmedhamada0/brain-tumor-detection and Saleh et al. [90], while the images with glioma and meningioma come from Saleh et al. [90] and Cheng et al. [31]. In experiments, we use 1000 normal images (with no tumors) as , and 600 normal and 600 abnormal images (300 with glioma and 300 with meningioma) as . 
LAG Dataset [60]. The dataset contains 3143 normal retinal fundus images and 1711 abnormal retinal fundus images with glaucoma. In experiments, we use 1500 normal images as , and 811 normal and 811 abnormal images as . 
ISIC2018 Dataset [33]. The dataset from Task 3 of the ISIC2018 challenge is used. It contains seven categories, from which we take the nevus (NV) as the normal category, following previous works [65, 39]. In experiments, we use 6705 normal (NV) images from the official training set as , and 909 normal (NV) images and 603 abnormal (other six categories) images from the official testing set as . 
Camelyon16 Dataset [11]. We use the well-processed version of Camelyon16 for AD provided by Bao et al. [5], and merge their validation and testing set as our . The whole slide images (WSIs) are cropped into patches at 40 magnification, which are randomly sampled to build the image dataset for AD. In experiments, we use 5088 normal images as , and 1120 normal and 1113 abnormal images as .

## 3.1.3 Pixel-level anomaly segmentation datasets

(a) Train Normal

(b) Test Normal

(c) Test Abnormal

Fig. 4: Statistics of slice indices in our processed BraTS2021 dataset. A central crop was performed before slice extraction, resulting in index 0 corresponding to index 50 of the original volume and index 69 corresponding to index 119 of the original volume.

Fig. 5: Examples of the collected datasets for AD. Samples enclosed by the green dashed circle are normal, while others are abnormal.

BraTS2021 [3] is reorganized for pixel-level anomaly segmentation in this paper. It provides 1251 MRI cases with the resolution , as well as the corresponding voxel-level annotation for tumor regions. Each case has multiple modalities: T1, T1ce, T2, and FLAIR. We use only the FLAIR in experiments as it is the most sensitive to tumor regions. In preprocessing, the scans undergo a central cropping operation to remove the empty corners, resulting in dimensions of . For data construction, we utilize 1051 scans for training slice extraction, and the remaining 200 scans for testing slice extraction. To construct , we uniformly sample slices from the original normal axial slices without tumors in the scans, ensuring a balanced representation. Additionally, we discard redundant slices to enforce a minimum spacing of five slices between each sampled slice, guaranteeing sufficient content variation among neighboring slices. As a result, a total of 4211 normal 2D axial slices are extracted from 1051 FLAIR scans. Following the same principle, we further extract 828 normal and 1948 tumor slices from the remaining 200 FLAIR scans to build .

Due to the intrinsic characteristics of brain MRIs, central slices typically exhibit more relevant content and anomalies, as illustrated in Fig. 4. This imbalance could introduce biases to slice-level anomaly classification. Consequently, this dataset is primarily intended for evaluating pixel-level anomaly segmentation, while we also provide image-level metrics for reference.

## 3.1.4 Summary of the datasets

Fig. 5 presents normal and abnormal examples from the seven datasets. Table 2 summarizes details of the image modality, supported task, and repartition in the datasets. Regarding the repartition, there is no validation set available for model selection due to the unavailability of abnormal samples and labels during the training of AD models.

The datasets display distinct abnormal patterns. The chest X-ray, brain MRI, and retinal fundus datasets (i.e., RSNA, VinDr-CXR, Brain Tumor, BraTS2021 and LAG) showcase local anomalies. This implies that abnormal images contain the healthy version, with the addition of lesions in some areas. In contrast, Camelyon16 and ISIC2018 present global semantic anomalies, wherein abnormal images belong to completely different categories compared to normal images.

## 3.1.5 Evaluation metrics

Unsupervised AD methods usually generate continuous predictions. However, determining an appropriate threshold for binarizing these predictions remains an unresolved problem [7]. Consequently, we evaluate the performance using metrics that are independent of thresholds. For image-level AnoCls, we assess the area under the ROC curve (AUC) and average precision (AP). For pixel-level AnoSeg, we utilize the pixel-level AP ( ) and the best possible Dice score ( Dice ). Note that Dice is a dataset-wise Dice score calculated at the optimal operating point on the testing set, eliminating the need to select a threshold and mitigating the associated effects. We do not employ the pixel-level AUC since it is insensitive to false positives, which is particularly relevant in medical images where the majority of pixels are negative.

All of our experiments were conducted three times using different random seeds, enabling us to report the mean and standard deviation of the metrics.

## 3.2 Implementation

## 3.2.1 Unified implementation of the reconstruction methods

Table 3: Default configuration for AE in reconstruction methods.

As depicted in Fig. 1, AE for reconstruction AD comprises an encoder that compresses the input into a compact latent feature representation, , and a decoder that reconstructs the original input by decoding the representation, .

To ensure fairness, we employ the same AE for all reconstruction-based methods whenever possible. The encoder consists of four convolutional blocks, each downsampling the resolution to . The encoder blocks are then followed by a flattening operation and two fully-connected layers, which compress the feature to a vector of dimension . The decoder exhibits an architecture symmetric to the encoder. Table 3 summarizes our default configuration for this AE.

## 3.2.2 Unified implementation of the self-supervised methods

Table 4: Default configuration for SSL methods. Note that the output layer is a single layer at the end of the cls/seg head. It is omitted in this table for simplicity.

As shown in Fig. 2, the one-stage SSL approach comprises a feature extractor and a classification/segmentation head / , while the two-stage approach comprises a feature extractor , a projection head , and a one-class classifier .

To ensure fairness, we employ ResNet18 [40], excluding classification layers, as the feature extractor for all SSL-based methods whenever possible. The input resolution is set to . For additional specifics, we use the unified implementation from Schlüter et al. [95] as the framework for all one-stage segmentation approaches, and the implementation from https://github.com/Runinho/pytorch-cutpaste as the foundation for all two-stage approaches. Since most two-stage approaches utilize the classification task as the pretext task, we implement the one-stage classification approaches based on the same framework, but retain the classification head for evaluation. Table 4 summarizes our default configuration for SSL methods.

## 4.1 Comparison of the state-of-the-arts

For image-level AnoCls, we observe from Table 6 that AE-PL, AE-U, and FAE-SSIM usually achieve SOTA performance among the reconstruction methods. Among the SSL methods, those that utilize or fine-tune ImageNet pre-trained weights are the most competitive. Notably, most of these SOTA methods, except for AE-U, leverage ImageNet pre-trained weights in some way.
These results demonstrate the effectiveness of ImageNet weights for medical AD and highlight their versatility in enhancing AD through various means, including distance measurement (e.g., AE-PL), input data transformation (e.g., feature-reconstruction methods), and direct feature extraction (e.g., two-stage SSL methods).

In the absence of the ImageNet weights, reconstruction methods outperform SSL methods in image-level AnoCls. When excluding the use of ImageNet weights, the SOTA SSL method is two-stage AnatPaste. However, this method exhibits unstable performance across datasets. It fails to outperform the vanilla AE on LAG and BraTS2021 datasets, indicating a high sensitivity to abnormal patterns. In contrast, AE-U and DAE, which are the SOTA reconstruction methods that do not use ImageNet weights, demonstrate stable and competitive performance on most datasets.

Notably, DDPM-based methods demonstrate especially high performance on histopathology images such as Camelyon16. As depicted in Table 6, when ImageNet weights are excluded, most AE- or GAN-based methods do not work at all on Camelyon16. Only AE-U and DAE achieve an AUC exceeding 51%. Conversely, DDPM-based methods like AutoDDPM and AnoDDPMSimplex achieve remarkable AUCs of 80.7% and 70.6% on Camelyon16, respectively, surpassing others by a significant margin. This phenomenon can be attributed to the close relationship between anomalies in histopathology images and cellular morphology. Consequently, models with robust reconstruction capabilities (e.g., DAE, AnoDDPMSimplex, and AutoDDPM) or feature extraction prowess (e.g., AE-PL, FAE, and ReContrast) are desirable to repair image-space morphological changes or recognize feature-space deviations. This hypothesis finds support in Fig. 5 and Table 6.

For pixel-level AnoSeg, reconstruction methods significantly outperform SSL methods. As shown in Table 7, the vanilla AE beats all SSL one-stage segmentation methods in terms of the segmentation metrics on BraTS2021. This can be attributed to the fact that SSL methods trained through synthetic data segmentation rely on the similarity between synthetic abnormal patterns and real anomalies. They struggle to recognize real abnormal regions when these regions exhibit significant differences in appearance compared to synthetic anomalies. Consequently, their performance deteriorates on such datasets. This point will be further discussed in Section 4.3.1.

The best AnoSeg performance is achieved by DAE, surpassing the second-best method by a margin of over 10% Dice . This remarkable performance can be attributed to the synergy between the customized UNet architecture and the proposed self-supervised denoising task. This collaboration enables the meticulous reconstruction of healthy regions while effectively eliminating disease regions. Specifically, the UNet, equipped with skip connections, preserves normal details for high-quality reconstruction. However, skip connections inadvertently introduce abnormal information from the input into the reconstruction, leading to false negatives [68]. The denoising task in DAE effectively mitigates this drawback of the UNet by optimizing the model to generate a clean version of the corrupted input image. As a result, the model is encouraged to repair corrupted content, such as anomalies, in input images, facilitating the generation of pseudo-healthy reconstructions.

Fig. 6: Visualization of the compared image-reconstruction methods on typical abnormal images. The first row displays input abnormal images along with the abnormal regions (if available). The second rows depict reconstructed images and anomaly maps generated by each method. The third column of BraTS2021 dataset depicts binarized predictions at operating points of Dice .

Fig. 7: Visualization of the compared methods (excluding image-reconstruction methods) on typical abnormal images. The first row presents the input abnormal images, while the subsequent rows depict the anomaly maps generated by each method.

## 4.2 Analysis of reconstruction methods

## 4.2.2 Effects of latent space restrictions in AE

Reconstruction AE-based AD methods map the input data into a condensed latent space and then reconstruct the input accordingly. The latent space acts as an information bottleneck, potentially impeding the propagation of abnormal information and, consequently, obstructing the reconstruction of anomalies.
While previous methods have incorporated various forms of latent space restriction, such as KL-divergence in VAE [7] or memory modules in MemAE [36], none of these studies systematically compare and analyze the effects of these strategies. Furthermore, the most straightforward approach for latent space restriction, namely latent dimension reduction, remains unexplored. To address these issues, we explicitly investigate effects of different restrictions imposed on the latent space using our curated datasets. This investigation aims to examine their effects and shed light on the underlying principles of AE-based methods.

To begin, we discuss latent dimension reduction. Table 12 shows that a remarkably compact latent size (e.g., 4–32) yields a substantial performance boost when applied to datasets containing local regional anomalies (i.e., RSNA, VinDr-CXR, Brain Tumor, LAG, and BraTS2021 datasets, as mentioned in Section 3.1.4). For example, decreasing the latent size from 128 to 4 improves the evaluation metrics by 12.4% AUC and 10.0% AP on RSNA dataset, 12.7% AUC and 12.2% AP on VinDr-CXR dataset, and 7.3% AUC and 6.9% AP on LAG dataset. In the case of brain MRI modalities, specifically the Brain Tumor and BraTS2021 datasets, a similar trend is observed, albeit with a larger optimal latent size of approximately 32 and 16, respectively.

Based on these results, we make two main conclusions. Firstly, a narrow enough bottleneck in reconstruction networks is preferred to prevent anomaly reconstruction in the detection of local anomalies. As mentioned in Section 3.1.4, abnormal samples with local anomalies exhibit unexpected changes in some areas compared to normal samples while still retaining most normal regions. An appropriately compact latent size allows AE to represent the normal variations and restrict its generalization ability, rendering it incapable of representing abnormal changes. If the latent size is too large, the AE could exhibit undesired generalization on unseen abnormal changes, leading to false negatives.

Secondly, the optimal latent size differs across datasets, with datasets in which the normal data exhibits more variations (i.e., is more informative) tending to prefer a larger latent size. As mentioned above, the optimal latent size of brain MRI datasets is larger compared to other datasets. This disparity can be attributed to the fact that MRIs offer more information content compared to 2D scans. MRIs are volumetric scans that capture detailed tissue information, exhibiting greater variations among healthy subjects and encompassing variations among axial slices. These characteristics enable MRI datasets to surpass the information content of other datasets, necessitating a larger latent size to adequately represent them.

One unexpected trend in the results is the performance on ISIC2018 dataset. As shown in Table 12, contrary to the aforementioned datasets that favor relatively small latent sizes, ISIC2018 demonstrates improved performance with increasing latent sizes. The potential reason of this phenomenon is the fact that ISIC2018 contains global semantic anomalies that encompass entirely different categories compared to the normal data. Unlike images with local anomalies, which primarily involve regional unexpected variations, abnormal images in ISIC2018 introduce entirely new subject categories that do not overlap with the normal ones. These samples are relatively far out-of-distribution (OOD). Consequently, increasing the latent size may be ineffective for enabling the network to generalize well on these far OOD samples, while still facilitating the reconstruction of normal samples. This outcome makes ISIC2018 dataset benefit from large latent sizes. However, Camelyon16, another dataset in our experiments that contains global anomalies, is so difficult that AEs with any latent sizes fail on this dataset. Consequently, we cannot derive conclusive evidence from Camelyon16 to validate our hypothesis based on experiments on ISIC2018 dataset. The property of global semantic anomalies still requires further exploration.

Furthermore, we explore the performance of the spatial latent size, where the bottleneck comprises convolutional layers instead of flattening and fully-connected layers. This allows the latent code to retain spatial shapes, such as or . While the spatial AE significantly reduces the number of parameters compared to the dense AE, the performance may decrease on certain datasets. Specifically, both the dense AE with and the spatial AE with have the same number of latent variables. However, the dense AE ( ) has 2.35M parameters, whereas the spatial AE ( ) only has 0.22M parameters. Regarding performance, the spatial version suffers from a significant drop on Brain Tumor and LAG datasets. This phenomenon can be attributed to the fact that the spatial bottleneck compresses different regions to a consistent degree, regardless of the varying amounts of information present in these regions.

In addition to the simplest latent dimension reduction, there exist other popular designs that impose latent space restrictions in various ways, such as VAE [54], Constrained AE [29], and MemAE [36]. However, Table 6 shows that none of the existing approaches for restricting the latent space demonstrate superior performance compared to latent dimension reduction. Potential reasons are that VAE samples the latent code from the learnt distribution instead of using a deterministic vector, making the reconstruction indeterministic, while Constrained AE does not explicitly restrict the latent space.
The unexpected failure of MemAE [36], despite its success on various natural images, raises questions. MemAE introduced a memory bank to store prototypes of normal latent features during training and utilized a combination of these prototypes to replace the latent feature of the input. It hypothesized a distinct difference between normal and abnormal features, aiming to render abnormal inputs unreconstructible using the combination of normal prototypes. However, this hypothesis is not necessarily valid due to the inherent nature of AE [13, 21]. Consequently, we attribute the failure of MemAE to the inseparability of latent features of normal and abnormal medical images. To substantiate our argument, we visualize the latent features of normal and abnormal medical images obtained from AE and present the performance of OC-SVM built on these features, in Fig. 8. The results illustrate that these features are mixed together and inseparable by OC-SVM. This finding contradicts the underlying hypothesis of MemAE and provides support for our argument, ultimately explaining the failure of MemAE in medical scenarios.

(a) RSNA - 0.48/0.53

(b) VinDrCXR - 0.40/0.47

(c) Brain Tumor - 0.22/0.35

(d) LAG - 0.64/0.60

(e) ISIC2018 - 0.60/0.51

(f) Camelyon16 - 0.49/0.50

(g) BraTS2021 - 0.66/0.82

Fig. 8: T-SNE visualization for the latent representations of AE on the seven datasets. The performance of OC-SVM built on the latent representations is presented in the format AUC/AP.

## 4.2.3 Effects of distance functions for the reconstruction error in AE

In addition to the simplest and distances [7], various distance functions have been explored to measure the reconstruction error for anomaly detection [17, 10, 99, 14]. For example, Bergmann et al. [17], Behrendt et al. [10] employed Structural Similarity Index Measure (SSIM) [114], while Shvetsova et al. [99], Bercea et al. [14] utilized perceptual loss (PL) [48]. However, these studies combine specific distance functions with other methodological designs, and they do not explicitly compare the effects of different distance functions on various types of images. Consequently, the characteristics of different distance functions and the principles for selecting the most suitable ones for reconstruction-based AD remain unclear. To address these questions, we explicitly investigate the effects of these distance functions by employing the same AE architecture but with different reconstruction error functions. The performance of AE ( ), AE- , AE-SSIM and AE-PL is presented in Tables 6 and 7.

Surprisingly, we observe a significant impact of the distance function on the performance of reconstruction-based AD. While the standard and losses exhibit comparable performance on the majority of datasets, SSIM and PL losses present remarkable outcomes. Specifically, replacing the default loss with SSIM results in an improvement of over 10% AUC on RSNA dataset, slightly worse performance on VinDr-CXR, and a drop of more than 10% AUC on LAG dataset. Notably, AE-PL demonstrates SOTA or comparable performance on six datasets: RSNA, VinDr-CXR, Brain Tumor, LAG, Camelyon16, and BraTS2021, surpassing the version by over 20% AUC on certain datasets. However, it performs worse than the loss on ISIC2018. These observations suggest that distance functions for measuring the reconstruction error play a substantial role in reconstruction-based AD, and their performance is closely related to the abnormal patterns present in the datasets. Therefore, developing a suitable distance function to measure the reconstruction error of anomalies in different scenarios is a promising direction.

## 4.2.4 Effects of the gradient strategy in AE

When comparing methods that use gradient-based anomaly scores in AE-based backbones, such as AE-Grad and VAE- , with those using original anomaly score, namely AE and VAE, we observe that gradient-based scores usually exhibit slightly better performance than the original reconstruction error. This finding could inspire us to aggregate the global information into scalars and use the gradient w.r.t. the input as prediction maps. However, VAE-Gradcombi, which incorporates the KL-term, performs worse than VAE-Gradrec. This raises a question regarding how to properly exploit the extra information as a complement to reconstruction errors through the gradient strategy.

## 4.2.5 Effects of noise types in DDPM

Current DDPM-based AD methods rely on the addition of noise during the diffusion process to corrupt abnormal regions, thereby facilitating pseudo-healthy reconstructions. Wyatt et al. [115] demonstrated the superiority of their proposed Simplex noise over the original Gaussian noise used in DDPM for corrupting abnormal regions, showcasing better performance on brain MRIs. We evaluate the performance of AnoDDPM [115] equipped with these two noise types on a wider range of datasets. Our findings align with their conclusions and provide additional insights into the limitations of DDPM-based AD methods stemming from their reliance on noise.

Table 7 presents that AnoDDPMSimplex outperforms its Gaussian noise counterpart on most datasets, particularly on BraTS2021, where it achieves a remarkable margin of over 30% Dice . Visual evidence provided in Fig. 6 demonstrates that AnoDDPMSimplex successfully repairs most abnormal regions in chest X-rays and brain MRIs, while AnoDDPMGaussian reconstructs numerous undesirable lesions. These findings establish the superiority of Simplex noise in corrupting abnormal regions across various image modalities.

However, the performance of DDPM-based methods on LAG and ISIC2018 datasets reveals limitations inherent to these methods. In both cases, the vanilla AE outperforms DDPM-based methods. The potential reason behind this observation is that DDPM-based methods heavily rely on the similarity between the noise type employed and the abnormal patterns to ensure the corruption of abnormal regions during the diffusion process. This characteristic introduces a strong bias that renders these methods unsuitable for anomalies that differ from the noise type. Despite attempts to integrate healthy context into the repair process, such as in AutoDDPM [12], the performance on LAG and ISIC2018 datasets still falls short compared to the performance of the vanilla AE. Consequently, this unresolved issue restricts the generalizability of DDPM-based methods for AD, making them less versatile than AE-based methods.

## 4.2.6 Reconstruction quality and AD performance

Correlation. Previously, Baur et al. [7] demonstrated a relatively weak correlation between reconstruction quality and AnoSeg performance on brain MRIs. Instead, it is the distinguishable residual histograms of normal and anomalous intensities that matter most. They observed that in certain cases, as the reconstruction error increases (i.e., the reconstruction quality decreases), the AnoSeg performance actually improves. Building upon their findings and conducting experiments on a wider range of datasets and methods, we extend their conclusion to encompass additional data modalities and provide further insights to certain datasets.

Expanding on the conclusion drawn by Baur et al. [7], we show that the relatively weak correlation between reconstruction quality and AD performance is also applicable to other modalities such as chest X-rays, retinal fundus images, and dermatoscopic images. A prominent example supporting this conclusion is the comparison between AnoDDPMGaussian and AE-PL. As depicted in Fig. 6, AnoDDPMGaussian achieves the highest reconstruction quality on all datasets, effectively preserving both normal and abnormal regions. However, as highlighted in Tables 6 and 7, AnoDDPMGaussian exhibits the poorest overall performance. This can be attributed to the ineffectiveness of Gaussian noise in corrupting low-frequency abnormal regions, leading to their well-reconstruction alongside normal regions. Conversely, despite generating visually “faulty" reconstructions, AE-PL demonstrates competitive performance across most datasets. The reason is that perceptual loss performs anomaly detection in the feature space, prioritizing high-level semantic information over intensity reconstruction.

It is noteworthy that some recent works [12, 62] achieve both high reconstruction quality and competitive AD performance. These studies concentrate on enhancing the reconstruction quality of normal areas, rather than the entire image, and employ strategies such as masking to degrade the reconstruction quality of abnormal regions. Therefore, they still support the conclusion that distinguishable residual histograms of normal and anomalous intensities are more crucial than the overall reconstruction quality.

Additionally, we reveal a complementary insight concerning the detection of specific abnormal patterns, such as tumor cells in histopathology images (Camelyon16), where high reconstruction quality can yield benefits. Combining Table 6 and Fig. 6, we observe that, excluding methods equipped with ImageNet weights, the top three performing methods on Camelyon16 – AutoDDPM, AnoDDPMSimplex, and DAE – consistently produce high-fidelity reconstructions. We attribute this observation to the distinctive abnormal patterns present in histopathology images, where tumor cells manifest morphological deviations compared to normal cells. High reconstruction quality is beneficial for recognizing these anomalies related to cellular morphology.

Fig. 9: Distribution of pixel-level anomaly scores calculated in image-space and feature-space. Scores are normalized through division by the maximum value. Note the substantial difference in the vertical scale of (a) and (b).

Characteristics of relevant methods. To investigate the disparity between reconstruction quality and performance metrics, we began from analyzing the binary prediction maps depicted in Fig. 6 (the third column of BraTS2021 dataset). The binary prediction maps illustrate that methods such as DAE and autoDDPM, known for their high-quality reconstruction, excel in segmenting small tumors. However, their prediction maps contain scattered noisy points on normal regions. In contrast, methods such as AE-PL, which generate coarse score maps from feature-space, tend to produce larger segmentation regions than actual abnormal areas but exhibit improved robustness in normal regions without introducing noisy points. These characteristics could be relevant to the calculation space (i.e., image-space and feature-space) of their anomaly scores.

For further examination, we visualized the distribution of pixel-level anomaly scores for typical methods in Fig. 9. Initially, Fig. 9 shows that image-space anomaly scores are concentrated around zero, reflecting high reconstruction quality of corresponding methods. Improvements in these methods should prioritize amplifying errors in abnormal regions to reduce indistinguishable anomalies. For instance, autoDDPM exhibits notably lower frequencies of abnormal histogram overlapping with normal ones near zero compared to AnoDDPM (Gaussian), consistent with its superior performance metrics. In contrast to the lower values of image-space anomaly scores, feature-space scores from AE-PL and FAE exhibit values distant from zero on both normal and abnormal pixels, with distinguishable scores between the two, explaining their coarse score maps yet high performance metrics.

Analyzing these characteristics is crucial for clinical practice. However, existing quantitative metrics may not fully capture their distinctions to reflect clinical utility. For instance, widely used metrics like Dice score favor overconfident predictions, thus benefiting methods inclined towards over-segmentation like AE-PL and FAE. Furthermore, while feature-space anomaly scores from FAE and AE-PL distinguish between normal and abnormal pixels and achieve satisfactory performance metrics, they pose a challenge in clinical scenarios where discerning intensity differences in non-zero positive scores without proper calibration can be difficult for human experts. Future efforts should develop metrics and calibration strategies to effectively evaluate and enhance the clinical utility of anomaly segmentation.

## 4.3 Analysis of SSL methods

The performance of SSL-based methods on AnoCls and AnoSeg is presented in Tables 6 and 7, respectively. To facilitate a clear discussion, we categorize these methods based on whether they utilize ImageNet weights. Methods that utilize ImageNet weights are denoted with “†" in the tables.

## 4.3.1 Methods without ImageNet weights

SSL methods without ImageNet weights mainly rely on training on synthetic data. From their results, we can draw two significant conclusions as follows.

Firstly, comparing methods with the same number of stages, we conclude that more realistic synthetic anomalies usually lead to better performance in SSL-based methods. For example, AnatPaste [92] is specifically designed for chest X-rays and generates more realistic lung lesions than CutPaste.
As a result, in the two-stage paradigm, AnatPaste outperforms CutPaste on the two chest X-ray datasets by a large margin, 20.2% AUC and 17.1% AP on RSNA dataset, and 14.0% AUC and 13.3% AP on VinDr-CXR dataset. A similar trend is also observed in the one-stage classification paradigm, where AnatPaste outperforms CutPaste on both RSNA and VirDr-CXR datasets. Additionally, in the one-stage segmentation mode, NSA [95] and PII [107] synthesize more realistic anomalies using Poisson image editing, and thereby consistently outperform CutPaste and FPI on all datasets.

Secondly, comparing the one-stage and two-stage paradigms using the same anomaly-synthesis method, we conclude that in SSL-based AD, the two-stage paradigm usually outperforms the one-stage paradigm. Specifically, anomaly-synthesis approaches can be employed for both paradigms. While these two paradigms share a training procedure that classifies normal and synthetic data, the two-stage paradigm has an extra procedure to remove the projection head and build a Gaussian density estimator on learned representations.
Results show that when using AnatPaste for self-supervised training, the two-stage paradigm outperforms the one-stage classification paradigm on four datasets: by 11.5% AUC and 15.2% AP on RSNA dataset, 5.3% AUC and 10% AP on VinDr-CXR dataset, 16.0% AUC and 24.0% AP on Brain Tumor dataset, and 3.9% AUC and 0.2% AP on LAG dataset. A consistent trend also appears when using CutPaste or CutPaste-3way.

Fig. 10: T-SNE visualization of representations learned through synthetic data classification. (a) CutPaste; (b) AnatPaste.

To elucidate the rationale behind these conclusions, we conduct t-SNE visualization of representations learned through AnatPaste and CutPaste. For the first conclusion (the efficacy of realistic synthesis), we compare the visualization of the two typical synthesis approaches. As depicted in Fig. 10(a), a model trained through CutPaste can easily differentiate between the normal data and the unrealistic CutPaste samples. However, due to the significant discrepancy between real anomalies and synthetic ones, this model struggles to distinguish real anomalies from normal data. In contrast, Fig. 10(b) illustrates that the model trained on realistic synthetic data can naturally recognize real anomalies by leveraging the classification training. This observation underscores the importance of the realism of synthetic data. For the second conclusion (the superiority of the two-stage paradigm), let us consider the example provided in Fig. 10(a). The visualization highlights that although the classifier trained on unrealistic synthetic data fails to recognize real anomalies, the training process enables the model to effectively distinguish between the features of normal and abnormal samples. As a result, the two-stage paradigm, which removes the classification head and utilizes the learned representations, outperforms the one-stage paradigm, which directly employs the subpar classification head.

## 4.3.2 Methods with ImageNet weights

Most SSL-based AD methods that utilize ImageNet weights were initially developed for industrial scenarios [59, 84, 85]. While some studies have leveraged ImageNet weights for medical AD [92, 57], they primarily utilized these weights for model initialization only. Consequently, the performance of ImageNet weights themselves in medical AD remains unclear, leading to potential misconceptions regarding their utility. To explicitly evaluate the performance of ImageNet weights in medical AD and assess the effectiveness of relevant SSL methods, we conducted evaluations not only on the existing methods but also on the vanilla ImageNet-pretrained ResNet18 and ResNet152 feature extractors without special designs. This allows us to uncover the true impact of ImageNet weights on medical AD and shed light on the effectiveness of existing methodologies.

Surprisingly, we observe from Table 6 that directly utilizing a fixed ImageNet pre-trained network to extract representations for one-class classifiers outperforms most prevailing SSL methods that incorporate more complex training processes. Specifically, ImageNet pre-trained ResNet18, employed under the two-stage mode, achieves top-3 performance on nearly all datasets. This finding highlights the effectiveness of ImageNet weights in medical AD, which has not received sufficient attention and exploration. While some approaches, such as PANDA [84] and MSC [85], attempt to adapt ImageNet weights for AD, the experimental results suggest that they do not significantly improve performance compared to directly utilizing these weights. Therefore, adapting the powerful ImageNet weights for medical AD remains a promising but unresolved problem.

## 5 Challenges and future directions

Fig. 11: Intensity distribution of normal and abnormal pixels in BraTS2021 dataset.

## 5.1 Anomalies with pronounced intensity differences

Meissen et al. [71] demonstrated that simple intensity thresholding outperforms several deep learning methods on FLAIR MR scans. To further investigate this phenomenon, we analyze the intensity distributions of normal and abnormal pixels in BraTS2021 dataset and incorporate intensity thresholding into our benchmark. Surprisingly, as illustrated in Fig. 11, normal and abnormal pixels in BraTS2021 dataset exhibit distinguishable intensity distributions. Quantitative results in Table 7 reveal that intensity thresholding achieves the second-best segmentation performance (measured by Dice ), even surpassing advanced methods based on DDPM. These findings suggest that FLAIR scans effectively highlight most tumor regions through intensity variations, while many sophisticated deep learning methods underperform compared to this simple approach in identifying tumor regions. Consequently, for anomalies with pronounced intensity differences, such as tumors in FLAIR scans, it is crucial to benchmark deep learning-based methods against intensity thresholding to ensure their clinical relevance and utility.

The current analysis of pixel-level AnoSeg remains limited due to the scarcity of annotations and the narrow range of anomaly types, primarily focusing on prominent tumors in brain MRIs. Future work should expand the evaluation to include diverse and subtle anomalies, which could better reveal the potential of deep learning methods and provide deeper insights into the capabilities and limitations of AD methods in real-world clinical scenarios.

## 5.2 Latent space configuration of AE

Section 4.2.2 demonstrates that the latent space is the core component in reconstruction-based AD, with a simple adjustment of the latent dimensions proving to be the most effective means of controlling the latent space and achieving satisfactory performance. Unfortunately, existing approaches still rely on testing results to find the optimal configuration, leaving the question of how to adjust the latent space to its optimal state for diverse datasets unresolved. Recently, Cai et al. [21] leveraged information theory to reveal that the entropy of an optimal latent space should align with that of normal data, but they did not develop a method to explicitly measure this entropy. To tackle this challenge, a promising direction would be to quantify the information entropy of normal training data and develop self-adaptive methods that dynamically constrain the latent space to approach the entropy of normal data on different datasets. This approach would enable the determination of the theoretically optimal solution of AE-based AD methods.

## 5.3 Distance function for measuring reconstruction error

Section 4.2.3 highlights the significance of distance functions in measuring reconstruction error for reconstruction-based AD. While some distance functions, such as perceptual loss (AE-PL), exhibit remarkable performance, none surpass the baseline AE- on all seven datasets. For instance, the powerful AE-PL performs 6.1% worse in AUC than AE- on ISIC2018, despite showing over 20% better AUC on datasets like RSNA and Camelyon16. These observations indicate that designing an effective distance function for reconstruction error remains a challenging problem, which has not been adequately investigated in the literature.

Driven by these findings, a fundamental question arises: what should be a good distance function for measuring reconstruction error? To answer this question, we compare different distance functions based on their reconstruction fidelity in Fig. 6 and their metrics in Tables 6 and 7. From a visual perspective, AE-SSIM generates high-quality reconstructions that preserve more fine-grained details compared to other methods. In contrast, AE-PL produces reconstructions that appear significantly distorted. However, AE-PL outperforms AE-SSIM by a considerable margin in terms of the metrics on six datasets, for both AnoCls and AnoSeg. This suggests that what is a good distance function can be counterintuitive. Therefore, it is preferable to learn a distance function automatically through deep learning rather than relying on manual design.

The concept of learning distance functions (similarity metrics) through deep learning was originally proposed for multimodal medical image registration. Traditional metrics often struggle to measure the similarity between different imaging modalities due to the high variability of tissue appearance. Simonovsky et al. [103] addressed this challenge by training a network to measure similarity using constructed image pairs. Analogously, in anomaly detection, certain reconstruction discrepancies may not necessarily correspond to actual anomalies but rather reflect inherent limitations in model capacity. Ideally, such discrepancies should be systematically excluded when computing the distance metric between input and reconstructed images, with emphasis placed solely on highlighting abnormal regions. Drawing inspiration from deep similarity metrics in registration, we believe it is possible to train a similarity network to automatically measure anomaly-related reconstruction errors. This network can be trained on synthesized image pairs generated from the normal training set, taking into account the data characteristics. Pursuing this direction may lead to the development of a robust distance function capable of effectively measuring reconstruction errors across various datasets with different image modalities.

## 5.4 Utilization of ImageNet pre-trained weights

As depicted in Tables 6 and 7, the SOTA methods among both reconstruction-based and SSL-based methods extensively utilize ImageNet pre-trained weights. While these methods demonstrate competitive performance, the utilization of ImageNet weights takes different forms, including distance measurement (e.g., AE-PL), input data transformation (e.g., feature-reconstruction methods), and direct feature extraction (e.g., two-stage SSL methods). These successful applications highlight the remarkable capability of ImageNet weights in discerning normal and abnormal patterns, providing inspiration to advance AD from various perspectives.

The effective utilization of ImageNet weights in distance measurement suggests that in reconstruction-based AD, it is desirable to measure semantic differences rather than low-level intensity differences in reconstruction errors. This aligns with the findings of Meissen et al. [73], which indicate that residual errors alone cannot reliably identify abnormal regions with moderate pixel intensity due to intrinsic errors in normal regions. The application of ImageNet weights in input data transformation indicates the feasibility of enhancing the saliency of abnormal regions using feature maps. As revealed in Fig. 5, medical abnormal regions often exhibit subtle and seamless characteristics, which may explain the relatively lower performance of AD in medical scenarios compared to industrial scenarios. Enhancing the saliency of these anomalies becomes crucial in such cases. Lastly, the explicit use of ImageNet weights for feature extraction underscores their discriminative capability in AD, motivating further adaptation to improve performance.

While ImageNet weights have been effectively applied in various contexts, it is important to highlight that their application in feature reference-based methods, such as knowledge distillation [122] and feature modeling [58] approaches, which are particularly popular in the industrial domain, is not suitable for medical AD. The performance of these methods in medical images, as shown in Table 13, is inferior to that of other strategies utilizing ImageNet weights, as indicated in Table 6. This observation prompts us to reconsider how we can enhance these commonly used strategies in industrial AD and adapt them effectively to the medical domain.

Table 13: Performance of SOTA feature reference-based methods.

0.6

Table 14: Performance of VLM-based methods [127] under the zero-shot setting. *The performance of the officially released weights.

Moreover, the ImageNet pre-trained weights are definitely sub-optimal due to the gap between natural images and medical images, making fine-tuning on target datasets a promising direction. Although Reiss et al. [84] and Reiss and Hoshen [85] tried to investigate this point with PANDA and MSC respectively, the experiments in Tables 6 and 7 show that these methods do not achieve satisfactory improvement. Therefore, how to fine-tune the pre-trained features on the target datasets remains an unresolved problem.

Meanwhile, vision language models (VLMs) [83] have witnessed substantial advancements recently. Trained on vast amounts of image-text data, these models exhibit exceptional generalizability and robustness across various downstream tasks. Naturally, exploring the utilization of these powerful models from the aforementioned perspectives is a worthwhile endeavor [105].

## 5.5 Special settings for anomaly detection

In addition to the traditional OCC setting that involves only normal training data for AD, recent works have increasingly focused on more challenging and meaningful AD settings that closely resemble real-world scenarios.

One-class semi-supervised setting performs training using both normal data and unlabeled data, which may contain some anomalies. In this setting, a typical idea is to employ two modules to learn the data distribution: one is trained exclusively on normal data, while the other is trained on both normal and unlabeled data [22, 23, 19]. These methods utilize the discrepancy in reconstruction between the two modules to identify anomalies. Other approaches [100, 123] train a GAN-based model to eliminate potential diseases in the unlabeled data, generating healthy reconstruction for both normal and unlabeled inputs. The reconstruction error is then applied as an anomaly score.

It is noteworthy that the presence of various rare diseases poses a challenge in incorporating all types of anomalies into the unlabeled training set. In other words, the testing set may include numerous unseen anomaly types that never appeared in the unlabeled training set. This mismatch has been shown by Oliver et al. [76] to lead to significant performance degradation in traditional semi-supervised learning approaches.
To address this challenge, various approaches have been proposed in this setting. For instance, Cai et al. [22], Cai et al. [23] employed an additional module to capture the distribution of both normal and unlabeled training data as a complement to the normative module. This module serves as a complement, enhancing the ability to identify seen anomalies present in the unlabeled training data without negative impact on recognizing unseen anomalies. Siddiquee et al. [100] utilized the unlabeled training data to facilitate the model in generating pseudo-healthy reconstructions rather than recognizing seen anomalies, thereby enhancing generalization to unseen anomalies.

While methods in this setting exploit readily available unlabeled data to assist in AD, a sufficient number of normal samples are required to train the model. Therefore, exploring techniques to train an effective model with a smaller amount of data would further enhance its applicability in clinical practice.

Few-/Zero-shot setting trains AD methods with little to no samples from the target datasets. This setting has gained significant attention in industrial defect detection [43, 116, 27]. Recently, with the rapid advancement of VLMs, these models have been widely adopted for the few-/zero-shot setting [45, 44, 127, 61]. Compared to the one-class and one-class semi-supervised settings, this setting reduces the requirement for a large amount of normal training data, enabling rapid deployment of models in entirely new scenarios. However, the few-/zero-shot setting has not been extensively explored in the medical domain, and existing methods have not exhibited satisfactory performance on medical data, as indicated in Table 14. Medical images, with more complex variations than natural industrial images, pose additional challenges for developing AD approaches under this setting. Addressing these challenges remains a crucial area for future research.

## 5.6 3D anomaly detection

Similar to most prevailing methods for AD in medical images, our analysis relies on leveraging 2D information. Even in the case of 3D volumetric scans, such as MRIs, the common approach is to extract axial slices and analyze them as 2D images. However, this strategy overlooks crucial information in the axial direction, leading to sub-optimal performance in AD for volumetric medical images.

Several previous works have explored AD on volumetric medical images. One common strategy is to directly adapt 2D methods into the 3D domain by replacing 2D layers in networks with their 3D counterparts. For example, Simarro Viana et al. [102] developed a 3D version of f-AnoGAN. Cho et al. [32] and Marimont and Tarroni [70] adapted the one-stage SSL-based AD methods for volumetric CT scans or MRIs. Recognizing that 3D networks often encounter depth limitations due to memory constraints, Kang and Park [50] proposed joint embedding to combine the advantages of both 2D and 3D networks by aligning their representations in the embedding space. Additionally, Naval Marimont and Tarroni [74] introduced implicit field learning approaches [79] to reconstruct voxel intensities based on the latent variables of the volume and the spatial coordinates of the voxels.

While the exploration of 3D AD on medical images presents a new avenue, it remains an area that requires further investigation. The lack of medical datasets that support both 2D and 3D AD poses challenges for comparing the performance of 3D and 2D methods. Moreover, memory limitations in 3D networks restrict their network designs for effective feature extraction. Future research should prioritize addressing these issues and developing solutions to advance the field.

## 6 Conclusion

This paper presents a comprehensive benchmark for medical anomaly detection, incorporating seven datasets and a comparison of thirty typical methods. Our extensive evaluation and analysis reveal several key findings and challenges to guide future research in this field.

Firstly, in the absence of pre-training, reconstruction-based methods demonstrate greater robustness compared to SSL-based methods. Among the reconstruction-based methods, the simplest AE serves as a good baseline, delivering satisfactory performance across various datasets and near-perfect metrics on simple datasets like Hyper-Kvasir and OCT2017. Therefore, we strongly recommend researchers to include AE as a reference in their comparisons.
Moreover, our results highlight the importance of latent space configuration and reconstruction error measurement in reconstruction methods, which display a substantial impact on performance. Regarding latent space configuration, datasets with near OOD (e.g., local anomalies) tend to benefit from very small latent sizes. Among these datasets, the more complex ones exhibit increasing optimal values of latent size. Conversely, datasets with far OOD (e.g., global semantic anomalies) benefit from large latent sizes. In terms of reconstruction error measurement, it is crucial to employ a distance function that captures the anomaly-related semantic difference rather than only low-level intensity difference. This is why perceptual loss outperforms loss by a significant margin on most datasets. However, the current strategies for latent space configuration and reconstruction error measurement are still sub-optimal, presenting a promising avenue for further investigation.

Additionally, we observe that ImageNet pre-trained weights exhibit high effectiveness and potency in medical AD. They are successfully employed in various ways, including distance measurement, input data transformation, and direct feature extraction. Fine-tuning these weights on task-specific datasets to enhance performance remains an unresolved challenge. Furthermore, the recent advancements in vision-language models (VLMs) offer new possibilities for leveraging these powerful pre-trained models in AD.

Lastly, we identify several special settings for AD, such as the one-class semi-supervised setting and the zero-/few-shot setting, which closely align with real-world scenarios and warrant further exploration. Particularly, the significant progress in VLMs facilitates the development of zero-/few-shot methods for AD, which should attract more attention in the future.

Overall, our benchmark establishes a foundation for researchers in medical AD, providing insights into the typical methods. We hope that this work will contribute to the development of more effective and robust AD methods, ultimately benefiting the medical domain in recognizing rare diseases and improving health screening.
