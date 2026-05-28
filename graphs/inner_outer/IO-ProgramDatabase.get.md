---
name: IO-ProgramDatabase.get
description: method in skydiscover/search/base_database.py (database)
metadata:
  type: project
---

# ProgramDatabase.get

**File:** `skydiscover/search/base_database.py:295`  
**Kind:** method  
**Layer:** #database

## Source
````python
    def get(self, program_id: str) -> Optional[Program]:
        """Get a program by ID"""
        return self.programs.get(program_id)
````

## → Calls
- [[IO-base_database.Program]]

## ← Called by
- [[IO-DiscoveryController._run_iteration]]
- [[IO-EvoxContextBuilder.build_prompt]]
- [[IO-formatters.filter_db_stats_by_horizon]]
- [[IO-formatters.format_current_program]]
- [[IO-formatters.format_db_stats_diff]]
- [[IO-formatters.format_execution_trace]]
- [[IO-formatters.format_population_state]]
- [[IO-formatters.format_search_window_context]]
- [[IO-formatters.format_single_program_section]]
- [[IO-formatters.identify_search_improvement_areas]]
- [[IO-formatters.prepare_search_algorithms_data]]
- [[IO-search_strategy_evaluator.evaluate]]
