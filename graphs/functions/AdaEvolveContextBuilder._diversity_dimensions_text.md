---
name: AdaEvolveContextBuilder._diversity_dimensions_text
description: method in skydiscover/context_builder/adaevolve/builder.py (context-builder)
metadata:
  type: project
---

# AdaEvolveContextBuilder._diversity_dimensions_text

**File:** `skydiscover/context_builder/adaevolve/builder.py:104`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _diversity_dimensions_text(self) -> str:
        if not self._is_multiobjective_enabled():
            return "The system maintains diversity across these dimensions: score, complexity."
        return "The system maintains diversity across Pareto trade-offs, novelty, and solution structure."
````

## → Calls
- [[AdaEvolveContextBuilder._is_multiobjective_enabled]]

## ← Called by
- [[AdaEvolveContextBuilder.build_prompt]]
