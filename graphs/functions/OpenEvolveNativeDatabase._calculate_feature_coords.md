---
name: OpenEvolveNativeDatabase._calculate_feature_coords
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._calculate_feature_coords

**File:** `skydiscover/search/openevolve_native/database.py:461`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _calculate_feature_coords(self, program: Program) -> List[int]:
        coords: List[int] = []
        for dim in self.feature_dimensions:
            # Priority 1: custom metric from evaluator
            if dim in program.metrics:
                coords.append(self._to_bin(dim, program.metrics[dim]))
            # Priority 2: built-in features
            elif dim == "complexity":
                coords.append(self._to_bin("complexity", float(len(program.solution))))
            elif dim == "diversity":
                if len(self.programs) < 2:
                    coords.append(0)
                else:
                    coords.append(self._to_bin("diversity", self._get_cached_diversity(program)))
            elif dim == "score":
                if not program.metrics:
                    coords.append(0)
                else:
                    coords.append(
                        self._to_bin(
                            "score",
                            _get_fitness(program.metrics, self.feature_dimensions),
                        )
                    )
            else:
                raise ValueError(
                    f"Feature dimension '{dim}' not found in program metrics. "
                    f"Available metrics: {list(program.metrics.keys())}. "
                    f"Built-in features: 'complexity', 'diversity', 'score'."
                )
        return coords
````

## → Calls
- [[CheckpointManager.load]]
- [[EvaluationResult.metrics]]
- [[OpenEvolveNativeDatabase._get_cached_diversity]]
- [[OpenEvolveNativeDatabase._to_bin]]
- [[Program.metrics]]
- [[Program.solution]]
- [[base_database.Program]]
- [[database._get_fitness]]

## ← Called by
- [[OpenEvolveNativeDatabase._sample_other_context_programs]]
- [[OpenEvolveNativeDatabase.add]]
