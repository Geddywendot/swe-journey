"""Tests for log parsing and stream handling."""

from pathlib import Path
from log_analyzer.models import LogRecord
from log_analyzer.parser import parse_line, parse_log_file, parse_log_stream
import pytest


def test_parse_valid_line():
  raw = (
      '192.168.1.10 - - [15/Nov/2026:10:00:01 +0000] "GET /api/v1/users'
      ' HTTP/1.1" 200 452 12.4'
  )
  record = parse_line(raw)
  assert record is not None
  assert record.ip_address == "192.168.1.10"
  assert record.method == "GET"
  assert record.endpoint == "/api/v1/users"
  assert record.protocol == "HTTP/1.1"
  assert record.status_code == 200
  assert record.bytes_sent == 452
  assert record.response_time_ms == 12.4


def test_parse_corrupt_line_returns_none():
  raw = "MALFORMED GARBAGE LINE"
  assert parse_line(raw) is None


def test_stream_parser_skips_invalid_rows():
  lines = [
      '192.168.1.1 - - [15/Nov/2026:10:00:01 +0000] "GET /test HTTP/1.1" 200'
      " 100 10.0",
      "CORRUPT LINE",
      '192.168.1.2 - - [15/Nov/2026:10:00:02 +0000] "POST /login HTTP/1.1" 401'
      " 50 15.0",
  ]
  records = list(parse_log_stream(lines))
  assert len(records) == 2
  assert records[0].ip_address == "192.168.1.1"
  assert records[1].ip_address == "192.168.1.2"


def test_stream_parser_filters_by_min_status():
  lines = [
      '1.1.1.1 - - [timestamp] "GET /a HTTP/1.1" 200 100 5.0',
      '2.2.2.2 - - [timestamp] "GET /b HTTP/1.1" 404 100 5.0',
      '3.3.3.3 - - [timestamp] "GET /c HTTP/1.1" 500 100 5.0',
  ]
  records = list(parse_log_stream(lines, min_status=400))
  assert len(records) == 2
  assert all(r.status_code >= 400 for r in records)


def test_parse_log_file_streams_lazily(tmp_path: Path):
  test_file = tmp_path / "test.log"
  test_file.write_text(
      '127.0.0.1 - - [date] "GET /health HTTP/1.1" 200 10 1.0\n'
  )
  generator = parse_log_file(test_file)
  record = next(generator)
  assert record.endpoint == "/health"
