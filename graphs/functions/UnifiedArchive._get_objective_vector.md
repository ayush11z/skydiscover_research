---
name: UnifiedArchive._get_objective_vector
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive._get_objective_vector

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:512`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _get_objective_vector(self, program: Program) -> List[float]:
        """Extract objective vector for a program (higher is always better internally)."""
        vec = []
        for obj_key in self.config.pareto_objectives:
            raw_val = program.metrics.get(obj_key, 0.0)
            if not isinstance(raw_val, (int, float)):
                raw_val = 0.0
            if not self.config.higher_is_better.get(obj_key, True):
                raw_val = -raw_val
            vec.append(float(raw_val))
        return vec
````

## → Calls
- [[DiscoveryControllerInput.config]]
- [[EvaluationResult.metrics]]
- [[Program.metrics]]
- [[UnifiedArchive.__init__]]
- [[base_database.Program]]

## ← Called by
- [[UnifiedArchive._compute_elite_score_for_new]]
