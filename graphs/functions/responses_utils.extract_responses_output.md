---
name: responses_utils.extract_responses_output
description: function in skydiscover/llm/responses_utils.py (llm)
metadata:
  type: project
---

# responses_utils.extract_responses_output

**File:** `skydiscover/llm/responses_utils.py:74`  
**Kind:** function  
**Layer:** #llm

## Source
````python
def extract_responses_output(
    response,
) -> Tuple[str, Optional[str], List[Dict[str, Any]]]:
    """Extract text, image, and tool calls from a Responses API response.

    Returns:
        (text, image_b64, tool_calls) where tool_calls is a list of
        Chat-Completions-compatible tool call dicts (may be empty).
    """
    text_parts: List[str] = []
    image_b64: Optional[str] = None
    tool_calls: List[Dict[str, Any]] = []

    for item in response.output:
        if item.type == "message":
            for part in item.content:
                if hasattr(part, "text"):
                    text_parts.append(part.text)
        elif item.type == "image_generation_call":
            if item.result:
                image_b64 = item.result
        elif item.type == "function_call":
            tool_calls.append(
                {
                    "id": item.call_id,
                    "type": "function",
                    "function": {"name": item.name, "arguments": item.arguments},
                }
            )

    return "\n".join(text_parts), image_b64, tool_calls
````

## → Calls
- [[BenchmarkConfig.name]]
- [[LLMModelConfig.name]]
- [[LLMResponse.text]]
- [[SearchConfig.type]]
- [[search_strategy_evaluator.result]]

## ← Called by
- [[AgenticGenerator._call_llm_responses]]
- [[OpenAILLM._generate_with_image]]
