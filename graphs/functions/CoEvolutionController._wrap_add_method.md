---
name: CoEvolutionController._wrap_add_method
description: method in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# CoEvolutionController._wrap_add_method

**File:** `skydiscover/search/evox/controller.py:569`  
**Kind:** method  
**Layer:** #outer-loop

## Source
````python
    def _wrap_add_method(self, db) -> None:
        """Wrap database.add() to ensure _update_best_program is always called."""
        original_add = db.add

        def wrapped_add(program, iteration=None, **kwargs):
            result = original_add(program, iteration=iteration, **kwargs)
            db._update_best_program(program)  # Idempotent safety for LLM-generated databases
            return result

        db.add = wrapped_add
````

## → Calls
- [[ProgramDatabase.add]]
- [[UnifiedArchive.add]]
- [[_wrap_add_method.wrapped_add]]

## ← Called by
- [[CoEvolutionController._switch_to_new_search_algorithm]]
