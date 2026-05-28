#!/usr/bin/env python3
"""Auto-generate Obsidian call-graph notes for the EvoX codebase.

Each note contains:
    • the function's full SOURCE CODE (so clicking a node shows the code)
    • → Calls      (functions it invokes)         — graph edges
    • ← Called by   (functions that invoke it)     — backlinks

Produces THREE separate, self-contained graphs (each in its own folder):

    graphs/functions/     ALL 96 files — the complete codebase graph (~940 nodes)
    graphs/inner_loop/    just the inner solution-evolution loop
    graphs/inner_outer/   inner loop + outer (search-strategy) loop

The two focused folders use a filename prefix (IN- / IO-) so their notes never
collide with the comprehensive set or each other — that keeps each graph clean.

View a graph in Obsidian:
    Ctrl+G, then in the filter box type:
        path:graphs/inner_loop        → inner-loop-only graph
        path:graphs/inner_outer       → inner + outer graph
        path:graphs/functions         → everything

Run:
    python scripts/gen_obsidian_auto.py

Requirements:  pip install pyan3
"""

import ast
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRAPHS = ROOT / "graphs"


# ── File membership ─────────────────────────────────────────────────────────

def all_files() -> list[str]:
    pkg = ROOT / "skydiscover"
    return sorted(str(p.relative_to(ROOT)) for p in pkg.rglob("*.py"))


# Inner loop: the solution-evolution cycle (sample → prompt → LLM → parse → eval → add).
INNER_FILES = [
    "skydiscover/search/default_discovery_controller.py",
    "skydiscover/llm/llm_pool.py",
    "skydiscover/llm/openai.py",
    "skydiscover/llm/base.py",
    "skydiscover/llm/responses_utils.py",
    "skydiscover/llm/agentic_generator.py",
    "skydiscover/llm/langfuse_tracer.py",
    "skydiscover/search/base_database.py",
    "skydiscover/context_builder/evox/builder.py",
    "skydiscover/context_builder/evox/formatters.py",
    "skydiscover/context_builder/base.py",
    "skydiscover/context_builder/utils.py",
    "skydiscover/context_builder/human_feedback.py",
    "skydiscover/evaluation/evaluator.py",
    "skydiscover/evaluation/wrapper.py",
    "skydiscover/evaluation/evaluation_result.py",
    "skydiscover/utils/code_utils.py",
    "skydiscover/utils/metrics.py",
]

# Outer loop: search-strategy (meta) evolution, added on top of the inner files.
OUTER_ONLY_FILES = [
    "skydiscover/runner.py",
    "skydiscover/search/evox/controller.py",
    "skydiscover/search/evox/utils/search_scorer.py",
    "skydiscover/search/evox/utils/variation_operator_generator.py",
    "skydiscover/search/evox/utils/coevolve_logging.py",
    "skydiscover/search/evox/utils/template.py",
    "skydiscover/search/evox/database/initial_search_strategy.py",
    "skydiscover/search/evox/database/search_strategy_db.py",
    "skydiscover/search/evox/database/search_strategy_evaluator.py",
]

INNER_OUTER_FILES = INNER_FILES + OUTER_ONLY_FILES


# ── Layer tags (for graph colour groups / filtering) ─────────────────────────

LAYER_BY_PATH = [
    ("search/evox/controller.py", "outer-loop"),
    ("search/evox", "evox"),
    ("search/default_discovery_controller.py", "inner-loop"),
    ("search/adaevolve", "adaevolve"),
    ("search/beam_search", "beam-search"),
    ("search/best_of_n", "best-of-n"),
    ("search/topk", "topk"),
    ("search/gepa_native", "gepa"),
    ("search/openevolve_native", "openevolve"),
    ("search/claude_code", "claude-code"),
    ("search/base_database.py", "database"),
    ("search/registry.py", "search-core"),
    ("search/route.py", "search-core"),
    ("search/utils", "search-utils"),
    ("search/", "search"),
    ("context_builder", "context-builder"),
    ("evaluation", "evaluation"),
    ("llm/langfuse_tracer.py", "observability"),
    ("llm/", "llm"),
    ("config", "config"),
    ("utils", "utils"),
    ("extras/monitor", "monitor"),
    ("extras/external", "external"),
    ("extras", "extras"),
    ("runner.py", "runner"),
    ("cli.py", "cli"),
    ("api.py", "api"),
]


def layer_for(path: str) -> str:
    for frag, layer in LAYER_BY_PATH:
        if frag in path:
            return layer
    return "other"


# ── Source-code extraction (AST) ─────────────────────────────────────────────

def build_source_index(rel_files: list[str]) -> dict:
    """abs_path → {def_lineno: source_code_str}.

    Functions/methods: full body. Classes: header up to the first method
    (capped at 30 lines) so we don't duplicate every method inside the class.
    """
    index: dict[str, dict[int, str]] = {}
    for rel in rel_files:
        path = ROOT / rel
        try:
            src = path.read_text()
            tree = ast.parse(src)
        except Exception:
            continue
        lines = src.splitlines()
        fmap: dict[int, str] = {}
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                s = node.lineno
                e = getattr(node, "end_lineno", s)
                fmap[s] = "\n".join(lines[s - 1:e])
            elif isinstance(node, ast.ClassDef):
                s = node.lineno
                method_starts = [
                    b.lineno for b in node.body
                    if isinstance(b, (ast.FunctionDef, ast.AsyncFunctionDef))
                ]
                e = (min(method_starts) - 1) if method_starts else getattr(node, "end_lineno", s)
                e = min(e, s + 30)
                fmap[s] = "\n".join(lines[s - 1:e])
        index[str(path)] = fmap
    return index


# ── pyan3 + parsing ──────────────────────────────────────────────────────────

def run_pyan3(rel_files: list[str]) -> str:
    cmd = [sys.executable, "-m", "pyan", "--dot", "--no-defines", "--annotated"]
    cmd += [str(ROOT / f) for f in rel_files if (ROOT / f).exists()]
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    if result.returncode != 0:
        print("pyan3 error:", result.stderr[:1500])
        sys.exit(1)
    return result.stdout


def parse(raw: str):
    node_re = re.compile(
        r'^\s*"([^"]+)"\s*\[.*?label="([^"]+)".*?tooltip="([^"]+)"', re.MULTILINE
    )
    edge_re = re.compile(r'^\s*"([^"]+)"\s*->\s*"([^"]+)"', re.MULTILINE)

    nodes: dict[str, dict] = {}
    for m in node_re.finditer(raw):
        node_id, short, tooltip = m.group(1), m.group(2).split("\\n")[0], m.group(3)
        parts = tooltip.split("\\n")
        qualified = parts[0]
        path_line = parts[1] if len(parts) > 1 else ""
        kind = parts[2] if len(parts) > 2 else ""
        if not qualified.startswith("skydiscover"):
            continue
        if kind.startswith("module") or not kind:
            continue
        file_path, _, line = path_line.partition(":")
        nodes[node_id] = {
            "short": short,
            "qualified": qualified,
            "file": file_path.replace(str(ROOT) + "/", ""),
            "abs_file": file_path,
            "line": line,
            "kind": kind.split(" in ")[0] if kind else "function",
            "layer": layer_for(file_path),
        }

    edges = []
    for m in edge_re.finditer(raw):
        src, dst = m.group(1), m.group(2)
        if src in nodes and dst in nodes:
            edges.append((src, dst))
    return nodes, edges


def assign_titles(nodes: dict, prefix: str) -> None:
    """Set n['title'] (used as note filename + wiki-link target), uniquely.

    Base = last 2 dotted segments (Class.method); deepen only collisions.
    Then apply the graph prefix so notes don't collide across folders.
    """
    def at_depth(q: str, d: int) -> str:
        s = q.split(".")
        return ".".join(s[-d:]) if len(s) >= d else q

    for n in nodes.values():
        n["base"] = at_depth(n["qualified"], 2)
    for depth in (3, 4, 5, 6):
        counts = Counter(n["base"] for n in nodes.values())
        dups = {t for t, c in counts.items() if c > 1}
        if not dups:
            break
        for n in nodes.values():
            if n["base"] in dups:
                n["base"] = at_depth(n["qualified"], depth)
    counts = Counter(n["base"] for n in nodes.values())
    seen: dict[str, int] = {}
    for n in nodes.values():
        if counts[n["base"]] > 1:
            seen[n["base"]] = seen.get(n["base"], 0) + 1
            n["base"] = f"{n['base']}#{seen[n['base']]}"
    for n in nodes.values():
        n["title"] = f"{prefix}{n['base']}"


def load_rich_descriptions() -> dict:
    try:
        sys.path.insert(0, str(ROOT / "scripts"))
        from gen_obsidian_notes import NOTES  # type: ignore
    except Exception:
        return {}
    out: dict[str, str] = {}
    for stem, body in NOTES.items():
        m = re.search(r"## What it does\s*\n(.+?)(?:\n## |\Z)", body, re.DOTALL)
        if m:
            out[stem] = m.group(1).strip()
    return out


# ── Note writing ─────────────────────────────────────────────────────────────

def write_graph(rel_files: list[str], out_dir: Path, prefix: str, rich: dict) -> None:
    raw = run_pyan3(rel_files)
    nodes, edges = parse(raw)
    assign_titles(nodes, prefix)
    src_index = build_source_index(rel_files)

    calls: dict[str, list] = {nid: [] for nid in nodes}
    called_by: dict[str, list] = {nid: [] for nid in nodes}
    for s, d in edges:
        if d not in calls[s]:
            calls[s].append(d)
        if s not in called_by[d]:
            called_by[d].append(s)
    id_to_title = {nid: n["title"] for nid, n in nodes.items()}

    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("*.md"):
        old.unlink()

    strip_links = bool(prefix)  # subset graphs: keep prose links from bleeding out

    for nid, n in nodes.items():
        title = n["title"]
        layer = n["layer"]
        body = [
            "---",
            f"name: {title}",
            f"description: {n['kind']} in {n['file']} ({layer})",
            "metadata:",
            "  type: project",
            "---",
            "",
            f"# {n['base']}",
            "",
            f"**File:** `{n['file']}:{n['line']}`  ",
            f"**Kind:** {n['kind']}  ",
            f"**Layer:** #{layer}",
            "",
        ]

        canonical = ".".join(n["qualified"].split(".")[-2:])
        desc = rich.get(n["base"]) or rich.get(canonical)
        if desc:
            if strip_links:
                desc = re.sub(r"\[\[([^\]]+)\]\]", r"\1", desc)
            body += ["## What it does", desc, ""]

        # Source code
        code = src_index.get(n["abs_file"], {}).get(int(n["line"]) if n["line"].isdigit() else -1)
        body.append("## Source")
        if code:
            body += ["````python", code, "````", ""]
        else:
            body += ["_(source not extracted — see file)_", ""]

        call_titles = sorted({id_to_title[c] for c in calls[nid]} - {title})
        body.append("## → Calls")
        body += ([f"- [[{t}]]" for t in call_titles]
                 if call_titles else ["_(leaf — calls nothing in this graph)_"])
        body.append("")

        caller_titles = sorted({id_to_title[c] for c in called_by[nid]} - {title})
        body.append("## ← Called by")
        body += ([f"- [[{t}]]" for t in caller_titles]
                 if caller_titles else ["_(entry point — nothing in this graph calls it)_"])
        body.append("")

        safe = title.replace("/", "_")
        (out_dir / f"{safe}.md").write_text("\n".join(body))

    print(f"  {out_dir.relative_to(ROOT)}/  →  {len(nodes)} notes, {len(edges)} edges")


def main() -> None:
    rich = load_rich_descriptions()
    print(f"Reusing {len(rich)} rich descriptions. Generating graphs…\n")

    print("[1/3] comprehensive (all files):")
    write_graph(all_files(), GRAPHS / "functions", prefix="", rich=rich)

    print("[2/3] inner loop only:")
    write_graph(INNER_FILES, GRAPHS / "inner_loop", prefix="IN-", rich=rich)

    print("[3/3] inner + outer loop:")
    write_graph(INNER_OUTER_FILES, GRAPHS / "inner_outer", prefix="IO-", rich=rich)

    print("\nDone. In Obsidian press Ctrl+G and filter by path:")
    print("  path:graphs/inner_loop     (inner only)")
    print("  path:graphs/inner_outer    (inner + outer)")
    print("  path:graphs/functions      (everything)")


if __name__ == "__main__":
    main()
