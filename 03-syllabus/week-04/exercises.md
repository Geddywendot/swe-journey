# Week 04 Exercises

Complete all Silver exercises to pass the week. Gold exercises are optional stretch challenges.

---

## Exercise 4.1: Inspecting and Replaying HTTP Requests with `curl`

**Type:** silver  
**Time box:** 60–90 min  
**Task:** Use `curl` to interact with a public JSON API (such as `https://httpbin.org` or GitHub API). Craft requests demonstrating `GET`, `POST` with JSON payload, custom request headers (`Authorization`, `Accept`, `User-Agent`), inspecting response status codes and response headers.

**Acceptance criteria:**
- [ ] Save shell commands in `scripts/curl_recipes.sh` with full comments.
- [ ] Perform a `POST` request sending JSON `{"name": "test", "active": true}` and assert that `Content-Type: application/json` is sent.
- [ ] Use `curl -v` or `curl -I` to capture and explain response headers (`Content-Type`, `Date`, `Cache-Control`).
- [ ] Inspect HTTP status codes (`200`, `201`, `400`, `404`) returned by the endpoint.

**Rules:** AI off. Use command-line `curl` only.  
**Hints:** See `hints.md` section 4.1

---

## Exercise 4.2: Debug This — Resolving Blocked CORS Requests

**Type:** silver ("debug this")  
**Time box:** 60–90 min  
**Task:** A frontend application running on `http://localhost:3000` attempts to fetch data from an API on `http://localhost:8000`, but requests fail in the browser console with:  
`Access to fetch at 'http://localhost:8000/api/data' from origin 'http://localhost:3000' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.`

Here is the server configuration causing the issue:
```python
# server.py (broken server mock)
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class BrokenHandler(BaseHTTPRequestHandler):

  def do_GET(self):
    # Bug: Missing Access-Control-Allow-Origin header
    self.send_response(200)
    self.send_header("Content-Type", "application/json")
    self.end_headers()
    self.wfile.write(json.dumps({"message": "Hello World"}).encode())

  def do_POST(self):
    # Bug: Rejects preflight OPTIONS requests or custom headers
    self.send_response(200)
    self.end_headers()
    self.wfile.write(b'{"status": "created"}')
```

**Acceptance criteria:**
- [ ] Implement `do_OPTIONS` to handle browser preflight checks.
- [ ] Return the required CORS headers: `Access-Control-Allow-Origin`, `Access-Control-Allow-Methods`, and `Access-Control-Allow-Headers`.
- [ ] Demonstrate a successful browser `fetch()` call across origins without console errors.

**Rules:** Do not use browser extensions that disable CORS. Fix the server headers.  
**Hints:** See `hints.md` section 4.2

---

## Exercise 4.3: Responsive Dashboard Card with Semantic HTML & Flexbox/Grid

**Type:** silver  
**Time box:** 60–90 min  
**Task:** Create an accessible, responsive dashboard layout in `index.html` and `styles.css` containing a navigation bar, a metrics summary section (3 stats cards using CSS Grid), and a responsive tabular list that switches to a stacked card layout on mobile viewports.

**Acceptance criteria:**
- [ ] 100% semantic HTML (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`).
- [ ] CSS Grid used for the multi-column metric card grid.
- [ ] Flexbox used for navigation alignment and card internals.
- [ ] Fully responsive with CSS media queries (`@media (max-width: 768px)`).
- [ ] WCAG AA compliant color contrast and visible `:focus-visible` outlines.

**Rules:** AI off. No CSS frameworks (no Tailwind, Bootstrap). Raw CSS only.  
**Hints:** See `hints.md` section 4.3

---

## Exercise 4.4: Raw Low-Level HTTP/1.1 Socket Client in Python

**Type:** gold (stretch)  
**Time box:** 120–180 min  
**Task:** Build a functional HTTP/1.1 client using only Python's low-level `socket` library (no `urllib`, `requests`, or `httpx`). Your client must open a TCP connection to port 80 (or 443 with `ssl`), construct the raw HTTP request string, send the bytes, read the response stream, parse status line and headers, and handle chunked transfer encoding (`Transfer-Encoding: chunked`).

**Acceptance criteria:**
- [ ] Opens socket and sends RFC 9112 compliant request string with `Host` header.
- [ ] Parses status line, headers dictionary, and body bytes.
- [ ] Correctly reassembles chunked transfer encoding streams.
- [ ] Passes pytest asserting correct body extraction from test HTTP server.

**Rules:** No hints provided for gold stretch exercises.
