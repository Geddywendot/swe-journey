from task_api.routers.auth import router as auth_router
from task_api.routers.users import router as users_router
from task_api.routers.tasks import router as tasks_router

__all__ = ["auth_router", "users_router", "tasks_router"]
