# 2 · 细胞和 RNA

> ⏱ 约 30 分钟 · 第 1 天 · 读懂

!!! abstract "读完能回答"
    - 细胞核、胞质、RNA 分别在哪里？
    - 为什么数 RNA 就能知道细胞在干什么？
    - 细胞类型和细胞状态有什么区别？它们在 obs 里是哪两列？

这一模块只讲后面用得到的最少生物知识。

## 第 1 步 · 一个细胞长什么样

<div class="grid" markdown>

![Animal cell: membrane, cytoplasm, nucleus, mitochondria / 动物细胞：细胞膜、胞质、细胞核、线粒体](img/animal_cell.png)

- **细胞膜**（cell membrane）：外面一层膜，把细胞和外界隔开。
- **细胞核**（nucleus）像机房，存着 **DNA**，也就是全部源代码。同一个人身上每个细胞的 DNA 几乎完全一样。
- **胞质**（cytoplasm）像车间，是真正干活的地方。
- **线粒体**（mitochondrion）在胞质里，是细胞的"电源"。它有自己的一小段 DNA，那些基因名以 `MT-` 开头，比如模块 1 里的 `MT-CO1`。

</div>

图：Wikimedia「Simple diagram of animal cell (en)」，domdomegg，CC BY 4.0。

## 第 2 步 · RNA 是什么、在哪里

细胞要用某个基因时，先在核里把这段 DNA **抄写成 RNA**（这一步叫转录，transcription），相当于打印一张"工单"。工单刚打印出来时还在核里，之后被送到胞质，车间照着它生产蛋白质。

所以一个细胞里的 RNA 分两部分：**核里有一小部分刚打印的，胞质里有一大部分已经送出去的。**模块 5 会用到这一点：只测细胞核，就只拿到前一部分。

![DNA in the nucleus is transcribed into mRNA, which leaves through nuclear pores to ribosomes in the cytoplasm / 核里的 DNA 被转录成 mRNA，经核孔送到胞质里的核糖体](img/transcription_export.png)

图的下半部分是细胞核：黑色的双螺旋是 **DNA**，橙色的线是刚抄出来的 **mRNA**（工单）。中间那层带蓝色小孔的是核膜，**核孔**（pore）就是工单出门的通道。上半部分是胞质：绿色的**核糖体**（ribosome）照着 mRNA 生产蛋白质（黑色的链）。其余标注（tRNA、chaperone、vesicle 等）这里用不到。

图：Wikimedia「ProteinTranscription+Synthesis」，Adjustit，CC BY-SA 4.0。

## 第 3 步 · 为什么数 RNA 就知道细胞在干什么

细胞经常用的基因，工单就多。所以数一个细胞里每种 RNA 各有几条，就知道它在干什么。这就是模块 1 里 X 的一行。

不同细胞会大量使用各自的"招牌"基因，叫**标记基因**（marker gene）。肾脏里几个常用的：

| 标记基因 | 细胞类型 | 为什么 |
|---|---|---|
| `NPHS1`, `NPHS2` | 足细胞 | 搭过滤屏障 |
| `LRP2` | 近端小管 | 从滤液里回收蛋白 |
| `UMOD` | 髓袢升支粗段 | 几乎只在这里产生 |
| `AQP2` | 集合管主细胞 | 水通道 |

!!! tip "计算机类比"
    同一个程序（DNA）装在每台机器上，但每台机器运行的进程不同。数 RNA 就像对每台机器跑一次 `ps`，看各个进程有多少个实例。标记基因就是某类机器专有的那个进程名。

## 第 4 步 · 细胞类型和细胞状态

- **细胞类型**（cell type）是**长期身份**：这个细胞是干哪份工作的，比如近端小管细胞。它几乎不会变。在 obs 里是 `subclass.l1`（17 个大类）和更细的 `subclass.l2`（75 个亚类）。
- **细胞状态**（cell state）是**当前状况**：同一类细胞，健康时、受伤时、修复时、分裂时，表达谱都不一样。在 obs 里是 `state.l1`（reference / altered）和 `state.l2`（具体哪种改变）。

Lake 2023 单核数据里 `state.l2` 的分布（我们从 GEO 标签表数的）：

| state.l2 | 意思 | 核数 |
|---|---|---|
| reference | 正常的参考态 | 128,090 |
| degenerative | 正在坏掉、失去功能 | 42,316 |
| adaptive – epi | 上皮在修复 | 25,150 |
| adaptive – str | 间质在修复 | 3,513 |
| cycling | 正在分裂补充细胞 | 839 |
| transitioning | 介于两种细胞类型之间 | 430 |
| NA | 没有标 | 3,364 |

`subclass.l2` 的名字把两者拼在了一起：**dPT** = degenerative（退化的）PT，**aTAL** = adaptive（修复中的）TAL。75 个亚类里有 28 个是 altered。

!!! tip "计算机类比"
    细胞类型像服务器的**角色**（数据库、网关、缓存），细胞状态像它此刻的**运行状态**（正常、过载、重启中、扩容中）。异常检测要找的是"状态不对"，而不是"这台是数据库"。

## 第 5 步 · 这些标签是怎么来的

没有人在显微镜下逐个给 20 万个细胞贴标签。实际流程是：

1. 用表达谱把细胞**聚类**；
2. 看每个簇里哪些**标记基因**高，人工判断它是哪种细胞、处于什么状态；
3. 把这个判断赋给簇里的所有细胞。

所以 `subclass` 和 `state` 是**专家对聚类结果的解读**，不是直接测出来的。大部分时候它们很可靠，但边界上的细胞、以及"看起来受损但其实是测量问题"的细胞，可能被标错。我们的工作恰恰关心这些边界（模块 6 和 8）。

## 自测

??? question "1. 只测细胞核，会丢掉哪部分 RNA？"
    丢掉已经送到胞质里的那一大部分，只剩核里刚转录出来的那一小部分。

??? question "2. 一个细胞的 `subclass.l1` 是 PT、`state.l2` 是 degenerative，它的 `subclass.l2` 最可能是什么？"
    dPT（degenerative PT，退化的近端小管细胞）。

??? question "3. 为什么说 `state` 标签不是真值？"
    它是专家看聚类和标记基因后判读出来的，不是实验直接测的；边界上的细胞和测量问题造成的"假受损"细胞可能被标错。

## 本模块名词

| 中文 | English | 一句话 |
|---|---|---|
| [细胞核](glossary.md#cell-nucleus) | Nucleus (cell nucleus) | 细胞里装 DNA 的部分；RNA 在这里被转录出来，之后再运到胞质。 |
| [转录（基因表达）](glossary.md#transcription) | Transcription (gene expression) | 把一个基因的 DNA 抄写成 RNA；数一个细胞里某个基因有几条 RNA，就是在量这个基因的活跃程度（表达量）。 |
| [基因表达签名](glossary.md#gene-expression-signature) | Gene-expression signature | 一组特定基因,其协同表达水平可标志某种细胞状态、疾病或治疗响应。 |
| [细胞类型](glossary.md#cell-type) | Cell type | 工作相同、表达谱特征一致的一类细胞（例如近端小管细胞）；通过聚类加看标记基因来确定。 |
| [细胞状态](glossary.md#cell-state) | Cell state | 细胞在其稳定的细胞类型身份之上所处的、可变的功能状态,如激活、耗竭或增殖。 |
