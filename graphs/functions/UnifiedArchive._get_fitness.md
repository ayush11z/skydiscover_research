---
name: UnifiedArchive._get_fitness
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive._get_fitness

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:534`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _get_fitness(self, program: Program) -> float:
        """Get primary fitness value from metrics."""
        metrics = program.metrics

        # Use configured fitness key if specified
        if self.config.fitness_key is not None:
            key = self.config.fitness_key
            normalized = self._normalize_metric_value(key, metrics.get(key))
            if normalized is not None:
                return normalized
            # Configured key not found - log warning and fallback
            logger.debug(
                f"Configured fitness_key '{key}' not found in metrics, "
                f"falling back to auto-detection"
            )

        # Prefer combined_score as the canonical scalar fallback.
        normalized = self._normalize_metric_value("combined_score", metrics.get("combined_score"))
        if normalized is not None:
            return normalized

        # Try common metric names as fallback
        for key in ["score", "fitness", "accuracy", "reward"]:
            normalized = self._normalize_metric_value(key, metrics.get(key))
            if normalized is not None:
                return normalized

        # Use first numeric metric
        for key, val in metrics.items():
            normalized = self._normalize_metric_value(key, val)
            if normalized is not None:
                return normalized

        return 0.0
````

## → Calls
- [[DiscoveryControllerInput.config]]
- [[EvaluationResult.metrics]]
- [[LangFuseTracer.get]]
- [[Program.metrics]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive._normalize_metric_value]]
- [[UnifiedArchive.get]]
- [[base_database.Program]]

## ← Called by
- [[UnifiedArchive._compute_elite_score_for_new]]
- [[UnifiedArchive._ensure_cache_valid]]
- [[UnifiedArchive._get_protected_ids]]
- [[UnifiedArchive.get_best]]
- [[UnifiedArchive.get_top_programs]]
- [[UnifiedArchive.sample_other_context_programs]]
