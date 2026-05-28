---
name: IO-HumanFeedbackReader.set_mode
description: method in skydiscover/context_builder/human_feedback.py (context-builder)
metadata:
  type: project
---

# HumanFeedbackReader.set_mode

**File:** `skydiscover/context_builder/human_feedback.py:96`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def set_mode(self, mode: str) -> None:
        """Set feedback mode: 'append' or 'replace'."""
        if mode not in ("append", "replace"):
            logger.warning(f"Invalid human feedback mode '{mode}', ignoring")
            return
        self.mode = mode
        logger.info(f"Human feedback mode set to: {mode}")
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
_(entry point — nothing in this graph calls it)_
