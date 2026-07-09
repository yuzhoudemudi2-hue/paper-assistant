"""Common operational models used across Paper Assistant modules."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ErrorInfo(BaseModel):
    """Represent a structured module error."""

    model_config = ConfigDict(frozen=True)

    module: str
    error_type: str
    message: str
    timestamp: datetime
    retryable: bool


class LogEntry(BaseModel):
    """Represent a structured log event described by the API design."""

    model_config = ConfigDict(frozen=True)

    timestamp: datetime
    module: str
    operation: str
    status: str
    duration: float
    message: str
