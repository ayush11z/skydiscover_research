---
name: base_database.ProgramDatabase
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
- [[AdaEvolveDatabase._expand_to_island_count]]
- [[AdaEvolveDatabase._spawn_island]]
- [[AdaEvolveDatabase.add]]
- [[AdaEvolveDatabase.add_merged_program]]
- [[AdaEvolveDatabase.load]]
- [[AdaEvolveDatabase.save]]
- [[BeamSearchDatabase.add]]
- [[BeamSearchDatabase.save]]
- [[BestOfNDatabase.add]]
- [[ClaudeCodeDatabase.add]]
- [[EvolvedProgramDatabase.add]]
- [[EvolvedProgramDatabase.sample]]
- [[GEPANativeDatabase.add]]
- [[GEPANativeDatabase.save]]
- [[LLMJudge.__init__]]
- [[OpenEvolveNativeDatabase.add]]
- [[OpenEvolveNativeDatabase.save]]
- [[SearchStrategyDatabase.add]]
- [[TopKDatabase.add]]
- [[database.AdaEvolveDatabase]]
- [[database.BeamSearchDatabase]]
- [[database.BestOfNDatabase]]
- [[database.ClaudeCodeDatabase]]
- [[database.GEPANativeDatabase]]
- [[database.OpenEvolveNativeDatabase]]
- [[database.TopKDatabase]]
- [[default_discovery_controller.DiscoveryControllerInput]]
- [[discovery_utils.load_database_from_file]]
- [[initial_search_strategy.EvolvedProgramDatabase]]
- [[registry.create_database]]
- [[registry.register_database]]
- [[search_strategy_db.SearchStrategyDatabase]]
- [[search_strategy_evaluator.evaluate]]
