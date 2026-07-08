# 07 Project Structure

## Paper Assistant Project Directory Specification

Version: v1.0

---

# 1. Purpose

This document defines the standard directory structure for the Paper Assistant project.

All source code, configuration files, documentation, templates, reports, tests, and resources must follow this structure.

Codex should never create arbitrary directories unless this document is updated.

---

# 2. Top-Level Directory Structure

```
paper-assistant/

├── config/
├── docs/
├── logs/
├── reports/
├── cache/
├── prompts/
├── src/
├── tests/
├── assets/
├── scripts/

├── .env
├── .gitignore
├── README.md
├── LICENSE
├── requirements.txt
├── pyproject.toml
```

---

# 3. Configuration Directory

```
config/

├── settings.yaml
├── email.yaml
├── filters.yaml
├── scheduler.yaml
├── logging.yaml
├── llm.yaml
```

Purpose

Store all configurable parameters.

Rules

- Never place source code here.
- Never hardcode configuration values elsewhere.

---

# 4. Documentation Directory

```
docs/

00_Codex_Instructions.md

01_Project_Requirements.md

02_System_Architecture.md

03_Development_Guidelines.md

04_Testing_Strategy.md

05_Roadmap.md

06_API_Design.md

07_Project_Structure.md

08_Prompts.md

09_Deployment.md
```

Purpose

Project documentation.

---

# 5. Source Code Directory

```
src/

├── crawler/
├── inspire/
├── filter/
├── analyzer/
├── translator/
├── summary/
├── report/
├── email/
├── scheduler/
├── cache/
├── config/
├── models/
├── services/
├── utils/
├── gui/
└── main.py
```

---

# 6. crawler/

Responsibilities

- Connect to arXiv
- Retrieve papers
- Parse metadata

Suggested files

```
crawler/

__init__.py

arxiv_client.py

parser.py

models.py
```

---

# 7. inspire/

Responsibilities

- Query INSPIRE
- Parse author information
- Cache results

Suggested files

```
inspire/

client.py

author.py

cache.py
```

---

# 8. filter/

Responsibilities

- Rule A
- Rule B
- Rule C

Suggested files

```
filter/

rules.py

engine.py

scoring.py
```

---

# 9. analyzer/

Responsibilities

Research hotspot analysis.

Suggested files

```
analyzer/

keyword.py

llm.py

score.py
```

---

# 10. translator/

Responsibilities

Translation.

Suggested files

```
translator/

translator.py

prompt.py
```

---

# 11. summary/

Responsibilities

Generate LLM summaries.

Suggested files

```
summary/

summarizer.py

formatter.py
```

---

# 12. report/

Responsibilities

Generate reports.

Suggested files

```
report/

markdown.py

html.py

pdf.py

template.py
```

---

# 13. email/

Responsibilities

Email sending.

Suggested files

```
email/

sender.py

smtp.py
```

---

# 14. scheduler/

Responsibilities

Automatic execution.

Suggested files

```
scheduler/

scheduler.py

jobs.py
```

---

# 15. cache/

Responsibilities

Local cache management.

Suggested files

```
cache/

author_cache.db

paper_cache.db
```

SQLite is recommended.

---

# 16. config/

Responsibilities

Configuration loader.

Suggested files

```
config/

loader.py

validator.py
```

---

# 17. models/

Purpose

Shared data models.

Suggested files

```
models/

paper.py

author.py

report.py

statistics.py
```

Every module should import models from here.

---

# 18. services/

Purpose

High-level orchestration.

Suggested files

```
services/

daily_pipeline.py

workflow.py
```

Services should coordinate modules but contain minimal business logic.

---

# 19. utils/

Purpose

Reusable utilities.

Suggested files

```
utils/

logger.py

time.py

network.py

retry.py

helpers.py
```

Rules

Utilities should remain generic and reusable.

---

# 20. gui/

Responsibilities

Desktop application.

Suggested files

```
gui/

main_window.py

settings.py

report_viewer.py

email_dialog.py

log_viewer.py
```

GUI should never contain business logic.

---

# 21. prompts/

```
prompts/

translation.md

summary.md

hot_topic.md

system.md
```

Purpose

Store all LLM prompts.

Never hardcode prompts inside Python files.

---

# 22. reports/

```
reports/

2026/

07/

2026-07-03.md

2026-07-03.html

2026-07-03.pdf
```

Organize reports by year and month.

---

# 23. logs/

```
logs/

2026/

07/

daily.log

error.log
```

Rotate logs automatically.

---

# 24. cache/

Cache examples

```
cache/

author_cache.db

paper_cache.db

translation_cache.db
```

Cache expiration should be configurable.

---

# 25. tests/

```
tests/

unit/

integration/

e2e/

fixtures/

mock_data/
```

Each source module should have corresponding tests.

---

# 26. assets/

```
assets/

logo/

icons/

images/

templates/

styles/
```

Store static resources only.

---

# 27. scripts/

```
scripts/

setup.py

build.py

release.py

clean.py
```

Automation scripts belong here.

---

# 28. Naming Conventions

Directories

Use lowercase.

Example

```
translator
```

Files

Use snake_case.

Example

```
paper_summary.py
```

Classes

Use PascalCase.

Example

```
PaperSummary
```

Functions

Use snake_case.

Example

```
translate_title()
```

Constants

Use uppercase.

Example

```
DEFAULT_TIMEOUT
```

---

# 29. Dependency Rules

Allowed dependency direction

```
GUI

↓

Services

↓

Business Modules

↓

Models

↓

Utilities
```

Lower layers must never import higher layers.

Example

Correct

```
GUI

↓

Report
```

Incorrect

```
Report

↓

GUI
```

---

# 30. Development Rules

Codex should follow these rules:

- Never move files without updating documentation.
- Never create duplicate modules.
- Reuse existing models whenever possible.
- Keep modules focused on a single responsibility.
- Avoid circular imports.
- Maintain a clean directory hierarchy.

Project structure should remain stable throughout development.

---