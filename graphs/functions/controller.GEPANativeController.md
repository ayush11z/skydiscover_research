---
name: controller.GEPANativeController
description: class in skydiscover/search/gepa_native/controller.py (gepa)
metadata:
  type: project
---

# controller.GEPANativeController

**File:** `skydiscover/search/gepa_native/controller.py:39`  
**Kind:** class  
**Layer:** #gepa

## Source
````python
class GEPANativeController(DiscoveryController):
    """
    Discovery controller implementing GEPA's guided evolution.

    Key Features:
    1. Reflective prompting: Structures evaluation failures and evaluator
       diagnostics as actionable feedback in the LLM prompt.
    2. Acceptance gating: Rejects mutations that don't improve on the parent,
       preventing population pollution.
    3. LLM-mediated merge: Combines two complementary programs both
       proactively (after each acceptance) and reactively (on stagnation).
    4. Merge deduplication: Tracks tried pairs to avoid redundant merges.
    5. Merge budget: Caps total merge attempts to bound LLM cost.
    """

````

## → Calls
- [[default_discovery_controller.DiscoveryController]]

## ← Called by
_(entry point — nothing in this graph calls it)_
