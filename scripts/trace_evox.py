#!/usr/bin/env python3
"""Run the EvoX co-evolution loop under viztracer.

Records every function call, argument, and return value, then writes
a single trace file you can open in the browser with vizviewer.

Usage:
    python scripts/trace_evox.py --iters 5
    python scripts/trace_evox.py --iters 10 --model gemma3:12b

After it finishes:
    vizviewer traces/evox_trace.json

Tips:
    • Start with --iters 3 to keep the trace file small (a few MB).
    • Each LLM call shows up as a long horizontal bar in the timeline.
    • Click any bar to see its arguments and return value in the side panel.
    • Use the time-axis to zoom into a specific iteration.
"""

import argparse
import asyncio
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

TRACES_DIR = PROJECT_ROOT / "traces"
TRACES_DIR.mkdir(exist_ok=True)


def _install_state_tracking() -> None:
    """Monkeypatch EvoX controller methods to plot key state on the timeline.

    Uses the global viztracer instance:
      • log_var(name, value)  → a line graph track (value over time)
      • log_instant(name)     → a vertical marker at a moment in time

    Tracks plotted:
      evox/best_score          best solution score so far
      evox/stagnant_count      stagnation counter (resets to 0 on improvement)
      evox/db_size             number of programs in the solution database
      evox/num_evolutions      how many times the outer loop has run
      evox/best_search_score   best score any search strategy achieved

    Markers dropped:
      ⚡ OUTER LOOP        when stagnation triggers search evolution
      🔀 STRATEGY SWITCHED when a new search algorithm replaces the old one
      ⭐ NEW BEST          when a new best solution is found
    """
    from viztracer import get_tracer
    from skydiscover.search.evox.controller import CoEvolutionController
    from skydiscover.search.default_discovery_controller import DiscoveryController

    def _score_of(prog) -> float:
        if prog is None:
            return 0.0
        m = getattr(prog, "metrics", {}) or {}
        s = m.get("combined_score")
        if s is None:
            s = m.get("score")
        return float(s) if isinstance(s, (int, float)) else 0.0

    # ── inner loop: after each iteration, plot db size + best score ──────────
    _orig_iter = DiscoveryController._run_iteration

    async def _traced_iter(self, iteration, retry_times=1):
        prev_best = _score_of(self.database.get_best_program())
        result = await _orig_iter(self, iteration, retry_times=retry_times)
        t = get_tracer()
        if t is not None:
            best = _score_of(self.database.get_best_program())
            t.log_var("evox/best_score", best)
            t.log_var("evox/db_size", len(self.database.programs))
            if best > prev_best + 1e-9:
                t.log_instant(f"⭐ NEW BEST {best:.4f} @ iter {iteration}", scope="g")
        return result

    DiscoveryController._run_iteration = _traced_iter

    # ── stagnation gate: plot stagnant_count, mark outer-loop trigger ────────
    _orig_should = CoEvolutionController._should_evolve_search

    def _traced_should(self):
        result = _orig_should(self)
        t = get_tracer()
        if t is not None:
            t.log_var("evox/stagnant_count", self._stagnant_count)
            t.log_var("evox/best_search_score", self._best_search_score or 0.0)
            if result:
                t.log_instant("⚡ OUTER LOOP triggered (stagnation)", scope="g")
        return result

    CoEvolutionController._should_evolve_search = _traced_should

    # ── strategy switch: mark + plot evolution count ─────────────────────────
    _orig_switch = CoEvolutionController._switch_to_new_search_algorithm

    def _traced_switch(self, result):
        success = _orig_switch(self, result)
        t = get_tracer()
        if t is not None:
            t.log_var("evox/num_evolutions", self._num_search_evolutions)
            if success:
                t.log_instant("🔀 STRATEGY SWITCHED (new search algorithm)", scope="g")
        return success

    CoEvolutionController._switch_to_new_search_algorithm = _traced_switch


async def _run(iters: int, model: str, output_dir: str) -> None:
    """Run the same EvoX configuration that probe_run.py uses."""
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
    ap.add_argument("--output-dir", default="outputs/trace_run")
    ap.add_argument(
        "--out",
        default=str(TRACES_DIR / "evox_trace.json"),
        help="Trace output file (.json)",
    )
    ap.add_argument(
        "--log-args",
        action="store_true",
        help="Also capture function args + return values (much slower — LLM prompts are huge)",
    )
    ap.add_argument(
        "--min-duration",
        type=float,
        default=50.0,
        help="Skip calls faster than this many microseconds. Default 50µs cuts asyncio noise.",
    )
    ap.add_argument(
        "--no-track-state",
        action="store_true",
        help="Disable EvoX state graphs (best_score, stagnant_count, db_size, …) on the timeline",
    )
    args = ap.parse_args()

    from viztracer import VizTracer

    # Exclude noisy library internals so the trace stays focused on our code.
    # We don't use include_files because absolute paths with spaces (e.g. "Yusu Wang")
    # can confuse the prefix matcher — exclude_files is more reliable.
    exclude_patterns = [
        "site-packages/openai",
        "site-packages/httpx",
        "site-packages/httpcore",
        "site-packages/anyio",
        "site-packages/numpy",
        "site-packages/yaml",
        "site-packages/urllib3",
        "site-packages/certifi",
        "site-packages/h11",
        "site-packages/sniffio",
        "site-packages/distro",
        "site-packages/pydantic",
        "site-packages/typing_extensions",
        "asyncio/base_events",
        "asyncio/events",
        "asyncio/futures",
        "asyncio/tasks",
        "asyncio/selector_events",
        "concurrent/futures",
        "logging/__init__",
        "json/decoder",
        "json/encoder",
    ]

    # Note: log_func_args is OFF by default — capturing every arg string makes
    # viztracer 50–100x slower because LLM prompts are huge strings sent every call.
    # Use --log-args to opt in for a deep-dive trace (much slower).
    tracer = VizTracer(
        output_file=args.out,
        exclude_files=exclude_patterns,
        log_func_args=args.log_args,
        log_func_retval=args.log_args,
        log_print=True,
        # Drop sub-microsecond noise calls (asyncio internal callbacks etc).
        min_duration=args.min_duration,
        max_stack_depth=80,
        file_info=True,
        register_global=True,  # so log_var/log_instant work inside the patches
        verbose=1,
    )

    # Install EvoX state graphs (best_score, stagnant_count, db_size, markers).
    if not args.no_track_state:
        _install_state_tracking()

    print(f"▶ Running {args.iters} iterations under viztracer …")
    print(f"   model = {args.model}")
    print(f"   trace → {args.out}")
    print(f"   state graphs: {'OFF' if args.no_track_state else 'ON'}")
    print()

    tracer.start()
    try:
        asyncio.run(_run(args.iters, args.model, args.output_dir))
    finally:
        tracer.stop()
        tracer.save()

    # Color the trace by subsystem (inner-loop=green, outer-loop=red, llm=orange, …).
    colored = Path(args.out).with_name(Path(args.out).stem + "_colored.json")
    try:
        from color_trace import colorize
        print()
        colorize(Path(args.out), colored)
        view_target = colored
    except Exception as exc:
        print(f"(color step skipped: {exc})")
        view_target = Path(args.out)

    print()
    print(f"✓ Trace written to {args.out}")
    print()
    print(f"View the COLOR-CODED trace with:")
    print(f"    vizviewer {view_target}")
    print()
    print(f"(slices are colored by subsystem — see the legend above. Drag to pan,")
    print(f" scroll to zoom, click any bar for its source.)")


if __name__ == "__main__":
    main()
