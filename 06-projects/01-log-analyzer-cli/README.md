# Project 01: High-Performance Log Analyzer CLI

A command-line log analysis utility built with Python 3.12+, `argparse`, and `pytest`.

---

## 1. Project Overview

Production web servers generate millions of access log records daily. Software engineers routinely diagnose outages, latency regressions, and security anomalies by querying log streams directly from the command line.

In this project, you will build `log-analyzer`, a fast, streaming CLI tool capable of processing arbitrarily large log files in constant memory ($O(1)$ RAM), extracting traffic metrics, and emitting structured reports in JSON or plain text.

---

## 2. Requirements & Specifications

### CLI Interface
```bash
log-analyzer [OPTIONS] [LOG_FILE]
```
If `[LOG_FILE]` is omitted, the CLI reads from `sys.stdin`, enabling Unix pipelines:
```bash
cat data/sample.log | log-analyzer --format json
```

### Supported Flags:
- `--format [text|json]`: Output format (default: `text`).
- `--min-status INTEGER`: Filter records to only include HTTP status codes >= threshold (e.g., `--min-status 400` for errors).
- `--top INTEGER`: Number of top requested endpoints to display (default: 5).
- `--quiet`: Suppress informational messages and progress logging on `stderr`.

### Exit Codes:
- `0`: Execution succeeded.
- `1`: Processing or calculation error (e.g. malformed data that could not be parsed).
- `2`: Invalid CLI arguments or unreadable file.

---

## 3. Project Setup

Use `uv` to initialize your project environment and run tests:

```bash
# In 06-projects/01-log-analyzer-cli/
uv sync
uv run pytest
```

When you first clone or inspect this repository, the tests in `tests/` will **fail with `NotImplementedError`**. Your goal is to implement the starter skeletons until all tests pass.

---

## 4. Acceptance Criteria Checklist

- [ ] All functions in `src/log_analyzer/` implemented without modifying test assertions.
- [ ] Log parser uses Python generators (`yield`) to stream records one-by-one.
- [ ] Memory consumption remains constant ($O(1)$) when processing large log files.
- [ ] Handles malformed log lines gracefully by logging a warning to `stderr` and continuing.
- [ ] Full test suite passes: `uv run pytest tests/` with zero failures.
- [ ] Static type check passes: `uv run mypy --strict src/`.
