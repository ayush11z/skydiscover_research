---
name: IN-DiscoveryController.postprocess_result
description: method in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# DiscoveryController.postprocess_result

**File:** `skydiscover/search/default_discovery_controller.py:899`  
**Kind:** method  
**Layer:** #inner-loop

## Source
````python
    async def postprocess_result(
        self, result: SerializableResult, iteration_number: int, verbose: bool = True
    ):
        """
        Process the iteration result and return the best program from the database.

        Used by co-evolution where evaluation can be delayed.
        """
        self._process_iteration_result(
            result, iteration_number, checkpoint_callback=None, verbose=verbose
        )
        return self.database.get_best_program()
````

## → Calls
- [[IN-DiscoveryController._process_iteration_result]]
- [[IN-ProgramDatabase.get_best_program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
