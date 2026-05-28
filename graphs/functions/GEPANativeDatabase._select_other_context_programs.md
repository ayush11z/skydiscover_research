---
name: GEPANativeDatabase._select_other_context_programs
description: method in skydiscover/search/gepa_native/database.py (gepa)
metadata:
  type: project
---

# GEPANativeDatabase._select_other_context_programs

**File:** `skydiscover/search/gepa_native/database.py:340`  
**Kind:** method  
**Layer:** #gepa

## Source
````python
    def _select_other_context_programs(
        self, parent_id: str, num_context_programs: int
    ) -> List[Program]:
        """Select context programs from elite pool + metric leaders.

        Picks top programs from the elite pool (excluding the parent),
        then appends any metric-best programs not already included.
        """
        seen = {parent_id}
        other_context_programs: List[Program] = []

        # Top programs from elite pool (excluding parent)
        for pid in self.elite_pool:
            if pid in seen or pid not in self.programs:
                continue
            other_context_programs.append(self.programs[pid])
            seen.add(pid)
            if len(other_context_programs) >= num_context_programs:
                break

        # Add metric-best programs not already included
        for _metric, (pid, _score) in self.metric_best.items():
            if pid in seen or pid not in self.programs:
                continue
            other_context_programs.append(self.programs[pid])
            seen.add(pid)

        return other_context_programs[:num_context_programs]
````

## → Calls
- [[CheckpointManager.load]]
- [[GEPANativeDatabase.__init__]]
- [[base_database.Program]]

## ← Called by
- [[GEPANativeDatabase.sample]]
