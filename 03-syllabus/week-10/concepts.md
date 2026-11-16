- **Concept 1 – Fetch API Basics**: The Fetch API returns a Promise that resolves to a Response object. You must call `.json()` or similar to extract the payload. Proper error handling includes checking `response.ok` and catching network errors.
  **Explain it back**: What steps are needed to safely retrieve JSON data using fetch?

- **Concept 2 – Controlled Components**: In React, form inputs derive their value from component state via the `value` prop and update state via `onChange`. This pattern ensures the UI reflects the source of truth.
  **Explain it back**: How does a controlled input keep the UI and state synchronized?

- **Concept 3 – Validation Hook**: A custom hook can encapsulate validation logic, returning error messages and a `validate` function. It enables reusability across multiple forms.
  **Explain it back**: What benefits does a custom validation hook provide?

- **Concept 4 – POST Request Handling**: Submitting form data typically uses `fetch` with method `POST` and a JSON body. The server must parse the body and return appropriate status codes.
  **Explain it back**: Which request options are required to send JSON data in a POST?

- **Concept 5 – Accessibility in Forms**: Proper labeling with `<label>` elements linked via `htmlFor`, and using ARIA attributes for error messages, ensures screen readers convey the form structure.
  **Explain it back**: How do you associate a label with an input for accessibility?
