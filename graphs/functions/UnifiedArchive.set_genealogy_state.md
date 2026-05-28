---
name: UnifiedArchive.set_genealogy_state
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive.set_genealogy_state

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:930`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def set_genealogy_state(self, state: Dict[str, Any]) -> None:
        """
        Restore genealogy state from checkpoint.

        Only restores relationships for programs currently in the archive.

        Args:
            state: Dict with parents and children mappings from get_genealogy_state()
        """
        if not state:
            return

        # Restore parents (only for programs in archive)
        parents_data = state.get("parents", {})
        for prog_id, parent_list in parents_data.items():
            if prog_id in self._programs:
                self._parents[prog_id] = list(parent_list)

        # Restore children (only relationships where both exist in archive)
        children_data = state.get("children", {})
        for parent_id, child_list in children_data.items():
            valid_children = [cid for cid in child_list if cid in self._programs]
            if valid_children:
                self._children[parent_id] = valid_children
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
_(entry point — nothing in this graph calls it)_
