---
name: AgenticGenerator._call_llm_responses
description: method in skydiscover/llm/agentic_generator.py (llm)
metadata:
  type: project
---

# AgenticGenerator._call_llm_responses

**File:** `skydiscover/llm/agentic_generator.py:231`  
**Kind:** method  
**Layer:** #llm

## Source
````python
    async def _call_llm_responses(
        self,
        model,
        system_message: str,
        conversation: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """Call the LLM via the Responses API (Azure-compatible) with tool support."""
        is_reasoning = is_openai_reasoning_model(model.model, getattr(model, "api_base", "") or "")

        input_items = convert_messages_to_responses_input(conversation)

        resp_params: Dict[str, Any] = {
            "model": model.model,
            "input": input_items,
            "instructions": system_message,
            "tools": TOOL_SCHEMAS_RESPONSES,
            "tool_choice": "auto",
        }
        if is_reasoning:
            if model.max_tokens:
                resp_params["max_output_tokens"] = model.max_tokens
            if getattr(model, "reasoning_effort", None):
                resp_params["reasoning"] = {"effort": model.reasoning_effort}
        else:
            if model.temperature is not None:
                resp_params["temperature"] = model.temperature
            if model.max_tokens is not None:
                resp_params["max_output_tokens"] = model.max_tokens

        loop = asyncio.get_running_loop()
        resp = await loop.run_in_executor(
            None, lambda: model.client.responses.create(**resp_params)
        )

        text, _, tool_calls = extract_responses_output(resp)
        out: Dict[str, Any] = {"role": "assistant", "content": text}
        if tool_calls:
            out["tool_calls"] = tool_calls
        return out
````

## → Calls
- [[LLMModelConfig.max_tokens]]
- [[LLMModelConfig.reasoning_effort]]
- [[LLMModelConfig.temperature]]
- [[openai.is_openai_reasoning_model]]
- [[responses_utils.convert_messages_to_responses_input]]
- [[responses_utils.extract_responses_output]]

## ← Called by
- [[AgenticGenerator._call_llm]]
