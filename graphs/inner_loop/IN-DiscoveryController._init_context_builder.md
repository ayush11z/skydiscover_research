---
name: IN-DiscoveryController._init_context_builder
description: method in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# DiscoveryController._init_context_builder

**File:** `skydiscover/search/default_discovery_controller.py:155`  
**Kind:** method  
**Layer:** #inner-loop

## Source
````python
    def _init_context_builder(self):
        """Initialize the appropriate context builder based on config."""
        if getattr(self.config.context_builder, "template", "default") == "evox":
            self.context_builder = EvoxContextBuilder(self.config)
            template_name = "search_evolution_user_message"
            self.context_builder.set_templates(user_template=template_name)
            self.context_builder.output_dir = self.output_dir
        else:
            self.context_builder = DefaultContextBuilder(self.config)
````

## → Calls
- [[IN-DiscoveryControllerInput.config]]
- [[IN-DiscoveryControllerInput.output_dir]]
- [[IN-builder.EvoxContextBuilder]]

## ← Called by
- [[IN-DiscoveryController.__init__]]
