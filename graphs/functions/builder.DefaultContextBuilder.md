---
name: builder.DefaultContextBuilder
description: class in skydiscover/context_builder/default/builder.py (context-builder)
metadata:
  type: project
---

# builder.DefaultContextBuilder

**File:** `skydiscover/context_builder/default/builder.py:43`  
**Kind:** class  
**Layer:** #context-builder

## Source
````python
class DefaultContextBuilder(ContextBuilder):
    """
    Builds LLM prompts from current program, metrics, and context programs.
    """

````

## → Calls
- [[base.ContextBuilder]]

## ← Called by
- [[DiscoveryController.__init__]]
- [[DiscoveryController._init_context_builder]]
- [[EvoxContextBuilder.build_prompt]]
- [[builder.AdaEvolveContextBuilder]]
- [[builder.EvoxContextBuilder]]
- [[builder.GEPANativeContextBuilder]]
