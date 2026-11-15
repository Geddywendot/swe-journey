"""Tests for CLI arguments, stream redirection, and exit codes."""

from pathlib import Path
from log_analyzer.cli import build_parser, main
import pytest


def test_build_parser_defaults():
  parser = build_parser()
  args = parser.parse_args(["app.log"])
  assert args.log_file == "app.log"
  assert args.format == "text"
  assert args.min_status == 0
  assert args.top == 5
  assert args.quiet is False


def test_cli_execution_with_file(tmp_path: Path, capsys):
  test_file = tmp_path / "access.log"
  test_file.write_text(
      '127.0.0.1 - - [timestamp] "GET /api HTTP/1.1" 200 100 10.0\n'
  )

  exit_code = main([str(test_file), "--format", "json"])
  assert exit_code == 0

  captured = capsys.readouterr()
  assert '"total_requests": 1' in captured.out


def test_cli_missing_file_returns_exit_code_2(capsys):
  exit_code = main(["non_existent_file.log"])
  assert exit_code == 2
  captured = capsys.readouterr()
  assert "not found" in captured.err.lower() or "error" in captured.err.lower()
