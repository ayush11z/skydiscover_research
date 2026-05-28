---
name: api.run_discovery
description: function in skydiscover/api.py (api)
metadata:
  type: project
---

# api.run_discovery

**File:** `skydiscover/api.py:58`  
**Kind:** function  
**Layer:** #api

## Source
````python
def run_discovery(
    evaluator: Union[str, Path, Callable],
    initial_program: Optional[Union[str, Path, List[str]]] = None,
    model: Optional[str] = None,
    iterations: Optional[int] = None,
    search: Optional[str] = None,
    config: Union[str, Path, Config, None] = None,
    agentic: bool = False,
    output_dir: Optional[str] = None,
    system_prompt: Optional[str] = None,
    api_base: Optional[str] = None,
    cleanup: bool = True,
) -> DiscoveryResult:
    """Run a discovery process and return the best result.

    Args:
        evaluator: File path or callable (program_path) -> metrics_dict.
        initial_program: File path or inline source code (string / list of lines).
            Optional — when omitted the LLM generates a solution from scratch.
        model: Model name(s), comma-separated. e.g. "gpt-5" or "gpt-5,gemini/gemini-3-pro".
        iterations: Max iterations (overrides config).
        search: Algorithm name ("topk", "adaevolve", "evox", "openevolve_native", etc.).
        config: YAML path, Config object, or None for defaults.
        agentic: Enable agentic mode (codebase root derived from initial_program).
        output_dir: Where to write results (temp dir if None).
        system_prompt: Domain-specific context for the LLM.
        api_base: Base URL for an OpenAI-compatible API.
        cleanup: Remove temp files after the run.

    Returns:
        DiscoveryResult with best program, score, solution, metrics, and output directory.
    """
    return asyncio.run(
        _run_discovery_async(
            initial_program,
            evaluator,
            config,
            iterations=iterations,
            output_dir=output_dir,
            cleanup=cleanup,
            agentic=agentic,
            model=model,
            search=search,
            system_prompt=system_prompt,
            api_base=api_base,
        )
    )
````

## → Calls
- [[Runner.run]]
- [[TaskPool.run]]
- [[api.DiscoveryResult]]
- [[api._run_discovery_async]]
- [[config.Config]]
- [[gepa_backend.run]]
- [[openevolve_backend.run]]
- [[shinkaevolve_backend.run]]
- [[wrapper.run]]

## ← Called by
- [[Runner.run]]
- [[api.discover_solution]]
