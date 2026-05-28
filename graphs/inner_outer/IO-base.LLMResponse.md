---
name: IO-base.LLMResponse
description: class in skydiscover/llm/base.py (llm)
metadata:
  type: project
---

# base.LLMResponse

**File:** `skydiscover/llm/base.py:9`  
**Kind:** class  
**Layer:** #llm

## Source
````python
class LLMResponse:
    """Response from an LLM generation call.

    text: generated text content.
    image_path: path to generated image file, or None for text-only.
    """

    text: str = ""
    image_path: Optional[str] = None
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-DiscoveryController._call_llm]]
- [[IO-LLMInterface.generate]]
- [[IO-LLMPool.generate]]
- [[IO-LLMPool.generate_all]]
- [[IO-OpenAILLM._generate_with_image]]
- [[IO-OpenAILLM.generate]]
