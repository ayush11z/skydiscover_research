---
name: DefaultContextBuilder.__init__
description: method in skydiscover/context_builder/default/builder.py (context-builder)
metadata:
  type: project
---

# DefaultContextBuilder.__init__

**File:** `skydiscover/context_builder/default/builder.py:48`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def __init__(self, config: Config):
        super().__init__(config)
        self.system_template_override = None
        self.user_template_override = None
        self.template_manager = TemplateManager(_TEMPLATES_DIR, self.context_config.template_dir)
````

## → Calls
- [[Config.context_builder]]
- [[ContextBuilder.__init__]]
- [[TemplateManager.__init__]]
- [[base.ContextBuilder]]
- [[config.Config]]
- [[utils.TemplateManager]]

## ← Called by
- [[AdaEvolveContextBuilder.__init__]]
- [[EvoxContextBuilder.__init__]]
- [[GEPANativeContextBuilder.__init__]]
