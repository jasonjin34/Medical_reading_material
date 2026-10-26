# 5.1 · Assays: from tissue to the count matrix

> ⏱ About 45 min · Day 1 · Understand

!!! abstract "After this module you can answer"
    - What do single-cell and single-nucleus sequencing capture, and at what cost?
    - How do barcodes and UMIs turn reads into a count matrix?

Module 1 showed the end point, the count matrix X. This page shows how X is made, in three stages:

1. the tissue is broken into single **cells** or **nuclei**;
2. each cell (or nucleus) is packed into a tiny droplet with a bead carrying a **barcode**, and its RNA is tagged with that barcode and a **UMI**;
3. after sequencing, barcodes and UMIs are used to **count** how many molecules of each gene each cell had.

Each stage leaves marks in X. Items marked [n] come from the literature; "our count" means counted from Lake 2023's public label tables on GEO.

## Step 1 · Whole cells or nuclei

<div class="grid" markdown>

![Lake 2023 Fig. 1a: tissue processed into cells or nuclei before droplet sequencing (Cv3) / 组织先处理成细胞或细胞核，再进液滴测序（Cv3）](img/lake2023_fig1a_crop.jpg)

Lake 2023 did both: **scCv3** profiles whole cells and **snCv3** profiles nuclei [1]. The first step differs:

- **Single-cell**: the tissue is **digested** with enzymes into single living cells, for example at 37 °C [2].
- **Single-nucleus**: the tissue (which can be **frozen**) is broken up and the nuclei are pulled out directly; no living cells are needed [2, 3].

</div>

Figure: Lake et al. 2023, Fig. 1a (cropped), Nature, CC BY 4.0.

**Cost 1: digestion changes the cells.** In mouse kidney, digestion at 37 °C strongly induces stress genes, including *Fos*, *Jun*, *Atf3*, *Egr1* and heat-shock proteins; digesting on ice avoids this [2]. In human kidney, whole-cell methods likewise showed a stress signature (*FOS*, *FOSB*, *DNAJB1*) that single-nucleus methods did not [3]. This is why module 1's figure gives FOS its own column: a high value might be disease, or might just be digestion (module 6).

**Cost 2: nuclei lack the cytoplasmic RNA.** Recall module 2: RNA is made in the nucleus and then shipped to the cytoplasm. Lake 2023 names the **cytosolic transcripts** as one advantage of whole-cell data [1]. Mitochondria sit in the cytoplasm, and their RNA is essentially absent from nuclei [3].

**Cost 3: the two routes recover different cell-type mixes.** In mouse kidney, single-cell data lacked glomerular cells such as podocytes, which single-nucleus data recovered [4]; conversely, single-nucleus data under-represented T, B and NK lymphocytes [2].

These differences show up directly in Lake 2023's two label tables (our count, medians):

| | snCv3 (nuclei | scCv3 (cells |
|---|---|---|
| Nuclei or cells | 203,702 | 109,741 |
| People | 36 | 45 |
| `percent.mt` (median | 0.81% | 22.99% |
| `nFeature_RNA` (median | 1,638 | 1,276 |
| `nCount_RNA` (median | 2,694 | ≈ 3,076 |

`percent.mt` differs by a factor of almost thirty, which is what you expect if mitochondrial RNA sits in the cytoplasm. Gene and molecule counts are close, consistent with the mouse-kidney finding that single-cell and single-nucleus methods detect similar numbers of genes [4]. The two datasets come from different people and tissue (scCv3 is all biopsies), so this is a description, not a controlled comparison.

!!! tip "Computer analogy"
    Single-cell is like pulling a running machine out of the rack to inspect it: the pulling itself fires alarms (stress genes). Single-nucleus is like reading only the disk: unaffected by the pulling, but you lose what was in memory (cytoplasmic RNA).

## Step 2 · Droplets and barcodes: which RNA came from which cell

The RNA of tens of thousands of cells is eventually sequenced together. To separate it again afterwards, each cell is labelled on its own first. Taking Drop-seq as the example, the steps are [5]:

1. prepare a cell suspension;
2. pack each cell with a barcoded bead into a nanolitre droplet;
3. lyse the cell inside the droplet;
4. let the bead's primers capture the cell's mRNA;
5. break all droplets and reverse-transcribe, amplify and sequence thousands of cells in one reaction;
6. use the barcodes to infer which cell each transcript came from.

10x Chromium, which Lake 2023 used (Cv3), works the same way; its droplets are called GEMs (Gel bead in EMulsion) [6].

Each primer on a bead has several parts [5]:

- **cell barcode**: **identical on all primers of one bead, different between beads**, so all RNA from one droplet carries the same barcode;
- **UMI**: **different on every primer**, used to recognise PCR duplicates (step 3);
- **oligo-dT**: a run of T that pairs with the run of A at the tail of an mRNA and captures it.

In the 10x 3′ v3 chemistry used by Lake 2023, the barcode is **16 bases** long, drawn from about **3.5 million** barcodes, and the UMI is **12 bases** [7]. Those are the 16 letters after `KB1_` in module 1's `KB1_AAACCCAAGCCGATAG`.

!!! tip "Computer analogy"
    The barcode is a **foreign key**: every RNA record carries the ID of its cell, and a final `GROUP BY` on that key splits the pooled records back into cells. Different runs can reuse the same barcodes, which is why a run prefix (`KB1_`) is added, like namespacing primary keys before merging two tables.

## Step 3 · UMIs: count molecules, not reads

Before sequencing, PCR amplifies the DNA many times over; otherwise there is too little to read. But amplification is uneven: different original molecules end up with different numbers of copies. Counting **reads** directly would measure how often things were copied, not how many molecules there were. With the tiny starting amounts in single-cell data this error is severe [8].

A UMI gives each **original molecule** a random tag. All copies share that tag, so de-duplicating on (barcode, UMI, gene) leaves the real number of molecules [5, 8, 9].

<figure class="umi" markdown="0"><div class="um-row">
<div class="um-panel"><p class="um-h">① Sequencing reads</p><table><tr><th>barcode</th><th>UMI</th><th>gene</th></tr>
<tr><td class="um-k" style="--c:var(--u1)">AAACCC…</td><td>TTGCATGGACTA</td><td class="um-gene">LRP2</td></tr>
<tr class="um-dup"><td class="um-k" style="--c:var(--u1)">AAACCC…</td><td>TTGCATGGACTA</td><td class="um-gene">LRP2</td></tr>
<tr class="um-dup"><td class="um-k" style="--c:var(--u1)">AAACCC…</td><td>TTGCATGGACTA</td><td class="um-gene">LRP2</td></tr>
<tr><td class="um-k" style="--c:var(--u2)">AAACCC…</td><td>GACTTACCGTAG</td><td class="um-gene">LRP2</td></tr>
<tr><td class="um-k" style="--c:var(--u3)">AAACGA…</td><td>CCATGAGTTACG</td><td class="um-gene">UMOD</td></tr>
<tr class="um-dup"><td class="um-k" style="--c:var(--u3)">AAACGA…</td><td>CCATGAGTTACG</td><td class="um-gene">UMOD</td></tr>
<tr><td class="um-k" style="--c:var(--u4)">AAACGA…</td><td>AGGTCCATTGCA</td><td class="um-gene">UMOD</td></tr>
<tr><td class="um-k" style="--c:var(--u5)">AAACCC…</td><td>CTTAGGCAAGTC</td><td class="um-gene">FOS</td></tr>
</table></div><div class="um-arrow" aria-hidden="true">→</div>
<div class="um-panel"><p class="um-h">② De-duplicate on (barcode, UMI, gene)</p><table><tr><th>barcode</th><th>UMI</th><th>gene</th></tr>
<tr><td class="um-k" style="--c:var(--u1)">AAACCC…</td><td>TTGCATGGACTA</td><td class="um-gene">LRP2</td></tr>
<tr><td class="um-k" style="--c:var(--u2)">AAACCC…</td><td>GACTTACCGTAG</td><td class="um-gene">LRP2</td></tr>
<tr><td class="um-k" style="--c:var(--u3)">AAACGA…</td><td>CCATGAGTTACG</td><td class="um-gene">UMOD</td></tr>
<tr><td class="um-k" style="--c:var(--u4)">AAACGA…</td><td>AGGTCCATTGCA</td><td class="um-gene">UMOD</td></tr>
<tr><td class="um-k" style="--c:var(--u5)">AAACCC…</td><td>CTTAGGCAAGTC</td><td class="um-gene">FOS</td></tr>
</table></div><div class="um-arrow" aria-hidden="true">→</div>
<div class="um-panel"><p class="um-h">③ Count: two rows of X</p><table><tr><th></th><th>LRP2</th><th>UMOD</th><th>FOS</th></tr>
<tr><td>AAACCC…</td><td class="um-n">2</td><td class="um-n um-z">·</td><td class="um-n">1</td></tr>
<tr><td>AAACGA…</td><td class="um-n um-z">·</td><td class="um-n">2</td><td class="um-n um-z">·</td></tr>
</table></div></div>
<figcaption>Illustrative data. Each read carries three things: a barcode (which cell), a UMI (which original molecule) and a gene (where the read aligns). One original molecule is copied several times by PCR, so ① has identical rows (same colour, repeats greyed). After de-duplicating on all three, each row is one real molecule; counting per barcode × gene gives X. Counting reads instead would give the first cell 4 LRP2, not 2.</figcaption></figure>

Every number in X, and `nCount_RNA` in obs, counts **UMIs** (module 1).

!!! tip "Computer analogy"
    A UMI is like an **idempotency key** in a message queue: the same message is delivered several times, and the consumer de-duplicates on the message ID so it counts once.

## Step 4 · Droplets go wrong (preview)

The steps above are the ideal case. In practice:

- **Not every cell is captured.** The original 10x paper reports about 50% cell capture efficiency [6].
- **Empty droplets.** Many droplets hold no cell but still contain free-floating RNA from the solution, called **ambient RNA**; it can be secreted by cells or released when cells burst (for example under the stress of dissociation) [10]. Droplets with a cell contain some of it too.
- **Two cells in one droplet**, a **doublet** (more than two: multiplet). The more cells are loaded, the more often this happens, as expected from Poisson loading [6].

All three can make a row of X look abnormal; module 6 covers them.

## Self-check

??? question "1. Why count UMIs instead of reads?"
    PCR amplification is uneven, so one original molecule may be copied many times. Reads measure copying; counting after de-duplicating on (barcode, UMI, gene) gives the number of original molecules.

??? question "2. Why is `percent.mt` low in single-nucleus data and high in single-cell data?"
    Mitochondria sit in the cytoplasm and their RNA is essentially absent from nuclei. Nuclei-only data has little of it (Lake 2023 median 0.81%); whole cells include the cytoplasm, so it is much higher (median 22.99%).

??? question "3. FOS is high in a single-cell dataset. Does that show the cells were injured?"
    No. Digestion at 37 °C itself induces FOS and other stress genes. Check whether the data is single-cell and how it was digested, and compare with single-nucleus or cold-digested data (module 6).

## References

1. Lake BB, Menon R, Winfree S, et al. An atlas of healthy and injured cell states and niches in the human kidney. *Nature* 2023;619:585–594. [doi:10.1038/s41586-023-05769-3](https://doi.org/10.1038/s41586-023-05769-3) — Results ("the addition of cytosolic transcripts from scCv3"); Fig. 1a. Deep-read: [Lake 2023](../papers/lake-kidney-atlas-nature-2023/index.md).
2. Denisenko E, Guo BB, Jones M, et al. Systematic assessment of tissue dissociation and storage biases in single-cell and single-nucleus RNA-seq workflows. *Genome Biol* 2020;21:130. [doi:10.1186/s13059-020-02048-6](https://doi.org/10.1186/s13059-020-02048-6) — mouse kidney; abstract and Results (stress genes after 37 °C digestion; lymphocytes in snRNA-seq). Deep-read: [Denisenko 2020](../papers/denisenko-dissociation-bias-genomebiol-2020/index.md).
3. Lake BB, Chen S, Hoshi M, et al. A single-nucleus RNA-sequencing pipeline to decipher the molecular anatomy and pathophysiology of human kidneys. *Nat Commun* 2019;10:2832. [doi:10.1038/s41467-019-10861-2](https://doi.org/10.1038/s41467-019-10861-2) — human kidney; Results (stress signature in whole-cell methods; frozen tissue; mitochondrial transcripts "not expressed in nuclei"). Deep-read: [Lake 2019](../papers/lake-snrna-pipeline-natcommun-2019/index.md).
4. Wu H, Kirita Y, Donnelly EL, Humphreys BD. Advantages of single-nucleus over single-cell RNA sequencing of adult kidney: rare cell types and novel cell states revealed in fibrosis. *J Am Soc Nephrol* 2019;30:23–32. [doi:10.1681/ASN.2018090912](https://doi.org/10.1681/ASN.2018090912) — mouse kidney; abstract.
5. Macosko EZ, Basu A, Satija R, et al. Highly parallel genome-wide expression profiling of individual cells using nanoliter droplets. *Cell* 2015;161:1202–1214. [doi:10.1016/j.cell.2015.05.002](https://doi.org/10.1016/j.cell.2015.05.002) — Results (six steps of Drop-seq; four parts of each primer; UMIs avoid double-counting).
6. Zheng GXY, Terry JM, Belgrader P, et al. Massively parallel digital transcriptional profiling of single cells. *Nat Commun* 2017;8:14049. [doi:10.1038/ncomms14049](https://doi.org/10.1038/ncomms14049) — Results (GEMs; ~50% cell capture efficiency; multiplet rate consistent with Poisson loading).
7. 10x Genomics. Technical Note CG000201 Rev A: Chromium Single Cell 3′ v3 reagent, workflow & software updates. [PDF](https://cdn.10xgenomics.com/image/upload/v1660261285/support-documents/CG000201_TechNote_Chromium_Single_Cell_3___v3_Reagent__Workflow___Software_Updates_RevA.pdf) — 16 nt barcode, 3.5 million barcodes, 12 nt UMI.
8. Islam S, Zeisel A, Joost S, et al. Quantitative single-cell RNA-seq with unique molecular identifiers. *Nat Methods* 2014;11:163–166. [doi:10.1038/nmeth.2772](https://doi.org/10.1038/nmeth.2772) — abstract.
9. Kivioja T, Vähärautio A, Karlsson K, et al. Counting absolute numbers of molecules using unique molecular identifiers. *Nat Methods* 2012;9:72–74. [doi:10.1038/nmeth.1778](https://doi.org/10.1038/nmeth.1778) — abstract.
10. Lun ATL, Riesenfeld S, Andrews T, et al. EmptyDrops: distinguishing cells from empty droplets in droplet-based single-cell RNA sequencing data. *Genome Biol* 2019;20:63. [doi:10.1186/s13059-019-1662-y](https://doi.org/10.1186/s13059-019-1662-y) — Background (ambient RNA in empty droplets and its origin).

"Our count" numbers: the `*_Metadata_03282022.txt.gz` files of GEO GSE183277 (snCv3) and GSE183276 (scCv3), medians of `nCount_RNA`, `nFeature_RNA` and `percent.mt`. scCv3's `nCount_RNA` is not an integer (median 3,075.95), so the authors processed it; we give a rounded value.

## Terms in this module

| English | 中文 | In one sentence |
|---|---|---|
| [Single-cell RNA sequencing (scRNA-seq)](glossary.md#single-cell-rna-seq) | 单细胞 RNA 测序(scRNA-seq) | A technique that profiles the transcriptome of individual cells, revealing cell-type heterogeneity that bulk sequencing averages away. |
| [Single-nucleus RNA-seq (snRNA-seq)](glossary.md#snrna-seq) | 单核 RNA 测序(snRNA-seq) | Dissociates tissue down to individual nuclei and sequences the RNA in each, giving genome-wide expression per nucleus at the cost of losing every cell's position in the tissue. |
| [Tissue dissociation](glossary.md#tissue-dissociation) | 组织解离 | Breaking tissue into single cells, usually with enzymes at 37 °C, before single-cell RNA-seq; needed for whole cells but stresses them. |
| [10x Chromium (Cv3)](glossary.md#chromium-10x) | 10x Chromium（Cv3 = 第 3 版试剂） | The most common commercial single-cell platform: it packs each cell or nucleus into an oil droplet with a barcoded bead. Cv3 = Chromium v3 chemistry (snCv3 / scCv3 in Lake 2023). |
| [Cell barcode](glossary.md#cell-barcode) | 细胞条形码 | A short DNA tag attached to every RNA from the same droplet (or the same split-pool path), so reads can be sorted back to their cell; becomes the row ID of the count matrix. |
| [UMI (unique molecular identifier)](glossary.md#umi) | UMI（分子唯一标识） | A random tag on each RNA molecule before amplification, so copies made by PCR can be collapsed; the numbers in the count matrix are UMI counts (nCount_RNA = total UMIs per cell). |
