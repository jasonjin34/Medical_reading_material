# A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks

> **文献键** `Lee2018_180703888` · **来源** Advances in Neural Information Processing Systems 31 (NeurIPS 2018)(2018) · **类别** anomaly · **相关度** high · **获取** open
> **链接** <https://arxiv.org/abs/1807.03888> · `status: complete`

---

## 一句话
不重新训练任何预训练 softmax 分类器,在它的特征空间里为每一类拟合**共享协方差的类条件高斯**(即 GDA/LDA),用测试样本到最近类均值的 **Mahalanobis 距离**作为置信分数;再加上输入预处理与多层特征集成,同一个分数同时在 OOD 检测和对抗样本检测上达到当时最优,对噪声标签和小样本训练集更稳健,还能免训练地做类增量学习。

## 研究问题
softmax 分类器对异常样本(统计上远离训练分布的 OOD 样本,或对抗样本)也给出过度自信的后验。此前的方法要么只针对 OOD(MSP 基线、ODIN 用输出层置信度),要么只针对对抗样本(核密度 KD+PU、LID),没有一个**通用检测器**两者都做得好。此外 ODIN 的超参要用 OOD 验证集调,而实际中 OOD 样本事先不可得。

## 方法
**从 softmax 到生成式分类器**:在 GDA 下,共享协方差的类条件高斯所诱导的后验与 softmax 分类器等价,因此预训练特征 f(x) 可能近似服从类条件高斯。用训练集估计经验类均值 μ̂_c 与共享协方差 Σ̂(即最大似然拟合)。**分数**:M(x) = max_c −(f(x)−μ̂_c)ᵀ Σ̂⁻¹ (f(x)−μ̂_c),对应测试样本对数密度。作者先验证:用 Mahalanobis 距离分类的准确率与 softmax 相当(打破「生成式分类器一定差于判别式」的常识),且 Mahalanobis 分数在 ResNet/CIFAR-10 vs TinyImageNet 上优于 Euclidean 距离和 MSP。**校准技巧**:(1) **输入预处理**——沿增大 M(x) 的方向给输入加小扰动 x̂ = x − ε·sign(∇ₓ距离),与 ODIN 类似但优化的是 Mahalanobis 分数;(2) **特征集成**——在每个 dense/residual block 末端提特征(通道维平均池化 F×H×W → F×1),各自算 M_ℓ,再用**逻辑回归**学权重 α_ℓ 加权求和;低层特征对 LSUN、TinyImageNet、DeepFool 往往更有效。超参(ε、α_ℓ)可用每对 ID/OOD 各 1000 张的验证集调,也可**只用 ID 样本 + FGSM 生成的对抗样本**来调(不需要任何 OOD 数据)。**类增量学习**:新类到来时只需计算其均值并更新共享协方差 Σ̂ ← C/(C+1)·Σ̂ + 1/(C+1)·Σ̂_{C+1},无需重训。

## 方法谱系
**范式:特征嵌入 + 密度(feature-embedding density / one-class 的参数化形式)**,同时属于 post-hoc 的 OOD 检测。它建立在 MSP 基线(`msp-ood-iclr-2017`,文中 [13])与 ODIN(输入预处理思想)之上,并把对抗检测里用特征密度的 KD+PU、LID(只用 Euclidean)推进到 Mahalanobis。**后续影响**:PaDiM(`padim-icpr-2020`)明确写「受 [23]、[26] 启发,我们用 Mahalanobis 距离」给每个 patch 位置打分,[26] 即本文——把这一思路从图像级 OOD 搬到工业图像的**像素级异常定位**,并进一步建模跨层相关;energy score(`energy-ood-neurips-2020`)把它作为对比基线;OpenOOD/综述(`generalized-ood-survey-ijcv-2024`)把它列为 distance-based 代表(MDS),并指出它在 MNIST 上好、在 CIFAR 上差,而非参数的 KNN 更通用。

## 数据
分类器:DenseNet-100 与 ResNet-34,训练于 CIFAR-10、CIFAR-100、SVHN。OOD 测试:在其余数据集之间互换,外加 TinyImageNet(ImageNet 子集,10,000 张测试图,200 类)与 LSUN(10,000 张测试图,10 个场景),降采样到 32×32。对抗攻击:FGSM、BIM、DeepFool、CW。类增量学习:ResNet-34,CIFAR-100 → 下采样 ImageNet(以及附录中 CIFAR-100 → CIFAR-10)。

## 主要结果
- **消融**(ResNet / CIFAR-10 vs SVHN,TNR@TPR95):MSP 基线 32.47、ODIN 86.55;Mahalanobis 不加任何技巧 54.51(AUROC 93.92),加上输入预处理 + 特征集成 96.42(AUROC 99.14,AUPR-out 99.60)。
- **OOD 全表**(以 OOD 验证集调参):所有 ID/OOD 组合都优于 MSP 与 ODIN。例如 DenseNet / CIFAR-100 vs LSUN 的 TNR@TPR95:MSP 16.7 / ODIN 41.2 / Mahalanobis 91.4;ResNet / CIFAR-100 vs LSUN:18.8 / 45.6 / 90.9(摘要中「45.6% → 90.9%」);DenseNet / CIFAR-10 vs SVHN 的 AUROC 89.9 / 95.5 / 98.1。
- **不用 OOD 数据调参**(只用 ID + FGSM):Mahalanobis 仍一致优于两者,甚至超过用 OOD 调参的 ODIN;而 ODIN 在某些情况下(如 SVHN 上的 DenseNet)反而不如基线。但 ResNet / CIFAR-100 上掉得明显(如 vs SVHN 的 TNR 41.9)。
- **对抗检测**:相对 LID,ResNet / CIFAR-10 上 CW 的 TNR 从 82.9% 提到 95.8%;只用 FGSM 调参也能检出未见过的 BIM、DeepFool、CW。
- **稳健性**:训练数据很少或带随机标签(最多 40%)时,Mahalanobis 的 AUROC 保持较高,MSP 与 ODIN 明显下降。
- **类增量学习**:所有新类加入后,AUC 40.0%(第二场景 22.1%),优于微调 softmax 的 32.7%(15.6%)和 Euclidean 分类器的 32.9%(17.1%)。

## 创新点
(1) 用 GDA–softmax 等价性为「在特征空间做类条件高斯密度」提供理论动机,并实证生成式分类器不损准确率;(2) 一个分数统一处理 OOD 与对抗样本;(3) 多层特征集成(低层特征往往更敏感);(4) 演示可以不用 OOD 数据、只用合成扰动样本调参;(5) 免训练类增量学习——只更新均值与共享协方差。

## 局限
共享协方差的高斯假设是强假设,类内分布多峰或各类方差差异大时不成立;最好结果依赖用 OOD 验证样本训练逻辑回归权重——作者给出的 FGSM 替代方案在 CIFAR-100/ResNet 上掉点明显;输入预处理需要对输入求梯度,测试时多一次前后向;所有实验是 32×32 小图;后来 OpenOOD 发现它在 CIFAR 近 OOD 上不如更晚的方法(见综述)。需要有标签的分类器(类均值)。

## 与本研究方向的关系
**这是课题 1 最自然的 detect 基线之一**。映射:样本 = 细胞(或 spot、H&E patch);特征空间 = scVI/scANVI latent、单细胞基础模型嵌入,或 H&E 病理基础模型(UNI、Virchow)的 patch 嵌入;「类」= 健康参照(KPMP、Lake 图谱、HuBMAP 正常肾)里的细胞类型;对每个细胞类型拟合均值与(共享)协方差,用到最近类型的 Mahalanobis 距离作为异常分——在 snRNA latent 和 snATAC latent 上**各算一次**,两者都高 → 更可能是疾病,只有一个高 → 更可能是 artifact,这正好是课题 1 跨模态一致性的打分方式。类增量算法也直接有用:专家确认一个新的损伤状态(如 aPT)后,把它作为新「正常类」加入参照,只需算均值与更新协方差,适合迭代构建 KidneyAnomalyBench。**哪些假设会断**:(1) **批次效应**——新 donor 或新平台的整体平移会让所有细胞的距离都升高,距离被 batch 主导;必须在整合后的 latent 上算,而 `refmap-eval-biorxiv-2025`(mapQC)正是用参照自身的样本间差异做零分布来处理这一点;(2) **共享协方差**不适合肾脏——PT 与免疫细胞的方差结构差别很大,需要按类型的协方差(QDA)或收缩估计,而稀有类型(如 MD、podocyte)细胞数少,协方差病态;(3) **doublet** 落在两个类均值之间,距离中等,可能漏报也可能误报;**环境 RNA** 把所有细胞往 soup 方向推,形成系统偏移;**分割错误**(Xenium)把邻居转录本混进来,同样形成「混合」嵌入;(4) **连续疾病状态**让「最近类」概念模糊;(5) 输入预处理需要对输入求梯度,对计数数据或冻结的基础模型嵌入不太适用;(6) 特征集成的权重要用 OOD 验证集学——肾脏里没有现成的 OOD 集;用合成扰动(作者用 FGSM)替代时要小心:若用模拟 doublet 或注入环境 RNA 调参,会**教检测器去找 artifact**。**仓库中已有的同类做法**:`padim-icpr-2020` 明确受本文启发,在每个 patch 位置用 Mahalanobis 距离做像素级异常定位(H&E patch 的直接模板);`kidney-multimodal-genomebiol-2026` 用 Mahalanobis 距离衡量整合后细胞群之间的分离度(用作整合指标,不是异常检测);`histo-anomaly-bi-repo` 在健康组织深度特征上拟合 one-class SVM、`histo-nejmai-2024` 在 CTransPath 特征上用改良 kNN——都是同一「健康特征空间中的距离/密度」家族;`healthy-ref-natgenet-2023` 和 `refmap-eval-biorxiv-2025` 在 scVI latent 中相对健康参照做邻域级比较。**对课题 2**:一个可调用、确定性的 Mahalanobis 打分工具适合测 agent 的重跑稳定性,并检查 agent 是否说明了它依赖的高斯/共享协方差假设。

## 可复用资产
- **代码:** 官方 PyTorch 实现(含特征集成与输入预处理)。
<https://github.com/pokaxpoka/deep_Mahalanobis_detector>
- **算法:** Algorithm 1(多层 Mahalanobis 分数)与 Algorithm 2(类增量更新均值/共享协方差),几行 numpy 即可在 scVI latent 上复现。
- **评估指标:** TNR@TPR95、AUROC、检测准确率、AUPR-in/out。

## 待读
- 「A simple fix to Mahalanobis distance for improving near-OOD detection」(Ren 等,2021,relative Mahalanobis)——针对近 OOD,与肾脏「轻度损伤 vs 正常」的场景更接近。
- 非参数 KNN OOD(Sun 等,2022;综述中表现更稳)——作为 Mahalanobis 在 scVI latent 上的对照。
- 在 KPMP 参照上比较共享协方差 vs 按类型协方差 vs 收缩估计,并分别报告批次、doublet、真实损伤三类「异常」上的 AUROC。

## 引用
```bibtex
@inproceedings{Lee2018_180703888,
  title = {A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks},
  author = {Lee, Kimin and Lee, Kibok and Lee, Honglak and Shin, Jinwoo},
  booktitle = {Advances in Neural Information Processing Systems 31 (NeurIPS 2018)},
  year = {2018},
  eprint = {1807.03888},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/1807.03888}
}
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
