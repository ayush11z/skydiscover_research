---
name: Evaluator._cascade_evaluate
description: method in skydiscover/evaluation/evaluator.py (evaluation)
metadata:
  type: project
---

# Evaluator._cascade_evaluate

**File:** `skydiscover/evaluation/evaluator.py:247`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    async def _cascade_evaluate(self, program_path: str) -> EvaluationResult:
        """Run cascade evaluation: stage1 → threshold check → stage2 → merge."""
        module = self._eval_module

        if not hasattr(module, "evaluate_stage1"):
            return self._normalize_result(
                await self._run_stage(self.evaluate_function, program_path)
            )

        # Stage 1
        try:
            stage1 = self._normalize_result(
                await self._run_stage(module.evaluate_stage1, program_path)
            )
        except asyncio.TimeoutError:
            logger.error(f"Stage 1 timed out ({self.config.timeout}s)")
            return EvaluationResult(
                metrics={"error": 0.0, "timeout": True},
                artifacts={"failure_stage": "stage1"},
            )
        except Exception as e:
            logger.error(f"Stage 1 failed: {e}")
            return EvaluationResult(
                metrics={"error": 0.0},
                artifacts={
                    "failure_stage": "stage1",
                    "stderr": str(e),
                    "traceback": traceback.format_exc(),
                },
            )

        if not self._passes_threshold(stage1.metrics, self.config.cascade_thresholds[0]):
            return stage1

        if not hasattr(module, "evaluate_stage2"):
            return stage1

        # Stage 2
        try:
            stage2 = self._normalize_result(
                await self._run_stage(module.evaluate_stage2, program_path)
            )
        except asyncio.TimeoutError:
            logger.error(f"Stage 2 timed out ({self.config.timeout}s)")
            stage1.metrics["timeout"] = True
            stage1.artifacts["failure_stage"] = "stage2"
            return stage1
        except Exception as e:
            logger.error(f"Stage 2 failed: {e}")
            stage1.artifacts.update({"failure_stage": "stage2", "stage2_stderr": str(e)})
            return stage1

        # Merge stages
        merged_metrics = {
            k: float(v)
            for k, v in {**stage1.metrics, **stage2.metrics}.items()
            if isinstance(v, (int, float)) and k != "error"
        }
        return EvaluationResult(
            metrics=merged_metrics,
            artifacts={**stage1.artifacts, **stage2.artifacts},
        )
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[ContainerizedEvaluator.__init__]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[EvaluationResult.artifacts]]
- [[EvaluationResult.metrics]]
- [[Evaluator.__init__]]
- [[Evaluator._normalize_result]]
- [[Evaluator._passes_threshold]]
- [[Evaluator._run_stage]]
- [[EvaluatorConfig.cascade_thresholds]]
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

## ← Called by
- [[Evaluator.evaluate_program]]
