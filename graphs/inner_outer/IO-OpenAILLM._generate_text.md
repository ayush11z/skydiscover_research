---
name: IO-OpenAILLM._generate_text
description: method in skydiscover/llm/openai.py (llm)
metadata:
  type: project
---

# OpenAILLM._generate_text

**File:** `skydiscover/llm/openai.py:132`  
**Kind:** method  
**Layer:** #llm

## What it does
Formats the messages, builds the API params (handles reasoning models vs standard), then enters the retry loop. Times each attempt and passes latency + token usage to LangFuseTracer.log_generation.

Reads `loop_type` and `iteration` from the async context var set by `set_llm_context`.

## Source
````python
    async def _generate_text(
        self, system_message: str, messages: List[Dict[str, Any]], **kwargs
    ) -> str:
        system_content = system_message if system_message is not None else ""
        formatted_messages = [{"role": "system", "content": system_content}]
        formatted_messages.extend(messages)

        is_reasoning = is_openai_reasoning_model(self.model, self.api_base)

        if is_reasoning:
            params = {
                "model": self.model,
                "messages": formatted_messages,
                "max_completion_tokens": kwargs.get("max_tokens", self.max_tokens),
            }
            reasoning_effort = kwargs.get("reasoning_effort", self.reasoning_effort)
            if reasoning_effort is not None:
                params["reasoning_effort"] = reasoning_effort
            if "verbosity" in kwargs:
                params["verbosity"] = kwargs["verbosity"]
        else:
            params = {
                "model": self.model,
                "messages": formatted_messages,
                "max_tokens": kwargs.get("max_tokens", self.max_tokens),
            }
            temperature = kwargs.get("temperature", self.temperature)
            if temperature is not None:
                params["temperature"] = temperature
            top_p = kwargs.get("top_p", self.top_p)
            if top_p is not None:
                params["top_p"] = top_p
            reasoning_effort = kwargs.get("reasoning_effort", self.reasoning_effort)
            if reasoning_effort is not None:
                params["reasoning_effort"] = reasoning_effort

        retries, retry_delay, timeout = self._resolve_retry_options(**kwargs)

        tracer = LangFuseTracer.get()
        ctx = get_llm_context()
        loop_type = ctx.get("loop_type") or _infer_loop_type(self.model)
        iteration = ctx.get("iteration", -1)

        for attempt in range(retries + 1):
            try:
                t0 = time.monotonic()
                text, usage = await asyncio.wait_for(self._call_api(params), timeout=timeout)
                latency_s = time.monotonic() - t0
                tracer.log_generation(
                    model=self.model,
                    messages=formatted_messages,
                    output=text or "",
                    latency_s=latency_s,
                    usage=usage,
                    loop_type=loop_type,
                    iteration=iteration,
                )
                return text
            except asyncio.TimeoutError:
                if attempt < retries:
                    logger.warning(f"Timeout attempt {attempt + 1}/{retries + 1}, retrying...")
                    await asyncio.sleep(retry_delay)
                else:
                    raise
            except Exception as e:
                if attempt < retries:
                    logger.warning(f"Error attempt {attempt + 1}/{retries + 1}: {e}, retrying...")
                    await asyncio.sleep(retry_delay)
                else:
                    raise
````

## → Calls
- [[IO-LangFuseTracer.get]]
- [[IO-LangFuseTracer.log_generation]]
- [[IO-OpenAILLM._call_api]]
- [[IO-OpenAILLM._resolve_retry_options]]
- [[IO-langfuse_tracer._infer_loop_type]]
- [[IO-langfuse_tracer.get_llm_context]]
- [[IO-openai.is_openai_reasoning_model]]

## ← Called by
- [[IO-OpenAILLM.generate]]
