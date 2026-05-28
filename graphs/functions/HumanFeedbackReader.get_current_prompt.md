---
name: HumanFeedbackReader.get_current_prompt
description: method in skydiscover/context_builder/human_feedback.py (context-builder)
metadata:
  type: project
---

# HumanFeedbackReader.get_current_prompt

**File:** `skydiscover/context_builder/human_feedback.py:125`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def get_current_prompt(self) -> str:
        """Return the current system prompt."""
        return self._current_system_prompt
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[MonitorServer._get_feedback_state]]
- [[MonitorServer._handle_client_msg]]
