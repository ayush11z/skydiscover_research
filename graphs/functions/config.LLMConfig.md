---
name: config.LLMConfig
description: class in skydiscover/config.py (config)
metadata:
  type: project
---

# config.LLMConfig

**File:** `skydiscover/config.py:151`  
**Kind:** class  
**Layer:** #config

## Source
````python
class LLMConfig(LLMModelConfig):
    """Configuration for LLM models"""

    # API configuration
    api_base: str = _PROVIDERS["openai"][0]

    # Generation parameters
    system_message: Optional[str] = "system_message"
    temperature: Optional[float] = 0.7
    top_p: Optional[float] = None
    max_tokens: int = 32000

    # Request parameters
    timeout: int = 600
    retries: int = 3
    retry_delay: int = 5

    # model(s) for solution discovery
    models: List[LLMModelConfig] = field(default_factory=list)

    # model(s) for evaluator
    evaluator_models: List[LLMModelConfig] = field(default_factory=lambda: [])

    # model(s) for guide tasks (idea generation, paradigm breakthroughs, etc.)
    # If not specified, falls back to using the main 'models' list
    guide_models: List[LLMModelConfig] = field(default_factory=lambda: [])

    # Reasoning parameters (inherited from LLMModelConfig but can be overridden)
    reasoning_effort: Optional[str] = None

````

## → Calls
- [[config.LLMModelConfig]]
- [[config._PROVIDERS]]

## ← Called by
- [[Config.from_dict]]
- [[Config.to_dict]]
- [[config.Config]]
- [[config.load_config]]
