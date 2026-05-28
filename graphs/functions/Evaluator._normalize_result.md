---
name: Evaluator._normalize_result
description: method in skydiscover/evaluation/evaluator.py (evaluation)
metadata:
  type: project
---

# Evaluator._normalize_result

**File:** `skydiscover/evaluation/evaluator.py:238`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _normalize_result(self, result: Any) -> EvaluationResult:
        if isinstance(result, EvaluationResult):
            return result
        if isinstance(result, dict):
            return EvaluationResult.from_dict(result)

        logger.warning(f"Unexpected result type: {type(result)}")
        return EvaluationResult(metrics={"error": 0.0})
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[ContainerizedEvaluator.__init__]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[EvaluationResult.from_dict]]
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
- [[SearchConfig.type]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[_FinalResult.__init__]]
- [[evaluation_result.EvaluationResult]]

## ← Called by
- [[Evaluator._cascade_evaluate]]
- [[Evaluator.evaluate_program]]
