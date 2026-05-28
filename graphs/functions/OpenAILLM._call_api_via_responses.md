---
name: OpenAILLM._call_api_via_responses
description: method in skydiscover/llm/openai.py (llm)
metadata:
  type: project
---

# OpenAILLM._call_api_via_responses

**File:** `skydiscover/llm/openai.py:227`  
**Kind:** method  
**Layer:** #llm

## Source
````python
    async def _call_api_via_responses(
        self, params: Dict[str, Any]
    ) -> Tuple[str, Optional[Dict[str, int]]]:
        """Translate a Chat-Completions-style *params* dict into a Responses API
        call and return (text, usage)."""
        messages = params.get("messages", [])
        input_items = self._convert_to_responses_input(
            [m for m in messages if m.get("role") != "system"]
        )
        system_msg = next((m["content"] for m in messages if m.get("role") == "system"), None)
        resp_params: Dict[str, Any] = {
            "model": params.get("model", self.model),
            "input": input_items,
        }
        if system_msg:
            resp_params["instructions"] = system_msg
        if params.get("max_tokens"):
            resp_params["max_output_tokens"] = params["max_tokens"]
        if params.get("max_completion_tokens"):
            resp_params["max_output_tokens"] = params["max_completion_tokens"]
        if params.get("temperature") is not None:
            resp_params["temperature"] = params["temperature"]
        if params.get("reasoning_effort") is not None:
            resp_params["reasoning"] = {"effort": params["reasoning_effort"]}

        loop = asyncio.get_running_loop()
        response = await loop.run_in_executor(
            None, lambda: self.client.responses.create(**resp_params)
        )
        text, _ = self._extract_responses_output(response)
        usage: Optional[Dict[str, int]] = None
        resp_usage = getattr(response, "usage", None)
        if resp_usage:
            usage = {
                "prompt_tokens": getattr(resp_usage, "input_tokens", 0) or 0,
                "completion_tokens": getattr(resp_usage, "output_tokens", 0) or 0,
                "total_tokens": getattr(resp_usage, "total_tokens", 0) or 0,
            }
        return text or "", usage
````

## → Calls
- [[BenchmarkConfig.name]]
- [[LLMModelConfig.name]]
- [[LangFuseTracer.get]]
- [[OpenAILLM.__init__]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[OpenAILLM._call_api]]
