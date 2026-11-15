# Project 03: Task Management REST API

A production-grade, asynchronous RESTful API built with **FastAPI**, **SQLAlchemy 2.0 (async)**, **Alembic**, and **JWT authentication**.

---

## 1. Project Overview

This project serves as the core capstone artifact for Phase 3 (Weeks 6–8) of the software engineering journey. It provides a secure, multi-tenant task tracking service where authenticated users can manage their personal tasks.

### Core Features
- **User Authentication:** Registration, salted password hashing with `bcrypt`, and stateless JWT bearer token issuance.
- **Relational Data Modeling:** Normalized SQLite/PostgreSQL models using SQLAlchemy 2.0 type-annotated declarations.
- **Database Migrations:** Schema versioning managed via Alembic.
- **Tenant Isolation:** Complete data privacy; users can only view, mutate, or delete their own tasks. Cross-tenant access attempts return `404 Not Found`.
- **Automated Test Suite:** Comprehensive async test suite using `pytest`, `pytest-asyncio`, and `httpx.AsyncClient` with an isolated in-memory test database.

---

## 2. Directory Structure

```
06-projects/03-task-api/
├── alembic/
│   ├── env.py              # Async migration runner
│   ├── script.py.mako      # Migration file template
│   └── versions/           # Migration revision scripts
├── alembic.ini             # Alembic configuration
├── pyproject.toml          # Project configuration and dependencies
├── src/
│   └── task_api/
│       ├── __init__.py
│       ├── config.py       # Pydantic Settings environment configuration
│       ├── database.py     # SQLAlchemy async engine, sessionmaker, get_db dependency
│       ├── dependencies.py # get_current_user dependency
│       ├── main.py         # FastAPI application entrypoint and middleware
│       ├── models/         # SQLAlchemy declarative models (User, Task)
│       ├── routers/        # API routers (auth, tasks, users)
│       ├── schemas/        # Pydantic v2 schemas (User, Task, Token)
│       └── security.py     # Password hashing and JWT generation
└── tests/
    ├── conftest.py         # Async SQLite test engine and client fixtures
    ├── test_auth.py        # Registration and authentication test suite
    └── test_tasks.py       # Task CRUD and tenant isolation test suite
```

---

## 3. Getting Started

### Prerequisites
- Python 3.12+
- `uv` package manager (recommended) or `pip`

### Installation
```bash
# Navigate to project directory
cd 06-projects/03-task-api

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
```

### Running Migrations
```bash
# Run migrations up to latest revision
alembic upgrade head
```

### Running the Development Server
```bash
uvicorn task_api.main:app --reload --port 8000
```
API documentation will be available at [http://localhost:8000/docs](http://localhost:8000/docs).

### Running Tests
```bash
pytest
```

---

## 4. Implementation Tasks

The starter code contains missing implementations marked with `TODO` and `NotImplementedError`. Your task is to implement the following modules:

1. **`src/task_api/security.py`**:
   - `hash_password(password: str) -> str`: Hash raw passwords with bcrypt.
   - `verify_password(plain_password: str, hashed_password: str) -> bool`: Verify matching passwords.
   - `create_access_token(data: dict, expires_delta: timedelta | None = None) -> str`: Generate signed JWTs.
2. **`src/task_api/dependencies.py`**:
   - `get_current_user(...)`: Extract Bearer token, verify claims, and fetch user from DB.
3. **`src/task_api/routers/auth.py`**:
   - Complete registration and login routes.
4. **`src/task_api/routers/tasks.py`**:
   - Complete CRUD endpoints enforcing `user_id == current_user.id`.

When all tasks are implemented correctly, all tests in `tests/` will pass!
