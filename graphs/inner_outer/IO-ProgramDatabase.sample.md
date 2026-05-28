---
name: IO-ProgramDatabase.sample
description: method in skydiscover/search/base_database.py (database)
metadata:
  type: project
---

# ProgramDatabase.sample

**File:** `skydiscover/search/base_database.py:134`  
**Kind:** method  
**Layer:** #database

## What it does
Selects one parent program and a list of context programs from the current population. The sampling strategy is implementation-defined — the default uses score-weighted sampling; the outer LLM can replace this with a custom `EvolvedProgramDatabase` class that overrides this method.

## Source
````python
    def sample(
        self,
        num_context_programs: Optional[int] = 4,
        **kwargs: Any,
    ) -> Tuple[
        Union[Program, Dict[str, Program]],
        Union[List[Program], Dict[str, List[Program]]],
    ]:
        """Sample a parent program and context programs for discovery.

        Args:
            num_context_programs: Number of context programs to sample.
            **kwargs: Search-specific parameters.

        Returns:
            (parent, context_programs) — each can be plain or dict-wrapped.
            Plain: (Program, [Program, ...])
            Dict-wrapped: ({info: Program}, {info: [Program, ...]})
                where the key is additional information about the program.
        """
        ...
````

## → Calls
- [[IO-base_database.Program]]

## ← Called by
- [[IO-DiscoveryController._run_iteration]]
- [[IO-EvolvedProgramDatabase.sample]]
- [[IO-SearchStrategyDatabase.sample]]
- [[IO-search_strategy_evaluator.evaluate]]
