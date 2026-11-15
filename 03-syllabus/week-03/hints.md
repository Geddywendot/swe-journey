# Week 03 Hints

> **Rule:** Attempt the exercise for at least 30 minutes before reading Hint 1. Wait an additional 15 minutes before reading Hint 2 or 3.

---

## Exercise 3.1: Parsing Arguments and Exit Codes with `argparse`

### Hint Level 1 (Nudge)
Use `nargs="+"` on positional arguments to accept one or more numbers: `parser.add_argument("numbers", type=float, nargs="+")`.

### Hint Level 2 (Concept Name)
Use `choices=["add", "multiply", "mean"]` on `--operation` to let `argparse` automatically validate allowed strings and generate helpful error messages.

### Hint Level 3 (Direction)
In `main(args=None)`, wrap execution in a `try...except` block. Catch mathematical errors like division by zero, print the error to `sys.stderr`, and return code `1`. For successful operations, print the formatted result to `sys.stdout` and return `0`.

---

## Exercise 3.2: Debug This — Flaky Pytest Suite with Leaking Global State

### Hint Level 1 (Nudge)
The problem occurs because Python modules are singletons in memory; `REGISTRY_DB` persists across test function invocations.

### Hint Level 2 (Concept Name)
Implement a pytest fixture with `autouse=True` that empties the dictionary before or after each test, or encapsulate the registry into a class: `class Registry: ...`.

### Hint Level 3 (Direction)
Best engineering approach: refactor the functions into a `UserRegistry` class that owns its own internal dictionary. Then create a pytest fixture in `conftest.py`:
```python
@pytest.fixture
def registry():
  return UserRegistry()
```
Inject this fixture into every test so each test gets a pristine, isolated instance.

---

## Exercise 3.3: Parametrized Pytest Fixtures for File Scenarios

### Hint Level 1 (Nudge)
Pytest provides a built-in fixture called `tmp_path` which is a `pathlib.Path` pointing to a temporary directory created uniquely for that test run.

### Hint Level 2 (Concept Name)
Use `tmp_path / "test.json"` and write test strings using `file_path.write_text(...)`.

### Hint Level 3 (Direction)
Use `with pytest.raises(ExpectedException) as exc_info:` to capture the error and assert that `exc_info.value` contains the expected error message or error code.
