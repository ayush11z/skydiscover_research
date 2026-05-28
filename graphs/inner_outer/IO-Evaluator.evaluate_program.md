---
name: IO-Evaluator.evaluate_program
description: method in skydiscover/evaluation/evaluator.py (evaluation)
metadata:
  type: project
---

# Evaluator.evaluate_program

**File:** `skydiscover/evaluation/evaluator.py:97`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    async def evaluate_program(
        self,
        program_solution: str,
        program_id: str = "",
        mode: str = "train",
    ) -> EvaluationResult:
        """Evaluate a program and return scores with optional artifacts.

        Args:
            program_solution: Source code of the candidate program.
            program_id: Optional identifier for logging.
            mode: ``"train"`` or ``"test"``.  Ignored by the Python evaluator
                  (the containerized evaluator passes it to evaluate.sh).
        """
        start_time = time.time()
        label = f" {program_id}" if program_id else ""

        last_exception = None
        for attempt in range(self.config.max_retries + 1):
            try:
                with tempfile.NamedTemporaryFile(suffix=self.program_suffix, delete=False) as f:
                    f.write(program_solution.encode("utf-8"))
                    temp_path = f.name
            except OSError as e:
                if e.errno == errno.ENOSPC:
                    logger.error("Disk full — cannot create temp file")
                    return EvaluationResult(metrics={"error": 0.0, "disk_space_error": True})
                raise

            sidecar_path = None
            if self.is_image_mode:
                sidecar_path = temp_path + ".image_path"
                try:
                    with open(sidecar_path, "w") as sf:
                        sf.write(program_solution)
                except Exception as e:
                    logger.warning(f"Failed to write image sidecar: {e}")

            try:
                if self.config.cascade_evaluation:
                    result = await self._cascade_evaluate(temp_path)
                else:
                    result = await self._run_stage(self.evaluate_function, temp_path)

                eval_result = self._normalize_result(result)

                if self.llm_judge:
                    llm_result = await self.llm_judge.evaluate(program_solution, program_id)
                    if llm_result:
                        for name, value in llm_result.metrics.items():
                            eval_result.metrics[f"llm_{name}"] = value
                        eval_result.artifacts.update(llm_result.artifacts)

                elapsed = time.time() - start_time
                logger.info(
                    f"Evaluated program{label} in {elapsed:.2f}s: {format_metrics(eval_result.metrics)}"
                )
                return eval_result

            except asyncio.TimeoutError:
                logger.error(
                    f"Program{label} timed out after {time.time() - start_time:.0f}s (limit: {self.config.timeout}s)"
                )
                return EvaluationResult(metrics={"error": 0.0, "timeout": True})

            except Exception as e:
                last_exception = e
                logger.warning(
                    f"Attempt {attempt + 1}/{self.config.max_retries + 1} failed{label}: {e}"
                )
                if attempt < self.config.max_retries:
                    await asyncio.sleep(1.0)

            finally:
                if os.path.exists(temp_path):
                    os.unlink(temp_path)
                if sidecar_path and os.path.exists(sidecar_path):
                    os.unlink(sidecar_path)

        logger.error(f"All attempts failed{label}: {last_exception}")
        return EvaluationResult(metrics={"error": 0.0})
````

## → Calls
- [[IO-EvaluationResult.artifacts]]
- [[IO-EvaluationResult.metrics]]
- [[IO-Evaluator.__init__]]
- [[IO-Evaluator._cascade_evaluate]]
- [[IO-Evaluator._normalize_result]]
- [[IO-Evaluator._run_stage]]
- [[IO-evaluation_result.EvaluationResult]]
- [[IO-metrics.format_metrics]]

## ← Called by
- [[IO-DiscoveryController._run_from_scratch_iteration]]
- [[IO-DiscoveryController._run_iteration]]
- [[IO-Evaluator.evaluate_batch]]
