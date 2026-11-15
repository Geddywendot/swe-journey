import pytest
from httpx import AsyncClient


async def create_user_and_token(client: AsyncClient, email: str, password: str = "password123") -> str:
    await client.post("/api/v1/auth/register", json={"email": email, "password": password})
    login_resp = await client.post(
        "/api/v1/auth/login",
        data={"username": email, "password": password},
    )
    return login_resp.json()["access_token"]


@pytest.mark.asyncio
async def test_create_task_authenticated(client: AsyncClient):
    token = await create_user_and_token(client, "user1@example.com")

    response = await client.post(
        "/api/v1/tasks/",
        json={"title": "Write unit tests", "description": "Ensure 100% coverage", "status": "todo"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Write unit tests"
    assert data["status"] == "todo"
    assert "id" in data
    assert "user_id" in data


@pytest.mark.asyncio
async def test_create_task_unauthenticated_fails(client: AsyncClient):
    response = await client.post(
        "/api/v1/tasks/",
        json={"title": "Unauthenticated task"},
    )
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_tenant_isolation_tasks(client: AsyncClient):
    # Create two distinct users
    token_user_a = await create_user_and_token(client, "user_a@example.com")
    token_user_b = await create_user_and_token(client, "user_b@example.com")

    # User A creates a task
    task_a_resp = await client.post(
        "/api/v1/tasks/",
        json={"title": "User A Private Task", "status": "todo"},
        headers={"Authorization": f"Bearer {token_user_a}"},
    )
    task_a_id = task_a_resp.json()["id"]

    # User B creates a task
    await client.post(
        "/api/v1/tasks/",
        json={"title": "User B Private Task", "status": "todo"},
        headers={"Authorization": f"Bearer {token_user_b}"},
    )

    # User A lists tasks -> should only see 1 task
    list_a = await client.get("/api/v1/tasks/", headers={"Authorization": f"Bearer {token_user_a}"})
    assert len(list_a.json()) == 1
    assert list_a.json()[0]["title"] == "User A Private Task"

    # User B attempts to access User A's task -> MUST return 404 Not Found (no leak)
    cross_get = await client.get(
        f"/api/v1/tasks/{task_a_id}",
        headers={"Authorization": f"Bearer {token_user_b}"},
    )
    assert cross_get.status_code == 404

    # User B attempts to update User A's task -> MUST return 404 Not Found
    cross_patch = await client.patch(
        f"/api/v1/tasks/{task_a_id}",
        json={"title": "Malicious Tamper"},
        headers={"Authorization": f"Bearer {token_user_b}"},
    )
    assert cross_patch.status_code == 404

    # User B attempts to delete User A's task -> MUST return 404 Not Found
    cross_delete = await client.delete(
        f"/api/v1/tasks/{task_a_id}",
        headers={"Authorization": f"Bearer {token_user_b}"},
    )
    assert cross_delete.status_code == 404


@pytest.mark.asyncio
async def test_update_and_delete_task_owner(client: AsyncClient):
    token = await create_user_and_token(client, "owner@example.com")

    # Create
    create_resp = await client.post(
        "/api/v1/tasks/",
        json={"title": "Original Title", "status": "todo"},
        headers={"Authorization": f"Bearer {token}"},
    )
    task_id = create_resp.json()["id"]

    # Patch update
    update_resp = await client.patch(
        f"/api/v1/tasks/{task_id}",
        json={"title": "Updated Title", "status": "done"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert update_resp.status_code == 200
    assert update_resp.json()["title"] == "Updated Title"
    assert update_resp.json()["status"] == "done"

    # Delete
    delete_resp = await client.delete(
        f"/api/v1/tasks/{task_id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert delete_resp.status_code == 204

    # Verify gone
    get_after = await client.get(
        f"/api/v1/tasks/{task_id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert get_after.status_code == 404
