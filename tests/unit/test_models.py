"""Tests for shared API data models."""

from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from models import Author, Paper, PaperSummary, Report, Statistics, TranslationResult


def test_paper_model_accepts_api_design_fields() -> None:
    """Verify the shared Paper model exposes the documented API fields."""

    author = Author(name="A. Researcher", total_citations=12)
    summary = PaperSummary(background="背景")
    paper = Paper(
        title="A Test Paper",
        authors=[author],
        abstract="A short abstract.",
        categories=["gr-qc"],
        arxiv_id="2607.00001",
        arxiv_url="https://arxiv.org/abs/2607.00001",
        pdf_url="https://arxiv.org/pdf/2607.00001",
        submitted_date=datetime(2026, 7, 8, tzinfo=UTC),
        summary=summary,
    )

    assert paper.authors[0].name == "A. Researcher"
    assert paper.summary.background == "背景"
    assert paper.priority_score == 0.0


def test_author_rejects_negative_statistics() -> None:
    """Verify citation statistics cannot be negative."""

    with pytest.raises(ValidationError):
        Author(name="A. Researcher", total_citations=-1)


def test_report_model_groups_report_sections() -> None:
    """Verify the Report model contains the documented report collections."""

    translation = TranslationResult(
        original_title="Original",
        translated_title="译文",
        original_abstract="Abstract",
        translated_abstract="摘要",
    )
    report = Report(
        date=datetime(2026, 7, 8, tzinfo=UTC).date(),
        statistics=Statistics(total_papers=1),
        translations=[translation],
    )

    assert report.statistics.total_papers == 1
    assert report.translations[0].translated_title == "译文"
