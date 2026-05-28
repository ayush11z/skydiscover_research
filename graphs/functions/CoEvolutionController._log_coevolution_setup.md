---
name: CoEvolutionController._log_coevolution_setup
description: method in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# CoEvolutionController._log_coevolution_setup

**File:** `skydiscover/search/evox/controller.py:613`  
**Kind:** method  
**Layer:** #outer-loop

## Source
````python
    def _log_coevolution_setup(self, db_cfg) -> None:
        logger.info("=" * 70)
        logger.info("[EVOX CO-EVOLUTION SETUP]")
        logger.info("-" * 70)
        logger.info(f"  [SOLUTION EVOLUTION]")
        logger.info(f"    Initial search strategy file : {db_cfg.database_file_path}")
        logger.info(f"    Solution database class      : {self.database.__class__.__name__}")
        logger.info(f"  [META EVOLUTION OF SEARCH STRATEGY]")
        logger.info(
            f"    Search strategy database class: {self.search_controller.database.__class__.__name__}"
        )
        logger.info(f"    Search strategy evaluator     : {db_cfg.evaluation_file}")
        logger.info(f"    Search strategy config        : {db_cfg.config_path}")
        logger.info("=" * 70)
````

## → Calls
- [[DiscoveryControllerInput.evaluation_file]]
- [[EvaluatorConfig.evaluation_file]]
- [[EvolveDatabaseConfig.database_file_path]]
- [[EvoxDatabaseConfig.config_path]]
- [[EvoxDatabaseConfig.evaluation_file]]

## ← Called by
- [[CoEvolutionController._init_search_evolution_controller]]
