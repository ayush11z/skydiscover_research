---
name: config.DatabaseConfig
description: class in skydiscover/config.py (config)
metadata:
  type: project
---

# config.DatabaseConfig

**File:** `skydiscover/config.py:342`  
**Kind:** class  
**Layer:** #config

## Source
````python
class DatabaseConfig:
    """Base configuration shared by all database types."""

    db_path: Optional[str] = None
    log_prompts: bool = True
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveDatabase.__init__]]
- [[AdaEvolveDatabase._init_archives]]
- [[BeamSearchDatabase.__init__]]
- [[BestOfNDatabase.__init__]]
- [[CheckpointManager.__init__]]
- [[Config.from_dict]]
- [[EvolvedProgramDatabase.__init__]]
- [[GEPANativeDatabase.__init__]]
- [[OpenEvolveNativeDatabase.__init__]]
- [[ProgramDatabase.__init__]]
- [[SearchStrategyDatabase.__init__]]
- [[TopKDatabase.__init__]]
- [[config.AdaEvolveDatabaseConfig]]
- [[config.BeamSearchDatabaseConfig]]
- [[config.BestOfNDatabaseConfig]]
- [[config.ClaudeCodeConfig]]
- [[config.EvolveDatabaseConfig]]
- [[config.GEPANativeDatabaseConfig]]
- [[config.OpenEvolveNativeDatabaseConfig]]
- [[config.SearchConfig]]
- [[registry.create_database]]
- [[search_strategy_evaluator.evaluate]]
- [[shinkaevolve_backend._map_config]]
