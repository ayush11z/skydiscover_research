---
name: BestOfNDatabase.sample.safe_score
description: function in skydiscover/search/best_of_n/database.py (best-of-n)
metadata:
  type: project
---

# BestOfNDatabase.sample.safe_score

**File:** `skydiscover/search/best_of_n/database.py:87`  
**Kind:** function  
**Layer:** #best-of-n

## Source
````python
            def safe_score(p):
                score = p.metrics.get("combined_score") if p.metrics else None
                if not isinstance(score, (int, float)):
                    return float("-inf")
                return float(score)
````

## → Calls
- [[EvaluationResult.metrics]]
- [[Program.metrics]]

## ← Called by
- [[BestOfNDatabase.sample]]
