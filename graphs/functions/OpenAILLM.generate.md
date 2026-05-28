---
name: OpenAILLM.generate
description: method in skydiscover/llm/openai.py (llm)
metadata:
  type: project
---

# OpenAILLM.generate

**File:** `skydiscover/llm/openai.py:119`  
**Kind:** method  
**Layer:** #llm

## What it does
Top-level method on the OpenAI-compatible client. Dispatches to [[OpenAILLM._generate_text]] for regular completions or `_generate_with_image` for image generation.

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
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[ContainerizedEvaluator.__init__]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[Evaluator.__init__]]
- [[HumanFeedbackReader.__init__]]
- [[HybridDiversity.__init__]]
- [[LLMJudge.__init__]]
- [[LLMPool.__init__]]
- [[LangFuseTracer.__init__]]
- [[LogWindowScorer.__init__]]
- [[MetricDiversity.__init__]]
- [[MonitorServer.__init__]]
- [[OpenAILLM.__init__]]
- [[OpenAILLM._generate_text]]
- [[OpenAILLM._generate_with_image]]
- [[ParadigmGenerator.__init__]]
- [[ProgramDatabase.__init__]]
- [[Runner.__init__]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[_FinalResult.__init__]]
- [[base.LLMResponse]]

## ← Called by
_(entry point — nothing in this graph calls it)_
