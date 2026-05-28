---
name: TaskPool.create_task
description: method in skydiscover/utils/async_utils.py (utils)
metadata:
  type: project
---

# TaskPool.create_task

**File:** `skydiscover/utils/async_utils.py:34`  
**Kind:** method  
**Layer:** #utils

## Source
````python
    def create_task(self, coro: Callable, *args: Any, **kwargs: Any) -> asyncio.Task:
        """Create, track, and return an ``asyncio.Task`` bounded by the pool."""
        task = asyncio.create_task(self.run(coro, *args, **kwargs))
        self.tasks.append(task)
        task.add_done_callback(lambda t: self.tasks.remove(t))
        return task
````

## → Calls
- [[TaskPool.__init__]]
- [[TaskPool.run]]
- [[search_strategy_evaluator.args]]

## ← Called by
- [[DiscoveryController._run_discovery_parallel]]
- [[MonitorServer._serve]]
- [[TaskPool.gather]]
- [[openevolve_backend.run]]
- [[shinkaevolve_backend.run]]
