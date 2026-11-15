from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
import jwt

from task_api.database import get_db
from task_api.models import User
from task_api.security import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
) -> User:
    """Validate JWT bearer token and return the authenticated User.

    TODO:
    1. Call decode_access_token(token).
    2. Extract user_id from payload "sub". If missing or invalid, raise 401 HTTPException.
    3. Query User from db by id (using db.get(User, int(user_id))).
    4. If user is None or not user.is_active, raise 401 HTTPException.
    5. Return the User object.
    """
    raise NotImplementedError("TODO: Implement get_current_user dependency")
