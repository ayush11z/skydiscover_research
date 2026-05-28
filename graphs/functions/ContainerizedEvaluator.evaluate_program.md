---
name: ContainerizedEvaluator.evaluate_program
description: method in skydiscover/evaluation/container_evaluator.py (evaluation)
metadata:
  type: project
---

# ContainerizedEvaluator.evaluate_program

**File:** `skydiscover/evaluation/container_evaluator.py:132`  
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
        """Evaluate one candidate program and return scores.

        Args:
            program_solution: Source code (or path, for image mode) of the candidate.
            program_id: Optional identifier for logging.
            mode: ``"train"`` for hot-loop evaluation, ``"test"`` for
                  authoritative/publish evaluation.
        """
        start_time = time.time()
        label = f" {program_id}" if program_id else ""

        last_exception = None
        for attempt in range(self.config.max_retries + 1):
            try:
                result = await asyncio.wait_for(
                    asyncio.get_running_loop().run_in_executor(
                        None, self._run_container, program_solution, mode
                    ),
                    timeout=self.config.timeout,
                )
                elapsed = time.time() - start_time
                logger.info(
                    f"Evaluated program{label} [{mode}] in {elapsed:.2f}s:"
                    f" {format_metrics(result.metrics)}"
                )
                return result

            except asyncio.TimeoutError:
                logger.error(f"Container timed out after {self.config.timeout}s{label}")
                return EvaluationResult(metrics={"error": 0.0, "timeout": True})

            except Exception as e:
                last_exception = e
                logger.warning(
                    f"Attempt {attempt + 1}/{self.config.max_retries + 1} failed{label}: {e}"
                )
                if attempt < self.config.max_retries:
                    await asyncio.sleep(1.0)

        logger.error(f"All attempts failed{label}: {last_exception}")
        return EvaluationResult(metrics={"error": 0.0})
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[ContainerizedEvaluator.__init__]]
- [[ContainerizedEvaluator._run_container]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[Evaluator.__init__]]
- [[EvaluatorConfig.max_retries]]
- [[EvaluatorConfig.timeout]]
- [[HumanFeedbackReader.__init__]]
- [[HybridDiversity.__init__]]
- [[LLMJudge.__init__]]
- [[LLMModelConfig.timeout]]
- [[LLMPool.__init__]]
- [[LangFuseTracer.__init__]]
- [[LogWindowScorer.__init__]]
- [[MetricDiversity.__init__]]
- [[MonitorServer.__init__]]
- [[OpenAILLM.__init__]]
- [[ParadigmGenerator.__init__]]
- [[ProgramDatabase.__init__]]
- [[Runner.__init__]]
- [[SerializableResult.error]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[_FinalResult.__init__]]
- [[evaluation_result.EvaluationResult]]
- [[metrics.format_metrics]]

## ← Called by
- [[ClaudeCodeController._final_evaluation]]
- [[ClaudeCodeController.run_discovery]]
- [[ContainerizedEvaluator.evaluate_batch]]
- [[DiscoveryController._run_from_scratch_iteration]]
- [[DiscoveryController._run_iteration]]
