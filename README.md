# Paper Assistant

Personal AI assistant for arXiv paper monitoring.

## Phase 1 Status

This repository currently contains the project initialization skeleton only. It includes
configuration loading, logging setup, shared data models, an application entry point, and tests.

Later pipeline features such as arXiv crawling, INSPIRE lookup, translation, LLM summaries,
report generation, email delivery, scheduling, and GUI logic are intentionally not implemented yet.

## Install

```bash
python -m pip install -e .[dev]
```

## Run

```bash
paper-assistant
```

or:

```bash
python -m main
```

## Test

```bash
pytest
```
