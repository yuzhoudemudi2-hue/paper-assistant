"""Application entry point for Paper Assistant Phase 1 initialization."""

from config.loader import ConfigurationError, load_application_config
from utils.logger import LoggingConfigurationError, configure_logging, get_logger


def run() -> int:
    """Initialize the application and exit successfully.

    Phase 1 verifies that configuration loading and logging work. Pipeline
    execution is intentionally reserved for later roadmap phases.

    Returns:
        Process exit code.
    """

    try:
        config = load_application_config()
        configure_logging()
    except (ConfigurationError, LoggingConfigurationError) as exc:
        raise SystemExit(f"Application initialization failed: {exc}") from exc

    logger = get_logger("main")
    logger.info(
        "Application initialized successfully.",
        extra={
            "application": config.application.name,
            "environment": config.application.environment,
        },
    )
    logger.info("Application shutdown complete.")
    return 0


def main() -> int:
    """Console script entry point.

    Returns:
        Process exit code.
    """

    return run()


if __name__ == "__main__":
    raise SystemExit(main())
