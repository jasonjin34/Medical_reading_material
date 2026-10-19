# Deep One-Class Classification

> **文献键** `Ruff_2018` · **来源** International Conference on Machine Learning (ICML 2018), PMLR 80(2018) · **类别** anomaly · **相关度** high · **获取** open
> **链接** <https://proceedings.mlr.press/v80/ruff18a.html> · `status: complete`

---

## 一句话
Deep SVDD 是第一个**直接以异常检测为目标**训练的深度方法(作者自述):训练一个神经网络 φ,让正常数据的表示尽量落进一个以固定中心 c 为圆心、体积最小的超球,测试时异常分数就是 ‖φ(x) − c‖²;论文同时证明了哪些网络设计会导致"超球坍缩"(偏置项、有界激活、可学习的中心),以及软边界版本的 ν-性质。

## 研究问题
经典方法(OC-SVM、KDE)在高维大数据上因扩展性差与维数灾难而失效,需要大量特征工程;核方法至少随样本数平方增长,预测还要存支持向量。而当时的深度异常检测(自编码器、AnoGAN 等)都是**为别的任务训练**(生成或压缩),再借重建误差这种启发式打分 —— 并不优化异常检测本身的目标;自编码器还面临"压缩到多少维"这个在无监督下难以选择的超参。作者要问:能否像 SVDD 一样定义一个**最小体积**的异常检测目标,但让特征由深度网络端到端学出?

## 方法
**目标函数**(权重 W 的网络 φ: X → F):**软边界 Deep SVDD**——min R² + (1/νn)·Σ max{0, ‖φ(xᵢ;W) − c‖² − R²} + (λ/2)·Σ‖W^ℓ‖²_F,ν ∈ (0,1] 权衡超球体积与越界样本;**One-Class Deep SVDD**(假设训练数据绝大多数正常)——min (1/n)·Σ‖φ(xᵢ;W) − c‖² + 权重衰减,即把所有表示到 c 的平均距离压小。异常分数 s(x) = ‖φ(x;W*) − c‖²(软边界版可再减去 R*²)。推理只需前向网络,**不存任何训练数据**。**优化**:SGD/Adam;软边界版交替优化 W 与 R(每 k=5 个 epoch 用线搜索解 R)。**防坍缩的理论**:命题 1——若 c 也作为自由变量,全零权重网络 + R=0 就是最优解,所以 c 必须固定且不等于全零权重网络的输出(实践中取初始前向输出的均值);命题 2——任何隐藏层有**偏置项**都能学出常数映射,故去掉所有偏置;命题 3——**有界激活**(如 sigmoid)可被饱和来模拟偏置,故用 ReLU/leaky ReLU 这类无界激活;命题 4——软边界版的 ν 是离群样本比例的上界、边界上或外样本比例的下界(ν-性质)。**实现细节**:LeNet 式 CNN,用训练好的卷积自编码器(DCAE)编码器初始化(预训练),BatchNorm,leaky ReLU(α=0.1),两阶段学习率 10⁻⁴ → 10⁻⁵(150+100 epoch),λ=10⁻⁶。

## 方法谱系
**范式:密度 / 单类(one-class)**。直接把 Tax & Duin 的核 SVDD(最小包围超球)和 Schölkopf 等的 OC-SVM / ν-性质搬到深度特征上;作者把此前方法分为"混合式"(先学表示再接浅层检测器,如 DBN + OC-SVM)和"全深度式"(直接用重建误差),Deep SVDD 是全深度、且目标就是异常检测。它引出了 Deep SAD(半监督、可用少量标注异常)、多超球扩展、以及 Patch SVDD(MEATRD 的图像基线之一)等;Ruff 等 2021 统一综述把它与核 SVDD 并列为同一"超球模型",并以此说明浅层与深度方法之间可以相互迁移改进。病理与空间组学中的"在冻结/学到的特征上做 one-class"(BI 的 center-loss + OC-SVM、MEATRD 的 Deep-SVDD 式打分)都是这条线的后代。

## 数据
**MNIST 与 CIFAR-10 单类设定**:每次取一个类为正常类、其余 9 类为异常;只用该类训练样本训练(MNIST 约 6,000、CIFAR-10 5,000),在标准测试集 10,000 张上算 AUC;预处理为 L1 全局对比度归一化 + min-max 缩放。**GTSRB 停车标志对抗样本检测**:训练 780 张正常停车标志;测试 270 张正常 + 20 张由 Boundary Attack 生成的对抗样本;裁掉 10% 边框、缩放到 32×32。对比方法:OC-SVM/SVDD(高斯核,γ 用 10% 测试样本小验证集网格搜索——作者注明这给了浅层 SVDD 一点监督优势)、KDE、Isolation Forest(三者先做保留 95% 方差的 PCA)、DCAE、AnoGAN。结果为 10 个随机种子的平均。

## 主要结果
**MNIST(表 1)**:One-Class Deep SVDD 在 10 个类中的 8 个上最好、类 4 与 OC-SVM 并列(94.9),只有类 0 低于 OC-SVM(98.0 vs 98.6);例如类 2:91.7±0.8(OC-SVM 82.5、IF 88.6、DCAE 85.4、AnoGAN 85.0);类 8:93.9±1.6(OC-SVM 88.9)。**CIFAR-10**:结果"喜忧参半"——Deep SVDD 在 AUTOMOBILE 65.9、CAT 59.1、DOG 65.7、HORSE 67.3 上最好;但 DEER(66.2 KDE vs 60.9)、FROG(74.9 KDE vs 67.7)、TRUCK(76.0 KDE vs 73.1)上**浅层 KDE / SVDD 反而更好**,AIRPLANE(67.1)与 BIRD(52.9)上 AnoGAN 最好,SHIP 上 DCAE 最好(76.8)。作者解释:这些类的正常样本有很强的**全局结构**(如卡车图像被路面/天空水平分割),局部 CNN 特征未必合适 —— 架构选择很关键。One-Class 版在两个数据集上都略好于软边界版(因训练集确实无异常)。**GTSRB(表 2)**:One-Class Deep SVDD **80.3±2.8** 最好,DCAE 79.1、软边界 77.8、IF 73.8、OC-SVM 67.5、KDE 60.5;**AnoGAN 的 DCGAN 因数据太少未收敛**,无结果。深度方法的标准差普遍更大(SGD 随机性)。

## 创新点
- 第一个全深度的单类分类目标:特征学习与最小体积超球联合优化。
- 系统刻画"超球坍缩"的成因(自由中心、偏置项、有界激活)及对应的设计规则 —— 这些规则至今仍是一切"把正常压紧"类方法的必查项。
- 证明软边界版的 ν-性质,可以把"训练集中可能有多少污染"作为先验写进模型。
- 模型完全由网络权重刻画,无需保存训练数据,内存与推理开销低。

## 局限
- 只在 MNIST / CIFAR-10 / GTSRB 这类"把分类数据集改造成单类任务"的设定上评估,异常是"别的类",与真实场景的细微异常差别很大(Ruff 等 2021 综述也批评了这种评估习惯)。
- CIFAR-10 上并不稳定优于浅层方法;对网络架构敏感,且 SGD 带来较大方差。
- 为防坍缩必须去偏置、固定中心、用 DCAE 预训练 —— 表示的好坏很大程度依赖预训练;超球只给出单一"正常模式",对多模态正常分布(多种细胞类型)天然不合适。
- 只给样本级分数,不提供定位或解释。

## 与本研究方向的关系
Deep SVDD 给 **detect** 阶段提供了最干净的"正常 = 紧致区域,异常 = 到中心的距离"打分形式,而且与 Plan A 最可能的主力路线——**在冻结的基础模型嵌入上做 one-class**——一一对应。**映射到肾脏组学**:样本 = snRNA 细胞、Xenium 细胞、Visium spot 或 H&E 图块;"正常训练集" = KPMP/HuBMAP 健康参考;φ = 在 scVI latent 或 H&E 基础模型嵌入之上加的一个小网络;异常分数 = 到"正常中心"的距离。**哪些假设会断**:(1) **单一超球 vs 多细胞类型**:肾脏正常组织本身就有 PT、TAL、足细胞、内皮、免疫等数十种状态,一个中心 c 会把"稀有但正常的细胞类型"判为异常;必须**按细胞类型分别建超球**,或用多中心/条件版本(这与 healthy-ref 的"先在健康图谱上学 latent、再与匹配对照比较"思路互补)。(2) **批次效应**:新批次整体平移就会远离 c —— 需要先参考映射并用 MapQC 式的样本间零分布校正。(3) **污染**:"健康"供肾里也可能有 doublet、ambient RNA 主导的细胞、Xenium 分割/溢出错误的细胞(见 xenium-split、ovrlpy);软边界版的 ν 正好可以写入"训练集中预计有多少比例是伪影"的先验,这比 One-Class 版更适合肾脏数据。(4) **连续疾病态**:‖φ(x) − c‖² 是连续量,但没有"异常从哪开始"的定义 —— 需要 conformal 校准(conformal-scrna)把分数变成有 FPR 保证的 p 值。(5) **无金标准**:与论文的"别的类 = 异常"不同,肾脏里没有现成的异常标签,KidneyAnomalyBench 的专家判定是评测前提。**跨模态一致性**:对同一组织,分别在 H&E 嵌入与表达嵌入上建两个超球;两个距离都大 → 疾病候选,只在一个模态大 → 伪影候选(例如分割错误只在表达侧,染色/折叠只在图像侧)。**仓库里已有的同类适配**:MEATRD(meatrd-aaai-2025)在潜在多模态重建误差上训练 Deep-SVDD 式单类分类器、以到中心 c 的距离打分;BI 的 histo-anomaly-bi-repo 在 center-loss 训练的 CNN 特征上拟合 one-class SVM(浅层 SVDD 的近亲);histo-nejmai-2024 比较了基础模型特征上的 kNN 与 one-class 微调,并把 Deep SVDD 列为迁移到空间组学的待读;MedIAnomaly 发现"冻结 ImageNet ResNet + one-class 分类器"几乎在所有数据集都进前三 —— 支持把"冻结基础模型嵌入 + 单类打分"当 Plan A 的默认强基线。

## 可复用资产
- **代码:** 作者的 Deep SVDD 实现(论文给出的地址)。
<https://github.com/lukasruff/DeepSVDD>
- **设计规则清单:** 固定中心(取初始前向均值)、去掉所有偏置、用无界激活、自编码器预训练 —— 任何"把正常嵌入压紧"的肾脏模型都应逐条检查。
- **评测协议:** 单类设定 + 10 个种子的均值±标准差;KDE / IF / OC-SVM(PCA 95% 方差)作为必须报告的浅层基线。

## 待读
- Deep SAD(Ruff 等 ICLR 2020):用少量已标注异常的半监督扩展 —— 对 KidneyAnomalyBench 中少量专家确认的病例尤其相关。
- Patch SVDD(Yi & Yoon, ACCV 2020):图块级 SVDD,MEATRD 的图像基线。
- Ruff 等 2021 统一综述(本仓库 ad-unifying-review-procieee-2021)。

## 引用
```bibtex
@inproceedings{Ruff_2018,
  title = {Deep One-Class Classification},
  author = {Ruff, Lukas and Vandermeulen, Robert A. and G{\"o}rnitz, Nico and Deecke, Lucas and Siddiqui, Shoaib A. and Binder, Alexander and M{\"u}ller, Emmanuel and Kloft, Marius},
  booktitle = {Proceedings of the 35th International Conference on Machine Learning (ICML)},
  series = {Proceedings of Machine Learning Research},
  volume = {80},
  pages = {4393--4402},
  publisher = {PMLR},
  year = {2018},
  url = {https://proceedings.mlr.press/v80/ruff18a.html}
}
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
