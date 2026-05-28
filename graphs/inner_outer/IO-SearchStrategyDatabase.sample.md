---
name: IO-SearchStrategyDatabase.sample
description: method in skydiscover/search/evox/database/search_strategy_db.py (evox)
metadata:
  type: project
---

# SearchStrategyDatabase.sample

**File:** `skydiscover/search/evox/database/search_strategy_db.py:38`  
**Kind:** method  
**Layer:** #evox

## Source
````python
    def sample(
        self, num_context_programs: Optional[int] = 4, **kwargs
    ) -> Tuple[Dict[str, SearchStrategy], Dict[str, List[SearchStrategy]]]:
        """
        Sample a search strategy to refine and other context strategies for evolution.
        """

        def safe_score(p):
            score = p.metrics.get("combined_score") if p.metrics else None
            if not isinstance(score, (int, float)):
                logger.warning(
                    f"Program {p.id} has invalid combined_score: {score}, metrics: {p.metrics}"
                )
            return float(score) if isinstance(score, (int, float)) else float("-inf")

        parent = max(self.programs.values(), key=safe_score)
        available_programs = list(self.programs.values())
        num_to_sample = max(0, min(num_context_programs, len(available_programs)))

        other_context_programs = (
            random.sample(available_programs, num_to_sample) if num_to_sample > 0 else []
        )
        other_context_programs = [p for p in other_context_programs if p.id != parent.id]
        return {"": parent}, {"": other_context_programs}
````

## → Calls
- [[IO-Program.id]]
- [[IO-ProgramDatabase.load]]
- [[IO-ProgramDatabase.sample]]
- [[IO-base_database.ProgramDatabase]]
- [[IO-sample.safe_score]]
- [[IO-search_strategy_db.SearchStrategy]]

## ← Called by
_(entry point — nothing in this graph calls it)_
