#!/usr/bin/env python3
"""Generate one Obsidian note per function in the EvoX runtime path.

Each note contains:
  - What the function does
  - What functions it calls  (as [[wiki-links]] → edges in Graph View)
  - Parameters it receives
  - State it reads / writes
  - Which file it lives in

Run:
    python scripts/gen_obsidian_notes.py

Output: graphs/functions/*.md   (one file per function)
Then open Obsidian Graph View (Ctrl+G) to see the interactive network.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "graphs" / "functions"
OUT.mkdir(parents=True, exist_ok=True)

# ── note definitions ────────────────────────────────────────────────────────
# Each entry: (filename_stem, markdown_body)
# Use [[Name]] for any cross-reference — those become graph edges.

NOTES = {

# ─── RUNNER ────────────────────────────────────────────────────────────────

"Runner.run": """
# Runner.run

**File:** `skydiscover/runner.py`
**Layer:** #runner

## What it does
Top-level entry point. Wires up the database, controller, and evaluator, then hands off to [[CoEvolutionController.run_discovery]] (or the appropriate controller for the config). Also sets up logging, monitoring, and checkpoint callbacks.

## Calls
- [[Runner._load_initial_program]] — reads initial code from disk
- [[Runner._add_initial_program]] — seeds the database with the initial program
- [[CoEvolutionController.run_discovery]] — runs the main search loop

## Parameters
| Name | Type | Meaning |
|---|---|---|
| `max_iterations` | `int` | Total solution iterations to run |

## State written
- `self.database` — `ProgramDatabase` instance (created here)
- `self.controller` — controller instance (created here)
- Checkpoint files written periodically via `checkpoint_callback`

## Returns
Best program found after all iterations.
""",

"Runner._load_initial_program": """
# Runner._load_initial_program

**File:** `skydiscover/runner.py`
**Layer:** #runner

## What it does
Reads the initial program source code from disk (path set in config). Called once during startup before the search loop begins.

## Calls
_(no cross-module calls — pure file I/O)_

## Parameters
| Name | Type | Meaning |
|---|---|---|
| `config.initial_program_file` | `str` | Path to the seed `.py` file |

## State written
- `self._initial_program_code` — raw source string stored on the runner

## Returns
`str` — source code of the initial program.
""",

"Runner._add_initial_program": """
# Runner._add_initial_program

**File:** `skydiscover/runner.py`
**Layer:** #runner

## What it does
Evaluates the initial program and adds it to the database with score 0 (or its real score if evaluation succeeds). This seeds the database so the first iteration has a parent to work from.

## Calls
- [[ProgramDatabase.add]] — stores the seed program

## Parameters
| Name | Type | Meaning |
|---|---|---|
| `initial_code` | `str` | Source code of the seed program |

## State written
- [[ProgramDatabase]] gets its first entry

## Returns
Nothing — side-effect only.
""",

# ─── CO-EVOLUTION CONTROLLER ───────────────────────────────────────────────

"CoEvolutionController.run_discovery": """
# CoEvolutionController.run_discovery

**File:** `skydiscover/search/evox/controller.py`
**Layer:** #outer-loop

## What it does
Main co-evolution loop. For each solution iteration:
1. Runs one inner-loop step via [[DiscoveryController._run_iteration]]
2. Records progress via [[LogWindowScorer.record_step]]
3. Checks stagnation via [[CoEvolutionController._should_evolve_search]]
4. If stagnant → triggers [[CoEvolutionController._evolve_search]]

Also calls [[CoEvolutionController._generate_variation_operators]] once at startup.

## Calls
- [[CoEvolutionController._generate_variation_operators]]
- [[DiscoveryController._run_iteration]]
- [[LogWindowScorer.record_step]]
- [[CoEvolutionController._should_evolve_search]]
- [[CoEvolutionController._evolve_search]]
- [[CoEvolutionController._finalize_pending_search]]

## Parameters
| Name | Type | Meaning |
|---|---|---|
| `start_iteration` | `int` | Iteration counter offset (for resumed runs) |
| `max_iterations` | `int` | How many solution iterations to run |

## State written
- `self._stagnant_count` — reset/incremented each iteration
- `self.database` — updated as improved programs are found
- `self._pending_search_result` — set when a new search alg is generated

## Returns
Best program in the database after the loop ends.
""",

"CoEvolutionController._should_evolve_search": """
# CoEvolutionController._should_evolve_search

**File:** `skydiscover/search/evox/controller.py`
**Layer:** #outer-loop

## What it does
Stagnation gate. After every inner-loop iteration, compares the current best score to the last tracked best:
- If improvement > 0.01 → reset `_stagnant_count` to 0
- Otherwise → increment `_stagnant_count`
- If `_stagnant_count >= _switch_interval` → return `True` (trigger outer loop)

`_switch_interval` defaults to 10% of `max_iterations`.

## Calls
_(reads `self.database.get_best_program()` — no cross-module calls)_

## Parameters
None (reads instance state)

## State written
- `self._stagnant_count` — incremented or reset
- `self._last_tracked_best_score` — updated to current best

## Returns
`bool` — `True` means "run the outer loop now".
""",

"CoEvolutionController._evolve_search": """
# CoEvolutionController._evolve_search

**File:** `skydiscover/search/evox/controller.py`
**Layer:** #outer-loop

## What it does
Entry point for the outer loop when stagnation is detected. On the very first call it initialises the search strategy database; on subsequent calls it:
1. Finalises and scores the previous search strategy via [[CoEvolutionController._finalize_pending_search]]
2. Resets the score window
3. Generates a new search algorithm via [[CoEvolutionController._generate_and_validate_search_algorithm]]

## Calls
- [[CoEvolutionController._finalize_pending_search]]
- [[CoEvolutionController._generate_and_validate_search_algorithm]]
- [[LogWindowScorer.reset_window]]

## Parameters
| Name | Type | Meaning |
|---|---|---|
| `solution_iter` | `int` | Current solution iteration number (passed to outer LLM for context) |

## State written
- `self._pending_search_result` — cleared (old) then set (new)
- `self.search_controller.database` — may gain a new program

## Returns
Nothing — side-effects only.
""",

"CoEvolutionController._finalize_pending_search": """
# CoEvolutionController._finalize_pending_search

**File:** `skydiscover/search/evox/controller.py`
**Layer:** #outer-loop

## What it does
Scores the search strategy that was active during the last window, stores the result in the search-strategy database, and clears `_pending_search_result`.

## Calls
- [[CoEvolutionController._assign_search_score]] — computes the performance score
- `search_controller.postprocess_result` — saves to disk / updates search DB

## Parameters
None (reads `self._pending_search_result`)

## State written
- `self._pending_search_result` → set to `None`
- `self._num_search_evolutions` → incremented by 1
- Search strategy database gains a scored program

## Returns
Nothing.
""",

"CoEvolutionController._assign_search_score": """
# CoEvolutionController._assign_search_score

**File:** `skydiscover/search/evox/controller.py`
**Layer:** #outer-loop

## What it does
Asks [[LogWindowScorer.get_score]] for the improvement metric over the last window, then attaches it to the pending search result as `metrics["combined_score"]`.

## Calls
- [[LogWindowScorer.get_score]]

## Parameters
None (reads `self._pending_search_result` and scorer state)

## State written
- `self._pending_search_result.child_program_dict["metrics"]` — score written in-place
- `self._best_search_score` — updated if new score is higher

## Returns
`bool` — `True` if this strategy beat the previous best.
""",

"CoEvolutionController._generate_and_validate_search_algorithm": """
# CoEvolutionController._generate_and_validate_search_algorithm

**File:** `skydiscover/search/evox/controller.py`
**Layer:** #outer-loop

## What it does
Asks the outer LLM (qwen2.5-coder:14b) to write a new `EvolvedProgramDatabase` subclass in Python, then validates it by attempting to instantiate it. If valid, calls [[CoEvolutionController._switch_to_new_search_algorithm]].

The LLM receives population statistics (scores, diversity, stagnation window) so it can reason about what sampling strategy to use next.

Sets `loop_type = "outer"` via [[LangFuseTracer.log_generation]] through the context var.

## Calls
- [[DiscoveryController.run_discovery]] (search_controller — 1 iteration)
- [[CoEvolutionController._switch_to_new_search_algorithm]]

## Parameters
| Name | Type | Meaning |
|---|---|---|
| `solution_iter` | `int` | Passed as context to the LLM |

## State written
- `self._pending_search_result` — set to the new result
- `self._num_search_evolutions` → incremented on failure

## Returns
Nothing — side-effects only.
""",

"CoEvolutionController._switch_to_new_search_algorithm": """
# CoEvolutionController._switch_to_new_search_algorithm

**File:** `skydiscover/search/evox/controller.py`
**Layer:** #outer-loop

## What it does
Dynamically loads the LLM-generated Python code as a new `EvolvedProgramDatabase` class, migrates all existing programs from the old database to it, and replaces `self.database`. The old database is kept as `self._fallback_database` in case the new strategy crashes.

## Calls
- `load_database_from_file` — dynamic import of LLM-generated code
- [[ProgramDatabase.add]] — via migration loop

## Parameters
| Name | Type | Meaning |
|---|---|---|
| `result` | `SerializableResult` | Contains the new search algorithm source in `child_program_dict["solution"]` |

## State written
- `self.database` → replaced with new `EvolvedProgramDatabase` instance
- `self._fallback_database` → old database saved here
- `self._active_search_algorithm_code` → updated

## Returns
`bool` — `True` if switch succeeded, `False` if code was invalid.
""",

"CoEvolutionController._generate_variation_operators": """
# CoEvolutionController._generate_variation_operators

**File:** `skydiscover/search/evox/controller.py`
**Layer:** #outer-loop

## What it does
Called once at startup. Uses the outer LLM to generate two short text labels — `DIVERGE_LABEL` and `REFINE_LABEL` — that get attached to the database. These labels guide whether the inner-loop LLM should explore new ideas or refine existing ones.

## Calls
- [[LLMPool.generate]] (via `search_controller.guide_llms`)

## Parameters
None — reads `self.config` and `self.evaluation_file`

## State written
- `self._diverge_label` — set once, never re-generated
- `self._refine_label` — set once, never re-generated
- `self.database.DIVERGE_LABEL` / `self.database.REFINE_LABEL` — attached to DB

## Returns
Nothing.
""",

# ─── DISCOVERY CONTROLLER (inner loop) ────────────────────────────────────

"DiscoveryController.run_discovery": """
# DiscoveryController.run_discovery

**File:** `skydiscover/search/default_discovery_controller.py`
**Layer:** #inner-loop

## What it does
Runs the sequential inner loop: calls [[DiscoveryController._run_iteration]] for each iteration up to `max_iterations`. Used both as the solution evolution loop (by [[Runner.run]]) and as the search-strategy generation loop (by [[CoEvolutionController._generate_and_validate_search_algorithm]] with `max_iterations=1`).

## Calls
- [[DiscoveryController._run_iteration]]

## Parameters
| Name | Type | Meaning |
|---|---|---|
| `start_iteration` | `int` | Iteration counter offset |
| `max_iterations` | `int` | Number of steps |

## State written
- `self.database` — updated as new programs are evaluated
- Checkpoint files (via callback)

## Returns
Best `Program` at the end of the loop.
""",

"DiscoveryController._run_iteration": """
# DiscoveryController._run_iteration

**File:** `skydiscover/search/default_discovery_controller.py`
**Layer:** #inner-loop

## What it does
One complete generate-evaluate cycle:
1. [[ProgramDatabase.sample]] — pick a parent and context programs
2. [[DiscoveryController._build_prompt]] — build system + user messages
3. [[DiscoveryController._call_llm]] → [[LLMPool.generate]] — call the inner LLM
4. [[DiscoveryController._parse_llm_response]] — extract child code (diff or full rewrite)
5. `evaluate_program` — run the evaluator subprocess
6. [[ProgramDatabase.add]] — store the child if valid

Sets `loop_type = "inner"` via `set_llm_context` so [[LangFuseTracer.log_generation]] tags the trace correctly.

## Calls
- [[ProgramDatabase.sample]]
- [[DiscoveryController._build_prompt]]
- [[DiscoveryController._call_llm]]
- [[DiscoveryController._parse_llm_response]]
- [[ProgramDatabase.add]]

## Parameters
| Name | Type | Meaning |
|---|---|---|
| `iteration` | `int` | Current iteration index |
| `retry_times` | `int` | How many LLM retries before giving up (default 1) |

## State written
- [[ProgramDatabase]] — new child program added if score improves
- `self._best_score` — updated if child beats current best

## Returns
`SerializableResult` — contains child program dict, score, error (if any).
""",

"DiscoveryController._build_prompt": """
# DiscoveryController._build_prompt

**File:** `skydiscover/search/default_discovery_controller.py`
**Layer:** #inner-loop

## What it does
Assembles the `{"system": ..., "user": ...}` dict that gets sent to the LLM. Passes the parent program, context programs (for few-shot examples), database stats, and any failed previous attempts to the `ContextBuilder`.

## Calls
- `ContextBuilder.build_prompt` — formats the templates

## Parameters
| Name | Type | Meaning |
|---|---|---|
| `current_program` | `Program` | Parent program to improve |
| `context_programs` | `dict[str, list[Program]]` | Additional examples |
| `failed_attempts` | `list` | Previous parse failures for retry context |

## State written
Nothing — pure computation.

## Returns
`dict` with keys `"system"` and `"user"` — the formatted prompt.
""",

"DiscoveryController._call_llm": """
# DiscoveryController._call_llm

**File:** `skydiscover/search/default_discovery_controller.py`
**Layer:** #inner-loop

## What it does
Thin wrapper: converts the prompt dict into `(system_message, messages)` format and calls [[LLMPool.generate]].

## Calls
- [[LLMPool.generate]]

## Parameters
| Name | Type | Meaning |
|---|---|---|
| `system_message` | `str` | System prompt |
| `user_message` | `str` | User turn |

## State written
Nothing — pure call-through.

## Returns
`LLMResponse` with `.text` field containing the raw LLM output.
""",

"DiscoveryController._parse_llm_response": """
# DiscoveryController._parse_llm_response

**File:** `skydiscover/search/default_discovery_controller.py`
**Layer:** #inner-loop

## What it does
Extracts the child program from the raw LLM text. Two modes depending on config:
- **diff mode** (`diff_based_generation=True`) — finds `SEARCH/REPLACE` blocks, applies them to the parent
- **full rewrite mode** — extracts a complete code block from the response

If nothing valid is found, returns `(None, None, error_message)` so the caller can retry.

## Calls
- `extract_diffs` / `apply_diff` (diff mode)
- `parse_full_rewrite` (full rewrite mode)

## Parameters
| Name | Type | Meaning |
|---|---|---|
| `llm_response` | `str` | Raw text from the LLM |
| `parent_solution` | `str` | Current parent code (needed for diff application) |
| `iteration` | `int` | For logging |

## State written
Nothing — pure parsing.

## Returns
`(child_solution, changes_summary, parse_error)` — all strings; parse_error is None on success.
""",

# ─── LOG WINDOW SCORER ─────────────────────────────────────────────────────

"LogWindowScorer.record_step": """
# LogWindowScorer.record_step

**File:** `skydiscover/search/evox/utils/search_scorer.py`
**Layer:** #scorer

## What it does
Records the best score seen so far into the sliding window buffer. Called once per inner-loop iteration by [[CoEvolutionController.run_discovery]].

## Calls
Nothing.

## Parameters
| Name | Type | Meaning |
|---|---|---|
| `score` | `float` | Current best score in the solution database |

## State written
- `self._window` — appends the new score

## Returns
Nothing.
""",

"LogWindowScorer.get_score": """
# LogWindowScorer.get_score

**File:** `skydiscover/search/evox/utils/search_scorer.py`
**Layer:** #scorer

## What it does
Computes the performance metric for the current search strategy over the window. Called by [[CoEvolutionController._assign_search_score]] when scoring a finished strategy. The metric reflects how much improvement happened during the window.

## Calls
Nothing.

## Parameters
None (reads `self._window`)

## State written
Nothing — pure computation.

## Returns
`float` — combined score (higher is better search strategy).
""",

"LogWindowScorer.reset_window": """
# LogWindowScorer.reset_window

**File:** `skydiscover/search/evox/utils/search_scorer.py`
**Layer:** #scorer

## What it does
Clears the score window so a fresh measurement starts for the new search strategy. Called by [[CoEvolutionController._evolve_search]] after switching strategies.

## Calls
Nothing.

## Parameters
| Name | Type | Meaning |
|---|---|---|
| `start_score` | `float` | Baseline score at the start of the new window |

## State written
- `self._window` → cleared and initialised with `start_score`
- `self._start_score` → updated

## Returns
Nothing.
""",

# ─── PROGRAM DATABASE ──────────────────────────────────────────────────────

"ProgramDatabase.sample": """
# ProgramDatabase.sample

**File:** `skydiscover/search/base_database.py`
**Layer:** #database

## What it does
Selects one parent program and a list of context programs from the current population. The sampling strategy is implementation-defined — the default uses score-weighted sampling; the outer LLM can replace this with a custom `EvolvedProgramDatabase` class that overrides this method.

## Calls
Nothing (reads `self.programs`).

## Parameters
| Name | Type | Meaning |
|---|---|---|
| `num_context_programs` | `int` | How many additional examples to return |

## State written
Nothing — read-only.

## Returns
`(parent, context_programs)` — the selected programs.
""",

"ProgramDatabase.add": """
# ProgramDatabase.add

**File:** `skydiscover/search/base_database.py`
**Layer:** #database

## What it does
Adds a new program to the population. May evict lower-scoring programs depending on the database type (top-k, beam, evox, etc.).

## Calls
Nothing.

## Parameters
| Name | Type | Meaning |
|---|---|---|
| `program` | `Program` | The new candidate program |
| `iteration` | `int` | Which iteration produced it |

## State written
- `self.programs` — new program inserted
- `self.best_program_id` — updated if the new program beats current best

## Returns
Nothing.
""",

# ─── LLM POOL ──────────────────────────────────────────────────────────────

"LLMPool.generate": """
# LLMPool.generate

**File:** `skydiscover/llm/llm_pool.py`
**Layer:** #llm

## What it does
Entry point for all LLM calls. Picks one model from the pool via [[LLMPool._sample_model]] (weighted random if multiple keys are configured), then delegates to [[OpenAILLM.generate]].

## Calls
- [[LLMPool._sample_model]]
- [[OpenAILLM.generate]]

## Parameters
| Name | Type | Meaning |
|---|---|---|
| `system_message` | `str` | System prompt |
| `messages` | `list[dict]` | Conversation turns |
| `**kwargs` | | Forwarded to the underlying LLM (temperature, max_tokens, etc.) |

## State written
Nothing (stateless dispatch).

## Returns
`LLMResponse` with `.text`.
""",

"LLMPool._sample_model": """
# LLMPool._sample_model

**File:** `skydiscover/llm/llm_pool.py`
**Layer:** #llm

## What it does
Picks which `OpenAILLM` instance to use for this call. With a single API key this always returns the same instance; with multiple keys it samples proportionally to weights.

## Calls
Nothing.

## Parameters
None (reads `self.models`).

## State written
Nothing.

## Returns
`OpenAILLM` instance to use.
""",

# ─── OPENAI LLM ────────────────────────────────────────────────────────────

"OpenAILLM.generate": """
# OpenAILLM.generate

**File:** `skydiscover/llm/openai.py`
**Layer:** #llm

## What it does
Top-level method on the OpenAI-compatible client. Dispatches to [[OpenAILLM._generate_text]] for regular completions or `_generate_with_image` for image generation.

## Calls
- [[OpenAILLM._generate_text]]

## Parameters
| Name | Type | Meaning |
|---|---|---|
| `system_message` | `str` | System prompt |
| `messages` | `list[dict]` | Conversation turns |
| `image_output` | `bool` | If True, use image generation mode |

## State written
Nothing.

## Returns
`LLMResponse(text=..., image_path=...)`.
""",

"OpenAILLM._generate_text": """
# OpenAILLM._generate_text

**File:** `skydiscover/llm/openai.py`
**Layer:** #llm

## What it does
Formats the messages, builds the API params (handles reasoning models vs standard), then enters the retry loop. Times each attempt and passes latency + token usage to [[LangFuseTracer.log_generation]].

Reads `loop_type` and `iteration` from the async context var set by `set_llm_context`.

## Calls
- [[OpenAILLM._call_api]]
- [[LangFuseTracer.log_generation]]

## Parameters
| Name | Type | Meaning |
|---|---|---|
| `system_message` | `str` | Prepended as the system role message |
| `messages` | `list[dict]` | User/assistant turns |
| `temperature` | `float` | Overrides instance default |
| `max_tokens` | `int` | Overrides instance default |

## State written
Nothing (the tracer call is a side-effect, not mutation of self).

## Returns
`str` — raw text content from the model.
""",

"OpenAILLM._call_api": """
# OpenAILLM._call_api

**File:** `skydiscover/llm/openai.py`
**Layer:** #llm

## What it does
Makes the actual HTTP request to the OpenAI-compatible endpoint (Ollama, Azure, OpenAI, etc.) using `client.chat.completions.create`. Runs in a thread-pool executor so it doesn't block the async event loop. Falls back to the Responses API if Chat Completions returns an "unsupported" error.

## Calls
- `self.client.chat.completions.create` (sync, in executor)

## Parameters
| Name | Type | Meaning |
|---|---|---|
| `params` | `dict` | Full API params (model, messages, temperature, max_tokens, …) |

## State written
Nothing.

## Returns
`(text: str, usage: dict | None)` — response text and token counts.
""",

# ─── LANGFUSE TRACER ───────────────────────────────────────────────────────

"LangFuseTracer.log_generation": """
# LangFuseTracer.log_generation

**File:** `skydiscover/llm/langfuse_tracer.py`
**Layer:** #observability

## What it does
Sends one generation record to LangFuse (if configured). Records:
- Full prompt (messages list)
- Full response text
- Latency in seconds
- Token usage (prompt / completion / total)
- `loop_type` — "inner" or "outer" — so you can filter by loop in the UI
- `iteration` number

Called by [[OpenAILLM._generate_text]] immediately after each successful API call. No-op if `LANGFUSE_PUBLIC_KEY` / `LANGFUSE_SECRET_KEY` are not set.

## Calls
- `self._client.generation(...)` — LangFuse v2 SDK

## Parameters
| Name | Type | Meaning |
|---|---|---|
| `model` | `str` | Model name (e.g. "gemma3:12b") |
| `messages` | `list[dict]` | Full prompt sent |
| `output` | `str` | Response text |
| `latency_s` | `float` | Wall-clock time for the API call |
| `usage` | `dict` | Token counts |
| `loop_type` | `str` | "inner" / "outer" / "unknown" |
| `iteration` | `int` | Current iteration number |

## State written
LangFuse remote trace (external side-effect only — nothing in-process).

## Returns
Nothing.
""",

}  # end NOTES


def write_notes() -> None:
    for stem, body in NOTES.items():
        path = OUT / f"{stem}.md"
        path.write_text(body.strip() + "\n")
    print(f"Written {len(NOTES)} notes to {OUT.relative_to(ROOT)}/")
    print("Open Obsidian → press Ctrl+G for the interactive graph.")


if __name__ == "__main__":
    write_notes()
