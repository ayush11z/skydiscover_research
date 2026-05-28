---
name: IO-Evaluator.__init__
description: method in skydiscover/evaluation/evaluator.py (evaluation)
metadata:
  type: project
---

# Evaluator.__init__

**File:** `skydiscover/evaluation/evaluator.py:34`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def __init__(
        self,
        config: EvaluatorConfig,
        llm_judge: Optional[LLMJudge] = None,
        max_concurrent: int = 4,
        env_vars: Optional[Dict[str, str]] = None,
    ):
        if not config.evaluation_file:
            raise ValueError("EvaluatorConfig.evaluation_file must be set")

        self.config = config
        self.evaluation_file = config.evaluation_file
        self.program_suffix = config.file_suffix
        self.is_image_mode = config.is_image_mode
        self.llm_judge = llm_judge
        self.task_pool = TaskPool(max_concurrency=max_concurrent)
        self.env_vars = dict(env_vars or {})

        self._load_evaluation_function()
        logger.info(f"Initialized evaluator with {self.evaluation_file}")
````

## → Calls
- [[IO-Evaluator._load_evaluation_function]]

## ← Called by
- [[IO-DiscoveryController._call_llm]]
- [[IO-DiscoveryController._create_child_program]]
- [[IO-DiscoveryController._run_from_scratch_iteration]]
- [[IO-Evaluator._cascade_evaluate]]
- [[IO-Evaluator._normalize_result]]
- [[IO-Evaluator._run_stage]]
- [[IO-Evaluator._validate_cascade_configuration]]
- [[IO-Evaluator.evaluate_program]]
