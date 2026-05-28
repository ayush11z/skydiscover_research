---
name: utils.TemplateManager
description: class in skydiscover/context_builder/utils.py (context-builder)
metadata:
  type: project
---

# utils.TemplateManager

**File:** `skydiscover/context_builder/utils.py:7`  
**Kind:** class  
**Layer:** #context-builder

## Source
````python
class TemplateManager:
    """Loads .txt templates from one or more directories.

    Directories are processed in order; later directories override
    templates with the same name from earlier ones.
    """

````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveContextBuilder.__init__]]
- [[DefaultContextBuilder.__init__]]
- [[DefaultContextBuilder._get_system_message]]
- [[EvoxContextBuilder.__init__]]
- [[GEPANativeContextBuilder.__init__]]
