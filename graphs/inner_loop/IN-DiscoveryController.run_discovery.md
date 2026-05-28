---
name: IN-DiscoveryController.run_discovery
description: method in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# DiscoveryController.run_discovery

**File:** `skydiscover/search/default_discovery_controller.py:192`  
**Kind:** method  
**Layer:** #inner-loop

## What it does
Runs the sequential inner loop: calls DiscoveryController._run_iteration for each iteration up to `max_iterations`. Used both as the solution evolution loop (by Runner.run) and as the search-strategy generation loop (by CoEvolutionController._generate_and_validate_search_algorithm with `max_iterations=1`).

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
        """
        Run the discovery process.

        When ``config.max_parallel_iterations == 1`` (default), iterations
        run sequentially — same behaviour as before.

        When ``> 1``, up to *N* iterations run concurrently as asyncio
        tasks, bounded by a semaphore.  Generation and evaluation naturally
        overlap across iterations: while iteration *i* evaluates, iteration
        *i+1* can generate, and iteration *i+2* can sample.

        Args:
            start_iteration: The iteration to start from.
            max_iterations: The number of iterations to run.
            checkpoint_callback: Optional callback for checkpointing.
            post_process_result: If True, add results to the database and
                return the best Program.  If False, return the raw
                ``SerializableResult`` from the last iteration.
            retry_times: Number of retry attempts per iteration.

        Returns:
            Best ``Program`` found (post_process_result=True) or raw
            ``SerializableResult`` (post_process_result=False).
        """
        max_parallel = self.config.max_parallel_iterations

        if max_parallel > 1:
            return await self._run_discovery_parallel(
                start_iteration,
                max_iterations,
                checkpoint_callback,
                post_process_result,
                retry_times,
                max_parallel,
            )

        return await self._run_discovery_sequential(
            start_iteration,
            max_iterations,
            checkpoint_callback,
            post_process_result,
            retry_times,
        )
````

## → Calls
- [[IN-DiscoveryController._run_discovery_parallel]]
- [[IN-DiscoveryController._run_discovery_sequential]]
- [[IN-base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
