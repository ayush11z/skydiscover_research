---
name: IO-coevolve_logging.update_saved_search_algorithm_score
description: function in skydiscover/search/evox/utils/coevolve_logging.py (evox)
metadata:
  type: project
---

# coevolve_logging.update_saved_search_algorithm_score

**File:** `skydiscover/search/evox/utils/coevolve_logging.py:139`  
**Kind:** function  
**Layer:** #evox

## Source
````python
async def update_saved_search_algorithm_score(
    outputs_dir: str,
    iteration: int,
    result: SerializableResult,
    is_new_best: bool,
    db_stats: Dict[str, Any],
) -> None:
    """Update the saved metadata file with the newly assigned score."""
    metadata_path = os.path.join(outputs_dir, f"iteration_{iteration}", "metadata.json")

    if not os.path.exists(metadata_path):
        logger.warning(
            f"Metadata file not found for iteration {iteration}, cannot update search strategy score"
        )
        return

    with open(metadata_path, "r") as f:
        metadata = json.load(f)

    child_dict = result.child_program_dict or {}
    metrics = child_dict.get("metrics", {})
    metadata["combined_score"] = metrics.get("combined_score")
    metadata["metrics"] = make_json_serializable(metrics)
    metadata["pending_score"] = False
    metadata["is_new_best"] = bool(is_new_best)

    start_db_stats = child_dict.get("metadata", {}).get("start_db_stats")
    if start_db_stats:
        metadata["start_db_stats"] = make_json_serializable(start_db_stats)

    metadata["end_db_stats"] = make_json_serializable(db_stats)

    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=2)
````

## → Calls
- [[IO-coevolve_logging.make_json_serializable]]

## ← Called by
- [[IO-CoEvolutionController._finalize_pending_search]]
