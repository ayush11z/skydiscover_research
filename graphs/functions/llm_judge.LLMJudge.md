---
name: llm_judge.LLMJudge
description: class in skydiscover/evaluation/llm_judge.py (evaluation)
metadata:
  type: project
---

# llm_judge.LLMJudge

**File:** `skydiscover/evaluation/llm_judge.py:19`  
**Kind:** class  
**Layer:** #evaluation

## Source
````python
class LLMJudge:
    """
    Scores programs via LLM feedback.

    Override _parse_response() to change how LLM output is interpreted.
    """

````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[DiscoveryController.__init__]]
- [[Evaluator.__init__]]
- [[evaluation.create_evaluator]]
