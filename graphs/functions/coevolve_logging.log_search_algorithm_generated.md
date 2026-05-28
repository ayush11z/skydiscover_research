---
name: coevolve_logging.log_search_algorithm_generated
description: function in skydiscover/search/evox/utils/coevolve_logging.py (evox)
metadata:
  type: project
---

# coevolve_logging.log_search_algorithm_generated

**File:** `skydiscover/search/evox/utils/coevolve_logging.py:37`  
**Kind:** function  
**Layer:** #evox

## Source
````python
async def log_search_algorithm_generated(
    outputs_dir: str,
    result: SerializableResult,
    iteration: int,
    diverge_label: str = "",
    refine_label: str = "",
) -> None:
    """Save newly generated search algorithm details to files (before scoring)."""
    if result.error:
        logger.warning(f"Search strategy generation failed (iteration {iteration}): {result.error}")
        return

    child_dict = result.child_program_dict or {}

    await save_search_algorithm(
        outputs_dir=outputs_dir,
        iteration=iteration,
        program_id=child_dict.get("id", "unknown"),
        solution=child_dict.get("solution", ""),
        score=None,
        metrics={},
        diverge_label=diverge_label,
        refine_label=refine_label,
        pending_score=True,
    )

    iteration_dir = os.path.join(outputs_dir, f"iteration_{iteration}")
    logger.info(
        f"New search algorithm generated (iteration {iteration}) - "
        f"saved to {os.path.abspath(iteration_dir)} (score pending)"
    )
````

## → Calls
- [[SerializableResult.child_program_dict]]
- [[SerializableResult.error]]
- [[coevolve_logging.save_search_algorithm]]
- [[discovery_utils.SerializableResult]]

## ← Called by
- [[CoEvolutionController._generate_and_validate_search_algorithm]]
