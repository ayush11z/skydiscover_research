---
name: DiscoveryController._run_discovery_sequential
description: method in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# DiscoveryController._run_discovery_sequential

**File:** `skydiscover/search/default_discovery_controller.py:248`  
**Kind:** method  
**Layer:** #inner-loop

## Source
````python
    async def _run_discovery_sequential(
        self,
        start_iteration: int,
        max_iterations: int,
        checkpoint_callback: Optional[Callable[[int], None]] = None,
        post_process_result: Optional[bool] = True,
        retry_times: Optional[int] = 3,
    ) -> Optional[Union[Program, SerializableResult]]:
        total_iterations = start_iteration + max_iterations

        result = None
        for iteration in range(start_iteration, total_iterations):
            if self.shutdown_event.is_set():
                logger.info("Shutdown requested, stopping discovery loop early")
                break

            try:
                result = await self._run_iteration(iteration, retry_times=retry_times)
                if result.error:
                    logger.warning(f"Iteration {iteration} failed: {result.error}")
                    continue

                if post_process_result:
                    self._process_iteration_result(result, iteration, checkpoint_callback)

            except Exception as e:
                logger.exception(f"Error in iteration {iteration}: {e}")

        if not post_process_result:
            return result

        return self._finalize_discovery()
````

## → Calls
- [[DiscoveryController._finalize_discovery]]
- [[DiscoveryController._process_iteration_result]]
- [[DiscoveryController._run_iteration]]
- [[SerializableResult.error]]
- [[base_database.Program]]
- [[discovery_utils.SerializableResult]]

## ← Called by
- [[DiscoveryController.run_discovery]]
