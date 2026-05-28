---
name: DiscoveryController._call_llm
description: method in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# DiscoveryController._call_llm

**File:** `skydiscover/search/default_discovery_controller.py:178`  
**Kind:** method  
**Layer:** #inner-loop

## What it does
Thin wrapper: converts the prompt dict into `(system_message, messages)` format and calls [[LLMPool.generate]].

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
- [[AgenticGenerator.__init__]]
- [[AgenticGenerator.generate]]
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
- [[LLMPool.generate]]
- [[LangFuseTracer.__init__]]
- [[LogWindowScorer.__init__]]
- [[MetricDiversity.__init__]]
- [[MonitorServer.__init__]]
- [[OpenAILLM.__init__]]
- [[ParadigmGenerator.__init__]]
- [[ProgramDatabase.__init__]]
- [[Runner.__init__]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[_FinalResult.__init__]]
- [[agentic_generator.AgenticGenerator]]
- [[base.LLMResponse]]

## ← Called by
- [[AdaEvolveController._execute_generation]]
- [[DiscoveryController._run_from_scratch_iteration]]
- [[DiscoveryController._run_iteration]]
