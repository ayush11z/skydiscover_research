---
name: IN-base_database.Program
description: class in skydiscover/search/base_database.py (database)
metadata:
  type: project
---

# base_database.Program

**File:** `skydiscover/search/base_database.py:24`  
**Kind:** class  
**Layer:** #database

## Source
````python
class Program:
    """Represents a program in the database"""

    # Program identification
    id: str
    solution: str
    language: str = "python"

    # Performance
    metrics: Dict[str, Any] = field(default_factory=dict)

    # Tracking information
    iteration_found: int = 0
    parent_id: Optional[str] = None  # Parent program ID it mutates from
    other_context_ids: Optional[List[str]] = (
        None  # other program IDs to provide as context to generate this program
    )
    parent_info: Optional[Tuple[str, str]] = None  # information about the parent program
    context_info: Optional[List[Tuple[str, str]]] = None  # information about the context programs

    timestamp: float = field(default_factory=time.time)

    # Metadata
    metadata: Dict[str, Any] = field(default_factory=dict)
    artifacts: Dict[str, Any] = field(default_factory=dict)

    # Prompts
    prompts: Optional[Dict[str, Any]] = None
    generation: int = 0

````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IN-ContextBuilder.build_prompt]]
- [[IN-DiscoveryController._build_prompt]]
- [[IN-DiscoveryController._create_child_program]]
- [[IN-DiscoveryController._finalize_discovery]]
- [[IN-DiscoveryController._process_iteration_result]]
- [[IN-DiscoveryController._run_discovery_parallel]]
- [[IN-DiscoveryController._run_discovery_sequential]]
- [[IN-DiscoveryController._run_from_scratch_iteration]]
- [[IN-DiscoveryController.run_discovery]]
- [[IN-EvoxContextBuilder.build_prompt]]
- [[IN-ProgramDatabase.__init__]]
- [[IN-ProgramDatabase._is_better]]
- [[IN-ProgramDatabase._save_program]]
- [[IN-ProgramDatabase._update_best_program]]
- [[IN-ProgramDatabase.add]]
- [[IN-ProgramDatabase.get]]
- [[IN-ProgramDatabase.get_best_program]]
- [[IN-ProgramDatabase.get_top_programs]]
- [[IN-ProgramDatabase.sample]]
- [[IN-formatters.format_current_program]]
- [[IN-formatters.format_search_algorithms]]
- [[IN-formatters.format_single_program_section]]
- [[IN-formatters.identify_search_improvement_areas]]
- [[IN-formatters.prepare_search_algorithms_data]]
