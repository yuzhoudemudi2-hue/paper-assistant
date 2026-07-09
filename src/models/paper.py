"""Paper-related shared data models defined by the project API design."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from models.author import Author


class PaperSummary(BaseModel):
    """Represent a structured scientific summary for a paper.

    The fields are intentionally empty by default during Phase 1 because LLM
    summary generation belongs to a later development phase.
    """

    model_config = ConfigDict(frozen=True)

    background: str = ""
    objective: str = ""
    method: str = ""
    logic: str = ""
    results: str = ""
    innovation: str = ""
    future_work: str = ""


class Paper(BaseModel):
    """Represent the central paper object exchanged by project modules.

    Attributes:
        title: Paper title.
        authors: Ordered paper author list.
        abstract: Paper abstract.
        categories: arXiv or provider subject categories.
        arxiv_id: arXiv identifier.
        arxiv_url: arXiv abstract page URL.
        pdf_url: Paper PDF URL.
        submitted_date: Submission timestamp.
        author_statistics: Citation-enriched author records.
        matched_rules: Names of filtering rules matched by the paper.
        priority_score: Configured priority score.
        is_hot: Whether the paper is considered a hot topic.
        hot_score: Hot topic score.
        hot_reason: Explanation for the hot topic decision.
        keywords: Hot topic keywords.
        translated_title: Simplified Chinese title translation.
        translated_abstract: Simplified Chinese abstract translation.
        summary: Structured LLM summary.
        report_section: Rendered report section text.
    """

    model_config = ConfigDict(frozen=True)

    title: str = Field(min_length=1)
    authors: list[Author] = Field(default_factory=list)
    abstract: str = ""
    categories: list[str] = Field(default_factory=list)
    arxiv_id: str = ""
    arxiv_url: str = ""
    pdf_url: str = ""
    submitted_date: datetime
    author_statistics: list[Author] = Field(default_factory=list)
    matched_rules: list[str] = Field(default_factory=list)
    priority_score: float = Field(default=0.0, ge=0.0)
    is_hot: bool = False
    hot_score: float = Field(default=0.0, ge=0.0)
    hot_reason: str = ""
    keywords: list[str] = Field(default_factory=list)
    translated_title: str = ""
    translated_abstract: str = ""
    summary: PaperSummary = Field(default_factory=PaperSummary)
    report_section: str = ""


class FilterResult(BaseModel):
    """Represent the output of the future filtering subsystem."""

    model_config = ConfigDict(frozen=True)

    paper: Paper
    matched_rules: list[str] = Field(default_factory=list)
    priority_score: float = Field(default=0.0, ge=0.0)


class TranslationResult(BaseModel):
    """Represent original and translated paper text."""

    model_config = ConfigDict(frozen=True)

    original_title: str
    translated_title: str
    original_abstract: str
    translated_abstract: str
