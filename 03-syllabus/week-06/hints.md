# Week 06 Hints

> **Rule:** Attempt the exercise for at least 30 minutes before reading Hint 1. Wait an additional 15 minutes before reading Hint 2 or 3.

---

## Exercise 6.1: Designing a Normalized 3NF Schema in PostgreSQL

### Hint Level 1 (Nudge)
Create `task_tags` junction table with composite primary key: `PRIMARY KEY (task_id, tag_id)`.

### Hint Level 2 (Concept Name)
Use PostgreSQL's native `TIMESTAMPTZ` with `DEFAULT NOW()` for all timestamp columns.

### Hint Level 3 (Direction)
Syntax example:
```sql
CREATE TABLE task_tags (
    task_id UUID NOT NULL REFERENCES tasks(id) ON DELETE CASCADE,
    tag_id UUID NOT NULL REFERENCES tags(id) ON DELETE CASCADE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (task_id, tag_id)
);
```

---

## Exercise 6.2: Debug This — Slow Sequential Scan & Cartesian Product Join

### Hint Level 1 (Nudge)
When you join both `tasks` (e.g. 5 rows) and `comments` (e.g. 10 rows) onto `users` directly in the same query, the relational engine creates 50 rows (5 * 10). `COUNT(t.id)` will count 50 instead of 5!

### Hint Level 2 (Concept Name)
Use CTEs or subqueries to calculate the aggregates for tasks and comments independently before joining to users: `WITH task_counts AS (...), comment_counts AS (...)`.

### Hint Level 3 (Direction)
Create indexes on the foreign key columns:
```sql
CREATE INDEX idx_users_created_at ON users(created_at);
CREATE INDEX idx_tasks_user_id ON tasks(user_id);
CREATE INDEX idx_comments_user_id ON comments(user_id);
```
And restructure the query:
```sql
WITH task_stats AS (
    SELECT user_id, COUNT(*) AS total_tasks FROM tasks GROUP BY user_id
),
comment_stats AS (
    SELECT user_id, COUNT(*) AS total_comments FROM comments GROUP BY user_id
)
SELECT u.id, u.email, 
       COALESCE(ts.total_tasks, 0) AS total_tasks,
       COALESCE(cs.total_comments, 0) AS total_comments
FROM users u
LEFT JOIN task_stats ts ON ts.user_id = u.id
LEFT JOIN comment_stats cs ON cs.user_id = u.id
WHERE u.created_at >= '2026-01-01';
```

---

## Exercise 6.3: Complex Analytical Queries with Window Functions and CTEs

### Hint Level 1 (Nudge)
A window function performs a calculation across a set of table rows that are somehow related to the current row without collapsing the rows into a single group like `GROUP BY`.

### Hint Level 2 (Concept Name)
Use `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW` inside the `OVER` clause to calculate the 7-day moving average.

### Hint Level 3 (Direction)
Ranking example:
```sql
SELECT 
    project_id, user_id, completion_days,
    DENSE_RANK() OVER (PARTITION BY project_id ORDER BY completion_days ASC) as rank
FROM task_completion_metrics;
```
