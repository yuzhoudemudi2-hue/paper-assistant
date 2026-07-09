"""Tests for the Phase 1 application entry point."""

from main import run


def test_run_initializes_application() -> None:
    """Verify the application entry point starts without pipeline execution."""

    assert run() == 0
