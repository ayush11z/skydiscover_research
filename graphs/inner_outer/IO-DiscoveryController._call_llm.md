---
name: IO-DiscoveryController._call_llm
description: method in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# DiscoveryController._call_llm

**File:** `skydiscover/search/default_discovery_controller.py:178`  
**Kind:** method  
**Layer:** #inner-loop

## What it does
Thin wrapper: converts the prompt dict into `(system_message, messages)` format and calls LLMPool.generate.

## Source
````python
    async def _call_llm(self, system_message: str, user_message: str, **kwargs) -> LLMResponse:
        """Call the LLM, using agentic mode if enabled (text-only)."""
        if self.agentic_generator and not kwargs.get("image_output"):
            text = await self.agentic_generator.generate(system_message, user_message)
            if text:
                return LLMResponse(text=text)
        return await self.llms.generate(
            system_message, [{"role": "user", "content": user_message}], **kwargs
        )
````

## → Calls
- [[IO-AgenticGenerator.generate]]
- [[IO-DiscoveryController.__init__]]
- [[IO-Evaluator.__init__]]
- [[IO-EvoxContextBuilder.__init__]]
- [[IO-LLMPool.__init__]]
- [[IO-LLMPool.generate]]
- [[IO-LangFuseTracer.__init__]]
- [[IO-ProgramDatabase.__init__]]
- [[IO-agentic_generator.AgenticGenerator]]
- [[IO-base.LLMResponse]]

## ← Called by
- [[IO-DiscoveryController._run_from_scratch_iteration]]
- [[IO-DiscoveryController._run_iteration]]
