---
name: ParadigmTracker.has_active_paradigm
description: method in skydiscover/search/adaevolve/paradigm/tracker.py (adaevolve)
metadata:
  type: project
---

# ParadigmTracker.has_active_paradigm

**File:** `skydiscover/search/adaevolve/paradigm/tracker.py:120`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def has_active_paradigm(self) -> bool:
        """Check if there's an active paradigm available for use."""
        if not self.active_paradigms:
            return False

        # Check if current paradigm is exhausted
        current_uses = self.paradigm_usage_counts.get(self.current_paradigm_index, 0)
        if current_uses >= self.max_paradigm_uses:
            # Try to rotate to next available paradigm
            return self._try_rotate_paradigm()

        return True
````

## → Calls
- [[LangFuseTracer.get]]
- [[ParadigmTracker._try_rotate_paradigm]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[AdaEvolveDatabase.get_comprehensive_iteration_stats]]
- [[AdaEvolveDatabase.has_active_paradigm]]
- [[ParadigmTracker.get_current_paradigm]]
- [[ParadigmTracker.is_paradigm_stagnating]]
