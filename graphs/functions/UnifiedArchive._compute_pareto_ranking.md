---
name: UnifiedArchive._compute_pareto_ranking
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive._compute_pareto_ranking

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:420`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _compute_pareto_ranking(self, programs: List[Program]) -> None:
        """
        NSGA-II non-dominated sorting + crowding distance on explicit objectives.

        Only runs when self.config.pareto_objectives is non-empty.
        Populates self._pareto_ranks (layer number) and self._crowding_distances.
        """
        objectives = self.config.pareto_objectives
        if not objectives:
            self._pareto_ranks = {}
            self._crowding_distances = {}
            return

        higher_is_better = self.config.higher_is_better

        # Build objective vectors (internally: higher is always better)
        obj_vectors: Dict[str, List[float]] = {}
        for p in programs:
            vec = []
            for obj_key in objectives:
                raw_val = p.metrics.get(obj_key, 0.0)
                if not isinstance(raw_val, (int, float)):
                    raw_val = 0.0
                if not higher_is_better.get(obj_key, True):
                    raw_val = -raw_val
                vec.append(float(raw_val))
            obj_vectors[p.id] = vec

        # Non-dominated sorting into layers
        remaining = set(p.id for p in programs)
        rank = 0
        pareto_ranks: Dict[str, int] = {}
        layers: List[List[str]] = []

        while remaining:
            front = []
            for pid_a in remaining:
                dominated = False
                for pid_b in remaining:
                    if pid_a == pid_b:
                        continue
                    if self._dominates(obj_vectors[pid_b], obj_vectors[pid_a]):
                        dominated = True
                        break
                if not dominated:
                    front.append(pid_a)

            for pid in front:
                pareto_ranks[pid] = rank
                remaining.discard(pid)
            layers.append(front)
            rank += 1

        self._pareto_ranks = pareto_ranks

        # Crowding distance within each layer
        num_objectives = len(objectives)
        crowding: Dict[str, float] = {pid: 0.0 for pid in pareto_ranks}

        for layer in layers:
            if len(layer) <= 2:
                for pid in layer:
                    crowding[pid] = float("inf")
                continue

            for m in range(num_objectives):
                sorted_layer = sorted(layer, key=lambda pid: obj_vectors[pid][m])
                crowding[sorted_layer[0]] = float("inf")
                crowding[sorted_layer[-1]] = float("inf")

                obj_range = obj_vectors[sorted_layer[-1]][m] - obj_vectors[sorted_layer[0]][m]
                if obj_range < 1e-10:
                    continue

                for i in range(1, len(sorted_layer) - 1):
                    crowding[sorted_layer[i]] += (
                        obj_vectors[sorted_layer[i + 1]][m] - obj_vectors[sorted_layer[i - 1]][m]
                    ) / obj_range

        self._crowding_distances = crowding
````

## → Calls
- [[DiscoveryControllerInput.config]]
- [[EvaluationResult.metrics]]
- [[LangFuseTracer.get]]
- [[Program.id]]
- [[Program.metrics]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive._dominates]]
- [[UnifiedArchive.get]]
- [[base_database.Program]]

## ← Called by
- [[UnifiedArchive._ensure_cache_valid]]
