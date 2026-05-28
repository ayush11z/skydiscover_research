---
name: defaults.apply_defaults
description: function in skydiscover/extras/external/defaults/__init__.py (external)
metadata:
  type: project
---

# defaults.apply_defaults

**File:** `skydiscover/extras/external/defaults/__init__.py:19`  
**Kind:** function  
**Layer:** #external

## Source
````python
def apply_defaults(obj, defaults: dict):
    """Recursively apply dict values to a dataclass-like object.

    Only sets attributes that already exist on the object.
    For nested dicts whose corresponding attribute is also an object,
    recurses into the sub-object.
    """
    for key, value in defaults.items():
        if not hasattr(obj, key):
            continue
        if isinstance(value, dict):
            sub = getattr(obj, key)
            if hasattr(sub, "__dict__"):
                apply_defaults(sub, value)
            else:
                setattr(obj, key, value)
        else:
            setattr(obj, key, value)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[openevolve_backend._map_config]]
