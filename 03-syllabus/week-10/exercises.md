## Exercises

**Silver 1**
- [ ] Implement a React form that creates a new item via a POST request to `/items`.
- [ ] Validate that the name field is non‑empty before sending.
- [ ] Show a success toast when the request succeeds.

**Silver 2**
- [ ] Add a loading spinner that appears while the list of items is being fetched from the API.
- [ ] Simulate a failed fetch (e.g., stop the API) and display an error alert with the error message.
- [ ] Implement an error boundary that catches a rendering error in the item list component.

**Gold**
- [ ] Enable optimistic UI: when adding a new item, update the list immediately, then roll back if the server returns an error.
- [ ] Use a Pydantic model in FastAPI to validate the incoming item payload (e.g., name: str, quantity: int > 0).
- [ ] Write a pytest test that posts an invalid payload and asserts a 422 response, then verify the front‑end shows the validation error.
