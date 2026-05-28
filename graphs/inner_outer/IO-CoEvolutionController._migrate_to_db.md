---
name: IO-CoEvolutionController._migrate_to_db
description: method in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# CoEvolutionController._migrate_to_db

**File:** `skydiscover/search/evox/controller.py:506`  
**Kind:** method  
**Layer:** #outer-loop

## Source
````python
    def _migrate_to_db(self, new_db) -> int:
        """Migrate all programs and prompts from current database to new database."""
        prog_class = getattr(new_db, "_program_class", None)
        for program in sorted(self.database.programs.values(), key=lambda x: x.iteration_found):
            converted = prog_class(**program.to_dict()) if prog_class else program
            new_db.add(converted, iteration=program.iteration_found)
        migrated = len(self.database.programs)

        # Migrate prompts
        if self.database.config.log_prompts:
            if new_db.prompts_by_program is None:
                new_db.prompts_by_program = {}

            old_prompts = self.database.prompts_by_program or {}
            new_db.prompts_by_program.update(
                {k: v for k, v in old_prompts.items() if k not in new_db.prompts_by_program}
            )

            for p in new_db.programs.values():
                if p.prompts and p.id not in new_db.prompts_by_program:
                    new_db.prompts_by_program[p.id] = p.prompts

        return migrated
````

## → Calls
- [[IO-DiscoveryControllerInput.config]]

## ← Called by
- [[IO-CoEvolutionController._switch_to_new_search_algorithm]]
