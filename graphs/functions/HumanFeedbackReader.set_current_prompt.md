---
name: HumanFeedbackReader.set_current_prompt
description: method in skydiscover/context_builder/human_feedback.py (context-builder)
metadata:
  type: project
---

# HumanFeedbackReader.set_current_prompt

**File:** `skydiscover/context_builder/human_feedback.py:121`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def set_current_prompt(self, system_prompt: str) -> None:
        """Store the current system prompt for dashboard visibility."""
        self._current_system_prompt = system_prompt
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[DiscoveryController._run_from_scratch_iteration]]
- [[DiscoveryController._run_iteration]]
- [[gepa_backend.run]]
- [[openevolve_backend.run]]
- [[openevolve_backend.run._poll_programs]]
- [[shinkaevolve_backend.run]]
- [[shinkaevolve_backend.run._poll_programs]]
