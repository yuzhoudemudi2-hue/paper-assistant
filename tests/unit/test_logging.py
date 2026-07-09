"""Tests for project logging initialization."""

import logging
from pathlib import Path

from utils.logger import configure_logging, get_logger


def test_configure_logging_creates_file_handler_directory(tmp_path: Path) -> None:
    """Verify logging setup creates parent directories for file handlers."""

    log_file = tmp_path / "logs" / "application.log"
    logging_config = tmp_path / "logging.yaml"
    logging_config.write_text(
        "\n".join(
            [
                "version: 1",
                "disable_existing_loggers: false",
                "formatters:",
                "  standard:",
                '    format: "%(levelname)s | %(name)s | %(message)s"',
                "handlers:",
                "  file:",
                "    class: logging.FileHandler",
                "    formatter: standard",
                "    level: INFO",
                f"    filename: {log_file.as_posix()}",
                "    encoding: utf-8",
                "loggers:",
                "  paper_assistant:",
                "    handlers:",
                "      - file",
                "    level: INFO",
                "    propagate: false",
                "root:",
                "  handlers:",
                "    - file",
                "  level: WARNING",
            ]
        ),
        encoding="utf-8",
    )

    configure_logging(logging_config)
    logger = get_logger("test")
    logger.info("Logging initialized.")
    logging.shutdown()

    assert log_file.exists()
    assert "Logging initialized." in log_file.read_text(encoding="utf-8")
