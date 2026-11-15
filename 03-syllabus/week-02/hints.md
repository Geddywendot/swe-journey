# Week 02 Hints

> **Rule:** Attempt the exercise for at least 30 minutes before reading Hint 1. Wait an additional 15 minutes before reading Hint 2 or 3.

---

## Exercise 2.1: Streaming Typed CSV Record Parser

### Hint Level 1 (Nudge)
Use `with open(file_path, "r", encoding="utf-8") as f:` and iterate over `f` directly rather than calling `f.readlines()` or `f.read()`.

### Hint Level 2 (Concept Name)
Use the standard library `csv.reader` wrapping the file object, and use `yield TransactionRecord(...)` inside the loop.

### Hint Level 3 (Direction)
Catch `(ValueError, InvalidOperation, IndexError)` within the loop body. When an invalid row is caught, write a diagnostic message to `sys.stderr` and use `continue` so that subsequent valid rows continue streaming without terminating the generator.

---

## Exercise 2.2: Debug This — Broken Connection Pool Context Manager

### Hint Level 1 (Nudge)
Notice that `__enter__` returns the connection, but `__exit__` does not have access to which connection was acquired unless it was saved to an instance attribute or returned through a dedicated context wrapper.

### Hint Level 2 (Concept Name)
In Python, if `__exit__` returns `True`, Python suppresses any active exception that occurred in the `with` block. If it returns `False` or `None`, exceptions propagate naturally.

### Hint Level 3 (Direction)
Create a helper context manager or wrap the acquired connection. In `__exit__(self, exc_type, exc_val, exc_tb)`, execute the cleanup in a `finally` block or unconditional release call, and ensure the method returns `False` so unhandled domain exceptions are raised to the caller.

---

## Exercise 2.3: Building a Queryable Collection with Python Dunder Methods

### Hint Level 1 (Nudge)
Internal storage can simply be a private dictionary `self._items: dict[str, T]`.

### Hint Level 2 (Concept Name)
To implement `__iter__`, delegate directly to `iter(self._items.values())`.

### Hint Level 3 (Direction)
For `__getitem__(self, key: str) -> T`: look up `self._items[key]`. If not present, allow Python's native `KeyError` to raise naturally or raise `KeyError(f"Record with key {key} not found")`.
