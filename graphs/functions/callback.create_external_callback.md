---
name: callback.create_external_callback
description: function in skydiscover/extras/monitor/callback.py (monitor)
metadata:
  type: project
---

# callback.create_external_callback

**File:** `skydiscover/extras/monitor/callback.py:153`  
**Kind:** function  
**Layer:** #monitor

## Source
````python
def create_external_callback(
    server: MonitorServer,
    start_time: float,
) -> Callable:
    """Create a monitor callback for external backends (no ProgramDatabase needed).

    Maintains its own lightweight program store for parent lookups and best tracking.
    Used by OpenEvolve, ShinkaEvolve, and GEPA backends.
    """
    programs: Dict[str, Any] = {}
    best_score = -float("inf")
    best_id: Optional[str] = None

    def _callback(program: Any, iteration: int) -> None:
        nonlocal best_score, best_id
        try:
            programs[program.id] = program

            score = (program.metrics or {}).get("combined_score", 0.0)
            if not isinstance(score, (int, float)):
                score = 0.0
            if score > best_score:
                best_score = score
                best_id = program.id
            is_best = program.id == best_id

            parent_id = getattr(program, "parent_id", None)
            parent_score, parent_solution = None, ""
            if parent_id and parent_id in programs:
                p = programs[parent_id]
                parent_score = (p.metrics or {}).get("combined_score")
                parent_solution = getattr(p, "solution", "")

            code = getattr(program, "solution", "") or ""
            elapsed = time.time() - start_time

            prog_data = {
                "id": program.id,
                "iteration": iteration,
                "score": score,
                "metrics": _safe_metrics(program.metrics or {}),
                "parent_id": parent_id,
                "parent_score": parent_score,
                "parent_iter": None,
                "context_ids": [],
                "context_scores": [],
                "label_type": "unknown",
                "solution_snippet": code[:SOLUTION_SNIPPET_LENGTH],
                "island": None,
                "is_best": is_best,
                "generation": getattr(program, "generation", 0),
                "image_path": (getattr(program, "metadata", {}) or {}).get("image_path"),
            }
            stats = {
                "total_programs": len(programs),
                "current_iteration": iteration,
                "best_score": best_score if best_score > -float("inf") else 0.0,
                "iterations_since_improvement": 0,
                "programs_per_min": round(len(programs) / elapsed * 60, 1) if elapsed > 0 else 0.0,
                "elapsed_seconds": round(elapsed, 1),
            }
            event = {
                "type": "new_program",
                "program": prog_data,
                "stats": stats,
                "is_best": is_best,
                "full_solution": code[: server.max_solution_length],
                "parent_full_solution": (
                    parent_solution[: server.max_solution_length] if parent_solution else ""
                ),
            }
            server.push_event(event)
        except Exception:
            logger.debug("External monitor callback error", exc_info=True)

    return _callback
````

## → Calls
- [[create_external_callback._callback]]
- [[server.MonitorServer]]

## ← Called by
- [[monitor.start_monitor]]
