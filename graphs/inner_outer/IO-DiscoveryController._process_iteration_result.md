---
name: IO-DiscoveryController._process_iteration_result
description: method in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# DiscoveryController._process_iteration_result

**File:** `skydiscover/search/default_discovery_controller.py:928`  
**Kind:** method  
**Layer:** #inner-loop

## Source
````python
    def _process_iteration_result(
        self,
        result: Any,
        iteration: int,
        checkpoint_callback: Optional[Callable[[int], None]] = None,
        verbose: bool = True,
    ) -> None:
        """
        Process the result from a single iteration.

        Args:
            result: The iteration result to process.
            iteration: Current iteration number.
            checkpoint_callback: Optional callback for checkpoint intervals.
            verbose: If True, log progress and metrics; if False, suppress logging.
        """
        if result.error:
            if verbose:
                logger.warning(f"Iteration {iteration} failed: {result.error}")
            return

        program_class = getattr(self.database, "_program_class", Program)
        child_program = program_class(**result.child_program_dict)

        self.database.add(child_program, iteration=iteration)

        # Fire monitor callback (live dashboard)
        if self.monitor_callback:
            try:
                self.monitor_callback(child_program, iteration)
            except Exception:
                logger.debug("Monitor callback error", exc_info=True)

        if result.prompt:
            self.database.log_prompt(
                template_key=(
                    "full_rewrite_user_message"
                    if not self.config.diff_based_generation
                    else "diff_user_message"
                ),
                program_id=child_program.id,
                prompt=result.prompt,
                responses=[result.llm_response] if result.llm_response else [],
            )

        if verbose:
            logger.info(
                f"Iteration {iteration}: "
                f"Program {child_program.id} "
                f"(parent: {result.parent_id}) "
                f"completed in {result.iteration_time:.2f}s"
                f" (llm: {result.llm_generation_time:.2f}s,"
                f" eval: {result.eval_time:.2f}s)"
            )

        if iteration > 0 and iteration % self.config.checkpoint_interval == 0:
            if verbose:
                logger.info(f"[CHECKPOINT] Checkpoint interval reached at iteration {iteration}")

            self.database.log_status()
            if checkpoint_callback:
                checkpoint_callback(iteration)

        if child_program.metrics:
            if verbose:
                metrics_str = ", ".join(
                    f"{k}={v:.4f}" if isinstance(v, (int, float)) else f"{k}={v}"
                    for k, v in child_program.metrics.items()
                )
                logger.info(f"Metrics: {metrics_str}")

            if not hasattr(self, "_warned_about_combined_score"):
                self._warned_about_combined_score = False

            if (
                "combined_score" not in child_program.metrics
                and not self._warned_about_combined_score
            ):
                if verbose:
                    logger.warning(
                        "⚠️  No 'combined_score' metric found in evaluation results. "
                        "Using 0.0 for discovery process guidance. "
                        "For better solution discovery results, please modify your evaluator to return a 'combined_score' "
                        "metric that properly weights different aspects of program performance."
                    )
                self._warned_about_combined_score = True

        if self.database.best_program_id == child_program.id and verbose:
            logger.info(f"🌟 New best solution found at iteration {iteration}")
````

## → Calls
- [[IO-DiscoveryControllerInput.database]]
- [[IO-Program.parent_id]]
- [[IO-ProgramDatabase.add]]
- [[IO-ProgramDatabase.log_prompt]]
- [[IO-ProgramDatabase.log_status]]
- [[IO-base_database.Program]]

## ← Called by
- [[IO-CoEvolutionController.run_discovery]]
- [[IO-DiscoveryController._run_discovery_sequential]]
- [[IO-DiscoveryController.postprocess_result]]
- [[IO-_run_discovery_parallel._bounded_iteration]]
