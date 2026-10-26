# 8 · 我们在解决什么问题

> ⏱ 约 20 分钟 · 第 1 天 · 读懂

!!! abstract "读完能回答"
    - 组里的研究课题各在问什么？
    - 为什么直接在 Lake 上跑异常检测会"假成功"？
    - 前面七个模块的知识，在各个课题里用在哪里？

## 正文

!!! note "正在编写"
    这一模块的正文还在写。

## 本模块名词

| 中文 | English | 一句话 |
|---|---|---|
| [异常检测](glossary.md#anomaly-detection) | Anomaly detection | 识别偏离所学“正常”概念的样本或区域,常仅用正常数据训练——即“检测→建模→逆转”流程的第一环。 |
| [改变态（参考态 vs 改变态）](glossary.md#altered-state) | Altered state (reference vs altered) | Lake 2023 给偏离健康的细胞状态起的名字（退化、修复、增殖、过渡），与'参考态'相对；是聚类后由专家判读的，健康人身上也有。 |
| [单类分类](glossary.md#one-class-classification) | One-class classification | 仅从单一正常类别的样本学习一个边界,凡落在边界之外者即判为异常。 |
| [域偏移](glossary.md#domain-shift) | Domain shift | 当测试数据与训练数据不同(例如换了扫描仪或染色方案)时导致的模型性能下降。 |
| [AUROC / AUC(ROC 曲线下面积)](glossary.md#auroc) | AUROC / AUC (area under the ROC curve) | 衡量分类器把正例排在负例之前能力的阈值无关指标;0.5 为随机,1.0 为完美区分。 |
