---
name: coevolve_logging.handle_generation_failure
description: function in skydiscover/search/evox/utils/coevolve_logging.py (evox)
metadata:
  type: project
---

# coevolve_logging.handle_generation_failure

**File:** `skydiscover/search/evox/utils/coevolve_logging.py:175`  
**Kind:** function  
**Layer:** #evox

## Source
````python
async def handle_generation_failure(
    outputs_dir: str,
    active_search_code: str,
    iteration: int,
    result: Optional[SerializableResult],
    solution_iter: int,
    stage: str = "generation",
) -> None:
    """Handle failed search algorithm generation or validation."""
    error_msg = result.error if result else "Unknown error"
    await log_failed_attempt(
        outputs_dir,
        iteration,
        result,
        error_msg if stage == "generation" else "Failed to load/validate",
        stage,
        solution_iter=solution_iter,
    )
    if stage == "generation":
        logger.warning(f"Failed to generate search algorithm: {error_msg}")
    await log_active_algorithm(outputs_dir, active_search_code, iteration)
````

## → Calls
- [[SerializableResult.error]]
- [[coevolve_logging.log_active_algorithm]]
- [[coevolve_logging.log_failed_attempt]]
- [[discovery_utils.SerializableResult]]

## ← Called by
- [[CoEvolutionController._generate_and_validate_search_algorithm]]
