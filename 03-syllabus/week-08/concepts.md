# Week 08 Concepts

Master these 6 backend persistence and security fundamentals. For each concept, practice explaining it aloud in your own words.

---

### 1. SQLAlchemy 2.0 Modern Declarative Mapping & Async Engine
- **Plain words:** SQLAlchemy 2.0 uses type-annotated declarations (`Mapped[int] = mapped_column(...)`) that harmonize Python's type system with SQL column types. When used asynchronously (`AsyncSession`), queries use modern `select()` syntax executed via `await session.execute(...)`. Crucially, lazy loading of relationships fails in async mode; relationships must be explicitly loaded using `selectinload` or `joinedload`.
- **Explain it back prompt:** *"Why does accessing an unloaded relationship attribute on an async SQLAlchemy model trigger a `MissingGreenlet` error, and how does `selectinload` resolve it?"*

### 2. Database Schema Migrations with Alembic
- **Plain words:** As application code changes, the underlying database schema must evolve without destroying existing production data. Alembic maintains a directed acyclic graph (DAG) of migration scripts and tracks the applied version in a special table (`alembic_version`). Each script defines an `upgrade()` and a corresponding `downgrade()` function to guarantee reversible schema changes.
- **Explain it back prompt:** *"Why should database schema alterations be managed via version-controlled migration files rather than letting an ORM call `Base.metadata.create_all()` in production?"*

### 3. Password Hashing, Salting, and Work Factors
- **Plain words:** Passwords must never be stored in plain text or using fast cryptographic hashes like MD5 or SHA-256 (which can be cracked at billions of hashes per second with GPUs). Adaptive algorithms like bcrypt or Argon2 incorporate a unique random salt per user (defeating rainbow tables) and a configurable computational cost factor (making brute-force guessing economically infeasible).
- **Explain it back prompt:** *"What is the difference between a fast cryptographic hash (like SHA-256) and a slow key derivation function (like bcrypt/Argon2) regarding password storage security?"*

### 4. Stateless JWT Authentication (Access & Refresh Tokens)
- **Plain words:** JSON Web Tokens (JWT) contain three base64url-encoded segments: Header (algorithm), Payload (claims: user ID, expiration, roles), and Signature (HMAC or RSA). The signature prevents tampering: only the server with the secret key can produce a valid token. Because the token is self-contained and verified cryptographically without database queries, it is stateless.
- **Explain it back prompt:** *"If a JWT is stateless and verified solely by its cryptographic signature, what is the architectural challenge of immediately revoking a compromised token before its expiration?"*

### 5. Dependency Injection for Database Sessions & Current User
- **Plain words:** FastAPI allows cleanly decoupling database connection management and authentication. A `get_db` dependency yields an `AsyncSession` per HTTP request, automatically committing transactions on success and rolling back on exceptions. A `get_current_user` dependency extracts the Bearer token, validates the JWT signature and expiration, queries the database, and injects the authenticated `User` object directly into protected route handlers.
- **Explain it back prompt:** *"How does chaining `get_current_user` as a dependency simplify authorization across dozens of protected API routes?"*

### 6. Relational Data Isolation & Multi-Tenancy
- **Plain words:** In a multi-user application, users must never access, view, or modify resources belonging to another user. Every query for a user-owned resource (such as tasks, notes, or payment methods) must explicitly filter by the authenticated user's ID (`WHERE task.user_id == current_user.id`), preventing Insecure Direct Object References (IDOR).
- **Explain it back prompt:** *"What is an Insecure Direct Object Reference (IDOR) vulnerability, and how do we prevent it when fetching a task by ID (`GET /tasks/{task_id}`)?"*
