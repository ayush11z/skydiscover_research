---
name: IN-AgenticGenerator._call_llm
description: method in skydiscover/llm/agentic_generator.py (llm)
metadata:
  type: project
---

# AgenticGenerator._call_llm

**File:** `skydiscover/llm/agentic_generator.py:161`  
**Kind:** method  
**Layer:** #llm

## Source
````python
    async def _call_llm(
        self, system_message: str, conversation: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Call a sampled LLM with tool schemas.

        Tries Chat Completions first; falls back to Responses API if the
        deployment does not support Chat Completions (common on Azure).
        """
        model = self.llm_pool.models[
            self.llm_pool.random_state.choices(
                range(len(self.llm_pool.models)), weights=self.llm_pool.weights, k=1
            )[0]
        ]

        if not hasattr(model, "client"):
            raise RuntimeError(
                f"Agentic mode requires an OpenAI-compatible LLM ({type(model).__name__} has no .client)"
            )

        # If we already know this model needs the Responses API, skip Chat Completions
        if getattr(model, "_use_responses_api", False):
            return await self._call_llm_responses(model, system_message, conversation)

        messages = [{"role": "system", "content": system_message}] + conversation
        is_reasoning = is_openai_reasoning_model(model.model, getattr(model, "api_base", "") or "")

        params: Dict[str, Any] = {
            "model": model.model,
            "messages": messages,
            "tools": TOOL_SCHEMAS,
            "tool_choice": "auto",
        }
        if is_reasoning:
            if model.max_tokens:
                params["max_completion_tokens"] = model.max_tokens
            if getattr(model, "reasoning_effort", None):
                params["reasoning_effort"] = model.reasoning_effort
        else:
            if model.temperature is not None:
                params["temperature"] = model.temperature
            if model.top_p is not None:
                params["top_p"] = model.top_p
            if model.max_tokens is not None:
                params["max_tokens"] = model.max_tokens

        loop = asyncio.get_running_loop()
        try:
            resp = await loop.run_in_executor(
                None, lambda: model.client.chat.completions.create(**params)
            )
        except Exception as exc:
            if "unsupported" not in str(exc).lower() and "not found" not in str(exc).lower():
                raise
            logger.info("Chat Completions unsupported for agentic; falling back to Responses API")
            model._use_responses_api = True
            return await self._call_llm_responses(model, system_message, conversation)

        msg = resp.choices[0].message
        out: Dict[str, Any] = {"role": "assistant", "content": msg.content or ""}
        if msg.tool_calls:
            out["tool_calls"] = [
                {
                    "id": tc.id,
                    "type": "function",
                    "function": {"name": tc.function.name, "arguments": tc.function.arguments},
                }
                for tc in msg.tool_calls
            ]
        return out
````

## → Calls
- [[IN-AgenticGenerator.__init__]]
- [[IN-AgenticGenerator._call_llm_responses]]
- [[IN-openai.is_openai_reasoning_model]]

## ← Called by
- [[IN-AgenticGenerator.generate]]
