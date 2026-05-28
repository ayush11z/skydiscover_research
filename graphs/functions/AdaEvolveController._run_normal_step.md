---
name: AdaEvolveController._run_normal_step
description: method in skydiscover/search/adaevolve/controller.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveController._run_normal_step

**File:** `skydiscover/search/adaevolve/controller.py:379`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    async def _run_normal_step(self, iteration: int) -> SerializableResult:
        """Run a normal iteration with optional retry."""
        last_error = None
        attempts = 1 + (self.max_retries if self.enable_retry else 0)

        for attempt in range(attempts):
            result = await self._generate_child(iteration, error_context=last_error)
            if not result.error:
                return result
            last_error = result.error
            logger.debug(f"Attempt {attempt + 1}/{attempts} failed: {last_error}")

        return SerializableResult(
            error=f"All {attempts} attempts failed: {last_error}",
            iteration=iteration,
        )
````

## → Calls
- [[AdaEvolveController._generate_child]]
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[ContainerizedEvaluator.__init__]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[Evaluator.__init__]]
- [[HumanFeedbackReader.__init__]]
- [[HybridDiversity.__init__]]
- [[LLMJudge.__init__]]
- [[LLMPool.__init__]]
- [[LangFuseTracer.__init__]]
- [[LogWindowScorer.__init__]]
- [[MetricDiversity.__init__]]
- [[MonitorServer.__init__]]
- [[OpenAILLM.__init__]]
- [[ParadigmGenerator.__init__]]
- [[ProgramDatabase.__init__]]
- [[Runner.__init__]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[_FinalResult.__init__]]
- [[discovery_utils.SerializableResult]]

## ← Called by
- [[AdaEvolveController._run_iteration]]
