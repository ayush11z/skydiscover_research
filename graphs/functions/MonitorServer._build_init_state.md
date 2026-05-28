---
name: MonitorServer._build_init_state
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer._build_init_state

**File:** `skydiscover/extras/monitor/server.py:228`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    def _build_init_state(self) -> Dict[str, Any]:
        """Build the full init_state payload for new/reconnecting WS clients."""
        state = {
            "type": "init_state",
            "programs": self._programs,
            "best_program_id": self._best_program_id,
            "stats": self._stats,
            "config_summary": self._config_summary,
            "summary_enabled": bool(self._summary_model),
            "summary_model": self._summary_model or "",
            "summary_text": self._summary_text,
            "summary_generating": self._summary_generating,
        }
        state.update(self._get_feedback_state())
        return state
````

## → Calls
- [[LangFuseTracer.get]]
- [[MonitorServer._get_feedback_state]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[MonitorServer._handle_client_msg]]
- [[MonitorServer._handle_ws]]
