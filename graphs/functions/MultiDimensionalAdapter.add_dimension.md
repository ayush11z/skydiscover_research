---
name: MultiDimensionalAdapter.add_dimension
description: method in skydiscover/search/adaevolve/adaptation.py (adaevolve)
metadata:
  type: project
---

# MultiDimensionalAdapter.add_dimension

**File:** `skydiscover/search/adaevolve/adaptation.py:272`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def add_dimension(self, state: AdaptiveState = None) -> int:
        """
        Add a new dimension (e.g., spawn a new island).

        Args:
            state: Optional pre-configured AdaptiveState

        Returns:
            Index of the new dimension
        """
        if state is None:
            state = AdaptiveState(decay=self.decay)
        self.states.append(state)
        self.dimension_visits.append(0)  # Raw count
        self.dimension_rewards.append(0.0)  # Decayed rewards
        self.decayed_visits.append(0.0)  # Decayed visits
        return len(self.states) - 1
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
- [[adaptation.AdaptiveState]]

## ← Called by
- [[AdaEvolveDatabase.__init__]]
- [[AdaEvolveDatabase._expand_to_island_count]]
- [[AdaEvolveDatabase._spawn_island]]
