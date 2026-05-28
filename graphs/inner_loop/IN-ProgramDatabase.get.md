---
name: IN-ProgramDatabase.get
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
- [[IN-base_database.Program]]

## ← Called by
- [[IN-DiscoveryController._run_iteration]]
- [[IN-EvoxContextBuilder.build_prompt]]
- [[IN-formatters.filter_db_stats_by_horizon]]
- [[IN-formatters.format_current_program]]
- [[IN-formatters.format_db_stats_diff]]
- [[IN-formatters.format_execution_trace]]
- [[IN-formatters.format_population_state]]
- [[IN-formatters.format_search_window_context]]
- [[IN-formatters.format_single_program_section]]
- [[IN-formatters.identify_search_improvement_areas]]
- [[IN-formatters.prepare_search_algorithms_data]]
