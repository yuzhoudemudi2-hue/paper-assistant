"""Configuration loading utilities for Paper Assistant."""

from pathlib import Path
from typing import Any

from pydantic import ValidationError

from config.env import load_environment_file
from config.models import ApplicationConfig
from utils.yaml import YamlLoadError, load_yaml_mapping

CONFIG_FILENAMES = (
    "settings.yaml",
    "filters.yaml",
    "scheduler.yaml",
    "email.yaml",
    "llm.yaml",
)


class ConfigurationError(RuntimeError):
    """Raised when application configuration cannot be loaded or validated."""


def load_yaml_file(path: Path) -> dict[str, Any]:
    """Load a YAML file as a dictionary.

    Args:
        path: YAML file path.

    Returns:
        Parsed YAML content.

    Raises:
        ConfigurationError: If the file is missing, invalid, or not a mapping.
    """

    if not path.exists():
        raise ConfigurationError(f"Configuration file is missing: {path}")

    try:
        content = load_yaml_mapping(path)
    except YamlLoadError as exc:
        raise ConfigurationError(f"Configuration file is invalid YAML: {path}") from exc

    return content


def merge_configurations(configurations: list[dict[str, Any]]) -> dict[str, Any]:
    """Merge top-level configuration mappings.

    Args:
        configurations: Parsed configuration dictionaries.

    Returns:
        A merged configuration dictionary.
    """

    merged: dict[str, Any] = {}
    for configuration in configurations:
        merged.update(configuration)
    return merged


def load_application_config(config_dir: Path | str = Path("config")) -> ApplicationConfig:
    """Load and validate the application configuration.

    Args:
        config_dir: Directory containing YAML configuration templates.

    Returns:
        Validated application configuration.

    Raises:
        ConfigurationError: If loading or validation fails.
    """

    load_environment_file()
    resolved_config_dir = Path(config_dir)
    configurations = [
        load_yaml_file(resolved_config_dir / filename) for filename in CONFIG_FILENAMES
    ]
    merged_configuration = merge_configurations(configurations)

    try:
        return ApplicationConfig.model_validate(merged_configuration)
    except ValidationError as exc:
        raise ConfigurationError("Application configuration validation failed.") from exc
