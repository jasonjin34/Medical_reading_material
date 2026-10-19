# MVTec AD — A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection

> **文献键** `Bergmann_2019` · **来源** 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)(2019) · **类别** anomaly · **相关度** medium · **获取** open
> **链接** <https://doi.org/10.1109/cvpr.2019.00982> · `status: complete`

---

## 一句话
MVTec AD 是第一个面向真实工业检测、多物体、多缺陷、**带像素级真值**的无监督异常检测数据集:15 个类别(5 纹理 + 10 物体)、5,354 张高分辨率图像、73 种缺陷、1,888 个手工标注的异常区域;训练集只含无缺陷图像。论文同时给出 AnoGAN、L2/SSIM 自编码器、CNN 特征字典、GMM 纹理模型、variation model 的初始基准,结论是没有一种方法在所有类别上都好。它此后成为 PaDiM、PatchCore、DRÆM、CFLOW-AD 等几乎所有视觉 AD 方法的标准评测集。

## 研究问题
当时的异常 / 新奇检测评测大多是"把 MNIST、CIFAR-10、ImageNet 中任意几类当离群类",离群样本与训练分布差异巨大,无法说明方法在**与训练数据极接近、只在小局部有细微偏差**的真实异常上表现如何;而少数能做分割评测的数据集(NanoTWICE 只有 45 张单一纹理、DAGM 2007 是人工合成纹理且只有椭圆粗标)规模小、多样性低。作者认为缺少一个像 ImageNet 之于分类那样的 AD 数据集。

## 方法
**采集**:2048×2048 工业 RGB 传感器 + 两个双远心镜头(放大倍率 1:5 和 1:1),高度受控光照(部分类别有意改变光照以增加变异),裁剪到 700²–1024²;grid、screw、zipper 只提供灰度图。部分物体粗略对齐(toothbrush、capsule、pill),部分随机旋转摆放(metal nut、screw、hazelnut)。缺陷是**人工制造**的,目标是逼真地模拟生产中会出现的缺陷:表面缺陷(划痕、凹痕)、结构缺陷(部件变形)、缺失部件等。**基准协议**:各方法输出单通道异常图;作者提出**只用无缺陷验证图像确定阈值**的方法 —— 对每类设定一个最小缺陷面积,在验证集上逐步提高阈值,直到最大连通"异常"区域面积刚好低于该面积,用此阈值评估。**指标**:图像分类分别报告无缺陷和缺陷图的正确率;分割报告该阈值下的 per-region overlap(PRO)以及与阈值无关的像素级 ROC AUC。**基线**:AnoGAN(潜空间搜索 300 次迭代)、L2 与 SSIM 卷积自编码器(纹理 128×128 patch、物体 256×256)、CNN 特征字典(ResNet-18 avgpool + PCA + k-means,Napoletano 等)、基于 GMM 的纹理检测模型(HALCON 实现)、variation model(逐像素均值/方差,需要形状匹配对齐)。深度方法通过增强扩到每类 10,000 个训练 patch。

## 方法谱系
这是**数据集/基准**而非方法;所评测的基线覆盖了 2019 年的两大范式 —— **reconstruction/generative**(AnoGAN、L2/SSIM-AE)与 **feature-embedding**(预训练 CNN 特征 + 聚类),外加经典的 **density / one-class**(GMM 纹理模型、逐像素高斯 variation model)。**承接**:Schlegl 等 AnoGAN(论文明确以其为 GAN 基线)、Bergmann 等 SSIM-AE、Napoletano 等 CNN 特征字典。**影响**:此后每一篇主流视觉 AD 论文都以它为主评测集 —— PaDiM、PatchCore、DRÆM、CFLOW-AD 的主结果全部在 MVTec AD 上;PaDiM 还据此构造了非对齐版本 Rd-MVTec AD;到 PatchCore 时图像级 AUROC 已达 99%+,基本饱和。PRO 指标也被沿用为标准定位指标。

## 数据
**规模**:3,629 张训练/验证(全部无缺陷)+ 1,725 张测试(467 无缺陷 + 1,258 有缺陷);15 类各有 60–391 张训练图,toothbrush 最少(60)、hazelnut 最多(391);每类 1–8 个缺陷组,共 73 种;共 1,888 个缺陷区域。**纹理**:carpet、grid(规则),leather、tile、wood(随机)。**物体**:bottle、cable、capsule、hazelnut、metal nut、pill、screw、toothbrush、transistor、zipper。**许可**:CC BY-NC-SA 4.0(禁止商用,来自 MVTec 官网)。

## 主要结果
- **没有赢家**:没有任何方法在所有物体与纹理类上都表现好。纹理类无明显胜者,只看 ROC AUC 时 CNN 特征字典最稳定;物体类上 L2 / SSIM 自编码器最好,哪一个更好取决于具体物体。
- **高 AUC ≠ 好分割**:像素 ROC AUC 高时,用无缺陷验证集估出的阈值下的 PRO 仍可能很低(例如 bottle 上四种深度方法 PRO 只有 0.05–0.22,而 ROC AUC 为 0.78–0.93)—— 说明**仅用正常样本定阈值**本身就是难题。
- **失败模式**:AnoGAN 出现 mode collapse,对形状/朝向多变的物体几乎无法重建,carpet 完全失败;自编码器在高频纹理(tile、zipper)上重建模糊、假阳性多;CNN 特征字典不含空间位置信息,物体类上退化;GMM 纹理模型只处理灰度,漏掉颜色缺陷;variation model 需要精确对齐,capsule 上随机位置的印字总被判为缺陷。

## 创新点
- 第一个多类别、多缺陷、像素级真值、面向真实应用的无监督 AD 数据集。
- **只用无缺陷验证图像确定阈值**的评测协议,以及 PRO 指标的使用 —— 后者成为定位的标准指标。
- 跨范式的初始基准,揭示了每类方法的具体失败模式。

## 局限
- 缺陷是人工制造的,采集条件高度受控(远心镜头、可控光照),与真实产线的变异性有差距;每类训练图较少(60–391)。
- 只有外观 / 结构类局部缺陷,没有"逻辑异常"(组件数量、排列错误)—— 这在后续 MVTec LOCO 中才被补上(本文未涉及)。
- 后来的方法把图像级 AUROC 推到 99%+,基准已近饱和,区分力下降;而 pathology-ad-bench-mlhealth-2025 显示 MVTec 上的好表现不能迁移到病理(工业平均 ROC-AUC 0.888 vs 真实病理 0.645)。
- 非商用许可,限制了工业用途。

## 与本研究方向的关系
MVTec AD 对 Plan A 的意义是**KidneyAnomalyBench 的设计模板与反面教材**。**可以直接借鉴的**:(1) "训练集只有正常、测试集正常 + 异常、异常带区域级真值"的结构 —— 对应"健康参考训练、95 例活检测试、专家标注的病变区域(肾小球硬化、间质纤维化、小管萎缩、炎症浸润)作为区域级真值";(2) **只用正常验证集定阈值**的协议 —— 肾脏数据里同样没有可用于调参的已知异常,论文揭示的"AUC 高但阈值下分割差"在组学中会更严重,因此 KidneyAnomalyBench 应同时报告阈值无关指标(AUROC/AP)与固定协议阈值下的区域重叠;(3) **按类别分别报告**:MVTec 的"没有方法在所有类别上都好"对应到肾脏就是按解剖单元 / 细胞类型 / 病变类型分别报告,而不是给一个全局 AUC。**哪些假设会破**:(1) MVTec 的"正常"是严格受控的单一产品,而健康肾本身就异质(皮质/髓质、小管节段、年龄相关改变),且"健康供体"并不完全健康;(2) MVTec 的异常是**离散、局部**的缺陷,肾病是**连续、弥散**的状态谱,二值像素 mask 不足以表达,需要分级标签(例如 IFTA 程度)或连续损伤评分(damage-scores-cellgenomics-2026 的 PDS/HDS 可作为连续伪真值);(3) MVTec 几乎没有"技术伪影 vs 真异常"的混淆,而组学中 ambient RNA、doublet、分割错误、批次效应都是会被检测为"异常"的伪影 —— KidneyAnomalyBench 应专门设一类**伪影型异常**并要求方法把它们与疾病区分开,这正是 Plan A 跨模态一致性的评测出口;(4) 像素级 mask 在 snRNA/snATAC 中不存在,只在 Xenium/H&E 空间数据上可近似。**仓库里已有的同类思想**:pathology-ad-bench-mlhealth-2025 把 MVTec 的 Hazelnut 与 Tile 作为工业参照,与 Camelyon16、Crohn 结肠、小鼠肾小球对比,并直接量化了工业→病理的性能断崖;medianomaly-media-2025 是医学影像版的统一 AD 基准(7 个数据集、30 种方法);nih-kidney-ai-challenge-2026 是肾脏方向可能的外部基准出口。

## 可复用资产
- **数据:** MVTec AD 下载与评测代码(CC BY-NC-SA 4.0)。
<https://www.mvtec.com/research-teaching/datasets/mvtec-ad>
- **评测协议:** 基于无缺陷验证集与最小缺陷面积的阈值估计;PRO(per-region overlap)指标 —— 可改写为按细胞 / 按区域的 KidneyAnomalyBench 指标。
- **库:** anomalib 内置 MVTec AD 数据加载与 PRO 计算。
<https://github.com/open-edge-platform/anomalib>

## 待读
- MVTec AD 的 IJCV 2021 期刊扩展版(更完整的基线与指标讨论)以及 MVTec LOCO(逻辑异常)。
- anogan-ipmi-2017(本文 GAN 基线)与 Bergmann 等 SSIM-AE(VISAPP 2019)。
- 为 KidneyAnomalyBench 写一份"MVTec 式"数据卡:正常参考来源、测试集构成、区域真值类型、伪影类、阈值协议。

## 引用
```bibtex
@inproceedings{Bergmann_2019, title={MVTec AD — A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection}, url={http://dx.doi.org/10.1109/CVPR.2019.00982}, DOI={10.1109/cvpr.2019.00982}, booktitle={2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)}, publisher={IEEE}, author={Bergmann, Paul and Fauser, Michael and Sattlegger, David and Steger, Carsten}, year={2019}, month=June, pages={9584–9592} }
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
