# Week 07 Exercises

Complete all Silver exercises to pass the week. Gold exercises are optional stretch challenges.

---

## Exercise 7.1: Building a Validated Item Catalog REST API

**Type:** silver  
**Time box:** 60–90 min  
**Task:** Build an asynchronous FastAPI microservice managing a product catalog with full CRUD operations, strict Pydantic v2 validation models, and custom filtering.

**Acceptance criteria:**
- [ ] Implement schemas: `ProductCreate`, `ProductUpdate` (with optional fields), and `ProductResponse` (with generated ID and timestamps).
- [ ] Implement endpoints:
  - `POST /products`: Validates input, prevents duplicate SKUs (returning `409 Conflict`), returns `201 Created`.
  - `GET /products`: Supports pagination (`limit`, `offset`) and optional category filtering.
  - `GET /products/{product_id}`: Returns product or `404 Not Found`.
  - `PATCH /products/{product_id}`: Updates provided fields atomically.
  - `DELETE /products/{product_id}`: Deletes product and returns `204 No Content`.
- [ ] In-memory dictionary storage utilizing thread-safe or async lock primitives.
- [ ] 100% test coverage using `httpx.AsyncClient`.

**Rules:** AI off. Pydantic v2 syntax only (use `model_config = ConfigDict(...)` and `@field_validator`).  
**Hints:** See `hints.md` section 7.1

---

## Exercise 7.2: Debug This — Event Loop Starvation & Leaked State in FastAPI

**Type:** silver ("debug this")  
**Time box:** 60–90 min  
**Task:** A colleague deployed a FastAPI endpoint that parses uploaded CSV reports and enriches them with data from a third-party service. Under benchmark testing, the entire server becomes unresponsive when 10 concurrent requests arrive, and users report seeing other users' data in their responses!

Here is the buggy implementation:
```python
# buggy_service.py
import time
import requests
from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()

# Bug 1: Global mutable state shared across all concurrent requests!
current_user_context = {}

class ReportRequest(BaseModel):
    user_id: str
    record_count: int

def get_external_metadata(user_id: str):
    # Bug 2: Blocking synchronous requests.get() inside async path!
    response = requests.get(f"https://api.example.internal/users/{user_id}/meta", timeout=5)
    return response.json()

@app.post("/reports/generate")
async def generate_report(payload: ReportRequest):
    global current_user_context
    current_user_context["user_id"] = payload.user_id
    
    # Bug 3: Blocking time.sleep() stalls the entire single-threaded asyncio loop!
    time.sleep(2.0)
    
    metadata = get_external_metadata(payload.user_id)
    current_user_context["tier"] = metadata.get("tier", "standard")
    
    # Simulate processing
    result = {
        "user_id": current_user_context["user_id"],
        "tier": current_user_context["tier"],
        "records_processed": payload.record_count
    }
    return result
```

**Acceptance criteria:**
- [ ] Eliminate the global mutable `current_user_context` dict to prevent state cross-contamination between concurrent requests.
- [ ] Replace blocking `requests.get` with asynchronous `httpx.AsyncClient.get` (or explain how to properly run blocking code via `asyncio.to_thread`).
- [ ] Replace `time.sleep(2.0)` with non-blocking `await asyncio.sleep(2.0)`.
- [ ] Write a concurrent test using `asyncio.gather()` simulating 10 simultaneous requests with distinct user IDs, asserting that no user receives another user's ID or metadata.

**Rules:** Explain why the original code failed under concurrent load.  
**Hints:** See `hints.md` section 7.2

---

## Exercise 7.3: Hierarchical Dependency Injection & API Key Authentication

**Type:** silver  
**Time box:** 60–90 min  
**Task:** Implement a modular FastAPI dependency hierarchy that enforces API key authorization, extracts client metadata, and applies per-key rate limits.

**Acceptance criteria:**
- [ ] Create `verify_api_key` dependency that inspects the `X-API-Key` header, validating against a known set of keys (e.g. `test-key-admin`, `test-key-read`).
- [ ] Sub-dependency `require_admin_role` that verifies the key has administrative privileges, raising `403 Forbidden` otherwise.
- [ ] Implement a request context dependency yielding request start time and client IP.
- [ ] Custom middleware adding `X-Response-Time` header to all outgoing responses.
- [ ] Comprehensive tests verifying `401 Unauthorized`, `403 Forbidden`, and `200 OK` responses with `app.dependency_overrides`.

**Rules:** AI off. Use `fastapi.security.APIKeyHeader` and `fastapi.Depends`.  
**Hints:** See `hints.md` section 7.3

---

## Exercise 7.4: Streaming Event Pipeline with Asynchronous Server-Sent Events (SSE)

**Type:** gold (stretch)  
**Time box:** 120–180 min  
**Task:** Build an asynchronous streaming endpoint in FastAPI using `StreamingResponse` that emits real-time Server-Sent Events (`text/event-stream`). Implement an internal pub-sub broker using `asyncio.Queue` supporting multiple concurrent subscribers listening to partitioned channels.

**Acceptance criteria:**
- [ ] `POST /channels/{channel_id}/broadcast`: Publishes event payload to all active channel listeners.
- [ ] `GET /channels/{channel_id}/stream`: Connects client and streams SSE frames formatted as `event: message\ndata: {...}\n\n`.
- [ ] Clean subscriber disconnect handling: When client closes the connection, the queue is unlinked to avoid memory leaks.
- [ ] Automated async test verifying broadcast delivery to two concurrent subscriber queues.

**Rules:** No hints provided for gold stretch exercises.
