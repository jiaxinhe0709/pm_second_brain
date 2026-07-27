"""Small, dependency-free helper for loading workspace environment variables."""

from __future__ import annotations

import os
from pathlib import Path


def load_workspace_env(start_path: str | Path) -> Path | None:
    """Load the nearest .env file without overwriting existing environment values."""
    current = Path(start_path).resolve()
    if current.is_file():
        current = current.parent

    for directory in (current, *current.parents):
        env_path = directory / ".env"
        if env_path.is_file():
            _load_env_file(env_path)
            return env_path

    return None


def _load_env_file(env_path: Path) -> None:
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()

        if not key:
            continue

        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]

        if not os.environ.get(key):
            os.environ[key] = value
