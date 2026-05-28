---
name: IO-sample.safe_score
description: function in skydiscover/search/evox/database/search_strategy_db.py (evox)
metadata:
  type: project
---

# sample.safe_score

**File:** `skydiscover/search/evox/database/search_strategy_db.py:45`  
**Kind:** function  
**Layer:** #evox

## Source
````python
        def safe_score(p):
            score = p.metrics.get("combined_score") if p.metrics else None
            if not isinstance(score, (int, float)):
                logger.warning(
                    f"Program {p.id} has invalid combined_score: {score}, metrics: {p.metrics}"
                )
            return float(score) if isinstance(score, (int, float)) else float("-inf")
````

## → Calls
- [[IO-Program.id]]
- [[IO-Program.metrics]]

## ← Called by
- [[IO-SearchStrategyDatabase.sample]]
