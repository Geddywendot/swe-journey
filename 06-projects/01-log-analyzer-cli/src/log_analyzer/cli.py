"""Command line interface entrypoint for log-analyzer."""

import argparse
from collections.abc import Sequence
import sys
from log_analyzer.models import LogSummary


def build_parser() -> argparse.ArgumentParser:
  """Build and configure command-line argument parser.

  TODO: Configure arguments:
  - LOG_FILE (optional positional)
  - --format choices ['text', 'json']
  - --min-status (int, default 0)
  - --top (int, default 5)
  - --quiet (flag)
  """
  raise NotImplementedError("Learner task: Implement build_parser()")


def format_report_text(summary: LogSummary) -> str:
  """Format summary statistics into clean, human-readable plain text.

  TODO: Implement readable text report.
  """
  raise NotImplementedError("Learner task: Implement format_report_text()")


def format_report_json(summary: LogSummary) -> str:
  """Format summary statistics into indented JSON string.

  TODO: Implement JSON formatting using summary.to_dict().
  """
  raise NotImplementedError("Learner task: Implement format_report_json()")


def main(argv: Sequence[str] | None = None) -> int:
  """CLI entrypoint.

  Parses arguments, executes streaming pipeline, outputs report, and returns
  exit code.

  TODO: Implement main flow returning 0 (success), 1 (error), or 2 (bad args).
  """
  raise NotImplementedError("Learner task: Implement main()")


if __name__ == "__main__":
  sys.exit(main())
