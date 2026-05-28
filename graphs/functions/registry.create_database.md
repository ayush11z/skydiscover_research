---
name: registry.create_database
description: function in skydiscover/search/registry.py (search-core)
metadata:
  type: project
---

# registry.create_database

**File:** `skydiscover/search/registry.py:55`  
**Kind:** function  
**Layer:** #search-core

## Source
````python
def create_database(search_type: str, config: DatabaseConfig) -> ProgramDatabase:
    """
    Create a database instance for a given search type.

    Supports both registered search types and dynamic loading for "evox"/"evolve" types
    when a custom database_file_path is specified.
    """
    if search_type in ("evox", "evolve") and getattr(config, "database_file_path", None):
        database_class, program_class = load_database_from_file(config.database_file_path)
        db = database_class(search_type, config)
        db._program_class = program_class
        return db

    if search_type not in _DATABASE_REGISTRY:
        available_types = ", ".join(sorted(_DATABASE_REGISTRY.keys()))
        raise ValueError(
            f"Unknown search type: '{search_type}'. "
            f"Available types: {available_types}. "
            f"For 'evox'/'evolve' type with custom database, set config.search.database.database_file_path"
        )

    database_class = _DATABASE_REGISTRY[search_type]
    return database_class(search_type, config)
````

## → Calls
- [[EvolveDatabaseConfig.database_file_path]]
- [[base_database.ProgramDatabase]]
- [[config.DatabaseConfig]]
- [[discovery_utils.load_database_from_file]]
- [[registry._DATABASE_REGISTRY]]

## ← Called by
- [[Runner.__init__]]
- [[Runner._add_initial_program]]
- [[Runner._push_existing_to_monitor]]
- [[Runner._start_monitor]]
- [[Runner._sync_database]]
- [[Runner.initial_score]]
- [[Runner.run]]
- [[registry.setup_search]]
