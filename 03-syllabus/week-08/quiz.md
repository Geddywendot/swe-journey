# Quiz 08

Test your understanding of SQLAlchemy 2.0 async, Alembic migrations, password hashing, and JWT tokens. Record your answers before checking with your learning partner.

1. Why does accessing an un-loaded relationship property (e.g. `user.tasks`) on an asynchronous SQLAlchemy model instance trigger a `MissingGreenlet` exception?
   a) Python does not support object relationships.  
   b) In async mode, SQLAlchemy disables synchronous lazy loading because transparent I/O would block the asyncio event loop; relationships must be explicitly eagerly loaded.  
   c) The database tables were created without foreign keys.  
   d) Greenlet is an obsolete library removed from Linux.  
   *(Answer key: `instructor-keys/quiz-08.md`)*

2. Why should fast cryptographic hashes like MD5, SHA-1, or SHA-256 never be used directly for storing user passwords?
   a) They generate strings that are too long for database columns.  
   b) Modern GPUs can compute billions of SHA-256 hashes per second, allowing attackers to crack password databases rapidly with precomputed rainbow tables or brute force; adaptive algorithms like bcrypt or Argon2 are designed to be intentionally slow.  
   c) They cannot handle Unicode characters.  
   d) They require paid commercial licensing.  
   *(Answer key: `instructor-keys/quiz-08.md`)*

3. What are the three period-separated parts of a standard JSON Web Token (JWT)?
   a) Username, Password, Timestamp  
   b) Header, Payload, Signature  
   c) Hostname, Protocol, Port  
   d) Public Key, Private Key, Ciphertext  
   *(Answer key: `instructor-keys/quiz-08.md`)*

4. How does Alembic track which database migrations have already been executed against a target database?
   a) By storing text files in the operating system's `/tmp` directory.  
   b) By querying a dedicated table called `alembic_version` inside the database, which contains the revision hash of the current schema state.  
   c) By inspecting the git commit log of the repository.  
   d) By pinging a central cloud server.  
   *(Answer key: `instructor-keys/quiz-08.md`)*

5. What is the fundamental difference between `selectinload` and `joinedload` strategies in SQLAlchemy when loading one-to-many relationships?
   a) `selectinload` executes a second query using an `IN (...)` clause of parent primary keys; `joinedload` executes an SQL `LEFT OUTER JOIN` in a single query (which can multiply rows for collections).  
   b) `joinedload` only works on SQLite.  
   c) `selectinload` is deprecated in SQLAlchemy 2.0.  
   d) There is no difference.  
   *(Answer key: `instructor-keys/quiz-08.md`)*

6. When designing a multi-tenant or multi-user API, why is returning `404 Not Found` preferable to `403 Forbidden` when a user attempts to access another user's private resource (e.g., `GET /tasks/999`)?
   a) Returning `404` saves server memory.  
   b) Returning `403` reveals that a resource with ID 999 exists in the system (information leakage / IDOR enumeration); `404` behaves identically whether the resource does not exist or does not belong to the caller.  
   c) `403 Forbidden` is invalid in REST APIs.  
   d) `404` allows automatic client retries.  
   *(Answer key: `instructor-keys/quiz-08.md`)*

7. What is the purpose of adding a random "salt" to a password before hashing it with bcrypt or Argon2?
   a) To make the password easier to decrypt by the administrator.  
   b) To ensure that two users with identical passwords produce completely different hash outputs, rendering precomputed lookup tables (rainbow tables) useless.  
   c) To compress the password length.  
   d) To comply with GDPR cookie regulations.  
   *(Answer key: `instructor-keys/quiz-08.md`)*

8. In a stateless JWT architecture, why is it recommended to keep access token lifetimes short (e.g., 15–30 minutes)?
   a) To reduce CPU usage during token verification.  
   b) Because stateless JWTs cannot be revoked without maintaining a server-side denylist/cache; short expiration minimizes the window of opportunity if a token is stolen.  
   c) Because browsers delete cookies after 15 minutes.  
   d) Because JWT payloads can only hold 15 minutes of clock drift.  
   *(Answer key: `instructor-keys/quiz-08.md`)*
