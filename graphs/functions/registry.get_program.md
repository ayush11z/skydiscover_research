---
name: registry.get_program
description: function in skydiscover/search/registry.py (search-core)
metadata:
  type: project
---

# registry.get_program

**File:** `skydiscover/search/registry.py:80`  
**Kind:** function  
**Layer:** #search-core

## Source
````python
def get_program(
    config: Config,
    initial_program_solution: str,
    initial_program_id: str,
    initial_metrics: Dict[str, Any],
    start_iteration: int,
) -> Program:
    """
    Create an initial Program instance appropriate to the search type.

    Supports both registered program classes and dynamic loading for "evox" type
    when a custom database_file_path is specified.
    """
    search_type = config.search.type

    if search_type == "evox" and getattr(config.search.database, "database_file_path", None):
        logger.info(f"Using search strategy from: {config.search.database.database_file_path}")
        _, program_class = load_database_from_file(config.search.database.database_file_path)
        return program_class(
            id=initial_program_id,
            solution=initial_program_solution,
            language=config.language,
            metrics=initial_metrics,
            iteration_found=start_iteration,
        )

    program_class = _PROGRAM_REGISTRY.get(search_type, Program)
    return program_class(
        id=initial_program_id,
        solution=initial_program_solution,
        language=config.language,
        metrics=initial_metrics,
        iteration_found=start_iteration,
    )
````

## → Calls
- [[Config.language]]
- [[Config.search]]
- [[Program.language]]
- [[base_database.Program]]
- [[config.Config]]
- [[discovery_utils.load_database_from_file]]
- [[registry._PROGRAM_REGISTRY]]

## ← Called by
- [[CoEvolutionController._initialize_first_search_program]]
- [[Runner._add_initial_program]]
