---
name: DefaultContextBuilder.set_templates
description: method in skydiscover/context_builder/default/builder.py (context-builder)
metadata:
  type: project
---

# DefaultContextBuilder.set_templates

**File:** `skydiscover/context_builder/default/builder.py:54`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def set_templates(
        self, system_template: Optional[str] = None, user_template: Optional[str] = None
    ) -> None:
        """Override the default system/user template keys.

        Pass None for either argument to keep the current value.
        """
        self.system_template_override = system_template
        self.user_template_override = user_template
        logger.info(f"Templates set: system={system_template}, user={user_template}")
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[DiscoveryController.__init__]]
- [[DiscoveryController._init_context_builder]]
