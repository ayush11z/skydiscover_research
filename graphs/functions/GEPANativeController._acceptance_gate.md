---
name: GEPANativeController._acceptance_gate
description: method in skydiscover/search/gepa_native/controller.py (gepa)
metadata:
  type: project
---

# GEPANativeController._acceptance_gate

**File:** `skydiscover/search/gepa_native/controller.py:240`  
**Kind:** method  
**Layer:** #gepa

## Source
````python
    def _acceptance_gate(self, result: SerializableResult, iteration: int) -> bool:
        """Apply GEPA acceptance gating.

        A child is accepted only if its fitness strictly exceeds the parent's.
        Rejected children are stored in the database's rejection history for
        use in reflective prompting.

        Returns:
            True if the child is accepted, False otherwise.
        """
        child_score = get_score(result.child_program_dict.get("metrics", {}))

        parent_score = 0.0
        if result.parent_id and result.parent_id in self.database.programs:
            parent = self.database.programs[result.parent_id]
            parent_score = get_score(parent.metrics)

        if child_score <= parent_score:
            child = Program.from_dict(result.child_program_dict)
            self.database.add_rejected(child)

            logger.info(
                f"Iteration {iteration}: REJECTED child "
                f"(child_score={child_score:.4f} <= parent_score={parent_score:.4f})"
            )
            self._iterations_without_improvement += 1
            return False

        return True
````

## → Calls
- [[DiscoveryControllerInput.database]]
- [[Program.from_dict]]
- [[Program.parent_id]]
- [[SearchConfig.database]]
- [[SerializableResult.child_program_dict]]
- [[SerializableResult.parent_id]]
- [[default_discovery_controller.DiscoveryController]]
- [[discovery_utils.SerializableResult]]
- [[metrics.get_score]]

## ← Called by
- [[GEPANativeController.run_discovery]]
