---
name: AdaptiveState.from_dict
description: classmethod in skydiscover/search/adaevolve/adaptation.py (adaevolve)
metadata:
  type: project
---

# AdaptiveState.from_dict

**File:** `skydiscover/search/adaevolve/adaptation.py:205`  
**Kind:** classmethod  
**Layer:** #adaevolve

## Source
````python
    def from_dict(cls, data: Dict[str, Any]) -> "AdaptiveState":
        """Deserialize state from checkpoint."""
        state = cls(
            decay=data.get("decay", 0.9),
            epsilon=data.get("epsilon", 1e-8),
            intensity_min=data.get("intensity_min", 0.1),
            intensity_max=data.get("intensity_max", 0.7),
        )
        state.accumulated_signal = data.get("accumulated_signal", 0.0)
        state.best_score = data.get("best_score", float("-inf"))
        state.improvement_count = data.get("improvement_count", 0)
        state.total_evaluations = data.get("total_evaluations", 0)
        return state
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
- [[LangFuseTracer.get]]
- [[LogWindowScorer.__init__]]
- [[MetricDiversity.__init__]]
- [[MonitorServer.__init__]]
- [[OpenAILLM.__init__]]
- [[ParadigmGenerator.__init__]]
- [[ProgramDatabase.__init__]]
- [[ProgramDatabase.get]]
- [[Runner.__init__]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[UnifiedArchive.get]]
- [[_FinalResult.__init__]]

## ← Called by
- [[MultiDimensionalAdapter.from_dict]]
