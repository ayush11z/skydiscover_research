---
name: config.LLMModelConfig
description: class in skydiscover/config.py (config)
metadata:
  type: project
---

# config.LLMModelConfig

**File:** `skydiscover/config.py:121`  
**Kind:** class  
**Layer:** #config

## Source
````python
class LLMModelConfig:
    """Configuration for a single LLM model"""

    # API configuration
    api_base: Optional[str] = None
    api_key: Optional[str] = None
    name: Optional[str] = None

    # Custom LLM client
    init_client: Optional[Callable] = None

    # Weight for model in pool, default to random sampling model based on weight
    weight: float = 1.0

    # Generation parameters
    system_message: Optional[str] = None
    temperature: Optional[float] = None
    top_p: Optional[float] = None
    max_tokens: Optional[int] = None

    # Request parameters
    timeout: Optional[int] = None
    retries: Optional[int] = None
    retry_delay: Optional[int] = None

    # Reasoning parameters
    reasoning_effort: Optional[str] = None
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[Config.from_dict]]
- [[Config.to_dict]]
- [[LLMConfig.__post_init__]]
- [[LLMPool.__init__]]
- [[OpenAILLM.__init__]]
- [[config.LLMConfig]]
- [[config.apply_overrides]]
- [[openevolve_backend._map_config]]
- [[variation_operator_generator.main]]
