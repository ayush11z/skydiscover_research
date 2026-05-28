---
name: MonitorServer.set_feedback_reader
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer.set_feedback_reader

**File:** `skydiscover/extras/monitor/server.py:175`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    def set_feedback_reader(self, reader: Any) -> None:
        """Attach a HumanFeedbackReader for dashboard human feedback controls."""
        self._feedback_reader = reader
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[MonitorServer._consume_queue]]
- [[MonitorServer._get_feedback_state]]
- [[MonitorServer._handle_client_msg]]
- [[Runner._setup_human_feedback]]
- [[monitor.start_monitor]]
