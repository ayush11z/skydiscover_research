---
name: IO-responses_utils.convert_messages_to_responses_input
description: function in skydiscover/llm/responses_utils.py (llm)
metadata:
  type: project
---

# responses_utils.convert_messages_to_responses_input

**File:** `skydiscover/llm/responses_utils.py:10`  
**Kind:** function  
**Layer:** #llm

## Source
````python
def convert_messages_to_responses_input(messages: List[Dict[str, Any]]) -> list:
    """Convert Chat Completions-style messages to Responses API input format.

    Handles:
    - user / assistant text messages (plain string or multipart content)
    - assistant messages with tool_calls -> function_call items
    - tool role messages -> function_call_output items
    """
    items: list = []
    for msg in messages:
        role = msg.get("role", "user")
        content = msg.get("content", "")

        if role == "tool":
            items.append(
                {
                    "type": "function_call_output",
                    "call_id": msg.get("tool_call_id", ""),
                    "output": content if isinstance(content, str) else "",
                }
            )
            continue

        if role == "assistant":
            tool_calls = msg.get("tool_calls", [])
            if tool_calls:
                for tc in tool_calls:
                    fn = tc.get("function", {})
                    items.append(
                        {
                            "type": "function_call",
                            "call_id": tc.get("id", ""),
                            "name": fn.get("name", ""),
                            "arguments": fn.get("arguments", "{}"),
                        }
                    )
                # If assistant had both text and tool_calls, skip the text
                # (Responses API treats function_call items as the assistant turn)
                if not content:
                    continue

        # Text-only message (user, assistant without tool_calls, or system)
        if isinstance(content, str):
            items.append(
                {
                    "type": "message",
                    "role": role,
                    "content": [{"type": "input_text", "text": content}],
                }
            )
        elif isinstance(content, list):
            parts = []
            for part in content:
                ptype = part.get("type", "")
                if ptype == "text":
                    parts.append({"type": "input_text", "text": part["text"]})
                elif ptype == "image_url":
                    url = part.get("image_url", {}).get("url", "")
                    parts.append({"type": "input_image", "image_url": url, "detail": "auto"})
            items.append({"type": "message", "role": role, "content": parts})

    return items
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-AgenticGenerator._call_llm_responses]]
- [[IO-OpenAILLM._generate_with_image]]
