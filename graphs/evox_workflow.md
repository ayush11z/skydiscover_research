# EvoX Co-Evolution Workflow

Rendered call-graph (open in Obsidian):
![[evox_callgraph.svg]]

---

## Runtime Flow

```mermaid
flowchart TD
    %% ── Startup ─────────────────────────────────────────────────────────
    subgraph Startup["🚀 Startup (once)"]
        A[Runner.run] --> B[_load_initial_program]
        A --> C[_add_initial_program\nDB.add  score = 0]
        A --> D[_generate_variation_operators\nouter LLM: qwen2.5-coder:14b]
    end

    %% ── Inner Loop ───────────────────────────────────────────────────────
    subgraph Inner["🔁 Inner Loop  — gemma3:12b"]
        E[run_discovery] --> F[_run_iteration]
        F --> G[ProgramDatabase.sample\npick parents]
        F --> H[_build_prompt\nContextBuilder]
        F --> I[_call_llm\nLLMPool.generate]
        I --> J[OpenAILLM._generate_text\n_call_api → Ollama]
        J -->|latency + tokens| K[LangFuseTracer.log_generation]
        F --> L[_parse_llm_response\nextract diff / full rewrite]
        F --> M[evaluate_program\nsubprocess evaluator.py]
        F --> N[ProgramDatabase.add\nif improved]
        F --> O[LogWindowScorer.record_step]
    end

    %% ── Stagnation Gate ─────────────────────────────────────────────────
    subgraph Stagnation["⏸ Stagnation Gate"]
        P{_should_evolve_search\nstagnant_count ≥ switch_interval?}
    end

    %% ── Outer Loop ───────────────────────────────────────────────────────
    subgraph Outer["🔄 Outer Loop  — qwen2.5-coder:14b"]
        Q[_evolve_search] --> R[_finalize_pending_search\nscore the previous strategy]
        R --> S[_assign_search_score\nLogWindowScorer.get_score]
        Q --> T[_generate_and_validate_search_algorithm\nsearch_controller._run_iteration\nouter LLM generates new search alg]
        T --> U[_switch_to_new_search_algorithm\nreplace variation ops]
        U --> V[LogWindowScorer.reset_window]
    end

    %% ── Connections ──────────────────────────────────────────────────────
    A --> E
    O --> P
    P -- yes --> Q
    P -- no  --> F
    Q --> F
```

---

## Key Data Flows

| Signal | From | To | Meaning |
|---|---|---|---|
| `score` | `evaluate_program` | `ProgramDatabase.add` | Fitness of new program |
| `stagnant_count` | `LogWindowScorer` | `_should_evolve_search` | Iterations without improvement |
| `search_algorithm` | outer LLM | `_switch_to_new_search_algorithm` | New variation operators / sampling strategy |
| `loop_type + iteration` | `set_llm_context()` | `LangFuseTracer.log_generation` | Tags LangFuse trace as inner / outer |

## File Map

| Component | File |
|---|---|
| Entry point | `skydiscover/runner.py` |
| Inner-loop controller | `skydiscover/search/default_discovery_controller.py` |
| Co-evolution controller | `skydiscover/search/evox/controller.py` |
| Stagnation scorer | `skydiscover/search/evox/utils/search_scorer.py` |
| Variation operator gen | `skydiscover/search/evox/utils/variation_operator_generator.py` |
| LLM pool | `skydiscover/llm/llm_pool.py` |
| OpenAI-compat client | `skydiscover/llm/openai.py` |
| LangFuse tracing | `skydiscover/llm/langfuse_tracer.py` |
| Program database ABC | `skydiscover/search/base_database.py` |
