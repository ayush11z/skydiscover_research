---
name: IN-LLMInterface.generate
description: method in skydiscover/llm/base.py (llm)
metadata:
  type: project
---

# LLMInterface.generate

**File:** `skydiscover/llm/base.py:27`  
**Kind:** method  
**Layer:** #llm

## Source
````python
    async def generate(
        self, system_message: str, messages: List[Dict[str, Any]], **kwargs
    ) -> LLMResponse:
        """Generate a response from the LLM.

        Args:
            system_message: system prompt string.
            messages: conversation history as list of {role, content} dicts.
            **kwargs: backend-specific options (e.g. image_output=True for
                image generation, output_dir, program_id, temperature).

        Returns:
            LLMResponse with text and optional image_path.
        """
        pass
````

## → Calls
- [[IN-base.LLMResponse]]

## ← Called by
- [[IN-LLMPool.generate]]
- [[IN-LLMPool.generate_all]]
