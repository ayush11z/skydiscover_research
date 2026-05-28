---
name: IN-Program.from_dict
description: classmethod in skydiscover/search/base_database.py (database)
metadata:
  type: project
---

# Program.from_dict

**File:** `skydiscover/search/base_database.py:59`  
**Kind:** classmethod  
**Layer:** #database

## Source
````python
    def from_dict(cls, data: Dict[str, Any]) -> Program:
        """Create from dictionary representation"""
        # Get the valid field names for the Program dataclass
        valid_fields = {f.name for f in fields(cls)}

        # Filter the data to only include valid fields
        filtered_data = {k: v for k, v in data.items() if k in valid_fields}

        # Log if we're filtering out any fields
        if len(filtered_data) != len(data):
            filtered_out = set(data.keys()) - set(filtered_data.keys())
            logger.debug(f"Filtered out unsupported fields when loading Program: {filtered_out}")

        return cls(**filtered_data)
````

## → Calls
- [[IN-ProgramDatabase.__init__]]

## ← Called by
_(entry point — nothing in this graph calls it)_
