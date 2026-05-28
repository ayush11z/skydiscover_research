---
name: UnifiedArchive.sample_parent
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive.sample_parent

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:630`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def sample_parent(self, mode: str = "balanced") -> Optional[Program]:
        """
        Sample a parent program for mutation.

        Args:
            mode: Sampling mode
                - "exploitation": Sample from top programs by fitness
                - "exploration": Sample proportional to novelty
                - "balanced": Mix of both

        Returns:
            Selected parent program, or None if archive empty
        """
        if not self._programs:
            return None

        self._ensure_cache_valid()
        programs = list(self._programs.values())

        if mode == "exploitation":
            # Sample from top programs by fitness
            top_progs = self.get_top_programs()
            if top_progs:
                return random.choice(top_progs)
            return random.choice(programs)

        elif mode == "exploration":
            # Sample proportional to novelty
            novelties = [max(self._novelty_scores.get(p.id, 0.0), 0.001) for p in programs]
            total = sum(novelties)
            if total <= 0:
                return random.choice(programs)

            r = random.random() * total
            cumsum = 0.0
            for p, n in zip(programs, novelties):
                cumsum += n
                if cumsum >= r:
                    return p
            return programs[-1]

        else:  # balanced
            if random.random() < 0.5:
                return self.sample_parent("exploitation")
            else:
                return self.sample_parent("exploration")
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.__init__]]
- [[UnifiedArchive._ensure_cache_valid]]
- [[UnifiedArchive.get]]
- [[UnifiedArchive.get_top_programs]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
