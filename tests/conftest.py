"""Session-scoped fixtures shared across the test suite."""

import json
import os
import urllib.request
import urllib.error

import pytest

OLLAMA_BASE = "http://127.0.0.1:11434/v1"
_OLLAMA_TAGS_URL = "http://127.0.0.1:11434/api/tags"
_DEFAULT_MODEL = "gemma3:12b"


def _is_ollama_running() -> bool:
    try:
        with urllib.request.urlopen(_OLLAMA_TAGS_URL, timeout=3) as resp:
            return resp.status == 200
    except Exception:
        return False


def _is_model_available(model: str) -> bool:
    """Return True if *model* appears in Ollama's local model list."""
    try:
        with urllib.request.urlopen(_OLLAMA_TAGS_URL, timeout=3) as resp:
            data = json.loads(resp.read())
        available = [m["name"] for m in data.get("models", [])]
        # Match on exact name or name without the tag (e.g. "qwen2.5:14b" vs "qwen2.5")
        return any(
            name == model or name.split(":")[0] == model.split(":")[0]
            for name in available
        )
    except Exception:
        return False


@pytest.fixture(scope="session")
def ollama_client():
    """Return an OpenAI client pointed at the local Ollama instance.

    Skips the entire session if Ollama is not reachable or if the model
    requested via SKYDISCOVER_TEST_MODEL is not available locally.
    """
    if not _is_ollama_running():
        pytest.skip(
            "Ollama is not reachable at http://127.0.0.1:11434 — "
            "skipping all integration tests"
        )

    model = os.environ.get("SKYDISCOVER_TEST_MODEL", _DEFAULT_MODEL)
    if not _is_model_available(model):
        pytest.skip(
            f"Model '{model}' is not available in Ollama — "
            f"run `ollama pull {model}` or set SKYDISCOVER_TEST_MODEL to an available model"
        )

    from openai import OpenAI

    return OpenAI(base_url=OLLAMA_BASE, api_key="ollama")
