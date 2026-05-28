---
name: MonitorServer._get_top_k_programs
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer._get_top_k_programs

**File:** `skydiscover/extras/monitor/server.py:829`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    def _get_top_k_programs(self) -> List[Dict[str, Any]]:
        """Get top-k programs by score across all islands."""
        if not self._programs:
            return []
        scored = [p for p in self._programs if isinstance(p.get("score"), (int, float))]
        scored.sort(key=lambda p: p["score"], reverse=True)

        # Deduplicate by score (keep best per unique score to show diversity)
        seen_scores = set()
        unique = []
        for p in scored:
            key = round(p["score"], 6)
            if key not in seen_scores:
                seen_scores.add(key)
                unique.append(p)
            if len(unique) >= self._summary_top_k:
                break
        # Fall back to just top-k if not enough unique
        if len(unique) < self._summary_top_k:
            unique = scored[: self._summary_top_k]
        return unique
````

## → Calls
- [[LangFuseTracer.get]]
- [[MonitorServer.__init__]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[MonitorServer._trigger_summary]]
