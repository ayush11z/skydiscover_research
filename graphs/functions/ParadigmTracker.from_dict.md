---
name: ParadigmTracker.from_dict
description: classmethod in skydiscover/search/adaevolve/paradigm/tracker.py (adaevolve)
metadata:
  type: project
---

# ParadigmTracker.from_dict

**File:** `skydiscover/search/adaevolve/paradigm/tracker.py:328`  
**Kind:** classmethod  
**Layer:** #adaevolve

## Source
````python
    def from_dict(cls, data: Dict[str, Any]) -> "ParadigmTracker":
        """Deserialize state from checkpoint."""
        tracker = cls(
            window_size=data.get("window_size", 30),
            improvement_threshold=data.get("improvement_threshold", 0.05),
            max_paradigm_uses=data.get("max_paradigm_uses", 5),
            max_tried_paradigms=data.get("max_tried_paradigms", 10),
            num_paradigms_to_generate=data.get("num_paradigms_to_generate", 3),
        )
        tracker.improvement_history = list(data.get("improvement_history", []))
        tracker.active_paradigms = list(data.get("active_paradigms", []))
        tracker.paradigm_usage_counts = {
            int(k): v for k, v in data.get("paradigm_usage_counts", {}).items()
        }
        tracker.current_paradigm_index = data.get("current_paradigm_index", 0)
        tracker.tried_paradigms = list(data.get("tried_paradigms", []))
        tracker.best_score_at_paradigm_gen = data.get("best_score_at_paradigm_gen", 0.0)
        tracker.best_score_during_paradigm = data.get("best_score_during_paradigm", 0.0)
        return tracker
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
- [[AdaEvolveDatabase.get_current_paradigm]]
- [[AdaEvolveDatabase.get_paradigm_num_to_generate]]
- [[AdaEvolveDatabase.get_previously_tried_ideas]]
- [[AdaEvolveDatabase.has_active_paradigm]]
- [[AdaEvolveDatabase.is_paradigm_stagnating]]
- [[AdaEvolveDatabase.load]]
- [[AdaEvolveDatabase.set_paradigms]]
- [[AdaEvolveDatabase.use_paradigm]]
