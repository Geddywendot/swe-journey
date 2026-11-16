## Quiz

1. What is the main benefit of using a controlled component for form inputs in React?
   a) Simpler HTML markup
   b) Automatic server validation
   c) Full control over the input value and validation logic
   d) Faster rendering performance

2. Which React feature allows you to show a fallback UI when a component throws an error during rendering?
   a) Suspense
   b) Error Boundary
   c) Lazy Loading
   d) Context API

3. When performing an optimistic UI update, what should you do if the server later returns an error?
   a) Keep the UI unchanged
   b) Reload the entire page
   c) Roll back the optimistic change and display an error message
   d) Ignore the error

4. In FastAPI, which of the following automatically validates incoming request bodies?
   a) SQLAlchemy models
   b) Pydantic models
   c) Marshmallow schemas
   d) Plain dictionaries

5. What HTTP status code does FastAPI return for a validation error produced by Pydantic?
   a) 400 Bad Request
   b) 401 Unauthorized
   c) 403 Forbidden
   d) 422 Unprocessable Entity

6. Which loading UI pattern is most appropriate when you only need to indicate that a list is being fetched?
   a) Full‑page skeleton screen
   b) Inline spinner next to the list header
   c) Modal dialog blocking the UI
   d) Toast notification

7. How can you simulate a network failure to test error handling in the front‑end?
   a) Change the HTTP method to GET
   b) Stop the FastAPI container or use an invalid URL
   c) Increase the fetch timeout
   d) Disable CORS in the browser

8. In a React form, where should you place the logic that disables the submit button until all required fields are valid?
   a) Inside the JSX markup
   b) In the `onSubmit` handler
   c) In a `useEffect` that watches input state
   d) In the CSS style rules
