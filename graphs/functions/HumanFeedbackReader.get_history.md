---
name: HumanFeedbackReader.get_history
description: method in skydiscover/context_builder/human_feedback.py (context-builder)
metadata:
  type: project
---

# HumanFeedbackReader.get_history

**File:** `skydiscover/context_builder/human_feedback.py:143`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def get_history(self) -> list:
        """Return the full feedback usage history."""
        return list(self._history)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[MonitorServer._get_feedback_state]]
- [[MonitorServer._handle_client_msg]]
