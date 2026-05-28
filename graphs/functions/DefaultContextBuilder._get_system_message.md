---
name: DefaultContextBuilder._get_system_message
description: method in skydiscover/context_builder/default/builder.py (context-builder)
metadata:
  type: project
---

# DefaultContextBuilder._get_system_message

**File:** `skydiscover/context_builder/default/builder.py:164`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _get_system_message(self) -> str:
        """Return system message from override, template, or raw config string."""
        if self.system_template_override:
            return self.template_manager.get_template(self.system_template_override)
        system_msg = self.context_config.system_message
        if system_msg in self.template_manager.templates:
            return self.template_manager.get_template(system_msg)
        return system_msg
````

## → Calls
- [[Config.context_builder]]
- [[TemplateManager.get_template]]
- [[base.ContextBuilder]]
- [[utils.TemplateManager]]

## ← Called by
- [[DefaultContextBuilder.build_prompt]]
- [[EvoxContextBuilder.build_prompt]]
