- **Silver Task 1**: Create a FastAPI endpoint `/items` that returns a static JSON array of item objects.
  - [ ] Endpoint returns 200 OK with correct JSON structure.
  - [ ] Includes Pydantic model for the response.

- **Silver Task 2**: Implement a React component `ItemList` that fetches `/items` and renders the list.
  - [ ] Uses `fetch` or `axios` to call the backend.
  - [ ] Displays each item's `name` and `description`.
  - [ ] Handles loading and error states.

- **Gold Task**: Secure the `/items` endpoint with an API key read from an environment variable and modify the React client to include this key in request headers.
  - [ ] FastAPI validates the API key and returns 401 for missing/invalid key.
  - [ ] React reads the API key from a `.env` variable and sends it correctly.
  - [ ] Demonstrates the full flow with protected data.
