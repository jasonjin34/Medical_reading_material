#!/usr/bin/env python3
"""Build the knowledge-map views — web (Cytoscape.js) and Obsidian — from one source.

Sources (hand-written):
    papers/*/metadata.yaml     plans / track / recommended_by decide view membership
    maps/views.yaml            columns, core concepts and their match patterns per view
    maps/matrix.yaml           method × data matrix: cells, Plan A gaps, method-lineage transfers
    maps/labels.yaml           short node labels
    maps/viewer.html           the interactive viewer (copied verbatim)
    scripts/build_relationships.py  CONCEPT_EDGES (paper ↔ paper), via relationships/graph.json
    glossary/*.yaml            definitions + `seen_in` links for concepts

Generated (do not hand-edit):
    docs/maps/viewer.html, docs/maps/<view>.json, docs/maps/matrix.html, docs/maps/matrix.json
    docs/knowledge-map.md, docs/knowledge-map.zh.md
    _maps/                     Obsidian hub notes, concept notes, MOCs and canvases

Run after build_relationships.py and before build_site.py:
    python scripts/build_maps.py
"""
from __future__ import annotations

import json
import re
import shutil
from collections import defaultdict
from pathlib import Path

import yaml

import _meta

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
MAPS_SRC = ROOT / "maps"
MAPS_WEB = DOCS / "maps"
VAULT = ROOT / "_maps"

COL_W, ROW_H = 270, 54           # web layout grid (Cytoscape model units)
CONCEPT_ROW_H = 46
CANVAS_COL_W, CANVAS_CARD_W, CANVAS_CARD_H, CANVAS_ROW_H = 440, 400, 140, 170
CANVAS_MAX_CARDS = 20
FLOW_TOP = 3                     # papers shown per pipeline step (Mermaid label, flow canvas)

PLAN_ORDER = ["A", "B", "EHR"]


# --------------------------------------------------------------------------- #
# Loading
# --------------------------------------------------------------------------- #
def load_views() -> dict:
    return yaml.safe_load((MAPS_SRC / "views.yaml").read_text(encoding="utf-8"))["views"]


_MATRIX: dict | None = None


def load_matrix() -> dict:
    global _MATRIX
    if _MATRIX is None:
        f = MAPS_SRC / "matrix.yaml"
        _MATRIX = (yaml.safe_load(f.read_text(encoding="utf-8")) or {}) if f.exists() else {}
    return _MATRIX


def load_glossary() -> dict:
    terms = {}
    for f in sorted((ROOT / "glossary").glob("*.yaml")):
        for t in yaml.safe_load(f.read_text(encoding="utf-8")) or []:
            terms.setdefault(t["id"], t)
    return terms


def load_paper_edges(slugs: set) -> list[dict]:
    """Curated paper↔paper edges (concept) and citations from relationships/graph.json."""
    g = json.loads((ROOT / "relationships" / "graph.json").read_text(encoding="utf-8"))
    out, seen = [], set()
    for e in g["edges"]:
        if e["type"] not in ("concept", "cites"):
            continue
        a, b = e["source"], e["target"]
        if a not in slugs or b not in slugs:
            continue
        key = tuple(sorted((a, b)))
        if key in seen:
            continue
        seen.add(key)
        out.append({"source": a, "target": b, "kind": e["type"], "label": e.get("label", "cites")})
    return out


def deep_read_en(slug: str) -> str:
    f = _meta.PAPERS / slug / "deep-read.md"
    if not f.exists():
        return ""
    lines = [ln.split("<!-- EN -->", 1)[1] for ln in f.read_text(encoding="utf-8").splitlines()
             if "<!-- EN -->" in ln]
    return "\n".join(lines)


def one_liner(slug: str) -> dict:
    f = _meta.PAPERS / slug / "deep-read.md"
    out = {"en": "", "zh": ""}
    if not f.exists():
        return out
    text = f.read_text(encoding="utf-8")
    m = re.search(r"^## [^\n]*One-liner\s*\n(.*?)(?=^## )", text, flags=re.M | re.S)
    if not m:
        return out
    for ln in m.group(1).splitlines():
        for tag, lang in (("<!-- ZH -->", "zh"), ("<!-- EN -->", "en")):
            if tag in ln and not out[lang]:
                part = ln.split(tag, 1)[1]
                if lang == "zh" and "<!-- EN -->" in part:
                    part = part.split("<!-- EN -->", 1)[0]
                out[lang] = re.sub(r"\*\*|`", "", part).strip()
    return out


_LABELS: dict | None = None


def short_label(m: dict) -> str:
    global _LABELS
    if _LABELS is None:
        f = MAPS_SRC / "labels.yaml"
        _LABELS = (yaml.safe_load(f.read_text(encoding="utf-8")) or {}) if f.exists() else {}
    if m["_dir"] in _LABELS:
        return _LABELS[m["_dir"]]
    title = (m.get("title") or m["id"]).strip()
    if "/" in title and " " not in title:                 # GitHub / HF repo ids
        return title.split("/")[-1]
    head = re.split(r"[:–—]", title, maxsplit=1)[0].strip()
    if head != title and len(head) <= 28:
        return head
    authors = m.get("authors") or []
    first = (authors[0] if authors else "").split(",")[0].strip()
    year = m.get("year") or ""
    if first and len(first) <= 24:
        return f"{first} {year}".strip()
    return title[:28] + "…"


# --------------------------------------------------------------------------- #
# View assembly
# --------------------------------------------------------------------------- #
def select_papers(spec: dict, metas: list[dict]) -> list[dict]:
    sel = spec.get("select", {})
    out = []
    for m in metas:
        plans = m.get("plans") or []
        if sel.get("all") or \
           ("plans" in sel and sel["plans"] in plans) or \
           ("plans_all" in sel and all(p in plans for p in sel["plans_all"])) or \
           ("recommended_by" in sel and m.get("recommended_by") == sel["recommended_by"]):
            out.append(m)
    return out


def _tracks(m: dict) -> list[str]:
    t = m.get("track") or []
    return [t] if isinstance(t, str) else list(t)


def column_of(view_id: str, spec: dict, m: dict) -> str:
    if "column_of" in spec:
        return spec["column_of"].get(m["_dir"], "")
    if view_id == "overview":
        return m.get("category", "other")
    if view_id == "ehr":
        return "EHR"
    tracks = _tracks(m)
    own = spec.get("tracks", {})
    for t in tracks:                       # the paper's track that this view has a column for
        if t in own:
            return t
    return tracks[0] if tracks else ""


def columns_for(view_id: str, spec: dict, papers: list[dict], views: dict) -> list[tuple[str, dict]]:
    if "columns" in spec:
        return list(spec["columns"].items())
    if "tracks" in spec:
        return list(spec["tracks"].items())
    if view_id == "bridge":
        tracks = {**views["plan-a"]["tracks"], **views["plan-b"]["tracks"]}
        used = sorted({_tracks(m)[0] for m in papers if _tracks(m)})
        return [(t, tracks[t]) for t in used if t in tracks]
    if view_id == "ehr":
        return [("EHR", {"en": "EHR & trajectories", "zh": "电子病历与轨迹"})]
    if view_id == "overview":
        import build_site
        used = {m.get("category", "other") for m in papers}
        return [(c, {"en": build_site.CAT_LABEL.get(c, c), "zh": build_site.CAT_LABEL.get(c, c)})
                for c in build_site.CAT_ORDER if c in used]
    return []


def concept_specs(view_id: str, spec: dict, views: dict) -> dict:
    out = {}
    for v in spec.get("concepts_from", []):
        out.update(views[v].get("concepts", {}))
    if "concepts_pick" in spec:
        out = {k: out[k] for k in spec["concepts_pick"]}
    out.update(spec.get("concepts", {}) or {})
    return out


def concept_links(cspecs: dict, papers: list[dict], glossary: dict) -> dict[str, list[str]]:
    texts = {m["_dir"]: deep_read_en(m["_dir"]) for m in papers}
    slugs = set(texts)
    links: dict[str, list[str]] = {}
    for cid, c in cspecs.items():
        pats = [re.compile(p, re.I) for p in c.get("match", [])]
        need, cap = c.get("min_hits", 2), c.get("max_links", 6)
        scored = []
        for s, t in texts.items():
            n = sum(len(p.findall(t)) for p in pats)
            if n >= need:
                scored.append((-n, s))
        hit = [s for _, s in sorted(scored)[:cap]]
        g = glossary.get(c.get("glossary", ""), {})
        hit += [s for s in g.get("seen_in", []) if s in slugs and s not in hit][: max(0, cap - len(hit))]
        links[cid] = sorted(hit)
    return links


def build_view(view_id: str, spec: dict, views: dict, metas: list[dict],
               glossary: dict) -> dict:
    papers = select_papers(spec, metas)
    slugs = {m["_dir"] for m in papers}
    cols = columns_for(view_id, spec, papers, views)
    col_index = {cid: i for i, (cid, _) in enumerate(cols)}
    plan_key = {"plan-a": "A", "plan-b": "B"}.get(view_id)

    nodes, edges = [], []
    # groups (one per column) and papers, stacked newest first inside a column
    by_col = defaultdict(list)
    for m in papers:
        by_col[column_of(view_id, spec, m)].append(m)
    paper_x = {}
    max_rows = 0
    for cid, label in cols:
        items = sorted(by_col.get(cid, []),
                       key=lambda m: (-(m.get("relevance") == "high"), -(int(m.get("year") or 0)),
                                      short_label(m).lower()))
        x = col_index[cid] * COL_W
        nodes.append({"id": f"group:{cid}", "kind": "group", "label": label,
                      "code": cid, "count": len(items), "x": x, "y": 0})
        for r, m in enumerate(items):
            s = m["_dir"]
            plans = m.get("plans") or []
            other = [p for p in plans if p != plan_key and p in ("A", "B")] if plan_key else []
            paper_x[s] = x
            nodes.append({
                "id": s, "kind": "paper", "parent": f"group:{cid}",
                "label": short_label(m), "title": m.get("title", s),
                "year": m.get("year"), "venue": m.get("venue") or "",
                "relevance": m.get("relevance", ""), "status": m.get("status", ""),
                "type": m.get("type", "paper"), "plans": plans, "also_in": other,
                "bridge": "A" in plans and "B" in plans,
                "recommended_by": m.get("recommended_by", ""),
                "oneliner": one_liner(s),
                "url": {"en": f"../papers/{s}/", "zh": f"../zh/papers/{s}/"},
                "x": x, "y": 70 + r * ROW_H,
            })
        max_rows = max(max_rows, len(items))
    unplaced = sorted(slugs - set(paper_x))
    if unplaced:
        raise SystemExit(f"! view {view_id}: papers without a column: {unplaced}")

    # concept nodes: each sits under its "home" column (the column holding most of its papers)
    cspecs = concept_specs(view_id, spec, views)
    skip = set(spec.get("concepts_skip_tracks", []))
    clinks = concept_links(cspecs, [m for m in papers if not skip & set(_tracks(m))], glossary)
    col_of_paper = {n["id"]: n["parent"] for n in nodes if n["kind"] == "paper"}
    slots = defaultdict(int)
    cnodes = []
    for cid, c in cspecs.items():
        linked = clinks.get(cid, [])
        if len(linked) < max(1, spec.get("min_links", 1)):
            continue
        counts = defaultdict(int)
        for s in linked:
            counts[col_of_paper[s]] += 1
        home = max(counts, key=lambda g: (counts[g], -next(i for i, n in enumerate(nodes) if n["id"] == g)))
        gx = next(n["x"] for n in nodes if n["id"] == home)
        gdef = glossary.get(c.get("glossary", ""), {})
        cn = {"id": f"concept:{cid}", "kind": "concept", "label": c["label"],
              "definition": {"en": gdef.get("def_en", ""), "zh": gdef.get("def_zh", "")},
              "count": len(linked), "home": home, "slot": slots[home], "x": gx,
              "y": 70 + max_rows * ROW_H + 110 + slots[home] * CONCEPT_ROW_H}
        slots[home] += 1
        cnodes.append(cn)
        for s in linked:
            edges.append({"source": cn["id"], "target": s, "kind": "mentions"})
    nodes += cnodes

    edges += [e for e in load_paper_edges(slugs)]
    have = {tuple(sorted((e["source"], e["target"]))) for e in edges if e["kind"] != "mentions"}
    for a, b, lab in load_matrix().get("transfers", []) or []:
        if a in slugs and b in slugs and tuple(sorted((a, b))) not in have:
            edges.append({"source": a, "target": b, "kind": "lineage", "label": lab})
    return {
        "flow": flow_steps(spec, nodes),
        "view": view_id,
        "title": spec["title"], "lead": spec.get("lead", {"en": "", "zh": ""}),
        "collapsed": view_id in ("plan-a", "plan-b", "overview"),
        "wrap": spec.get("wrap", 0),
        "nodes": nodes, "edges": edges,
        "stats": {"papers": len(papers), "concepts": len(cnodes), "edges": len(edges)},
    }


def flow_steps(spec: dict, nodes: list[dict]) -> list[dict]:
    """Pipeline steps of a view, each with its papers (must-read first, in column order)."""
    steps = []
    for st in spec.get("flow", []) or []:
        groups = [f"group:{c}" for c in st["columns"]]
        kids = [n for g in groups for n in nodes if n.get("parent") == g]
        kids.sort(key=lambda n: n["relevance"] != "high")          # stable: keeps column order
        steps.append({"id": st["id"], "label": st["label"], "columns": st["columns"],
                      "count": len(kids), "papers": [n["id"] for n in kids],
                      "top": [n["label"] for n in kids[:FLOW_TOP]]})
    return steps


def mermaid_flow(d: dict, lang: str) -> str:
    def q(t: str) -> str:                  # markdown-string labels (Mermaid ≥ 10.1): no quotes / backticks / *
        return t.replace('"', "'").replace("`", "'").replace("*", "")
    unit = "papers" if lang == "en" else "篇"
    out = ["flowchart TD"]
    for i, st in enumerate(d["flow"], 1):
        top = " · ".join(st["top"])
        out.append(f'  s{i}["`**{i}. {q(st["label"][lang])}** ({st["count"]} {unit})\n{q(top)}`"]')
    out += [f"  s{i} --> s{i + 1}" for i in range(1, len(d["flow"]))]
    return "\n".join(out)


def build_matrix(metas: list[dict]) -> dict:
    """Method × data matrix: rows = AD paradigms, cols = data domains, papers in cells, lineage arrows."""
    mx = load_matrix()
    by_slug = {m["_dir"]: m for m in metas}
    rows, cols = mx["rows"], mx["cols"]
    cells, papers, missing = defaultdict(list), {}, []
    for s, where in mx["cells"].items():
        if s not in by_slug:
            missing.append(s)
            continue
        pairs = [where] if isinstance(where[0], str) else where
        for r, c in pairs:
            if r not in rows or c not in cols:
                raise SystemExit(f"! matrix: {s} in unknown cell {r}/{c}")
            cells[f"{r}|{c}"].append(s)
        m = by_slug[s]
        papers[s] = {"label": short_label(m), "title": m.get("title", s), "year": m.get("year"),
                     "venue": m.get("venue") or "", "relevance": m.get("relevance", ""),
                     "type": m.get("type", "paper"), "category": m.get("category", ""),
                     "plans": m.get("plans") or [], "oneliner": one_liner(s),
                     "url": {"en": f"../papers/{s}/", "zh": f"../zh/papers/{s}/"}}
    if missing:
        print(f"  ! matrix: not in papers/ yet, skipped: {', '.join(missing)}")
    for k in cells:
        cells[k].sort(key=lambda s: (papers[s]["relevance"] != "high", papers[s]["year"] or 0))
    transfers = []
    for a, b, lab in mx.get("transfers", []) or []:
        if a in papers and b in papers:
            transfers.append({"from": a, "to": b, "label": lab})
        else:
            print(f"  ! matrix: transfer {a} → {b} skipped (paper missing)")
    return {"title": mx["title"], "lead": mx["lead"],
            "rows": [{"id": k, **v} for k, v in rows.items()],
            "cols": [{"id": k, **v} for k, v in cols.items()],
            "cells": dict(cells), "papers": papers, "transfers": transfers,
            "gaps": mx.get("gaps", []) or [],
            "stats": {"papers": len(papers), "transfers": len(transfers)}}


# --------------------------------------------------------------------------- #
# Web output
# --------------------------------------------------------------------------- #
def write_web(built: dict, matrix: dict) -> None:
    if MAPS_WEB.exists():
        shutil.rmtree(MAPS_WEB)
    MAPS_WEB.mkdir(parents=True)
    shutil.copyfile(MAPS_SRC / "viewer.html", MAPS_WEB / "viewer.html")
    shutil.copyfile(MAPS_SRC / "matrix.html", MAPS_WEB / "matrix.html")
    (MAPS_WEB / "matrix.json").write_text(json.dumps(matrix, ensure_ascii=False, indent=1), encoding="utf-8")
    index = [{"id": vid, "title": d["title"], "lead": d["lead"], "stats": d["stats"]}
             for vid, d in built.items()]
    (MAPS_WEB / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")
    for vid, data in built.items():
        (MAPS_WEB / f"{vid}.json").write_text(json.dumps(data, ensure_ascii=False, indent=1),
                                              encoding="utf-8")
    for lang, name, up in (("en", "knowledge-map.md", "../"), ("zh", "knowledge-map.zh.md", "../../")):
        out = ["# Knowledge map\n" if lang == "en" else "# 知识图谱\n"]
        out.append(
            "Each view is its own graph. Groups start collapsed: click a group to open it, click a "
            "node to see its neighbours, double-click a paper to open its deep-read.\n"
            if lang == "en" else
            "每个视图是一张独立的图。组默认折叠：点击组展开，点击节点只看它的邻居，双击论文打开精读。\n")
        out.append((f"## Method map\n\n{matrix['lead']['en']} "
                    f"[Open full screen ↗](maps/matrix.html?lang=en){{target=_blank}}\n" if lang == "en" else
                    f"## 方法图\n\n{matrix['lead']['zh']} "
                    f"[全屏打开 ↗](maps/matrix.html?lang=zh){{target=_blank}}\n"))
        out.append(f'<iframe src="{up}maps/matrix.html?lang={lang}&embed=1" '
                   f'style="width:100%;height:760px;border:1px solid var(--md-default-fg-color--lightest);'
                   f'border-radius:6px" loading="lazy"></iframe>\n')
        out.append("## Reading-list views\n" if lang == "en" else "## 按阅读清单的视图\n")
        out.append("| View | Papers | Concepts |\n| --- | --- | --- |" if lang == "en"
                   else "| 视图 | 论文 | 概念 |\n| --- | --- | --- |")
        for vid, d in built.items():
            href = f"maps/viewer.html?view={vid}&lang={lang}"   # mkdocs rewrites md links per page
            out.append(f"| [{d['title'][lang]} ↗]({href}){{target=_blank}} — {d['lead'][lang]} "
                       f"| {d['stats']['papers']} | {d['stats']['concepts']} |")
        flows = [(vid, d) for vid, d in built.items() if d["flow"]]
        if flows:
            out.append("\n## Pipelines\n" if lang == "en" else "\n## 流程图\n")
            out.append("Each plan as a pipeline; every step lists its must-read papers. "
                       "The links below each chart open that step in the map.\n" if lang == "en" else
                       "每个 plan 画成一条流程，每一步列出它的必读论文。图下面的链接会在图谱里打开对应的那一步。\n")
        for vid, d in flows:
            out.append(f"### {d['title'][lang]}\n")
            out.append("```mermaid\n" + mermaid_flow(d, lang) + "\n```\n")
            steps = [f"[{i}. {st['label'][lang]}](maps/viewer.html?view={vid}&lang={lang}"
                     f"&focus=group:{st['columns'][0]}){{target=_blank}}"
                     for i, st in enumerate(d["flow"], 1)]
            out.append(("Open in map: " if lang == "en" else "在图谱中打开：") + " · ".join(steps) + "\n")
        first = next(iter(built))
        out.append(f"\n## {built[first]['title'][lang]}\n")
        out.append(f'<iframe src="{up}maps/viewer.html?view={first}&lang={lang}&embed=1" '
                   f'style="width:100%;height:640px;border:1px solid var(--md-default-fg-color--lightest);'
                   f'border-radius:6px" loading="lazy"></iframe>\n')
        (DOCS / name).write_text("\n".join(out) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------- #
# Obsidian output
# --------------------------------------------------------------------------- #
def _fm(d: dict) -> str:
    return "---\n" + yaml.safe_dump(d, allow_unicode=True, sort_keys=False).strip() + "\n---\n"


def _safe(name: str) -> str:
    return re.sub(r'[\\/:*?"<>|#^\[\]]', "-", name).strip()


def write_obsidian(built: dict, views: dict, metas: list[dict], glossary: dict, matrix: dict) -> None:
    if VAULT.exists():
        shutil.rmtree(VAULT)
    (VAULT / "papers").mkdir(parents=True)
    (VAULT / "concepts").mkdir()
    by_slug = {m["_dir"]: m for m in metas}

    # collect links across all views
    paper_links = defaultdict(dict)        # slug -> {other: label}
    paper_concepts = defaultdict(dict)     # slug -> {concept_id: label_en}
    concept_info = {}
    for vid, d in built.items():
        for n in d["nodes"]:
            if n["kind"] == "concept":
                concept_info[n["id"].split(":", 1)[1]] = n
        for e in d["edges"]:
            if e["kind"] == "mentions":
                cid = e["source"].split(":", 1)[1]
                paper_concepts[e["target"]][cid] = concept_info[cid]["label"]["en"]
            else:
                paper_links[e["source"]][e["target"]] = e["label"]
                paper_links[e["target"]][e["source"]] = e["label"]

    view_of = defaultdict(list)
    for vid, d in built.items():
        for n in d["nodes"]:
            if n["kind"] == "paper":
                view_of[n["id"]].append(vid)

    def plink(s: str) -> str:
        return f"[[_maps/papers/{s}|{short_label(by_slug[s])}]]"

    for s, m in by_slug.items():
        ol = one_liner(s)
        fm = {"title": m.get("title", s), "aliases": [short_label(m)],
              "plans": m.get("plans") or [], "track": _tracks(m),
              "year": m.get("year"), "relevance": m.get("relevance", ""),
              "category": m.get("category", ""), "recommended_by": m.get("recommended_by", ""),
              "views": view_of.get(s, []), "tags": ["paper"] + [f"plan/{p}" for p in m.get("plans") or []]}
        body = [_fm(fm), f"# {m.get('title', s)}\n",
                f"> {ol['en']}\n" if ol["en"] else "",
                f"> {ol['zh']}\n" if ol["zh"] else ""]
        if paper_links.get(s):
            body.append("## Related papers / 相关论文")
            body += [f"- {plink(o)} — {lab}" for o, lab in sorted(paper_links[s].items())]
            body.append("")
        if paper_concepts.get(s):
            body.append("## Concepts / 概念")
            body += [f"- [[_maps/concepts/{c}|{lab}]]" for c, lab in sorted(paper_concepts[s].items())]
            body.append("")
        body.append(f"## Deep-read / 精读\n\n![[papers/{s}/deep-read]]\n")
        (VAULT / "papers" / f"{s}.md").write_text("\n".join(body), encoding="utf-8")

    for cid, n in concept_info.items():
        linked = sorted({e["target"] for d in built.values() for e in d["edges"]
                         if e["kind"] == "mentions" and e["source"] == f"concept:{cid}"})
        body = [_fm({"title": n["label"]["en"], "aliases": [n["label"]["zh"]], "tags": ["concept"]}),
                f"# {n['label']['en']} / {n['label']['zh']}\n"]
        if n["definition"]["en"]:
            body += [f"> {n['definition']['en']}", f"> {n['definition']['zh']}\n"]
        body.append("## Papers / 论文")
        body += [f"- {plink(s)} — {by_slug[s].get('title', s)}" for s in linked]
        (VAULT / "concepts" / f"{cid}.md").write_text("\n".join(body) + "\n", encoding="utf-8")

    # one MOC + one canvas per view
    readme = ["# Knowledge maps (generated)\n",
              "Generated by `scripts/build_maps.py` — do not edit; it is overwritten on every build. "
              "Put your own notes outside `_maps/`.\n",
              "**Graph view tips:** filter with `path:_maps` to hide the raw paper folders; colour groups "
              "`tag:#plan/A`, `tag:#plan/B`, `tag:#plan/EHR`, `tag:#concept`.\n", "## Views"]
    for vid, d in built.items():
        title = d["title"]["en"]
        fname = _safe(title)
        readme.append(f"- [[_maps/{fname}|{title}]] · canvas: [[_maps/{fname}.canvas|{fname}.canvas]]")
        moc = [_fm({"title": title, "tags": ["moc"]}), f"# {title}\n",
               f"{d['lead']['en']}\n", f"{d['lead']['zh']}\n"]
        if d["flow"]:
            ftitle = f"{fname} — flow"
            readme.append(f"  - flow canvas: [[_maps/{ftitle}.canvas|{ftitle}.canvas]]")
            moc += ["## Pipeline / 流程\n", "```mermaid", mermaid_flow(d, "en"), "```\n",
                    f"Flow canvas: [[_maps/{ftitle}.canvas|{ftitle}]]\n"]
            (VAULT / f"{ftitle}.canvas").write_text(json.dumps(flow_canvas(d), indent=1), encoding="utf-8")
        groups = [n for n in d["nodes"] if n["kind"] == "group"]
        for g in groups:
            moc.append(f"## {g['label']['en']} / {g['label']['zh']}")
            for n in d["nodes"]:
                if n.get("parent") == g["id"]:
                    star = " ★" if n["relevance"] == "high" else ""
                    moc.append(f"- {plink(n['id'])}{star} — {n['title']}")
            moc.append("")
        (VAULT / f"{fname}.md").write_text("\n".join(moc), encoding="utf-8")
        (VAULT / f"{fname}.canvas").write_text(json.dumps(canvas_for(d), indent=1), encoding="utf-8")
    write_matrix_obsidian(matrix, plink)
    readme.insert(4, "- [[_maps/Method matrix|Method matrix]] · canvas: [[_maps/Method matrix.canvas|Method matrix.canvas]]")
    (VAULT / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")


def write_matrix_obsidian(mx: dict, plink) -> None:
    """Method matrix as a markdown table + lineage list, and a grid canvas of text cards."""
    gaps = {(g["row"], g["col"]): g["note"] for g in mx["gaps"]}
    head = "| Paradigm / 范式 | " + " | ".join(f"{c['en']}<br>{c['zh']}" for c in mx["cols"]) + " |"
    lines = [_fm({"title": mx["title"]["en"], "tags": ["moc", "matrix"]}), f"# {mx['title']['en']}\n",
             f"{mx['lead']['en']}\n", f"{mx['lead']['zh']}\n", head,
             "|" + " --- |" * (len(mx["cols"]) + 1)]
    for r in mx["rows"]:
        row = [f"**{r['en']}**<br>{r['zh']}"]
        for c in mx["cols"]:
            items = [plink(s) for s in mx["cells"].get(f"{r['id']}|{c['id']}", [])]
            if (r["id"], c["id"]) in gaps:
                items.append("*Plan A gap*")
            row.append("<br>".join(items) or "·")
        lines.append("| " + " | ".join(row) + " |")
    lines += ["", "## Paradigms / 范式", ""]
    for r in mx["rows"]:
        lines += [f"- **{r['en']} / {r['zh']}** — {r['idea']['en']} {r['idea']['zh']}",
                  f"  - Kidney omics / 肾脏组学: {r['omics']['en']} {r['omics']['zh']}"]
    if mx["gaps"]:
        lines += ["", "## Plan A gaps / Plan A 的空白", ""]
        lines += [f"- {g['row']} × {g['col']}: {g['note']['en']} {g['note']['zh']}" for g in mx["gaps"]]
    if mx["transfers"]:
        lines += ["", "## Method lineage / 方法迁移", ""]
        lines += [f"- {plink(t['from'])} → {plink(t['to'])} — {t['label']}" for t in mx["transfers"]]
    (VAULT / "Method matrix.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    W, H, GX, GY = 300, 220, 320, 240
    nodes = [{"id": f"col-{c['id']}", "type": "text", "text": f"## {c['en']}\n{c['zh']}",
              "x": (j + 1) * GX, "y": 0, "width": W, "height": 90, "color": "5"} for j, c in enumerate(mx["cols"])]
    for i, r in enumerate(mx["rows"]):
        y = 110 + i * GY
        nodes.append({"id": f"row-{r['id']}", "type": "text", "x": 0, "y": y, "width": W, "height": H, "color": "4",
                      "text": f"## {r['en']}\n{r['zh']}\n\n{r['idea']['en']}"})
        for j, c in enumerate(mx["cols"]):
            items = [f"- {plink(s)}" for s in mx["cells"].get(f"{r['id']}|{c['id']}", [])]
            gap = next((g for g in mx["gaps"] if g["row"] == r["id"] and g["col"] == c["id"]), None)
            if gap:
                items.append(f"\n**Plan A:** {gap['note']['en']}")
            if items:
                node = {"id": f"cell-{r['id']}-{c['id']}", "type": "text", "text": "\n".join(items),
                        "x": (j + 1) * GX, "y": y, "width": W, "height": H}
                if gap:
                    node["color"] = "1"
                nodes.append(node)
    (VAULT / "Method matrix.canvas").write_text(json.dumps({"nodes": nodes, "edges": []}, indent=1),
                                                encoding="utf-8")


def canvas_for(d: dict) -> dict:
    """JSON Canvas: one group per column, only must-read papers (≤ CANVAS_MAX_CARDS)."""
    papers = [n for n in d["nodes"] if n["kind"] == "paper"]
    keep = papers if len(papers) <= CANVAS_MAX_CARDS else [n for n in papers if n["relevance"] == "high"]
    if len(keep) > CANVAS_MAX_CARDS or not keep:
        keep = sorted(papers, key=lambda n: (n["relevance"] != "high", -(n["year"] or 0)))[:CANVAS_MAX_CARDS]
    keep_ids = {n["id"] for n in keep}
    nodes, edges = [], []
    groups = [n for n in d["nodes"] if n["kind"] == "group"]
    col = 0
    for g in groups:
        kids = [n for n in keep if n.get("parent") == g["id"]]
        if not kids:
            continue
        x = col * CANVAS_COL_W
        h = 60 + len(kids) * CANVAS_ROW_H
        nodes.append({"id": g["id"].replace(":", "-"), "type": "group", "x": x - 20, "y": -60,
                      "width": CANVAS_CARD_W + 40, "height": h + 20,
                      "label": f"{g['code']} · {g['label']['en']}"})
        for r, n in enumerate(kids):
            nodes.append({"id": n["id"], "type": "file", "file": f"_maps/papers/{n['id']}.md",
                          "x": x, "y": r * CANVAS_ROW_H, "width": CANVAS_CARD_W, "height": CANVAS_CARD_H})
        col += 1
    for i, e in enumerate(d["edges"]):
        if e["kind"] != "mentions" and e["source"] in keep_ids and e["target"] in keep_ids:
            edges.append({"id": f"e{i}", "fromNode": e["source"], "toNode": e["target"],
                          "fromSide": "right", "toSide": "left", "label": e["label"]})
    return {"nodes": nodes, "edges": edges}


def flow_canvas(d: dict) -> dict:
    """JSON Canvas: one group per pipeline step (left → right), its top papers inside, arrows between steps."""
    nodes, edges = [], []
    for i, st in enumerate(d["flow"]):
        x = i * CANVAS_COL_W
        top = st["papers"][:FLOW_TOP]
        gid = f"step-{st['id']}"
        nodes.append({"id": gid, "type": "group", "x": x - 20, "y": -60,
                      "width": CANVAS_CARD_W + 40, "height": 80 + max(1, len(top)) * CANVAS_ROW_H,
                      "label": f"{i + 1}. {st['label']['en']} / {st['label']['zh']} ({st['count']})"})
        for r, s in enumerate(top):
            nodes.append({"id": f"{gid}-{s}", "type": "file", "file": f"_maps/papers/{s}.md",
                          "x": x, "y": r * CANVAS_ROW_H, "width": CANVAS_CARD_W, "height": CANVAS_CARD_H})
        if not top:
            nodes.append({"id": f"{gid}-empty", "type": "text", "text": "—", "x": x, "y": 0,
                          "width": CANVAS_CARD_W, "height": 60})
        if i:
            edges.append({"id": f"flow{i}", "fromNode": f"step-{d['flow'][i - 1]['id']}", "toNode": gid,
                          "fromSide": "right", "toSide": "left"})
    return {"nodes": nodes, "edges": edges}


# --------------------------------------------------------------------------- #
def main() -> None:
    views = load_views()
    metas = _meta.all_meta()
    glossary = load_glossary()
    built = {vid: build_view(vid, spec, views, metas, glossary) for vid, spec in views.items()}
    matrix = build_matrix(metas)
    write_web(built, matrix)
    write_obsidian(built, views, metas, glossary, matrix)
    for vid, d in built.items():
        s = d["stats"]
        print(f"  {vid:10s} papers={s['papers']:3d} concepts={s['concepts']:2d} edges={s['edges']}")
    print(f"  matrix     papers={matrix['stats']['papers']:3d} transfers={matrix['stats']['transfers']}")
    print(f"✓ maps: {len(built)} views + method matrix → docs/maps/ + _maps/ (Obsidian)")


if __name__ == "__main__":
    main()
