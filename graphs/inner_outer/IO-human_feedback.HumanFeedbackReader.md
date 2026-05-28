---
name: IO-human_feedback.HumanFeedbackReader
description: class in skydiscover/context_builder/human_feedback.py (context-builder)
metadata:
  type: project
---

# human_feedback.HumanFeedbackReader

**File:** `skydiscover/context_builder/human_feedback.py:31`  
**Kind:** class  
**Layer:** #context-builder

## Source
````python
class HumanFeedbackReader:
    """
    Reads human feedback from a markdown file on disk.

    The dashboard writes via write_from_dashboard(); the discovery loop
    reads via read(). External editors can also modify the file directly.

    Supports two modes:
    - "append" (default): feedback is appended to the system message
    - "replace": feedback replaces the system message entirely
    """

````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-Runner._setup_human_feedback]]
