"""Log file stream parser using Python generators."""

from collections.abc import Generator, Iterable
from pathlib import Path
from log_analyzer.models import LogRecord


def parse_line(line: str) -> LogRecord | None:
  """Parse a single log line into a LogRecord.

  Returns None if line is malformed or unparseable.

  TODO: Implement regex or token splitting to parse access log line.
  Format: <ip> - - [<timestamp>] "<method> <endpoint> <protocol>" <status> <bytes> <latency_ms>
  """
  raise NotImplementedError("Learner task: Implement parse_line()")


def parse_log_stream(
    lines: Iterable[str], min_status: int = 0
) -> Generator[LogRecord, None, None]:
  """Stream and yield LogRecord instances from an iterable of lines.

  Filters records where status_code >= min_status.
  Logs unparseable lines to stderr without raising exceptions.

  TODO: Implement generator yielding valid LogRecord objects.
  """
  raise NotImplementedError("Learner task: Implement parse_log_stream()")


def parse_log_file(
    file_path: Path, min_status: int = 0
) -> Generator[LogRecord, None, None]:
  """Open and stream records lazily from a file path.

  TODO: Open file with context manager and delegate to parse_log_stream().
  """
  raise NotImplementedError("Learner task: Implement parse_log_file()")
