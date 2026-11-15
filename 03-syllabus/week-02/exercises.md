# Week 02 Exercises

Complete all Silver exercises to pass the week. Gold exercises are optional stretch challenges.

---

## Exercise 2.1: Streaming Typed CSV Record Parser

**Type:** silver  
**Time box:** 60–90 min  
**Task:** Build a memory-efficient generator `stream_records(file_path: Path) -> Generator[TransactionRecord, None, None]` that parses large CSV files of financial transactions into immutable dataclasses without loading the whole file into RAM.

**Starter skeleton:**
```python
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
from typing import Generator


@dataclass(frozen=True)
class TransactionRecord:
  transaction_id: str
  account_id: str
  amount: Decimal
  timestamp: str


def stream_records(
    file_path: Path,
) -> Generator[TransactionRecord, None, None]:
  """Stream and yield TransactionRecord objects line by line.

  Skips malformed rows by logging to stderr.
  """
  # TODO: Implement line-by-line streaming generator
  pass
```

**Acceptance criteria:**
- [ ] Uses a generator with `yield` to maintain $O(1)$ memory consumption regardless of file size.
- [ ] Validates that `amount` converts accurately to `Decimal` (never floating-point).
- [ ] Skips and records malformed rows to `sys.stderr` without crashing the stream.
- [ ] Passes static type checking with `mypy --strict`.

**Rules:** AI off. Do not use `pandas`. Use standard library `csv` or manual line splitting.  
**Hints:** See `hints.md` section 2.1

---

## Exercise 2.2: Debug This — Broken Connection Pool Context Manager

**Type:** silver ("debug this")  
**Time box:** 60–90 min  
**Task:** A junior developer wrote a database connection pool context manager, but under heavy exception loads it leaks connections and crashes the application because exceptions are silently swallowed or locks are left acquired.

Here is the broken implementation:
```python
class BrokenConnectionPool:

  def __init__(self, capacity: int = 5):
    self.capacity = capacity
    self.pool = [f"conn_{i}" for i in range(capacity)]
    self.active = []

  def acquire(self):
    conn = self.pool.pop(0)
    self.active.append(conn)
    return conn

  def release(self, conn):
    self.active.remove(conn)
    self.pool.append(conn)

  def __enter__(self):
    # Bug 1: What happens if pool is empty?
    return self.acquire()

  def __exit__(self, exc_type, exc_val, exc_tb):
    # Bug 2: Missing connection reference to release!
    # Bug 3: Returning True unconditionally suppresses all application crashes!
    return True
```

**Acceptance criteria:**
- [ ] Refactor the class to implement a proper context manager managing acquired connections reliably.
- [ ] Ensure `__exit__` always returns connections to the pool even when an exception is raised within the `with` block.
- [ ] Ensure exceptions are properly propagated (not silently swallowed) unless specifically handled.
- [ ] Raise a descriptive `PoolExhaustedError` when all connections are active.

**Rules:** Write tests proving that connections are restored even when the caller raises a `RuntimeError`.  
**Hints:** See `hints.md` section 2.2

---

## Exercise 2.3: Building a Queryable Collection with Python Dunder Methods

**Type:** silver  
**Time box:** 60–90 min  
**Task:** Implement a custom collection class `RecordIndex` that wraps a collection of records and implements standard Python dunder methods: `__len__`, `__getitem__`, `__contains__`, `__iter__`, and a meaningful `__repr__`.

**Starter skeleton:**
```python
from typing import Generic, Iterator, TypeVar

T = TypeVar("T")


class RecordIndex(Generic[T]):

  def __init__(self) -> None:
    # TODO: Initialize internal lookup data structures
    pass

  def add(self, key: str, record: T) -> None:
    # TODO: Store record
    pass

  def __len__(self) -> int:
    # TODO: Return count
    pass

  def __getitem__(self, key: str) -> T:
    # TODO: Return record or raise KeyError
    pass

  def __contains__(self, key: object) -> bool:
    # TODO: Membership check
    pass

  def __iter__(self) -> Iterator[T]:
    # TODO: Iterate over all records
    pass

  def __repr__(self) -> str:
    # TODO: Clear debugging representation
    pass
```

**Acceptance criteria:**
- [ ] Supports `len(index)`, `index["id123"]`, `"id123" in index`, and `for r in index:`.
- [ ] Raises `KeyError` when an item is missing.
- [ ] Implements generic typing `Generic[T]`.

**Rules:** AI off. Write clean unit tests asserting each dunder protocol.  
**Hints:** See `hints.md` section 2.3

---

## Exercise 2.4: Structural Subtyping with `typing.Protocol`

**Type:** gold (stretch)  
**Time box:** 120–180 min  
**Task:** Build a pluggable data export pipeline using `typing.Protocol`. Define an `Exporter` protocol requiring `export(records: Sequence[Record]) -> bytes` and `content_type: str`. Implement three completely independent classes (`JsonExporter`, `CsvExporter`, `ParquetExporter`) without inheriting from a common base class, and verify type compliance with static analysis.

**Acceptance criteria:**
- [ ] Define `@runtime_checkable` `Protocol` with both method and property signatures.
- [ ] Zero inheritance (`class JsonExporter:` with no base class).
- [ ] Pipeline function `publish_report(exporter: Exporter)` accepts any conforming class.
- [ ] Passes `mypy --strict`.

**Rules:** No hints provided for gold stretch exercises.
