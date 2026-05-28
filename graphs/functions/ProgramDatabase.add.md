---
name: ProgramDatabase.add
description: method in skydiscover/search/base_database.py (database)
metadata:
  type: project
---

# ProgramDatabase.add

**File:** `skydiscover/search/base_database.py:121`  
**Kind:** method  
**Layer:** #database

## What it does
Adds a new program to the population. May evict lower-scoring programs depending on the database type (top-k, beam, evox, etc.).

## Source
````python
    def add(self, program: Program, iteration: Optional[int] = None, **kwargs: Any) -> str:
        """Add a program to the database.

        Args:
            program: Program to add.
            iteration: Current iteration (for tracking).

        Returns:
            Program ID.
        """
        ...
````

## → Calls
- [[base_database.Program]]

## ← Called by
- [[AgenticGenerator._tool_read_file]]
- [[ClaudeCodeController.run_discovery]]
- [[CoEvolutionController._migrate_to_db]]
- [[CoEvolutionController._restore_fallback_database]]
- [[CoEvolutionController._wrap_add_method]]
- [[DiscoveryController._process_iteration_result]]
- [[Runner._add_initial_program]]
- [[_wrap_add_method.wrapped_add]]
- [[search_strategy_evaluator.evaluate]]
