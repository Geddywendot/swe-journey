- **Silver Task 1**: Write a Vitest unit test for a pure function `add(a, b)` that checks correct sum and edge cases (negative numbers, zero).
  - [ ] Test file imports the function and uses `expect(...).toBe(...)`.
  - [ ] Includes a test for invalid inputs returning NaN or throwing.

- **Silver Task 2**: Create a React Testing Library test for a `Button` component that renders a label and calls an `onClick` handler.
  - [ ] Renders the button with given text.
  - [ ] Simulates a click and verifies the handler is called.
  - [ ] Checks for proper ARIA role.

- **Gold Task**: Implement a simple Cypress (or Playwright) end‑to‑end test that visits the app, fills a form, submits it, and asserts a success message appears.
  - [ ] Test launches the dev server or uses a deployed URL.
  - [ ] Interacts with input fields, selects options, and clicks submit.
  - [ ] Verifies the success notification and that the network request succeeded (status 200).
