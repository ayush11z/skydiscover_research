---
name: GEPANativeDatabase._rebuild_elite_pool
description: method in skydiscover/search/gepa_native/database.py (gepa)
metadata:
  type: project
---

# GEPANativeDatabase._rebuild_elite_pool

**File:** `skydiscover/search/gepa_native/database.py:282`  
**Kind:** method  
**Layer:** #gepa

## Source
````python
    def _rebuild_elite_pool(self) -> None:
        """Rebuild elite pool and metric_best from loaded programs."""
        self.elite_pool = sorted(
            self.programs.keys(),
            key=lambda pid: get_score(self.programs[pid].metrics or {}),
            reverse=True,
        )[: self.population_size]

        # Infer initial program as the earliest-seen one
        if self.programs:
            self.initial_program_id = min(
                self.programs,
                key=lambda pid: self.programs[pid].iteration_found,
            )

        for pid, prog in self.programs.items():
            if not prog.metrics:
                continue
            for metric_name, value in prog.metrics.items():
                if not isinstance(value, (int, float)):
                    continue
                current = self.metric_best.get(metric_name)
                if current is None or value > current[1]:
                    self.metric_best[metric_name] = (pid, value)
                    self.program_at_metric_front[metric_name] = {pid}
                elif value == current[1]:
                    self.program_at_metric_front[metric_name].add(pid)
````

## → Calls
- [[CheckpointManager.load]]
- [[EvaluationResult.metrics]]
- [[GEPANativeDatabase.__init__]]
- [[Program.metrics]]
- [[metrics.get_score]]

## ← Called by
- [[GEPANativeDatabase.load]]
