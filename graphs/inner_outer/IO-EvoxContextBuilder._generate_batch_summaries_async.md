---
name: IO-EvoxContextBuilder._generate_batch_summaries_async
description: method in skydiscover/context_builder/evox/builder.py (context-builder)
metadata:
  type: project
---

# EvoxContextBuilder._generate_batch_summaries_async

**File:** `skydiscover/context_builder/evox/builder.py:142`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    async def _generate_batch_summaries_async(self, batch_user_message: str) -> str:
        """Generate batch summaries via LLM."""
        self._save_guide_prompt(self._batch_sections["SYSTEM"], batch_user_message)
        result = await self.summary_llm.generate(
            system_message=self._batch_sections["SYSTEM"],
            messages=[{"role": "user", "content": batch_user_message}],
        )
        return result.text
````

## → Calls
- [[IO-EvoxContextBuilder._parse_template_sections]]
- [[IO-EvoxContextBuilder._save_guide_prompt]]
- [[IO-LLMPool.generate]]

## ← Called by
- [[IO-build_prompt.gather_llm_calls]]
