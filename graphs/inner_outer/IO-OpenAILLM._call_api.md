---
name: IO-OpenAILLM._call_api
description: method in skydiscover/llm/openai.py (llm)
metadata:
  type: project
---

# OpenAILLM._call_api

**File:** `skydiscover/llm/openai.py:203`  
**Kind:** method  
**Layer:** #llm

## What it does
Makes the actual HTTP request to the OpenAI-compatible endpoint (Ollama, Azure, OpenAI, etc.) using `client.chat.completions.create`. Runs in a thread-pool executor so it doesn't block the async event loop. Falls back to the Responses API if Chat Completions returns an "unsupported" error.

## Source
````python
    async def _call_api(
        self, params: Dict[str, Any]
    ) -> Tuple[str, Optional[Dict[str, int]]]:
        loop = asyncio.get_running_loop()
        try:
            response = await loop.run_in_executor(
                None, lambda: self.client.chat.completions.create(**params)
            )
            usage: Optional[Dict[str, int]] = None
            if response.usage:
                usage = {
                    "prompt_tokens": response.usage.prompt_tokens or 0,
                    "completion_tokens": response.usage.completion_tokens or 0,
                    "total_tokens": response.usage.total_tokens or 0,
                }
            return response.choices[0].message.content, usage
        except (openai.BadRequestError, openai.APIStatusError) as exc:
            # Some Azure deployments only expose the Responses API.
            # Fall back transparently when Chat Completions is unsupported.
            if "unsupported" not in str(exc).lower() and "not found" not in str(exc).lower():
                raise
            logger.info("Chat Completions unsupported; falling back to Responses API")
            return await self._call_api_via_responses(params)
````

## → Calls
- [[IO-OpenAILLM._call_api_via_responses]]

## ← Called by
- [[IO-OpenAILLM._generate_text]]
