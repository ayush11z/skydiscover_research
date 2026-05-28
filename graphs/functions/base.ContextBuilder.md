---
name: base.ContextBuilder
description: class in skydiscover/context_builder/base.py (context-builder)
metadata:
  type: project
---

# base.ContextBuilder

**File:** `skydiscover/context_builder/base.py:10`  
**Kind:** class  
**Layer:** #context-builder

## Source
````python
class ContextBuilder(ABC):
    """Abstract base for building LLM prompts.

    Subclass this and implement build_prompt(). Each subclass sets up its
    own template_manager and any other resources it needs.
    """

````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[DefaultContextBuilder.__init__]]
- [[DefaultContextBuilder._get_system_message]]
- [[DefaultContextBuilder._identify_improvement_areas]]
- [[DefaultContextBuilder.build_prompt]]
- [[EvoxContextBuilder.build_prompt]]
- [[LLMJudge.__init__]]
- [[builder.DefaultContextBuilder]]
