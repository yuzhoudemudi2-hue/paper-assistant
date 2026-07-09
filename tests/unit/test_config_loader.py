"""Tests for application configuration loading."""

from pathlib import Path

import pytest

from config.loader import ConfigurationError, load_application_config, load_yaml_file


def test_load_application_config_reads_project_templates() -> None:
    """Verify the committed configuration templates load into typed settings."""

    config = load_application_config()

    assert config.application.name == "Paper Assistant"
    assert config.filters.citation_threshold == 5000
    assert config.scheduler.run_time == "12:00"
    assert config.email.retry_count == 3
    assert config.llm.enabled is False


def test_load_yaml_file_rejects_missing_file(tmp_path: Path) -> None:
    """Verify missing configuration files fail with a project-specific error."""

    missing_file = tmp_path / "missing.yaml"

    with pytest.raises(ConfigurationError):
        load_yaml_file(missing_file)


def test_load_yaml_file_rejects_non_mapping_content(tmp_path: Path) -> None:
    """Verify configuration files must contain mappings."""

    invalid_file = tmp_path / "invalid.yaml"
    invalid_file.write_text("- invalid\n- content\n", encoding="utf-8")

    with pytest.raises(ConfigurationError):
        load_yaml_file(invalid_file)
