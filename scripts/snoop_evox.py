#!/usr/bin/env python3
"""Line-by-line variable tracing of core EvoX functions using snoop.

Unlike viztracer (which shows the call timeline), snoop prints every line
of a chosen function as it executes, along with each variable's value the
moment it changes. Best for understanding the *logic* inside a function.

Usage:
    python scripts/snoop_evox.py --iters 5
    python scripts/snoop_evox.py --iters 5 --functions should_evolve,record_step
    python scripts/snoop_evox.py --iters 5 --depth 2     # follow nested calls deeper

Output:
    traces/snoop_evox.log   — the full line-by-line trace (also echoed to console)

Available functions to snoop (--functions, comma-separated; default = all):
    should_evolve   CoEvolutionController._should_evolve_search   (stagnation counter logic)
    assign_score    CoEvolutionController._assign_search_score     (search-strategy scoring)
    record_step     LogWindowScorer.record_step                    (score-window append)
    compute_metrics LogWindowScorer.compute_metrics                (the J_t score formula)
"""

import argparse
import asyncio
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

TRACES_DIR = PROJECT_ROOT / "traces"
TRACES_DIR.mkdir(exist_ok=True)

# short-name → (import path, class name, method name)
TARGETS = {
    "should_evolve": (
        "skydiscover.search.evox.controller",
        "CoEvolutionController",
        "_should_evolve_search",
    ),
    "assign_score": (
        "skydiscover.search.evox.controller",
        "CoEvolutionController",
        "_assign_search_score",
    ),
    "record_step": (
        "skydiscover.search.evox.utils.search_scorer",
        "LogWindowScorer",
        "record_step",
    ),
    "compute_metrics": (
        "skydiscover.search.evox.utils.search_scorer",
        "LogWindowScorer",
        "compute_metrics",
    ),
}


def _install_snoop(function_keys: list[str], depth: int, log_path: Path) -> "object":
    """Configure snoop output and decorate the chosen functions."""
    import importlib
    import snoop

    # Tee output to both the log file and the console.
    class _Tee:
        def __init__(self, *streams):
            self.streams = streams

        def write(self, data):
            for s in self.streams:
                s.write(data)

        def flush(self):
            for s in self.streams:
                s.flush()

    log_file = open(log_path, "w")
    tee = _Tee(log_file, sys.stderr)

    # color=False because we're writing to a file; columns adds a wall-clock column.
    snoop.install(out=tee, color=False, columns=["time"])

    for key in function_keys:
        if key not in TARGETS:
            print(f"  ! unknown function '{key}', skipping (valid: {', '.join(TARGETS)})")
            continue
        mod_path, cls_name, method_name = TARGETS[key]
        module = importlib.import_module(mod_path)
        cls = getattr(module, cls_name)
        original = getattr(cls, method_name)
        setattr(cls, method_name, snoop(depth=depth)(original))
        print(f"  ✓ snooping {cls_name}.{method_name}  (depth={depth})")

    return log_file


async def _run(iters: int, model: str, output_dir: str) -> None:
    """Run the same EvoX configuration as trace_evox.py / probe_run.py."""
    from skydiscover.config import load_config, EvoxDatabaseConfig
    from skydiscover.runner import Runner
    import yaml

    EVOX = PROJECT_ROOT / "skydiscover/search/evox/config/search.yaml"
    EVAL = PROJECT_ROOT / "benchmarks/math/circle_packing/evaluator.py"
    INIT = PROJECT_ROOT / "benchmarks/math/circle_packing/initial_program.py"
    CPCFG = PROJECT_ROOT / "benchmarks/math/circle_packing/config.yaml"

    config = load_config(str(EVOX))
    config.search.type = "evox"
    config.search.database = EvoxDatabaseConfig()
    config.max_iterations = iters
    config.checkpoint_interval = iters
    config.monitor.enabled = False
    config.llm.models[0].name = model

    with open(CPCFG) as f:
        cp = yaml.safe_load(f)
    config.context_builder.system_message = cp.get("prompt", {}).get("system_message", "")
    config.context_builder.template = "evox"

    runner = Runner(
        evaluation_file=str(EVAL),
        initial_program_path=str(INIT),
        config=config,
        output_dir=output_dir,
    )
    await runner.run(iterations=iters)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--iters", type=int, default=5)
    ap.add_argument("--model", default="qwen2.5-coder:14b")
    ap.add_argument("--output-dir", default="outputs/snoop_run")
    ap.add_argument(
        "--functions",
        default=",".join(TARGETS),
        help="Comma-separated functions to snoop (default: all). "
        f"Choices: {', '.join(TARGETS)}",
    )
    ap.add_argument(
        "--depth",
        type=int,
        default=1,
        help="How many levels of nested calls to follow (1 = just the function itself)",
    )
    ap.add_argument("--out", default=str(TRACES_DIR / "snoop_evox.log"))
    args = ap.parse_args()

    keys = [k.strip() for k in args.functions.split(",") if k.strip()]
    log_path = Path(args.out)

    print(f"▶ snoop trace of EvoX  ({args.iters} iterations)")
    print(f"   model = {args.model}")
    print(f"   log   → {log_path}")
    print()
    log_file = _install_snoop(keys, args.depth, log_path)
    print()

    try:
        asyncio.run(_run(args.iters, args.model, args.output_dir))
    finally:
        log_file.flush()
        log_file.close()

    print()
    print(f"✓ snoop trace written to {log_path}")
    print(f"   open it with:  less {log_path}")
    print()
    print("   Each '....' line shows a variable's value the moment it changed.")
    print("   '>>> Call' marks entry, '<<< Return' marks exit.")


if __name__ == "__main__":
    main()
