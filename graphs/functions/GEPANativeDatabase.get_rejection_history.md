---
name: GEPANativeDatabase.get_rejection_history
description: method in skydiscover/search/gepa_native/database.py (gepa)
metadata:
  type: project
---

# GEPANativeDatabase.get_rejection_history

**File:** `skydiscover/search/gepa_native/database.py:174`  
**Kind:** method  
**Layer:** #gepa

## Source
````python
    def get_rejection_history(self, limit: Optional[int] = None) -> List[Program]:
        """Return recent rejected programs, most-recent last.

        Args:
            limit: If given, return only the *limit* most recent entries.
        """
        items = list(self.rejection_history)
        if limit is not None:
            items = items[-limit:]
        return items
````

## → Calls
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
