# 2 · 细胞和 RNA / 2 · Cells and RNA

<!-- ZH -->
!!! abstract "读完能回答"
    - 细胞核、胞质、RNA 分别在哪里？
    - 为什么数 RNA 就能知道细胞在干什么？
    - 细胞类型和细胞状态有什么区别？它们在 obs 里是哪两列？
<!-- EN -->
!!! abstract "After this module you can answer"
    - Where are the nucleus, the cytoplasm and the RNA?
    - Why does counting RNA tell you what a cell is doing?
    - How do a cell type and a cell state differ, and which two obs columns hold them?

<!-- ZH -->
这一模块只讲后面用得到的最少生物知识。
<!-- EN -->
This module covers only the minimum biology the rest of onboarding needs.

## 第 1 步 · 一个细胞长什么样 / Step 1 · What a cell looks like

<!-- ZH/EN --> <div class="grid" markdown>

<!-- ZH/EN --> ![Animal cell: membrane, cytoplasm, nucleus, mitochondria / 动物细胞：细胞膜、胞质、细胞核、线粒体](img/animal_cell.png)

<!-- ZH -->
- **细胞膜**（cell membrane）：外面一层膜，把细胞和外界隔开。
- **细胞核**（nucleus）像机房，存着 **DNA**，也就是全部源代码。同一个人身上每个细胞的 DNA 几乎完全一样。
- **胞质**（cytoplasm）像车间，是真正干活的地方。
- **线粒体**（mitochondrion）在胞质里，是细胞的"电源"。它有自己的一小段 DNA，那些基因名以 `MT-` 开头，比如模块 1 里的 `MT-CO1`。
<!-- EN -->
- The **cell membrane** is the outer layer that separates the cell from its surroundings.
- The **nucleus** is the server room. It holds the **DNA**, the full source code. Almost every cell in one person carries the same DNA.
- The **cytoplasm** is the workshop where the actual work happens.
- **Mitochondria** sit in the cytoplasm and are the cell's power supply. They carry a small DNA of their own, whose genes are named with an `MT-` prefix, such as `MT-CO1` in module 1.

<!-- ZH/EN --> </div>

<!-- ZH -->
图：Wikimedia「Simple diagram of animal cell (en)」，domdomegg，CC BY 4.0。
<!-- EN -->
Figure: Wikimedia "Simple diagram of animal cell (en)" by domdomegg, CC BY 4.0.


## 第 2 步 · RNA 是什么、在哪里 / Step 2 · What RNA is and where it sits

<!-- ZH -->
细胞要用某个基因时，先在核里把这段 DNA **抄写成 RNA**（这一步叫转录，transcription），相当于打印一张"工单"。工单刚打印出来时还在核里，之后被送到胞质，车间照着它生产蛋白质。

所以一个细胞里的 RNA 分两部分：**核里有一小部分刚打印的，胞质里有一大部分已经送出去的。**模块 5.1 会用到这一点：只测细胞核，就只拿到前一部分。
<!-- EN -->
When a cell uses a gene, it first **copies that stretch of DNA into RNA** inside the nucleus (transcription), like printing a work order. A freshly printed order is still in the nucleus; it is then shipped to the cytoplasm, where the workshop uses it to build protein.

So a cell's RNA sits in two places: **a small, freshly made part in the nucleus and a larger, shipped part in the cytoplasm.** Module 5.1 uses this: measuring only the nucleus gets only the first part.

<!-- ZH/EN --> ![DNA in the nucleus is transcribed into mRNA, which leaves through nuclear pores to ribosomes in the cytoplasm / 核里的 DNA 被转录成 mRNA，经核孔送到胞质里的核糖体](img/transcription_export.png)

<!-- ZH -->
图的下半部分是细胞核：黑色的双螺旋是 **DNA**，橙色的线是刚抄出来的 **mRNA**（工单）。中间那层带蓝色小孔的是核膜，**核孔**（pore）就是工单出门的通道。上半部分是胞质：绿色的**核糖体**（ribosome）照着 mRNA 生产蛋白质（黑色的链）。其余标注（tRNA、chaperone、vesicle 等）这里用不到。

图：Wikimedia「ProteinTranscription+Synthesis」，Adjustit，CC BY-SA 4.0。
<!-- EN -->
The lower part of the figure is the nucleus: the black double helix is **DNA**, the orange strands are freshly copied **mRNA** (the work orders). The layer with blue gaps is the nuclear envelope, and the **pores** are where orders leave. The upper part is the cytoplasm: green **ribosomes** read the mRNA and build protein (black chains). The other labels (tRNA, chaperone, vesicle…) are not needed here.

Figure: Wikimedia "ProteinTranscription+Synthesis" by Adjustit, CC BY-SA 4.0.

## 第 3 步 · 为什么数 RNA 就知道细胞在干什么 / Step 3 · Why counting RNA tells you what a cell does

<!-- ZH -->
细胞经常用的基因，工单就多。所以数一个细胞里每种 RNA 各有几条，就知道它在干什么。这就是模块 1 里 X 的一行。

不同细胞会大量使用各自的"招牌"基因，叫**标记基因**（marker gene）。肾脏里几个常用的：
<!-- EN -->
Genes a cell uses a lot have many work orders. Counting each kind of RNA in a cell therefore tells you what the cell is doing; that count vector is one row of X from module 1.

Each kind of cell uses its own signature genes heavily; these are **marker genes**. A few common ones in the kidney:

| Marker gene / 标记基因 | Cell type / 细胞类型 | Why / 为什么 |
|---|---|---|
| `NPHS1`, `NPHS2` | Podocyte (POD) / 足细胞 | build the filter / 搭过滤屏障 |
| `LRP2` | Proximal tubule (PT) / 近端小管 | takes proteins back from the fluid / 从滤液里回收蛋白 |
| `UMOD` | Thick ascending limb (TAL) / 髓袢升支粗段 | made almost only here / 几乎只在这里产生 |
| `AQP2` | Collecting duct principal cell (PC) / 集合管主细胞 | water channel / 水通道 |

<!-- ZH -->
!!! tip "计算机类比"
    同一个程序（DNA）装在每台机器上，但每台机器运行的进程不同。数 RNA 就像对每台机器跑一次 `ps`，看各个进程有多少个实例。标记基因就是某类机器专有的那个进程名。
<!-- EN -->
!!! tip "Computer analogy"
    The same program (DNA) is installed on every machine, but each machine runs different processes. Counting RNA is like running `ps` on each machine and counting instances of each process. A marker gene is the process name that only one kind of machine runs.

## 第 4 步 · 细胞类型和细胞状态 / Step 4 · Cell type and cell state

<!-- ZH -->
- **细胞类型**（cell type）是**长期身份**：这个细胞是干哪份工作的，比如近端小管细胞。它几乎不会变。在 obs 里是 `subclass.l1`（17 个大类）和更细的 `subclass.l2`（75 个亚类）。
- **细胞状态**（cell state）是**当前状况**：同一类细胞，健康时、受伤时、修复时、分裂时，表达谱都不一样。在 obs 里是 `state.l1`（reference / altered）和 `state.l2`（具体哪种改变）。
<!-- EN -->
- A **cell type** is a **lasting identity**: which job the cell does, for example a proximal tubule cell. It hardly changes. In obs it is `subclass.l1` (17 broad classes) and the finer `subclass.l2` (75 subclasses).
- A **cell state** is the **current condition**: the same cell type looks different when healthy, injured, repairing or dividing. In obs it is `state.l1` (reference / altered) and `state.l2` (which kind of change).

<!-- ZH -->
Lake 2023 单核数据里 `state.l2` 的分布（我们从 GEO 标签表数的）：
<!-- EN -->
The distribution of `state.l2` in Lake 2023's single-nucleus data (counted by us from the GEO label table):

| state.l2 | Meaning / 意思 | Nuclei / 核数 |
|---|---|---|
| reference | healthy reference state / 正常的参考态 | 128,090 |
| degenerative | losing normal function / 正在坏掉、失去功能 | 42,316 |
| adaptive – epi | epithelial repair (aPT, aTAL) / 上皮在修复 | 25,150 |
| adaptive – str | stromal repair (fibroblast-like) / 间质在修复 | 3,513 |
| cycling | dividing to replace lost cells / 正在分裂补充细胞 | 839 |
| transitioning | between two cell types / 介于两种细胞类型之间 | 430 |
| NA | not assigned / 没有标 | 3,364 |

<!-- ZH -->
`subclass.l2` 的名字把两者拼在了一起：**dPT** = degenerative（退化的）PT，**aTAL** = adaptive（修复中的）TAL。75 个亚类里有 28 个是 altered。

!!! tip "计算机类比"
    细胞类型像服务器的**角色**（数据库、网关、缓存），细胞状态像它此刻的**运行状态**（正常、过载、重启中、扩容中）。异常检测要找的是"状态不对"，而不是"这台是数据库"。
<!-- EN -->
`subclass.l2` names combine the two: **dPT** = degenerative PT, **aTAL** = adaptive (repairing) TAL. 28 of the 75 subclasses are altered.

!!! tip "Computer analogy"
    A cell type is a server's **role** (database, gateway, cache); a cell state is its current **runtime status** (healthy, overloaded, restarting, scaling up). Anomaly detection looks for a wrong status, not for "this one is a database".

## 第 5 步 · 这些标签是怎么来的 / Step 5 · Where these labels come from

<!-- ZH -->
没有人在显微镜下逐个给 20 万个细胞贴标签。实际流程是：

1. 用表达谱把细胞**聚类**；
2. 看每个簇里哪些**标记基因**高，人工判断它是哪种细胞、处于什么状态；
3. 把这个判断赋给簇里的所有细胞。

所以 `subclass` 和 `state` 是**专家对聚类结果的解读**，不是直接测出来的。大部分时候它们很可靠，但边界上的细胞、以及"看起来受损但其实是测量问题"的细胞，可能被标错。我们的工作恰恰关心这些边界（模块 6 和 8）。
<!-- EN -->
Nobody labels 200,000 cells one by one under a microscope. In practice:

1. cells are **clustered** by their expression profiles;
2. experts look at which **marker genes** are high in each cluster and decide its cell type and state;
3. that decision is given to every cell in the cluster.

So `subclass` and `state` are **expert interpretations of clusters**, not measurements. They are usually reliable, but cells on boundaries, and cells that look injured because of measurement problems, can be mislabelled. Our work is about exactly those boundaries (modules 6 and 8).

## 自测 / Self-check

<!-- ZH -->
??? question "1. 只测细胞核，会丢掉哪部分 RNA？"
    丢掉已经送到胞质里的那一大部分，只剩核里刚转录出来的那一小部分。

??? question "2. 一个细胞的 `subclass.l1` 是 PT、`state.l2` 是 degenerative，它的 `subclass.l2` 最可能是什么？"
    dPT（degenerative PT，退化的近端小管细胞）。

??? question "3. 为什么说 `state` 标签不是真值？"
    它是专家看聚类和标记基因后判读出来的，不是实验直接测的；边界上的细胞和测量问题造成的"假受损"细胞可能被标错。
<!-- EN -->
??? question "1. If you measure only the nucleus, which RNA do you lose?"
    The large part already shipped to the cytoplasm; only the small, freshly made part in the nucleus remains.

??? question "2. A cell has `subclass.l1` = PT and `state.l2` = degenerative. What is its `subclass.l2` most likely?"
    dPT (degenerative proximal tubule).

??? question "3. Why is the `state` label not ground truth?"
    Experts assigned it by reading clusters and marker genes; it was not measured. Boundary cells and cells that look injured because of measurement problems can be mislabelled.
