---
name: OpenEvolveNativeDatabase._update_diversity_reference_set
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._update_diversity_reference_set

**File:** `skydiscover/search/openevolve_native/database.py:574`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _update_diversity_reference_set(self) -> None:
        if not self.programs:
            return
        all_progs = list(self.programs.values())

        if len(all_progs) <= self.diversity_reference_size:
            self.diversity_reference_set = [p.solution for p in all_progs]
            return

        # Greedy-diverse selection
        selected: List[Program] = []
        remaining = all_progs.copy()

        selected.append(remaining.pop(random.randint(0, len(remaining) - 1)))

        while len(selected) < self.diversity_reference_size and remaining:
            best_idx, best_div = -1, -1.0
            for i, cand in enumerate(remaining):
                min_d = min(self._fast_code_diversity(cand.solution, s.solution) for s in selected)
                if min_d > best_div:
                    best_div = min_d
                    best_idx = i
            if best_idx >= 0:
                selected.append(remaining.pop(best_idx))

        self.diversity_reference_set = [p.solution for p in selected]
````

## → Calls
- [[CheckpointManager.load]]
- [[OpenEvolveNativeDatabase._fast_code_diversity]]
- [[base_database.Program]]

## ← Called by
- [[OpenEvolveNativeDatabase._get_cached_diversity]]
