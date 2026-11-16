- **Concept 1 – Testing Pyramid Overview**: The testing pyramid visualizes test distribution: many fast unit tests at the base, fewer integration/component tests in the middle, and a handful of slow end‑to‑end tests at the top. This structure balances confidence and feedback speed.
  **Explain it back**: Why are unit tests more numerous than e2e tests?

- **Concept 2 – Unit Tests with Vitest**: Vitest runs in the Vite ecosystem, offering fast hot‑module reloading and native ESM support. Tests focus on isolated functions, using mocks to replace dependencies.
  **Explain it back**: What advantage does mocking give in unit tests?

- **Concept 3 – Component Tests with React Testing Library**: RTL encourages testing the component from a user’s perspective, querying by role or text rather than implementation details, leading to more robust UI tests.
  **Explain it back**: How does RTL differ from shallow rendering?

- **Concept 4 – End‑to‑End Tests Basics**: E2E tests drive the whole application in a real browser, verifying critical user flows. They are slower and more fragile, so they should cover only essential paths.
  **Explain it back**: What makes an E2E test flaky and how can you reduce flakiness?

- **Concept 5 – Test Coverage and CI Integration**: Generating coverage reports helps identify untested code. Integrating tests into CI ensures every commit is validated.
  **Explain it back**: Why is it important to enforce a coverage threshold in CI?
