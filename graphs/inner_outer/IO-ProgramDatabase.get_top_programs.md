---
name: IO-ProgramDatabase.get_top_programs
description: method in skydiscover/search/base_database.py (database)
metadata:
  type: project
---

# ProgramDatabase.get_top_programs

**File:** `skydiscover/search/base_database.py:275`  
**Kind:** method  
**Layer:** #database

## Source
````python
    def get_top_programs(self, n: int = 10, metric: Optional[str] = None) -> List[Program]:
        """Get the top N programs, optionally by a specific metric."""
        if not self.programs:
            return []

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

        return sorted_programs[:n]
````

## → Calls
- [[IO-Program.metrics]]
- [[IO-ProgramDatabase.load]]
- [[IO-base_database.Program]]
- [[IO-metrics.get_score]]

## ← Called by
_(entry point — nothing in this graph calls it)_
