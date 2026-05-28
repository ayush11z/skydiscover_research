---
name: AdaEvolveController._run_iteration
description: method in skydiscover/search/adaevolve/controller.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveController._run_iteration

**File:** `skydiscover/search/adaevolve/controller.py:300`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    async def _run_iteration(self, iteration: int, checkpoint_callback) -> None:
        """Execute one evolution iteration."""
        iteration_start_time = time.time()

        # Check for global paradigm stagnation
        # Use database flag directly to stay in sync after checkpoint load
        if self.database.use_paradigm_breakthrough and self.database.is_paradigm_stagnating():
            await self._generate_paradigms_if_needed()

        result = await self._run_normal_step(iteration)

        iteration_time = time.time() - iteration_start_time

        if result.error:
            logger.warning(f"Iteration {iteration}: {result.error}")
            # Log failed iteration stats
            self._log_iteration_stats(
                iteration=iteration,
                sampling_mode=self._last_sampling_mode,
                sampling_intensity=self._last_sampling_intensity,
                child_program=None,
                iteration_time=iteration_time,
                llm_generation_time=result.llm_generation_time,
                eval_time=result.eval_time,
                error=result.error,
            )
        else:
            self._process_result(result, iteration, checkpoint_callback)
            # Log successful iteration stats
            self._log_iteration_stats(
                iteration=iteration,
                sampling_mode=self._last_sampling_mode,
                sampling_intensity=self._last_sampling_intensity,
                child_program=result.child_program_dict,
                iteration_time=result.iteration_time,
                llm_generation_time=result.llm_generation_time,
                eval_time=result.eval_time,
                error=None,
            )
````

## → Calls
- [[AdaEvolveController._generate_paradigms_if_needed]]
- [[AdaEvolveController._log_iteration_stats]]
- [[AdaEvolveController._process_result]]
- [[AdaEvolveController._run_normal_step]]
- [[DiscoveryControllerInput.database]]
- [[SearchConfig.database]]
- [[default_discovery_controller.DiscoveryController]]

## ← Called by
- [[AdaEvolveController.run_discovery]]
