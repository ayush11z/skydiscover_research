---
name: EvoxContextBuilder._generate_stats_insight_async
description: method in skydiscover/context_builder/evox/builder.py (context-builder)
metadata:
  type: project
---

# EvoxContextBuilder._generate_stats_insight_async

**File:** `skydiscover/context_builder/evox/builder.py:103`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    async def _generate_stats_insight_async(self, stats_text: str) -> str:
        """Generate stats insight via LLM."""
        if not stats_text:
            return ""
        system_msg = self.template_manager.get_template("stats_insight_system_message")
        user_content = f"Population Statistics:\n\n{stats_text}"
        self._save_guide_prompt(system_msg, user_content)
        result = await self.summary_llm.generate(
            system_message=system_msg,
            messages=[{"role": "user", "content": user_content}],
        )
        return result.text
````

## → Calls
- [[EvoxContextBuilder._save_guide_prompt]]
- [[LLMPool.generate]]
- [[TemplateManager.get_template]]

## ← Called by
- [[build_prompt.gather_llm_calls]]
