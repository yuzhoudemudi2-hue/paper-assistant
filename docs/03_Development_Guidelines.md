# 03 Development Guidelines

## Paper Assistant Development Guidelines

Version: v1.0

---

# 1. Goal

This document defines the implementation rules for the entire project.

Every feature implemented by Codex must follow these development principles.

Priority:

1. Correctness
2. Reliability
3. Maintainability
4. Performance

Never sacrifice correctness for speed.

---

# 2. General Principles

- The whole project must be written in Python.
- Recommended Python version: **Python 3.12+**
- Follow a layered architecture.

```
UI
│
├── Application Layer
│
├── Service Layer
│
├── Data Layer
│
└── Utilities
```

Rules:

- Business logic must never be placed inside the UI.
- Each layer should be independent.
- Modules should have single responsibilities.
- Avoid tight coupling.

---

# 3. Code Style

The entire project should follow PEP8.

Requirements:

- Maximum line length: 100 characters.
- Every function must contain:
  - Docstring
  - Type hints
- Every class must include documentation.
- Avoid global variables.
- Avoid duplicated code.
- Prefer small functions over long functions.
- Prefer composition over inheritance.

Example:

```python
def search_author(name: str) -> AuthorInfo:
    """
    Search author information from INSPIRE.
    """
```

---

# 4. Project Folder Responsibilities

## config/

Only configuration files.

Examples:

```
settings.py
email.yaml
prompt.yaml
```

Never place business logic here.

---

## src/

Contains all implementation code.

Suggested modules:

```
src/
    crawler/
    inspire/
    ranking/
    analyzer/
    translator/
    email/
    scheduler/
    report/
    cache/
    utils/
```

---

## reports/

Generated reports only.

Examples:

```
2026-07-05.md
2026-07-05.html
2026-07-05.pdf
```

---

## logs/

Contains only log files.

Use Python logging.

Never print debugging information.

---

## tests/

Contains all unit tests and integration tests.

Every core module should have corresponding tests.

---

# 5. Logging Rules

Use the standard logging module.

Every important operation should be logged.

Example:

```
Checking arXiv...

Found 18 new papers.

Searching INSPIRE...

Translation completed.

Generating report...

Sending email...

Finished.
```

Supported log levels:

- INFO
- WARNING
- ERROR

Unexpected exceptions must include stack traces.

---

# 6. Error Handling

The program must never crash because of:

- Network timeout
- API timeout
- Website unavailable
- Missing author information
- Translation failure
- Email failure

Every network request must support:

- Timeout
- Retry
- Graceful failure

Recommended retry count:

```
3
```

---

# 7. Network Access Rules

Preferred libraries:

- requests
- httpx

Every request should include:

- User-Agent
- Timeout
- Retry
- Sleep interval

Avoid excessive requests to external websites.

---

# 8. arXiv Module

Responsibilities:

- Visit arXiv daily.
- Monitor:
  - gr-qc
  - hep-th
- Parse the recent submissions.

Return:

- Title
- Authors
- Abstract
- Categories
- arXiv ID
- PDF URL
- Submission date

No filtering logic should exist in this module.

---

# 9. INSPIRE Module

Input:

```
Author Name
```

Output:

- Total citations
- Number of papers
- Highest cited paper
- Highest citation count
- H-index
- INSPIRE profile URL

Support local cache to avoid repeated queries.

---

# 10. Paper Filtering Module

Filtering rules must be configurable.

Current rules:

## Rule A

Any author satisfies:

```
Total citations >= 5000
```

---

## Rule B

Any author satisfies:

```
Highest cited paper >= 500 citations
```

---

## Rule C

Hot topic score exceeds configurable threshold.

Filtering logic must remain independent from data collection.

Future rules should be easy to add.

---

# 11. Hot Topic Analyzer

Support two modes.

## Mode 1

Keyword based.

Example keywords:

- Quantum Gravity
- Black Hole
- AdS/CFT
- String Theory
- Cosmology
- Dark Matter
- Machine Learning

---

## Mode 2

LLM based.

Use an online LLM to determine:

- Whether the paper belongs to current research hotspots.
- Hot score.
- Keywords.
- Reason.

Output:

- Hot score
- Keywords
- Explanation

---

# 12. Translation Module

Translate:

- Title
- Abstract

Requirements:

Preserve:

- Mathematical formulas
- LaTeX
- Greek letters
- Equation numbers
- References

Do not translate:

- Author names
- Institution names
- Journal names
- arXiv identifiers

Output format:

```
English

↓

Chinese
```

---

# 13. LLM Summary Module

For important papers generate:

- Research background
- Research objective
- Main methodology
- Logical flow
- Main conclusions
- Innovation
- Future work

Language:

Chinese only.

Maximum length:

800 words.

Support interchangeable providers:

- OpenAI
- Claude
- Gemini
- DeepSeek

---

# 14. Report Generator

Generate:

- Markdown

Then automatically export:

- HTML
- PDF

Report sections:

1. Daily Overview
2. Important Authors
3. Important Papers
4. Hot Topic Papers
5. Translation
6. LLM Summary
7. Statistics

Important papers should be highlighted using red borders.

---

# 15. Email Module

Support:

- Single recipient
- Multiple recipients

Email format:

HTML

Optional attachments:

- PDF
- Markdown

Retry automatically when sending fails.

---

# 16. Scheduler

Automatically execute every day.

Execution time:

```
12:00 (Beijing Time)
```

Requirements:

- Never execute twice.
- Support manual execution.
- Record execution history.

---

# 17. Configuration

All thresholds must be configurable.

Example:

```yaml
citation_threshold: 5000
paper_threshold: 500
hot_score_threshold: 0.75
timezone: Asia/Shanghai

email:
  retry: 3
```

No magic numbers inside source code.

---

# 18. Security

Never hardcode:

- Passwords
- API Keys
- Email credentials

Store sensitive information in:

```
.env
```

Sensitive information must never appear in logs.

---

# 19. Performance

Use asynchronous requests whenever possible.

Recommended libraries:

- asyncio
- httpx

Maximum concurrent requests:

```
10
```

Cache INSPIRE queries whenever possible.

Avoid duplicate requests.

---

# 20. Extensibility

Future versions should easily support:

Additional arXiv categories:

- hep-ph
- hep-lat
- astro-ph

Additional languages:

- Japanese
- German
- French

Additional report outputs:

- Notion
- WeChat
- Feishu
- Slack

---

# 21. Development Workflow

For every implementation task, Codex must follow these steps:

1. Read the related requirements in `01_Project_Requirements.md`.
2. Read the architecture in `02_System_Architecture.md`.
3. Implement only one module at a time.
4. Keep module interfaces stable.
5. Write unit tests before considering the task complete.
6. Run formatting and linting.
7. Update documentation if APIs change.
8. Never modify unrelated modules.
9. Commit only after all tests pass.

---

# 22. Acceptance Criteria

The implementation is complete only if all of the following are satisfied:

- Detect new papers from gr-qc and hep-th automatically.
- Query INSPIRE author statistics successfully.
- Correctly apply all configurable filtering rules.
- Translate titles and abstracts into Simplified Chinese.
- Generate LLM summaries for important papers.
- Produce Markdown, HTML and PDF reports.
- Send scheduled emails successfully.
- Support multiple recipients.
- Include complete logging and exception handling.
- Pass all unit tests.
- Support future extensions without major refactoring.

---