"""Project-wide logging utilities."""

from __future__ import annotations

import logging
import logging.config
from pathlib import Path
from typing import Any

from utils.yaml import YamlLoadError, load_yaml_mapping


class LoggingConfigurationError(RuntimeError):
    """Raised when logging configuration cannot be initialized."""


def configure_logging(config_path: Path | str = Path("config/logging.yaml")) -> None:
    """Configure project logging from a YAML file.

    Args:
        config_path: Path to the logging YAML configuration file.

    Raises:
        LoggingConfigurationError: If logging cannot be configured.
    """

    resolved_config_path = Path(config_path)
    if not resolved_config_path.exists():
        raise LoggingConfigurationError(f"Logging configuration is missing: {resolved_config_path}")

    try:
        logging_config = load_yaml_mapping(resolved_config_path)
    except YamlLoadError as exc:
        raise LoggingConfigurationError("Logging configuration contains invalid YAML.") from exc

    _ensure_file_handler_directories(logging_config)
    logging.config.dictConfig(logging_config)


def get_logger(name: str) -> logging.Logger:
    """Return a logger under the project namespace.

    Args:
        name: Module or component name.

    Returns:
        Configured logger instance.
    """

    return logging.getLogger(f"paper_assistant.{name}")


def _ensure_file_handler_directories(logging_config: dict[str, Any]) -> None:
    """Create directories required by configured file handlers."""

    handlers = logging_config.get("handlers", {})
    if not isinstance(handlers, dict):
        return

    for handler in handlers.values():
        if isinstance(handler, dict) and "filename" in handler:
            Path(handler["filename"]).parent.mkdir(parents=True, exist_ok=True)
