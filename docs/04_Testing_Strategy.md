# 04 Testing Strategy

## Paper Assistant Testing Strategy

Version: v1.0

---

# 1. Purpose

This document defines the testing strategy for the Paper Assistant project.

Every module developed by Codex must be verified through automated testing before being considered complete.

Testing should ensure:

- Correctness
- Reliability
- Stability
- Maintainability
- Extensibility

Testing is mandatory.

No feature should be considered complete without passing all required tests.

---

# 2. Testing Principles

The project follows the following testing philosophy:

1. Test early.
2. Test automatically.
3. Test every module independently.
4. Test complete workflows.
5. Test failure scenarios.
6. Prevent regression.

All new features should include corresponding tests.

---

# 3. Testing Levels

The project contains four testing levels.

```
Unit Test

↓

Integration Test

↓

End-to-End Test

↓

Regression Test
```

Every feature should pass all applicable levels.

---

# 4. Test Directory Structure

Suggested structure:

```
tests/

    unit/

        test_crawler.py

        test_inspire.py

        test_filter.py

        test_translation.py

        test_summary.py

        test_report.py

        test_email.py

        test_scheduler.py

    integration/

        test_pipeline.py

        test_email_pipeline.py

    e2e/

        test_daily_workflow.py
```

---

# 5. Unit Testing

Each module must have independent unit tests.

Modules include:

- arXiv crawler
- INSPIRE search
- Filtering engine
- Translation module
- LLM summary module
- Report generator
- Email sender
- Scheduler
- Configuration loader

Each public function should have at least one test.

---

# 6. arXiv Module Testing

Verify:

- Successfully connects to arXiv.
- Correctly parses recent submissions.
- Correctly extracts:
  - Title
  - Authors
  - Abstract
  - Categories
  - PDF URL
  - arXiv ID
- Handles empty result pages.
- Handles connection failures.
- Handles malformed HTML.

---

# 7. INSPIRE Module Testing

Verify:

- Search by author name.
- Retrieve:
  - Total citations
  - Highest cited paper
  - Highest citation count
  - H-index
- Handle authors with identical names.
- Handle authors not found.
- Handle API timeout.
- Handle rate limiting.
- Verify cache behavior.

---

# 8. Paper Filtering Testing

Verify Rule A:

```
Any author total citations >= 5000
```

Verify Rule B:

```
Any author highest cited paper >= 500 citations
```

Verify Rule C:

```
Hot topic score exceeds configured threshold
```

Additional tests:

- Borderline values
- Multiple authors
- Missing citation data
- Empty paper list

---

# 9. Translation Testing

Verify:

- English title translated correctly.
- Abstract translated correctly.
- Mathematical formulas remain unchanged.
- LaTeX expressions remain unchanged.
- Greek letters remain unchanged.
- References remain unchanged.
- Author names are not translated.
- arXiv identifiers remain unchanged.

---

# 10. LLM Summary Testing

Verify generated summaries contain:

- Research background
- Research objective
- Methodology
- Logical flow
- Main conclusions
- Innovation
- Future work

Verify:

- Chinese output only.
- Length does not exceed configured limit.
- Empty abstract handled correctly.
- API failure handled gracefully.

---

# 11. Report Generator Testing

Verify generated reports include:

- Daily overview
- Important papers
- Important authors
- Hot topic papers
- Translation section
- LLM summary
- Statistics

Verify export formats:

- Markdown
- HTML
- PDF

Verify:

- Red highlighted boxes appear correctly.
- Unicode characters display correctly.
- Mathematical formulas display correctly.

---

# 12. Email Module Testing

Verify:

- Single recipient.
- Multiple recipients.
- HTML email generation.
- Attachment generation.
- PDF attachment.
- Markdown attachment.
- Retry after failure.
- Authentication failure.
- SMTP timeout.
- Invalid email address.

---

# 13. Scheduler Testing

Verify:

- Runs exactly once every day.
- Uses Asia/Shanghai timezone.
- Does not execute twice.
- Manual execution works.
- Missed execution recovery.
- Execution history recorded correctly.

---

# 14. Configuration Testing

Verify configuration loading.

Test:

- Missing configuration file.
- Invalid YAML.
- Invalid threshold values.
- Missing environment variables.
- Invalid email settings.
- Invalid API keys.

---

# 15. Integration Testing

Verify the complete workflow.

Pipeline:

```
arXiv

↓

INSPIRE

↓

Filtering

↓

Translation

↓

LLM Summary

↓

Report Generation

↓

Email Sending
```

Verify that every stage passes data correctly to the next stage.

---

# 16. End-to-End Testing

Simulate an actual daily execution.

Scenario:

1. Detect new papers.
2. Query INSPIRE.
3. Filter papers.
4. Translate papers.
5. Generate summaries.
6. Generate report.
7. Send email.
8. Record logs.

The entire workflow must complete successfully.

---

# 17. Failure Recovery Testing

Simulate failures:

- Internet disconnected.
- arXiv unavailable.
- INSPIRE unavailable.
- Translation API unavailable.
- LLM unavailable.
- SMTP unavailable.
- Disk full.
- Permission denied.

Verify:

- Program does not crash.
- Error is logged.
- Retry is performed.
- Remaining workflow continues whenever possible.

---

# 18. Performance Testing

Measure:

- Total execution time.
- Average INSPIRE query time.
- Translation speed.
- Report generation time.
- Email sending time.

Target:

- Daily workflow completes within 10 minutes.
- Support processing at least 200 papers.
- Support querying hundreds of authors efficiently.

---

# 19. Mock Testing

External services should be mocked during testing.

Mock:

- arXiv
- INSPIRE
- Translation API
- LLM API
- SMTP Server

Tests should not depend on external network availability.

---

# 20. Logging Verification

Verify logs include:

- Start time
- End time
- Number of papers
- Number of important papers
- Processing duration
- Error messages
- Retry information

Sensitive information must never appear in logs.

---

# 21. Code Coverage

Minimum coverage requirements:

```
Overall coverage >= 90%
```

Critical modules should achieve:

```
100%
```

Critical modules include:

- Filtering engine
- Scheduler
- Email sender
- Configuration loader

---

# 22. Continuous Testing

Codex should run tests:

- Before every commit.
- After major refactoring.
- After adding new features.
- Before every release.

Tests must pass before code is considered complete.

---

# 23. Acceptance Checklist

A version is accepted only if all items below are satisfied.

- arXiv crawler passes all tests.
- INSPIRE module passes all tests.
- Filtering engine passes all tests.
- Translation module passes all tests.
- LLM summary passes all tests.
- Report generator passes all tests.
- Email sender passes all tests.
- Scheduler passes all tests.
- Integration tests pass.
- End-to-end workflow passes.
- Regression tests pass.
- Coverage requirement is satisfied.
- No critical bugs remain.

---

# 24. Development Rules for Codex

Before marking any task as complete, Codex must:

1. Implement the feature.
2. Write corresponding unit tests.
3. Run all unit tests.
4. Run integration tests.
5. Verify no regression is introduced.
6. Ensure code coverage meets project requirements.
7. Fix all detected issues.
8. Update documentation if necessary.
9. Only then consider the task completed.

Testing is an essential part of development and must never be skipped.

---