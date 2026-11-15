# Week 06 Concepts

Master these 6 relational database fundamentals. For each concept, practice explaining it aloud in your own words.

---

### 1. Relational Normalization (1NF, 2NF, 3NF)
- **Plain words:** Normalization structures database tables to eliminate duplicate data and prevent update anomalies. **1NF** enforces atomic values (no lists in cells). **2NF** removes partial dependencies on composite keys. **3NF** removes transitive dependencies (non-key columns depending on other non-key columns).
- **Explain it back prompt:** *"Why does storing comma-separated tags in a single string column violate 1NF, and what anomalies occur when querying or updating it?"*

### 2. Constraints & Referential Integrity
- **Plain words:** The database is the ultimate authority on data integrity. `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`, and `CHECK` constraints guarantee invalid data cannot be saved, even if application code contains bugs. Foreign key cascade options (`ON DELETE CASCADE` vs `ON DELETE RESTRICT`) dictate child record behavior when parent rows are deleted.
- **Explain it back prompt:** *"What is the difference between `ON DELETE CASCADE` and `ON DELETE SET NULL`, and when is cascading deletion dangerous?"*

### 3. B-Tree Indexing & Query Execution Plans (`EXPLAIN ANALYZE`)
- **Plain words:** Without an index, finding a single row requires a sequential scan of every page on disk ($O(N)$). A B-Tree index maintains a balanced search tree of sorted column values pointing to row pointers (TIDs), enabling lookups in $O(\log N)$ time. `EXPLAIN ANALYZE` executes the query and reports actual disk page hits, index scans, and timing bottlenecks.
- **Explain it back prompt:** *"Why can adding too many indexes to a table significantly degrade write (`INSERT`/`UPDATE`) performance?"*

### 4. ACID Guarantees & Transaction Isolation Levels
- **Plain words:** Transactions bundle multiple SQL statements into an all-or-nothing unit (**Atomicity**). PostgreSQL supports isolation levels: *Read Committed* (default: queries see only committed data), *Repeatable Read* (queries see a snapshot from transaction start), and *Serializable* (guarantees results match some sequential execution).
- **Explain it back prompt:** *"What is a 'phantom read' and which transaction isolation level prevents it?"*

### 5. Joins, Common Table Expressions (CTEs), and Subqueries
- **Plain words:** Relational queries link tables together. `INNER JOIN` matches rows in both tables; `LEFT JOIN` preserves all rows from the left table; `FULL OUTER JOIN` preserves all rows. CTEs (`WITH ... AS (...)`) break complex nested queries into readable, reusable logical steps.
- **Explain it back prompt:** *"What is the difference between an `INNER JOIN` and a `LEFT OUTER JOIN` when a child record does not exist?"*

### 6. Connection Pooling & Database Sockets
- **Plain words:** Establishing a PostgreSQL connection requires a TCP handshake, TLS negotiation, authentication, and fork/process allocation on the server, which can take tens of milliseconds. A connection pool maintains an active pool of open connections, allowing web requests to borrow and return connections in sub-millisecond time.
- **Explain it back prompt:** *"What happens to an API server if incoming traffic spikes and connection pooling is unconfigured or misconfigured?"*
