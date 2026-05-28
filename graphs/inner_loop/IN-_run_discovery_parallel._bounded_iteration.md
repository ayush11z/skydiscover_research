---
name: IN-_run_discovery_parallel._bounded_iteration
description: function in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# _run_discovery_parallel._bounded_iteration

**File:** `skydiscover/search/default_discovery_controller.py:304`  
**Kind:** function  
**Layer:** #inner-loop

## Source
````python
        async def _bounded_iteration(iteration: int) -> Tuple[int, Optional[SerializableResult]]:
            """Run one iteration under the semaphore, then process its result.

            Result processing (database.add) happens here rather than being
            collected later so that subsequent iterations see the latest DB
            state as soon as the ``await`` inside ``_run_iteration`` yields.
            """
            async with sem:
                if self.shutdown_event.is_set():
                    return iteration, None
                try:
                    result = await self._run_iteration(iteration, retry_times=retry_times)
                except Exception as e:
                    logger.exception(f"Error in parallel iteration {iteration}: {e}")
                    return iteration, None

            # Process outside the semaphore — database.add() is sync and
            # completes atomically between await-points, so no lock needed.
            if result and not result.error and post_process_result:
                self._process_iteration_result(result, iteration, checkpoint_callback)
            elif result and result.error:
                logger.warning(f"Iteration {iteration} failed: {result.error}")

            return iteration, result
````

## → Calls
- [[IN-DiscoveryController._process_iteration_result]]
- [[IN-DiscoveryController._run_iteration]]

## ← Called by
- [[IN-DiscoveryController._run_discovery_parallel]]
