# AGENTS.md

## Project Overview

This repository contains a research assistant for monitoring arXiv papers in the fields of General Relativity and Quantum Cosmology (gr-qc) and High Energy Physics - Theory (hep-th).

The project is developed incrementally according to the design documents under the `docs/` directory.

---

## Instructions for AI Coding Agents

Before implementing any code:

1. Read all documents in the `docs/` directory.
2. Follow the development order defined in `05_Roadmap.md`.
3. Implement **only one Phase at a time**.
4. Do not modify completed Phases unless required.
5. Follow the interfaces defined in `06_API_Design.md`.
6. Keep configuration outside source code.
7. Write unit tests for every new module.
8. Update documentation if interfaces change.
9. Keep the project structure consistent with `07_Project_Structure.md`.
10. Make small, focused changes rather than large refactors.

---

## Coding Standards

- Python 3.12+
- Follow PEP 8.
- Use type hints.
- Use docstrings.
- Avoid duplicated code.
- Never hardcode API keys or credentials.

---

## Testing Requirements

Before completing a task:

- Run unit tests.
- Ensure existing tests still pass.
- Do not introduce breaking changes.

---

## Git Workflow

For each completed Phase:

1. Implement the feature.
2. Run tests.
3. Update documentation if necessary.
4. Commit with a meaningful Git message.