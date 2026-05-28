---
name: IO-ProgramDatabase.log_status
description: method in skydiscover/search/base_database.py (database)
metadata:
  type: project
---

# ProgramDatabase.log_status

**File:** `skydiscover/search/base_database.py:334`  
**Kind:** method  
**Layer:** #database

## Source
````python
    def log_status(self) -> None:
        """Log the status of the database"""
        best_program = self.get_best_program()
        if best_program and best_program.metrics:
            score_str = format_metrics(best_program.metrics)
        else:
            score_str = "N/A"
        logger.info(
            f"Database has {len(self.programs)} programs, best program score is {score_str}"
        )
````

## → Calls
- [[IO-Program.metrics]]
- [[IO-ProgramDatabase.get_best_program]]
- [[IO-ProgramDatabase.load]]
- [[IO-metrics.format_metrics]]

## ← Called by
- [[IO-DiscoveryController._process_iteration_result]]
- [[IO-ProgramDatabase.load]]
- [[IO-Runner.run]]
