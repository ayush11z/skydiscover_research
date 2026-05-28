---
name: IN-formatters.format_execution_trace
description: function in skydiscover/context_builder/evox/formatters.py (context-builder)
metadata:
  type: project
---

# formatters.format_execution_trace

**File:** `skydiscover/context_builder/evox/formatters.py:34`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
def format_execution_trace(execution_trace: list, window_start_score: float = None) -> str:
    """Format execution trace with program/parent/context tuples."""
    if not execution_trace:
        return ""

    def fmt_id(pid):
        return pid[:8] if pid and len(pid) > 8 else (pid or "None")

    def fmt_score(s):
        return f"{s:.4f}" if s is not None else "N/A"

    def unpack_tuple(t):
        if not t:
            return None, None, None
        if len(t) >= 3:
            return t[0], t[1], t[2]
        return None, t[0], t[1]

    def fmt_program_ref(t, prefix=""):
        label, pid, score = unpack_tuple(t)
        if pid is None:
            return f"{prefix}=None (seed program)" if prefix else "None"
        label_str = f'label="{label}", ' if label else ""
        return (
            f"{prefix} ({label_str}id={fmt_id(pid)}, score={fmt_score(score)})"
            if prefix
            else f"({label_str}id={fmt_id(pid)}, score={fmt_score(score)})"
        )

    lines = []
    best = window_start_score

    for entry in execution_trace:
        prog_tuple = entry.get("program")
        if prog_tuple is None:
            continue

        _, _, prog_score = unpack_tuple(prog_tuple)
        _, _, parent_score = unpack_tuple(entry.get("parent"))

        parent_str = fmt_program_ref(entry.get("parent"), "Parent")
        ctx = entry.get("context") or []
        context_str = f"Context=[{', '.join(fmt_program_ref(c) for c in ctx)}]"

        if prog_score is not None:
            prog_score, parent_score = round(prog_score, 4), (
                round(parent_score, 4) if parent_score is not None else None
            )
            if best is None:
                best, outcome = prog_score, "first program"
            elif prog_score > best:
                outcome, best = f"⭐ NEW BEST (was {best:.4f})", prog_score
            elif parent_score is not None and prog_score > parent_score:
                outcome = f"above parent, best still {best:.4f}"
            elif parent_score is not None and prog_score < parent_score:
                outcome = f"regression, best still {best:.4f}"
            else:
                outcome = f"no change, best still {best:.4f}"
        else:
            outcome = "N/A"

        lines.extend(
            [
                f"Iter {entry.get('iteration', '?')}: {parent_str}, {context_str}",
                f"       -> Generated child score={fmt_score(prog_score)} ({outcome})",
                "",
            ]
        )

    return "\n".join(lines[:-1]) if lines else ""
````

## → Calls
- [[IN-ProgramDatabase.get]]
- [[IN-format_execution_trace.fmt_program_ref]]
- [[IN-format_execution_trace.fmt_score]]
- [[IN-format_execution_trace.unpack_tuple]]

## ← Called by
- [[IN-formatters.format_db_stats_diff]]
