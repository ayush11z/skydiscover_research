---
name: CoEvolutionController.run_discovery
description: method in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# CoEvolutionController.run_discovery

**File:** `skydiscover/search/evox/controller.py:107`  
**Kind:** method  
**Layer:** #outer-loop

## What it does
Main co-evolution loop. For each solution iteration:
1. Runs one inner-loop step via [[DiscoveryController._run_iteration]]
2. Records progress via [[LogWindowScorer.record_step]]
3. Checks stagnation via [[CoEvolutionController._should_evolve_search]]
4. If stagnant → triggers [[CoEvolutionController._evolve_search]]

Also calls [[CoEvolutionController._generate_variation_operators]] once at startup.

## Source
````python
    async def run_discovery(
        self,
        start_iteration: int,
        max_iterations: int,
        checkpoint_callback=None,
        post_process_result: Optional[bool] = True,
    ):
        """Run co-evolution of solution programs and search algorithms."""
        self.total_solution_iterations = start_iteration + max_iterations
        self._max_solution_iterations = max_iterations

        if self._switch_interval is None:
            self._switch_interval = max(1, int(max_iterations * self.DEFAULT_SWITCH_RATIO))
            logger.info(f"Switch if {self._switch_interval} iterations of stagnation detected")

        self.start_db_stats = self.database.get_statistics(
            improvement_threshold=self.DEFAULT_IMPROVEMENT_THRESHOLD
        )

        # Set up search window and labels
        self._reset_search_window()

        # Generate variation labels for the search algorithm
        await self._generate_variation_operators()

        # Run co-evolution
        iteration = start_iteration
        while iteration < self.total_solution_iterations:
            if self.shutdown_event.is_set():
                logger.info("Shutdown requested")
                break

            try:
                # Run solution iteration
                result = await self._run_iteration(iteration, retry_times=3)
                attempts_used = getattr(result, "attempts_used", 1)

                if result.error:
                    logger.warning(
                        f"Iteration {iteration} failed (used {attempts_used} attempts): {result.error}"
                    )
                    # Database error after a switch: fall back and retry
                    if self._fallback_database is not None and result.prompt is None:
                        self._restore_fallback_database()
                        continue  # Retry same iteration with restored database
                else:
                    self._process_iteration_result(result, iteration, checkpoint_callback)

                for _ in range(attempts_used):
                    self._record_search_window_step()

                completed_solution_iter = iteration
                iteration += attempts_used

                # Co-evolve search strategy if needed (skip on final iteration)
                if iteration < self.total_solution_iterations and self._should_evolve_search():
                    logger.info(
                        f"Stagnation detected -> evolving search strategy (solution_iter={completed_solution_iter})"
                    )
                    await self._evolve_search(completed_solution_iter)

            except Exception as e:
                logger.error(f"Error in iteration {iteration}: {e}", exc_info=True)
                # Exception from database.add() after a switch: fall back and retry
                if self._fallback_database is not None:
                    self._restore_fallback_database()
                    continue  # Retry same iteration
                iteration += 1  # Normal error — advance

        if self._pending_search_result:
            await self._finalize_pending_search()

        logger.info(f"[SOLUTION EVOLUTION] Evolution completed: {self.database.name}")
        return self.database.get_best_program()
````

## → Calls
- [[BenchmarkConfig.name]]
- [[CoEvolutionController._evolve_search]]
- [[CoEvolutionController._finalize_pending_search]]
- [[CoEvolutionController._generate_variation_operators]]
- [[CoEvolutionController._record_search_window_step]]
- [[CoEvolutionController._reset_search_window]]
- [[CoEvolutionController._restore_fallback_database]]
- [[CoEvolutionController._should_evolve_search]]
- [[DiscoveryController._process_iteration_result]]
- [[DiscoveryController._run_iteration]]
- [[DiscoveryControllerInput.database]]
- [[LLMModelConfig.name]]
- [[ProgramDatabase.get_best_program]]
- [[ProgramDatabase.get_statistics]]
- [[SearchConfig.database]]
- [[SerializableResult.error]]
- [[default_discovery_controller.DiscoveryController]]

## ← Called by
_(entry point — nothing in this graph calls it)_
