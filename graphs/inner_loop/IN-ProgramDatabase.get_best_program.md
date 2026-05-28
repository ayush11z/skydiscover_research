---
name: IN-ProgramDatabase.get_best_program
description: method in skydiscover/search/base_database.py (database)
metadata:
  type: project
---

# ProgramDatabase.get_best_program

**File:** `skydiscover/search/base_database.py:241`  
**Kind:** method  
**Layer:** #database

## Source
````python
    def get_best_program(self, metric: Optional[str] = None) -> Optional[Program]:
        """Get the best program, optionally by a specific metric."""
        if not self.programs:
            return None

        if metric is None and self.best_program_id:
            if self.best_program_id in self.programs:
                return self.programs[self.best_program_id]
            else:
                logger.warning(
                    f"Tracked best program {self.best_program_id} no longer exists, will recalculate"
                )
                self.best_program_id = None

        if metric:
            sorted_programs = sorted(
                [p for p in self.programs.values() if metric in p.metrics],
                key=lambda p: p.metrics[metric],
                reverse=True,
            )
        else:
            sorted_programs = sorted(
                self.programs.values(),
                key=lambda p: get_score(p.metrics),
                reverse=True,
            )

        if sorted_programs and (
            self.best_program_id is None or sorted_programs[0].id != self.best_program_id
        ):
            self.best_program_id = sorted_programs[0].id

        return sorted_programs[0] if sorted_programs else None
````

## → Calls
- [[IN-Program.id]]
- [[IN-Program.metrics]]
- [[IN-ProgramDatabase.load]]
- [[IN-base_database.Program]]
- [[IN-metrics.get_score]]

## ← Called by
- [[IN-DiscoveryController._finalize_discovery]]
- [[IN-DiscoveryController.postprocess_result]]
- [[IN-ProgramDatabase.log_status]]
