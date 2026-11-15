from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from task_api.config import settings
from task_api.database import get_db
from task_api.models import User
from task_api.schemas import UserCreate, UserResponse, Token
from task_api.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    """Register a new user account.

    TODO:
    1. Check if user with user_in.email already exists (select(User).where(User.email == user_in.email)).
    2. If found, raise HTTPException(status_code=409, detail="Email already registered").
    3. Hash password using hash_password(user_in.password).
    4. Create User instance, add to db, commit, and refresh.
    5. Return the created user.
    """
    raise NotImplementedError("TODO: Implement /auth/register")


@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):
    """Authenticate with username (email) and password, returning JWT bearer token.

    TODO:
    1. Query User by form_data.username (matching User.email).
    2. Verify user exists and verify_password(form_data.password, user.hashed_password).
    3. If invalid or user not active, raise HTTPException(status_code=401, detail="Incorrect email or password").
    4. Create access token with sub=str(user.id).
    5. Return Token(access_token=token, token_type="bearer").
    """
    raise NotImplementedError("TODO: Implement /auth/login")
