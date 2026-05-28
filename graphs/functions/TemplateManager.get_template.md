---
name: TemplateManager.get_template
description: method in skydiscover/context_builder/utils.py (context-builder)
metadata:
  type: project
---

# TemplateManager.get_template

**File:** `skydiscover/context_builder/utils.py:32`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def get_template(self, name: str) -> str:
        if name not in self.templates:
            raise ValueError(f"Template '{name}' not found")
        return self.templates[name]
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveContextBuilder._format_previous_attempts]]
- [[DefaultContextBuilder._format_previous_attempts]]
- [[DefaultContextBuilder._get_system_message]]
- [[DefaultContextBuilder.build_prompt]]
- [[EvoxContextBuilder.__init__]]
- [[EvoxContextBuilder._generate_problem_context_summary_async]]
- [[EvoxContextBuilder._generate_stats_insight_async]]
- [[EvoxContextBuilder.build_prompt]]
- [[LLMJudge.evaluate]]
