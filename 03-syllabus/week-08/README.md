# Week 08: ORM, Migrations & Authentication

**Goal:** Integrate relational databases with FastAPI using SQLAlchemy 2.0 (async), manage schema evolution with Alembic migrations, and secure endpoints with password hashing (bcrypt) and JWT bearer authentication.
**You are done when:** You can design normalized database models with SQLAlchemy declarative mapping, run automated migrations with Alembic, authenticate users with salted password hashing, and protect REST endpoints with JSON Web Tokens (JWT).
**Time plan (4 hrs/day):**
- Day 1–2: Lessons and concepts (about 6 hrs)
- Day 3–4: Exercises silver tasks (about 8 hrs)
- Day 5: Gate and retro (about 4 hrs)
- Lighter day: Review OWASP authentication guidelines, practice running Alembic downgrade/upgrade cycles

**Partner session agenda (45–60 min):**
1. Concept explain-back: SQLAlchemy 2.0 async session lifecycles, Alembic revision graphs, password salt/hash mechanics, and JWT token anatomy (header, payload, signature).
2. Gate walk-through: Live demonstration of Project 3: Task API (`06-projects/03-task-api/`), showing user registration, JWT login, protected task CRUD, and passing test suite.
3. PR review: Review your `week-08/gate` Pull Request.
