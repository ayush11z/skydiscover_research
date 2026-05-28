---
name: gepa_backend.run
description: function in skydiscover/extras/external/gepa_backend.py (external)
metadata:
  type: project
---

# gepa_backend.run

**File:** `skydiscover/extras/external/gepa_backend.py:197`  
**Kind:** function  
**Layer:** #external

## Source
````python
async def run(
    program_path: str,
    evaluator_path: str,
    config_obj: Config,
    iterations: int,
    output_dir: str,
    monitor_callback=None,
    feedback_reader=None,
) -> DiscoveryResult:
    """Run evolution using GEPA's optimize_anything API."""
    from gepa.optimize_anything import optimize_anything

    from skydiscover.api import DiscoveryResult
    from skydiscover.config import bridge_provider_env
    from skydiscover.search.base_database import Program

    bridge_provider_env(config_obj)
    _ensure_litellm_api_key(config_obj)

    with open(program_path, "r") as f:
        seed_solution = f.read()

    # Handle EVOLVE-BLOCK markers: GEPA replaces the entire candidate text,
    # so if the program has code outside the markers we need to split it and
    # only evolve the block, reconstructing the full file for evaluation.
    _START_TAG = "# EVOLVE-BLOCK-START"
    _END_TAG = "# EVOLVE-BLOCK-END"
    prefix = ""
    suffix = ""
    if _START_TAG in seed_solution and _END_TAG in seed_solution:
        start_idx = seed_solution.index(_START_TAG)
        end_idx = seed_solution.index(_END_TAG) + len(_END_TAG)
        prefix = seed_solution[:start_idx]
        suffix = seed_solution[end_idx:]
        seed_solution = seed_solution[start_idx:end_idx]

    # Build evaluator adapter
    evaluator = _make_gepa_evaluator(
        evaluator_path,
        monitor_callback=monitor_callback,
        solution_prefix=prefix,
        solution_suffix=suffix,
    )

    # Build GEPA config
    gepa_config = _build_gepa_config(config_obj, iterations)

    # Extract system prompt for domain context
    system_prompt = config_obj.system_prompt_override
    if system_prompt is None and hasattr(config_obj, "context_builder"):
        sp = config_obj.context_builder.system_message
        # Only use it if it's actual text, not a template name
        if sp and sp not in ("system_message", "evaluator_system_message"):
            system_prompt = sp

    # Human feedback: apply any pending feedback to the system prompt and set for dashboard
    if feedback_reader:
        if system_prompt:
            feedback_reader.set_current_prompt(system_prompt)
        feedback = feedback_reader.read()
        if feedback:
            if feedback_reader.mode == "replace":
                system_prompt = feedback
            else:
                system_prompt = (system_prompt or "") + "\n\n## Human Guidance\n" + feedback
            feedback_reader.set_current_prompt(system_prompt)
            logger.info(
                f"Human feedback applied to GEPA background ({len(feedback)} chars, mode={feedback_reader.mode})"
            )
            logger.info("Note: GEPA runs synchronously; feedback is applied once at startup.")

    # Log to file so screen output is captured
    log_dir = os.path.join(output_dir, "logs")
    os.makedirs(log_dir, exist_ok=True)
    from datetime import datetime

    log_file = os.path.join(log_dir, f"gepa_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )
    logging.getLogger().addHandler(file_handler)

    # Run GEPA — optimize_anything is synchronous
    try:
        result = optimize_anything(
            seed_candidate=seed_solution,
            evaluator=evaluator,
            objective="Evolve the solution to maximise the combined_score metric.",
            background=system_prompt,
            config=gepa_config,
        )
    finally:
        logging.getLogger().removeHandler(file_handler)
        file_handler.close()

    # Extract results — reconstruct full file if we split on EVOLVE markers
    best_block = (
        result.best_candidate
        if isinstance(result.best_candidate, str)
        else str(result.best_candidate)
    )
    best_solution = prefix + best_block + suffix
    best_score = result.val_aggregate_scores[result.best_idx]
    scores = result.val_aggregate_scores
    initial_score = scores[0] if scores else 0.0

    best_program = Program(
        id=str(uuid.uuid4()),
        solution=best_solution,
        language=getattr(config_obj, "language", None) or "python",
        metrics={"combined_score": best_score},
        iteration_found=result.best_idx,
        generation=result.best_idx,
    )

    # Save best program and info to output dir
    import json

    best_dir = os.path.join(output_dir, "best")
    os.makedirs(best_dir, exist_ok=True)
    with open(os.path.join(best_dir, "best_program.py"), "w") as f:
        f.write(best_solution)
    with open(os.path.join(best_dir, "best_program_info.json"), "w") as f:
        json.dump(
            {
                "id": best_program.id,
                "iteration": result.best_idx,
                "best_score": best_score,
                "initial_score": initial_score,
                "total_candidates": result.num_candidates,
            },
            f,
            indent=2,
        )

    return DiscoveryResult(
        best_program=best_program,
        best_score=best_score,
        best_solution=best_solution,
        metrics={"combined_score": best_score, "total_candidates": result.num_candidates},
        output_dir=output_dir,
        initial_score=initial_score,
    )
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[Config.context_builder]]
- [[Config.system_prompt_override]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[ContainerizedEvaluator.__init__]]
- [[ContainerizedEvaluator.close]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[DiscoveryController.close]]
- [[Evaluator.__init__]]
- [[Evaluator.close]]
- [[HumanFeedbackReader.__init__]]
- [[HumanFeedbackReader.read]]
- [[HumanFeedbackReader.set_current_prompt]]
- [[HybridDiversity.__init__]]
- [[LLMJudge.__init__]]
- [[LLMPool.__init__]]
- [[LangFuseTracer.__init__]]
- [[LogWindowScorer.__init__]]
- [[MetricDiversity.__init__]]
- [[MonitorServer.__init__]]
- [[OpenAILLM.__init__]]
- [[ParadigmGenerator.__init__]]
- [[Program.id]]
- [[ProgramDatabase.__init__]]
- [[Runner.__init__]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[_FinalResult.__init__]]
- [[api.DiscoveryResult]]
- [[base_database.Program]]
- [[config.Config]]
- [[config.bridge_provider_env]]
- [[gepa_backend._build_gepa_config]]
- [[gepa_backend._ensure_litellm_api_key]]
- [[gepa_backend._make_gepa_evaluator]]

## ← Called by
- [[ClaudeCodeController._ensure_image_built]]
- [[ClaudeCodeController._save_evaluator_image]]
- [[ClaudeCodeController.run_discovery]]
- [[ContainerizedEvaluator._build_image]]
- [[ContainerizedEvaluator._inject_file]]
- [[ContainerizedEvaluator._remove_file]]
- [[ContainerizedEvaluator._run_single_in_container]]
- [[ContainerizedEvaluator._start_container]]
- [[ContainerizedEvaluator.close]]
- [[HarborEvaluator._build_image]]
- [[HarborEvaluator._exec]]
- [[HarborEvaluator._init_container]]
- [[HarborEvaluator._read_reward]]
- [[HarborEvaluator._run_container]]
- [[api.run_discovery]]
- [[builder.run_async_safely]]
- [[cli.main]]
- [[openevolve_backend.run]]
- [[shinkaevolve_backend.run]]
- [[variation_operator_generator.get_available_packages]]
- [[variation_operator_generator.main]]
