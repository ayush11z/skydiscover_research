---
name: diversity.create_diversity_strategy
description: function in skydiscover/search/adaevolve/archive/diversity.py (adaevolve)
metadata:
  type: project
---

# diversity.create_diversity_strategy

**File:** `skydiscover/search/adaevolve/archive/diversity.py:348`  
**Kind:** function  
**Layer:** #adaevolve

## Source
````python
def create_diversity_strategy(strategy_type: str = "code", **kwargs) -> DiversityStrategy:
    """
    Factory function to create diversity strategies.

    Args:
        strategy_type: One of "code", "metric", "hybrid"
        **kwargs: Strategy-specific arguments

    Returns:
        Configured DiversityStrategy instance
    """
    if strategy_type == "code":
        return CodeDiversity(
            token_weight=kwargs.get("token_weight", 0.5),
            structure_weight=kwargs.get("structure_weight", 0.3),
            length_weight=kwargs.get("length_weight", 0.2),
        )

    elif strategy_type == "text":
        # For natural language (prompts): token Jaccard + length, no code structure
        return CodeDiversity(
            token_weight=kwargs.get("token_weight", 0.7),
            structure_weight=0.0,
            length_weight=kwargs.get("length_weight", 0.3),
        )

    elif strategy_type == "metric":
        return MetricDiversity(
            higher_is_better=kwargs.get("higher_is_better"),
        )

    elif strategy_type == "hybrid":
        # Default: 50% code, 50% metric
        code_weight = kwargs.get("code_weight", 0.5)
        metric_weight = kwargs.get("metric_weight", 0.5)
        return HybridDiversity(
            [
                (CodeDiversity(), code_weight),
                (MetricDiversity(kwargs.get("higher_is_better")), metric_weight),
            ]
        )

    else:
        raise ValueError(f"Unknown strategy type: {strategy_type}")
````

## → Calls
- [[CodeDiversity.__init__]]
- [[HybridDiversity.__init__]]
- [[MetricDiversity.__init__]]
- [[diversity.CodeDiversity]]
- [[diversity.DiversityStrategy]]
- [[diversity.HybridDiversity]]
- [[diversity.MetricDiversity]]

## ← Called by
- [[AdaEvolveDatabase._expand_to_island_count]]
- [[AdaEvolveDatabase._init_archives]]
- [[AdaEvolveDatabase._spawn_island]]
