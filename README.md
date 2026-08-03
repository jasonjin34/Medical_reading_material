# Medical Reading Material

A **living, standardized literature base** for one research direction:

> **Anomaly-detection-based virtual tissue modelling** — detect regions of
> biomedical images & spatial-omics that changed due to disease or drug
> perturbation, model them as *virtual tissues*, then predict the key genes to
> **revert** the anomaly (experimental validation done by a wet-lab team).

Every paper gets: a bilingual (中英) close-reading, an AI-ready text extract, a
BibTeX entry, and a place in the relationship graph — all browsable as a website.

## What's inside

| Path | 内容 / What |
|---|---|
| `papers/<slug>/deep-read.md` | 论文精读 — bilingual close reading |
| `papers/<slug>/ai-ready.md` | AI-ready clean text (paste into an LLM) |
| `papers/<slug>/metadata.yaml` | canonical record (doi, venue, tags, relevance…) |
| `papers/<slug>/citation.bib` | per-paper BibTeX fragment |
| `references.bib` | 引用库 — all entries, auto-built |
| `literature-review.md` | 综述 — synthesis across all papers |
| `relationships/` | citation/topic graph (`graph.json`, `graph.mmd`, `relationships.md`) |
| `docs/` + `mkdocs.yml` | the GitHub Pages site (auto-generated) |
| `templates/`, `scripts/` | the standardized pipeline (see below) |

## Add a new paper (the whole workflow)

```bash
pip install -r requirements.txt          # once

python scripts/add_paper.py <url|doi|arxiv> --category foundation --relevance high
#   → creates papers/<slug>/ with metadata + templated notes + citation.bib

# edit papers/<slug>/deep-read.md  (fill the bilingual 精读)

python scripts/build_bib.py              # refresh references.bib
python scripts/build_relationships.py    # refresh the graph
python scripts/build_site.py             # refresh docs/ + mkdocs nav
git add -A && git commit -m "add <slug>" && git push
```

`--category` ∈ single-cell · spatial · virtual-tissue · histopath · foundation ·
pathology · imaging · competition · other.

See **[CONTRIBUTING.md](CONTRIBUTING.md)** for the full standard.

## Local preview

```bash
mkdocs serve      # http://127.0.0.1:8000
```

## Live site

Published via GitHub Actions to
**https://jasonjin34.github.io/Medical_reading_material/**
(enable once: repo **Settings → Pages → Source: GitHub Actions**).
