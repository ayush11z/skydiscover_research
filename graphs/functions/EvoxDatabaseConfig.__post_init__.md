---
name: EvoxDatabaseConfig.__post_init__
description: method in skydiscover/config.py (config)
metadata:
  type: project
---

# EvoxDatabaseConfig.__post_init__

**File:** `skydiscover/config.py:367`  
**Kind:** method  
**Layer:** #config

## Source
````python
    def __post_init__(self):
        if self.database_file_path is None:
            # Initial guide strategy for the solution discovery
            self.database_file_path = str(self._evox_database_dir / "initial_search_strategy.py")
        if self.evaluation_file is None:
            # Dummy evaluator for the guide strategy
            self.evaluation_file = str(self._evox_database_dir / "search_strategy_evaluator.py")
        if self.config_path is None:
            # Default config for the guide strategy
            self.config_path = str(self._evox_config_dir / "search.yaml")
````

## → Calls
- [[EvolveDatabaseConfig.database_file_path]]
- [[EvoxDatabaseConfig._evox_config_dir]]
- [[EvoxDatabaseConfig._evox_database_dir]]

## ← Called by
_(entry point — nothing in this graph calls it)_
