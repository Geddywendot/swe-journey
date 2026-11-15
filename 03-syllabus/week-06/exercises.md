# Week 06 Exercises

Complete all Silver exercises to pass the week. Gold exercises are optional stretch challenges.

---

## Exercise 6.1: Designing a Normalized 3NF Schema in PostgreSQL

**Type:** silver  
**Time box:** 60–90 min  
**Task:** Write a SQL migration script `schema.sql` that designs a relational database for a collaborative project management system containing `users`, `projects`, `tasks`, and `tags`.

**Acceptance criteria:**
- [ ] Conforms strictly to Third Normal Form (3NF).
- [ ] Enforces `PRIMARY KEY` (UUID or BIGSERIAL), `UNIQUE` email constraint, and `NOT NULL` constraints.
- [ ] Foreign keys established with appropriate `ON DELETE` rules (`ON DELETE CASCADE` for project tasks; `ON DELETE RESTRICT` for task creators).
- [ ] Many-to-many relationship between `tasks` and `tags` implemented via a junction table `task_tags`.
- [ ] Includes `CHECK` constraints (e.g. `status IN ('todo', 'in_progress', 'done')`).

**Rules:** AI off. Raw PostgreSQL SQL only. Test execution with `psql` or Docker PostgreSQL.  
**Hints:** See `hints.md` section 6.1

---

## Exercise 6.2: Debug This — Slow Sequential Scan & Cartesian Product Join

**Type:** silver ("debug this")  
**Time box:** 60–90 min  
**Task:** A query reporting user task completion metrics takes over 12 seconds to run on a test database with 100,000 tasks, triggering CPU spikes and locking server connections.

Here is the slow, buggy query:
```sql
-- slow_query.sql
EXPLAIN ANALYZE
SELECT 
    u.id, 
    u.email, 
    COUNT(t.id) AS total_tasks,
    COUNT(c.id) AS total_comments
FROM users u
LEFT JOIN tasks t ON t.user_id = u.id
LEFT JOIN comments c ON c.user_id = u.id -- Bug 1: Cartesian product between tasks and comments!
WHERE u.created_at >= '2026-01-01'
GROUP BY u.id, u.email;
-- Bug 2: Missing index on users(created_at) and tasks(user_id) causing full table sequential scans!
```

**Acceptance criteria:**
- [ ] Run `EXPLAIN ANALYZE` and document the cost, execution time, and Seq Scan nodes.
- [ ] Resolve the Cartesian join inflating count totals (using subqueries, independent CTEs, or distinct counts).
- [ ] Add necessary B-Tree indexes to optimize filtering and join performance.
- [ ] Verify execution time drops to under 50 milliseconds with Index Scan in `EXPLAIN ANALYZE`.

**Rules:** Explain why the original query inflated counts.  
**Hints:** See `hints.md` section 6.2

---

## Exercise 6.3: Complex Analytical Queries with Window Functions and CTEs

**Type:** silver  
**Time box:** 60–90 min  
**Task:** Write an analytical SQL query `task_velocity.sql` that computes:
1. The running total of tasks completed per project over time.
2. The 7-day moving average of task completion time.
3. The top 3 fastest task completers per project using `DENSE_RANK() OVER (...)`.

**Acceptance criteria:**
- [ ] Uses Common Table Expressions (`WITH ... AS (...)`) for modularity.
- [ ] Uses window functions: `SUM(...) OVER (PARTITION BY ... ORDER BY ...)`.
- [ ] Uses `DENSE_RANK()` or `ROW_NUMBER()` for ranking without skipping ranks.
- [ ] Tested against populated seed data.

**Rules:** AI off. No application-level processing (Python); all calculations done inside PostgreSQL engine.  
**Hints:** See `hints.md` section 6.3

---

## Exercise 6.4: Custom Connection Pool with Transaction Rollback Semantics

**Type:** gold (stretch)  
**Time box:** 120–180 min  
**Task:** Build a lightweight Python async connection pool manager over raw `asyncpg` sockets. It must support `acquire()` returning a connection context manager that automatically issues `BEGIN` on enter, commits on normal exit, and issues `ROLLBACK` if any exception occurs.

**Acceptance criteria:**
- [ ] Maintains a fixed queue of available connections with capacity limits.
- [ ] Context manager handles `BEGIN`, `COMMIT`, and `ROLLBACK` deterministically.
- [ ] Raises `TimeoutError` if no connection is available within 3.0 seconds.
- [ ] 100% pytest test coverage simulating database errors and verifying rollbacks.

**Rules:** No hints provided for gold stretch exercises.
