---
name: DefaultContextBuilder._select_template_key
description: method in skydiscover/context_builder/default/builder.py (context-builder)
metadata:
  type: project
---

# DefaultContextBuilder._select_template_key

**File:** `skydiscover/context_builder/default/builder.py:144`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _select_template_key(
        self, language: str, diff_based: bool, has_current_program: bool = True
    ) -> str:
        """Pick template: override > auto (from_scratch / image / diff / full rewrite)."""
        if self.user_template_override:
            return self.user_template_override

        if not has_current_program:
            return "from_scratch_user_message"

        if language == "image":
            return "image_user_message"

        if diff_based:
            return "diff_user_message"

        if language.lower() in _TEXT_LANGUAGES:
            return "full_rewrite_prompt_opt_user_message"
        return "full_rewrite_user_message"
````

## → Calls
- [[builder._TEXT_LANGUAGES]]

## ← Called by
- [[DefaultContextBuilder.build_prompt]]
