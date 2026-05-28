---
name: BestOfNDatabase.sample
description: method in skydiscover/search/best_of_n/database.py (best-of-n)
metadata:
  type: project
---

# BestOfNDatabase.sample

**File:** `skydiscover/search/best_of_n/database.py:61`  
**Kind:** method  
**Layer:** #best-of-n

## Source
````python
    def sample(
        self, num_context_programs: Optional[int] = 4, **kwargs
    ) -> Tuple[Program, List[Program]]:
        """
        Sample a parent program and context programs for evolution.

        Reuses the same parent for N iterations, then samples a new parent.
        context programs are sampled fresh each iteration from top programs.

        Args:
            num_context_programs: Number of context programs to sample (defaults to 5)
            **kwargs: Additional keyword arguments

        Returns:
            Tuple of (parent, other_context_programs).
        """
        if not self.programs:
            raise ValueError("Cannot sample: no programs in database")

        # Check if we need to sample a new parent
        if (
            self.current_parent_id is None
            or self.parent_iteration_count >= self.n
            or self.current_parent_id not in self.programs
        ):
            # Sample new parent (best program)
            def safe_score(p):
                score = p.metrics.get("combined_score") if p.metrics else None
                if not isinstance(score, (int, float)):
                    return float("-inf")
                return float(score)

            parent = max(self.programs.values(), key=safe_score)
            self.current_parent_id = parent.id
            self.parent_iteration_count = 0

            logger.info(
                f"Best-of-N: sampled new parent {parent.id} (score={safe_score(parent):.4f})"
            )
        else:
            # Reuse current parent
            parent = self.programs[self.current_parent_id]
            logger.debug(
                f"Best-of-N: reusing parent {parent.id} (count={self.parent_iteration_count}/{self.n})"
            )

        # Sample context from top programs (excluding parent)
        # Get more top programs than needed to ensure we have enough after excluding parent
        top_pool_size = max(num_context_programs * 2, 10)
        top_programs = self.get_top_programs(top_pool_size)

        # Filter out parent and sample
        candidates = [p for p in top_programs if p.id != parent.id]
        num_to_sample = min(num_context_programs, len(candidates))

        if num_to_sample > 0:
            other_context_programs = random.sample(candidates, num_to_sample)
        else:
            # Fallback: use all available programs except parent
            all_candidates = [p for p in self.programs.values() if p.id != parent.id]
            other_context_programs = (
                random.sample(all_candidates, min(num_context_programs, len(all_candidates)))
                if all_candidates
                else []
            )

        return parent, other_context_programs
````

## → Calls
- [[BestOfNDatabase.sample.safe_score]]
- [[CheckpointManager.load]]
- [[Program.id]]
- [[ProgramDatabase.get_top_programs]]
- [[ProgramDatabase.sample]]
- [[UnifiedArchive.get_top_programs]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
