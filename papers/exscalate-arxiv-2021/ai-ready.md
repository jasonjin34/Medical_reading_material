<!--
AI-ready extract: clean, self-contained text meant to be pasted into an LLM context.
No images, no nav chrome. Full text for open sources; abstract + structured metadata for paywalled.
-->
# EXSCALATE: An extreme-scale in-silico virtual screening platform to evaluate 1 trillion compounds in 60 hours on 81 PFLOPS supercomputers

- **Authors:** Davide Gadioli; Emanuele Vitali; Federico Ficarelli; Chiara Latini; Candida Manelfi; Carmine Talarico; Cristina Silvano; Carlo Cavazzoni; Gianluca Palermo; Andrea Rosario Beccari
- **Venue / Year:** arXiv preprint · 2021
- **DOI:** 
- **URL:** https://arxiv.org/abs/2110.11644
- **Bibkey:** Gadioli2021_211011644
- **Status:** complete

## Abstract
The social and economic impact of the COVID-19 pandemic demands the reduction of the time required to find a therapeutic cure. In the contest of urgent computing, we re-designed the Exscalate molecular docking platform to benefit from heterogeneous computation nodes and to avoid scaling issues. We deployed the Exscalate platform on two top European supercomputers (CINECA-Marconi100 and ENI-HPC5), with a combined computational power of 81 PFLOPS, to evaluate the interaction between 70 billions of small molecules and 15 binding-sites of 12 viral proteins of Sars-Cov2. The experiment lasted 60 hours and overall it performed a trillion of evaluations.

## Full text / Extract
<!-- Full cleaned text for open-access; for paywalled leave the note below. -->
> Source: arXiv open full text (arXiv:2110.11644v1, cs.DC, 22 Oct 2021), main text + figure/table captions. Condensed extract: the two-column PDF text layer is interleaved, so this is a cleaned, section-faithful condensation rather than a verbatim dump; figures are described, not reproduced.

# AFFILIATIONS
Politecnico di Milano, Department of Electronics, Information and Bioengineering, Milano, Italy (Gadioli, Vitali, Silvano, Palermo); CINECA, SuperComputing Applications and Innovation Department, Casalecchio di Reno, Italy (Ficarelli, Latini); Dompé farmaceutici S.p.A. — EXSCALATE, Napoli, Italy (Manelfi, Talarico, Beccari); Leonardo SPA, Genova, Italy (Cavazzoni).

Keywords: extreme-scale virtual screening, molecular docking, COVID-19, SARS-COV-2.

# 1. INTRODUCTION
Drug discovery involves in-silico, in-vitro and in-vivo stages. Its outcome is a molecule (ligand) with the strongest interaction with at least one binding site (pocket) of the target protein representing the disease. Virtual screening is an early stage that selects promising ligands from a vast chemical library. Its complexity comes from ligand and pocket flexibility: both can change shape on interaction, so estimating interaction strength with a scoring function also requires predicting atom displacement via a docking algorithm — computationally heavy and well known in the literature. To raise the probability of finding promising candidates one wants a larger chemical library, which worsens complexity. Because the evaluation is in silico, new molecules can be designed by simulating known chemical reactions, so library size is limited only by the system's computational power.

In the context of urgent computing, where time-to-cure should be as short as possible, the Exscalate platform was re-designed to virtually screen as many ligands as possible within a given time budget. To maximise docking throughput the authors target HPC supercomputers, whose design maximises double-precision Flop/s (the TOP500 ranks machines by throughput). Four of the top five supercomputers have heterogeneous nodes relying heavily on accelerators, typically GPUs; one must therefore hinge on node accelerators and scale efficiently across nodes. Even at the software level there are multiple well-known issues: how to use accelerators efficiently, how to transfer data within a node to feed accelerators, how to move data from storage devices to the node and back, how to minimise inter-node communication and inter-process synchronisation, and how to improve resilience so faults do not inflate time-to-solution.

Within the EXSCALATE4CoV European project (https://www.exscalate4cov.eu/), which targets new potential drugs against the COVID-19 pandemic, the Exscalate platform was deployed on two HPC machines with a combined throughput of 81 PFLOPS to rank a chemical library of more than 70 billion ligands against 15 binding sites of 12 viral proteins of SARS-CoV-2. Crystal structures of the main functional units of the SARS-CoV-2 proteome were obtained from the Protein Data Bank; homology models were generated for proteins without a crystal structure. The experiment lasted 60 hours and performed a trillion docking operations, becoming the largest virtual screening campaign up to that moment. The knowledge generated is publicly released through the MEDIATE website (https://mediate.exscalate4cov.eu).

## Table 1 — The 3D targets used in the molecular docking experiments (a target might have different pockets)
| Protein | PDB code |
|---|---|
| 3CL protease (NSP5) | 6LU7 |
| N-protein | 6VYO |
| NSP3 | 6W02 |
| NSP6 | De novo model |
| NSP9 | 6W4B |
| NSP12 | 7BV2 |
| NSP13 | 6XEZ |
| NSP14 | Homology Model |
| NSP15 | 6W01 |
| NSP16 | 6W4H |
| PL protease | 6W9C |
| Spike-ACE2 | 6M0J |

# 2. RELATED WORKS
Molecular docking applications span a performance–accuracy spectrum. Since docking is used here to select the most promising candidates, fast approaches are of interest — ICM, PSOVina, EUDOCK — but few can use accelerators, which account for most of the computational power of the target supercomputers.

AutoDock is the most related work: it has been ported to CUDA (AutoDock-GPU) and deployed on the Summit supercomputer, where over one billion molecules were docked on two SARS-CoV-2 proteins in less than two days. That work hinges on Summit's NVMe local storage to dock batches of ligands and store intermediate results. AutoDock-GPU uses OpenMP for a thread-based pipeline in which each thread reads ligands from file, launches CUDA kernels, waits for completion and writes back results. Since most docking algorithms use a fast but approximate scoring function to drive 3D pose estimation, it is common to re-score the most promising poses with a more accurate function; they use a custom CUDA version of RFScore-VS for that and BlazingSQL for computing statistics and selecting top-scoring ligands. The workflow is orchestrated with FireWorks from an external cluster to ensure a consistent state in the presence of faults in the computation nodes.

The Exscalate design differs in several ways: a monolithic application docks and re-scores ligands, using MPI to scale out and C++11 threads to scale up. This reaches high throughput without relying on node-local storage, which is not available on the target HPC systems. The application is further enveloped in a more complex workflow that compensates for its weak points. Finally, because the docking algorithm is deterministic, only the molecule's structure (SMILES format) and the best score found need be stored; the 3D displacement of atoms can be regenerated on demand.

# 3. EXSCALATE PLATFORM

## 3.1 The dock and score algorithm
The algorithm's output is an estimate of bond strength between a given ligand and the target protein's binding site. In virtual screening it is common to reduce complexity with heuristics and empirical rules instead of molecular dynamics. One implication is that a ligand's numeric score is strongly correlated with the given 3D displacement of its atoms, which is non-trivial to compute because of the many degrees of freedom: beyond the six from rigid-body rotation and translation, ligand flexibility must be considered — a subset of bonds (torsional bonds) partitions the ligand's atoms into two disjoint sets that can rotate about the bond axis, changing shape. A small molecule can have tens of torsional bonds.

The algorithm has four steps:
1. Ligand pre-processing: flatten the ligand by rotating torsional bonds to maximise the sum of internal distances between all molecule atoms. Protein-independent.
2. Dock the ligand inside the target binding site with a greedy optimisation algorithm with multiple restarts. The scoring function driving docking considers only geometrical steric effects. Ligand flexibility is taken into account; the pocket is a rigid body. In the experiment, 256 different initial poses were evaluated for each ligand.
3. Sort the generated poses to select a few for re-scoring: cluster poses using an RMSD of 3 Å as the threshold for deeming two poses similar, then sort so that the top-scoring pose of each cluster comes first, followed by all others sorted by the geometrical scoring function. In the experiment only the top 30 poses per ligand were scored.
4. Re-score with the LiGen chemical scoring function. The ligand's score is the score of the best pose found.

The algorithm is implemented in C++17 for CPUs, with OpenACC and CUDA implementations for accelerators; CUDA is fastest on NVIDIA GPUs. Asymptotic complexity is O(n·m) for n atoms and m torsional bonds (features of the docking site are omitted since they are constant during the application's lifetime).

Figure 2 measures the time to dock and score a ligand on a Marconi100 node while varying implementation, atom count and torsional-bond count (2a: C++ on a single core of an IBM 8335-GTG 2.6 GHz; 2b: CUDA on a single NVIDIA V100). Per the text: the C++ implementation's performance is as expected (roughly 100–1,100 ms across 20–120 atoms and 1–20 torsional bonds), while the CUDA one (roughly 2–18 ms over the same range) is less related to the number of atoms, because hardware parallelism can process atoms in parallel whereas torsional bonds must be processed serially to preserve molecule geometry. Because elaboration is organised in bundles of 32 atoms, docking time increases steeply after 64 and after 96 atoms. In both implementations docking time is heavily input-dependent: the difference between the fastest and slowest class of ligands is more than one order of magnitude.

## 3.2 Exscalate high-throughput docking application
The only information needed to dock and score a ligand in the target binding site is their description, so virtual screening is an embarrassingly parallel problem. It is nonetheless of paramount importance to design how data are read from storage, transferred to the accelerator, and written back.

The application (Figure 3) is an MPI application implementing an asynchronous pipeline: one process per available node, each spawning a pipeline that uses all the node's computation resources, with a dedicated thread per pipeline stage and a thread-safe input queue per stage.
- Reader: reads a chunk of data from the file representing the chemical library and enqueues it in the splitter's queue.
- Splitter: inspects each chunk to separate all the ligand descriptions it contains, enqueuing each description in the docker's queue. In the experiment a ligand is described with a custom binary format derived from TRIPOS Mol2.
- Docker: dequeues a ligand description, constructs the related data structures, performs dock and score, and enqueues the ligand's score in the writer's queue.
- Writer: dequeues the score and accumulates the output (the ligand's SMILES representation and its score value, CSV-like) in an internal buffer; when the buffer is full it initiates the writing procedure.

Only the docker stage can be composed of several threads operating on the same queues, enabling work stealing. Different algorithm implementations (CUDA and C++) can be used to leverage node heterogeneity; any docker thread is a worker — CUDA workers or CPP workers accordingly. A single CUDA worker is tied to a single GPU, but multiple CUDA workers may be tied to the same GPU. The target binding site is considered constant during elaboration, so each process fetches its information once at the beginning; each implementation stores pocket data structures in the most appropriate memory location during initialisation — constant static memory for C++, texture memory for CUDA.

The Exscalate Docking Pipeline library contains all stage implementations. It parallelises computation using the high-level interfaces for MPI and C++ threads provided by libdpipe. The LiGenDock/LiGenScore libraries implement the domain-specific functional concerns. The hardware stack is CINECA/ENI computation nodes: CPUs, 4× NVIDIA V100 GPUs, InfiniBand network interface card.

Even though the problem is embarrassingly parallel, all application instances must be synchronised with MPI when performing I/O (Figure 4). To distribute the workload the input file is split into even slabs according to file size and the number of MPI processes. Because a molecule description's size depends on ligand properties such as atom count, a slab seldom starts and ends exactly at description boundaries; by convention each process elaborates all ligands whose description begins between its slab start and stop, so the last description may end after the slab stop. On the one hand this is a very I/O-friendly access pattern, reading a file sequentially. On the other hand the static data partition negates work stealing among MPI processes, so application throughput equals that of the slowest process. The frequency at which each process reads from the input file depends on pipeline throughput. The writer stage uses collective I/O operations to coalesce write requests before writing to storage; the user can configure the number of processes that issue I/O operations to reduce pressure on the file system. All writing operations are parallel and sequential, which is I/O-friendly.

## 3.3 Exscalate workflow
In principle all ligands could be stored in a single file and the docking application deployed on the whole machine, but this has drawbacks. The main concern is fault resiliency: the default action on a fault in an MPI communicator, for example after a node failure, is to terminate all processes, which can lose a significant amount of computation effort — a well-known problem in the literature. Another concern is performance: docking and scoring a large, complex ligand takes much more time than a small, simple one, so there is significant imbalance between MPI processes if all the ligands with many atoms and torsional bonds are close together.

The Exscalate workflow (Figure 5) addresses these with a pre-processing phase on the chemical library, yielding a relatively small number of jobs that can run in parallel using a plain job array such as those provided by SLURM or PBS. It requires two kinds of domain input. First, the binding sites of the target proteins — obtaining them is a complex procedure considered outside the scope of the article. Second, the chemical library of molecules to evaluate; here the library is assumed to be stored in SMILES format, which encodes a molecule in a single string containing only its structure (ignoring hydrogen), the most compact option.

The next pre-processing step broadly classifies ligands into buckets according to expected execution time, to reduce imbalance during computation. Torsional-bond and atom counts seem good predictors, but they are not trivial to extract from the SMILES representation. For this reason a model was trained to predict execution time from properties more accessible at this point of the workflow: the number of heavy atoms, the number of rings, and the number of chains, also considering interactions between them. A decision tree model with a maximum depth of 16 predicts the ligand's execution time.

After classification by complexity, pre-processing proper is performed: for each ligand, hydrogen atoms are added, the initial displacement of its atoms in 3D space is generated, and the molecule is unfolded (Section 3.1). This elaboration is required once and can be reused in all virtual screening campaigns. In addition to ligand pre-processing, the size of the ligand binary files used in the docking phase must be set.

Finally, with target binding sites and ligand binaries in hand, the virtual screening campaign launches the docking application on all ligand files, one pocket at a time. Its output is the ranking of the chemical library against each docking site. When domain experts select ligands with a strong interaction with multiple docking sites or proteins, the 3D displacement of the ligand's atoms can be recreated on demand; for this reason only the molecule's structure in SMILES notation need be stored.

# 4. EXPERIMENTAL RESULTS
The platform was validated by a virtual screening campaign over the ligand library against 15 binding sites of 12 viral proteins of SARS-CoV-2. (Note: the opening sentence of §4 reads "70 million ligands", which contradicts the 70+ billion reported in the abstract, §1 and §5; apparently a typo.) The platform was deployed on HPC5 at ENI and Marconi100 at CINECA. A Marconi100 node has 32 IBM POWER9 AC922 cores (128 hardware threads) and 4 NVIDIA V100 GPUs with NVLINK 2.0. An HPC5 computation node is very similar, also with 4 NVIDIA V100 GPUs, but relies on Intel Xeon Gold 6252 24C CPUs (24 cores, 48 hardware threads) and uses NVLINK only for GPU interconnection.

## 4.1 Evaluating the storage requirements
Storage is a main concern in HPC systems; at the scale of a trillion docking operations what is read and written, and in what format, must be evaluated in detail.

Binding-site information for the target proteins is not an issue: 29 MB total, read once when the application starts. The chemical library needs more care. Domain experts work with SMILES as the most compact representation; the library evaluated in the experiment requires 3.3 TB in SMILES. The docking application requires a richer molecule description. The most widely used format for that information is TRIPOS Mol2, encoded in ASCII characters and focused on readability rather than efficiency; instead a custom binary format stores only the information the docking application requires, such as atom position, type and bonds. Comparing the same molecules, Mol2 requires 5–6× more space than the binary format. Nonetheless the whole binary chemical library for the experiment requires 59 TB of storage.

Storing all docked poses is unfeasible: with 15 binding sites and 30 alternative re-scored poses per input ligand it would require 26 PB. Instead only the molecule's SMILES and its best score are stored in a CSV-like file, and the docked pose can be regenerated on demand because the docking algorithm is deterministic. The size of the final output is 7.3 TB of data. (§5 instead states that the results account for 64 TB of data; the discrepancy is not explained in the paper.)

## 4.2 Predicting the ligand complexity
The main shortcoming of the docking application is its inability to perform work stealing among different nodes, potentially leading to execution imbalance. For this reason the workflow clusters the input chemical library according to the expected time to elaborate a ligand, using features trivially accessible from the SMILES format.

Figure 6 shows the campaign used to train a decision tree regressor (scikit-learn) to predict docking time from the number of heavy atoms, rings and chains, and their interactions. Figure 6a shows measured execution time for a dataset of 21 million ligands with differing numbers of atoms and torsional bonds (the histogram spans roughly 0–65 ms, with most mass below ~25 ms). 80% of the data was used to train the model and the remainder to compute the prediction error in Figure 6b (errors concentrated near 0, spanning roughly −20 to +20 ms). The model has a negligible mean error (−0.00088 ms) with a standard deviation of 3.81 ms.

Even though the average error is close to zero, the standard deviation shows that the docking time of a given ligand is mispredicted. In the experiment ligands were clustered in buckets of 10 ms to account for this variability. Since high-throughput docking aims at avoiding imbalance, the average behaviour is what matters.

## 4.3 Exploiting node heterogeneity
Having multiple implementations of the dock-and-score algorithm grants access to heterogeneous resources, but the relationship between the number of CUDA and CPU workers and application throughput is not trivial. Figure 7 shows application throughput in docked ligands per second while varying the number of CUDA workers (columns: 4, 8, 12, 16, 24, 32, 48, 64, 128) and CPP workers (rows: 0, 4, 8, 12, 16, 20, 32, 48, 64, 96, 128) on a Marconi100 node. The application binds each CUDA worker to a single GPU round-robin: with 24 CUDA workers, 6 threads feed data and retrieve results for each GPU in the node.

Reported values range from 659 to 2,414 ligands/s. Throughput peaks at high CUDA-worker counts (e.g. 2,414 at 16 CPP × 64 CUDA; 2,406 at 12 CPP × 128 CUDA; 2,400 at 20 CPP × 128 CUDA), while the 128-CPP-worker row collapses to 659–985 ligands/s. Increasing CPU workers to match the number of hardware threads harms performance: in this case study it is better to use CPUs to support accelerators and I/O operations rather than to contribute to the elaboration itself. Furthermore, a single CUDA worker is not enough to benefit most from a GPU, because the CUDA worker must parse the ligand description and initialise the related data structures before launching any CUDA kernel; using more CUDA workers hides these overheads and fully utilises the GPU.

This analysis used the dataset "Commercial Compound MW<330" from the MEDIATE website, 5 million small molecules, publicly available.

## 4.4 Scaling on the target HPC machine
To overcome the limitations of a single MPI application running on the whole supercomputer, several instances are run on different portions of the input data. The input set was divided into ~3,400 jobs, each composed of 32 MPI processes lasting about 5 minutes and targeting a single binding site. For this experiment the binding sites were evaluated sequentially.

### Table 2 — Throughput reached per node and per machine for each binding site
| Binding site | Thr (ligands/sec/node) | Thr (ligands/sec) | HPC machine |
|---|---|---|---|
| PLPRO | 2496 | 1,996,800 | M100 |
| SPIKEACE | 2498 | 1,998,400 | M100 |
| NS12thumb | 2499 | 1,999,200 | M100 |
| NS13palm | 2486 | 1,988,800 | M100 |
| 3CL | 2427 | 1,941,600 | M100 |
| NSP13allo | 2498 | 1,998,400 | M100 |
| Nprot | 2010 | 3,015,000 | HPC5 |
| NSP16 | 1980 | 2,970,000 | HPC5 |
| NSP3 | 1969 | 2,953,500 | HPC5 |
| NSP6 | 1985 | 2,977,500 | HPC5 |
| NSP12ortho | 2001 | 3,001,500 | HPC5 |
| NSP14 | 1965 | 2,947,500 | HPC5 |
| NSP9 | 1996 | 2,994,000 | HPC5 |
| NSP15 | 1990 | 2,985,000 | HPC5 |
| NSP13ortho | 2454 / 1987 | 1,963,200 / 2,980,500 | M100 / HPC5 |

(NSP13ortho was partially computed on both machines.)

Node throughput was computed by sampling application log files for the average throughput per MPI process (equal to node performance) and averaging. Machine throughput was computed by dividing the time-to-solution of the experiment — the wall time required to dock the whole chemical library against the target docking site — by the number of ligands in the library, so it takes into consideration all execution overheads. On average, single-node throughput is 2.2k ligands per second, while the combined throughput of both supercomputers is 5M ligands per second.

The per-node throughput measured while scaling to the whole machine is comparable to that measured while tuning the number of CUDA and CPU workers; therefore the Exscalate platform was able to exploit all the available resources.

# 5. CONCLUSION
In the context of urgent computing, the Exscalate molecular docking platform was re-designed to target HPC systems and used to perform the largest virtual screening campaign against 15 binding sites of 12 viral proteins of SARS-CoV-2. The results account for 64 TB of data representing the score of each of the 70+ billion ligands on the target pockets. The set of most promising compounds filtered for each target has been made available on the MEDIATE portal (https://mediate.exscalate4cov.eu/data.html) to permit researchers around the world to start more detailed de-novo campaigns from a reduced set of compounds. The document describes the Exscalate platform design from a software engineering point of view and reports its validation in the experiment: the docking application can hinge on a node's accelerators to carry out computation while using the CPU mainly to support it — synchronising I/O toward the file system and feeding the GPUs with data — and it scaled over the two full HPC systems, CINECA-Marconi100 and ENI-HPC5, which at the time of the experiment were the most powerful European supercomputers.

# ACKNOWLEDGEMENTS
Conducted under the project "EXaSCale smArt pLatform Against paThogEns for Corona Virus — Exscalate4CoV", funded by the EU's H2020-SC1-PHE-CORONAVIRUS-2020 call, grant N. 101003551.

# SELECTED REFERENCES (as cited in the text)
- Pagadala, Syed, Tuszynski. Software for molecular docking: a review. *Biophysical Reviews* 9, 91–102 (2017).
- Neves, Totrov, Abagyan. Docking and scoring with ICM. *J. Comput.-Aided Mol. Design* 26, 675–686 (2012).
- Ng, Fong, Siu. PSOVina. *J. Bioinform. Comput. Biol.* 13, 1–18 (2015).
- Pang et al. EUDOC on the IBM Blue Gene/L system. *IBM J. Res. Dev.* 52, 69–81 (2010).
- Morris et al. AutoDock4 and AutoDockTools4. *J. Comput. Chem.* 30, 2785–2791 (2009).
- LeGrand et al. GPU-accelerated drug discovery with docking on the Summit supercomputer. ACM-BCB (2020), 1–10.
- Glaser et al. High-throughput virtual laboratory for drug discovery using massive datasets. *IJHPCA* (2021).
- Wójcikowski, Ballester, Siedlecki. Performance of machine-learning scoring functions in structure-based virtual screening. *Sci. Rep.* 7 (2017). [RFScore-VS]
- Jain et al. FireWorks: a dynamic workflow system. *Concurrency Computat.* 27, 5037–5059 (2015).
- Weininger. SMILES. *J. Chem. Inf. Comput. Sci.* 28, 31–36 (1988).
- Veber et al. Molecular properties that influence the oral bioavailability of drug candidates. *J. Med. Chem.* 45, 2615–2623 (2002).
- Vitali et al. Accelerating a geometric approach to molecular docking with OpenACC. PBio (2018), 45–51.
- Beato, Beccari, Cavazzoni, Lorenzi, Costantino. Use of experimental design to optimize docking performance: the case of LiGenDock, the docking module of LiGen. (2013).
- Vitali, Gadioli, Palermo, Beccari, Cavazzoni, Silvano. Exploiting OpenMP and OpenACC to accelerate a geometric approach to molecular docking in heterogeneous HPC nodes. *J. Supercomput.* 75, 3374–3396 (2019).
- Snir et al. Addressing failures in exascale computing. *IJHPCA* 28, 129–173 (2014).
- Rocco, Gadioli, Palermo. Legio: fault resiliency for embarrassingly parallel MPI applications. *J. Supercomput.* (2021).
- Yoo, Jette, Grondona. SLURM. JSSPP (2003), 44–60.
- Gervasoni et al. A comprehensive mapping of the druggable cavities within the SARS-CoV-2 therapeutically relevant proteins by combining pocket and docking searches as implemented in Pockets 2.0. *IJMS* 21, 5152 (2020).
- Pedregosa et al. Scikit-learn. *JMLR* 12, 2825–2830 (2011).
