---
name: HumanFeedbackReader.write_from_dashboard
description: method in skydiscover/context_builder/human_feedback.py (context-builder)
metadata:
  type: project
---

# HumanFeedbackReader.write_from_dashboard

**File:** `skydiscover/context_builder/human_feedback.py:89`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def write_from_dashboard(self, text: str) -> None:
        """
        Write feedback from the dashboard UI.
        Pass empty string to clear feedback.
        """
        self._write_feedback(text)
````

## → Calls
- [[HumanFeedbackReader._write_feedback]]

## ← Called by
- [[MonitorServer._handle_client_msg]]
