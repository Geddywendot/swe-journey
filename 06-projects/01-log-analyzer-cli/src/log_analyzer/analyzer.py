"""Statistical aggregation over log record streams."""

from collections.abc import Iterable
from log_analyzer.models import LogRecord, LogSummary


def calculate_summary(
    records: Iterable[LogRecord], top_k: int = 5
) -> LogSummary:
  """Aggregate total requests, status code distribution, top endpoints, and latencies.

  TODO: Process records lazily, calculate median and 95th percentile response
  times,
  and identify the top_k most requested endpoints.
  """
  raise NotImplementedError("Learner task: Implement calculate_summary()")
