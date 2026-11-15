# Week 04 Hints

> **Rule:** Attempt the exercise for at least 30 minutes before reading Hint 1. Wait an additional 15 minutes before reading Hint 2 or 3.

---

## Exercise 4.1: Inspecting and Replaying HTTP Requests with `curl`

### Hint Level 1 (Nudge)
Use `-X POST` to change the HTTP method, `-H` to set headers, and `-d` to provide the request body payload.

### Hint Level 2 (Concept Name)
To inspect the complete request and response headers along with TLS negotiation, pass the `-v` (verbose) or `-i` (include headers in output) flag.

### Hint Level 3 (Direction)
Syntax example:
```bash
curl -v -X POST "https://httpbin.org/post" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer test_token" \
  -d '{"name": "test", "active": true}'
```

---

## Exercise 4.2: Debug This — Resolving Blocked CORS Requests

### Hint Level 1 (Nudge)
The browser makes two requests when a request contains custom headers or methods like `POST` with `application/json`: an initial `OPTIONS` request (preflight), followed by the actual request.

### Hint Level 2 (Concept Name)
You must set `self.send_header('Access-Control-Allow-Origin', 'http://localhost:3000')` (or `'*'`) on both the `OPTIONS` response and all data responses.

### Hint Level 3 (Direction)
Add a `do_OPTIONS(self)` method to `BrokenHandler`:
```python
def do_OPTIONS(self):
  self.send_response(204)
  self.send_header("Access-Control-Allow-Origin", "*")
  self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
  self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
  self.end_headers()
```
And ensure `Access-Control-Allow-Origin` is also sent in `do_GET` and `do_POST`.

---

## Exercise 4.3: Responsive Dashboard Card with Semantic HTML & Flexbox/Grid

### Hint Level 1 (Nudge)
Use `box-sizing: border-box;` globally in CSS to ensure padding does not unexpectedly expand element widths.

### Hint Level 2 (Concept Name)
For the metric cards container, use `display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;`.

### Hint Level 3 (Direction)
For each card's internal layout, use Flexbox: `display: flex; flex-direction: column; justify-content: space-between;`. This aligns title, metric value, and footer elements consistently across cards of varying heights.
