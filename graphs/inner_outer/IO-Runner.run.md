---
name: IO-Runner.run
description: method in skydiscover/runner.py (runner)
metadata:
  type: project
---

# Runner.run

**File:** `skydiscover/runner.py:108`  
**Kind:** method  
**Layer:** #runner

## What it does
Top-level entry point. Wires up the database, controller, and evaluator, then hands off to CoEvolutionController.run_discovery (or the appropriate controller for the config). Also sets up logging, monitoring, and checkpoint callbacks.

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
- [[IO-DiscoveryController.__init__]]
- [[IO-DiscoveryController.close]]
- [[IO-DiscoveryController.run_discovery]]
- [[IO-DiscoveryControllerInput.config]]
- [[IO-DiscoveryControllerInput.output_dir]]
- [[IO-Program.id]]
- [[IO-Program.metrics]]
- [[IO-Program.solution]]
- [[IO-ProgramDatabase.__init__]]
- [[IO-ProgramDatabase.log_status]]
- [[IO-Runner.__init__]]
- [[IO-Runner._add_initial_program]]
- [[IO-Runner._get_best_program]]
- [[IO-Runner._install_signal_handlers]]
- [[IO-Runner._load_checkpoint]]
- [[IO-Runner._push_existing_to_monitor]]
- [[IO-Runner._save_best_program]]
- [[IO-Runner._save_checkpoint]]
- [[IO-Runner._setup_human_feedback]]
- [[IO-Runner._setup_monitor_summary]]
- [[IO-Runner._start_monitor]]
- [[IO-Runner._sync_database]]
- [[IO-base_database.Program]]
- [[IO-default_discovery_controller.DiscoveryControllerInput]]
- [[IO-metrics.format_metrics]]
- [[IO-run.checkpoint_cb]]

## ← Called by
- [[IO-Runner._add_initial_program]]
- [[IO-Runner._push_existing_to_monitor]]
- [[IO-Runner._setup_human_feedback]]
- [[IO-Runner._start_monitor]]
- [[IO-_install_signal_handlers.on_signal]]
