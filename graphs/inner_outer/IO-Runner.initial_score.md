---
name: IO-Runner.initial_score
description: method in skydiscover/runner.py (runner)
metadata:
  type: project
---

# Runner.initial_score

**File:** `skydiscover/runner.py:87`  
**Kind:** method  
**Layer:** #runner

## Source
````python
    def initial_score(self) -> Optional[float]:
        """Score of the seed program, or None if unavailable."""
        if not self.database or not self.database.programs or not self.initial_program_solution:
            return None

        seed_solution = self.initial_program_solution
        seed_prog = None
        for prog in self.database.programs.values():
            if prog.solution == seed_solution:
                seed_prog = prog
                break
        if seed_prog is None:
            for prog in self.database.programs.values():
                if prog.iteration_found == 0:
                    seed_prog = prog
                    break

        if seed_prog and seed_prog.metrics:
            return get_score(seed_prog.metrics)
        return None
````

## → Calls
- [[IO-Program.iteration_found]]
- [[IO-Program.metrics]]
- [[IO-Program.solution]]
- [[IO-metrics.get_score]]

## ← Called by
_(entry point — nothing in this graph calls it)_
