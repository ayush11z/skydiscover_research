---
name: openevolve_backend.run
description: function in skydiscover/extras/external/openevolve_backend.py (external)
metadata:
  type: project
---

# openevolve_backend.run

**File:** `skydiscover/extras/external/openevolve_backend.py:169`  
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
    """Run evolution using the OpenEvolve package."""
    from openevolve.controller import OpenEvolve

    from skydiscover.api import DiscoveryResult
    from skydiscover.config import bridge_provider_env

    bridge_provider_env(config_obj)

    oe_config = _map_config(config_obj, iterations, output_dir)

    # Human feedback: set initial system prompt on feedback reader for dashboard visibility
    original_sys_prompt = ""
    if hasattr(oe_config, "prompt") and hasattr(oe_config.prompt, "system_message"):
        original_sys_prompt = oe_config.prompt.system_message or ""
    if feedback_reader and original_sys_prompt:
        feedback_reader.set_current_prompt(original_sys_prompt)

    controller = OpenEvolve(
        initial_program_path=program_path,
        evaluation_file=evaluator_path,
        config=oe_config,
        output_dir=output_dir,
    )

    # Monitor polling task + Human feedback injection
    seen_ids: set = set()
    poll_task = None

    if monitor_callback or feedback_reader:

        async def _poll_programs():
            _last_feedback = ""
            while True:
                await asyncio.sleep(2)
                # Poll new programs for monitor
                if monitor_callback:
                    try:
                        db = getattr(controller, "database", None)
                        if db is None:
                            continue
                        for pid, p in list(db.programs.items()):
                            if pid not in seen_ids:
                                seen_ids.add(pid)
                                sky_prog = _to_skydiscover_program(p)
                                monitor_callback(sky_prog, getattr(p, "iteration_found", 0))
                    except Exception:
                        logger.debug("Monitor poll error", exc_info=True)
                # Human feedback: inject feedback into OpenEvolve's config
                if feedback_reader:
                    try:
                        feedback = feedback_reader.read()
                        if feedback != _last_feedback:
                            _last_feedback = feedback
                            if feedback:
                                if feedback_reader.mode == "replace":
                                    new_prompt = feedback
                                else:
                                    new_prompt = (
                                        original_sys_prompt + "\n\n## Human Guidance\n" + feedback
                                    )
                            else:
                                new_prompt = original_sys_prompt
                            # Update OpenEvolve's prompt config and model configs
                            if hasattr(oe_config, "prompt"):
                                oe_config.prompt.system_message = new_prompt
                            for m in getattr(oe_config.llm, "models", []):
                                if hasattr(m, "system_message"):
                                    m.system_message = new_prompt
                            feedback_reader.set_current_prompt(new_prompt)
                            if feedback:
                                logger.info(
                                    f"Human feedback injected into OpenEvolve ({len(feedback)} chars, mode={feedback_reader.mode})"
                                )
                    except Exception:
                        logger.debug("Human feedback injection error", exc_info=True)

        poll_task = asyncio.create_task(_poll_programs())

    best = await controller.run(iterations=iterations)

    if poll_task:
        poll_task.cancel()
        # Flush remaining programs
        db = getattr(controller, "database", None)
        if db:
            for pid, p in db.programs.items():
                if pid not in seen_ids:
                    seen_ids.add(pid)
                    try:
                        monitor_callback(
                            _to_skydiscover_program(p), getattr(p, "iteration_found", 0)
                        )
                    except Exception:
                        logger.debug("Monitor flush error", exc_info=True)

    # Extract results from the OpenEvolve database
    programs = getattr(controller, "database", None)
    programs_dict = programs.programs if programs else {}

    initial_score = _get_initial_score(programs_dict)

    best_skydiscover = _to_skydiscover_program(best) if best else None
    best_score = _score_of(best.metrics) if best else 0.0

    return DiscoveryResult(
        best_program=best_skydiscover,
        best_score=best_score or 0.0,
        best_solution=best.code if best else "",
        metrics=(best.metrics or {}) if best else {},
        output_dir=output_dir,
        initial_score=initial_score,
    )
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[ContainerizedEvaluator.__init__]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[Evaluator.__init__]]
- [[HumanFeedbackReader.__init__]]
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
- [[ProgramDatabase.__init__]]
- [[Runner.__init__]]
- [[Runner.run]]
- [[SerializableResult.prompt]]
- [[TaskPool.__init__]]
- [[TaskPool.create_task]]
- [[TaskPool.run]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[_FinalResult.__init__]]
- [[api.DiscoveryResult]]
- [[config.Config]]
- [[config.bridge_provider_env]]
- [[gepa_backend.run]]
- [[openevolve_backend._get_initial_score]]
- [[openevolve_backend._map_config]]
- [[openevolve_backend._score_of]]
- [[openevolve_backend._to_skydiscover_program]]
- [[openevolve_backend.run._poll_programs]]
- [[shinkaevolve_backend.run]]
- [[wrapper.run]]

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
- [[shinkaevolve_backend.run]]
- [[variation_operator_generator.get_available_packages]]
- [[variation_operator_generator.main]]
