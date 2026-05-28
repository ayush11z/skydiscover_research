---
name: IO-EvolvedProgramDatabase.__init__
description: method in skydiscover/search/evox/database/initial_search_strategy.py (evox)
metadata:
  type: project
---

# EvolvedProgramDatabase.__init__

**File:** `skydiscover/search/evox/database/initial_search_strategy.py:28`  
**Kind:** method  
**Layer:** #evox

## Source
````python
    def __init__(self, name: str, config: DatabaseConfig, **kwargs: Any):
        super().__init__(name, config, **kwargs)
        self.initial_program = None
        # State tracked in add() — read in sample()
        self._best_score_history: List[float] = []   # one entry per iteration
        self._stagnant_count: int = 0
        self._last_best: Optional[float] = None
````

## → Calls
- [[IO-ProgramDatabase.__init__]]

## ← Called by
- [[IO-EvolvedProgramDatabase.add]]
