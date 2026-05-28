---
name: IO-CoEvolutionController._init_search_evolution_controller
description: method in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# CoEvolutionController._init_search_evolution_controller

**File:** `skydiscover/search/evox/controller.py:52`  
**Kind:** method  
**Layer:** #outer-loop

## Source
````python
    def _init_search_evolution_controller(self) -> None:
        """This creates a second DiscoveryController — one for evolving search strategies. So have two controllers running:
            self — evolves circle packing solutions
            self.search_controller — evolves search strategies"""
        
        """Initialize search controller, scorer, and load initial algorithm."""
        db_cfg = self.config.search.database
        if not db_cfg.database_file_path:
            raise ValueError(
                "config.search.database.database_file_path is required for co-evolution"
            )

        controller_input, self._search_initial_code = setup_search(
            initial_program_path=db_cfg.database_file_path,
            evaluation_file=db_cfg.evaluation_file,
            config_path=db_cfg.config_path,
            output_dir=self.config.search.output_dir,
            evaluator_env_vars=self.evaluator_env_vars,
            parent_llm_config=self.config.llm if self.config.search.share_llm else None,
        )
        self.search_controller = DiscoveryController(controller_input)
        self.search_scorer = LogWindowScorer()
        self._active_search_algorithm_code = self._search_initial_code

        self._log_coevolution_setup(db_cfg)
        self._init_search_tracking()
````

## → Calls
- [[IO-CoEvolutionController._init_search_tracking]]
- [[IO-CoEvolutionController._log_coevolution_setup]]
- [[IO-DiscoveryController.__init__]]
- [[IO-DiscoveryControllerInput.config]]
- [[IO-DiscoveryControllerInput.evaluation_file]]
- [[IO-DiscoveryControllerInput.evaluator_env_vars]]
- [[IO-LogWindowScorer.__init__]]
- [[IO-default_discovery_controller.DiscoveryController]]
- [[IO-search_scorer.LogWindowScorer]]

## ← Called by
- [[IO-CoEvolutionController.__init__]]
