---
name: IN-ProgramDatabase.__init__
description: method in skydiscover/search/base_database.py (database)
metadata:
  type: project
---

# ProgramDatabase.__init__

**File:** `skydiscover/search/base_database.py:87`  
**Kind:** method  
**Layer:** #database

## Source
````python
    def __init__(self, name: str, config: DatabaseConfig, **kwargs: Any):
        self.name = name
        self.config = config

        # In-memory program storage
        self.programs: Dict[str, Program] = {}

        # Track the last iteration number (for resuming)
        self.last_iteration: int = 0

        # Optionally track initial program info (set by controller on first add)
        self.initial_program_id: Optional[str] = None
        self.initial_program_score: Optional[float] = None

        # Best program tracking
        self.best_program_id: Optional[str] = None

        # Prompt log
        self.prompts_by_program: Optional[Dict[str, Dict[str, Dict[str, str]]]] = None

        # Initialize checkpoint manager (imported here to avoid circular imports)
        from skydiscover.search.utils.checkpoint_manager import CheckpointManager

        self.checkpoint_manager = CheckpointManager(self.config)

        # Load database from disk if path is provided
        if config.db_path and os.path.exists(config.db_path):
            self.load(config.db_path)
````

## → Calls
- [[IN-ProgramDatabase.load]]
- [[IN-base_database.Program]]

## ← Called by
- [[IN-DiscoveryController._call_llm]]
- [[IN-DiscoveryController._create_child_program]]
- [[IN-DiscoveryController._run_from_scratch_iteration]]
- [[IN-EvoxContextBuilder.__init__]]
- [[IN-Program.from_dict]]
- [[IN-ProgramDatabase.log_prompt]]
