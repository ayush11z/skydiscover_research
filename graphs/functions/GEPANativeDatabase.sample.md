---
name: GEPANativeDatabase.sample
description: method in skydiscover/search/gepa_native/database.py (gepa)
metadata:
  type: project
---

# GEPANativeDatabase.sample

**File:** `skydiscover/search/gepa_native/database.py:140`  
**Kind:** method  
**Layer:** #gepa

## Source
````python
    def sample(
        self,
        num_context_programs: Optional[int] = 4,
        **kwargs: Any,
    ) -> Tuple[Dict[str, Program], Dict[str, List[Program]]]:
        """Sample a parent and context programs.

        Uses epsilon-greedy selection for the parent and top-of-pool +
        metric leaders for other context programs.

        Returns:
            Tuple of ({"": parent}, {"": [other context, ...]}).
        """
        if not self.programs:
            raise ValueError("Cannot sample: no programs in database")

        parent = self._select_parent()
        other_context_programs = self._select_other_context_programs(
            parent.id, num_context_programs or 4
        )

        return {"": parent}, {"": other_context_programs}
````

## → Calls
- [[CheckpointManager.load]]
- [[GEPANativeDatabase._select_other_context_programs]]
- [[GEPANativeDatabase._select_parent]]
- [[Program.id]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
