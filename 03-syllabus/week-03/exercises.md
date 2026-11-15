# Week 03 Exercises

Complete all Silver exercises to pass the week. Gold exercises are optional stretch challenges.

---

## Exercise 3.1: Parsing Arguments and Exit Codes with `argparse`

**Type:** silver  
**Time box:** 60–90 min  
**Task:** Build a CLI module `cli_calc.py` that accepts positional numbers and options `--operation` (`add`, `multiply`, `mean`), `--round` (integer precision), and `--quiet` (suppresses status text).

**Starter skeleton:**
```python
import argparse
import sys
from typing import Sequence


def parse_args(args: Sequence[str] | None = None) -> argparse.Namespace:
  parser = argparse.ArgumentParser(
      description="Perform mathematical operations on a list of numbers."
  )
  # TODO: Configure positional and optional arguments
  return parser.parse_args(args)


def main(args: Sequence[str] | None = None) -> int:
  # TODO: Parse arguments, execute calculation, print to stdout/stderr
  # Return 0 on success, 1 on calculation error, 2 on invalid input
  return 0


if __name__ == "__main__":
  sys.exit(main())
```

**Acceptance criteria:**
- [ ] Returns exit code `0` on successful operation with calculation result written to `stdout`.
- [ ] Returns exit code `2` with usage instructions written to `stderr` if arguments are missing or invalid.
- [ ] `--quiet` suppresses informational messages while keeping the final output on `stdout`.
- [ ] Fully tested with pytest passing mock argument lists to `parse_args()` and `main()`.

**Rules:** AI off. Use Python standard library `argparse` only.  
**Hints:** See `hints.md` section 3.1

---

## Exercise 3.2: Debug This — Flaky Pytest Suite with Leaking Global State

**Type:** silver ("debug this")  
**Time box:** 60–90 min  
**Task:** A developer created a test suite for a user registry, but tests pass when run individually (`pytest -k test_a`) and fail when run as a full suite (`pytest`), or pass in one order and fail in another due to leaking mutable global state.

Here is the buggy code:
```python
# registry.py
REGISTRY_DB = {}


def register_user(username: str, role: str = "member"):
  if username in REGISTRY_DB:
    raise ValueError(f"User {username} already registered")
  REGISTRY_DB[username] = {"role": role}
  return REGISTRY_DB[username]


def get_user_count():
  return len(REGISTRY_DB)


# test_registry.py
from registry import get_user_count, register_user


def test_user_registration():
  user = register_user("alice")
  assert user["role"] == "member"
  assert get_user_count() == 1


def test_duplicate_registration_fails():
  register_user("bob")
  # Flaky: If test_user_registration ran before, user count is not 1!
  assert get_user_count() == 1


def test_admin_registration():
  user = register_user("admin", role="admin")
  assert user["role"] == "admin"
```

**Acceptance criteria:**
- [ ] Refactor the architecture to avoid mutable global module state, or write a pytest fixture with an autouse teardown that resets state between tests.
- [ ] Use `tmp_path` or dependency injection to provide clean registry instances to each test.
- [ ] Verify that running tests in random order (`pytest --random-order`) passes 100% reliably.

**Rules:** Do not disable test assertions. Fix the architecture and test isolation.  
**Hints:** See `hints.md` section 3.2

---

## Exercise 3.3: Parametrized Pytest Fixtures for File Scenarios

**Type:** silver  
**Time box:** 60–90 min  
**Task:** Write a comprehensive test suite testing a file validation function `validate_config_file(path: Path) -> dict[str, str]` against multiple realistic scenarios: valid JSON, empty file, non-existent path, corrupted JSON, and permission denied.

**Acceptance criteria:**
- [ ] Use `pytest.fixture` with `tmp_path` to generate isolated test fixtures on the fly.
- [ ] Use `@pytest.mark.parametrize` to test valid inputs and expected outcomes.
- [ ] Use `pytest.raises` to assert specific custom exceptions on corrupted or missing files.
- [ ] Ensure all generated temporary files are cleaned up after the test session.

**Rules:** AI off. Do not leave temporary test files in the workspace directory.  
**Hints:** See `hints.md` section 3.3

---

## Exercise 3.4: Building a Pluggable CLI Subcommand Architecture

**Type:** gold (stretch)  
**Time box:** 120–180 min  
**Task:** Using either `argparse` subparsers or `click`, build a Git-like modular command runner supporting commands like `run`, `validate`, and `report`. Each subcommand must live in its own isolated Python module with its own argument definitions and handlers, dynamically discovered at runtime without a giant hardcoded `if/elif` block.

**Acceptance criteria:**
- [ ] Main entrypoint automatically registers subcommands found in a `commands/` directory.
- [ ] Subcommands define their own arguments, help strings, and handlers.
- [ ] Global options (`--verbose`, `--config`) are inherited and accessible by subcommands.
- [ ] Passing full pytest suite testing command invocation and error handling.

**Rules:** No hints provided for gold stretch exercises.
