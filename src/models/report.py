"""Report data models shared by future renderers and delivery modules."""

from datetime import date

from pydantic import BaseModel, ConfigDict, Field

from models.author import Author
from models.paper import Paper, PaperSummary, TranslationResult
from models.statistics import Statistics


class Report(BaseModel):
    """Represent the complete daily report before rendering."""

    model_config = ConfigDict(frozen=True)

    date: date
    statistics: Statistics = Field(default_factory=Statistics)
    important_authors: list[Author] = Field(default_factory=list)
    important_papers: list[Paper] = Field(default_factory=list)
    hot_papers: list[Paper] = Field(default_factory=list)
    translations: list[TranslationResult] = Field(default_factory=list)
    summaries: list[PaperSummary] = Field(default_factory=list)
