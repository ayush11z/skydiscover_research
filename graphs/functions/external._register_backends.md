---
name: external._register_backends
description: function in skydiscover/extras/external/__init__.py (external)
metadata:
  type: project
---

# external._register_backends

**File:** `skydiscover/extras/external/__init__.py:48`  
**Kind:** function  
**Layer:** #external

## Source
````python
def _register_backends():
    """Attempt to register each backend. Missing packages are silently skipped."""
    import importlib
    import logging

    _logger = logging.getLogger(__name__)
    for name, module_path, func_name in _BACKENDS:
        try:
            mod = importlib.import_module(module_path)
            _REGISTRY[name] = getattr(mod, func_name)
        except ImportError:
            pass  # Package not installed — expected
        except Exception as e:
            _logger.warning("Backend '%s' package is installed but failed to register: %s", name, e)
````

## → Calls
- [[external._BACKENDS]]

## ← Called by
_(entry point — nothing in this graph calls it)_
