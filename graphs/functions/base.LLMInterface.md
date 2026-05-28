---
name: base.LLMInterface
description: class in skydiscover/llm/base.py (llm)
metadata:
  type: project
---

# base.LLMInterface

**File:** `skydiscover/llm/base.py:20`  
**Kind:** class  
**Layer:** #llm

## Source
````python
class LLMInterface(ABC):
    """Abstract base for LLM backends.

    Subclass this and implement generate() to add a new LLM provider.
    """

    @abstractmethod
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[openai.OpenAILLM]]
