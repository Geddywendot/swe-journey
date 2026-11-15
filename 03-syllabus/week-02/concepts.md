# Week 02 Concepts

Master these 6 core Python principles. For each concept, practice explaining it aloud in your own words.

---

### 1. The Python Data Model & Dunder Methods
- **Plain words:** Python does not expose syntax like `len(x)` or `for item in x` as arbitrary language magic. Instead, Python delegates to special methods implemented on the object: `__len__()`, `__iter__()`, and `__getitem__()`. Implementing these dunder methods makes your custom objects behave like native language constructs.
- **Explain it back prompt:** *"What is the difference between `__str__` and `__repr__`, and who is each intended for?"*

### 2. Modern Static Typing (`typing`, `Protocol`)
- **Plain words:** Python remains dynamically typed at runtime, but type annotations (`str | None`, `list[dict[str, Any]]`) enable static type checkers (`mypy`, `pyright`) to verify correctness before code executes. `typing.Protocol` enables structural subtyping ("duck typing with compile-time checking").
- **Explain it back prompt:** *"How does `Protocol` differ from subclassing an Abstract Base Class (ABC)?"*

### 3. Iterators and Generators (`yield`)
- **Plain words:** An iterator produces values one at a time on demand (`next()`). A generator function uses `yield` to pause execution and preserve state between iterations. This allows processing datasets larger than system memory because only a single record is held in RAM at any moment.
- **Explain it back prompt:** *"Why does `[x * 2 for x in large_list]` exhaust memory while `(x * 2 for x in large_list)` does not?"*

### 4. Context Managers & Resource Lifecycles (`__enter__`, `__exit__`)
- **Plain words:** The `with` statement guarantees cleanup of system resources (files, sockets, database locks), even if unhandled exceptions are raised. A context manager implements `__enter__()` to allocate the resource and `__exit__()` to release it.
- **Explain it back prompt:** *"What are the four arguments passed to `__exit__()`, and how do you suppress an exception inside a context manager?"*

### 5. Dataclasses & Value Objects
- **Plain words:** `@dataclass` automatically generates standard boilerplate methods (`__init__`, `__repr__`, `__eq__`) based on type-annotated class attributes. Setting `frozen=True` makes instances immutable and hashable.
- **Explain it back prompt:** *"When should you choose a `@dataclass` over a standard dictionary or a Pydantic model?"*

### 6. Exception Hierarchies & Defensive Error Handling
- **Plain words:** Custom domain exceptions should inherit from Python's standard `Exception` (never `BaseException`). Catching broad exceptions like `except Exception:` without re-raising or logging masks bugs and makes root cause analysis impossible.
- **Explain it back prompt:** *"What is exception chaining using `raise CustomError(...) from original_error`, and why is it essential for debugging?"*
