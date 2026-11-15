"""Tests for statistical aggregation and summary metrics."""

from log_analyzer.analyzer import calculate_summary
from log_analyzer.models import LogRecord
import pytest


def make_record(
    status: int, endpoint: str, latency: float, bytes_sent: int = 100
) -> LogRecord:
  return LogRecord(
      ip_address="10.0.0.1",
      timestamp="2026-11-15T12:00:00Z",
      method="GET",
      endpoint=endpoint,
      protocol="HTTP/1.1",
      status_code=status,
      bytes_sent=bytes_sent,
      response_time_ms=latency,
  )


def test_calculate_summary_empty_records():
  summary = calculate_summary([])
  assert summary.total_requests == 0
  assert summary.median_latency_ms == 0.0
  assert summary.p95_latency_ms == 0.0
  assert summary.top_endpoints == []


def test_calculate_summary_aggregations():
  records = [
      make_record(200, "/users", 10.0),
      make_record(200, "/users", 20.0),
      make_record(404, "/not-found", 30.0),
      make_record(500, "/crash", 40.0),
      make_record(200, "/users", 50.0),
  ]
  summary = calculate_summary(records, top_k=2)

  assert summary.total_requests == 5
  assert summary.status_counts == {200: 3, 404: 1, 500: 1}
  assert summary.top_endpoints == [("/users", 3), ("/not-found", 1)]
  assert summary.median_latency_ms == 30.0
  assert summary.p95_latency_ms >= 40.0


def test_summary_to_dict():
  records = [make_record(200, "/home", 15.0)]
  summary = calculate_summary(records)
  data = summary.to_dict()
  assert data["total_requests"] == 1
  assert "status_counts" in data
  assert "median_latency_ms" in data
