"""
probe_run.py  v5 — Complete state-change trace (extended)

Traces EVERY function call and variable update across ALL files per iteration.

Per-iteration tree (10 steps):
  1. sample()                   — which parent/context selected, label key
  2. _build_prompt() wrapper    — db.get_statistics() call, context dict assembly
  3. EvoxContextBuilder.build_prompt() — prompt strings constructed
  4. _call_llm()                — model, timing, response preview
  5. _parse_llm_response()      — code extraction mode + result
  6. evaluate_program()         — score, validity, timing
  7. _create_child_program()    — Program dataclass fields set
  8. database.add() + _update_best_program() — db mutations
  9. log_prompt()               — prompt logging step
 10. LogWindowScorer.record_step() — window updated
 11. _should_evolve_search()    — stagnation check + tree flush

Search evolution block (when triggered):
  A. _reset_search_window()     — window boundary reset
  B. _initialize_first_search_program() OR _generate_and_validate_search_algorithm()
  C. _build_search_stats()      — context passed to search LLM
  D. _finalize_pending_search() + _assign_search_score() — strategy scored
  E. _switch_to_new_search_algorithm() — exec() + db swap

Usage:
    python probe_run.py --iters 20
"""

import argparse
import asyncio
import logging
import os
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

# ─── Logging ──────────────────────────────────────────────────────────────────
PROBE_LOG = PROJECT_ROOT / "probe_run.log"
_pl = logging.getLogger("PROBE")
_pl.setLevel(logging.DEBUG)
_pl.propagate = False
_fmt = logging.Formatter("%(asctime)s  %(message)s", datefmt="%H:%M:%S")
for _h in [logging.StreamHandler(sys.stdout),
           logging.FileHandler(PROBE_LOG, mode="w")]:
    _h.setFormatter(_fmt)
    _pl.addHandler(_h)

def p(msg=""): _pl.info(msg)


# ─── State ────────────────────────────────────────────────────────────────────
class _State:
    iter_num           = 0
    events             = []       # (tag, file, msg) list for current iteration
    search_evo_num     = 0
    in_search_evo      = False    # True while inside _evolve_search
    active_search_code = ""       # current search algorithm source

_S = _State()

def evt(tag, file, msg):
    _S.events.append((tag, file, msg))

def _f(v, d=4):   return f"{v:.{d}f}" if isinstance(v, (int, float)) else str(v)
def _score(prog):
    if prog is None: return "None"
    m = getattr(prog, "metrics", {}) or {}
    s = m.get("combined_score") or m.get("score")
    return _f(s) if isinstance(s, (int, float)) else "?"
def _snip(t, n=200):
    if not t: return "(empty)"
    t = t.replace("\n", "↵ ")
    return t[:n] + (f"  …[{len(t)-n}]" if len(t) > n else "")


# ─── Tree/snapshot printers ───────────────────────────────────────────────────
def _print_tree(title, events, border="═"):
    p(); p(f"{border*70}"); p(f"  {title}"); p(f"{border*70}")
    for i, (tag, file, msg) in enumerate(events):
        last = (i == len(events) - 1)
        con  = "└─" if last else "├─"
        ind  = "     " if last else "  │  "
        p(f"  {con} [{tag}]")
        p(f"{ind}  file : {file}")
        for ln in msg.strip().splitlines():
            p(f"{ind}  {ln}")
    p()

def _print_iteration_tree():
    _print_tree(f"ITERATION {_S.iter_num}", _S.events)
    _S.events.clear()

def _print_search_evo_tree(events):
    _print_tree(f"SEARCH EVOLUTION #{_S.search_evo_num}  (outer loop triggered)",
                events, border="▓")

def _print_state_snapshot(ctrl):
    """Print full CoEvolutionController state after each iteration."""
    db     = ctrl.database
    sdb    = ctrl.search_controller.database
    scorer = ctrl.search_scorer

    best = db.get_best_program()
    best_id    = str(getattr(best, "id", "?"))[:8] if best else "None"
    best_score = _score(best)

    sbest = sdb.get_best_program()
    sbest_score = _score(sbest) if sbest else "None"
    sbest_id    = str(getattr(sbest, "id", "?"))[:8] if sbest else "None"

    pending = ctrl._pending_search_result
    pend_str = (f"SET  id={str((pending.child_program_dict or {}).get('id','?'))[:8]}"
                f"  (score pending until next strategy switch)"
                if pending else "None (no strategy waiting to be scored)")

    fallback_str = ("SET  (prev DB saved, can restore if new strategy crashes)"
                    if ctrl._fallback_database else "None")

    active_code = ctrl._active_search_algorithm_code or ""
    code_len = len(active_code)
    code_ver = (f"evolved_strategy  ({code_len} chars)"
                if active_code and active_code != ctrl._search_initial_code
                else f"initial_search_strategy  ({code_len} chars)")

    window_size  = scorer.get_window_size()
    start_score  = scorer.get_start_score()
    window_scores = [round(x, 4) for x in scorer._best_scores] if hasattr(scorer, "_best_scores") else "?"

    p(f"  {'─'*68}")
    p(f"  STATE SNAPSHOT  (all variables after iteration {_S.iter_num})")
    p(f"  {'─'*68}")
    p(f"")
    p(f"  SOLUTION DATABASE  (search/base_database.py → EvolvedProgramDatabase)")
    p(f"    programs dict     : {len(db.programs)} entries  "
      f"[{', '.join(str(k)[:6] for k in list(db.programs.keys())[-4:])}{'...' if len(db.programs)>4 else ''}]")
    p(f"    best_program_id   : {best_id}  score={best_score}")
    p(f"    DIVERGE_LABEL set : {'YES' if getattr(db,'DIVERGE_LABEL','') else 'NO'}"
      f"  ({len(getattr(db,'DIVERGE_LABEL',''))} chars)")
    p(f"    REFINE_LABEL set  : {'YES' if getattr(db,'REFINE_LABEL','') else 'NO'}"
      f"  ({len(getattr(db,'REFINE_LABEL',''))} chars)")
    p(f"")
    p(f"  STAGNATION TRACKING  (controller.py)")
    p(f"    _last_tracked_best_score : {_f(ctrl._last_tracked_best_score)}"
      f"  ← updated EVERY iteration in _should_evolve_search()")
    p(f"    _stagnant_count          : {ctrl._stagnant_count}"
      f"  ← 0 if improved, +1 if not, resets to 0 when trigger fires")
    p(f"    _switch_interval         : {ctrl._switch_interval}"
      f"  = max(1, int(max_iters × 0.10))")
    p(f"")
    p(f"  SEARCH EVOLUTION TRACKING  (controller.py)")
    p(f"    _num_search_evolutions   : {ctrl._num_search_evolutions}"
      f"  ← incremented when a strategy is FINALIZED (scored + added to search_db)")
    p(f"    _pending_search_result   : {pend_str}")
    p(f"    _best_search_score       : {_f(ctrl._best_search_score)}"
      f"  ← best score ANY search strategy achieved")
    p(f"    _fallback_database       : {fallback_str}")
    p(f"    _active_search_algorithm : {code_ver}")
    p(f"")
    p(f"  SCORE WINDOW  (search/evox/utils/search_scorer.py — LogWindowScorer)")
    p(f"    _start_score : {_f(start_score)}"
      f"  ← score at window open (resets on each strategy switch)")
    p(f"    _best_scores : {window_scores}  ({window_size} steps)")
    p(f"    formula when scored: combined = (end−start) × log_wt / √horizon")
    p(f"")
    p(f"  SEARCH STRATEGY DB  (search_controller.database — inner DB)")
    p(f"    programs : {len(sdb.programs)} strategies stored")
    for sp in list(sdb.programs.values())[-3:]:
        sc = (sp.metrics or {}).get("combined_score")
        p(f"      id={str(sp.id)[:8]}  score={_f(sc)}")
    p(f"    best_strategy   : id={sbest_id}  score={sbest_score}")
    p(f"  {'─'*68}")
    p(f"")


# ─── Patches ─────────────────────────────────────────────────────────────────
def _install_patches():
    from skydiscover.search.evox.controller import CoEvolutionController
    from skydiscover.search.evox.utils.search_scorer import LogWindowScorer
    from skydiscover.search.default_discovery_controller import DiscoveryController
    from skydiscover.context_builder.evox.builder import EvoxContextBuilder
    from skydiscover.evaluation.evaluator import Evaluator
    from skydiscover.search.base_database import ProgramDatabase

    # ── 1. run_discovery header/footer ───────────────────────────────────────
    _orig_run = CoEvolutionController.run_discovery
    async def _patched_run(self, start_iteration, max_iterations, **kwargs):
        p(); p(f"{'━'*70}")
        p(f"  CoEvolutionController.run_discovery  START")
        p(f"  file: skydiscover/search/evox/controller.py")
        p(f"  start={start_iteration}  max={max_iterations}")
        si = max(1, int(max_iterations * 0.10))
        p(f"  switch_interval = max(1, int({max_iterations}×0.10)) = {si}")
        p(f"  meaning: search evolves after every {si} stagnant iteration(s)")
        p(f"{'━'*70}")
        _S.iter_num = start_iteration
        result = await _orig_run(self, start_iteration, max_iterations, **kwargs)
        if _S.events: _print_iteration_tree()
        p(f"{'━'*70}")
        p(f"  run_discovery RETURNED  type={type(result).__name__}")
        if result and hasattr(result, "metrics") and result.metrics:
            p(f"  best: id={str(getattr(result,'id','?'))[:8]}  score={_f(result.metrics.get('combined_score'))}")
        p(f"  ✓ Returns best Program object → Runner.run() saves checkpoint")
        p(f"{'━'*70}")
        return result
    CoEvolutionController.run_discovery = _patched_run

    # ── 2. _generate_variation_operators ─────────────────────────────────────
    _orig_gen = CoEvolutionController._generate_variation_operators
    async def _patched_gen(self):
        p(); p("┌─ _generate_variation_operators()")
        p("│  file: skydiscover/search/evox/controller.py")
        p("│        → skydiscover/search/evox/utils/variation_operator_generator.py")
        p(f"│  guide model: {[m.name for m in self.search_controller.guide_llms.models_cfg]}")
        p("│  calling guide LLM once at startup to write DIVERGE + REFINE label text …")
        t0 = time.time()
        await _orig_gen(self)
        p(f"│  done in {time.time()-t0:.1f}s")
        p(f"│")
        p(f"│  DIVERGE_LABEL ({len(self._diverge_label)} chars):")
        for ln in self._diverge_label[:600].splitlines(): p(f"│    {ln}")
        if len(self._diverge_label) > 600: p(f"│    ... [{len(self._diverge_label)-600} more chars]")
        p(f"│")
        p(f"│  REFINE_LABEL ({len(self._refine_label)} chars):")
        for ln in self._refine_label[:400].splitlines(): p(f"│    {ln}")
        if len(self._refine_label) > 400: p(f"│    ... [{len(self._refine_label)-400} more chars]")
        p(f"│")
        p(f"│  WHERE LABELS END UP:")
        p(f"│    controller._diverge_label / _refine_label = full text above")
        p(f"│    db.DIVERGE_LABEL / db.REFINE_LABEL = same text, assigned to database")
        p(f"│    They appear in solution prompts ONLY IF sample() returns")
        p(f"│      parent_dict = {{DIVERGE_LABEL: parent}}  ← key = full label text")
        p(f"│    Initial strategy returns {{'' : parent}} → label NEVER shows in prompts")
        p("└─ done"); p()
    CoEvolutionController._generate_variation_operators = _patched_gen

    # ── 3. _run_iteration: clear events ──────────────────────────────────────
    _orig_iter = DiscoveryController._run_iteration
    async def _patched_iter(self, iteration, retry_times=1):
        _S.iter_num = iteration
        _S.events.clear()
        result = await _orig_iter(self, iteration, retry_times=retry_times)
        return result
    DiscoveryController._run_iteration = _patched_iter

    # ── 4. sample() per-instance probe ───────────────────────────────────────
    def _install_sample_probe(db, strategy_name="initial_search_strategy"):
        _orig = db.sample
        def _wrapped(*args, **kwargs):
            parent_dict, ctx_dict = _orig(*args, **kwargs)
            parent    = next(iter(parent_dict.values()), None)
            label_key = next(iter(parent_dict.keys()), "")
            ctx_all   = [x for lst in ctx_dict.values() for x in lst]
            diverge   = getattr(db, "DIVERGE_LABEL", "")
            refine    = getattr(db, "REFINE_LABEL",  "")

            if   label_key == diverge and diverge: lm = "DIVERGE ← LLM told to use fundamentally different approach"
            elif label_key == refine  and refine:  lm = "REFINE  ← LLM told to refine/exploit current approach"
            elif label_key == "":                  lm = '(empty) ← NO label block injected into this prompt'
            else:                                  lm = f'"{label_key[:50]}"'

            code = _S.active_search_code
            uses_d = "DIVERGE_LABEL" in code if code else False
            uses_r = "REFINE_LABEL"  in code if code else False
            if uses_d and uses_r:
                lu = "code references both labels → COULD return them as parent_dict keys"
            elif code:
                lu = "code does NOT use DIVERGE_LABEL/REFINE_LABEL → will always return empty key"
            else:
                lu = "(initial strategy hardcoded → always returns empty key)"

            msg = (
                f"DB class    : {type(db).__name__}  strategy_file: {strategy_name}\n"
                f"db.programs : {len(db.programs)} entries total\n"
                f"parent      : id={str(getattr(parent,'id','?'))[:8]}  score={_score(parent)}"
                f"  gen={getattr(parent,'generation',0)}  iter={getattr(parent,'iteration_found','?')}\n"
                f"ctx programs: {len(ctx_all)} provided  "
                f"scores=[{', '.join(_score(x) for x in ctx_all)}]\n"
                f"\n"
                f"LABEL KEY returned by sample():\n"
                f"  {lm}\n"
                f"\n"
                f"db.DIVERGE_LABEL ({len(diverge)} chars): {_snip(diverge, 70)}\n"
                f"db.REFINE_LABEL  ({len(refine)}  chars): {_snip(refine, 70)}\n"
                f"\n"
                f"Label usage in active search code:\n"
                f"  {lu}\n"
                f"\n"
                f"DESIGN CHECK: sample() returns (parent_dict, ctx_dict).\n"
                f"  parent_dict key → injected as label block in prompt (empty = no injection).\n"
                f"  ctx programs provide additional examples for the LLM to learn from."
            )
            if not _S.in_search_evo:
                evt("sample()", f"skydiscover/search/evox/database/{strategy_name}.py", msg)
            return parent_dict, ctx_dict
        db.sample = _wrapped
    _install_sample_probe._fn = _install_sample_probe

    # ── 5. DiscoveryController._build_prompt() wrapper ───────────────────────
    _orig_bpw = DiscoveryController._build_prompt
    def _patched_bpw(self, current_program, context_programs, failed_attempts):
        db_stats_cached = bool(self._prompt_context.get("db_stats"))
        num_progs = len(self.database.programs)
        label_key = (next(iter(current_program.keys()), "")
                     if isinstance(current_program, dict) else "")
        num_failed = len(failed_attempts or [])
        msg = (
            f"db.get_statistics()  : {'CACHED ← _prompt_context[db_stats] reused' if db_stats_cached else 'CALLED FRESH ← computes score distribution, execution trace'}\n"
            f"db size at call      : {num_progs} programs\n"
            f"label_key (from sample()): '{label_key[:60] if label_key else '(empty)'}'\n"
            f"failed_attempts fed  : {num_failed} (retry context for LLM)\n"
            f"\n"
            f"context dict assembled:\n"
            f"  program_metrics      ← parent's score/validity\n"
            f"  other_context_programs ← ctx programs from sample()\n"
            f"  previous_programs    ← from db_stats.previous_programs (recent history)\n"
            f"  db_stats             ← full score distribution summary\n"
            f"  errors               ← failed_attempts (if any, feeds back parse/eval errors)\n"
            f"\n"
            f"CALLS → EvoxContextBuilder.build_prompt()  (next event in tree)"
        )
        if not _S.in_search_evo:
            evt("_build_prompt() wrapper", "skydiscover/search/default_discovery_controller.py", msg)
        return _orig_bpw(self, current_program, context_programs, failed_attempts)
    DiscoveryController._build_prompt = _patched_bpw

    # ── 6. EvoxContextBuilder.build_prompt ───────────────────────────────────
    _orig_build = EvoxContextBuilder.build_prompt
    def _patched_build(self, current_program, context=None, **kwargs):
        result = _orig_build(self, current_program, context, **kwargs)
        sys_msg  = result.get("system", "")
        user_msg = result.get("user",   "")
        label_key = ""
        if isinstance(current_program, dict) and current_program:
            label_key = next(iter(current_program.keys()), "")
        if label_key:
            ln = f'label_key="{_snip(label_key, 60)}" → INJECTED before "# Current Solution"'
        else:
            ln = 'label_key="" → no DIVERGE/REFINE block added to prompt'
        msg = (
            f"template : search_evolution_user_message  (context_builder/evox/templates/)\n"
            f"label    : {ln}\n"
            f"system   : {len(sys_msg):,} chars   "
            f"preview: {_snip(sys_msg, 80)}\n"
            f"user     : {len(user_msg):,} chars\n"
            f"  first 200: {_snip(user_msg, 200)}\n"
            f"\n"
            f"WHAT GROWS user_msg over iterations:\n"
            f"  - parent program code (grows as programs get longer)\n"
            f"  - context programs code (up to 2 shown)\n"
            f"  - previous iteration scores + program history\n"
            f"  - failed attempt error messages (when retrying)\n"
            f"\n"
            f"DESIGN CHECK: EvoxContextBuilder correctly selected (not DefaultContextBuilder).\n"
            f"  Set via config.context_builder.template='evox' → _init_context_builder()."
        )
        if not _S.in_search_evo:
            evt("EvoxContextBuilder.build_prompt()", "skydiscover/context_builder/evox/builder.py", msg)
        return result
    EvoxContextBuilder.build_prompt = _patched_build

    # ── 7. _call_llm ─────────────────────────────────────────────────────────
    _orig_call = DiscoveryController._call_llm
    async def _patched_call(self, system_message, user_message, **kwargs):
        t0 = time.time()
        result = await _orig_call(self, system_message, user_message, **kwargs)
        elapsed = time.time() - t0
        text = getattr(result, "text", "") or ""
        mcfg = getattr(self.llms, "models_cfg", [])
        model = mcfg[0].name if mcfg and hasattr(mcfg[0], "name") else "?"
        msg = (
            f"model    : {model}  (via llm/openai.py → ollama compatible endpoint)\n"
            f"elapsed  : {elapsed:.1f}s\n"
            f"input    : system={len(system_message):,} chars  user={len(user_message):,} chars\n"
            f"output   : {len(text):,} chars\n"
            f"preview  : {_snip(text, 200)}\n"
            f"\n"
            f"DESIGN CHECK: _call_llm() correctly called.\n"
            f"  Routes through LLMPool → picks one model → calls openai-compatible API.\n"
            f"  No agentic_generator (agentic mode disabled in this config)."
        )
        if not _S.in_search_evo:
            evt("_call_llm()", "skydiscover/llm/llm_pool.py → llm/openai.py", msg)
        return result
    DiscoveryController._call_llm = _patched_call

    # ── 8. _parse_llm_response ────────────────────────────────────────────────
    _orig_parse = DiscoveryController._parse_llm_response
    def _patched_parse(self, llm_response, parent_solution, iteration, attempt, retry_times):
        child, summary, err = _orig_parse(self, llm_response, parent_solution, iteration, attempt, retry_times)
        mode = "diff-based" if self.config.diff_based_generation else "full-rewrite"
        if err:
            r = f"PARSE ERROR → {err}"
        else:
            r = (f"OK  extracted {len(child or ''):,} chars\n"
                 f"  changes: {_snip(summary or '', 80)}")
        msg = (
            f"mode     : {mode}  (config.diff_based_generation={self.config.diff_based_generation})\n"
            f"attempt  : {attempt}/{retry_times}\n"
            f"input    : {len(llm_response or ''):,} chars\n"
            f"result   : {r}\n"
            f"\n"
            f"DESIGN CHECK: full-rewrite mode correctly used.\n"
            f"  parse_full_rewrite() extracts code from ```python ... ``` block.\n"
            f"  If parsing fails → stored in failed_attempts → fed back to LLM on retry."
        )
        if not _S.in_search_evo:
            evt("_parse_llm_response()", "skydiscover/utils/code_utils.py", msg)
        return child, summary, err
    DiscoveryController._parse_llm_response = _patched_parse

    # ── 9. evaluate_program ───────────────────────────────────────────────────
    _orig_eval = Evaluator.evaluate_program
    async def _patched_eval(self, program_solution, program_id="", mode="train"):
        t0 = time.time()
        result = await _orig_eval(self, program_solution, program_id, mode)
        elapsed = time.time() - t0
        metrics  = getattr(result, "metrics", {}) or {}
        score    = metrics.get("combined_score")
        validity = metrics.get("validity", "?")
        err      = getattr(result, "error", None)
        r = (f"ERROR: {err}" if err else
             f"combined_score={_f(score)}  validity={validity}\n"
             f"  full metrics: {metrics}")
        msg = (
            f"program_id : {str(program_id)[:8]}\n"
            f"mode       : {mode}\n"
            f"eval_time  : {elapsed:.2f}s\n"
            f"result     : {r}\n"
            f"\n"
            f"DESIGN CHECK: evaluate_program() correctly called.\n"
            f"  Writes code to tempfile → subprocess runs it → reads .results file.\n"
            f"  Validity=0 means circles overlapped/out-of-bounds → invalid solution.\n"
            f"  If invalid: stored in failed_attempts → fed back to LLM on retry (up to 3x)."
        )
        if not _S.in_search_evo:
            evt("evaluate_program()", "skydiscover/evaluation/evaluator.py", msg)
        return result
    Evaluator.evaluate_program = _patched_eval

    # ── 10. _create_child_program ─────────────────────────────────────────────
    _orig_ccp = DiscoveryController._create_child_program
    def _patched_ccp(self, child_id, child_solution, parent, context_program_ids,
                     parent_info, context_info, child_metrics, iteration,
                     changes_summary, extra_metadata=None, artifacts=None):
        result = _orig_ccp(self, child_id, child_solution, parent, context_program_ids,
                           parent_info, context_info, child_metrics, iteration,
                           changes_summary, extra_metadata, artifacts)
        score = _f((child_metrics or {}).get("combined_score"))
        parent_score = _f((parent.metrics or {}).get("combined_score"))
        msg = (
            f"Program dataclass fields set:\n"
            f"  id               : {str(child_id)[:8]}  (uuid4)\n"
            f"  solution         : {len(child_solution or ''):,} chars  (full rewrite)\n"
            f"  language         : {self.config.language}\n"
            f"  iteration_found  : {iteration}\n"
            f"  parent_id        : {str(parent.id)[:8]}  (score was {parent_score})\n"
            f"  other_context_ids: {len(context_program_ids)} programs\n"
            f"  metrics          : combined_score={score}\n"
            f"  metadata.changes : '{changes_summary}'\n"
            f"  metadata.parent_metrics: {parent.metrics}\n"
            f"  artifacts        : {len(artifacts or {})} entries\n"
            f"\n"
            f"DESIGN: _create_child_program() bundles all fields into Program dataclass.\n"
            f"  Returned as SerializableResult.child_program_dict (via .to_dict()).\n"
            f"  _process_iteration_result() reconstructs Program from that dict on add()."
        )
        if not _S.in_search_evo:
            evt("_create_child_program()", "skydiscover/search/default_discovery_controller.py", msg)
        return result
    DiscoveryController._create_child_program = _patched_ccp

    # ── 11. database.add() + _update_best_program ─────────────────────────────
    _orig_proc = DiscoveryController._process_iteration_result
    def _patched_proc(self, result, iteration, checkpoint_callback=None, verbose=True):
        _orig_proc(self, result, iteration, checkpoint_callback, verbose)
        if result.error:
            evt("database.add()", "skydiscover/search/base_database.py",
                f"SKIPPED — iteration failed: {result.error}")
            return
        child   = result.child_program_dict or {}
        score   = (child.get("metrics") or {}).get("combined_score")
        best    = self.database.get_best_program()
        best_sc = _f(best.metrics.get("combined_score")) if (best and best.metrics) else "?"
        is_best = (child.get("id") == getattr(best, "id", None))
        msg = (
            f"new program        : id={str(child.get('id','?'))[:8]}  score={_f(score)}"
            f"{'  ⭐ NEW BEST' if is_best else ''}\n"
            f"db_size after add  : {len(self.database.programs)} programs\n"
            f"db.best now        : {best_sc}\n"
            f"\n"
            f"VARIABLES UPDATED IN base_database.py:\n"
            f"  database.programs[id]     ← dict gets new Program entry\n"
            f"  database.last_iteration   ← updated to {iteration}\n"
            f"  database.best_program_id  ← {str(getattr(self.database,'best_program_id','?'))[:8]}"
            f"  {'← CHANGED (new best!)' if is_best else '← unchanged'}\n"
            f"\n"
            f"DESIGN CHECK: ALL programs stored regardless of score (no pruning in EvolvedProgramDatabase).\n"
            f"  Contrast with TopKDatabase which prunes worst.\n"
            f"  _update_best_program() called inside add() to maintain best_program_id pointer."
        )
        if not _S.in_search_evo:
            evt("database.add() + _update_best_program()", "skydiscover/search/base_database.py", msg)
    DiscoveryController._process_iteration_result = _patched_proc

    # ── 12. ProgramDatabase._update_best_program ──────────────────────────────
    _orig_ubp = ProgramDatabase._update_best_program
    def _patched_ubp(self, program):
        old_best_id = self.best_program_id
        old_best = self.programs.get(old_best_id) if old_best_id else None
        old_score = _f((old_best.metrics or {}).get("combined_score")) if old_best else "None"
        new_score = _f((program.metrics or {}).get("combined_score"))

        _orig_ubp(self, program)

        new_best_id = self.best_program_id
        changed = (old_best_id != new_best_id)
        msg = (
            f"incoming program : id={str(program.id)[:8]}  score={new_score}\n"
            f"current best     : id={str(old_best_id)[:8] if old_best_id else 'None'}  score={old_score}\n"
            f"decision         : {'CHANGED → ' + str(new_best_id)[:8] + ' is new best_program_id' if changed else 'UNCHANGED → current best retained (incoming not better)'}\n"
            f"\n"
            f"LOGIC: _is_better() uses get_score(prog.metrics) which reads 'combined_score'.\n"
            f"  database.best_program_id {'← UPDATED to ' + str(new_best_id)[:8] if changed else '← NOT changed'}"
        )
        if not _S.in_search_evo:
            evt("_update_best_program()", "skydiscover/search/base_database.py", msg)
    ProgramDatabase._update_best_program = _patched_ubp

    # ── 13. ProgramDatabase.log_prompt ────────────────────────────────────────
    _orig_lp = ProgramDatabase.log_prompt
    def _patched_lp(self, program_id, template_key, prompt, responses=None):
        enabled = getattr(self.config, "log_prompts", False)
        pre_count = len(self.prompts_by_program or {})
        _orig_lp(self, program_id, template_key, prompt, responses)
        post_count = len(self.prompts_by_program or {})
        msg = (
            f"program_id          : {str(program_id)[:8]}\n"
            f"template_key        : {template_key}\n"
            f"config.log_prompts  : {enabled}  {'→ STORED in prompts_by_program' if enabled else '→ SKIPPED (disabled)'}\n"
            f"prompts_by_program  : {pre_count} → {post_count} programs logged\n"
            f"\n"
            f"DESIGN: log_prompt() stores prompt+response in database.prompts_by_program dict.\n"
            f"  Only writes if config.log_prompts=True (disabled here by default).\n"
            f"  Enables post-run analysis of every prompt sent to the LLM."
        )
        if not _S.in_search_evo:
            evt("log_prompt()", "skydiscover/search/base_database.py", msg)
    ProgramDatabase.log_prompt = _patched_lp

    # ── 14. LogWindowScorer.record_step ──────────────────────────────────────
    _orig_rec = LogWindowScorer.record_step
    def _patched_rec(self, best_score):
        _orig_rec(self, best_score)
        bs = f"{best_score:.4f}" if best_score is not None else "None"
        ss = f"{self._start_score:.4f}" if self._start_score is not None else "None"
        msg = (
            f"record_step(best_score={bs})\n"
            f"window so far : {[round(x,4) for x in self._best_scores]}\n"
            f"window_start  : {ss}   window_size: {self.get_window_size()}\n"
            f"\n"
            f"VARIABLE UPDATED:\n"
            f"  search_scorer._best_scores  ← list appended with {bs}\n"
            f"\n"
            f"DESIGN CHECK: record_step called once per iteration attempt.\n"
            f"  Multiple calls happen when retry_times>1 — each attempt counts as a step.\n"
            f"  Window scores are used to compute the final search strategy score."
        )
        if not _S.in_search_evo:
            evt("LogWindowScorer.record_step()", "search/evox/utils/search_scorer.py", msg)
    LogWindowScorer.record_step = _patched_rec

    # ── 15. _should_evolve_search — TRIGGERS tree + state snapshot ────────────
    _orig_should = CoEvolutionController._should_evolve_search
    def _patched_should(self):
        pre_last  = self._last_tracked_best_score
        pre_stag  = self._stagnant_count
        pre_curr  = self._get_best_score()

        result = _orig_should(self)

        post_stag = self._stagnant_count
        post_last = self._last_tracked_best_score

        if _S.events:
            _print_iteration_tree()

        delta = pre_curr - (pre_last or 0)
        if pre_last is None:
            rule = "first call → stagnant reset to 0 (no comparison yet)"
        elif delta > 0.01:
            rule = f"Δ={delta:+.4f} > 0.01 → stagnant RESET to 0"
        else:
            rule = f"Δ={delta:+.4f} ≤ 0.01 → stagnant +1 (was {pre_stag}, now {pre_stag+1})"

        if result:
            check = (f"YES ⚡  → stagnant({pre_stag+1 if pre_last is not None and delta<=0.01 else pre_stag})"
                     f" >= switch_interval({self._switch_interval}) → counter RESET to 0 → _evolve_search() runs")
        else:
            check = f"no  → stagnant={post_stag} < switch_interval={self._switch_interval}"

        p(f"  [_should_evolve_search]  file: skydiscover/search/evox/controller.py")
        p(f"  BEFORE: last_tracked={_f(pre_last)}  current={_f(pre_curr)}")
        p(f"  RULE  : {rule}")
        p(f"  AFTER : _last_tracked_best_score ← {_f(post_last)}  "
          f"_stagnant_count ← {post_stag}")
        p(f"  → TRIGGER: {check}")
        p()

        _print_state_snapshot(self)

        return result
    CoEvolutionController._should_evolve_search = _patched_should

    # ── 16. _reset_search_window ──────────────────────────────────────────────
    _orig_rsw = CoEvolutionController._reset_search_window
    def _patched_rsw(self, start_iteration=None):
        pre_start = self.search_scorer.get_start_score()
        pre_scores = list(getattr(self.search_scorer, "_best_scores", []))
        _orig_rsw(self, start_iteration)
        post_start = self.search_scorer.get_start_score()

        p(f"  [_reset_search_window()]  file: skydiscover/search/evox/controller.py")
        p(f"  WHY: new search strategy starting (or startup) → open fresh scoring window")
        p(f"  start_iteration param : {start_iteration}")
        p(f"  VARIABLES UPDATED:")
        p(f"    search_scorer._start_score : {_f(pre_start)} → {_f(post_start)}")
        p(f"    search_scorer._best_scores : {[round(x,4) for x in pre_scores]} → []  (cleared)")
        p()
    CoEvolutionController._reset_search_window = _patched_rsw

    # ── 17. _evolve_search ────────────────────────────────────────────────────
    _orig_evo = CoEvolutionController._evolve_search
    async def _patched_evo(self, solution_iter):
        _S.search_evo_num += 1
        _S.in_search_evo = True
        await _orig_evo(self, solution_iter)
        _S.in_search_evo = False
    CoEvolutionController._evolve_search = _patched_evo

    # ── 18. _initialize_first_search_program ──────────────────────────────────
    _orig_init_first = CoEvolutionController._initialize_first_search_program
    async def _patched_init_first(self, solution_iter):
        p()
        p(f"  ┌─ _initialize_first_search_program()  [controller.py]")
        p(f"  │  Runs on VERY FIRST search evolution only")
        p(f"  │  Scores the initial (file-based) search strategy before generating first replacement")
        p(f"  │  solution_iter        : {solution_iter}")
        p(f"  │  current window start : {_f(self.search_scorer.get_start_score())}")
        p(f"  │  window steps so far  : {[round(x,4) for x in getattr(self.search_scorer,'_best_scores',[])]}")
        pre_evos = self._num_search_evolutions
        pre_best = self._best_search_score

        await _orig_init_first(self, solution_iter)

        p(f"  │  VARIABLES UPDATED:")
        p(f"  │    _num_search_evolutions : {pre_evos} → {self._num_search_evolutions}")
        p(f"  │    _best_search_score     : {_f(pre_best)} → {_f(self._best_search_score)}"
          f"  ← initial strategy's score becomes the bar to beat")
        p(f"  │    search_controller.database.programs : {len(self.search_controller.database.programs)} strategies")
        p(f"  │  → then calls _generate_and_validate_search_algorithm() to generate first replacement")
        p(f"  └─ done")
        p()
    CoEvolutionController._initialize_first_search_program = _patched_init_first

    # ── 19. _build_search_stats ───────────────────────────────────────────────
    _orig_bss = CoEvolutionController._build_search_stats
    def _patched_bss(self, solution_iter):
        result = _orig_bss(self, solution_iter)
        sa = result.get("search_algorithm_stats", {})
        db_s = result.get("db_stats", {})
        pop  = db_s.get("population_size", 0)
        top_scores = db_s.get("top_solution_scores", [])[:5]
        score_summary = db_s.get("solution_score_summary", {})
        recent = db_s.get("recent_solution_stats", {})
        traj = recent.get("score_trajectory", [])

        p(f"  │  _build_search_stats()  [controller.py]  ← context passed to search LLM")
        p(f"  │  search_algorithm_stats:")
        p(f"  │    window_start_iteration : {sa.get('window_start_iteration')}")
        p(f"  │    total_iterations       : {sa.get('total_iterations')}")
        p(f"  │    search_window_horizon  : {sa.get('search_window_horizon')}")
        p(f"  │    improvement_threshold  : {sa.get('improvement_threshold')}")
        p(f"  │  db_stats (population snapshot passed to search LLM):")
        p(f"  │    population_size        : {pop} programs")
        p(f"  │    top_5_scores           : {[round(s,4) for s in top_scores]}")
        p(f"  │    score_summary          : best={_f(score_summary.get('best'))}  "
          f"q75={_f(score_summary.get('q75'))}  q50={_f(score_summary.get('q50'))}  "
          f"worst={_f(score_summary.get('worst'))}")
        p(f"  │    recent_score_trajectory: {[round(s,4) for s in traj[-5:]]}")
        p(f"  │  NOTE: search LLM uses these stats to decide HOW to sample parents/context")
        p()
        return result
    CoEvolutionController._build_search_stats = _patched_bss

    # ── 20. _assign_search_score ─────────────────────────────────────────────
    _orig_ass = CoEvolutionController._assign_search_score
    def _patched_ass(self):
        win_size    = self.search_scorer.get_window_size()
        start_score = self.search_scorer.get_start_score() or 0.0
        end_score   = self._get_best_score()
        window      = [round(x,4) for x in getattr(self.search_scorer,"_best_scores",[])]

        is_new_best = _orig_ass(self)

        pend = self._pending_search_result
        computed = None
        if pend:
            computed = (pend.child_program_dict or {}).get("metrics", {}).get("combined_score")

        p(f"  │  _assign_search_score():")
        p(f"  │    start_score   : {_f(start_score)}  ← score when this strategy first activated")
        p(f"  │    end_score     : {_f(end_score)}   ← current best solution score")
        p(f"  │    improvement   : {_f(end_score - start_score)} = end − start")
        p(f"  │    window        : {window}  ({win_size} steps)")
        p(f"  │    formula       : (end−start) × log_weight / √horizon")
        p(f"  │    combined_score: {_f(computed)}")
        p(f"  │    is_new_best   : {is_new_best}  (_best_search_score now {_f(self._best_search_score)})")
        return is_new_best
    CoEvolutionController._assign_search_score = _patched_ass

    # ── 21. _finalize_pending_search ─────────────────────────────────────────
    _orig_fin = CoEvolutionController._finalize_pending_search
    async def _patched_fin(self):
        pend = self._pending_search_result
        pend_id = str((pend.child_program_dict or {}).get("id","?"))[:8] if pend else "?"
        pre_num = self._num_search_evolutions
        pre_best_ss = self._best_search_score

        p()
        p(f"  ┌─ _finalize_pending_search()  [controller.py]")
        p(f"  │  Previous search strategy being SCORED (window closing)")
        p(f"  │  strategy_id    : {pend_id}")
        p(f"  │  window_start   : {_f(self.search_scorer.get_start_score())}")
        p(f"  │  window_end     : {_f(self._get_best_score())}")
        p(f"  │  CALLS → _assign_search_score() (next)")

        await _orig_fin(self)

        p(f"  │  VARIABLES UPDATED:")
        p(f"  │    _num_search_evolutions : {pre_num} → {self._num_search_evolutions}")
        p(f"  │    _best_search_score     : {_f(pre_best_ss)} → {_f(self._best_search_score)}")
        p(f"  │    _pending_search_result : SET → None  (cleared after scoring)")
        p(f"  │    search_controller.database.programs : {len(self.search_controller.database.programs)} strategies total")
        p(f"  └─ done")
    CoEvolutionController._finalize_pending_search = _patched_fin

    # ── 22. _generate_and_validate_search_algorithm ───────────────────────────
    _orig_gv = CoEvolutionController._generate_and_validate_search_algorithm
    async def _patched_gv(self, solution_iter):
        p()
        p(f"  ┌─ _generate_and_validate_search_algorithm()  [controller.py]")
        p(f"  │  Asks search_controller (inner LLM) to write a new EvolvedProgramDatabase class")
        p(f"  │  solution_iter       : {solution_iter}")
        p(f"  │  _num_search_evolutions: {self._num_search_evolutions}  (this is the iteration index)")
        p(f"  │  search_controller.database: {len(self.search_controller.database.programs)} strategies stored")
        p(f"  │  CALLS → _build_search_stats() then search_controller.run_discovery(max_iterations=1)")
        p(f"  │          then search_strategy_evaluator.evaluate() to validate the new class")
        pre_pend = self._pending_search_result

        await _orig_gv(self, solution_iter)

        post_pend = self._pending_search_result
        p(f"  │  RESULT:")
        p(f"  │    _pending_search_result : {'NONE → was' if not post_pend else 'SET'}"
          f"{'generation failed/invalid' if not post_pend else ' → new strategy ready'}")
        p(f"  └─ done")
        p()
    CoEvolutionController._generate_and_validate_search_algorithm = _patched_gv

    # ── 23. _switch_to_new_search_algorithm ───────────────────────────────────
    _orig_sw = CoEvolutionController._switch_to_new_search_algorithm
    def _patched_sw(self, result):
        old_code  = _S.active_search_code
        new_code  = (result.child_program_dict or {}).get("solution", "")
        old_db_id = id(self.database)

        success = _orig_sw(self, result)

        if success:
            _S.active_search_code = new_code
            _install_sample_probe._fn(self.database, "evolved_strategy")

        p(); p(f"  {'─'*68}")
        p(f"  _switch_to_new_search_algorithm()  success={success}")
        p(f"  file: skydiscover/search/evox/controller.py")
        p()
        p(f"  WHAT HAPPENED (step by step):")
        p(f"    1. new_code (LLM output) written to tempfile")
        p(f"    2. load_database_from_file(tempfile)  ← exec()'s the Python code")
        p(f"       → gets new EvolvedProgramDatabase class  (dynamically created)")
        p(f"    3. new_db created with config  + DIVERGE/REFINE labels assigned via _assign_labels_to_db()")
        p(f"    4. ALL {len(self.database.programs) if success else '?'} programs migrated: "
          f"_migrate_to_db() copies every Program to new_db (no data lost)")
        p(f"    5. _wrap_add_method(new_db)  ← wraps add() to guarantee _update_best_program() fires")
        p(f"    6. _fallback_database = old db  (saved for crash recovery)")
        p(f"    7. self.database = new_db  ← POINTER SWAPPED")
        p(f"    8. _active_search_algorithm_code = new code")
        p()
        p(f"  VARIABLES UPDATED in controller:")
        p(f"    self.database          : OLD id={old_db_id}  → NEW id={id(self.database) if success else 'FAILED'}")
        p(f"    _fallback_database     : {'set' if success else 'unchanged'} (restores if new strategy crashes)")
        p(f"    _fallback_search_code  : old algorithm code saved")
        p(f"    _active_search_algorithm_code : {len(new_code)} chars")
        p()

        uses_d = "DIVERGE_LABEL" in new_code
        uses_r = "REFINE_LABEL"  in new_code
        p(f"  NEW search algorithm ({len(new_code)} chars):")
        p(f"    Uses DIVERGE_LABEL : {'YES → label CAN appear in prompts' if uses_d else 'NO  → label will NOT appear in prompts'}")
        p(f"    Uses REFINE_LABEL  : {'YES' if uses_r else 'NO'}")
        p()

        if new_code == old_code:
            p(f"  CHANGE: NONE — LLM wrote identical code to previous strategy")
            p(f"  NOTE: The search strategy did not actually change.")
        else:
            lines = new_code.splitlines()
            in_sample, sample_lines = False, []
            for ln in lines:
                if "def sample(" in ln: in_sample = True
                if in_sample:
                    sample_lines.append(ln)
                    if len(sample_lines) > 2 and ln.strip() and not ln.startswith(" ") and "def sample" not in ln:
                        break
            p(f"  NEW sample() ({len(sample_lines)} lines shown):")
            for ln in sample_lines[:40]: p(f"    {ln}")
            if len(sample_lines) > 40: p(f"    ... [{len(sample_lines)-40} more lines]")
        p(f"  {'─'*68}"); p()
        return success
    CoEvolutionController._switch_to_new_search_algorithm = _patched_sw

    p("All 23 patches installed.")
    p()
    return _install_sample_probe


# ─── Main ─────────────────────────────────────────────────────────────────────
async def _run(iters, output_dir):
    install_probe = _install_patches()

    from skydiscover.config import load_config, EvoxDatabaseConfig
    from skydiscover.runner import Runner
    import yaml

    EVOX  = PROJECT_ROOT / "skydiscover/search/evox/config/search.yaml"
    EVAL  = PROJECT_ROOT / "benchmarks/math/circle_packing/evaluator.py"
    INIT  = PROJECT_ROOT / "benchmarks/math/circle_packing/initial_program.py"
    CPCFG = PROJECT_ROOT / "benchmarks/math/circle_packing/config.yaml"

    config = load_config(str(EVOX))
    config.search.type = "evox"
    config.search.database = EvoxDatabaseConfig()
    config.max_iterations = iters
    config.checkpoint_interval = iters
    config.monitor.enabled = False

    # Solution LLM = gemma3:12b (writes circle packing code)
    # Search strategy LLM = qwen2.5-coder:14b (evolves sample() — loaded independently
    #   from search.yaml via EvoxDatabaseConfig.config_path, since share_llm=False)
    config.llm.models[0].name = "gemma3:12b"

    with open(CPCFG) as f:
        cp = yaml.safe_load(f)
    config.context_builder.system_message = cp.get("prompt", {}).get("system_message", "")
    config.context_builder.template = "evox"

    p(f"{'━'*70}")
    p(f"  PROBE RUN v5 — evox co-evolution  ({iters} iterations)")
    p(f"  LLM: {[m.name for m in config.llm.models]}   output → {output_dir}")
    p(f"{'━'*70}"); p()
    p("  FULL PIPELINE per iteration (23 probes across all files):")
    p("  controller.py → run_discovery() loop:")
    p("    1.  sample()                        search/evox/database/*.py")
    p("    2.  _build_prompt() wrapper         search/default_discovery_controller.py")
    p("        → db.get_statistics() for context assembly")
    p("    3.  EvoxContextBuilder.build_prompt() context_builder/evox/builder.py")
    p("        → system+user prompt strings constructed")
    p("    4.  _call_llm()                     llm/llm_pool.py → llm/openai.py")
    p("    5.  _parse_llm_response()           utils/code_utils.py")
    p("    6.  evaluate_program()              evaluation/evaluator.py")
    p("    7.  _create_child_program()         search/default_discovery_controller.py")
    p("        → Program dataclass fields set")
    p("    8.  database.add() + _update_best_program()  search/base_database.py")
    p("        → programs dict updated, best_program_id updated")
    p("    9.  log_prompt()                    search/base_database.py")
    p("   10.  LogWindowScorer.record_step()   search/evox/utils/search_scorer.py")
    p("   11.  _should_evolve_search()         search/evox/controller.py  ← flushes tree")
    p("    [if triggered]:")
    p("   12.  _reset_search_window()          controller.py")
    p("   13.  _initialize_first_search_program() OR _generate_and_validate_search_algorithm()")
    p("   14.  _build_search_stats()           controller.py  ← db context for search LLM")
    p("   15.  _finalize_pending_search()      controller.py")
    p("   16.  _assign_search_score()          controller.py  ← formula: (end-start)×log/√horizon")
    p("   17.  _switch_to_new_search_algorithm() controller.py  ← exec() + db pointer swap")
    p()

    runner = Runner(
        evaluation_file=str(EVAL),
        initial_program_path=str(INIT),
        config=config,
        output_dir=output_dir,
    )
    install_probe(runner.database, "initial_search_strategy")

    best = await runner.run(iterations=iters)
    p(); p(f"{'━'*70}")
    p(f"  RUN COMPLETE  best: id={str(getattr(best,'id','?'))[:8]}"
      f"  score={_f(best.metrics.get('combined_score')) if best and best.metrics else '?'}")
    p(f"  log → {PROBE_LOG}")
    p(f"{'━'*70}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--iters", type=int, default=20)
    ap.add_argument("--output-dir", default="outputs/probe_run_v5")
    args = ap.parse_args()
    asyncio.run(_run(args.iters, args.output_dir))

if __name__ == "__main__":
    main()
