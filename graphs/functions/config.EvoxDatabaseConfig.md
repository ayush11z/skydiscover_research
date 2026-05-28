---
name: config.EvoxDatabaseConfig
description: class in skydiscover/config.py (config)
metadata:
  type: project
---

# config.EvoxDatabaseConfig

**File:** `skydiscover/config.py:357`  
**Kind:** class  
**Layer:** #config

## Source
````python
class EvoxDatabaseConfig(EvolveDatabaseConfig):
    """Evox (co-evolution) database config with built-in defaults."""

    evaluation_file: Optional[str] = None
    config_path: Optional[str] = None
    auto_generate_variation_operators: bool = True

    _evox_config_dir = Path(__file__).parent / "search" / "evox" / "config"
    _evox_database_dir = Path(__file__).parent / "search" / "evox" / "database"

````

## → Calls
- [[config.EvolveDatabaseConfig]]

## ← Called by
_(entry point — nothing in this graph calls it)_
