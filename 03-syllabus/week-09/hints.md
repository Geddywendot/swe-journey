- **Silver Task 1 Hint – Level 1**: Start by defining a Pydantic model for an item with `name` and `description` fields.
- **Silver Task 1 Hint – Level 2**: Use FastAPI's `@app.get` decorator and return `List[Item]`.
- **Silver Task 1 Hint – Level 3**: Ensure the endpoint returns `items` as JSON with the correct status code; no extra logic needed.

- **Silver Task 2 Hint – Level 1**: Use `useEffect` to trigger a fetch when the component mounts.
- **Silver Task 2 Hint – Level 2**: Map the returned JSON array to JSX elements displaying `name` and `description`.
- **Silver Task 2 Hint – Level 3**: Add a loading state and an error catch block; render appropriate UI.

- **Gold Task Hint – Level 1**: Store the API key in a `.env` file and read it via `process.env`.
- **Gold Task Hint – Level 2**: In FastAPI, read the key from `os.getenv` and compare it to a request header.
- **Gold Task Hint – Level 3**: Return `401 Unauthorized` if the header does not match; update the React fetch to include `Authorization` header.
