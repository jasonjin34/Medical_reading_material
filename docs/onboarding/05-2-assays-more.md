# 5.2 · Assays: ATAC, multiome, spatial, pooling

> ⏱ About 45 min · Day 1 · Understand

!!! abstract "After this module you can answer"
    - What does ATAC measure, and what matrix does it give?
    - Why does measuring two things in the same nucleus (multiome / SNARE2) matter?
    - What extra information does spatial sequencing give?
    - When several people are pooled in one run, how are cells assigned back to each person?

The RNA assays of 5.1 answer "which genes is the cell using **right now**". This page covers other assays: they measure something other than RNA, or record something extra alongside it. Each still ends up as a matrix. Items marked [n] come from the literature.

## Step 1 · DNA is open or closed

Module 2 said the nucleus stores DNA. Think of DNA as a very long thread with "instructions" written all over it: the genes. The cell winds this thread, stretch by stretch, around small spools; one spool with its DNA is called a **nucleosome**. DNA together with its spools is called chromatin.

- Where the winding is tight, the thread is wrapped up and nothing can touch it. That part is not in use for now: it is **closed**.
- Where the winding is loose and the thread is exposed, the cell can read it at any time: it is **open**. The start of a gene in use (its promoter) is usually exposed, with no spool on it [1].

**Open means the cell is using, or getting ready to use, that part of the instructions.** Open places are not only gene starts but also the regulatory regions near genes that control them. Whether a stretch of DNA is open is called chromatin accessibility, and that is what ATAC measures.

The top row of the figure below shows both states: the tightly packed blue balls on the left are closed, the sparse region labelled Gene on the right is open.

![ATAC-seq: Tn5 cuts and tags open chromatin; sequenced fragments pile up into peaks over open regions / ATAC-seq：Tn5 在开放区剪开并贴上接头，测序片段在开放区堆成 peak](img/atac_seq.png)

Figure: Wikimedia "Figure.1 ATAC-Seq illustration" by Deema108, CC BY-SA 4.0.

!!! tip "Computer analogy"
    Think of DNA as a huge code repository. Most files are compressed into archives (closed), so programs cannot read them; a few are unpacked in the working directory (open) and ready to run. This is only an aid to intuition; the real picture is more complicated.

## Step 2 · Tn5 only cuts exposed DNA

ATAC stands for Assay for Transposase-Accessible Chromatin: "use a transposase to see which chromatin can be reached". Its tool is an engineered enzyme called **Tn5**, the green blocks in the second row of the figure.

Think of Tn5 as a pair of scissors that **can only cut exposed thread**:

- As it cuts the DNA, it sticks a label on the cut end: a sequencing **adapter**, the small red and blue tails in the figure. Cutting and labelling in one move is called tagmentation [1].
- Thread wound inside a spool is shielded by the nucleosome, so Tn5 cannot reach it; only exposed thread gets cut [1].

So nearly all the cut pieces (fragments) come from open regions. **Where there are many fragments, the DNA is open.**

Single-cell ATAC also needs to know which nucleus each fragment came from: as in 5.1, each nucleus's fragments carry that nucleus's own barcode and are sorted back by barcode after sequencing.

## Step 3 · From fragments to peaks to a matrix

**Where a fragment came from: aligning to the genome.** After sequencing, each fragment is a short string of letters (A, C, G, T). The human reference genome is like a book of about 3 billion letters. Aligning means searching the book for the place that string was copied from, like a full-text search. Once found, you know the fragment's position in the genome.

**How a position is written: an address.** `chr2:169,200,000-169,200,500` means chromosome 2 (think "volume 2"), the stretch from letter 169,200,000 to letter 169,200,500.

**From fragments to a matrix, with 3 nuclei as an example:**

1. Pool the fragments of all 3 nuclei and align them to the genome. They are not spread evenly; they crowd into a few stretches (the open regions) and pile up into hills called **peaks** (bottom row of the figure). Say they crowd into stretches A, B and C.
2. These three stretches are the 3 columns of the matrix. Each column's name is an address like the one above.
3. Then count, for each nucleus, how many of its fragments fall in A, B and C. Each nucleus is one row.

| nucleus | segment A | segment B | segment C |
|---|---|---|---|
| nucleus 1 | 1 | 0 | 1 |
| nucleus 2 | 0 | 1 | 0 |
| nucleus 3 | 1 | 0 | 0 |

(Illustrative numbers.) So the **columns of an ATAC matrix are not genes but addresses of stretches of the genome**.

**Why almost only 0 and 1?** RNA is a "photocopy": a gene can have dozens of copies in one cell. DNA is the "original": each stretch exists in only **two copies** per cell, one from each parent (the genome is diploid). Either copy may well not get cut, so one nucleus yields very few fragments at any one position [2].

The consequence: a 0 in one nucleus cannot tell "closed" from "open but not cut". Single-cell ATAC is therefore **extremely sparse**; but a few hundred nuclei of the same type added together closely resemble a profile from tens of millions of cells [2].

!!! warning "The most common beginner mistake"
    A 0 for a peak in one nucleus does **not** mean that region is closed; most likely it simply was not cut. Judge openness from many nuclei of the same type added together.

**In one sentence:** RNA shows "which pages of the instructions the cell is reading now"; ATAC shows "which pages lie open, ready to be read". Only with both can you infer what controls what; step 4 shows Lake 2023 using them this way.

## Step 4 · Two measurements from one nucleus: SNARE2

If RNA and ATAC come from **two different batches of nuclei**, it is like two guest lists from two different parties: they are not even the same people, so you cannot match the rows one to one, only guess by similarity who resembles whom.

**SNARE-seq2** (SNARE2 in Lake 2023) measures both **in the same nucleus**: Tn5 first cuts the ATAC fragments, then the RNA is captured [3]. The hard part is making both kinds of molecules remember "which nucleus I came from". The trick is a few rounds of "split into groups, add one piece of label, pool again" (split-pool):

1. split the nuclei into many groups and add a different piece of barcode to each group;
2. pour all nuclei back together, mix, split again and add a second piece;
3. one more round adds a third piece.

After three rounds, the RNA and ATAC fragments of one nucleus carry **the same barcode combination** [3], and two different nuclei almost never end up with the same combination. The two tables therefore have the same rows and line up one to one. In the Lake Fig. 1a crop shown in module 4, BC1, BC2 and BC3 under SNARE2 are the three pieces added in those three rounds.

The figure below draws the two tables side by side, in the same style as module 1's X / obs figure:

<figure class="xobs" markdown="0"><div class="xo-scroll"><table aria-label="RNA and ATAC matrices of the same nuclei, aligned by row">
<thead><tr class="xo-cap"><th></th><th colspan="3"><span class="xo-tag">RNA</span>RNA counts <span class="xo-sub">· nuclei × genes</span></th><th></th><th colspan="3"><span class="xo-tag">ATAC</span>ATAC counts <span class="xo-sub">· nuclei × peaks</span></th><th></th><th></th></tr>
<tr class="xo-genes"><th></th><th>LRP2<i style="background:var(--xo-pt)"></i></th><th>UMOD<i style="background:var(--xo-tal)"></i></th><th>NPHS2<i style="background:var(--xo-pod)"></i></th><th></th><th>chr2:169.2M<i style="background:var(--xo-pt)"></i></th><th>chr16:20.3M<i style="background:var(--xo-tal)"></i></th><th>chr1:179.6M<i style="background:var(--xo-pod)"></i></th><th></th><th class="xo-o">cell type</th></tr></thead><tbody>
<tr tabindex="0"><td class="xo-bc">AAACAGCC…</td><td class="xo-x"><b style="--c:var(--xo-pt);--a:65%">11</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-seam"><div></div></td><td class="xo-x"><b style="--c:var(--xo-pt);--a:65%">1</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-seam"><div></div></td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-pt)">PT</span></td></tr>
<tr tabindex="0"><td class="xo-bc">AAACATGC…</td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-tal);--a:80%">19</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-seam"><div></div></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-tal);--a:85%">2</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-seam"><div></div></td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-tal)">TAL</span></td></tr>
<tr tabindex="0"><td class="xo-bc">AAACCAAC…</td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-pod);--a:50%">5</b></td><td class="xo-seam"><div></div></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x"><b style="--c:var(--xo-pod);--a:65%">1</b></td><td class="xo-seam"><div></div></td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-pod)">POD</span></td></tr>
<tr tabindex="0"><td class="xo-bc">AAACCGAA…</td><td class="xo-x"><b style="--c:var(--xo-pt);--a:56%">7</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-seam"><div></div></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-x xo-z"><b>·</b></td><td class="xo-seam"><div></div></td><td class="xo-o"><span class="xo-chip" style="--c:var(--xo-pt)">PT</span></td></tr>
</tbody></table></div>
<p class="xo-hint">Click the figure to enlarge; click again or press Esc to close</p>
<figcaption>Illustrative data. Both tables come from the same nuclei, so their rows are the same barcodes. ATAC columns are not genes but stretches of the genome (shown as chromosome and approximate position; chr2:169.2M means about 169.2 million bases into chromosome 2; the three stretches lie in the LRP2, UMOD and NPHS2 genes, positions from Ensembl GRCh38), and the numbers are mostly 0, 1 or 2. The PT nucleus in row 4 has LRP2 RNA but no ATAC fragment in that stretch: ATAC data is very sparse, and missing in one nucleus does not mean closed.</figcaption></figure>

**In the data**: Lake 2023's SNARE2 has 104,809 nuclei, but from only 7 healthy people (see the [Lake 2023 dataset page](../datasets/lake-2023.md)). So if you want RNA and ATAC together, you only have healthy tissue. Lake 2023 used SNARE2's ATAC part to find regulatory regions and to infer gene regulatory networks for TAL [4]. Cell-type labels for the single-cell and SNARE2 data were obtained by aligning them to the single-nucleus data [4].

## Step 5 · Spatial: keeping the position

Every method so far starts by breaking the tissue apart, which loses **where each cell was**. Spatial transcriptomics instead lays a tissue section directly on a slide covered with primers carrying **positional barcodes**, so each RNA records where it was captured [5].

- **Visium**: the slide has an array of round spots; Lake 2023 gives the spot ("bead" in the paper) diameter as 55 µm [4]. A spot usually covers several cells, so its expression is a mixture, and single-cell data is used to work out which cell types are in each spot [6].
- **Xenium**: images the section directly, down to subcellular resolution, but measures only a **pre-selected panel of genes**; Janesick 2023 used 313 [6].

Spatial data adds a **coordinate table**: one row per spot (or cell) with its x and y on the section. Lake 2023 includes Visium data; our current work does not use it.

## Step 6 · Pooling people: assigning cells back with SNPs

To save cost or reduce batch differences, cells from **several people are sometimes pooled** into one run [8]. How do you then know whose each cell is?

Through small natural differences in each person's DNA, called **SNPs** (single-nucleotide polymorphisms): at a given position, some people have A and others G. Reads that cover these positions let you match a droplet to a person like a fingerprint [7, 8]:

- **demuxlet** needs each person's genotype in advance. In simulations, 50 SNPs per cell assign 97% of single cells correctly, in pools of up to 64 people [7].
- **souporcell** needs no prior genotypes and clusters cells by the variants in their reads [8].

A bonus: a droplet that carries SNPs from **two people** must be a doublet [7, 8], and such doublets may be invisible from expression alone [8].

**In the data**: for pooled runs, the `patient` column in obs is computed this way rather than recorded at the bench. Whether a dataset was pooled is stated in its methods.

## Summary: all assays in 5.1 and 5.2

| Assay | One row | One column | Main bias | In Lake 2023 |
|---|---|---|---|---|
| scRNA-seq (scCv3) | cell | gene | dissociation stress, high `percent.mt`, cell-type loss | 109,741 cells |
| snRNA-seq (snCv3) | nucleus | gene | no cytoplasmic RNA, fewer lymphocytes | 203,702 nuclei |
| snATAC-seq | nucleus | peak (genome interval) | extremely sparse, near 0/1 | in SNARE2 |
| SNARE2 (RNA + ATAC) | nucleus | gene + peak | healthy donors only in Lake | 104,809 nuclei |
| Visium | spot | gene | a spot mixes several cells | yes, not used by us |
| Xenium | cell | pre-selected genes | panel only | — |
| SNP demultiplexing | — | — | assigns `patient`, finds cross-person doublets | — |

Numbers are from 5.1 and the [Lake 2023 dataset page](../datasets/lake-2023.md); sources for the biases are in 5.1 and the steps above.

## Self-check

??? question "1. What is one column of an ATAC matrix, and how does it differ from the RNA matrix?"
    A column is a peak, a stretch of the genome given by coordinates, not a gene. Each number is how many fragments fell in that stretch, nearly always 0 or 1 in a single nucleus.

??? question "2. A nucleus has 0 at some peak. Does that mean the region is closed?"
    No. Single-cell ATAC is extremely sparse, so 0 most likely means not captured. Look at many nuclei of the same type together.

??? question "3. What does SNARE2 gain over measuring RNA and ATAC separately?"
    Both come from the same nucleus with the same barcode, so the rows of the two tables match one to one; measured separately, you can only guess with algorithms which nuclei correspond.

??? question "4. In a pooled run, how do you know whose a cell is, and what else do you find?"
    Match the SNPs in its reads like a fingerprint (demuxlet, souporcell). A droplet with SNPs from two people is a doublet.

## References

1. Buenrostro JD, Giresi PG, Zaba LC, et al. Transposition of native chromatin for fast and sensitive epigenomic profiling of open chromatin, DNA-binding proteins and nucleosome position. *Nat Methods* 2013;10:1213–1218. [doi:10.1038/nmeth.2688](https://doi.org/10.1038/nmeth.2688) — Results (Tn5 tagmentation; steric hindrance in less accessible chromatin; nucleosome-free promoter at active TSSs).
2. Buenrostro JD, Wu B, Litzenburger UM, et al. Single-cell chromatin accessibility reveals principles of regulatory variation. *Nature* 2015;523:486–490. [doi:10.1038/nature14590](https://doi.org/10.1038/nature14590) — abstract; Results (two copies in a diploid genome, near-digital 0/1; sparse data).
3. Plongthongkum N, Diep D, Chen S, et al. Scalable dual-omics profiling with single-nucleus chromatin accessibility and mRNA expression sequencing 2 (SNARE-seq2). *Nat Protoc* 2021;16:4992–5029. [doi:10.1038/s41596-021-00507-3](https://doi.org/10.1038/s41596-021-00507-3) — abstract.
4. Lake BB, Menon R, Winfree S, et al. An atlas of healthy and injured cell states and niches in the human kidney. *Nature* 2023;619:585–594. [doi:10.1038/s41586-023-05769-3](https://doi.org/10.1038/s41586-023-05769-3) — Results (SNARE2 regulatory elements and TAL GRNs; anchoring scCv3 and SNARE2 to snCv3; 55 µm Visium beads). Deep-read: [Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md).
5. Ståhl PL, Salmén F, Vickovic S, et al. Visualization and analysis of gene expression in tissue sections by spatial transcriptomics. *Science* 2016;353:78–82. [doi:10.1126/science.aaf2403](https://doi.org/10.1126/science.aaf2403) — abstract.
6. Janesick A, Shelansky R, Gottscho AD, et al. High resolution mapping of the tumor microenvironment using integrated single-cell, spatial and in situ analysis. *Nat Commun* 2023;14:8353. [doi:10.1038/s41467-023-43458-x](https://doi.org/10.1038/s41467-023-43458-x) — Results (313-gene Xenium panel; subcellular resolution; deconvolving cell types in Visium spots).
7. Kang HM, Subramaniam M, Targ S, et al. Multiplexed droplet single-cell RNA-sequencing using natural genetic variation. *Nat Biotechnol* 2018;36:89–94. [doi:10.1038/nbt.4042](https://doi.org/10.1038/nbt.4042) — abstract.
8. Heaton H, Talman AM, Knights A, et al. Souporcell: robust clustering of single-cell RNA-seq data by genotype without reference genotypes. *Nat Methods* 2020;17:615–620. [doi:10.1038/s41592-020-0820-1](https://doi.org/10.1038/s41592-020-0820-1) — abstract (why donors are pooled; cross-genotype doublets).

## Terms in this module

| English | 中文 | In one sentence |
|---|---|---|
| [Single-nucleus ATAC-seq (snATAC-seq)](glossary.md#snatac-seq) | 单核 ATAC 测序(snATAC-seq) | Uses a transposase that cuts only unpacked DNA to map which genomic regions are open per nucleus, revealing which genes are permitted to be expressed rather than which currently are. |
| [Chromatin accessibility](glossary.md#chromatin-accessibility) | 染色质开放性 | How physically reachable a stretch of DNA is for transcription machinery; tightly packed regions are effectively switched off, loosened ones are available for expression. |
| [Tn5 transposase](glossary.md#tn5-transposase) | Tn5 转座酶 | The enzyme used in ATAC-seq: it can only cut into open (unwound) DNA and inserts sequencing adapters as it cuts, so where it cuts marks accessible chromatin. |
| [ATAC peak](glossary.md#atac-peak) | ATAC 峰 | A genomic interval where transposase cut sites pile up across many nuclei, defining a region of open chromatin and forming the row dimension of the peak-by-cell matrix. |
| [Multiome (joint RNA + ATAC)](glossary.md#multiome) | Multiome(RNA 与 ATAC 同核联测) | An assay that measures transcription and chromatin accessibility in the very same nucleus, pairing 'what is expressed' with 'what is permitted' without having to match cells across separate runs. |
| [SNARE-seq2](glossary.md#snare-seq2) | SNARE-seq2（SNARE2） | Single-Nucleus chromatin Accessibility and mRNA Expression sequencing, version 2: measures RNA and ATAC in the same nucleus using split-pool (combinatorial) barcoding instead of droplets; used for 7 healthy donors in Lake 2023. |
| [Spatial transcriptomics](glossary.md#spatial-transcriptomics) | 空间转录组学 | A family of technologies that measure gene expression while preserving each cell's or spot's position within an intact tissue section. |
| [Visium](glossary.md#visium) | Visium | A widely used 10x Genomics spatial-transcriptomics platform that captures gene expression on a grid of barcoded spots overlaid on a tissue slide. |
| [Xenium](glossary.md#xenium) | Xenium | A 10x Genomics imaging-based platform that measures a targeted panel of transcripts in situ at subcellular resolution with single-cell segmentation. |
| [SNP / genotype](glossary.md#snp-genotype) | SNP / 基因型 | Single-base differences between people (or mouse strains); the set a person carries is their genotype, a DNA fingerprint stored in VCF files and measured by WES or arrays. |
| [Genotype multiplexing / demultiplexing](glossary.md#genotype-demultiplexing) | 基因型混样 / 分人 | Pooling cells from several people in one run and sorting them back by SNPs (demuxlet, souporcell, vireo); it also reveals droplets with two people's SNPs (doublets) and foreign RNA (ambient contamination). |
