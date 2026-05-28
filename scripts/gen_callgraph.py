#!/usr/bin/env python3
"""Generate a filtered call graph of the EvoX runtime path.

Usage:
    python scripts/gen_callgraph.py

Outputs:
    graphs/evox_callgraph.dot   — Graphviz DOT source
    graphs/evox_callgraph.svg   — SVG (embed in Obsidian with ![[evox_callgraph.svg]])
    graphs/evox_callgraph.png   — PNG fallback

Requirements:
    pip install pyan3
    brew install graphviz   # (or: conda install graphviz)
"""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRAPHS = ROOT / "graphs"
GRAPHS.mkdir(exist_ok=True)

TARGET_FILES = [
    "skydiscover/runner.py",
    "skydiscover/search/default_discovery_controller.py",
    "skydiscover/search/evox/controller.py",
    "skydiscover/search/evox/utils/search_scorer.py",
    "skydiscover/search/evox/utils/variation_operator_generator.py",
    "skydiscover/search/base_database.py",
    "skydiscover/llm/llm_pool.py",
    "skydiscover/llm/openai.py",
    "skydiscover/llm/langfuse_tracer.py",
]

# Short names (first part of pyan3 label, before \n) to include
KEEP_NAMES = {
    "Runner", "run", "_add_initial_program", "_load_initial_program",
    "DiscoveryController", "_run_iteration", "_build_prompt", "_call_llm",
    "_parse_llm_response", "run_discovery",
    "CoEvolutionController", "_should_evolve_search", "_evolve_search",
    "_finalize_pending_search", "_assign_search_score",
    "_generate_and_validate_search_algorithm", "_switch_to_new_search_algorithm",
    "LogWindowScorer", "record_step", "reset_window", "get_score",
    "VariationOperatorGenerator", "_generate_variation_operators",
    "ProgramDatabase", "sample", "add",
    "LLMPool", "generate", "_sample_model",
    "OpenAILLM", "_generate_text", "_call_api",
    "LangFuseTracer", "log_generation",
}

# Color scheme per layer
LAYER_COLORS = {
    "runner": "#dae8fc",       # blue
    "controller": "#d5e8d4",   # green
    "evox": "#fff2cc",         # yellow
    "llm": "#f8cecc",          # red/pink
    "database": "#e1d5e7",     # purple
    "tracer": "#ffe6cc",       # orange
}

NODE_LAYER = {
    "Runner": "runner", "run": "runner",
    "_add_initial_program": "runner", "_load_initial_program": "runner",
    "DiscoveryController": "controller", "_run_iteration": "controller",
    "_build_prompt": "controller", "_call_llm": "controller",
    "_parse_llm_response": "controller", "run_discovery": "controller",
    "CoEvolutionController": "evox", "_should_evolve_search": "evox",
    "_evolve_search": "evox", "_finalize_pending_search": "evox",
    "_assign_search_score": "evox",
    "_generate_and_validate_search_algorithm": "evox",
    "_switch_to_new_search_algorithm": "evox",
    "LogWindowScorer": "evox", "record_step": "evox",
    "reset_window": "evox", "get_score": "evox",
    "VariationOperatorGenerator": "evox", "_generate_variation_operators": "evox",
    "ProgramDatabase": "database", "sample": "database", "add": "database",
    "LLMPool": "llm", "generate": "llm", "_sample_model": "llm",
    "OpenAILLM": "llm", "_generate_text": "llm", "_call_api": "llm",
    "LangFuseTracer": "tracer", "log_generation": "tracer",
}


def run_pyan3(files: list[str]) -> str:
    cmd = [
        sys.executable, "-m", "pyan",
        "--dot",
        "--no-defines",
        "--no-grouped",
        "--annotated",
    ] + files
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    if result.returncode != 0:
        print("pyan3 stderr:", result.stderr[:2000])
        sys.exit(1)
    return result.stdout


def parse_and_filter(raw_dot: str) -> tuple[dict, list]:
    """Return (kept_nodes, kept_edges).

    kept_nodes: {node_id: short_name}
    kept_edges: list of (src_id, dst_id)
    """
    node_re = re.compile(
        r'^\s*"([^"]+)"\s*\[.*?label\s*=\s*"([^"]+)"', re.MULTILINE
    )
    edge_re = re.compile(
        r'^\s*"([^"]+)"\s*->\s*"([^"]+)"', re.MULTILINE
    )

    kept_nodes: dict[str, str] = {}
    for m in node_re.finditer(raw_dot):
        node_id = m.group(1)
        label = m.group(2)
        # label is like "ShortName\n(/path:line)" — split on literal \n
        short_name = label.split("\\n")[0]
        if short_name in KEEP_NAMES:
            kept_nodes[node_id] = short_name

    kept_edges: list[tuple[str, str]] = []
    for m in edge_re.finditer(raw_dot):
        src, dst = m.group(1), m.group(2)
        if src in kept_nodes and dst in kept_nodes:
            kept_edges.append((src, dst))

    return kept_nodes, kept_edges


def build_dot(kept_nodes: dict, kept_edges: list) -> str:
    lines = [
        "digraph EvoX {",
        '    graph [rankdir=TB, ranksep=0.8, nodesep=0.5, fontname="Helvetica"];',
        '    node [shape=box, style="filled,rounded", fontname="Helvetica", fontsize=11];',
        '    edge [color="#555555", fontsize=9];',
        "",
    ]

    # Emit nodes grouped by layer
    emitted: set[str] = set()
    layer_groups: dict[str, list] = {}
    for node_id, name in kept_nodes.items():
        layer = NODE_LAYER.get(name, "controller")
        layer_groups.setdefault(layer, []).append((node_id, name))

    layer_order = ["runner", "controller", "evox", "database", "llm", "tracer"]
    layer_labels = {
        "runner": "Runner",
        "controller": "Discovery Controller (inner loop)",
        "evox": "EvoX / Co-Evolution (outer loop)",
        "database": "Program Database",
        "llm": "LLM Layer",
        "tracer": "LangFuse Observability",
    }

    for layer in layer_order:
        nodes = layer_groups.get(layer, [])
        if not nodes:
            continue
        color = LAYER_COLORS[layer]
        lines.append(f'    subgraph "cluster_{layer}" {{')
        lines.append(f'        label="{layer_labels[layer]}";')
        lines.append(f'        style="filled,rounded";')
        lines.append(f'        fillcolor="{color}88";')
        lines.append(f'        color="{color}";')
        for node_id, name in nodes:
            lines.append(
                f'        "{node_id}" [label="{name}", fillcolor="{color}"];'
            )
            emitted.add(node_id)
        lines.append("    }")
        lines.append("")

    # Emit edges
    for src, dst in kept_edges:
        lines.append(f'    "{src}" -> "{dst}";')

    lines.append("}")
    return "\n".join(lines)


def render(dot_path: Path) -> None:
    for fmt in ("svg", "png"):
        out = dot_path.with_suffix(f".{fmt}")
        result = subprocess.run(
            ["dot", f"-T{fmt}", str(dot_path), "-o", str(out)],
            capture_output=True, text=True,
        )
        if result.returncode == 0:
            print(f"  Written: {out.relative_to(ROOT)}")
        else:
            print(f"  graphviz error for {fmt}: {result.stderr[:400]}")


def main() -> None:
    abs_files = [str(ROOT / f) for f in TARGET_FILES if (ROOT / f).exists()]
    missing = [f for f in TARGET_FILES if not (ROOT / f).exists()]
    if missing:
        print("Warning: files not found:", missing)

    print(f"Running pyan3 on {len(abs_files)} files…")
    raw = run_pyan3(abs_files)

    print("Parsing + filtering to EvoX runtime nodes…")
    kept_nodes, kept_edges = parse_and_filter(raw)
    print(f"  Kept {len(kept_nodes)} nodes, {len(kept_edges)} edges")

    dot = build_dot(kept_nodes, kept_edges)
    dot_path = GRAPHS / "evox_callgraph.dot"
    dot_path.write_text(dot)
    print(f"  Written: {dot_path.relative_to(ROOT)}")

    print("Rendering with graphviz…")
    render(dot_path)
    print("Done.")


if __name__ == "__main__":
    main()
