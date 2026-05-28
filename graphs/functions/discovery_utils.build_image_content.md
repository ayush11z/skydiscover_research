---
name: discovery_utils.build_image_content
description: function in skydiscover/search/utils/discovery_utils.py (search-utils)
metadata:
  type: project
---

# discovery_utils.build_image_content

**File:** `skydiscover/search/utils/discovery_utils.py:121`  
**Kind:** function  
**Layer:** #search-utils

## Source
````python
def build_image_content(text_prompt: str, parent: Program, other_context: dict) -> list:
    """Build multimodal content array with images for VLM (image generation mode).

    Encodes parent and other context images as base64 and interleaves them
    with the text prompt so the VLM can see what the current images look like.
    """
    import base64
    import os

    _MIME = {
        "png": "image/png",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "webp": "image/webp",
        "gif": "image/gif",
    }

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

    content = []

    # Parent image
    parent_img = (getattr(parent, "metadata", {}) or {}).get("image_path")
    img_part = _encode_image(parent_img)
    if img_part:
        score = (parent.metrics or {}).get("combined_score", "?")
        content.append({"type": "text", "text": f"Current best image (score: {score}):"})
        content.append(img_part)

    # Other context images (limit to 3 to keep token cost reasonable)
    img_count = 0
    for progs in other_context.values():
        for prog in progs:
            if img_count >= 3:
                break
            prog_img = (getattr(prog, "metadata", {}) or {}).get("image_path")
            img_part = _encode_image(prog_img)
            if img_part:
                score = (prog.metrics or {}).get("combined_score", "?")
                content.append({"type": "text", "text": f"Other context images (score: {score}):"})
                content.append(img_part)
                img_count += 1

    # Text prompt (with all the formatted context from prompt generator)
    content.append({"type": "text", "text": text_prompt})

    return content
````

## → Calls
- [[EvaluationResult.metrics]]
- [[Program.metrics]]
- [[base_database.Program]]
- [[build_image_content._encode_image]]

## ← Called by
- [[AdaEvolveController._execute_generation]]
- [[DiscoveryController._run_iteration]]
