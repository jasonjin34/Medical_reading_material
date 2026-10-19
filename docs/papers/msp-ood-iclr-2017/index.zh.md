# A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks

> **文献键** `Hendrycks2016_161002136` · **来源** International Conference on Learning Representations (ICLR 2017)(2017) · **类别** anomaly · **相关度** medium · **获取** open
> **链接** <https://arxiv.org/abs/1610.02136> · `status: complete`

---

## 一句话
OOD 检测领域的起点论文:训练好的分类器给出的**最大 softmax 概率(MSP)**本身不能当作置信度(MNIST 分类器对高斯噪声也给出 91% 的「置信度」),但正确分类样本的 MSP 统计上高于错分样本和分布外样本,所以把 MSP 当阈值分数,就能在视觉、NLP、语音任务上检出错误和 OOD;作者同时定义了一套标准任务与指标(AUROC + 两种 AUPR),并用一个「辅助解码器 + 异常模块」说明这个基线可以被超越。

## 研究问题
分类器在训练与测试分布不一致时往往**静默失败**:高置信度地给出错误答案。作者举的例子就是医学诊断——模型对困难样本也高置信度输出,而本应把它们交给人工。两个相关问题:(1) **错误/成功预测**:能否预测分类器在某个测试样本上会出错;(2) **分布内/分布外检测**:能否判断测试样本是否来自与训练数据不同的分布。softmax 用指数函数,logit 的小变化就会引起输出分布的大变化,所以很少对 OOD 输入给出均匀分布。

## 方法
**基线**:对每个测试样本取预测类别的 softmax 概率(即 MSP)作为分数。错误检测时把正确/错误样本分开看;OOD 检测时把分布内测试集当作正类、OOD 样本当作负类(或取负号后把异常当正类)。作者也试过 softmax 分布与均匀分布之间的 KL 散度,结果与 MSP 高度相关。**评估**:强调不能用准确率,而用阈值无关的 **AUROC**,以及 **AUPR**——并且分别报告把「成功/分布内」当正类(AUPR Succ / AUPR In)与把「错误/分布外」当正类(AUPR Err / AUPR Out)两种情况,同时列出随机检测器的基线值(Base),因为 AUPR 依赖正类比例。所有 AUROC 与随机基线的差异经 Wilcoxon 秩和检验都高度显著。语音任务(CTC)中计算 softmax 时**去掉 blank 符号的 logit**,否则大多数时间步都高置信度地预测 blank。**异常模块(abnormality module)**:在分类器上接一个重构输入的辅助解码器,与分类器在分布内数据上联合训练;然后冻结,另训练一个小网络(sigmoid 输出),用干净样本与**人工加噪样本**(白噪声、棕噪声、粉噪声;MNIST 用模糊、旋转、高斯噪声)区分「正常/异常」。

## 方法谱系
**范式:基于分类器的 OOD(classifier-based OOD)**。它直接建立在「softmax 置信度不可靠」这类经验观察之上(Nguyen 等),是此后几乎所有 OOD 论文的默认基线:ODIN(温度缩放 + 输入扰动)、Mahalanobis(`mahalanobis-ood-neurips-2018`,改在特征空间做密度)、energy score(`energy-ood-neurips-2020`,证明 log MSP 是被平移过的 free energy)、Outlier Exposure(Hendrycks 自己的后续工作)以及 OpenOOD 基准(`generalized-ood-survey-ijcv-2024`,把 MSP 作为领域起点)。论文第 4 节的异常模块——用人工噪声当负样本训练「正常 vs 异常」判别器——是后来**合成异常 / 自监督**一支(如 DRAEM)的早期雏形;辅助解码器则带有**重构**范式的味道。

## 数据
**视觉**:MNIST(三层 256 宽全连接网络,GELU)、CIFAR-10/100(40-4 Wide ResNet);OOD 用 SUN 场景、Omniglot、notMNIST、黑白 CIFAR-10、高斯与均匀噪声。**NLP**:IMDB 情感分类(OOD:Customer Review、Movie Review);20 Newsgroups / Reuters 8 / Reuters 52 文本分类(留出部分类别作 OOD:15/5、6/2、40/12);WSJ 与 Twitter 词性标注(OOD:推文、English Web Treebank weblog)。**语音**:TIMIT(双向 LSTM + CTC),OOD 为叠加 Aurora-2 噪声(机场、嘈杂人声、汽车等,噪声音量 30%,平均 SNR≈5)与中文语料 THCHS-30。

## 主要结果
- **错误检测**(AUROC/随机基线 50):MNIST 97、CIFAR-10 93、CIFAR-100 87;错分样本的平均 MSP 仍高达 86% / 80% / 66%——说明 MSP 单独看是误导性的置信度。IMDB 82;15 Newsgroups 89、Reuters 6 89、Reuters 40 91;WSJ 96、Twitter 89。
- **OOD 检测**(AUROC):CIFAR-10/SUN 95、CIFAR-10/高斯 97、CIFAR-100/SUN 91、CIFAR-100/高斯 88;MNIST/Omniglot 96、/notMNIST 85、/均匀噪声 99。IMDB/All 94;15/5 Newsgroups 75(最难)、Reuters40/12 95;WSJ/Twitter 80、WSJ/Weblog 61(weblog 与新闻文体接近,几乎检不出);TIMIT 加噪 98–100、TIMIT/中文 85。
- **异常模块**:TIMIT(全连接网络,加噪后帧错误率只从 29.69% 升到 30.43%,softmax 几乎失效)平均 AUROC 从 softmax 的 80 提升到 97;MNIST 平均 AUROC 从 93 提升到 100。注意异常模块训练时用的噪声类型与测试时的失真不同,仍能泛化。

## 创新点
(1) 把「错误检测」与「OOD 检测」形式化为两个标准任务,并提出简单而跨领域有效的 MSP 基线;(2) 确立评估规范:AUROC + 正负两种 AUPR + 随机基线 + 报告底层分类器准确率(作者指出:一个总是错的分类器在以错误为正类时能拿到最大 AUPR);(3) 建议在多种任务与架构上测试,而不只在视觉上;(4) 用异常模块证明基线可被超越,开启后续研究。

## 局限
MSP 必须有一个训练好的分类器,且只看输出层——远离决策边界的 OOD 样本也可能拿到高 MSP(后续 Mahalanobis/energy 论文正是从这里切入)。近 OOD(文体接近的 weblog、相近新闻主题)效果差(AUROC 61–75)。早期 OOD 数据集可能含有与 ID 类别重叠的图像,导致评估不准(survey 明确指出了这一点)。异常模块依赖人工噪声类型的选择,只在 TIMIT 和 MNIST 上展示。所有实验都是 2016 年左右的小模型。

## 与本研究方向的关系
**映射到肾脏组学**:样本 = 单个细胞或 Visium/Xenium spot;「分类器」= 在健康参照(KPMP / Lake 图谱 / HuBMAP 正常肾)上训练的细胞类型注释器(scANVI、CellTypist 或 scVI latent 上的 MLP),H&E 侧则是 patch 级组织分类器;MSP 低 = 「这个细胞不像参照中任何一类」,即候选异常/新状态。这是 Plan A 里最便宜的 detect 基线,任何注释流程都免费给出。**哪些假设会断**:(1) **连续疾病状态**——肾损伤是 PT → aPT/injured PT → 失败修复的连续谱,中间态在两类之间,MSP 低是因为**类别歧义**而非新颖,MSP 把 aleatoric 歧义和真正的 OOD 混在一起;(2) **doublet** 天然是两类的混合,MSP 低——会被当成「异常」,其实是技术 artifact;(3) **环境 RNA / 质量差的细胞**同样拉低 MSP;(4) **批次效应**改变 logit 尺度,新 donor 的正常细胞也可能 MSP 偏低。因此 MSP 单独使用会把 artifact 报成疾病——这正是 Plan A 用**跨模态一致性**(snRNA 与 snATAC、Xenium 与 H&E 是否同时报警)来区分 artifact 与疾病的动机;MSP 可作为每个模态内部的基线分数。**可直接借用的部分**:本文的评估规范——AUROC + AUPR-Out(异常为正类,因为异常稀少)+ 随机基线 + 报告注释器准确率——应原样写进 KidneyAnomalyBench 的评测协议;「错误检测」半边也直接对应「标出注释器可能注错的细胞」。**仓库里已有的相关做法**:`conformal-scrna-bioinformatics-2025` 明确批评「对 softmax 分数设阈值」没有保证,改用 conformal p 值;`histo-nejmai-2024` 的最佳方案是 Outlier Exposure 二分类器给出的异常类概率(MSP 思路的训练版);`scatac-novel-genomeres-2026`(CARA)做「参照外」新类型检测。**对 Plan B**:MSP 是「用模型自身置信度当 verifier 信号」的原型,其核心教训——原始置信度不校准(噪声也 91%)——同样适用于 agent / LLM 的自报置信度,支持 Plan B 需要**单独校准的 verifier**,而不是相信 agent 的自信度。

## 可复用资产
- **代码:** 作者实验代码。
<https://github.com/hendrycks/error-detection>
- **评估协议:** AUROC + AUPR-In/Out(或 Succ/Err)+ 随机基线 + 底层分类器准确率;Wilcoxon 秩和检验。
- **基线实现:** MSP 在 OpenOOD 中有标准实现,可作为任何肾脏注释器的零成本基线。
<https://github.com/Jingkang50/OpenOOD>

## 待读
- ODIN(Liang 等,温度缩放 + 输入扰动)与 Outlier Exposure(Hendrycks 等,2019)——仓库里尚无条目;后者是 `histo-nejmai-2024` 的核心方法。
- 在 KPMP 健康参照上训练注释器,测 MSP 对 doublet、低质量细胞与 aPT 状态各自的 AUROC,量化「artifact 被当成异常」的程度。

## 引用
```bibtex
@inproceedings{Hendrycks2016_161002136,
  title = {A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks},
  author = {Hendrycks, Dan and Gimpel, Kevin},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year = {2017},
  eprint = {1610.02136},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/1610.02136}
}
```


---

📄 **[AI-ready 全文提取 →](ai-ready.md)**
