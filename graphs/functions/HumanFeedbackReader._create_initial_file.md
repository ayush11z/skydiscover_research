---
name: HumanFeedbackReader._create_initial_file
description: method in skydiscover/context_builder/human_feedback.py (context-builder)
metadata:
  type: project
---

# HumanFeedbackReader._create_initial_file

**File:** `skydiscover/context_builder/human_feedback.py:51`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _create_initial_file(self) -> None:
        """Create the feedback file with instructions if it doesn't exist."""
        if not os.path.exists(self.path):
            os.makedirs(os.path.dirname(self.path), exist_ok=True)
            with open(self.path, "w") as f:
                f.write(_INITIAL_TEMPLATE)
            logger.info(f"Created human feedback file: {self.path}")
````

## → Calls
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]

## ← Called by
- [[HumanFeedbackReader.__init__]]
