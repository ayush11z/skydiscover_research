---
name: EvaluationResult.from_dict
description: classmethod in skydiscover/evaluation/evaluation_result.py (evaluation)
metadata:
  type: project
---

# EvaluationResult.from_dict

**File:** `skydiscover/evaluation/evaluation_result.py:15`  
**Kind:** classmethod  
**Layer:** #evaluation

## Source
````python
    def from_dict(cls, metrics: Dict[str, float]) -> "EvaluationResult":
        return cls(metrics=metrics)
````

## → Calls
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

## ← Called by
- [[Evaluator._normalize_result]]
