---
name: config.EvaluatorConfig
description: class in skydiscover/config.py (config)
metadata:
  type: project
---

# config.EvaluatorConfig

**File:** `skydiscover/config.py:310`  
**Kind:** class  
**Layer:** #config

## Source
````python
class EvaluatorConfig:
    """Configuration for program evaluation"""

    evaluation_file: Optional[str] = None
    file_suffix: str = ".py"
    is_image_mode: bool = False

    timeout: int = 360
    max_retries: int = 3

    # Evaluation strategies
    cascade_evaluation: bool = True
    cascade_thresholds: List[float] = field(default_factory=lambda: [0.3, 0.6])

    # When True, the evaluator source code (or instruction.md for Harbor
    # tasks) is prepended to the LLM system message so the model can see
    # exactly how solutions are scored.  Disabled by default to avoid
    # leaking implementation details that may introduce noise.
    inject_evaluator_context: bool = False

    # LLM-as-a-judge: when True, an LLMJudge scores programs alongside the
    # evaluator and appends llm_* metrics to the result.
    # This will read from prompt.evaluator_system_message if provided, otherwise use the default system prompt.
    llm_as_judge: bool = False
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[Config.from_dict]]
- [[Config.to_dict]]
- [[ContainerizedEvaluator.__init__]]
- [[Evaluator.__init__]]
- [[config.Config]]
