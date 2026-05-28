---
name: IN-HumanFeedbackReader.log_usage
description: method in skydiscover/context_builder/human_feedback.py (context-builder)
metadata:
  type: project
---

# HumanFeedbackReader.log_usage

**File:** `skydiscover/context_builder/human_feedback.py:129`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def log_usage(self, iteration: int, feedback_text: str, mode: str) -> None:
        """Record that feedback was applied at a given iteration."""
        entry = {
            "iteration": iteration,
            "timestamp": _time.time(),
            "text": feedback_text,
            "mode": mode,
        }
        self._history.append(entry)
        logger.info(
            f"Human feedback logged: iteration={iteration}, mode={mode}, "
            f"chars={len(feedback_text)}"
        )
````

## → Calls
- [[IN-HumanFeedbackReader.__init__]]

## ← Called by
_(entry point — nothing in this graph calls it)_
