# Quiz 03

Test your understanding of command line interface standards, test fixtures, and mock isolation. Record your answers before consulting your learning partner.

1. In Unix and POSIX operating systems, what is the standard meaning of an exit status of 0?
   a) The program timed out.  
   b) The program executed successfully with no errors.  
   c) The program was aborted with SIGINT.  
   d) The program produced zero bytes of output.  
   *(Answer key: `instructor-keys/quiz-03.md`)*

2. Why should tests never share mutable global state across different test functions?
   a) Python raises a `GlobalStateError` on second invocation.  
   b) It introduces test order dependency, causing tests to pass or fail depending on execution sequence.  
   c) Pytest cannot measure line coverage on global variables.  
   d) Operating systems restrict memory access after the first test.  
   *(Answer key: `instructor-keys/quiz-03.md`)*

3. What is the execution lifecycle of a pytest fixture that uses `yield`?
   a) Code before `yield` runs before the test (setup); code after `yield` runs after the test finishes (teardown).  
   b) The fixture runs continuously in a background thread.  
   c) `yield` converts the test into an asynchronous coroutine.  
   d) Pytest disables teardown if the test fails.  
   *(Answer key: `instructor-keys/quiz-03.md`)*

4. When should you use `@pytest.mark.parametrize`?
   a) When you want to run tests across multiple operating systems simultaneously.  
   b) When you want to execute the same test logic against multiple distinct input sets and expected outputs.  
   c) When you want to mock external API network calls.  
   d) When you need to increase test execution priority.  
   *(Answer key: `instructor-keys/quiz-03.md`)*

5. What does the built-in pytest fixture `tmp_path` provide?
   a) A string pointing to `/tmp`.  
   b) A unique, temporary `pathlib.Path` directory object created specifically for the test invocation and cleaned up automatically.  
   c) A mock RAM disk in kernel space.  
   d) A database transaction rollback pointer.  
   *(Answer key: `instructor-keys/quiz-03.md`)*

6. Why is mocking internal implementation details (private methods) considered an anti-pattern in unit testing?
   a) Python prevents access to methods prefixed with `_`.  
   b) It ties tests tightly to internal refactorings, causing tests to break even when public behavior remains completely intact.  
   c) Mocks slow down CPU cache performance.  
   d) Mocking private methods requires third-party C extensions.  
   *(Answer key: `instructor-keys/quiz-03.md`)*

7. What happens when a user runs a CLI command and redirects standard output to a file (`app > out.txt`), but the app prints errors to `sys.stdout` instead of `sys.stderr`?
   a) The operating system raises an I/O error.  
   b) The error messages are written into the output file, polluting the generated data and hiding the error from the terminal user.  
   c) The terminal automatically beeps.  
   d) The file is deleted on exit.  
   *(Answer key: `instructor-keys/quiz-03.md`)*

8. What is the primary difference between a unit test and an integration test?
   a) Unit tests are written in Python; integration tests are written in Bash.  
   b) Unit tests verify small, isolated components in memory without external dependencies; integration tests verify that multiple components, databases, or systems work correctly together.  
   c) Unit tests only run in CI/CD environments.  
   d) Integration tests cannot use assertions.  
   *(Answer key: `instructor-keys/quiz-03.md`)*
