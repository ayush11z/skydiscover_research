---
name: CoEvolutionController._switch_to_new_search_algorithm
description: method in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# CoEvolutionController._switch_to_new_search_algorithm

**File:** `skydiscover/search/evox/controller.py:424`  
**Kind:** method  
**Layer:** #outer-loop

## What it does
Dynamically loads the LLM-generated Python code as a new `EvolvedProgramDatabase` class, migrates all existing programs from the old database to it, and replaces `self.database`. The old database is kept as `self._fallback_database` in case the new strategy crashes.

## Source
````python
    def _switch_to_new_search_algorithm(self, result: SerializableResult) -> bool:
        """Switch solution database to use the new search algorithm."""
        child_dict = result.child_program_dict or {}
        search_code = child_dict.get("solution")
        if not search_code:
            logger.warning("No solution in search result; skipping transition")
            return False

        search_program_id = child_dict.get("id", "unknown")
        fd, file_path = tempfile.mkstemp(suffix=".py", prefix="evox_search_")
        try:
            with os.fdopen(fd, "w") as f:
                f.write(search_code)

            # Load the new search algorithm database
            new_db_class, prog_class = load_database_from_file(file_path)
            # Ensure labels exist for databases that use them in __init__ (before _assign_labels_to_db)
            if not hasattr(new_db_class, "DIVERGE_LABEL"):
                new_db_class.DIVERGE_LABEL = ""
            if not hasattr(new_db_class, "REFINE_LABEL"):
                new_db_class.REFINE_LABEL = ""
            new_db = new_db_class(self.config.search.type, self.config.search.database)
            new_db._program_class = prog_class

            # Assign labels to the new search algorithm database
            self._assign_labels_to_db(new_db)

            # Migrate programs and prompts from the current database to the new database
            migrated_count = self._migrate_to_db(new_db)

            self._wrap_add_method(new_db)
            new_db.get_best_program()  # Sets best_program_id (None -> actual best)

            self._fallback_database = self.database
            self._fallback_search_code = self._active_search_algorithm_code

            self.database = new_db
            if self.evaluator.llm_judge:
                self.evaluator.llm_judge.database = new_db
            logger.info(
                f"Switched to search algorithm {search_program_id} ({migrated_count} programs migrated)"
            )

            self._active_search_algorithm_code = search_code
            return True

        except Exception as e:
            logger.error(f"Failed to load search algorithm {search_program_id}: {e}")
            return False
        finally:
            if os.path.exists(file_path):
                os.unlink(file_path)
````

## → Calls
- [[CoEvolutionController._assign_labels_to_db]]
- [[CoEvolutionController._migrate_to_db]]
- [[CoEvolutionController._wrap_add_method]]
- [[Config.evaluator]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[DiscoveryControllerInput.config]]
- [[DiscoveryControllerInput.database]]
- [[ProgramDatabase.get_best_program]]
- [[SearchConfig.database]]
- [[SerializableResult.child_program_dict]]
- [[SerializableResult.error]]
- [[default_discovery_controller.DiscoveryController]]
- [[discovery_utils.SerializableResult]]
- [[discovery_utils.load_database_from_file]]
- [[evaluation.create_evaluator]]
- [[registry.setup_search]]

## ← Called by
- [[CoEvolutionController._generate_and_validate_search_algorithm]]
