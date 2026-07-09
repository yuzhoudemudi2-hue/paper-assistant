"""Validated configuration models for Paper Assistant."""

from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field


class ApplicationSettings(BaseModel):
    """Represent top-level application settings."""

    model_config = ConfigDict(frozen=True)

    name: str = "Paper Assistant"
    environment: str = "development"
    timezone: str = "Asia/Shanghai"


class PathSettings(BaseModel):
    """Represent configurable project paths."""

    model_config = ConfigDict(frozen=True)

    cache_dir: Path = Path("cache")
    logs_dir: Path = Path("logs")
    reports_dir: Path = Path("reports")
    prompts_dir: Path = Path("prompts")


class FilterSettings(BaseModel):
    """Represent paper filtering thresholds."""

    model_config = ConfigDict(frozen=True)

    citation_threshold: int = Field(default=5000, ge=0)
    top_paper_threshold: int = Field(default=500, ge=0)
    hot_score_threshold: float = Field(default=0.75, ge=0.0, le=1.0)


class SchedulerSettings(BaseModel):
    """Represent scheduler configuration."""

    model_config = ConfigDict(frozen=True)

    enabled: bool = False
    timezone: str = "Asia/Shanghai"
    run_time: str = "12:00"
    prevent_duplicate_runs: bool = True


class EmailSettings(BaseModel):
    """Represent email delivery configuration."""

    model_config = ConfigDict(frozen=True)

    enabled: bool = False
    smtp_host: str = ""
    smtp_port: int = Field(default=587, ge=1, le=65535)
    use_tls: bool = True
    sender: str = ""
    recipients: list[str] = Field(default_factory=list)
    retry_count: int = Field(default=3, ge=0)


class LlmSettings(BaseModel):
    """Represent LLM provider configuration reserved for future phases."""

    model_config = ConfigDict(frozen=True)

    enabled: bool = False
    provider: str = ""
    model: str = ""
    temperature: float = Field(default=0.0, ge=0.0)
    max_tokens: int = Field(default=0, ge=0)


class ApplicationConfig(BaseModel):
    """Represent the complete validated application configuration."""

    model_config = ConfigDict(frozen=True)

    application: ApplicationSettings = Field(default_factory=ApplicationSettings)
    paths: PathSettings = Field(default_factory=PathSettings)
    filters: FilterSettings = Field(default_factory=FilterSettings)
    scheduler: SchedulerSettings = Field(default_factory=SchedulerSettings)
    email: EmailSettings = Field(default_factory=EmailSettings)
    llm: LlmSettings = Field(default_factory=LlmSettings)
