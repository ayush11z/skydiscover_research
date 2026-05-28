---
name: GEPANativeController.run_discovery
description: method in skydiscover/search/gepa_native/controller.py (gepa)
metadata:
  type: project
---

# GEPANativeController.run_discovery

**File:** `skydiscover/search/gepa_native/controller.py:88`  
**Kind:** method  
**Layer:** #gepa

## Source
````python
    async def run_discovery(
        self,
        start_iteration: int,
        max_iterations: int,
        checkpoint_callback: Optional[Callable[[int], None]] = None,
        post_process_result: Optional[bool] = True,
        retry_times: Optional[int] = 3,
    ) -> Optional[Union[Program, SerializableResult]]:
        """Run GEPA discovery with acceptance gating and merge scheduling.

        The loop follows this order each iteration:
        1. Proactive merge (if scheduled from a prior acceptance).
        2. Normal mutation via ``_run_iteration``.
        3. Acceptance gating — reject if child <= parent.
        4. If accepted: process result, schedule next proactive merge.
        5. Track improvement; trigger stagnation merge if stuck.
        """
        total_iterations = start_iteration + max_iterations

        # Initialise best-score from database if resuming
        best = self.database.get_best_program()
        if best and best.metrics:
            self._best_score_seen = get_score(best.metrics)

        result = None
        for iteration in range(start_iteration, total_iterations):
            if self.shutdown_event.is_set():
                logger.info("Shutdown requested, stopping discovery loop early")
                break

            try:
                # Proactive merge: attempt before normal iteration if scheduled
                if self._merge_due:
                    self._merge_due = False
                    await self._attempt_merge(iteration)

                result = await self._run_iteration(iteration, retry_times=retry_times)

                if result.error:
                    logger.warning(f"Iteration {iteration} failed: {result.error}")
                    self._iterations_without_improvement += 1

                    if self._should_merge():
                        await self._attempt_merge(iteration)
                    continue

                # --- Acceptance gating (skip for from-scratch programs) ---
                if self.acceptance_gating and result.child_program_dict and result.parent_id:
                    accepted = self._acceptance_gate(result, iteration)
                    if not accepted:
                        if self._should_merge():
                            await self._attempt_merge(iteration)
                        continue

                # --- Accept: process normally ---
                if post_process_result:
                    self._process_iteration_result(result, iteration, checkpoint_callback)

                # Schedule a proactive merge after successful acceptance
                if self.use_merge and self._merge_attempts_used < self.max_merge_attempts:
                    self._merge_due = True

                # Track improvement
                if result.child_program_dict:
                    child_score = get_score(result.child_program_dict.get("metrics", {}))
                    if child_score > self._best_score_seen:
                        self._best_score_seen = child_score
                        self._iterations_without_improvement = 0
                    else:
                        self._iterations_without_improvement += 1
                else:
                    self._iterations_without_improvement += 1

                # Stagnation-triggered merge (fallback)
                if self._should_merge():
                    await self._attempt_merge(iteration)

            except Exception as e:
                logger.exception(f"Error in iteration {iteration}: {e}")
                self._iterations_without_improvement += 1

        if not post_process_result:
            return result

        if self.shutdown_event.is_set():
            logger.info(
                f"Discovery completed (search strategy = {self.database.name}) "
                "- Shutdown requested"
            )
        else:
            logger.info(
                f"Discovery completed (search strategy = {self.database.name}) "
                "- Maximum iterations reached"
            )

        return self.database.get_best_program()
````

## → Calls
- [[DiscoveryController._process_iteration_result]]
- [[DiscoveryController._run_iteration]]
- [[DiscoveryControllerInput.database]]
- [[EvaluationResult.metrics]]
- [[GEPANativeController._acceptance_gate]]
- [[GEPANativeController._attempt_merge]]
- [[GEPANativeController._should_merge]]
- [[Program.metrics]]
- [[Program.parent_id]]
- [[SearchConfig.database]]
- [[SerializableResult.child_program_dict]]
- [[SerializableResult.error]]
- [[SerializableResult.parent_id]]
- [[base_database.Program]]
- [[default_discovery_controller.DiscoveryController]]
- [[discovery_utils.SerializableResult]]
- [[metrics.get_score]]

## ← Called by
_(entry point — nothing in this graph calls it)_
