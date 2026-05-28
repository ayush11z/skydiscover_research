---
name: AdaEvolveContextBuilder.__init__
description: method in skydiscover/context_builder/adaevolve/builder.py (context-builder)
metadata:
  type: project
---

# AdaEvolveContextBuilder.__init__

**File:** `skydiscover/context_builder/adaevolve/builder.py:46`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def __init__(self, config: Config):
        super().__init__(config)
        default_templates = str(Path(__file__).parent.parent / "default" / "templates")
        adaevolve_templates = str(Path(__file__).parent / "templates")
        self.template_manager = TemplateManager(
            default_templates, adaevolve_templates, self.context_config.template_dir
        )
````

## → Calls
- [[DefaultContextBuilder.__init__]]
- [[TemplateManager.__init__]]
- [[config.Config]]
- [[utils.TemplateManager]]

## ← Called by
_(entry point — nothing in this graph calls it)_
