---
name: IN-TemplateManager.__init__
description: method in skydiscover/context_builder/utils.py (context-builder)
metadata:
  type: project
---

# TemplateManager.__init__

**File:** `skydiscover/context_builder/utils.py:14`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def __init__(self, *directories: Optional[str]):
        """
        Initializes the TemplateManager with the given directories.
        If there are multiple directories, the templates from the later directories will override
        the templates from the earlier directories.
        """
        self.templates: dict[str, str] = {}
        for d in directories:
            if d:
                path = Path(d)
                if path.exists():
                    self._load_from_directory(path)
````

## → Calls
- [[IN-TemplateManager._load_from_directory]]

## ← Called by
- [[IN-EvoxContextBuilder.__init__]]
