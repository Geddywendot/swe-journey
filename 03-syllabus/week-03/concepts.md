# Week 03 Concepts

Master these 6 CLI and testing principles. For each concept, practice explaining it aloud in your own words.

---

### 1. Test-Driven Development (Red-Green-Refactor)
- **Plain words:** Write a failing test defining the desired behavior before writing any implementation code (Red). Write the simplest possible code to pass the test (Green). Then clean up the architecture while maintaining passing tests (Refactor). This ensures testability and prevents writing dead code.
- **Explain it back prompt:** *"Why is it crucial that a test fails before you implement the solution?"*

### 2. Pytest Fixture Lifecycle & Dependency Injection
- **Plain words:** A pytest fixture is a setup function that runs before a test to provide test data, temporary directories, or open mock connections. Using `yield` inside a fixture allows cleanup code to run automatically after the test finishes, regardless of whether the test passed or failed.
- **Explain it back prompt:** *"What is the difference between `scope='function'` and `scope='session'` in pytest fixtures?"*

### 3. Test Parameterization (`@pytest.mark.parametrize`)
- **Plain words:** Instead of copying and pasting the same test function five times with different inputs, parameterization runs the exact same test body across a table of input-output tuples. Each scenario is treated as an independent test case with its own report.
- **Explain it back prompt:** *"How does parameterization improve the signal when 1 out of 10 edge cases fails?"*

### 4. POSIX CLI Exit Codes & Conventions
- **Plain words:** When a program finishes, it returns an integer exit code (0–255) to the operating system. An exit code of `0` means success. Any non-zero code (`1`, `2`, `127`) indicates an error. Automated pipelines rely entirely on exit codes to know whether a step succeeded.
- **Explain it back prompt:** *"What standard exit code does a Unix tool return for invalid command-line flags versus a runtime execution error?"*

### 5. Mocking Boundaries vs. Mocking Implementation
- **Plain words:** Tests should mock external boundary dependencies (network requests, third-party APIs, disk filesystem access) to ensure tests run fast and deterministically. Never mock internal pure functions or private helper methods; test through the public interface.
- **Explain it back prompt:** *"Why do over-mocked tests give a false sense of security while breaking during trivial refactors?"*

### 6. Standard Streams in CLI Design
- **Plain words:** A well-behaved CLI writes its requested data or results to `stdout` and writes status messages, progress spinners, and error alerts to `stderr`. This allows users to redirect data into a file or another tool without corrupting it with logs.
- **Explain it back prompt:** *"What happens if your CLI writes 'Processing finished!' to `stdout` when a user pipes its output into `jq`?"*
