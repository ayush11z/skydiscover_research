---
name: IO-EvolvedProgramDatabase.sample
description: method in skydiscover/search/evox/database/initial_search_strategy.py (evox)
metadata:
  type: project
---

# EvolvedProgramDatabase.sample

**File:** `skydiscover/search/evox/database/initial_search_strategy.py:67`  
**Kind:** method  
**Layer:** #evox

## Source
````python
    def sample(
        self, num_context_programs: Optional[int] = 4, **kwargs
    ) -> Tuple[Dict[str, EvolvedProgram], Dict[str, List[EvolvedProgram]]]:
        """Select parent and context, injecting a label when the search needs guidance.

        Label logic:
          stagnant >= 4 AND best < 0.35  → DIVERGE  (stuck at low score, need new ideas)
          stagnant >= 3 AND best >= 0.35 → REFINE   (promising area, polish it)
          otherwise                       → ""       (making progress, no label needed)
        """
        candidates = list(self.programs.values())
        if not candidates:
            raise ValueError("No candidates available for sampling")

        current_best = self._last_best or 0.0

        # Choose label based on stagnation state
        if self._stagnant_count >= 4 and current_best < 0.35:
            label = self.DIVERGE_LABEL   # tell LLM to try something fundamentally different
        elif self._stagnant_count >= 3 and current_best >= 0.35:
            label = self.REFINE_LABEL    # tell LLM to polish the current best approach
        else:
            label = ""                   # no label — let parent/context selection do the work

        # Pick parent: best program when refining, random otherwise to avoid fixation
        if label == self.REFINE_LABEL:
            scored = [p for p in candidates
                      if isinstance(p.metrics.get("combined_score"), (int, float))]
            parent = max(scored, key=lambda p: p.metrics["combined_score"]) if scored else random.choice(candidates)
        else:
            parent = random.choice(candidates)

        # Context: pick diverse programs excluding the parent
        sample_size = min(num_context_programs + 1, len(candidates))
        examples = random.sample(candidates, sample_size)
        examples = [p for p in examples if p.id != parent.id][:num_context_programs]

        parent_dict = {label: parent}
        context_programs_dict = {"": examples}

        return parent_dict, context_programs_dict
````

## → Calls
- [[IO-Program.id]]
- [[IO-Program.metrics]]
- [[IO-ProgramDatabase.DIVERGE_LABEL]]
- [[IO-ProgramDatabase.REFINE_LABEL]]
- [[IO-ProgramDatabase.load]]
- [[IO-ProgramDatabase.sample]]
- [[IO-base_database.ProgramDatabase]]
- [[IO-initial_search_strategy.EvolvedProgram]]

## ← Called by
_(entry point — nothing in this graph calls it)_
