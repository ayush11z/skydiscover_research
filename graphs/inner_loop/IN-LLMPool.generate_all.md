---
name: IN-LLMPool.generate_all
description: method in skydiscover/llm/llm_pool.py (llm)
metadata:
  type: project
---

# LLMPool.generate_all

**File:** `skydiscover/llm/llm_pool.py:63`  
**Kind:** method  
**Layer:** #llm

## Source
````python
    async def generate_all(
        self, system_message: str, messages: List[Dict[str, Any]], **kwargs
    ) -> List[LLMResponse]:
        """Generate using all models concurrently."""
        return await asyncio.gather(
            *(model.generate(system_message, messages, **kwargs) for model in self.models)
        )
````

## → Calls
- [[IN-LLMInterface.generate]]
- [[IN-LLMPool.generate]]
- [[IN-base.LLMResponse]]

## ← Called by
_(entry point — nothing in this graph calls it)_
