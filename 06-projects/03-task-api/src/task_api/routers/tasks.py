from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from task_api.database import get_db
from task_api.dependencies import get_current_user
from task_api.models import User, Task
from task_api.schemas import TaskCreate, TaskUpdate, TaskResponse

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(
    task_in: TaskCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Create a new task owned by the authenticated user.

    TODO:
    1. Create Task instance with task_in data and user_id=current_user.id.
    2. Add to db, commit, and refresh.
    3. Return created task.
    """
    raise NotImplementedError("TODO: Implement POST /tasks")


@router.get("/", response_model=list[TaskResponse])
async def list_tasks(
    status_filter: str | None = Query(None, alias="status"),
    limit: int = Query(50, ge=1, le=100),
    offset: int = Query(0, ge=0),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """List tasks owned by the authenticated user with optional status filter and pagination.

    TODO:
    1. Build query: select(Task).where(Task.user_id == current_user.id).
    2. If status_filter is provided, add filter condition.
    3. Apply offset and limit.
    4. Execute query and return list of tasks.
    """
    raise NotImplementedError("TODO: Implement GET /tasks")


@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Retrieve a single task owned by the authenticated user.

    TODO:
    1. Query task where Task.id == task_id and Task.user_id == current_user.id.
    2. If not found, raise HTTPException(status_code=404, detail="Task not found").
    3. Return task.
    """
    raise NotImplementedError("TODO: Implement GET /tasks/{task_id}")


@router.patch("/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: int,
    task_in: TaskUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Update fields on a task owned by the authenticated user.

    TODO:
    1. Query task where Task.id == task_id and Task.user_id == current_user.id.
    2. If not found, raise HTTPException(status_code=404, detail="Task not found").
    3. Update provided attributes (exclude_unset=True).
    4. Commit, refresh, and return updated task.
    """
    raise NotImplementedError("TODO: Implement PATCH /tasks/{task_id}")


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Delete a task owned by the authenticated user.

    TODO:
    1. Query task where Task.id == task_id and Task.user_id == current_user.id.
    2. If not found, raise HTTPException(status_code=404, detail="Task not found").
    3. Delete task, commit, and return None.
    """
    raise NotImplementedError("TODO: Implement DELETE /tasks/{task_id}")
