---
name: config.EvolveDatabaseConfig
description: class in skydiscover/config.py (config)
metadata:
  type: project
---

# config.EvolveDatabaseConfig

**File:** `skydiscover/config.py:350`  
**Kind:** class  
**Layer:** #config

## Source
````python
class EvolveDatabaseConfig(DatabaseConfig):
    """Read database from a file."""

    database_file_path: Optional[str] = None
````

## → Calls
- [[config.DatabaseConfig]]

## ← Called by
- [[config.EvoxDatabaseConfig]]
