---
name: Evaluator.evaluate_program
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
- [[AgenticGenerator.__init__]]
- [[BenchmarkConfig.name]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[ContainerizedEvaluator.__init__]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[EvaluationResult.artifacts]]
- [[EvaluationResult.metrics]]
- [[Evaluator.__init__]]
- [[Evaluator._cascade_evaluate]]
- [[Evaluator._normalize_result]]
- [[Evaluator._run_stage]]
- [[EvaluatorConfig.cascade_evaluation]]
- [[EvaluatorConfig.file_suffix]]
- [[EvaluatorConfig.is_image_mode]]
- [[EvaluatorConfig.max_retries]]
- [[EvaluatorConfig.timeout]]
- [[HumanFeedbackReader.__init__]]
- [[HybridDiversity.__init__]]
- [[LLMJudge.__init__]]
- [[LLMJudge.evaluate]]
- [[LLMModelConfig.name]]
- [[LLMModelConfig.timeout]]
- [[LLMPool.__init__]]
- [[LangFuseTracer.__init__]]
- [[LogWindowScorer.__init__]]
- [[MetricDiversity.__init__]]
- [[MonitorServer.__init__]]
- [[OpenAILLM.__init__]]
- [[ParadigmGenerator.__init__]]
- [[Program.artifacts]]
- [[Program.metrics]]
- [[ProgramDatabase.__init__]]
- [[Runner.__init__]]
- [[SerializableResult.error]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[_FinalResult.__init__]]
- [[evaluation_result.EvaluationResult]]
- [[metrics.format_metrics]]
- [[search_strategy_evaluator.evaluate]]

## ← Called by
- [[ClaudeCodeController._final_evaluation]]
- [[ClaudeCodeController.run_discovery]]
- [[DiscoveryController._run_from_scratch_iteration]]
- [[DiscoveryController._run_iteration]]
- [[Evaluator.evaluate_batch]]
