# Engineering Glossary

A living dictionary of core software engineering terminology defined in plain English. Expand this glossary as you encounter new terms each week.

---

## Foundational Terms

### Architecture Decision Record (ADR)
A short text document capturing an architectural decision, its context, considered options, and trade-offs.

### Application Programming Interface (API)
A well-defined contract allowing two computer systems to communicate and exchange data reliably.

### ACID Properties
The four fundamental guarantees of relational databases:
- **Atomicity:** All operations in a transaction succeed, or none do.
- **Consistency:** Data remains valid according to all schema rules and constraints.
- **Isolation:** Concurrent transactions execute without interfering with each other.
- **Durability:** Once committed, changes survive system failures and power outages.

### Asynchronous I/O (`async` / `await`)
A programming pattern where a process does not wait idly for slow operations (such as disk reads or network calls) to complete, but instead releases the thread to execute other work.

### CI/CD (Continuous Integration / Continuous Delivery)
Automated practices and pipelines that test, build, and deploy code changes whenever a commit is pushed to version control.

### CORS (Cross-Origin Resource Sharing)
A browser security mechanism that restricts a web application running at one origin (domain/port) from requesting resources from a different origin unless explicitly permitted by server headers.

### Docker & Containerization
Packaging an application and all its runtime dependencies, system libraries, and configurations into a lightweight, portable container image that runs identically on any host machine.

### Idempotency
A property of an operation where executing it multiple times produces the exact same result as executing it once (e.g., HTTP `GET`, `PUT`, `DELETE`).

### JSON Web Token (JWT)
A compact, URL-safe means of representing claims between two parties. Commonly used for stateless authentication and authorization.

### Object-Relational Mapping (ORM)
A technique that lets you query and manipulate data from a database using an object-oriented programming paradigm instead of writing raw SQL strings.

### Pull Request (PR)
A formal mechanism in Git platforms (like GitHub) for proposing code changes from a feature branch into a base branch, enabling peer code review, automated testing, and discussion prior to merging.

### Standard Streams (`stdin`, `stdout`, `stderr`)
The default input and output channels provided to a program by the operating system:
- `stdin` (0): Stream from which the program reads input data.
- `stdout` (1): Stream where normal program output is written.
- `stderr` (2): Stream dedicated to diagnostic messages and error logging.

### Virtual Environment
An isolated directory tree containing a Python installation for a specific version of Python, plus a number of additional packages, preventing dependency collisions across projects.
