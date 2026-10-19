<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# DRÆM – A discriminatively trained reconstruction embedding for surface anomaly detection

- **Authors:** Vitjan Zavrtanik; Matej Kristan; Danijel Skočaj
- **Venue / Year:** 2021 IEEE/CVF International Conference on Computer Vision (ICCV) · 2021
- **DOI:** 10.1109/ICCV48922.2021.00822
- **URL:** https://arxiv.org/abs/2108.07610
- **arXiv:** 2108.07610
- **Bibkey:** Zavrtanik2021_210807610
- **Type:** paper
- **Status:** complete

## Abstract
Visual surface anomaly detection aims to detect local image regions that significantly deviate from normal appearance. Recent surface anomaly detection methods rely on generative models to accurately reconstruct the normal areas and to fail on anomalies. These methods are trained only on anomaly-free images, and often require hand-crafted post-processing steps to localize the anomalies, which prohibits optimizing the feature extraction for maximal detection capability. In addition to reconstructive approach, we cast surface anomaly detection primarily as a discriminative problem and propose a discriminatively trained reconstruction anomaly embedding model (DRAEM). The proposed method learns a joint representation of an anomalous image and its anomaly-free reconstruction, while simultaneously learning a decision boundary between normal and anomalous examples. The method enables direct anomaly localization without the need for additional complicated post-processing of the network output and can be trained using simple and general anomaly simulations. On the challenging MVTec anomaly detection dataset, DRAEM outperforms the current state-of-the-art unsupervised methods by a large margin and even delivers detection performance close to the fully-supervised methods on the widely used DAGM surface-defect detection dataset, while substantially outperforming them in localization accuracy.

## Full text / Extract
<!-- Auto-extracted from the open arXiv v2 (2108.07610) with pdftotext; body text from Introduction to Conclusion. Numeric table bodies, figure graphics and the reference list are dropped (table captions kept) — see deep-read.md for the key numbers. Some two-column interleaving artefacts may remain. -->

### 1. Introduction

Surface anomaly detection addresses localization of image regions that deviate from a normal appearance (Figure 1). A closely related general anomaly detection problem considers anomalies as entire images that significantly differ from the non-anomalous training set images. In contrast, in surface anomaly detection problems, the anomalies occupy only a small fraction of image pixels and are typically close to the training set distribution. This is a particu1

synthetic appearance, but rather learns a local-appearanceconditioned distance function between the original and reconstructed anomaly appearance, which generalizes well over a range of real anomalies (see Figure 2, bottom). To validate our hypothesis, we propose, as our main contribution, a new deep surface anomaly detection network, discriminatively trained in an end-to-end manner on synthetically generated just-out-of-distribution patterns, which do not have to faithfully represent the target-domain anomalies. The network is composed of a reconstructive subnetwork, followed by a discriminative sub-network (Figure 3). The reconstructive sub-network is trained to learn anomaly-free reconstruction, while the discriminative subnetwork learns a discriminative model over the joint appearance of the original and reconstructed images, producing a high-fidelity per-pixel anomaly detection map (Figure 1). In contrast to related approaches that learn surrogate generative tasks, the proposed model is trained discriminatively, yet does not require the synthetic anomaly appearances to closely match the anomalies at test time and outperforms the recent, more complex, state-of-the-art methods by a large margin.

Figure 2. Autoencoders over-generalize to anomalies, while discriminative approaches over-fit to the synthetic anomalies and do not generalize to real data. Our approach jointly discriminatively learns the reconstruction subspace and a hyper-plane over the joint original and reconstructed space using the simulated anomalies and leads to substantially better generalization to real anomalies.

### 2. Related work

Many surface anomaly detection methods focus on image reconstruction and detect anomalies based on image reconstruction error [1, 2, 5, 24, 23, 26, 31]. Auto-encoders are commonly used for image reconstruction [5]. In [1, 2, 26] auto-encoders are trained with adversarial losses. The anomaly score of the image is then based on the image reconstruction quality or in the case of adversarially trained auto-encoders, the discriminator output. In [24, 23] a GAN [13] is trained to generate images that fit the training distribution. In [23] an encoder network is additionally trained that finds the latent representation of the input image that minimizes the reconstruction loss when used as the input by the pretrained generator. The anomaly score is then based on the reconstruction quality and the discriminator output. In [29] an interpolation auto-encoder is trained to learn a dense representation space of in-distribution samples. The anomaly score is then based on a discriminator, trained to estimate the distance between the input-input and input-output joint distributions, however the approach to surface anomaly detection remains generative as the discriminator evaluates the reconstruction quality. Instead of the commonly used image space reconstruction, the reconstruction of pretrained network features can also be used for surface anomaly detection [4, 25]. Anomalies are detected based on the assumption that features of a pre-trained network will not be faithfully reconstructued by another network trained only on anomaly-free images. Alternatively [20, 11] propose surface anomaly detection as identifying significant deviations from a Gaussian fitted to

construction. However, determining the presence of anomalies that are not substantially different from normal appearance remains challenging, since these are often well reconstructed, as depicted in Figure 2, top-left. Recent improvements thus consider the difference between deep features extracted from a general-purpose network and a network specialized for anomaly-free images [4]. Discrimination can also be formulated as a deviation from a dense clustering of non-anomalous textures within the deep subspace [22, 7], as forming such a compact subspace prevents anomalies from being mapped close to anomaly-free samples. A common drawback of the generative methods is that they only learn the model from anomaly-free data, and are not explicitly optimized for discriminative anomaly detection, since positive examples (i.e., anomalies) are not available at training time. Synthetic anomalies could be considered to train discriminative segmentation methods [8, 21], but this leads to over-fitting to synthetic appearances and results in a learned decision boundary that generalizes poorly to real anomalies (Figure 2, top-right). We hypothesize that over-fitting can be substantially reduced by training a discriminative model over the joint, reconstructed and original, appearance along with the reconstruction subspace. This way the model does not overfit to

Ir , centered at image coordinates (i, j). The reconstruction loss is therefore:

anomaly-free features of a pre-trained network. This requires a unimodal distribution of the anomaly-free visual features which is problematic on diverse datasets. [16] propose a one-class variational auto-encoder gradient-based attention maps as output anomaly maps. However the method is sensitive to subtle anomalies close to the normal sample distribution. Recently Patch-based one-class classification methods have been considered for surface anomaly detection [30]. These are based on one-class methods [22, 7] which attempt to estimate a decision boundary around anomaly-free data that separates it from anomalous samples by assuming a unimodal distribution of the anomaly-free data. This assumption is often violated in surface anomaly data.

Lrec (I, Ir ) = λLSSIM (I, Ir ) + l2 (I, Ir ),

where λ is a loss balancing hyper-parameter. Note that an additional training signal is acquired from the downstream discriminative network (Section 3.2), which performs anomaly localization by detecting the reconstruction difference.

### 3.2. Discriminative sub-network

The discriminative sub-network uses U-Net [21]-like architecture. The sub-network input Ic is defined as the channel-wise concatenation of the reconstructive subnetwork output Ir and the input image I. Due to the normality-restoring property of the reconstructive subnetwork, the joint appearance of I and Ir differs significantly in anomalous images, providing the information necessary for anomaly segmentation. In reconstruction-based anomaly detection methods anomaly maps are obtained using similarity functions such as SSIM [27] to compare the original image to its reconstruction, however a surface anomaly detection-specific similarity measure is difficult to hand-craft. In contrast, the discriminative sub-network learns the appropriate distance measure automatically. The network outputs an anomaly score map Mo of the same size as I. Focal Loss [14] (Lseg ) is applied on the discriminative sub-network output to increase robustness towards accurate segmentation of hard examples. Considering both the segmentation and the reconstructive objectives of the two sub-networks, the total loss used in training DRÆM is

### 3. DRÆM

The proposed discriminative joint reconstructionanomaly embedding method (DRÆM) is composed from a reconstructive and a discriminative sub-networks (see Figure 3). The reconstructive sub-network is trained to implicitly detect and reconstruct the anomalies with semantically plausible anomaly-free content, while keeping the non-anomalous regions of the input image unchanged. Simultaneously, the discriminative sub-network learns a joint reconstruction-anomaly embedding and produces accurate anomaly segmentation maps from the concatenated reconstructed and original appearance. Anomalous training examples are created by a conceptually simple process that simulates anomalies on anomaly-free images. This anomaly generation method provides an arbitrary amount of anomalous samples as well as pixel-perfect anomaly segmentation maps which can be used for training the proposed method without real anomalous samples.

L(I, Ir , Ma , M ) = Lrec (I, Ir ) + Lseg (Ma , M ),

### 3.1. Reconstructive sub-network

where Ma and M are the ground truth and the output anomaly segmentation masks, respectively.

The reconstructive sub-network is formulated as an encoder-decoder architecture that converts the local patterns of an input image into patterns closer to the distribution of normal samples. The network is trained to reconstruct the original image I from an artificially corrupted version Ia obtained by a simulator (see Section 3.3). An l2 loss is often used in reconstruction based anomaly detection methods [1, 2], however this assumes an independence between neighboring pixels, therefore a patch based SSIM [27] loss is additionally used as in [5, 31]: LSSIM (I, Ir ) =

### 3.3. Simulated anomaly generation

DRÆM does not require simulations to realistically reflect the real anomaly appearance in the target domain, but rather to generate just-out-of-distribution appearances, which allow learning the appropriate distance function to recognize the anomaly by its deviation from normality. The proposed anomaly simulator follows this paradigm. A noise image is generated by a Perlin noise generator [18] to capture a variety of anomaly shapes (Figure 4, P ) and binarized by a threshod sampled uniformly at random (Figure 4, Ma ) into an anomaly map Ma . The anomaly texture source image A is sampled from an anomaly source image dataset which is unrelated to the input image distribution (Figure 4, A). Random augmentation sampling, inspired by RandAugment [10], is then applied by a set

1 XX

1 − SSIM I, Ir (i,j) , (1) Np i=1 j=1

where H and W are the height and width of image I, respectively. Np is equal to the number of pixels in I. Ir is the reconstructed image output by the network. SSIM (I, Ir )(i,j) is the SSIM value for patches of I and

Reconstructive sub-network

Discriminative sub-network

Figure 3. The anomaly detection process of the proposed method. First anomalous regions are implicitly detected and inpainted by the reconstructive sub-network trained using Lrec . The output of the reconstructive sub-network and the input image are then concatenated and fed into the discriminative sub-network. The segmentation network, trained using the Focal loss Lf ocal [14], localizes the anomalous region and produces an anomaly map. The image level anomaly score η is acquired from the anomaly score map.

of 3 random augmentation functions sampled from the set: {posterize, sharpness, solarize, equalize, brightness change, color change, auto-contrast}. The augmented texture image A is masked with the anomaly map Ma and blended with I to create anomalies that are just-out-ofdistribution, and thus help tighten the decision boundary in the trained network. The augmented training image Ia is therefore defined as Ia = M a

where M a is the inverse of Ma , is the element-wise multiplication operation and β is the opacity parameter in blending. This parameter is sampled uniformly from an interval, i.e., β ∈ [0.1, 1.0]. The randomized blending and augmentation afford generating diverse anomalous images from as little as a single texture (see Figure 5). The above described simulator thus generates training sample triplets containing the original anomaly-free image I, the augmented image containing simulated anomalies Ia and the pixel-perfect anomaly mask Ma .

Figure 4. Simulated anomaly generation process. The binary anomaly mask Ma is generated from Perlin noise P . The anomalous regions are sampled from A according to Ma and placed on the anomaly free image I to generate the anomalous image Ia .

### 3.4. Surface anomaly localization and detection

The output of the discriminative sub-network is a pixellevel anomaly detection mask Mo , which can be interpreted in a straight-forward way for the image-level anomaly score estimation, i.e., whether an anomaly is present in the image. First, Mo is smoothed by a mean filter convolution layer to aggregate the local anomaly response information. The final image-level anomaly score η is computed by taking the maximum value of the smoothed anomaly score map: η = max Mo ∗ fsf ×sf ,

Figure 5. The original anomaly source image (left) can be augmented several times (center) to generate a wide variety of simulated anomalous regions (right).

where fsf ×sf is a mean filter of size sf × sf and ∗ is the convolution operator. In a preliminary study, we trained a classification network for the image-level anomaly classification, but did not observe improvements over the direct score estimation method (5).

Class bottle capsule grid leather pill tile transistor zipper cable carpet hazelnut metal nut screw toothbrush wood

### 4. Experiments

DRÆM is extensively evaluated and compared with the recent state-of-the-art on unsupervised surface anomaly detection and localization. Additionally, individual components of the proposed method and the effectiveness of training on simulated anomalies are evaluated by an ablation study. Finally, the results are placed in a broader perspective by comparing DRÆM with state-of-the-art weaklysupervised and fully-supervised surface-defect detection methods.

### 4.1. Comparison with unsupervised methods

DRÆM is evaluated on the recent challenging MVTec anomaly detection dataset [3], which has been established as a standard benchmark dataset for evaluating unsupervised surface anomaly detection methods. We evaluate DRÆM on the tasks of surface anomaly detection and localisation. The MVTec dataset contains 15 object classes with a diverse set anomalies which enables a general evaluation of surface anomaly detection methods. Anomalous examples of the MVTec dataset are shown in Figure 8. For evaluation, the standard metric in anomaly detection, AUROC, is used. Image-level AUROC is used for anomaly detection and a pixel-based AUROC for evaluating anomaly localization [5, 24, 17, 26]. The AUROC, however, does not reflect the localization accuracy well in surface anomaly detection setups, where only a small fraction of pixels are anomalous. The reason is that false positive rate is dominated by the a-priori very high number of non-anomalous pixels and is thus kept low despite of false positive detections. We thus additionally report the pixel-wise average precision metric (AP), which is more appropriate for highly imbalanced classes and in particular for surface anomaly detection, where the precision plays an important role. In our experiments, the network is trained for 700 epochs on the MVTec anomaly detection dataset [3]. The learning rate is set to 10−4 and is multiplied by 0.1 after 400 and 600 epochs. Image rotation in the range of (−45, 45) degrees is used as a data augmentation method on anomaly free images during training to alleviate overfitting due to the relatively small anomaly-free training set size. The Describable Textures Dataset [9] is used as the anomaly source dataset. A number of obtained qualitative examples are presented in Figure 8. As one can observe, the obtained anomaly masks are very detailed and resemble the given ground truth labels to a high degree of accuracy. Consequently, DRÆM achieves state-of-the-art quantitative results across all MVTec classes for surface anomaly detection as well as localization. Surface Anomaly Detection. Table 1 quantitatively compares DRÆM with recent approaches on the task of image-level surface anomaly detection. DRÆM significantly outperforms all recent surface anomaly detec-

Table 1. Results for the task of surface anomaly detection on the MVTec dataset (AUROC). An average score over all classes is also reported the last row (avg).

tion methods, achieving the highest AUROC in 9 out of 15 classes and achieving comparable results in the other classes. It surpasses the previous best state-of-the-art approach by 2.5 percentage points. The reduced performance in some classes could be explained by particularly difficult anomalies that are close to the normal image distribution. The absence of a part of the object is especially difficult to detect. Regions, where the object features are missing, usually contain other commonly occurring features. This makes such anomalies difficult to distinguish from anomaly-free regions. An example of this can be seen in Figure 6, where some of the transistor leads had been cut. The ground truth marks the area where the broken lead should be as anomalous. DRÆM only detects anomalous features in a small region of the cut lead, as the background features are common during training. Anomaly Localization. Table 2 compares DRÆM to the recent state-of-the-art on the task of pixel-level surface anomaly detection. DRÆM achieves comparable results to the previous best-performing methods in terms of AUROC scores and surpasses the state-of-the-art by 13.4 percentage points in terms of AP. A better AP score is achieved in 11 out of 15 classes and is comparable to the state-of-the-art in other classes. A qualitative comparison with the state-ofthe-art method Uninformed Students [4] and PaDim [11] is shown in Figure 7. DRÆM achieves a significant improvement in anomaly segmentation accuracy. A detailed inspection showed that some of the detection errors can be attributed to the inaccurate ground truth labels on ambiguous anomalies. An example of this is shown in Figure 6, where the ground truth covers the entire surface of the pill, yet only the yellow dots are anomalous. DRÆM produces an anomaly map that correctly localizes the yellow dots, but the discrepancy with the ground truth mask

### 4.2. Ablation Study

The DRÆM design choices are analyzed by groups of experiments evaluating (i) the method architecture, (ii) the choice of anomaly appearance patterns and (iii) low perturbation example generation. Results are visually grouped by shades of gray in Table 3. Architecture. The DRÆM reconstructive sub-network impact on the downstream surface anomaly detection performance is evaluated by removing it from the pipeline and training the discriminative sub-network alone. The results are shown in Table 3, experiment Disc. Note a reduction in performance in comparison to the full DRÆM architecture (Table 3, experiment DRÆM). The performance drop is due to overfitting of the discriminative sub-network to the simulated anomalies, which are not a faithful representation of the real ones. Next, the discriminative power of the reconstructive subnetwork alone is analyzed by evaluating it as an autoencoder-based surface anomaly detector. The reconstructed image output of the sub-network is compared to the input image using the SSIM function [27] to generate the anomaly map. The results of this approach are shown in Table 3, experiment Recon.-AE. Recon.-AE outperforms the recent auto-encoder-based surface anomaly detection method AESSIM[5] (see results in Table 2) This suggests that simulated anomaly training introduces additional information into the auto-encoder-based training, but judging by the performance gap to DRÆM, the SSIM similarity function may not be optimal for extraction of the anomaly information. Indeed, using the recently proposed similarity function MSGMS [31] (Recon.-AEM SGM S ) improves the performance, but the results are still significantly worse than when using the entire DRÆM architecture, which indicates that both reconstructive and discriminative parts are required for optimal results. To further emphasize the contribution of the DRÆM backbone, we replace it entirely by the recent state-of-theart supervised discriminative surface anomaly detection network [6] and re-train with the simulated anomalies (Table 3, Božič et al.). Performance substantially drops, which further supports the power of learning the anomaly deviation extent from normality rather than the anomaly or normality appearance. Anomaly appearance patterns. DRÆM is re-trained using ImageNet [12] as the texture source in the anomaly simulator to study the influence of the anomaly generation dataset (DRÆMImageN et in Table 3). Results are comparable to using the much smaller DTD [9] dataset. Figure 9 shows the performance at various anomaly source dataset sizes. Results suggest that the augmentation and opacity randomization substantially contribute to performance allowing remarkably small number of texture images (less than 10). As an extreme case, the anomaly textures are

Figure 6. The original image (a) contains anomalies which are difficult to mark in the ground truth mask (b) which causes a discrepancy between the ground truth and the output anomaly map (c,d).

Figure 7. The anomalous images are shown in the first row. The middle three rows show the anomaly maps generated by our implementation of Uninformed Students [4], PaDim [11] and DRÆM, respectively. The last row shows the direct anomaly map output of DRÆM.

increases the performance error. These annotation ambiguities also impact the AP score of the evaluated methods. Class bottle capsule grid leather pill tile transistor zipper cable carpet hazelnut metal nut screw toothbrush wood

Table 2. Results for the task of anomaly localization on the MVTec dataset (AUROC / AP).

Figure 8. Qualitative examples. The original image, the anomaly map overlay, the anomaly map and the ground truth map are shown.

Method Disc. Recon.-AE Recon.-AEM SGM S Božič et al. [6] DRÆMImageN et DRÆMcolor DRÆMrect DRÆMno aug DRÆMimg aug DRÆMβ DRÆM

Architecture Recon. Net. Discr. Net.

Anomaly Generation ImageNet DTD Perlin

Table 3. Surface anomaly detection (Det.) and localization (Loc.) experiments of the ablation study grouped by shades of gray into (i) method architecture, (ii) anomaly source dataset, (iii) hard simulated anomaly generation, (iv) simulated anomaly shape, and (v) the performance of DRÆM for reference.

generated as homogeneous regions of a randomly sampled color (DRÆMcolor ). Note that DRÆMcolor still achieves state-of-the-art results, further suggesting that DRÆM does not require simulations to closely match the real anomalies. The impact of the anomaly shape generator is evaluated by replacing the Perlin noise generator by a rectangular region generator. The anomaly mask is thus generated by sampling multiple rectangular areas for the anomalous regions (DRÆMrect in Table 3). Training on rectangular anomalies causes only a slight performance drop and suggests that the simulated anomaly shape does not have to be realistic to generalize well to real world anomalies. Examples of anomalies generated in anomaly appearance ablation experiments are shown in Figure 10. Low perturbation examples. The anomaly source image augmentation and the opacity randomization are re-

sponsible for tightening the decision boundary around the anomaly-free training distribution. Table 3 reports the results of DRÆM variants trained (i) without image augmentation and opacity randomization (DRÆMno aug ), (ii) using only image augmentation (DRÆMimg aug ) and (iii) using only opacity randomization (DRÆMβ ). There is a significant localization performance gap between DRÆMno aug and DRÆM, however, this can be significantly narrowed by using the opacity randomization in training even without image data augmentation.

### 4.3. Comparison with supervised methods

Supervised methods require anomaly annotations at training time and cannot be evaluated on MVTec. We thus compare DRÆM with the supervised methods on the DAGM dataset [28] that contains 10 textured object classes

Methods RIAD [31] US [4] MAD [20] PaDim [11] DRÆM CADN [32] Rački et al. [19] Lin et al. [15] Božič et al. [6]

Table 4. DRÆM outperforms unsupervised methods on DAGM dataset and performs on par with fully supervised ones.

Figure 9. DRÆM achieves a remarkable detection and localization performance already at as low as 10 texture source images in the simulator when augmentation is applied.

Figure 10. Anomalies simulated using the DTD [9] (DRÆM), ImageNet [12] (DRÆMImageN et ), homogeneous color regions (DRÆMcolor ) and rectangular masks (DRÆMrect ), from left to right.

Figure 11. Supervised methods replicate the approximate ground truth training annotations, leading to a low localization accuracy. DRÆM does not use the ground truth, yet produces far better localization.

with small anomalies visually very similar to the background, which makes the dataset particularly challenging for the unsupervised methods. DRÆM is trained only on anomaly-free training samples using the same parameters as in previous experiments. The standard evaluation protocol on this dataset [19, 32, 15, 6] is used – the challenge is to classify whether the image contains the anomaly; localization accuracy is not measured, since the anomalies are only coarsely labeled. Table 4 shows that the best fully supervised methods nearly perfectly classify anomalous images, while the stateof-the-art unsupervised methods like RIAD [31] and US [4] struggle with subtle anomalies on highly textured regions1 . DRÆM significantly outperforms these methods, and even the weakly supervised CADN [32] by a large margin, obtaining classification performance close to the best fullysupervised methods, which is a remarkable result. Furthermore, DRÆM outperforms all supervised methods in terms of anomaly localization accuracy on this dataset. Since the training images are only coarsely annotated with ellipses that approximately cover the surface defects and contain background, the supervised methods produce inaccurate localization in test images as well. In contrast, DRÆM does not use the labels at all, and thus produces more accurate anomaly maps, as shown in Figure 11.

### 5. Conclusion

A discriminative end-to-end trainable surface anomaly detection and localization method DRÆM was presented. DRÆM outperforms the current state-of-the-art on the MVTec dataset [3] by 2.5 AUROC points on the surface anomaly detection task and by 13.5 AP points on the localization task. On the DAGM dataset [28], DRÆM delivers anomalous image classification accuracy close to fully supervised methods, while outperforming them in localization accuracy. This is a remarkable result since DRÆM is not trained on real anomalies. In fact, a detailed analysis shows that our paradigm of learning a joint reconstruction-anomaly embedding through a reconstructive sub-network significantly improves the results over standard methods and that an accurate decision boundary can be well estimated by learning the extent of deviation from reconstruction on simple simulations rather than learning either the normality or real anomaly appearance.
