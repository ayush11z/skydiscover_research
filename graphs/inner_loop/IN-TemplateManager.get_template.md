---
name: IN-TemplateManager.get_template
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
- [[IN-EvoxContextBuilder.__init__]]
- [[IN-EvoxContextBuilder._generate_problem_context_summary_async]]
- [[IN-EvoxContextBuilder._generate_stats_insight_async]]
- [[IN-EvoxContextBuilder.build_prompt]]
