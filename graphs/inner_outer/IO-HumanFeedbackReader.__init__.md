---
name: IO-HumanFeedbackReader.__init__
description: method in skydiscover/context_builder/human_feedback.py (context-builder)
metadata:
  type: project
---

# HumanFeedbackReader.__init__

**File:** `skydiscover/context_builder/human_feedback.py:43`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def __init__(self, feedback_file_path: str, mode: str = "append"):
        self.path = os.path.abspath(feedback_file_path)
        self.mode = mode if mode in ("append", "replace") else "append"
        self._last_content: str = ""
        self._current_system_prompt: str = ""
        self._history: list = []
        self._create_initial_file()
````

## → Calls
- [[IO-HumanFeedbackReader._create_initial_file]]

## ← Called by
- [[IO-HumanFeedbackReader.log_usage]]
