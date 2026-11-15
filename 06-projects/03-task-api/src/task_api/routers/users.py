from fastapi import APIRouter, Depends

from task_api.dependencies import get_current_user
from task_api.models import User
from task_api.schemas import UserResponse

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=UserResponse)
async def read_current_user(current_user: User = Depends(get_current_user)):
    """Return the profile of the currently authenticated user."""
    return current_user
