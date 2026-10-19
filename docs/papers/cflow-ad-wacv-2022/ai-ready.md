<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# CFLOW-AD: Real-Time Unsupervised Anomaly Detection with Localization via Conditional Normalizing Flows

- **Authors:** Denis Gudovskiy; Shun Ishizaka; Kazuki Kozuka
- **Venue / Year:** 2022 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV) · 2022
- **DOI:** 10.1109/WACV51458.2022.00188
- **URL:** https://arxiv.org/abs/2107.12571
- **arXiv:** 2107.12571
- **Bibkey:** Gudovskiy2021_210712571
- **Type:** paper
- **Status:** complete

## Abstract
Unsupervised anomaly detection with localization has many practical applications when labeling is infeasible and, moreover, when anomaly examples are completely missing in the train data. While recently proposed models for such data setup achieve high accuracy metrics, their complexity is a limiting factor for real-time processing. In this paper, we propose a real-time model and analytically derive its relationship to prior methods. Our CFLOW-AD model is based on a conditional normalizing flow framework adopted for anomaly detection with localization. In particular, CFLOW-AD consists of a discriminatively pretrained encoder followed by a multi-scale generative decoders where the latter explicitly estimate likelihood of the encoded features. Our approach results in a computationally and memory-efficient model: CFLOW-AD is faster and smaller by a factor of 10x than prior state-of-the-art with the same input setting. Our experiments on the MVTec dataset show that CFLOW-AD outperforms previous methods by 0.36% AUROC in detection task, by 1.12% AUROC and 2.5% AUPRO in localization task, respectively. We open-source our code with fully reproducible experiments.

## Full text / Extract
<!-- Auto-extracted from the open arXiv v1 (2107.12571) with pdftotext; body text from Introduction to Conclusion. Numeric table bodies, figure graphics and the reference list are dropped (table captions kept) — see deep-read.md for the key numbers. Some two-column interleaving artefacts may remain. -->

### 1. Introduction

Anomaly detection with localization (AD) is a growing area of research in computer vision with many practical applications e.g. industrial inspection [4], road traffic monitoring [20], medical diagnostics [44] etc. However, the common supervised AD [32] is not viable in practical applications due to several reasons. First, it requires labeled data which is costly to obtain. Second, anomalies are usually rare long-tail examples and have low probability to be acquired by sensors. Lastly, consistent labeling of anomalies is subjective and requires extensive domain expertise as illustrated in Figure 1 with industrial cable defects.

1 Our code is available at github.com/gudovskiy/cflow-ad

With these limitations of the supervised AD, a more appealing approach is to collect only unlabeled anomaly-free images for train dataset Dtrain as in Figure 1 (top row). Then, any deviation from anomaly-free images is classified as an anomaly. Such data setup with low rate of anomalies is generally considered to be unsupervised [4]. Hence, the AD task can be reformulated as a task of out-of-distribution detection (OOD) with the AD objective. While OOD for low-dimensional industrial sensors (e.g. power-line or acoustic) can be accomplished using a common k-nearest-neighbor or more advanced clustering methods [10], it is less trivial for high-resolution images. Re-

cently, convolutional neural networks (CNNs) have gained popularity in extracting semantic information from images into downsampled feature maps [4]. Though feature extraction using CNNs has relatively low complexity, the postprocessing of feature maps is far from real-time processing in the state-of-the-art unsupervised AD methods [8]. To address this complexity drawback, we propose a CFLOW-AD model that is based on conditional normalizing flows. CFLOW-AD is agnostic to feature map spatial dimensions similar to CNNs, which leads to a higher accuracy metrics as well as a lower computational and memory requirements. We present the main idea behind our approach in a toy OOD detector example in Figure 1. A distribution of the anomaly-free image patches x with probability density function pX (x) is learned by the AD model. Our translation-equivariant model is trained to transform the original distribution with pX (x) density into a Gaussian distribution with pZ (z) density. Finally, this model separates in-distribution patches z with pZ (z) from the outof-distribution patches with pZ̃ (z) using a threshold τ computed as the Euclidean distance from the distribution mean.

anomaly scores proxies. These fully-generative models are unable to estimate the exact data likelihoods [6, 24] and do not perform better than the traditional methods [25, 7] according to MVTec survey in [4]. Recent works [34, 15] show that these models tend to capture only low-level correlations instead of relevant semantic information. To overcome the latter drawback, a hybrid DFR model [37] uses a pretrained feature extractor with multi-scale pyramid pooling followed by a convolutional autoencoder (CAE). However, DFR model is unable to estimate the exact likelihoods. Another line of research proposes to employ a studentteacher type of framework [5, 33, 41]. Teacher is a pretrained feature extractor and student is trained to estimate a scoring function for AD. Unfortunately, such frameworks underperform compared to state-of-the-art models. Patch SVDD [42] and CutPaste [19] introduce a selfsupervised pretraining scheme for AD. Moreover, Patch SVDD proposes a novel method to combine multi-scale scoring masks to a final anomaly map. Unlike the nearestneighbor search in [42], CutPaste estimates anomaly scores using an efficient Gaussian density estimator. While the self-supervised pretraining can be helpful in uncommon data domains, Schirrmeister et al. [34] argue that large natural-image datasets such as ImageNet can be a more representative for pretraining compared to a small applicationspecific datasets e.g. industrial MVTec [4]. The state-of-the-art PaDiM [8] proposes surprisingly simple yet effective approach for anomaly localization. Similarly to [37, 7, 42], this approach relies on ImageNetpretrained feature extractor with multi-scale pyramid pooling. However, instead of slow test-time clustering in [7] or nearest-neighbor search in [42], PaDiM uses a wellknown Mahalanobis distance metric [23] as an anomaly score. The metric parameters are estimated for each feature vector from the pooled feature maps. PaDiM has been inspired by Rippel et al. [29] who firstly advocated to use this measure for anomaly detection without localization. DifferNet [30] uses a promising class of generative models called normalizing flows (NFLOWs) [9] for image-level AD. The main advantage of NFLOW models is ability to estimate the exact likelihoods for OOD compared to other generative models [35, 36, 3, 38, 37]. In this paper, we extend DifferNet approach to pixel-level anomaly localization task using our CFLOW-AD model. In contrast to RealNVP [9] architecture with global average pooling in [30], we propose to use conditional normalizing flows [2] to make CFLOW-AD suitable for low-complexity processing of multi-scale feature maps for localization task. We develop our CFLOW-AD with the following contributions:

### 2. Related work

We review models2 that employ the data setup from Figure 1 and provide experimental results for popular MVTec dataset [4] with factory defects or Shanghai Tech Campus (STC) dataset [22] with surveillance camera videos. We highlight the research related to a more challenging task of pixel-level anomaly localization (segmentation) rather than a more simple image-level anomaly detection. Napoletano et al. [25] propose to use CNN feature extractors followed by a principal component analysis and kmean clustering for AD. Their feature extractor is a ResNet18 [13] pretrained on a large-scale ImageNet dataset [16]. Similarly, SPADE [7] employs a Wide-ResNet-50 [43] with multi-scale pyramid pooling that is followed by a k-nearestneighbor clustering. Unfortunately, clustering is slow at test-time with high-dimensional data. Thus, parallel convolutional methods are preferred in real-time systems. Numerous methods are based on a natural idea of generative modeling. Unlike models with the discriminativelypretrained feature extractors [25, 7], generative models learn distribution of anomaly-free data and, therefore, are able to estimate a proxy metrics for anomaly scores even for the unseen images with anomalies. Recent models employ generative adversarial networks (GANs) [35, 36] and variational autoencoders (VAEs) [3, 38]. A fully-generative models [35, 36, 3, 38] are directly applied to images in order to estimate pixel-level probability density and compute per-pixel reconstruction errors as

• Our theoretical analysis shows why multivariate Gaussian assumption is a justified prior in previous models and why a more general NFLOW framework objective converges to similar results with the less compute.

2 For comprehensive review of the existing AD methods we refer readers to Ruff et al. [31] and Pang et al. [26] surveys.

• We propose to use conditional normalizing flows for unsupervised anomaly detection with localization using computational and memory-efficient architecture.

This framework with MVG distribution assumption shows its effectiveness in image-level anomaly detection task [29] and is adopted by the state-of-the-art PaDiM [8] model in pixel-level anomaly localization task.

• We show that our model outperforms previous stateof-the art in both detection and localization due to the unique properties of the proposed CFLOW-AD model.

### 3.3. Relationship with the flow framework

Dinh et al. [9] introduce a class of generative probabilistic models called normalizing flows. These models apply change of variable formula to fit an arbitrary density pZ (z) by a tractable base distribution with pU (u) density and a bijective invertible mapping g −1 : Z → U . Then, the loglikelihood of any z ∈ Z can be estimated by

### 3. Theoretical background

### 3.1. Feature extraction with Gaussian prior

Consider a CNN h(λ) trained for classification task. Its parameters λ are usually found by minimizing KullbackLeibler (DKL ) divergence between joint train data distribution Qx,y and the learned model distribution Px,y (λ), where (x, y) is an input-label pair for supervised learning. Typically, the parameters λ are initialized by the values sampled from the Gaussian distribution [12] and optimization process is regularized as arg min DKL [Qx,y kPx,y (λ)] + αR(λ),

log p̂Z (z, θ) = log pU (u) + log |det J | ,

where a sample u ∼ pU is usually from standard MVG distribution (u ∼ N (0, I)) and a matrix J = ∇z g −1 (z, θ) is the Jacobian of a bijective invertible flow model (z = g(u, θ) and u = g −1 (z, θ)) parameterized by vector θ. The flow model g(θ) is a set of basic layered transformations with tractable Jacobian determinants. For example, log | det J | in RealNVP [9] coupling layers is a simple sum of layer’s diagonal elements. These models are optimized using stochastic gradient descent by maximizing loglikelihood in (4). Equivalently, optimization can be done by minimizing the reverse DKL [p̂Z (z, θ)kpZ (z)] [27], where p̂Z (z, θ) is the model prediction and pZ (z) is a target density. The loss function for this objective is defined as

where R(λ) is a regularization term and α is a hyperparameter that defines regularization strength. The most popular CNNs [13, 43] are trained with L2 weight decay [17] regularization (R(λ) = kλk22 ). That imposes multivariate Gaussian (MVG) prior not only to parameters λ, but also to the feature vectors z extracted from the feature maps of h(λ) [11] intermediate layers.

### 3.2. A case for Mahalanobis distance

L(θ) = Ep̂Z (z,θ) [log p̂Z (z, θ) − log pZ (z)] .

With the same MVG prior assumption, Lee et al. [18] recently proposed to model distribution of feature vectors z by MVG density function and to use Mahalanobis distance [23] as a confidence score in CNN classifiers. Inspired by [18], Rippel et al. [29] adopt Mahalanobis distance for anomaly detection task since this measure determines a distance of a particular feature vector z to its MVG distribution. Consider a MVG distribution N (µ, Σ) with a density function pZ (z) for random variable z ∈ RD defined as

pZ (z) = (2π)−D/2 det Σ−1/2 e− 2 (z−µ) Σ

If pZ (z) is distributed according to Section 3.1 MVG assumption, we can express (5) as a function of Mahalanobis distance M (z) using its definition from (3) as | det J | M (z) − E 2 (u) + log L(θ) = Ep̂Z (z,θ) det Σ−1/2 where E 2 (u) = kuk22 is a squared Euclidean distance of a sample u ∼ N (0, I) (detailed proof in Appendix A). Then, the loss in (6) converges to zero when the likelihood contribution term | det J | of the model g(θ) (normalized by det Σ−1/2 ) compensates the difference between a squared Mahalanobis distance for z from the target density and a squared Euclidean distance for u ∼ N (0, I). This normalizing flow framework can estimate the exact likelihoods of any arbitrary distribution with pZ density, while Mahalanobis distance is limited to MVG distribution only. For example, CNNs trained with L1 regularization would have Laplace prior [11] or have no particular prior in the absence of regularization. Moreover, we introduce conditional normalizing flows in the next section and show that they are more compact in size and have fully-convolutional parallel architecture compared to [7, 8] models.

where µ ∈ R is a mean vector and Σ ∈ R is a covariance matrix of a true anomaly-free density pZ (z). Then, the Mahalanobis distance M (z) is calculated as M (z) = (z − µ)T Σ−1 (z − µ), Since the true anomaly-free data distribution is unknown, mean vector and covariance matrix from (3) are replaced by the estimates µ̂ and Σ̂ calculated from the empirical train dataset Dtrain . At the same time, density function pZ̃ (z) of anomaly data has different µ̃ and Σ̃ statistics, which allows to separate out-of-distribution and indistribution feature vectors using M (z) from (3).

Figure 2. Overview of our CFLOW-AD with a fully-convolutional translation-equivariant architecture. Encoder h(λ) is a CNN feature extractor with multi-scale pyramid pooling. Pyramid pooling captures both global and local semantic information with the growing from top to bottom receptive fields. Pooled feature vectors zik are processed by a set of decoders gk (θk ) independently for each kth scale. Our decoder is a conditional normalizing flow network with a feature input zik and a conditional input cki with spatial information from a positional encoder (PE). The estimated multi-scale likelihoods pki are upsampled to the input size and added up to produce anomaly map.

### 4. The proposed CFLOW-AD model

sumed to be independent of their spatial location in the general framework. To increase efficacy of distribution modeling, we propose to incorporate spatial prior into g(θ) model using conditional flow framework. In addition, we model p̂kZ (z, θ) densities using K independent decoder models gk (θk ) due to multi-scale feature pyramid pooling setup. Our conditional normalizing flow (CFLOW) decoder architecture is presented in Figure 2. We generate a conditional vector cki using a 2D form of conventional positional encoding (PE) [39]. Each cki ∈ RCk contains sin and cos harmonics that are unique to its spatial location (hk , wk )i . We extend unconditional flow framework to CFLOW by concatenating the intermediate vectors inside decoder coupling layers with the conditional vectors ci as in [2]. Then, the kth CFLOW decoder contains a sequence of conventional coupling layers with the additional conditional input. Each coupling layer comprises of fully-connected layer with (Dk +Ck )×(Dk +Ck ) kernel, softplus activation and output vector permutations. Usually, the conditional extension does not increase model size since Ck Dk . For example, we use the fixed Ck = 128 in all our experiments. Our CFLOW decoder has translation-equivariant architecture, because it slides along feature vectors extracted from the intermediate feature maps with kernel parameter sharing. As a result, both the encoder h(λ) and decoders gk (θk ) have convolutional translation-equivariant architectures. We train CFLOW-AD using a maximum likelihood objective, which is equivalent to minimizing loss defined by

### 4.1. CFLOW encoder for feature extraction

We implement a feature extraction scheme with multiscale feature pyramid pooling similar to recent models [7, 8]. We define the discriminatively-trained CNN feature extractor as an encoder h(λ) in Figure 2. The CNN encoder maps image patches x into a feature vectors z that contain relevant semantic information about their content. CNNs accomplish this task efficiently due to their translationequivariant architecture with the shared kernel parameters. In our experiments, we use ImageNet-pretrained encoder following Schirrmeister et al. [34] who show that large natural-image datasets can serve as a representative distribution for pretraining. If a large application-domain unlabeled data is available, the self-supervised pretraining from [42, 19] can be a viable option. One important aspect of a CNN encoder is its effective receptive field [21]. Since the effective receptive field is not strictly bounded, the size of encoded patches x cannot be exactly defined. At the same time, anomalies have various sizes and shapes, and, ideally, they have to be processed with the variable receptive fields. To address the ambiguity between CNN receptive fields and anomaly variability, we adopt common multi-scale feature pyramid pooling approach. Figure 2 shows that the feature vectors zik ∈ RDk , i ∈ {Hk × Wk } are extracted by K pooling layers. Pyramid pooling captures both local and global patch information with small and large receptive fields in the first and last CNN layers, respectively. For convenience, we number pooling layers in the last to first layer order.

L(θ) = DKL [pZ (z)k p̂Z (z, c, θ)] ≈

1 X kui k22

− log |det Ji | + const, N i=1

### 4.2. CFLOW decoders for likelihood estimation

where the random variable ui = g −1 (zi , ci , θ), the Jacobian Ji = ∇z g −1 (zi , ci , θ) for CFLOW decoder and an expectation operation in DKL is replaced by an empirical train dataset Dtrain of size N . For brevity, we drop the kth scale notation. The derivation is given in Appendix B.

We use the general normalizing flow framework from Section 3.3 to estimate log-likelihoods of feature vectors z. Hence, our generative decoder model g(θ) aims to fit true density pZ (z) by an estimated parameterized density p̂Z (z, θ) from (1). However, the feature vectors are as4

Table 1. Complexity estimates for SPADE [7], PaDiM [8] and our CFLOW-AD. We compare train and test complexity as well as memory requirements. All models use the same encoder h(λ) setup, but diverge in the post-processing. SPADE allocates memory for a train gallery G used in k-nearest-neighbors. PaDiM keeps large matrices (Σki )−1 , i ∈ {Hk ×Wk } for Mahalanobis distance. Our model employs trained decoders gk (θk ) for post-processing.

### 5. Experiments

code is in PyTorch [28] with the FrEIA library [1] used for generative normalizing flow modeling. Industrial MVTec dataset comprises 15 classes with total of 3,629 images for training and 1,725 images for testing. The train dataset contains only anomaly-free images without any defects. The test dataset contains both images containing various types of defects and defect-free images. Five classes contain different types of textures (carpet, grid, leather, tile, wood), while the remaining 10 classes represent various types of objects. We resize MVTec images without cropping according to the specified image resolution (e.g. H × W = 256 × 256, 512 × 512 etc.) and apply ±5◦ augmentation rotations during training phase only. STC dataset contains 274,515 training and 42,883 testing frames extracted from surveillance camera videos and divided into 13 distinct university campus scenes. Because STC is significantly larger than MVTec, we experiment only with 256 × 256 resolution and apply the same preprocessing and augmentation pipeline as for MVTec. We compare CFLOW-AD with the models reviewed in Section 2 using MVTec and STC datasets. We use widely-used threshold-agnostic evaluation metrics for localization: area under the receiver operating characteristic curve (AUROC) and area under the per-region-overlap curve (AUPRO) [4]. AUROC is skewed towards large-area anomalies, while AUPRO metric ensures that both large and small anomalies are equally important in localization. Image-level AD detection is reported by the AUROC only. We run each CFLOW-AD experiment four times on the MVTec and report mean (µ) of the evaluation metric and, if specified, its standard deviation (±σ). For the larger STC dataset, we conduct only a single experiment. As in other methods, we train a separate CFLOW-AD model for each MVTec class and each STC scene. All our models use the same training hyperparameters: Adam optimizer with 2e-4 learning rate, 100 train epochs, 32 mini-batch size for encoder and cosine learning rate annealing with 2 warm-up epochs. Since our decoders are agnostic to feature map dimensions and have low memory requirements, we train and test CFLOW-AD decoders with 8,192 (32×256) mini-batch size for feature vector processing. During the train phase 8,192 feature vectors are randomly sampled from 32 random feature maps. Similarly, 8,192 feature vectors are sequentially sampled during the test phase. The feature pyramid pooling setup for ResNet-18 and WideResnet-50 encoder is identical to PaDiM [8]. The effects of other architectural hyperparameters are studied in the ablation study.

### 5.1. Experimental setup

### 5.2. Ablation study

We conduct unsupervised anomaly detection (imagelevel) and localization (pixel-level segmentation) experiments using the MVTec [4] dataset with factory defects and the STC [22] dataset with surveillance camera videos. The

Table 2 presents a comprehensive study of various design choices for CFLOW-AD on the MVTec dataset using AUROC metric. In particular, we experiment with the input image resolution (H × W ), encoder architecture (ResNet-

Model SPADE [7] PaDiM [8] Ours

M (zi ) log p̂Z (zi , ci , θ)

After training the decoders gk (θk ) for all K scales using (7), we estimate test dataset Dtest log-likelihoods as kui k22 + D log(2π) + log |det Ji | . Next, we convert log-likelihoods to probabilities pki = elog p̂Z (zi ,ci ,θ̂k ) for each kth scale using (8) and normalize them to be in [0 : 1] range. Then, we upsample pki to the input image resolution (H ×W ) using bilinear interpolation Pk = b(pk ) ∈ RH×W . Finally, we calculate anomaly score maps S H×W by aggregating all upsampled probabilities as S = maxPK Pk − k=1 Pk . log p̂Z (zi , ci , θ̂) = −

### 4.3. Complexity analysis

Table 1 analytically compares complexity of CFLOWAD and recent state-of-the-art models with the same pyramid pooling setup i.e. z k∈{1...K} = h(x, λ). SPADE [7] performs k-nearest-neighbor clustering between each test point zik and a gallery G of train data. Therefore, the method requires large memory allocation for gallery G and a clustering procedure that is typically slow compared to convolutional methods. PaDiM [8] estimates train-time statistics i.e. inverses of covariance matrices (Σki )−1 ∈ RDk ×Dk , i ∈ {Hk × Wk } to calculate M (zik ) at test-time. Hence, it has low computational complexity, but it stores in memory Hk × Wk matrices of Dk × Dk size for every kth pooling layer. Our method optimizes generative decoders gk (θk ) using (7) during the train phase. At the test phase, CFLOWAD simply infers data log-likelihoods log p̂Z (zi , ci , θ̂) using (8) in a fully-convolutional fashion. Decoder parameters θk∈{1...K} are relatively small as reported in Table 6.

Table 2. Ablation study of CFLOW-AD using localization AUROC metric on the MVTec [4] dataset, %. We experiment with input image resolution (H × W ), encoder architecture (ResNet-18 (R18), WideResnet-50 (WRN50) and MobileNetV3L (MNetV3)), type of normalizing flow (unconditional (UFLOW) and conditional (CFLOW)), number of coupling (# of CL) and pooling layers (# of PL).

Bottle Cable Capsule Carpet Grid Hazelnut Leather Metal Nut Pill Screw Tile Toothbrush Transistor Wood Zipper

Table 3. The detailed comparison of PaDiM [8], SPADE [7], CutPaste [19] and our CFLOW-AD on the MVTec [4] dataset for every class using AUROC or, if available, a tuple (AUROC, AUPRO) metric, %. CFLOW-AD model is with the best hyperparameters from Section 5.2 ablation study. For fair comparison, we group together results with the same encoder architectures such as ResNet-18 and WideResNet-50.

Bottle Cable Capsule Carpet Grid Hazelnut Leather Metal Nut Pill Screw Tile Toothbrush Transistor Wood Zipper

Table 4. Average AUROC and AUPRO on the MVTec [4] dataset, %. Both the best detection and localization metrics are presented, if available. CFLOW-AD is with WideResNet-50 encoder.

### 5.3. Quantitative comparison

Table 4 summarizes average MVTec results for the best published models. CFLOW-AD with WideResNet-50 encoder outperforms state-of-the-art by 0.36% AUROC in detection, by 1.12% AUROC and 2.5% AUPRO in localization, respectively. Table 3 contains per-class comparison for the subset of models grouped by the task and type of encoder architecture. CFLOW-AD is on par or significantly exceeds the best models in per-class comparison with the same encoder setups. Table 5 presents high-level comparison of the best recently published models on the STC dataset. CFLOW-AD outperforms state-of-the-art SPADE [7] by 0.73% AUROC in anomaly detection and PaDiM [8] by 3.28% AUROC in anomaly localization tasks, respectively. Note that our CFLOW-AD models in Tables 3-4 use variable input resolution as discussed in the ablation study: 512×512, 256×256 or 128×128 depending on the MVTec class. We used fixed 256×256 input resolution in Table 5 for the large STC dataset to decrease training time. Other reference hyperparameters in Tables 4-5 are set as: WideResnet-50 encoder with 3-scale pooling layers, conditional normalizing flow decoders with 8 coupling layers.

DifferNet [30] DFR [37] SVDD [42] SPADE [7] CutPaste [19] PaDiM [8]

Table 5. Average AUROC on the STC [22] dataset, %. Both the best available detection and localization metrics are showed. CFLOW-AD is with WideResNet-50 encoder.

CAVGA [40] SPADE [7] PaDiM [8]

### 5.4. Qualitative results

Figure 3 visually shows examples from the MVTec and the corresponding CFLOW-AD predictions. The top row shows ground truth masks from Dtest including examples with and without anomalies. Then, our model produces anomaly score maps (middle row) using the architecture from Figure 2. Finally, we show the predicted segmentation masks with the threshold selected to maximize F1-score. Figure 4 presents an additional evidence that our CFLOW-AD model actually addresses the OOD task sketched in Figure 1 toy example. We plot distribution of output anomaly scores for anomaly-free (green) and anomalous feature vectors (red). Then, CFLOW-AD is able to distinguish in-distribution and out-of-distribution feature vectors and separate them using a scalar threshold τ .

18 [13], WideResnet-50 [43], MobileNetV3L [14]), type of normalizing flow (unconditional (UFLOW) or conditional (CFLOW)), number of flow coupling layers (# of CL) and pooling layers (# of PL). Our study shows that the increase in number of decoder’s coupling layers from 4 to 8 gives on average 0.15% gain due to a more accurate distribution modeling. Even higher 1.4% AUROC improvement is achieved when processing 3-scale feature maps (layers 1, 2 and 3) compared 2-scale only (layers 2, 3). The additional feature map (layer 1) with larger scale (H1 × W1 = 32 × 32) provides more precise spatial semantic information. The conditional normalizing flow (CFLOW) is on average 0.5% better than the unconditional (UFLOW) due to effective encoding of spatial prior. Finally, larger WideResnet-50 outperforms smaller ResNet18 by 0.81%. MobileNetV3L, however, could be a good design choice for both fast inference and high AUROC. Importantly, we find that the optimal input resolution is not consistent among MVTec classes. The classes with macro objects e.g. cable or pill tend to benefit from the smaller-scale processing (256×256), which, effectively, translates to larger CNN receptive fields. Majority of classes perform better with 512×512 inputs i.e. smaller receptive fields. Finally, we discover that the transistor class has even higher AUROC with the resized to 128×128 images. Hence, we report results with the highest performing input resolution settings in the Section 5.3 comparisons.

### 5.5. Complexity evaluations

In addition to analytical estimates in Table 1, we present the actual complexity evaluations for the trained models using inference speed and model size metrics. Particularly, Table 1 compares CFLOW-AD with the models from Tables 4-5 that have been studied by Defard et al. [8]. The model size in Table 6 is measured as the size of all floating-point parameters in the corresponding model i.e. its encoder and decoder (post-processing) models. Because the encoder architectures are identical, only the post-processing models are different. Since CFLOW-AD decoders do not explicitly depend on the feature map dimensions (only on feature vector depths), our model is significantly smaller

Ground Truth Score Map Predicted Mask

Figure 3. Examples of the input images with ground truth anomaly masks (top row) for various classes of the MVTec. Our CFLOW-AD model from Table 4 estimates anomaly score maps (middle row) and generates segmentation masks (bottom row) for a threshold selected to maximize F1-score. The predicted segmentation mask should match the corresponding ground truth as close as possible.

than SPADE and PaDiM. If we exclude the encoder parameters for fair comparison, CFLOW-AD is 1.7× to 50× smaller than SPADE and 2× to 7× smaller than PaDiM. Inference speed in Table 6 is measured with INTEL I7 CPU for SPADE and PaDiM in Defard et al. [8] study with 256×256 inputs. We deduce that this suboptimal CPU choice was made due to large memory requirements for these models in Table 6. Thus, their GPU allocation for fast inference is infeasible. In contrast, our CFLOW-AD can be processed in real-time with 8× to 25× faster inference speed on 1080 8GB GPU with the same input resolution and feature extractor. In addition, MobileNetV3L encoder provides a good trade-off between accuracy, model size and inference speed for practical inspection systems.

Figure 4. Distribution of anomaly scores for the cable class from the MVTec learned by CFLOW-AD model from Table 4. Green density represent scores for the anomaly-free feature vectors, while region of red-color density shows scores for feature vectors with anomalies. The threshold τ is selected to optimize F1-score.

### 6. Conclusions

We proposed to use conditional normalizing flow framework to estimate the exact data likelihoods which is infeasible in other generative models. Moreover, we analytically showed the relationship of this framework to previous distance-based models with multivariate Gaussian prior. We introduced CFLOW-AD model that addresses the complexity limitations of existing unsupervised AD models by employing fully-convolutional translation-equivariant architecture. As a result, CFLOW-AD is faster and smaller by a factor of 10× than prior models with the same input resolution and feature extractor setup. CFLOW-AD achieves new state-of-the-art for popular MVTec with 98.26% AUROC in detection, 98.62% AUROC and 94.60% AUPRO in localization. Our new stateof-the-art for STC dataset is 72.63% and 94.48% AUROC in detection and localization, respectively. Our ablation study analyzed design choices for practical real-time processing including feature extractor choice, multi-scale pyramid pooling setup and the flow model hyperparameters.

Table 6. Complexity comparison in terms of inference speed (fps) and model size (MB). Inference speed for CFLOW-AD models from Table 3 is measured for (256×256) / (512×512) inputs.

Complexity metric and Model

R18 encoder only PaDiM-R18 [8] CFLOW-AD-R18

WRN50 encoder only SPADE-WRN50 [7] PaDiM-WRN50 [8] CFLOW-AD-WRN50

MNetV3 encoder only CFLOW-AD-MNetV3
