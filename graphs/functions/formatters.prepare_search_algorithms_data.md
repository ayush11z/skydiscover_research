---
name: formatters.prepare_search_algorithms_data
description: function in skydiscover/context_builder/evox/formatters.py (context-builder)
metadata:
  type: project
---

# formatters.prepare_search_algorithms_data

**File:** `skydiscover/context_builder/evox/formatters.py:489`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
def prepare_search_algorithms_data(
    other_context_programs: Union[List[Program], Dict[str, List[Program]]],
    format_stats_diff=format_db_stats_diff,
    filter_by_horizon=filter_db_stats_by_horizon,
) -> List[Dict[str, Any]]:
    """Prepare data for batch summarization of context programs."""
    if not other_context_programs:
        return []

    if isinstance(other_context_programs, dict):
        flat_programs = []
        for programs in other_context_programs.values():
            if programs:
                flat_programs.extend(programs)
        programs_list = flat_programs
    else:
        programs_list = other_context_programs

    all_programs_data = []

    for idx, program in enumerate(programs_list, start=1):
        solution = prog_attr(program, "solution")
        metrics = prog_attr(program, "metrics", {})
        metadata = prog_attr(program, "metadata", {})

        start_db_stats = metadata.get("start_db_stats")
        end_db_stats = metadata.get("end_db_stats")
        horizon = int(metrics.get("search_window_horizon", 0))

        if start_db_stats and end_db_stats:
            start_db_stats = filter_by_horizon(start_db_stats, horizon)
            end_db_stats = filter_by_horizon(end_db_stats, horizon)

        if start_db_stats and end_db_stats:
            db_stats_text = format_stats_diff(start_db_stats, end_db_stats, horizon=horizon)
            all_programs_data.append(
                {
                    "program_num": idx,
                    "solution": solution,
                    "db_stats_text": db_stats_text,
                    "combined_score": metrics.get("combined_score", 0.0),
                    "improvement": metrics.get("search_window_end_score", 0.0)
                    - metrics.get("search_window_start_score", 0.0),
                }
            )

    return all_programs_data
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[base_database.Program]]
- [[formatters.filter_db_stats_by_horizon]]
- [[formatters.format_db_stats_diff]]
- [[utils.prog_attr]]

## ← Called by
- [[EvoxContextBuilder.build_prompt]]
