---
name: OpenEvolveNativeDatabase.__init__
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase.__init__

**File:** `skydiscover/search/openevolve_native/database.py:99`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def __init__(self, name: str, config: DatabaseConfig, **kwargs: Any):
        # --- Read config (getattr for fields not on base DatabaseConfig) ---
        self.num_islands: int = getattr(config, "num_islands", 5)
        self.population_size: int = getattr(config, "population_size", 40)
        self.archive_size: int = getattr(config, "archive_size", 100)
        self.exploration_ratio: float = getattr(config, "exploration_ratio", 0.2)
        self.exploitation_ratio: float = getattr(config, "exploitation_ratio", 0.7)
        self.elite_selection_ratio: float = getattr(config, "elite_selection_ratio", 0.1)
        self.feature_dimensions: List[str] = list(
            getattr(config, "feature_dimensions", ["complexity", "diversity"])
        )

        raw_bins = getattr(config, "feature_bins", 10)
        if isinstance(raw_bins, int):
            self.feature_bins: int = max(
                raw_bins,
                int(pow(self.archive_size, 1 / max(len(self.feature_dimensions), 1)) + 0.99),
            )
        else:
            self.feature_bins = 10

        if isinstance(raw_bins, dict):
            self.feature_bins_per_dim: Dict[str, int] = raw_bins
        else:
            self.feature_bins_per_dim = {d: self.feature_bins for d in self.feature_dimensions}

        self.diversity_reference_size: int = getattr(config, "diversity_reference_size", 20)
        self.migration_interval: int = getattr(config, "migration_interval", 10)
        self.migration_rate: float = getattr(config, "migration_rate", 0.1)

        # --- Island state (MUST be set before super().__init__ which may
        #     call self.load() if db_path exists) ---
        self.islands: List[Set[str]] = [set() for _ in range(self.num_islands)]
        self.island_feature_maps: List[Dict[str, str]] = [{} for _ in range(self.num_islands)]
        self.island_best_programs: List[Optional[str]] = [None] * self.num_islands
        self.island_generations: List[int] = [0] * self.num_islands
        self.current_island: int = 0
        self.last_migration_generation: int = 0

        # --- Global archive ---
        self.archive: Set[str] = set()

        # --- Feature scaling ---
        self.feature_stats: Dict[str, Dict[str, Any]] = {}

        # --- Diversity cache ---
        self.diversity_cache: Dict[int, Dict[str, float]] = {}
        self.diversity_cache_size: int = 1000
        self.diversity_reference_set: List[str] = []

        # --- Now safe to call super (which may trigger self.load) ---
        super().__init__(name, config, **kwargs)

        # --- Seed RNG ---
        random_seed = getattr(config, "random_seed", None)
        if random_seed is not None:
            random.seed(random_seed)

        logger.info(
            "OpenEvolveNativeDatabase: %d islands, pop=%d, archive=%d, "
            "features=%s, bins=%d, migration_interval=%d, migration_rate=%.2f",
            self.num_islands,
            self.population_size,
            self.archive_size,
            self.feature_dimensions,
            self.feature_bins,
            self.migration_interval,
            self.migration_rate,
        )
````

## → Calls
- [[ProgramDatabase.__init__]]
- [[config.DatabaseConfig]]

## ← Called by
_(entry point — nothing in this graph calls it)_
