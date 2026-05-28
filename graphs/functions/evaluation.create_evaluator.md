---
name: evaluation.create_evaluator
description: function in skydiscover/evaluation/__init__.py (evaluation)
metadata:
  type: project
---

# evaluation.create_evaluator

**File:** `skydiscover/evaluation/__init__.py:59`  
**Kind:** function  
**Layer:** #evaluation

## Source
````python
def create_evaluator(
    config,
    llm_judge: Optional[LLMJudge] = None,
    max_concurrent: int = 4,
    env_vars: Optional[Dict[str, str]] = None,
) -> Union[Evaluator, ContainerizedEvaluator, HarborEvaluator]:
    """Return the right evaluator for the given config.

    Detection order (most specific first):
      1. Harbor task — instruction.md + tests/ + environment/Dockerfile
      2. Containerized — Dockerfile + evaluate.sh
      3. Python evaluator — fallback
    """
    path = config.evaluation_file or ""
    if _is_harbor_task(path):
        return HarborEvaluator(path, config, max_concurrent=max_concurrent, env_vars=env_vars)
    if _is_containerized(path):
        return ContainerizedEvaluator(
            path, config, max_concurrent=max_concurrent, env_vars=env_vars
        )
    return Evaluator(config, llm_judge=llm_judge, max_concurrent=max_concurrent, env_vars=env_vars)
````

## → Calls
- [[ContainerizedEvaluator.__init__]]
- [[DiscoveryControllerInput.evaluation_file]]
- [[Evaluator.__init__]]
- [[EvaluatorConfig.evaluation_file]]
- [[EvoxDatabaseConfig.evaluation_file]]
- [[container_evaluator.ContainerizedEvaluator]]
- [[evaluation._is_containerized]]
- [[evaluation._is_harbor_task]]
- [[evaluator.Evaluator]]
- [[harbor_evaluator.HarborEvaluator]]
- [[llm_judge.LLMJudge]]

## ← Called by
- [[AdaEvolveController._execute_generation]]
- [[ClaudeCodeController.__init__]]
- [[ClaudeCodeController._final_evaluation]]
- [[ClaudeCodeController.run_discovery]]
- [[CoEvolutionController._restore_fallback_database]]
- [[CoEvolutionController._switch_to_new_search_algorithm]]
- [[DiscoveryController.__init__]]
- [[DiscoveryController._run_from_scratch_iteration]]
- [[DiscoveryController._run_iteration]]
- [[DiscoveryController.close]]
- [[GEPANativeController._attempt_merge]]
