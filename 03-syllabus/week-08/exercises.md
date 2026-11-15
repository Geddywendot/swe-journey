# Week 08 Exercises

Complete all Silver exercises to pass the week. Gold exercises are optional stretch challenges.

---

## Exercise 8.1: Declarative SQLAlchemy 2.0 Async Models and Alembic Pipeline

**Type:** silver  
**Time box:** 60–90 min  
**Task:** Configure a modern SQLAlchemy 2.0 async engine and establish an Alembic migration pipeline for a multi-user Task Management system.

**Acceptance criteria:**
- [ ] Define `User` model (`id`, `email`, `hashed_password`, `is_active`, `created_at`) with unique index on `email`.
- [ ] Define `Task` model (`id`, `title`, `description`, `status`, `user_id`, `created_at`, `updated_at`) with foreign key constraint referencing `users.id` with `ON DELETE CASCADE`.
- [ ] Setup `alembic.ini` and `alembic/env.py` to support `async_engine` and target metadata.
- [ ] Generate initial migration script using `alembic revision --autogenerate -m "create users and tasks"`.
- [ ] Execute `alembic upgrade head`, inspect the generated SQLite or PostgreSQL schema, and verify downgrade capability with `alembic downgrade -1`.

**Rules:** AI off. Modern SQLAlchemy 2.0 style only (use `Mapped[...]` and `mapped_column(...)`).  
**Hints:** See `hints.md` section 8.1

---

## Exercise 8.2: Debug This — Missing Greenlet in Async SQLAlchemy & N+1 Query

**Type:** silver ("debug this")  
**Time box:** 60–90 min  
**Task:** A developer built an endpoint to list all users alongside their assigned tasks. When running the code with `AsyncSession`, the server crashes with `sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call a await-only method in a sync context`. Furthermore, when fixed incorrectly with synchronous calls, it executes 101 separate SQL queries for 100 users (the classic N+1 query problem).

Here is the buggy route:
```python
# buggy_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import User
from database import get_db

router = APIRouter()

@router.get("/users-with-tasks")
async def get_users_with_tasks(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    
    response = []
    for user in users:
        # Bug 1: Accessing relationship attribute `user.tasks` triggers lazy loading,
        # which attempts synchronous I/O inside async event loop, raising MissingGreenlet!
        user_tasks = [t.title for t in user.tasks]
        response.append({
            "id": user.id,
            "email": user.email,
            "tasks": user_tasks
        })
    return response
```

**Acceptance criteria:**
- [ ] Identify why accessing `user.tasks` triggers `MissingGreenlet` in SQLAlchemy async mode.
- [ ] Refactor the query to use `select(User).options(selectinload(User.tasks))` to eagerly load tasks in a single coalesced query.
- [ ] Explain the difference between `selectinload` and `joinedload` for one-to-many collections.
- [ ] Verify using SQL query logging (`echo=True`) that only 2 queries are issued (1 for users, 1 for all related tasks via `IN (...)`), completely eliminating the N+1 problem.

**Rules:** Explain the greenlet mechanics and query reduction.  
**Hints:** See `hints.md` section 8.2

---

## Exercise 8.3: Project 3 Milestone — The Task Management API

**Type:** silver (milestone core artifact)  
**Time box:** 180–240 min  
**Task:** Complete the starter code in `06-projects/03-task-api/`. Implement full user registration, password verification, JWT access token generation, and authenticated CRUD for user tasks with complete multi-tenant isolation.

**Acceptance criteria:**
- [ ] Complete `src/task_api/security.py`: Implement `hash_password`, `verify_password`, `create_access_token`, and token decoding using `pwdlib`/`passlib` and `PyJWT`.
- [ ] Complete `src/task_api/dependencies.py`: Implement `get_current_user` verifying `Authorization: Bearer <token>` and fetching user from database.
- [ ] Complete `src/task_api/routers/auth.py`: `POST /auth/register` (hashes password, returns `201`), `POST /auth/login` (validates credentials, returns JWT bearer token).
- [ ] Complete `src/task_api/routers/tasks.py`: Full CRUD for tasks. Crucially, a user must ONLY be able to read, update, or delete tasks where `task.user_id == current_user.id`. Accessing another user's task returns `404 Not Found`.
- [ ] Run the full test suite in `06-projects/03-task-api/tests/` and achieve 100% passing tests with pytest and `pytest-asyncio`.

**Rules:** AI off. Adhere strictly to the project structure and type hints.  
**Hints:** See `hints.md` section 8.3

---

## Exercise 8.4: Refresh Token Rotation & Invalidation Store

**Type:** gold (stretch)  
**Time box:** 120–180 min  
**Task:** Extend the authentication system with short-lived access tokens (15 minutes) and long-lived refresh tokens (7 days). Implement refresh token rotation: every time a refresh token is used, it is revoked, and a new pair is issued. Detect token reuse: if an already-revoked refresh token is presented, immediately revoke all active refresh tokens for that user (compromise detection).

**Acceptance criteria:**
- [ ] `POST /auth/refresh` accepts refresh token and issues fresh access/refresh token pair.
- [ ] Revoked tokens stored in a database blacklist or cache table.
- [ ] Automatic revocation of all family tokens upon detection of reused refresh token.
- [ ] Automated integration test proving token reuse triggers security lockout.

**Rules:** No hints provided for gold stretch exercises.
