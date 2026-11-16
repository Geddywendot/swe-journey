## Exercises

**Silver 1**  
- [ ] Build a FastAPI endpoint that returns a static JSON list of items.
- [ ] In React, fetch the endpoint and display the list in a component.
- [ ] Show a loading spinner while the request is pending.

**Silver 2**  
- [ ] Add CORS middleware to FastAPI to allow requests from `http://localhost:3000`.
- [ ] Configure React to read the API URL from an environment variable.
- [ ] Verify the request succeeds without CORS errors.

**Gold**  
- [ ] Create a `.env` file for FastAPI with a secret key and load it at runtime.
- [ ] Expose the secret (e.g., an API token) to React via a separate endpoint **only** after proper authentication simulation.
- [ ] Implement error handling in React for 401/403 responses and display an appropriate message.
