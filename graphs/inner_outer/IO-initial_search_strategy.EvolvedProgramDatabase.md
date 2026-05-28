---
name: IO-initial_search_strategy.EvolvedProgramDatabase
description: class in skydiscover/search/evox/database/initial_search_strategy.py (evox)
metadata:
  type: project
---

# initial_search_strategy.EvolvedProgramDatabase

**File:** `skydiscover/search/evox/database/initial_search_strategy.py:18`  
**Kind:** class  
**Layer:** #evox

## Source
````python
class EvolvedProgramDatabase(ProgramDatabase):
    """Initial search strategy database.

    Demonstrates the full label mechanism so evolved strategies can build on it:
    - Tracks per-iteration improvement in add() so sample() can read state.
    - Uses DIVERGE_LABEL when the population stagnates at a low score.
    - Uses REFINE_LABEL when a high-scoring program has stalled recently.
    - Falls back to empty "" (no label) when the search is making steady progress.
    """

````

## → Calls
- [[IO-base_database.ProgramDatabase]]

## ← Called by
_(entry point — nothing in this graph calls it)_
