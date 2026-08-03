# Contributing standard / 标准化流程

This repo is a **pipeline**, not just a folder of notes. Follow the same steps
for every new paper so the bib, graph, and site stay consistent and the whole
thing keeps building itself.

## 0. One-time setup

```bash
pip install -r requirements.txt
```

## 1. Add the item

```bash
python scripts/add_paper.py <url|doi|arxiv> --category <c> --relevance <high|medium|low>
```

- `<url|doi|arxiv>`: a landing URL, a bare DOI (`10.1038/...`), or an arXiv id (`2406.16192`).
- `--category`: one of `single-cell, spatial, virtual-tissue, histopath, foundation, pathology, imaging, competition, other`.
- This creates `papers/<slug>/` containing:
  - `metadata.yaml` — auto-filled (title, authors, year, venue, doi, s2_id, abstract-driven `status`).
  - `deep-read.md`, `ai-ready.md` — from `templates/`, pre-filled with what we know.
  - `citation.bib` — BibTeX fetched via DOI content-negotiation / arXiv.
  - `s2.json` *(optional)* — cache Semantic Scholar output here (`references`) to make the graph reproducible offline.

## 2. Read & fill

Edit `papers/<slug>/deep-read.md` — keep every section **bilingual (中 + EN)**.
Mandatory sections: 一句话/One-liner, 研究问题/Problem, 方法/Method, 数据/Data,
主要结果/Key results, 创新点/Contributions, 局限/Limitations,
**与本研究方向的关系/Relation to our direction**, 可复用资产/Reusable assets.

Paywalled paper? Leave `status: abstract-only`. Later, drop the PDF at
`papers/<slug>/source.pdf` and enrich `ai-ready.md` + the full-text sections.

## 3. Rebuild the derived artifacts (always, in this order)

```bash
python scripts/build_bib.py            # references.bib
python scripts/build_relationships.py  # relationships/graph.* + relationships.md
python scripts/build_site.py           # docs/ + mkdocs.yml nav
```

These are **idempotent** — safe to re-run any time. Never hand-edit
`references.bib`, `relationships/relationships.md`, `docs/**`, or the generated
`mkdocs.yml`; edit the sources (`citation.bib`, `_narrative.md`, the templates)
and rebuild. The relationship narrative is hand-written in
`relationships/_narrative.md` and prepended into `relationships.md` on build.

## 4. Preview & commit

```bash
mkdocs serve                           # optional local check
mkdocs build --strict                  # must pass (CI runs this too)
git add -A && git commit -m "add <slug>: <short title>" && git push
```

Pushing to `main` triggers `.github/workflows/pages.yml`, which rebuilds and
deploys the site.

## Conventions

- **slug** = short kebab of title/topic + year (e.g. `virchow-2024`, `hest1k-2024`).
- **bibkey** comes from the fetched BibTeX; keep it stable once cited.
- **relevance `high`** ⇔ the ★ items the PI flagged; surfaces first everywhere.
- One item = one folder. Datasets/models/repos/competitions are valid items
  (`type: dataset|model|code|competition`) with a lighter "resource card" read.
