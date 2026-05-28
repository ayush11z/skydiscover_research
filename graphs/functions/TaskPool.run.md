---
name: TaskPool.run
description: method in skydiscover/utils/async_utils.py (utils)
metadata:
  type: project
---

# TaskPool.run

**File:** `skydiscover/utils/async_utils.py:29`  
**Kind:** method  
**Layer:** #utils

## Source
````python
    async def run(self, coro: Callable, *args: Any, **kwargs: Any) -> Any:
        """Run a single coroutine function under the concurrency semaphore."""
        async with self.semaphore:
            return await coro(*args, **kwargs)
````

## → Calls
- [[TaskPool.semaphore]]
- [[search_strategy_evaluator.args]]

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
- [[TaskPool.create_task]]
- [[api.run_discovery]]
- [[builder.run_async_safely]]
- [[cli.main]]
- [[openevolve_backend.run]]
- [[shinkaevolve_backend.run]]
- [[variation_operator_generator.get_available_packages]]
- [[variation_operator_generator.main]]
