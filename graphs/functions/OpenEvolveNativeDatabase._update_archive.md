---
name: OpenEvolveNativeDatabase._update_archive
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._update_archive

**File:** `skydiscover/search/openevolve_native/database.py:620`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _update_archive(self, program: Program) -> None:
        if len(self.archive) < self.archive_size:
            self.archive.add(program.id)
            return

        # Clean stale refs
        valid = []
        for pid in list(self.archive):
            if pid in self.programs:
                valid.append(self.programs[pid])
            else:
                self.archive.discard(pid)

        if len(self.archive) < self.archive_size:
            self.archive.add(program.id)
            return

        # Replace worst if new program is better
        if valid:
            worst = min(
                valid,
                key=lambda p: _get_fitness(p.metrics, self.feature_dimensions),
            )
            if self._is_better(program, worst):
                self.archive.discard(worst.id)
                self.archive.add(program.id)
        else:
            self.archive.add(program.id)
````

## → Calls
- [[CheckpointManager.load]]
- [[EvaluationResult.metrics]]
- [[OpenEvolveNativeDatabase._is_better]]
- [[Program.id]]
- [[Program.metrics]]
- [[base_database.Program]]
- [[database._get_fitness]]

## ← Called by
- [[OpenEvolveNativeDatabase.add]]
