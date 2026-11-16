- **Silver Task 1**: Build a React component `ItemList` that fetches data from a mock `/api/items` endpoint and renders each item in a list.
  - [ ] Shows a loading indicator while awaiting the response.
  - [ ] Displays an error message if the fetch fails.
  - [ ] Renders the item `name` and `description` once data is loaded.

- **Silver Task 2**: Create a controlled form `ContactForm` with at least two text inputs and a select dropdown, including client‑side validation.
  - [ ] Inputs update state on change and reflect the current value.
  - [ ] Validation prevents submission when fields are empty or invalid, showing inline error messages.
  - [ ] Shows a success message after a successful mock submit.

- **Gold Task**: Connect the `ContactForm` to a FastAPI `POST /contact` endpoint, handling both success and error responses.
  - [ ] FastAPI validates the request body and returns appropriate status codes.
  - [ ] React sends JSON with the correct headers and processes the response.
  - [ ] UI shows a distinct success or error notification based on the server reply.
