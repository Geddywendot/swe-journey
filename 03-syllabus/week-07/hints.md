# Week 07 Hints

> **Rule:** Attempt the exercise for at least 30 minutes before reading Hint 1. Wait an additional 15 minutes before reading Hint 2 or 3.

---

## Exercise 7.1: Building a Validated Item Catalog REST API

### Hint Level 1 (Nudge)
Define a base Pydantic schema `ProductBase` with shared fields (title, price, description) and inherit from it for `ProductCreate` and `ProductResponse`.

### Hint Level 2 (Concept Name)
Use `ConfigDict(from_attributes=True)` in `ProductResponse` so it can serialize ORM or dictionary objects seamlessly.

### Hint Level 3 (Direction)
Pydantic v2 example:
```python
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class ProductBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    sku: str = Field(pattern=r"^[A-Z0-9]{6,12}$")
    price_cents: int = Field(gt=0)

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
```

---

## Exercise 7.2: Debug This — Event Loop Starvation & Leaked State in FastAPI

### Hint Level 1 (Nudge)
In Python's `asyncio`, any synchronous blocking call (`time.sleep()`, synchronous socket operations) stops the whole thread. Other tasks cannot resume until the blocking call returns.

### Hint Level 2 (Concept Name)
Never store request-specific state in global module variables. Keep variables local to the function or pass them via FastAPI's `Request.state` or dependency injection.

### Hint Level 3 (Direction)
Refactor using `httpx.AsyncClient`:
```python
import asyncio
import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI()

async def fetch_metadata(client: httpx.AsyncClient, user_id: str) -> dict:
    resp = await client.get(f"https://api.example.internal/users/{user_id}/meta", timeout=5.0)
    resp.raise_for_status()
    return resp.json()

@app.post("/reports/generate")
async def generate_report(payload: ReportRequest):
    # Non-blocking async sleep
    await asyncio.sleep(2.0)
    
    async with httpx.AsyncClient() as client:
        metadata = await fetch_metadata(client, payload.user_id)
        
    return {
        "user_id": payload.user_id,
        "tier": metadata.get("tier", "standard"),
        "records_processed": payload.record_count
    }
```

---

## Exercise 7.3: Hierarchical Dependency Injection & API Key Authentication

### Hint Level 1 (Nudge)
FastAPI's `Depends` can be nested. A dependency function can take another dependency as its own parameter: `def require_admin(key: str = Depends(verify_api_key)): ...`.

### Hint Level 2 (Concept Name)
Use `Security` with `APIKeyHeader(name="X-API-Key", auto_error=True)` to extract header values and automatically document the security scheme in OpenAPI/Swagger UI.

### Hint Level 3 (Direction)
Structure:
```python
from fastapi import Security, HTTPException, status, Depends
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key")

VALID_KEYS = {
    "key-admin-123": {"role": "admin", "client": "internal"},
    "key-read-456": {"role": "read", "client": "partner"}
}

async def get_api_client(key: str = Security(api_key_header)) -> dict:
    client = VALID_KEYS.get(key)
    if not client:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key"
        )
    return client

async def require_admin(client: dict = Depends(get_api_client)) -> dict:
    if client.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required"
        )
    return client
```
