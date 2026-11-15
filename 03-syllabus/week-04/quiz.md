# Quiz 04

Test your understanding of web protocols, browser security models, and layout mechanics. Record your answers before checking with your learning partner.

1. Why does an HTTP client send an `OPTIONS` request before sending a cross-origin `POST` request with a `Content-Type: application/json` header?
   a) To establish an encrypted TLS tunnel.  
   b) As a CORS preflight check to verify if the server allows cross-origin requests with that method and header before sending actual data.  
   c) To download the website's favicon.  
   d) Because HTTP/2 mandates OPTIONS for every packet.  
   *(Answer key: `instructor-keys/quiz-04.md`)*

2. What is the fundamental security guarantee provided by the browser's Same-Origin Policy (SOP)?
   a) It prevents a malicious website from reading sensitive data or session cookies from another origin inside the victim's browser.  
   b) It encrypts all network packets using AES-256.  
   c) It blocks all cross-site image and video loading.  
   d) It prevents denial-of-service attacks against backend databases.  
   *(Answer key: `instructor-keys/quiz-04.md`)*

3. What does an HTTP `401 Unauthorized` status indicate compared to a `403 Forbidden` status?
   a) `401` indicates authentication is missing or invalid (unauthenticated); `403` indicates the user is recognized but lacks permission for the resource (unauthorized).  
   b) `401` is for database errors; `403` is for frontend crashes.  
   c) `401` is temporary; `403` is permanent.  
   d) There is zero difference; both are interchangeable in the RFC specification.  
   *(Answer key: `instructor-keys/quiz-04.md`)*

4. What is the effect of setting CSS `box-sizing: border-box;` on an HTML element?
   a) It forces the element to render as a flex container.  
   b) It includes padding and border widths inside the element's total specified `width` and `height`, preventing layout overflow.  
   c) It disables all CSS margins.  
   d) It converts all text to uppercase.  
   *(Answer key: `instructor-keys/quiz-04.md`)*

5. In CSS layout architecture, what is the core structural difference between Flexbox and CSS Grid?
   a) Flexbox only works with images; Grid only works with text.  
   b) Flexbox is a 1-dimensional layout model (rows OR columns); CSS Grid is a 2-dimensional layout model (rows AND columns simultaneously).  
   c) Grid is deprecated in modern CSS.  
   d) Flexbox requires JavaScript polyfills.  
   *(Answer key: `instructor-keys/quiz-04.md`)*

6. Why is using semantic HTML elements (`<button>`, `<nav>`, `<main>`) superior to generic `<div>` elements with click handlers?
   a) Semantic elements execute in WebAssembly.  
   b) Semantic elements provide native keyboard accessibility (tab focus, Enter/Space activation) and screen reader landmarks without custom JavaScript.  
   c) Semantic elements bypass CORS restrictions.  
   d) Browsers do not support CSS styles on `<div>` elements.  
   *(Answer key: `instructor-keys/quiz-04.md`)*

7. What is an HTTP header, and how is it formatted over the wire in HTTP/1.1?
   a) A binary bitmask at the beginning of each TCP frame.  
   b) A case-insensitive ASCII key-value pair separated by a colon (`Key: Value`) terminated by CRLF (`\r\n`).  
   c) A JSON object stringified in base64.  
   d) A gzip compressed metadata block.  
   *(Answer key: `instructor-keys/quiz-04.md`)*

8. When a web server responds with `Cache-Control: no-cache`, what does this instruct the browser to do?
   a) Never store the response under any circumstance.  
   b) Store the cached response, but revalidate with the origin server (using `ETag` or `If-Modified-Since`) before using it.  
   c) Cache the response for exactly 24 hours.  
   d) Discard the response and throw an error.  
   *(Answer key: `instructor-keys/quiz-04.md`)*
