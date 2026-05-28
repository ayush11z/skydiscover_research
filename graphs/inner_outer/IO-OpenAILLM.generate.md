---
name: IO-OpenAILLM.generate
description: method in skydiscover/llm/openai.py (llm)
metadata:
  type: project
---

# OpenAILLM.generate

**File:** `skydiscover/llm/openai.py:119`  
**Kind:** method  
**Layer:** #llm

## What it does
Top-level method on the OpenAI-compatible client. Dispatches to OpenAILLM._generate_text for regular completions or `_generate_with_image` for image generation.

## Source
````python
    async def generate(
        self, system_message: str, messages: List[Dict[str, Any]], **kwargs
    ) -> LLMResponse:
        """Generate a response. Pass image_output=True for image generation."""
        if kwargs.get("image_output"):
            return await self._generate_with_image(system_message, messages, **kwargs)
        text = await self._generate_text(system_message, messages, **kwargs)
        return LLMResponse(text=text)
````

## → Calls
- [[IO-LangFuseTracer.__init__]]
- [[IO-OpenAILLM.__init__]]
- [[IO-OpenAILLM._generate_text]]
- [[IO-OpenAILLM._generate_with_image]]
- [[IO-base.LLMResponse]]

## ← Called by
_(entry point — nothing in this graph calls it)_
