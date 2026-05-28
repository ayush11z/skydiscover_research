---
name: config.ContextBuilderConfig
description: class in skydiscover/config.py (config)
metadata:
  type: project
---

# config.ContextBuilderConfig

**File:** `skydiscover/config.py:104`  
**Kind:** class  
**Layer:** #config

## Source
````python
class ContextBuilderConfig:
    """Configuration for prompt generation"""

    template: str = "default"  # "default", "evox"
    template_dir: Optional[str] = None
    system_message: str = "system_message"
    evaluator_system_message: str = "evaluator_system_message"

    suggest_simplification_after_chars: Optional[int] = 500
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[Config.from_dict]]
- [[Config.to_dict]]
- [[config.Config]]
- [[config.load_config]]
