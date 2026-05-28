---
name: GEPANativeDatabase._select_parent
description: method in skydiscover/search/gepa_native/database.py (gepa)
metadata:
  type: project
---

# GEPANativeDatabase._select_parent

**File:** `skydiscover/search/gepa_native/database.py:314`  
**Kind:** method  
**Layer:** #gepa

## Source
````python
    def _select_parent(self) -> Program:
        """Epsilon-greedy or Pareto-based parent selection."""
        if self.candidate_selection_strategy == "best" or not self.elite_pool:
            return self.get_best_program()

        if self.candidate_selection_strategy == "pareto":
            return self._select_parent_pareto()

        if self.rng.random() < self.epsilon and len(self.elite_pool) > 1:
            pid = self.rng.choice(self.elite_pool)
            return self.programs[pid]
        return self.get_best_program()
````

## → Calls
- [[CheckpointManager.load]]
- [[GEPANativeDatabase._select_parent_pareto]]
- [[ProgramDatabase.get_best_program]]
- [[base_database.Program]]

## ← Called by
- [[GEPANativeDatabase.sample]]
