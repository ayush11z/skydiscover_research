---
name: callback._push_program_event
description: function in skydiscover/extras/monitor/callback.py (monitor)
metadata:
  type: project
---

# callback._push_program_event

**File:** `skydiscover/extras/monitor/callback.py:37`  
**Kind:** function  
**Layer:** #monitor

## Source
````python
def _push_program_event(
    server: MonitorServer,
    database: Any,
    program: Any,
    iteration: int,
    result: Any,
    start_time: float,
) -> None:
    """Serialize program data and push to the monitor server."""
    metrics = program.metrics or {}
    score = metrics.get("combined_score", 0.0)
    if not isinstance(score, (int, float)):
        score = 0.0

    parent_id = getattr(program, "parent_id", None)
    parent_score = None
    parent_iter = None
    parent_solution = ""
    if parent_id:
        parent_prog = database.get(parent_id) if hasattr(database, "get") else None
        if parent_prog:
            parent_metrics = parent_prog.metrics or {}
            parent_score = parent_metrics.get("combined_score")
            parent_iter = getattr(parent_prog, "iteration_found", None)
            parent_solution = getattr(parent_prog, "solution", "")

    context_ids = getattr(program, "other_context_ids", None) or []
    context_scores = []
    for cid in context_ids:
        cp = database.get(cid) if hasattr(database, "get") else None
        if cp and cp.metrics:
            context_scores.append(cp.metrics.get("combined_score"))
        else:
            context_scores.append(None)

    # Label type from parent_info or metadata
    label_type = None
    parent_info = getattr(program, "parent_info", None)
    if parent_info and isinstance(parent_info, (list, tuple)) and len(parent_info) >= 1:
        label_str = str(parent_info[0]).lower()
        if "diverge" in label_str:
            label_type = "diverge"
        elif "refine" in label_str:
            label_type = "refine"
        elif "crossover" in label_str:
            label_type = "crossover"
    md = getattr(program, "metadata", {}) or {}
    if label_type is None:
        label_type = md.get("label_type", "unknown")

    island = md.get("island")

    is_best = getattr(database, "best_program_id", None) == program.id

    # Solution snippet (first N chars)
    code = getattr(program, "solution", "") or ""
    solution_snippet = code[:SOLUTION_SNIPPET_LENGTH]

    # Image path from metadata (image evolution mode)
    image_path = (getattr(program, "metadata", {}) or {}).get("image_path")

    total_programs = len(database.programs) if hasattr(database, "programs") else 0
    best_prog = database.get_best_program() if hasattr(database, "get_best_program") else None
    best_score = 0.0
    if best_prog and best_prog.metrics:
        best_score = best_prog.metrics.get("combined_score", 0.0)

    elapsed = time.time() - start_time
    rate = total_programs / elapsed * 60 if elapsed > 0 else 0.0

    iters_since_improvement = 0
    if best_prog:
        best_iter = getattr(best_prog, "iteration_found", 0)
        iters_since_improvement = iteration - best_iter

    prog_data = {
        "id": program.id,
        "iteration": iteration,
        "score": score,
        "metrics": _safe_metrics(metrics),
        "parent_id": parent_id,
        "parent_score": parent_score,
        "parent_iter": parent_iter,
        "context_ids": context_ids,
        "context_scores": context_scores,
        "label_type": label_type,
        "solution_snippet": solution_snippet,
        "island": island,
        "is_best": is_best,
        "generation": getattr(program, "generation", 0),
        "image_path": image_path,
    }

    stats = {
        "total_programs": total_programs,
        "current_iteration": iteration,
        "best_score": best_score,
        "iterations_since_improvement": iters_since_improvement,
        "programs_per_min": round(rate, 1),
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
````

## → Calls
- [[EvaluationResult.metrics]]
- [[LangFuseTracer.get]]
- [[MonitorConfig.max_solution_length]]
- [[MonitorServer.push_event]]
- [[Program.id]]
- [[Program.metrics]]
- [[ProgramDatabase.get]]
- [[ProgramDatabase.get_best_program]]
- [[UnifiedArchive.get]]
- [[callback._safe_metrics]]
- [[server.MonitorServer]]

## ← Called by
- [[create_monitor_callback._callback]]
