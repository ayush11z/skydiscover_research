---
name: SafeJSONEncoder.default
description: method in skydiscover/search/utils/checkpoint_manager.py (search-utils)
metadata:
  type: project
---

# SafeJSONEncoder.default

**File:** `skydiscover/search/utils/checkpoint_manager.py:26`  
**Kind:** method  
**Layer:** #search-utils

## Source
````python
    def default(self, obj):
        # Convert numpy arrays/scalars to Python types
        try:
            import numpy as np

            if isinstance(obj, np.ndarray):
                return obj.tolist()
            if isinstance(obj, (np.integer,)):
                return int(obj)
            if isinstance(obj, (np.floating,)):
                return float(obj)
            if isinstance(obj, np.bool_):
                return bool(obj)
        except ImportError:
            pass
        # Convert sets to sorted lists for consistency
        if isinstance(obj, set):
            return sorted(list(obj))
        # Convert frozensets to sorted lists
        if isinstance(obj, frozenset):
            return sorted(list(obj))
        # Let the base class raise TypeError for other non-serializable types
        return super().default(obj)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
_(entry point — nothing in this graph calls it)_
