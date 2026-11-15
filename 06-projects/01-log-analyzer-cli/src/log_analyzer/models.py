"""Data models for log records and summary statistics."""

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class LogRecord:
  """Represents a single parsed access log record."""

  ip_address: str
  timestamp: str
  method: str
  endpoint: str
  protocol: str
  status_code: int
  bytes_sent: int
  response_time_ms: float


@dataclass(frozen=True)
class LogSummary:
  """Aggregated statistics across a collection of log records."""

  total_requests: int
  status_counts: dict[int, int]
  top_endpoints: list[tuple[str, int]]
  median_latency_ms: float
  p95_latency_ms: float

  def to_dict(self) -> dict[str, Any]:
    """Convert summary to JSON-serializable dictionary.

    TODO: Implement dictionary serialization.
    """
    raise NotImplementedError("Learner task: Implement to_dict()")
