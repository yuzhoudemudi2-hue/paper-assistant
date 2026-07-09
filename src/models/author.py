"""Author data models shared across Paper Assistant modules."""

from pydantic import BaseModel, ConfigDict, Field


class Author(BaseModel):
    """Represent author metadata and optional citation statistics.

    Attributes:
        name: Author name as it should appear in reports.
        total_citations: Total citation count from a citation provider.
        paper_count: Number of known papers from a citation provider.
        highest_cited_paper: Title of the author's highest cited paper.
        highest_citations: Citation count of the highest cited paper.
        h_index: Author h-index from a citation provider.
        inspire_url: Optional INSPIRE profile URL.
    """

    model_config = ConfigDict(frozen=True)

    name: str = Field(min_length=1)
    total_citations: int = Field(default=0, ge=0)
    paper_count: int = Field(default=0, ge=0)
    highest_cited_paper: str = ""
    highest_citations: int = Field(default=0, ge=0)
    h_index: int = Field(default=0, ge=0)
    inspire_url: str = ""
