---
name: shinkaevolve_backend.run
description: function in skydiscover/extras/external/shinkaevolve_backend.py (external)
metadata:
  type: project
---

# shinkaevolve_backend.run

**File:** `skydiscover/extras/external/shinkaevolve_backend.py:152`  
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
    """Run evolution using the ShinkaEvolve package."""
    from shinka.core import AsyncEvolutionRunner

    from skydiscover.api import DiscoveryResult
    from skydiscover.config import bridge_provider_env

    bridge_provider_env(config_obj)

    evo_config, job_config, db_config = _map_config(
        config_obj,
        iterations,
        evaluator_path,
        output_dir,
    )

    # Human feedback: set initial system prompt on feedback reader for dashboard visibility
    if feedback_reader and evo_config.task_sys_msg:
        feedback_reader.set_current_prompt(evo_config.task_sys_msg)

    # ShinkaEvolve supports passing code as strings directly
    with open(program_path, "r") as f:
        init_str = f.read()
    with open(evaluator_path, "r") as f:
        eval_str = f.read()

    # ShinkaEvolve runs the evaluator as a CLI subprocess:
    #   python evaluate.py --program_path X --results_dir Y
    # and expects results written to results_dir/metrics.json.
    # SkyDiscover evaluators are just a function: evaluate(path) -> dict.
    # Bridge the gap by appending a CLI wrapper.
    if "__main__" not in eval_str:
        eval_str += """

if __name__ == "__main__":
    import argparse, json, os
    parser = argparse.ArgumentParser()
    parser.add_argument("--program_path", required=True)
    parser.add_argument("--results_dir", required=True)
    args = parser.parse_args()
    os.makedirs(args.results_dir, exist_ok=True)
    result = evaluate(args.program_path)
    with open(os.path.join(args.results_dir, "metrics.json"), "w") as f:
        json.dump(result, f)
"""

    runner = AsyncEvolutionRunner(
        evo_config=evo_config,
        job_config=job_config,
        db_config=db_config,
        init_program_str=init_str,
        evaluate_str=eval_str,
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
                        all_progs = runner.db.get_all_programs()
                        for p in all_progs:
                            if p.id not in seen_ids:
                                seen_ids.add(p.id)
                                sky_prog = _to_skydiscover_program(p)
                                monitor_callback(sky_prog, getattr(p, "generation", 0))
                    except Exception:
                        logger.debug("Monitor poll error", exc_info=True)
                # Human feedback: inject feedback into ShinkaEvolve's prompt sampler
                if feedback_reader:
                    try:
                        feedback = feedback_reader.read()
                        if feedback != _last_feedback:
                            _last_feedback = feedback
                            sampler = getattr(runner, "prompt_sampler", None)
                            original_prompt = evo_config.task_sys_msg or ""
                            if feedback and sampler:
                                if feedback_reader.mode == "replace":
                                    sampler.task_sys_msg = feedback
                                else:
                                    sampler.task_sys_msg = (
                                        original_prompt + "\n\n## Human Guidance\n" + feedback
                                    )
                                feedback_reader.set_current_prompt(sampler.task_sys_msg)
                                logger.info(
                                    f"Human feedback injected into ShinkaEvolve ({len(feedback)} chars, mode={feedback_reader.mode})"
                                )
                            elif sampler and not feedback:
                                # Feedback cleared — revert to original
                                sampler.task_sys_msg = original_prompt
                                feedback_reader.set_current_prompt(original_prompt)
                    except Exception:
                        logger.debug("Human feedback injection error", exc_info=True)

        poll_task = asyncio.create_task(_poll_programs())

    await runner.run()

    if poll_task:
        poll_task.cancel()
        # Flush remaining programs
        try:
            for p in runner.db.get_all_programs():
                if p.id not in seen_ids:
                    seen_ids.add(p.id)
                    try:
                        monitor_callback(_to_skydiscover_program(p), getattr(p, "generation", 0))
                    except Exception:
                        logger.debug("Monitor flush error", exc_info=True)
        except Exception:
            logger.debug("Final program flush error", exc_info=True)

    # Extract results from the ShinkaEvolve database
    best_sp = runner.db.get_best_program()
    all_programs = runner.db.get_all_programs()

    # get_best_program() only returns "correct" programs. For continuous-score
    # problems (no pass/fail), fall back to the highest-scoring program overall.
    if best_sp is None and all_programs:
        best_sp = max(all_programs, key=lambda p: float(getattr(p, "combined_score", 0) or 0))

    initial_score = _get_initial_score(all_programs)

    best_skydiscover = _to_skydiscover_program(best_sp) if best_sp else None
    best_score = float(best_sp.combined_score or 0.0) if best_sp else 0.0

    return DiscoveryResult(
        best_program=best_skydiscover,
        best_score=best_score,
        best_solution=best_sp.code if best_sp else "",
        metrics=best_skydiscover.metrics if best_skydiscover else {},
        output_dir=output_dir,
        initial_score=initial_score,
    )
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
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
- [[Program.id]]
- [[ProgramDatabase.__init__]]
- [[Runner.__init__]]
- [[Runner.run]]
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
- [[openevolve_backend.run]]
- [[shinkaevolve_backend._get_initial_score]]
- [[shinkaevolve_backend._map_config]]
- [[shinkaevolve_backend._to_skydiscover_program]]
- [[shinkaevolve_backend.run._poll_programs]]
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
- [[openevolve_backend.run]]
- [[variation_operator_generator.get_available_packages]]
- [[variation_operator_generator.main]]
