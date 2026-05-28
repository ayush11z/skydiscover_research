---
name: IN-DiscoveryController._inject_evaluator_context
description: method in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# DiscoveryController._inject_evaluator_context

**File:** `skydiscover/search/default_discovery_controller.py:128`  
**Kind:** method  
**Layer:** #inner-loop

## Source
````python
    def _inject_evaluator_context(self):
        """Load evaluator/task description and prepend to the system message.

        For Harbor tasks this loads instruction.md; for containerized benchmarks
        it loads the evaluator source files. The content gives the LLM essential
        context about the problem it needs to solve.

        Controlled by ``evaluator.inject_evaluator_context`` (default False).
        """
        if not self.config.evaluator.inject_evaluator_context:
            return

        from skydiscover.search.utils.discovery_utils import load_evaluator_code

        task_description = load_evaluator_code(self.evaluation_file)
        if not task_description:
            return

        ctx = self.config.context_builder
        existing = ctx.system_message or ""
        # Prepend the task description so the LLM always sees it.
        ctx.system_message = (
            f"# Task Description\n\n{task_description}\n\n{existing}"
            if existing
            else f"# Task Description\n\n{task_description}"
        )
````

## → Calls
- [[IN-DiscoveryControllerInput.evaluation_file]]

## ← Called by
- [[IN-DiscoveryController.__init__]]
