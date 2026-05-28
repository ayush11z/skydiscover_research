---
name: HumanFeedbackReader.apply_feedback
description: method in skydiscover/context_builder/human_feedback.py (context-builder)
metadata:
  type: project
---

# HumanFeedbackReader.apply_feedback

**File:** `skydiscover/context_builder/human_feedback.py:104`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def apply_feedback(self, prompt: dict) -> dict:
        """Apply current feedback to a prompt dict.

        In append mode, feedback is added after the system message.
        In replace mode, feedback replaces the system message entirely.
        Returns the modified prompt.
        """
        feedback = self.read()
        if not feedback:
            return prompt

        if self.mode == "replace":
            prompt["system"] = feedback
        else:
            prompt["system"] = prompt["system"] + "\n\n## Human Guidance\n" + feedback
        return prompt
````

## → Calls
- [[HumanFeedbackReader.read]]

## ← Called by
- [[DiscoveryController._run_from_scratch_iteration]]
- [[DiscoveryController._run_iteration]]
