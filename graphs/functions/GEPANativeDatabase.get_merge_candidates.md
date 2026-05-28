---
name: GEPANativeDatabase.get_merge_candidates
description: method in skydiscover/search/gepa_native/database.py (gepa)
metadata:
  type: project
---

# GEPANativeDatabase.get_merge_candidates

**File:** `skydiscover/search/gepa_native/database.py:185`  
**Kind:** method  
**Layer:** #gepa

## Source
````python
    def get_merge_candidates(self) -> Tuple[Program, Program]:
        """Select two complementary programs for LLM-mediated merge.

        Selection strategy:
        1. Prefer two programs that each lead on a different metric.
        2. Fallback: best program + random from top 5.
        3. Last resort: best program returned twice (caller should guard).
        """
        if len(self.elite_pool) < 2:
            best = self.get_best_program()
            return best, best

        # Try to find two programs that each lead on a different metric
        leaders: Dict[str, str] = {}
        for metric_name, (pid, _score) in self.metric_best.items():
            if pid in self.programs and pid in self.elite_pool:
                leaders[metric_name] = pid

        unique_leaders = sorted(set(leaders.values()))
        if len(unique_leaders) >= 2:
            pids = self.rng.sample(unique_leaders, 2)
            return self.programs[pids[0]], self.programs[pids[1]]

        # Fallback: best + random from top 5
        best = self.get_best_program()
        top5_ids = [pid for pid in self.elite_pool[:5] if pid != best.id]
        if top5_ids:
            other_id = self.rng.choice(top5_ids)
            return best, self.programs[other_id]

        return best, best
````

## → Calls
- [[CheckpointManager.load]]
- [[GEPANativeDatabase.__init__]]
- [[Program.id]]
- [[ProgramDatabase.get_best_program]]
- [[ProgramDatabase.sample]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
