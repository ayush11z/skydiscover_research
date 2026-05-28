---
name: TaskPool.gather
description: method in skydiscover/utils/async_utils.py (utils)
metadata:
  type: project
---

# TaskPool.gather

**File:** `skydiscover/utils/async_utils.py:41`  
**Kind:** method  
**Layer:** #utils

## Source
````python
    async def gather(
        self,
        coros: Sequence[Callable],
        args_list: Sequence[Tuple[Any, ...]] = (),
        kwargs_list: Sequence[dict] = (),
        return_exceptions: bool = False,
    ) -> List[Any]:
        """Run *coros* concurrently (bounded by the semaphore), return results in order."""
        n = len(coros)
        _args = args_list if args_list else [() for _ in range(n)]
        _kwargs = kwargs_list if kwargs_list else [{} for _ in range(n)]

        if len(_args) != n:
            raise ValueError(f"args_list length ({len(_args)}) must match coros length ({n})")
        if len(_kwargs) != n:
            raise ValueError(f"kwargs_list length ({len(_kwargs)}) must match coros length ({n})")

        tasks = [
            self.create_task(coro, *args, **kwargs)
            for coro, args, kwargs in zip(coros, _args, _kwargs)
        ]
        return await asyncio.gather(*tasks, return_exceptions=return_exceptions)
````

## → Calls
- [[TaskPool.create_task]]

## ← Called by
- [[ContainerizedEvaluator.evaluate_batch]]
- [[Evaluator.evaluate_batch]]
- [[LLMPool.generate_all]]
- [[MonitorServer._run_loop]]
- [[MonitorServer._serve]]
- [[build_prompt.gather_llm_calls]]
