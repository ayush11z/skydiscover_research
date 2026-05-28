---
name: database.AdaEvolveDatabase
description: class in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# database.AdaEvolveDatabase

**File:** `skydiscover/search/adaevolve/database.py:150`  
**Kind:** class  
**Layer:** #adaevolve

## Source
````python
class AdaEvolveDatabase(ProgramDatabase):
    """
    AdaEvolve population database with adaptive multi-island search.

    Key Design Principles:
    1. MultiDimensionalAdapter handles ALL per-island adaptive state
    2. No separate island arrays - adapter.states[i] is the adaptive state for island i
    3. UnifiedArchive per island for quality-diversity (can be disabled for ablation)
    4. No explicit stagnation tracking - search intensity handles exploration automatically
    5. UCB with decayed magnitude rewards prevents breakthrough memory problem
    6. Dynamic island spawning when global productivity drops
    7. Paradigm breakthrough for high-level strategy shifts
    """

````

## → Calls
- [[base_database.ProgramDatabase]]

## ← Called by
_(entry point — nothing in this graph calls it)_
