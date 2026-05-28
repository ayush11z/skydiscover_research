---
name: MultiDimensionalAdapter.from_dict
description: classmethod in skydiscover/search/adaevolve/adaptation.py (adaevolve)
metadata:
  type: project
---

# MultiDimensionalAdapter.from_dict

**File:** `skydiscover/search/adaevolve/adaptation.py:541`  
**Kind:** classmethod  
**Layer:** #adaevolve

## Source
````python
    def from_dict(cls, data: Dict[str, Any]) -> "MultiDimensionalAdapter":
        """Deserialize state from checkpoint."""
        adapter = cls(
            ucb_exploration=data.get("ucb_exploration", 1.41),
            min_visits=data.get("min_visits", 3),
            decay=data.get("decay", 0.9),
            epsilon=data.get("epsilon", 1e-8),
        )
        adapter.states = [AdaptiveState.from_dict(s) for s in data.get("states", [])]
        adapter.dimension_visits = list(data.get("dimension_visits", []))
        adapter.dimension_rewards = list(data.get("dimension_rewards", []))
        adapter.decayed_visits = list(data.get("decayed_visits", []))
        adapter.global_best_score = data.get("global_best_score", float("-inf"))

        # Backward compatibility: if decayed_visits not in checkpoint,
        # initialize from raw visits (loses decay history but functional)
        if not adapter.decayed_visits and adapter.dimension_visits:
            adapter.decayed_visits = [float(v) for v in adapter.dimension_visits]

        # Backward compatibility: if global_best_score not in checkpoint,
        # compute from per-dimension best scores
        if adapter.global_best_score == float("-inf") and adapter.states:
            adapter.global_best_score = (
                max(s.best_score for s in adapter.states if not math.isinf(s.best_score))
                if any(not math.isinf(s.best_score) for s in adapter.states)
                else float("-inf")
            )

        return adapter
````

## → Calls
- [[AdaptiveState.best_score]]
- [[AdaptiveState.from_dict]]
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[ContainerizedEvaluator.__init__]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[DiscoveryResult.best_score]]
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
- [[AdaEvolveDatabase._expand_to_island_count]]
- [[AdaEvolveDatabase._should_spawn_island]]
- [[AdaEvolveDatabase._spawn_island]]
- [[AdaEvolveDatabase.add_merged_program]]
- [[AdaEvolveDatabase.load]]
