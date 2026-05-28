---
name: AdaEvolveDatabase.get_children
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.get_children

**File:** `skydiscover/search/adaevolve/database.py:1714`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_children(self, parent_id: str, limit: int = 5) -> List[Program]:
        """
        Get recent children of a parent on the current island.

        Used by controller for sibling context - shows what mutations
        have been tried on this parent before.

        Args:
            parent_id: ID of the parent program
            limit: Maximum number of children to return

        Returns:
            List of child programs (most recent last)
        """
        if self.use_unified_archive and self.archives:
            archive = self.archives[self.current_island]

            # Use archive's genealogy tracking if available
            if hasattr(archive, "get_children"):
                children = archive.get_children(parent_id)
                return children[-limit:]

            # Fallback: scan all programs (less efficient)
            children = [p for p in archive.get_all() if getattr(p, "parent_id", None) == parent_id]
        else:
            # Legacy mode: use children_map
            child_ids = self.children_map[self.current_island].get(parent_id, [])
            children = [self.programs[cid] for cid in child_ids if cid in self.programs]

        # Sort by iteration_found to get most recent
        children.sort(key=lambda p: getattr(p, "iteration_found", 0))
        return children[-limit:]
````

## → Calls
- [[CheckpointManager.load]]
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
