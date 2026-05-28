---
name: IO-coevolve_logging.save_search_algorithm
description: function in skydiscover/search/evox/utils/coevolve_logging.py (evox)
metadata:
  type: project
---

# coevolve_logging.save_search_algorithm

**File:** `skydiscover/search/evox/utils/coevolve_logging.py:70`  
**Kind:** function  
**Layer:** #evox

## Source
````python
async def save_search_algorithm(
    outputs_dir: str,
    iteration: int,
    program_id: str,
    solution: str,
    score: Optional[float],
    metrics: Dict[str, Any],
    system_prompt: str = "",
    user_prompt: str = "",
    llm_response: str = "",
    diverge_label: str = "",
    refine_label: str = "",
    pending_score: bool = False,
) -> None:
    """Save search algorithm details to files in search/iteration_x/."""
    iteration_dir = os.path.join(outputs_dir, f"iteration_{iteration}")
    os.makedirs(iteration_dir, exist_ok=True)

    metadata = {
        "iteration": iteration,
        "program_id": program_id,
        "score": score,
        "metrics": metrics,
        "pending_score": pending_score,
    }

    with open(os.path.join(iteration_dir, "metadata.json"), "w") as f:
        json.dump(metadata, f, indent=2)

    if solution:
        with open(os.path.join(iteration_dir, "code.py"), "w") as f:
            f.write(solution)

    prompts = {
        k: v
        for k, v in [
            ("system_prompt", system_prompt),
            ("user_prompt", user_prompt),
            ("llm_response", llm_response),
        ]
        if v
    }
    if prompts:
        with open(os.path.join(iteration_dir, "prompts.json"), "w") as f:
            json.dump(prompts, f, indent=2)

    if iteration == 1:
        labels_path = os.path.join(iteration_dir, "labels.yaml")
        try:
            labels_text = (
                f"iteration: {iteration}\n"
                f"diverge_label_length: {len(diverge_label)}\n"
                f"refine_label_length: {len(refine_label)}\n\n"
                f"diverge_label: |\n"
            )
            for line in diverge_label.splitlines():
                labels_text += f"  {line}\n"
            labels_text += "\nrefine_label: |\n"
            for line in refine_label.splitlines():
                labels_text += f"  {line}\n"
            with open(labels_path, "w") as f:
                f.write(labels_text)
            logger.info(
                f"Saved labels to {labels_path} ({len(diverge_label)}/{len(refine_label)} chars)"
            )
        except Exception as e:
            logger.warning(f"Failed to save labels.yaml: {e}")
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-coevolve_logging.log_search_algorithm_generated]]
