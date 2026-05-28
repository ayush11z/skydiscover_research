---
name: AdaEvolveDatabase.get_program_proxy_score
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.get_program_proxy_score

**File:** `skydiscover/search/adaevolve/database.py:1526`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_program_proxy_score(self, program: Optional[Program]) -> float:
        """Public wrapper for the scalar proxy used by AdaEvolve internals."""
        if program is None:
            return float("-inf")
        return self._get_multiobjective_proxy_score(program)
````

## → Calls
- [[AdaEvolveDatabase._get_multiobjective_proxy_score]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
