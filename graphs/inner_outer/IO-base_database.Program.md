---
name: IO-base_database.Program
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
- [[IO-ContextBuilder.build_prompt]]
- [[IO-DiscoveryController._build_prompt]]
- [[IO-DiscoveryController._create_child_program]]
- [[IO-DiscoveryController._finalize_discovery]]
- [[IO-DiscoveryController._process_iteration_result]]
- [[IO-DiscoveryController._run_discovery_parallel]]
- [[IO-DiscoveryController._run_discovery_sequential]]
- [[IO-DiscoveryController._run_from_scratch_iteration]]
- [[IO-DiscoveryController.run_discovery]]
- [[IO-EvoxContextBuilder.build_prompt]]
- [[IO-ProgramDatabase.__init__]]
- [[IO-ProgramDatabase._is_better]]
- [[IO-ProgramDatabase._save_program]]
- [[IO-ProgramDatabase._update_best_program]]
- [[IO-ProgramDatabase.add]]
- [[IO-ProgramDatabase.get]]
- [[IO-ProgramDatabase.get_best_program]]
- [[IO-ProgramDatabase.get_top_programs]]
- [[IO-ProgramDatabase.sample]]
- [[IO-Runner._get_best_program]]
- [[IO-Runner._save_best_program]]
- [[IO-Runner.run]]
- [[IO-formatters.format_current_program]]
- [[IO-formatters.format_search_algorithms]]
- [[IO-formatters.format_single_program_section]]
- [[IO-formatters.identify_search_improvement_areas]]
- [[IO-formatters.prepare_search_algorithms_data]]
- [[IO-initial_search_strategy.EvolvedProgram]]
- [[IO-search_strategy_db.SearchStrategy]]
- [[IO-search_strategy_evaluator.evaluate]]
