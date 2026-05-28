---
name: BeamSearchDatabase._reconstruct_depths
description: method in skydiscover/search/beam_search/database.py (beam-search)
metadata:
  type: project
---

# BeamSearchDatabase._reconstruct_depths

**File:** `skydiscover/search/beam_search/database.py:661`  
**Kind:** method  
**Layer:** #beam-search

## Source
````python
    def _reconstruct_depths(self) -> None:
        """
        Reconstruct depth information for all programs based on parent relationships.

        Uses BFS from root programs (those without parents) to assign depths.
        """
        # Find all root programs (no parent or parent not in database)
        roots = []
        for pid, prog in self.programs.items():
            if not prog.parent_id or prog.parent_id not in self.programs:
                self.depth[pid] = 0
                roots.append(pid)

        # BFS to assign depths
        queue = list(roots)
        visited = set(roots)

        # Build child lookup
        children: Dict[str, List[str]] = defaultdict(list)
        for pid, prog in self.programs.items():
            if prog.parent_id and prog.parent_id in self.programs:
                children[prog.parent_id].append(pid)

        while queue:
            current = queue.pop(0)
            current_depth = self.depth.get(current, 0)

            for child_id in children[current]:
                if child_id not in visited:
                    self.depth[child_id] = current_depth + 1
                    visited.add(child_id)
                    queue.append(child_id)

        # Handle orphaned programs (shouldn't happen but just in case)
        for pid in self.programs:
            if pid not in self.depth:
                self.depth[pid] = 0
                logger.warning(f"Orphaned program {pid}, assigned depth 0")
````

## → Calls
- [[CheckpointManager.load]]
- [[LangFuseTracer.get]]
- [[Program.parent_id]]
- [[ProgramDatabase.get]]
- [[SerializableResult.parent_id]]
- [[UnifiedArchive.get]]

## ← Called by
- [[BeamSearchDatabase._validate_and_reconstruct_beam]]
