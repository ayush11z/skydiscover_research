---
name: GEPANativeDatabase.__init__
description: method in skydiscover/search/gepa_native/database.py (gepa)
metadata:
  type: project
---

# GEPANativeDatabase.__init__

**File:** `skydiscover/search/gepa_native/database.py:53`  
**Kind:** method  
**Layer:** #gepa

## Source
````python
    def __init__(self, name: str, config: DatabaseConfig, **kwargs: Any):
        # Read GEPA-specific config before super().__init__ (which may call load)
        self.population_size: int = getattr(config, "population_size", 40)
        self.candidate_selection_strategy: str = getattr(
            config, "candidate_selection_strategy", "epsilon_greedy"
        )
        self.epsilon: float = getattr(config, "epsilon", 0.1)
        max_rejection_history: int = getattr(config, "max_rejection_history", 20)
        seed: int = getattr(config, "random_seed", 42) or 42

        self.elite_pool: List[str] = []  # program IDs sorted by score desc
        self.rejection_history: collections.deque = collections.deque(maxlen=max_rejection_history)
        self.metric_best: Dict[str, Tuple[str, float]] = {}  # metric -> (prog_id, value)
        self.program_at_metric_front: Dict[str, Set[str]] = {}  # metric -> set of prog_ids at best
        self.rng = random.Random(seed)

        super().__init__(name, config, **kwargs)
````

## → Calls
- [[ProgramDatabase.__init__]]
- [[config.DatabaseConfig]]

## ← Called by
- [[GEPANativeDatabase._rebuild_elite_pool]]
- [[GEPANativeDatabase._select_other_context_programs]]
- [[GEPANativeDatabase.add]]
- [[GEPANativeDatabase.get_merge_candidates]]
- [[GEPANativeDatabase.save]]
