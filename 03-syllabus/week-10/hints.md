- **Silver Task 1 Hint – Level 1**: Use `useEffect` to start the fetch when the component mounts.
- **Silver Task 1 Hint – Level 2**: Check `response.ok` and call `response.json()` before updating state.
- **Silver Task 1 Hint – Level 3**: Render a spinner while `loading` is true and an error message if `error` is set.

- **Silver Task 2 Hint – Level 1**: Create `useState` entries for each input and bind them via `value` and `onChange`.
- **Silver Task 2 Hint – Level 2**: Validate fields on submit; if any are empty, set an error state.
- **Silver Task 2 Hint – Level 3**: Show each error directly under its input element with appropriate ARIA attributes.

- **Gold Task Hint – Level 1**: Define a FastAPI route with a Pydantic model for the request body.
- **Gold Task Hint – Level 2**: In React, `fetch` with `method:"POST"`, `headers:{"Content-Type":"application/json"}`, and `body:JSON.stringify(data)`.
- **Gold Task Hint – Level 3**: After the response, display a toast or banner indicating success or error based on the HTTP status.
