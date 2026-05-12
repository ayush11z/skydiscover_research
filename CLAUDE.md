# SkyDiscover — Codebase Map

## What this project does
SkyDiscover is an evolutionary search framework that uses LLMs to iteratively improve programs (solutions). Given an initial program and an evaluator, it runs a search loop: sample programs from a database → build a prompt → call an LLM → evaluate the result → store improved programs. It supports multiple search strategies (evox co-evolution, adaevolve, beam search, topk, best-of-n, etc.) and multiple LLM providers.

---

## Entry Points

| File | Purpose |
|---|---|
| `skydiscover/runner.py` | Top-level `Runner` class — loads config, wires database + controller, runs the search loop, saves checkpoints |
| `skydiscover/cli.py` | CLI wrapper around `Runner` |
| `skydiscover/api.py` | Public Python API |

---

## Core Package: `skydiscover/`

### Config
| File | Purpose |
|---|---|
| `skydiscover/config.py` | `Config` dataclass + YAML loader. Handles provider/model resolution (openai, gemini, anthropic, etc.) |

### Search
| File | Purpose |
|---|---|
| `skydiscover/search/base_database.py` | `Program` dataclass + `ProgramDatabase` ABC — the shared interface for all search backends |
| `skydiscover/search/registry.py` | Registry + factory: maps search type strings → database/controller/program classes |
| `skydiscover/search/route.py` | Picks the right controller for a given config |
| `skydiscover/search/default_discovery_controller.py` | Default `DiscoveryController` — the sample→prompt→LLM→evaluate loop |

#### Search Strategies (each has `database.py` + optional `controller.py`)
| Directory | Strategy |
|---|---|
| `skydiscover/search/evox/` | **Co-evolution**: evolves solution programs AND search algorithms simultaneously. `controller.py` = `CoEvolutionController`; `database/` has `search_strategy_db.py`, `search_strategy_evaluator.py`, `initial_search_strategy.py` |
| `skydiscover/search/adaevolve/` | Adaptive evolution with a unified archive + diversity scoring |
| `skydiscover/search/beam_search/` | Beam search over programs |
| `skydiscover/search/best_of_n/` | Sample N programs, keep the best |
| `skydiscover/search/topk/` | Keep top-k programs in database |
| `skydiscover/search/gepa_native/` | GEPA (Pareto-based) search |
| `skydiscover/search/openevolve_native/` | OpenEvolve-compatible backend |
| `skydiscover/search/claude_code/` | Claude Code agentic search |

#### Evox Utilities (`skydiscover/search/evox/utils/`)
| File | Purpose |
|---|---|
| `coevolve_logging.py` | Logs search algorithm generations and scores |
| `search_scorer.py` | `LogWindowScorer` — scores a search strategy by improvement over a window |
| `variation_operator_generator.py` | Generates LLM-based variation operators for search strategies |
| `template.py` | Template helpers for evox prompts |

#### Search Utilities (`skydiscover/search/utils/`)
| File | Purpose |
|---|---|
| `checkpoint_manager.py` | Save/load run checkpoints |
| `discovery_utils.py` | Misc helpers: `SerializableResult`, `load_database_from_file`, `build_image_content` |
| `logging_utils.py` | Search run logging setup |

### Context Builders (`skydiscover/context_builder/`)
Each builder constructs the prompt messages sent to the LLM.

| Directory | Builder |
|---|---|
| `default/` | `DefaultContextBuilder` — standard diff/full-rewrite/from-scratch prompts |
| `evox/` | `EvoxContextBuilder` — prompts for co-evolution (search strategy evolution) |
| `adaevolve/` | AdaEvolve-specific prompts |
| `gepa_native/` | GEPA-specific prompts |
| `base.py` | ABC for all context builders |
| `human_feedback.py` | Human-in-the-loop feedback injection |
| `utils.py` | Shared formatting helpers |

Each builder's `templates/` folder holds the `.txt` prompt templates it uses.

Key evox templates:
- `evox/templates/system_message.txt` — main system prompt for solution evolution
- `skydiscover/search/evox/config/evox_search_sys_prompt.txt` — system prompt for search strategy evolution

### Evaluation (`skydiscover/evaluation/`)
| File | Purpose |
|---|---|
| `evaluator.py` | Base evaluator + `create_evaluator()` factory |
| `container_evaluator.py` | Runs evaluation inside a Docker container |
| `harbor_evaluator.py` | Harbor-based evaluator |
| `llm_judge.py` | LLM-as-judge evaluator |
| `evaluation_result.py` | `EvaluationResult` dataclass |
| `wrapper.py` | Subprocess wrapper for user-defined `evaluate()` functions |

### LLM (`skydiscover/llm/`)
| File | Purpose |
|---|---|
| `base.py` | `LLMResponse` dataclass + base LLM interface |
| `openai.py` | OpenAI-compatible client (covers openai, gemini, anthropic, etc.) |
| `llm_pool.py` | `LLMPool` — manages parallel LLM calls across multiple API keys |
| `agentic_generator.py` | Agentic (tool-using) LLM generation |
| `responses_utils.py` | Parse streaming responses |

### Utilities (`skydiscover/utils/`)
| File | Purpose |
|---|---|
| `code_utils.py` | `extract_diffs`, `apply_diff`, `parse_full_rewrite`, `extract_solution_language` |
| `metrics.py` | `get_score`, `format_metrics` |
| `async_utils.py` | Async helpers |
| `prepare.py` | Setup helpers |

### Extras (`skydiscover/extras/`)
| File | Purpose |
|---|---|
| `monitor/` | Live dashboard: `server.py` serves `dashboard.html`, `callback.py` hooks into the search loop |
| `external/` | Backends for external frameworks (openevolve, shinkaevolve, gepa) |

---

## Configs (`configs/`)
Pre-built YAML configs for each search strategy:
- `default.yaml` — standard evolutionary search
- `evox.yaml` — co-evolution (evox)
- `adaevolve.yaml` — adaptive evolution
- `human_in_the_loop.yaml` — human feedback enabled
- `llm_judge.yaml` — LLM-as-judge evaluator
- `openevolve_native.yaml` — OpenEvolve backend

---

## Benchmarks (`benchmarks/`)
Each benchmark has a `config.yaml`, `initial_program.*`, and an `evaluator/` folder with `evaluator.py` + `wrapper.py`.

| Directory | Problem |
|---|---|
| `math/circle_packing/` | Pack circles in a unit square (main benchmark being worked on) |
| `math/circle_packing_rect/` | Circle packing in a rectangle |
| `math/erdos_min_overlap/` | Erdős minimum overlap problem |
| `math/first_autocorr_ineq/` | First autocorrelation inequality |
| `ADRS/cloudcast/` | Weather forecasting |
| `ADRS/eplb/` | Expert parallel load balancing |
| `ADRS/llm_sql/` | LLM-based SQL |
| `ADRS/txn_scheduling/` | Transaction scheduling |
| `ale_bench/` | AtCoder Heuristic Contest problems |
| `arc_benchmark/` | ARC-AGI tasks |
| `kernelbench/` | GPU kernel optimization |
| `gpu_mode/` | GPU benchmarks (grayscale, mla_decode, trimul, vecadd) |
| `frontier-cs-eval/` | Frontier CS evaluation |
| `image_gen/` | Image generation tasks |

---

## Tests (`tests/`)
| File/Directory | Tests |
|---|---|
| `conftest.py` | Shared fixtures |
| `test_smoke.py` | End-to-end smoke test |
| `test_llm_integration.py` | LLM API integration tests |
| `test_time_instrumentation.py` | Timing/profiling tests |
| `search/test_evox.py` | Evox co-evolution unit tests |
| `search/test_adaevolve_multiobjective.py` | AdaEvolve multi-objective tests |
| `evaluation/` | Evaluator unit tests |
| `config/` | Config loading tests |
| `cli/` | CLI tests |
