#!/usr/bin/env python3
"""Write per-layer color groups into Obsidian's graph config (.obsidian/graph.json).

Each layer tag (#inner-loop, #outer-loop, #llm, …) gets a distinct color so the
graph view is colour-coded by subsystem. Preserves all other graph settings.

Run:
    python scripts/gen_graph_colors.py

Then in Obsidian: close and reopen the Graph View tab (or press Cmd+R to reload)
so it picks up the new colors.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRAPH_JSON = ROOT / ".obsidian" / "graph.json"

# layer tag → hex color. High-contrast, visually distinct palette.
TAG_COLORS = {
    "outer-loop":      "#e6194B",  # red
    "inner-loop":      "#3cb44b",  # green
    "evox":            "#f58231",  # orange
    "llm":             "#4363d8",  # blue
    "database":        "#911eb4",  # purple
    "context-builder": "#42d4f4",  # cyan
    "evaluation":      "#ffe119",  # yellow
    "observability":   "#f032e6",  # magenta
    "runner":          "#000075",  # navy
    "utils":           "#9A6324",  # brown
    "config":          "#808000",  # olive
    "search":          "#469990",  # teal
    "search-core":     "#000000",  # black
    "search-utils":    "#aaffc3",  # mint
    "adaevolve":       "#bfef45",  # lime
    "beam-search":     "#fabed4",  # pink
    "best-of-n":       "#ffd8b1",  # apricot
    "topk":            "#dcbeff",  # lavender
    "gepa":            "#800000",  # maroon
    "openevolve":      "#fffac8",  # beige
    "claude-code":     "#a9a9a9",  # grey
    "monitor":         "#00b4d8",  # sky
    "external":        "#7f7f7f",  # mid-grey
    "extras":          "#c0c0c0",  # light grey
    "cli":             "#2f4f4f",  # dark slate
    "api":             "#ff7f0e",  # amber
}


def hex_to_rgb_int(h: str) -> int:
    return int(h.lstrip("#"), 16)


def main() -> None:
    if GRAPH_JSON.exists():
        cfg = json.loads(GRAPH_JSON.read_text())
    else:
        cfg = {}

    cfg["colorGroups"] = [
        {"query": f"tag:#{tag}", "color": {"a": 1, "rgb": hex_to_rgb_int(hexcol)}}
        for tag, hexcol in TAG_COLORS.items()
    ]
    cfg["collapse-color-groups"] = False  # show the groups expanded
    cfg.setdefault("showTags", True)

    GRAPH_JSON.parent.mkdir(parents=True, exist_ok=True)
    GRAPH_JSON.write_text(json.dumps(cfg, indent=2))

    print(f"Wrote {len(TAG_COLORS)} color groups to {GRAPH_JSON.relative_to(ROOT)}")
    print("In Obsidian: close + reopen the Graph View tab (or Cmd+R) to load colors.")
    for tag, hexcol in TAG_COLORS.items():
        print(f"  {hexcol}  #{tag}")


if __name__ == "__main__":
    main()
