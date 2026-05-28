---
name: IN-OpenAILLM._call_responses_api
description: method in skydiscover/llm/openai.py (llm)
metadata:
  type: project
---

# OpenAILLM._call_responses_api

**File:** `skydiscover/llm/openai.py:350`  
**Kind:** method  
**Layer:** #llm

## Source
````python
    async def _call_responses_api(self, params: Dict[str, Any]):
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, lambda: self.client.responses.create(**params))
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IN-OpenAILLM._generate_with_image]]
