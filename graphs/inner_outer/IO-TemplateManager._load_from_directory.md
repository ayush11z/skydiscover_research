---
name: IO-TemplateManager._load_from_directory
description: method in skydiscover/context_builder/utils.py (context-builder)
metadata:
  type: project
---

# TemplateManager._load_from_directory

**File:** `skydiscover/context_builder/utils.py:27`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _load_from_directory(self, directory: Path) -> None:
        for txt_file in directory.glob("*.txt"):
            with open(txt_file, "r") as f:
                self.templates[txt_file.stem] = f.read()
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-TemplateManager.__init__]]
