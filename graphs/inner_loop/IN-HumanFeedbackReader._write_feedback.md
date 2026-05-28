---
name: IN-HumanFeedbackReader._write_feedback
description: method in skydiscover/context_builder/human_feedback.py (context-builder)
metadata:
  type: project
---

# HumanFeedbackReader._write_feedback

**File:** `skydiscover/context_builder/human_feedback.py:155`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _write_feedback(self, text: str) -> None:
        """Write feedback text to the file, preserving the comment header."""
        with open(self.path, "w") as f:
            if text:
                f.write(_INITIAL_TEMPLATE + "\n" + text + "\n")
            else:
                f.write(_INITIAL_TEMPLATE)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IN-HumanFeedbackReader.write_from_dashboard]]
