# Week 04 Concepts

Master these 6 web architecture concepts. For each concept, practice explaining it aloud in your own words.

---

### 1. The HTTP Request/Response Lifecycle
- **Plain words:** HTTP is an application-layer protocol built over TCP/IP. A client sends a plain-text request consisting of a method (`GET`, `POST`), target path (`/api/users`), headers (`Content-Type`, `Authorization`), and an optional body. The server processes the request and responds with a numeric status code (`200 OK`, `404 Not Found`), response headers, and payload data.
- **Explain it back prompt:** *"Trace what happens from the moment a browser sends a request to the moment the response is rendered."*

### 2. HTTP Statelessness & Session State
- **Plain words:** The HTTP protocol itself has no memory; each request is handled completely independently without reference to previous requests. To maintain user identity or session state across requests, servers and clients use explicit tokens passed via HTTP headers or `Set-Cookie` directives.
- **Explain it back prompt:** *"Why does HTTP being stateless make horizontal scaling easier for web backend servers?"*

### 3. Cross-Origin Resource Sharing (CORS)
- **Plain words:** By default, browsers enforce the Same-Origin Policy, preventing JavaScript on `site-a.com` from reading data fetched from `api.site-b.com`. CORS is a server-side handshake that tells the browser which origins, HTTP methods, and headers are permitted to access the resource.
- **Explain it back prompt:** *"What is an `OPTIONS` preflight request, and why does the browser send it before your `POST` request?"*

### 4. The Document Object Model (DOM) Tree
- **Plain words:** When a browser downloads an HTML document, it parses the markup into an in-memory tree of node objects called the DOM. JavaScript does not manipulate HTML text directly; it interacts with this living object model via browser APIs (`document.getElementById`, `addEventListener`).
- **Explain it back prompt:** *"Why are frequent, uncontrolled direct DOM mutations expensive for browser rendering engines?"*

### 5. The CSS Box Model & Modern Layout (Flexbox vs. Grid)
- **Plain words:** Every visual element on a webpage is a rectangular box made of content, padding, border, and margin (`box-sizing: border-box`). **Flexbox** handles one-dimensional layouts (a single row or column), while **CSS Grid** is designed for two-dimensional layouts (simultaneous rows and columns).
- **Explain it back prompt:** *"When would you choose CSS Grid over Flexbox for a page layout?"*

### 6. Semantic HTML & Accessibility (a11y)
- **Plain words:** Using meaningful HTML tags (`<header>`, `<nav>`, `<main>`, `<article>`, `<button>`) instead of generic `<div>` tags conveys structural meaning to search engines and assistive technologies (like screen readers). It also provides built-in keyboard navigation and focus management.
- **Explain it back prompt:** *"Why should a clickable UI element always be a `<button>` rather than a `<div onClick={...}>`?"*
