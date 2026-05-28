#!/usr/bin/env python3
"""Color a viztracer trace by subsystem/layer.

viztracer colors slices by a hash of the function name (arbitrary). This
post-processor instead colors each slice by which file/layer it belongs to —
so all inner-loop calls share one color, all LLM calls another, etc., matching
the Obsidian graph scheme as closely as the viewer's fixed palette allows.

It works by setting each event's `cname` field to one of the Catapult trace
viewer's reserved color names (the bundled vizviewer honors these).

Run standalone:
    python scripts/color_trace.py traces/evox_trace.json

Or it's called automatically at the end of scripts/trace_evox.py.
"""

import json
import re
import sys
from pathlib import Path

# file-path fragment → layer  (first match wins; most specific first)
LAYER_BY_PATH = [
    ("search/evox/controller.py", "outer-loop"),
    ("search/evox/utils/search_scorer.py", "evox"),
    ("search/evox", "evox"),
    ("search/default_discovery_controller.py", "inner-loop"),
    ("search/base_database.py", "database"),
    ("context_builder", "context-builder"),
    ("evaluation", "evaluation"),
    ("llm/langfuse_tracer.py", "observability"),
    ("llm/", "llm"),
    ("config", "config"),
    ("utils", "utils"),
    ("runner.py", "runner"),
    ("search/", "search"),
]

# layer → Catapult reserved color name (these render as distinct colors).
LAYER_CNAME = {
    "inner-loop":      "good",                   # green
    "outer-loop":      "terrible",               # red
    "evox":            "yellow",                 # yellow
    "llm":             "thread_state_iowait",    # orange (LLM call == IO wait — fitting)
    "database":        "detailed_memory_dump",   # magenta
    "context-builder": "rail_response",          # blue
    "evaluation":      "background_memory_dump",  # teal
    "observability":   "olive",                  # olive
    "runner":          "light_memory_dump",      # dark blue
    "config":          "thread_state_unknown",   # tan
    "utils":           "grey",                   # light grey
    "search":          "generic_work",           # grey
    "other":           "generic_work",           # grey
}

# human-readable color for the printed legend
CNAME_HUMAN = {
    "good": "green", "terrible": "red", "yellow": "yellow",
    "thread_state_iowait": "orange", "detailed_memory_dump": "magenta",
    "rail_response": "blue", "background_memory_dump": "teal",
    "olive": "olive", "light_memory_dump": "dark blue",
    "thread_state_unknown": "tan", "grey": "grey", "generic_work": "grey",
}

_PATH_RE = re.compile(r"\(([^()]*\.py):\d+\)")


def layer_for(name: str) -> str:
    m = _PATH_RE.search(name or "")
    if not m:
        return "other"
    path = m.group(1)
    for frag, layer in LAYER_BY_PATH:
        if frag in path:
            return layer
    return "other"


def colorize(in_path: Path, out_path: Path) -> Path:
    data = json.loads(in_path.read_text())
    events = data.get("traceEvents", [])
    counts: dict[str, int] = {}
    for e in events:
        # Color only function-call slices (complete 'X' or begin 'B').
        if e.get("ph") not in ("X", "B"):
            continue
        layer = layer_for(e.get("name", ""))
        cname = LAYER_CNAME.get(layer, "generic_work")
        e["cname"] = cname
        counts[layer] = counts.get(layer, 0) + 1

    out_path.write_text(json.dumps(data))
    print(f"Colored {sum(counts.values())} slices → {out_path}")
    print("Legend (layer → color):")
    for layer in sorted(counts, key=lambda l: -counts[l]):
        cname = LAYER_CNAME.get(layer, "generic_work")
        print(f"  {CNAME_HUMAN.get(cname, cname):<10} {layer:<16} ({counts[layer]} slices)")
    return out_path


def main() -> None:
    in_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("traces/evox_trace.json")
    out_path = (Path(sys.argv[2]) if len(sys.argv) > 2
                else in_path.with_name(in_path.stem + "_colored.json"))
    if not in_path.exists():
        print(f"trace not found: {in_path}")
        sys.exit(1)
    colorize(in_path, out_path)
    print(f"\nView it:\n    vizviewer {out_path}")


if __name__ == "__main__":
    main()
