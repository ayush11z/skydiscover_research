---
name: IN-DiscoveryController._run_discovery_parallel
description: method in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# DiscoveryController._run_discovery_parallel

**File:** `skydiscover/search/default_discovery_controller.py:285`  
**Kind:** method  
**Layer:** #inner-loop

## Source
````python
    async def _run_discovery_parallel(
        self,
        start_iteration: int,
        max_iterations: int,
        checkpoint_callback: Optional[Callable[[int], None]] = None,
        post_process_result: Optional[bool] = True,
        retry_times: Optional[int] = 3,
        max_parallel: int = 4,
    ) -> Optional[Union[Program, SerializableResult]]:
        total_iterations = start_iteration + max_iterations
        sem = asyncio.Semaphore(max_parallel)
        pending: set = set()
        last_result: Optional[SerializableResult] = None

        logger.info(
            f"Parallel discovery: up to {max_parallel} iterations in flight "
            f"({start_iteration}..{total_iterations - 1})"
        )

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

        for iteration in range(start_iteration, total_iterations):
            if self.shutdown_event.is_set():
                break

            task = asyncio.create_task(_bounded_iteration(iteration), name=f"iter_{iteration}")
            pending.add(task)
            task.add_done_callback(pending.discard)

            # When the pipeline is full, wait for at least one to finish
            # before scheduling more — this provides backpressure.
            if len(pending) >= max_parallel:
                done, pending = await asyncio.wait(
                    pending,
                    return_when=asyncio.FIRST_COMPLETED,
                )
                for t in done:
                    try:
                        _, res = t.result()
                        if res is not None:
                            last_result = res
                    except Exception as e:
                        logger.warning(
                            f"A task in parallel discovery failed with an exception: {e}"
                        )

        # Drain remaining tasks
        if pending:
            done, _ = await asyncio.wait(pending)
            for t in done:
                try:
                    _, res = t.result()
                    if res is not None:
                        last_result = res
                except Exception as e:
                    logger.warning(
                        f"A task in parallel discovery (drain) failed with an exception: {e}"
                    )

        if not post_process_result:
            return last_result

        return self._finalize_discovery()
````

## → Calls
- [[IN-DiscoveryController._finalize_discovery]]
- [[IN-_run_discovery_parallel._bounded_iteration]]
- [[IN-base_database.Program]]

## ← Called by
- [[IN-DiscoveryController.run_discovery]]
