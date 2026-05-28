---
name: MonitorServer._get_feedback_state
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer._get_feedback_state

**File:** `skydiscover/extras/monitor/server.py:207`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    def _get_feedback_state(self) -> Dict[str, Any]:
        """Return current human feedback state."""
        if not self._feedback_reader:
            return {
                "human_feedback_enabled": False,
                "feedback_text": "",
                "feedback_active": False,
                "human_feedback_mode": "append",
                "human_feedback_current_prompt": "",
                "human_feedback_history": [],
            }
        text = self._feedback_reader.read()
        return {
            "human_feedback_enabled": True,
            "feedback_text": text,
            "feedback_active": bool(text),
            "human_feedback_mode": self._feedback_reader.mode,
            "human_feedback_current_prompt": self._feedback_reader.get_current_prompt(),
            "human_feedback_history": self._feedback_reader.get_history(),
        }
````

## → Calls
- [[HumanFeedbackReader.get_current_prompt]]
- [[HumanFeedbackReader.get_history]]
- [[HumanFeedbackReader.read]]
- [[MonitorServer.set_feedback_reader]]

## ← Called by
- [[MonitorServer._build_init_state]]
- [[MonitorServer._handle_client_msg]]
