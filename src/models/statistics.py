"""Execution statistics models for Paper Assistant reports."""

from pydantic import BaseModel, ConfigDict, Field


class Statistics(BaseModel):
    """Represent daily processing statistics.

    Attributes:
        total_papers: Number of papers retrieved.
        important_papers: Number of papers selected as important.
        hot_papers: Number of hot topic papers.
        translated_papers: Number of translated papers.
        processing_time: Execution duration in seconds.
    """

    model_config = ConfigDict(frozen=True)

    total_papers: int = Field(default=0, ge=0)
    important_papers: int = Field(default=0, ge=0)
    hot_papers: int = Field(default=0, ge=0)
    translated_papers: int = Field(default=0, ge=0)
    processing_time: float = Field(default=0.0, ge=0.0)
