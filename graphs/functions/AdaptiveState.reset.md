---
name: AdaptiveState.reset
description: method in skydiscover/search/adaevolve/adaptation.py (adaevolve)
metadata:
  type: project
---

# AdaptiveState.reset

**File:** `skydiscover/search/adaevolve/adaptation.py:184`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def reset(self) -> None:
        """Reset adaptive state (e.g., when spawning a new island)."""
        self.accumulated_signal = 0.0
        self.best_score = float("-inf")
        self.improvement_count = 0
        self.total_evaluations = 0
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[langfuse_tracer.reset_llm_context]]
