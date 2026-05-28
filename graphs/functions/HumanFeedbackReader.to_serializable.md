---
name: HumanFeedbackReader.to_serializable
description: method in skydiscover/context_builder/human_feedback.py (context-builder)
metadata:
  type: project
---

# HumanFeedbackReader.to_serializable

**File:** `skydiscover/context_builder/human_feedback.py:147`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def to_serializable(self) -> dict:
        """Return current state for pickling to Island workers."""
        return {
            "feedback_text": self._last_content,
            "mode": self.mode,
            "current_prompt": self._current_system_prompt,
        }
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
_(entry point — nothing in this graph calls it)_
