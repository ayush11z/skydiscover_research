---
name: OpenEvolveNativeDatabase.sample
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase.sample

**File:** `skydiscover/search/openevolve_native/database.py:173`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def sample(
        self,
        num_context_programs: Optional[int] = 4,
        **kwargs: Any,
    ) -> Tuple[Program, List[Program]]:
        if not self.programs:
            raise ValueError("Cannot sample: no programs in database")

        parent = self._sample_parent()
        if num_context_programs is None:
            num_context_programs = 4
        other_context_programs = self._sample_other_context_programs(parent, n=num_context_programs)

        logger.debug(
            "Sampled parent %s from island %d, %d other context programs",
            parent.id,
            self.current_island,
            len(other_context_programs),
        )

        # Round-robin island rotation AFTER sampling so the first call
        # uses island 0 (OpenEvolve's controller calls next_island()
        # separately; we do it here because DiscoveryController doesn't).
        self.current_island = (self.current_island + 1) % self.num_islands

        return parent, other_context_programs
````

## → Calls
- [[CheckpointManager.load]]
- [[OpenEvolveNativeDatabase._sample_other_context_programs]]
- [[OpenEvolveNativeDatabase._sample_parent]]
- [[Program.id]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
