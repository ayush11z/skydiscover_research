---
name: Runner.run
description: method in skydiscover/runner.py (runner)
metadata:
  type: project
---

# Runner.run

**File:** `skydiscover/runner.py:108`  
**Kind:** method  
**Layer:** #runner

## What it does
Top-level entry point. Wires up the database, controller, and evaluator, then hands off to [[CoEvolutionController.run_discovery]] (or the appropriate controller for the config). Also sets up logging, monitoring, and checkpoint callbacks.

## Source
````python
    async def run(
        self,
        iterations: Optional[int] = None,
        checkpoint_path: Optional[str] = None,
    ) -> Optional[Program]:
        """Entrypoint for the discovery process.

        Args:
            iterations: max iterations (uses config.max_iterations if None).
            checkpoint_path: resume from this checkpoint directory if provided.

        Returns:
            Best Program found, or None if no valid programs were produced.
        """
        max_iterations = iterations if iterations is not None else self.config.max_iterations

        start_iteration = 0
        if checkpoint_path and os.path.exists(checkpoint_path):
            self._load_checkpoint(checkpoint_path)
            start_iteration = self.database.last_iteration + 1
            logger.info(f"Resuming from iteration {start_iteration}")
        else:
            start_iteration = self.database.last_iteration

        # Create the discovery controller input
        controller_input = DiscoveryControllerInput(
            config=self.config,
            evaluation_file=self.evaluation_file,
            database=self.database,
            file_suffix=self.config.file_suffix,
            output_dir=self.output_dir,
            evaluator_env_vars=self.evaluator_env_vars,
        )

        # Get the discovery controller
        self.discovery_controller = get_discovery_controller(controller_input)

        # Add initial program to database if not resuming
        should_add_initial = (
            start_iteration == 0
            and len(self.database.programs) == 0
            and self.initial_program_solution is not None
        )

        if should_add_initial:
            await self._add_initial_program(start_iteration)
        else:
            logger.info(
                f"Resuming from iteration {start_iteration} with {len(self.database.programs)} programs"
            )

        # Start the monitor
        monitor_server = None
        try:
            monitor_server = self._start_monitor(max_iterations)
            self._setup_human_feedback(monitor_server)
            self._setup_monitor_summary(monitor_server)
            self._push_existing_to_monitor()
            self._install_signal_handlers()

            discovery_start = start_iteration + 1 if should_add_initial else start_iteration
            self.database.log_status()

            def checkpoint_cb(iteration: int) -> None:
                self._sync_database()
                self._save_checkpoint(iteration)

            # MAIN LOOP: Run the discovery
            await self.discovery_controller.run_discovery(
                discovery_start,
                max_iterations,
                checkpoint_callback=checkpoint_cb,
            )

            self._sync_database()
            final_iteration = discovery_start + max_iterations - 1
            if final_iteration > 0:
                self._save_checkpoint(final_iteration)

            # Re-evaluate best program in test mode (authoritative score).
            best = self._get_best_program()
            if best:
                try:
                    test_result = await self.discovery_controller.evaluator.evaluate_program(
                        best.solution, best.id, mode="test"
                    )
                    for k, v in test_result.metrics.items():
                        best.metrics[f"test_{k}"] = v
                    logger.info(
                        f"Test evaluation for best program: {format_metrics(test_result.metrics)}"
                    )
                    # Persist test metrics to disk so they survive the run.
                    self._save_best_program(best)
                except Exception as e:
                    logger.warning(f"Test-mode re-evaluation failed: {e}")

        finally:
            # Stop the monitor
            early_stopped = (
                self.discovery_controller is not None
                and self.discovery_controller.early_stopping_triggered
            )
            if self.discovery_controller is not None:
                self.discovery_controller.close()
            self.discovery_controller = None

            if monitor_server:
                try:
                    reason = "early_stopping" if early_stopped else "completed"
                    monitor_server.push_event({"type": "discovery_complete", "reason": reason})
                    time.sleep(0.5)
                    monitor_server.stop()
                except Exception:
                    logger.debug("Failed to stop monitor server", exc_info=True)

        # Get the best program
        best_program = self._get_best_program()
        if best_program:
            status = "early stopping" if early_stopped else "completed"
            logger.info(f"Discovery {status}. Best: {format_metrics(best_program.metrics)}")
            self._save_best_program(best_program)
            return best_program

        logger.warning("No valid programs found")
        return None
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[Config.evaluator]]
- [[ContainerizedEvaluator.__init__]]
- [[ContainerizedEvaluator.close]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[DiscoveryController.close]]
- [[DiscoveryController.run_discovery]]
- [[DiscoveryControllerInput.config]]
- [[DiscoveryControllerInput.output_dir]]
- [[DiscoveryResult.output_dir]]
- [[EvaluationResult.metrics]]
- [[Evaluator.__init__]]
- [[Evaluator.close]]
- [[HumanFeedbackReader.__init__]]
- [[HybridDiversity.__init__]]
- [[LLMJudge.__init__]]
- [[LLMPool.__init__]]
- [[LangFuseTracer.__init__]]
- [[LogWindowScorer.__init__]]
- [[MetricDiversity.__init__]]
- [[MonitorServer.__init__]]
- [[MonitorServer.push_event]]
- [[MonitorServer.stop]]
- [[OpenAILLM.__init__]]
- [[ParadigmGenerator.__init__]]
- [[Program.id]]
- [[Program.metrics]]
- [[Program.solution]]
- [[ProgramDatabase.__init__]]
- [[ProgramDatabase.log_status]]
- [[Runner.__init__]]
- [[Runner._add_initial_program]]
- [[Runner._get_best_program]]
- [[Runner._install_signal_handlers]]
- [[Runner._load_checkpoint]]
- [[Runner._push_existing_to_monitor]]
- [[Runner._save_best_program]]
- [[Runner._save_checkpoint]]
- [[Runner._setup_human_feedback]]
- [[Runner._setup_monitor_summary]]
- [[Runner._start_monitor]]
- [[Runner._sync_database]]
- [[SearchConfig.output_dir]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[_FinalResult.__init__]]
- [[api.run_discovery]]
- [[base_database.Program]]
- [[default_discovery_controller.DiscoveryControllerInput]]
- [[metrics.format_metrics]]
- [[registry.create_database]]
- [[route.get_discovery_controller]]
- [[run.checkpoint_cb]]

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
- [[Runner._add_initial_program]]
- [[Runner._push_existing_to_monitor]]
- [[Runner._setup_human_feedback]]
- [[Runner._start_monitor]]
- [[_install_signal_handlers.on_signal]]
- [[api._run_discovery_async]]
- [[api.run_discovery]]
- [[builder.run_async_safely]]
- [[cli.main]]
- [[cli.main_async]]
- [[openevolve_backend.run]]
- [[shinkaevolve_backend.run]]
- [[variation_operator_generator.get_available_packages]]
- [[variation_operator_generator.main]]
