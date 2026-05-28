---
name: AdaEvolveDatabase._init_archives
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._init_archives

**File:** `skydiscover/search/adaevolve/database.py:287`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _init_archives(self, config: DatabaseConfig) -> None:
        """Initialize per-island UnifiedArchives."""
        higher_is_better = getattr(config, "higher_is_better", {})
        pareto_objectives = getattr(config, "pareto_objectives", [])
        pareto_objectives_weight = getattr(config, "pareto_objectives_weight", 0.0)
        self._diversity_strategy_type = getattr(config, "diversity_strategy", "code")

        for i in range(self.num_islands):
            archive_config = ArchiveConfig(
                max_size=config.population_size,
                k_neighbors=getattr(config, "k_neighbors", 5),
                elite_ratio=getattr(config, "archive_elite_ratio", 0.2),
                pareto_weight=getattr(config, "pareto_weight", 0.4),
                fitness_weight=getattr(config, "fitness_weight", 0.3),
                novelty_weight=getattr(config, "novelty_weight", 0.3),
                higher_is_better=higher_is_better,
                pareto_objectives=pareto_objectives,
                pareto_objectives_weight=pareto_objectives_weight,
                fitness_key=getattr(config, "fitness_key", None),
            )

            # Create FRESH diversity strategy per island
            # This is critical for stateful strategies like MetricDiversity
            # which maintain internal state (KNN archive) that would be
            # contaminated if shared across islands
            diversity_strategy = create_diversity_strategy(
                self._diversity_strategy_type,
                higher_is_better=higher_is_better,
            )

            archive = UnifiedArchive(
                config=archive_config,
                diversity_strategy=diversity_strategy,
            )
            self.archives.append(archive)

        logger.debug(
            f"Initialized {self.num_islands} archives: "
            f"max_size={config.population_size}, diversity={self._diversity_strategy_type}"
        )
````

## → Calls
- [[AdaEvolveDatabase.__init__]]
- [[AdaEvolveDatabaseConfig.population_size]]
- [[GEPANativeDatabaseConfig.population_size]]
- [[OpenEvolveNativeDatabaseConfig.population_size]]
- [[config.DatabaseConfig]]
- [[diversity.create_diversity_strategy]]
- [[unified_archive.ArchiveConfig]]
- [[unified_archive.UnifiedArchive]]

## ← Called by
- [[AdaEvolveDatabase.__init__]]
- [[AdaEvolveDatabase.load]]
