---
name: shinkaevolve_backend._map_config
description: function in skydiscover/extras/external/shinkaevolve_backend.py (external)
metadata:
  type: project
---

# shinkaevolve_backend._map_config

**File:** `skydiscover/extras/external/shinkaevolve_backend.py:23`  
**Kind:** function  
**Layer:** #external

## Source
````python
def _map_config(config: Config, iterations: Optional[int], evaluator_path: str, output_dir: str):
    """Convert SkyDiscover Config to ShinkaEvolve's three config objects."""
    from dataclasses import fields as dc_fields

    from shinka.core.runner import EvolutionConfig
    from shinka.database import DatabaseConfig as ShinkaDBC
    from shinka.launch import LocalJobConfig

    # Power-user escape hatch
    ext = getattr(config, "external_config", None)
    if ext is not None and isinstance(ext, dict):
        evo = ext.get("evo_config", EvolutionConfig())
        job = ext.get("job_config", LocalJobConfig(eval_program_path=evaluator_path))
        dbc = ext.get("db_config", ShinkaDBC())
        if iterations is not None:
            evo.num_generations = iterations
        return evo, job, dbc

    # Load tuned backend defaults
    from skydiscover.extras.external.defaults import load_defaults

    defaults = load_defaults("shinkaevolve_default.yaml")
    evo_defaults = defaults.get("evolution", {})
    db_defaults = defaults.get("database", {})

    # EvolutionConfig
    evo_kwargs: Dict[str, Any] = {
        "num_generations": iterations or config.max_iterations,
        "results_dir": output_dir,
        "job_type": "local",
        "language": getattr(config, "language", None) or "python",
    }

    # Map LLM model names (from --model / -c config)
    if config.llm.models:
        evo_kwargs["llm_models"] = [m.name for m in config.llm.models]

    # Apply tuned defaults for evolution (patch types, LLM kwargs, meta, etc.)
    valid_evo_fields = {f.name for f in dc_fields(EvolutionConfig)}
    for key, value in evo_defaults.items():
        if key in valid_evo_fields and key not in evo_kwargs:
            evo_kwargs[key] = value

    # Cap parallelism to iteration count to avoid over-submission when
    # target generations is small (ShinkaEvolve auto-scales proposal jobs
    # from max_parallel_jobs; too many slots for few generations causes
    # directory collisions and stuck detection).
    iters = evo_kwargs["num_generations"]
    if "max_parallel_jobs" in evo_kwargs and iters < evo_kwargs["max_parallel_jobs"]:
        evo_kwargs["max_parallel_jobs"] = max(1, iters)

    # Meta model follows the main model
    if config.llm.models and evo_defaults.get("meta_rec_interval"):
        evo_kwargs["meta_llm_models"] = [config.llm.models[0].name]

    # System prompt -> task_sys_msg
    sys_prompt = config.system_prompt_override
    if sys_prompt is None and hasattr(config, "context_builder"):
        sp = config.context_builder.system_message
        if sp and sp not in ("system_message", "evaluator_system_message"):
            sys_prompt = sp
    if sys_prompt:
        evo_kwargs["task_sys_msg"] = sys_prompt

    evo = EvolutionConfig(**evo_kwargs)

    # --- JobConfig ---
    job_kwargs: Dict[str, Any] = {"eval_program_path": evaluator_path}
    if hasattr(config, "evaluator") and config.evaluator.timeout:
        secs = int(config.evaluator.timeout)
        h, m, s = secs // 3600, (secs % 3600) // 60, secs % 60
        job_kwargs["time"] = f"{h:02d}:{m:02d}:{s:02d}"
    job = LocalJobConfig(**job_kwargs)

    # --- DatabaseConfig ---
    valid_db_fields = {f.name for f in dc_fields(ShinkaDBC)}
    dbc_kwargs = {k: v for k, v in db_defaults.items() if k in valid_db_fields}
    dbc = ShinkaDBC(**dbc_kwargs)

    return evo, job, dbc
````

## → Calls
- [[BenchmarkConfig.name]]
- [[Config.context_builder]]
- [[Config.evaluator]]
- [[Config.llm]]
- [[Config.max_iterations]]
- [[Config.system_prompt_override]]
- [[LLMModelConfig.name]]
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[config.Config]]
- [[config.DatabaseConfig]]
- [[defaults.load_defaults]]

## ← Called by
- [[shinkaevolve_backend.run]]
- [[shinkaevolve_backend.run._poll_programs]]
