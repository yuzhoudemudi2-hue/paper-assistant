# 06 API Design

## Paper Assistant Module Interface Specification

Version: v1.0

---

# 1. Purpose

This document defines the interfaces and data models shared between all modules.

Every module must follow these interface definitions.

Modules should communicate only through these standardized data structures.

Business logic should never depend on implementation details of other modules.

---

# 2. Data Flow

The complete workflow is:

```
arXiv

↓

Paper Metadata

↓

INSPIRE

↓

Author Statistics

↓

Filtering Engine

↓

Translation

↓

LLM Summary

↓

Report Generator

↓

Email Sender
```

---

# 3. Paper Object

Every paper should be represented using the following structure.

```python
class Paper:
    title: str
    authors: list[Author]
    abstract: str
    categories: list[str]

    arxiv_id: str
    arxiv_url: str
    pdf_url: str
    submitted_date: datetime

    # INSPIRE Information
    author_statistics: list[Author]

    # Filtering
    matched_rules: list[str]
    priority_score: float

    # Hot Topic Analysis
    is_hot: bool
    hot_score: float
    hot_reason: str
    keywords: list[str]

    # Translation
    translated_title: str
    translated_abstract: str

    # LLM Summary
    summary: PaperSummary

    # Report
    report_section: str
```

---

# 4. Author Object

```python
class Author:
    name: str

    total_citations: int
    paper_count: int

    highest_cited_paper: str
    highest_citations: int

    h_index: int

    inspire_url: str
```

---

# 5. Filter Result

```python
FilterResult

paper: Paper

matched_rules: list[str]

priority_score: float
```

Example:

```
matched_rules

Rule A

Rule C
```

---

# 6. Translation Result

```python
TranslationResult

original_title

translated_title

original_abstract

translated_abstract
```

---

# 7. LLM Summary

```python
PaperSummary

background

objective

method

logic

results

innovation

future_work
```

All fields should be written in Simplified Chinese.

---

# 8. Report Model

A report consists of:

```
Report

date

statistics

important_authors

important_papers

hot_papers

translations

summaries
```

---

# 9. Statistics Model

```python
Statistics

total_papers

important_papers

hot_papers

translated_papers

processing_time
```

---

# 10. Configuration Model

Configuration should be loaded from YAML files.

Example:

```yaml
filters:

  citation_threshold: 5000

  top_paper_threshold: 500

  hot_score_threshold: 0.75

scheduler:

  timezone: Asia/Shanghai

  run_time: "12:00"

email:

  retry: 3
```

No hardcoded values should exist inside source code.

---

# 11. Crawler Interface

Input

```
None
```

Output

```python
list[Paper]
```

Responsibilities

- Connect to arXiv
- Download recent papers
- Parse metadata

Should NOT

- Translate
- Filter
- Generate summaries

---

# 12. INSPIRE Interface

Input

```python
Paper
```

Output

```python
list[Author]
```

Should return one Author object for every paper author.

---

# 13. Filtering Interface

Input

```python
Paper

+

list[Author]
```

Output

```python
FilterResult
```

Filtering should never modify Paper objects directly.

---

# 14. Translation Interface

Input

```python
Paper
```

Output

```python
TranslationResult
```

---

# 15. LLM Summary Interface

Input

```python
Paper
```

Output

```python
PaperSummary
```

---

# 16. Report Generator Interface

Input

```
Statistics

FilterResult

TranslationResult

PaperSummary
```

Output

```
Markdown

HTML

PDF
```

---

# 17. Email Interface

Input

```
HTML Report

PDF

Markdown
```

Output

```
Email Status
```

Status examples

```
Success

Retry

Failure
```

---

# 18. Scheduler Interface

Input

```
None
```

Output

```
Daily Workflow
```

Responsibilities

- Trigger crawler
- Trigger filtering
- Trigger translation
- Trigger report generation
- Trigger email sending

---

# 19. Error Model

Every module should return structured errors.

Example

```python
ErrorInfo

module

error_type

message

timestamp

retryable
```

Example

```
Module

INSPIRE

Retryable

True
```

---

# 20. Logging Model

Each log entry should contain

```
Timestamp

Module

Operation

Status

Duration

Message
```

---

# 21. Cache Model

Cache author queries.

Suggested cache key

```
Author Name
```

Suggested expiration

```
7 days
```

---

# 22. Future Interfaces

Future versions may add

- Semantic search
- Citation network analysis
- Knowledge graph generation
- Automatic recommendation
- Multiple LLM providers
- Plugin system

Existing interfaces should remain backward compatible.

---

# 23. Development Rules

Codex must never modify an interface unless absolutely necessary.

If an interface changes:

1. Update this document.
2. Update all affected modules.
3. Update corresponding unit tests.
4. Verify backward compatibility.

Interface stability has higher priority than implementation convenience.