# Quiz 06

Test your understanding of relational database normalization, indexing, and transactions. Record your answers before checking with your learning partner.

1. What is the core requirement of Third Normal Form (3NF)?
   a) Every column must be an integer.  
   b) The table must be in 2NF and have no transitive dependencies (every non-key attribute must depend directly on the primary key, and nothing but the primary key).  
   c) The table must contain fewer than 10 columns.  
   d) All queries must use B-Tree indexes.  
   *(Answer key: `instructor-keys/quiz-06.md`)*

2. Why does joining two independent one-to-many child tables (`tasks` and `comments`) directly onto a parent table (`users`) in a single query produce incorrect `COUNT()` totals?
   a) PostgreSQL syntax forbids multiple joins.  
   b) It produces a Cartesian product (cross-multiplication) of matching rows, multiplying the count of each child table by the count of the other.  
   c) Joins automatically truncate rows.  
   d) Foreign keys cannot be traversed simultaneously.  
   *(Answer key: `instructor-keys/quiz-06.md`)*

3. In an `EXPLAIN ANALYZE` query plan, what does a `Seq Scan` node indicate?
   a) An index lookup completed in sequential order.  
   b) The database engine scanned every single disk page and row in the table from start to finish because no suitable index was available or selected.  
   c) A memory buffer cache hit.  
   d) An encrypted disk read.  
   *(Answer key: `instructor-keys/quiz-06.md`)*

4. What is the fundamental difference between `ON DELETE CASCADE` and `ON DELETE RESTRICT`?
   a) `CASCADE` deletes child records automatically when the parent is deleted; `RESTRICT` aborts the deletion if any child records reference the parent.  
   b) `CASCADE` requires root database permissions.  
   c) `RESTRICT` deletes records after 30 days.  
   d) Both behave identically in PostgreSQL.  
   *(Answer key: `instructor-keys/quiz-06.md`)*

5. Under the standard `Read Committed` transaction isolation level in PostgreSQL, what guarantees are provided?
   a) Each query within the transaction sees only data committed before that query began; dirty reads of uncommitted data are prohibited.  
   b) All transactions run strictly one-by-one on a single CPU core.  
   c) Writes are never persisted to disk until the database restarts.  
   d) Queries can see uncommitted updates from other active sessions.  
   *(Answer key: `instructor-keys/quiz-06.md`)*

6. What is a PostgreSQL `TIMESTAMPTZ` column type?
   a) An unformatted string containing local clock time.  
   b) A timestamp stored internally in UTC that converts to the client session's timezone on retrieval.  
   c) A Unix millisecond timestamp stored as a 32-bit integer.  
   d) A deprecated data type replaced by `BIGINT`.  
   *(Answer key: `instructor-keys/quiz-06.md`)*

7. When is a database B-Tree index NOT chosen by the PostgreSQL query planner even if the index exists on the filtered column?
   a) When the table is larger than 1 gigabyte.  
   b) When the planner estimates that the query will match a very large percentage of rows (e.g. > 20-30%), making a sequential scan faster than random index page lookups.  
   c) When foreign keys are enabled.  
   d) When `SELECT *` is used.  
   *(Answer key: `instructor-keys/quiz-06.md`)*

8. What is the primary purpose of a database connection pool?
   a) To store query results in RAM permanently.  
   b) To reuse pre-established TCP database connections, eliminating the high latency and CPU overhead of repeatedly creating and tearing down database processes.  
   c) To encrypt data stored on disk.  
   d) To replace SQL queries with JSON.  
   *(Answer key: `instructor-keys/quiz-06.md`)*
