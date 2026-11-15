# Phase 2 Comprehensive Exam: Web Architecture, Relational Data & Production Backend

- **Scope:** Weeks 04–08 (Web protocols, React component architecture, PostgreSQL normalization & indexing, FastAPI async event loop, SQLAlchemy 2.0, Alembic, and JWT authentication)
- **Time Allocated:** 3 Hours (180 minutes)
- **Passing Threshold:** 70% overall, and **Part B must be passed on its own**.
- **Rules:** No AI assistance. Official Python, FastAPI, PostgreSQL, and React documentation permitted. Answer keys are retained by your learning partner.

---

## Part A: Conceptual Depth (30% - 45 Minutes)

Answer each question in 3 to 5 clear sentences.

1. **HTTP/2 Multiplexing vs HTTP/1.1 Pipelining:** How does binary framing in HTTP/2 resolve Head-of-Line (HoL) blocking at the application layer compared to HTTP/1.1 persistent connections, and why can HoL blocking still occur at the transport layer (TCP)?
2. **React Reconciliation & Virtual DOM:** Describe how React's diffing algorithm utilizes `key` props when reconciling list updates. What performance bug occurs if array indexes are supplied as keys in dynamic lists?
3. **Database Normalization Trade-offs:** What specific anomaly does Third Normal Form (3NF) eliminate, and under what high-scale analytical conditions is intentional denormalization justified?
4. **B-Tree Indexing & Query Planners:** Explain why the PostgreSQL query planner might opt for a sequential scan over an index scan even when a B-Tree index exists on the filtered column.
5. **FastAPI Event Loop Starvation:** Describe the internal consequence when a synchronous blocking network call or `time.sleep()` is invoked inside an `async def` endpoint. How should blocking calls be integrated properly?
6. **Stateless JWT Security & Token Revocation:** Explain why stateless JWTs introduce complexity when an administrator needs to immediately revoke a compromised user session. What architectural patterns solve this trade-off?

---

## Part B: Practical Timed Engineering Task (50% - 90 Minutes)

> **Scenario:** You are building an internal transactional billing credit service for a team. The service must support atomic balance transfers between accounts with balance checks, database transactions, concurrency locking, and audit logging.

### Requirements:
1. **Data Model:**
   - Account: `id` (int/UUID), `owner_email` (str), `balance_cents` (int, non-negative `CHECK (balance_cents >= 0)`).
   - TransferAudit: `id`, `source_account_id`, `destination_account_id`, `amount_cents`, `timestamp`.
2. **Transfer Endpoint (`POST /transfers`):**
   - Accept: `source_account_id`, `destination_account_id`, `amount_cents`.
   - Validate that `amount_cents > 0` and `source_account_id != destination_account_id`.
   - Execute the transfer inside an atomic database transaction.
   - Prevent race conditions (e.g. double spending) using row-level locking (`SELECT ... FOR UPDATE` or strict atomic `UPDATE` arithmetic).
   - If `source_account` has insufficient balance, abort with `400 Bad Request` and roll back transaction.
   - Record an immutable entry in `TransferAudit`.
   - Return `201 Created` with transfer details and updated source balance.
3. **Security & Authentication:**
   - Endpoint must require valid JWT Bearer authentication.
   - Verify that the authenticated caller owns the `source_account_id` (prevent IDOR).
4. **Tests:**
   - Write pytest tests asserting:
     - Successful transfer updates both balances and creates audit entry.
     - Insufficient balance returns 400 and modifies neither account.
     - Unauthenticated requests return 401.
     - Unauthorized requests (transferring from someone else's account) return 404/403.
     - Concurrent transfer attempts are handled safely without negative balances.

---

## Part C: Technical Defense & Socratic Interview (20% - 30 Minutes)

During the partner sync, walk through your implementation. You will defend your code and answer these two live questions:

1. *"Under a flash sale spike with 1,000 concurrent transfers per second targeting the same popular merchant account, what database bottlenecks will emerge with row-level locking, and how would you redesign the ledger to scale horizontally?"*
2. *"If a downstream microservice requires notifications whenever a transfer completes, why is publishing to a message broker (RabbitMQ/Kafka) inside the database transaction dangerous, and how does the Transactional Outbox pattern solve this?"*
