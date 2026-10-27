---
title: Learning the natural history of human disease with generative transformers
aliases:
- Delphi-2M
plans:
- EHR
track: []
year: 2025
relevance: high
category: ehr
recommended_by: core-reading
views:
- reading-list
- ehr
- overview
tags:
- paper
- plan/EHR
---

# Learning the natural history of human disease with generative transformers

> Delphi-2M turns GPT-2 into a continuous-time, competing-risk generative model of disease: given a person's ICD-10 diagnoses ordered by age at first diagnosis (1,256 diseases) plus sex, BMI, smoking and alcohol, it predicts which disease (or death) comes next and how long until it happens. Trained on 0.4M UK Biobank participants with only 2.2M parameters, it reaches an average age–sex-stratified AUC of ~0.76 across >1,000 diseases in internal validation, 0.67 on 1.93M Danish individuals with no parameter changes, and can sample synthetic future health trajectories up to 20 years ahead (Abstract; Fig. 2b; Fig. 5a).

> Delphi-2M 把 GPT-2 改成连续时间、竞争风险的疾病生成模型:输入一个人按首诊年龄排列的 ICD-10 诊断(1,256 种疾病)以及性别、BMI、吸烟、饮酒,输出下一事件是哪种病(或死亡)以及多久之后发生;在 40 万 UK Biobank 参与者上训练、仅 220 万参数,内部验证中 >1,000 种疾病的平均年龄-性别分层 AUC 约 0.76,不改参数用于 193 万丹麦人平均 AUC 0.67,并能采样最长 20 年的合成未来健康轨迹(Abstract;Fig. 2b;Fig. 5a)。

## Related papers / 相关论文
- [[_maps/papers/ehr-apollo-arxiv-2026|APOLLO virtual patient]] — patient-trajectory foundation model
- [[_maps/papers/ehr-comet-natmachintell-2025|COMET (EHR + omics)]] — UK Biobank EHR modelling
- [[_maps/papers/ehr-pancreatic-trajectory-natmed-2023|Pancreatic cancer trajectories]] — cites

## Deep-read / 精读

![[papers/ehr-delphi2m-nature-2025/deep-read]]
