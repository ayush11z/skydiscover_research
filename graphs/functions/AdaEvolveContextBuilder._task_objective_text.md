---
name: AdaEvolveContextBuilder._task_objective_text
description: method in skydiscover/context_builder/adaevolve/builder.py (context-builder)
metadata:
  type: project
---

# AdaEvolveContextBuilder._task_objective_text

**File:** `skydiscover/context_builder/adaevolve/builder.py:92`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _task_objective_text(self) -> str:
        subject = (
            "prompt" if (self.config.language or "").lower() in ("text", "prompt") else "program"
        )
        if not self._is_multiobjective_enabled():
            return f"Suggest improvements to the {subject} that will improve its COMBINED_SCORE."
        return (
            f"Suggest improvements to the {subject} that improve its Pareto trade-offs across: "
            + ", ".join(self._objective_descriptions())
            + "."
        )
````

## → Calls
- [[AdaEvolveContextBuilder._is_multiobjective_enabled]]
- [[AdaEvolveContextBuilder._objective_descriptions]]
- [[DiscoveryControllerInput.config]]

## ← Called by
- [[AdaEvolveContextBuilder.build_prompt]]
