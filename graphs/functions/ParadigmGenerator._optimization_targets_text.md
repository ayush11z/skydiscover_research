---
name: ParadigmGenerator._optimization_targets_text
description: method in skydiscover/search/adaevolve/paradigm/generator.py (adaevolve)
metadata:
  type: project
---

# ParadigmGenerator._optimization_targets_text

**File:** `skydiscover/search/adaevolve/paradigm/generator.py:89`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _optimization_targets_text(self) -> str:
        """Describe what the paradigms should optimize."""
        if not self._is_multiobjective():
            return "Optimize the primary scalar score defined by the evaluator."

        parts = []
        for objective in self.objective_names:
            direction = "maximize" if self.higher_is_better.get(objective, True) else "minimize"
            parts.append(f"{objective} ({direction})")

        text = "Optimize the Pareto trade-offs across: " + ", ".join(parts) + "."
        if self.fitness_key:
            text += (
                f" Use `{self.fitness_key}` only as a scalar proxy when one score is needed for"
                " ranking, stagnation detection, or tie-breaking."
            )
        return text
````

## → Calls
- [[ParadigmGenerator._is_multiobjective]]

## ← Called by
- [[ParadigmGenerator._build_problem_context]]
- [[ParadigmGenerator._build_prompt_opt_context]]
