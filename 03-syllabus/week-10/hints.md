## Hints

**Silver 1**
- *Level 1*: The form should collect `name` and `quantity` and call `fetch('/items', {method:'POST',body:JSON.stringify({name,quantity})})`.
- *Level 2*: Use `useState` for each input and disable the submit button while any field is empty.
- *Level 3*: After a successful POST, call `setItems(prev=>[...prev, newItem])` and show a toast with a library like `react-hot-toast`.

**Silver 2**
- *Level 1*: Wrap the fetch call with a `loading` boolean state and render a spinner component when true.
- *Level 2*: Catch fetch errors (`catch(err => setError(err.message))`) and display an alert component with the error text.
- *Level 3*: Create an `ErrorBoundary` component that uses `componentDidCatch` (class) or the `react-error-boundary` package to render a fallback UI.

**Gold**
- *Level 1*: Optimistically push the new item into `items` state before awaiting the response.
- *Level 2*: Define a Pydantic model `class ItemCreate(BaseModel): name: str; quantity: conint(gt=0)` in FastAPI.
- *Level 3*: Write a pytest test using `client.post('/items', json={'name':'', 'quantity':-1})` and assert `response.status_code == 422`; ensure the front‑end displays the validation error message.
