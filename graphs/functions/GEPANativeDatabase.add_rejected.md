---
name: GEPANativeDatabase.add_rejected
description: method in skydiscover/search/gepa_native/database.py (gepa)
metadata:
  type: project
---

# GEPANativeDatabase.add_rejected

**File:** `skydiscover/search/gepa_native/database.py:167`  
**Kind:** method  
**Layer:** #gepa

## Source
````python
    def add_rejected(self, program: Program) -> None:
        """Store a rejected program for reflective prompting.

        The program is NOT added to the elite pool or ``self.programs``.
        """
        self.rejection_history.append(program)
````

## → Calls
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
