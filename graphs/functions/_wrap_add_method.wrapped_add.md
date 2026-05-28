---
name: _wrap_add_method.wrapped_add
description: function in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# _wrap_add_method.wrapped_add

**File:** `skydiscover/search/evox/controller.py:573`  
**Kind:** function  
**Layer:** #outer-loop

## Source
````python
        def wrapped_add(program, iteration=None, **kwargs):
            result = original_add(program, iteration=iteration, **kwargs)
            db._update_best_program(program)  # Idempotent safety for LLM-generated databases
            return result
````

## → Calls
- [[ProgramDatabase._update_best_program]]
- [[ProgramDatabase.add]]
- [[UnifiedArchive.add]]

## ← Called by
- [[CoEvolutionController._wrap_add_method]]
