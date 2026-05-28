---
name: IO-base_database.ProgramDatabase
description: class in skydiscover/search/base_database.py (database)
metadata:
  type: project
---

# base_database.ProgramDatabase

**File:** `skydiscover/search/base_database.py:75`  
**Kind:** class  
**Layer:** #database

## Source
````python
class ProgramDatabase(ABC):
    """
    Abstract base class for program storage and sampling.

    This interface captures the essential operations needed for any discovery process:
    - Add a program to the database
    - Sample a program and context programs to learn from past experiences for the next discovery step
    """

    DIVERGE_LABEL: str = "diverge"
    REFINE_LABEL: str = "refine"

````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-EvolvedProgramDatabase.add]]
- [[IO-EvolvedProgramDatabase.sample]]
- [[IO-SearchStrategyDatabase.add]]
- [[IO-SearchStrategyDatabase.sample]]
- [[IO-default_discovery_controller.DiscoveryControllerInput]]
- [[IO-initial_search_strategy.EvolvedProgramDatabase]]
- [[IO-search_strategy_db.SearchStrategyDatabase]]
- [[IO-search_strategy_evaluator.evaluate]]
