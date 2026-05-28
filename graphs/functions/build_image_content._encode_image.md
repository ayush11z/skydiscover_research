---
name: build_image_content._encode_image
description: function in skydiscover/search/utils/discovery_utils.py (search-utils)
metadata:
  type: project
---

# build_image_content._encode_image

**File:** `skydiscover/search/utils/discovery_utils.py:138`  
**Kind:** function  
**Layer:** #search-utils

## Source
````python
    def _encode_image(path: str) -> dict | None:
        if not path or not os.path.exists(path):
            return None
        try:
            with open(path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
            ext = os.path.splitext(path)[1].lstrip(".").lower()
            mime = _MIME.get(ext, "image/png")
            return {"type": "image_url", "image_url": {"url": f"data:{mime};base64,{b64}"}}
        except Exception:
            return None
````

## → Calls
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]

## ← Called by
- [[discovery_utils.build_image_content]]
