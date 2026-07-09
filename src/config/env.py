"""Environment file loading helpers."""

from pathlib import Path


def load_environment_file(path: Path | str = Path(".env")) -> None:
    """Load local environment variables when a .env file exists.

    Args:
        path: Environment file path.
    """

    env_path = Path(path)
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        stripped_line = line.strip()
        if not stripped_line or stripped_line.startswith("#") or "=" not in stripped_line:
            continue
        key, value = stripped_line.split("=", 1)
        _set_default_environment_variable(key.strip(), value.strip())


def _set_default_environment_variable(key: str, value: str) -> None:
    """Set an environment variable if the host has not already provided it."""

    import os

    os.environ.setdefault(key, value)
