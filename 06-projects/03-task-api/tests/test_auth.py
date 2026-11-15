import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_register_user_success(client: AsyncClient):
    response = await client.post(
        "/api/v1/auth/register",
        json={"email": "alice@example.com", "password": "securepassword123", "full_name": "Alice Smith"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "alice@example.com"
    assert data["full_name"] == "Alice Smith"
    assert "id" in data
    assert "hashed_password" not in data


@pytest.mark.asyncio
async def test_register_duplicate_email_fails(client: AsyncClient):
    payload = {"email": "bob@example.com", "password": "password123"}
    resp1 = await client.post("/api/v1/auth/register", json=payload)
    assert resp1.status_code == 201

    resp2 = await client.post("/api/v1/auth/register", json=payload)
    assert resp2.status_code == 409
    assert "already registered" in resp2.json()["detail"].lower()


@pytest.mark.asyncio
async def test_register_short_password_validation(client: AsyncClient):
    response = await client.post(
        "/api/v1/auth/register",
        json={"email": "charlie@example.com", "password": "short"},
    )
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_login_success(client: AsyncClient):
    # Register user first
    await client.post(
        "/api/v1/auth/register",
        json={"email": "dan@example.com", "password": "mypassword123"},
    )

    # Login with OAuth2 form data
    response = await client.post(
        "/api/v1/auth/login",
        data={"username": "dan@example.com", "password": "mypassword123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_login_invalid_password(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={"email": "eva@example.com", "password": "correctpassword"},
    )

    response = await client.post(
        "/api/v1/auth/login",
        data={"username": "eva@example.com", "password": "wrongpassword"},
    )
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_get_current_user_me(client: AsyncClient):
    # Register and login
    await client.post(
        "/api/v1/auth/register",
        json={"email": "frank@example.com", "password": "mypassword123"},
    )
    login_resp = await client.post(
        "/api/v1/auth/login",
        data={"username": "frank@example.com", "password": "mypassword123"},
    )
    token = login_resp.json()["access_token"]

    # Access protected /users/me
    response = await client.get(
        "/api/v1/users/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    assert response.json()["email"] == "frank@example.com"


@pytest.mark.asyncio
async def test_get_current_user_unauthorized(client: AsyncClient):
    response = await client.get("/api/v1/users/me")
    assert response.status_code == 401
