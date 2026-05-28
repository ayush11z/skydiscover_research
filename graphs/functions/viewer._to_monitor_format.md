---
name: viewer._to_monitor_format
description: function in skydiscover/extras/monitor/viewer.py (monitor)
metadata:
  type: project
---

# viewer._to_monitor_format

**File:** `skydiscover/extras/monitor/viewer.py:140`  
**Kind:** function  
**Layer:** #monitor

## Source
````python
def _to_monitor_format(prog: Dict, all_progs: Dict[str, Dict]) -> Dict:
    """Convert checkpoint program dict → monitor event program dict."""
    metrics = prog.get("metrics") or {}
    score = metrics.get("combined_score", 0.0)
    if not isinstance(score, (int, float)):
        score = 0.0

    parent_id = prog.get("parent_id")
    parent_score = None
    parent_iter = None
    if parent_id and parent_id in all_progs:
        pm = all_progs[parent_id].get("metrics") or {}
        parent_score = pm.get("combined_score")
        parent_iter = all_progs[parent_id].get("iteration_found")

    context_ids = prog.get("other_context_ids") or []
    context_scores = []
    for cid in context_ids:
        if cid in all_progs:
            cm = all_progs[cid].get("metrics") or {}
            context_scores.append(cm.get("combined_score"))
        else:
            context_scores.append(None)

    # Label
    label_type = "unknown"
    pi = prog.get("parent_info")
    if pi and isinstance(pi, (list, tuple)) and len(pi) >= 1:
        ls = str(pi[0]).lower()
        if "diverge" in ls:
            label_type = "diverge"
        elif "refine" in ls:
            label_type = "refine"
        elif "crossover" in ls:
            label_type = "crossover"
    if label_type == "unknown":
        label_type = (prog.get("metadata") or {}).get("label_type", "unknown")

    island = (prog.get("metadata") or {}).get("island")
    image_path = (prog.get("metadata") or {}).get("image_path")
    solution = prog.get("solution", "")

    from skydiscover.extras.monitor.callback import _safe_metrics

    return {
        "id": prog["id"],
        "iteration": prog.get("iteration_found", 0),
        "score": score,
        "metrics": _safe_metrics(metrics),
        "parent_id": parent_id,
        "parent_score": parent_score,
        "parent_iter": parent_iter,
        "context_ids": context_ids,
        "context_scores": context_scores,
        "label_type": label_type,
        "solution_snippet": solution[:500],
        "island": island,
        "generation": prog.get("generation", 0),
        "image_path": image_path,
    }
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[callback._safe_metrics]]

## ← Called by
- [[viewer.main]]
