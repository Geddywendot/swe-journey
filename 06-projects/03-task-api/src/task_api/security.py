from datetime import datetime, timedelta, timezone
import jwt
from passlib.context import CryptContext

from task_api.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """Hash a plaintext password using bcrypt.

    TODO: Implement password hashing using pwd_context.hash().
    """
    raise NotImplementedError("TODO: Implement hash_password using pwd_context.hash()")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plaintext password against a stored bcrypt hash.

    TODO: Implement password verification using pwd_context.verify().
    """
    raise NotImplementedError("TODO: Implement verify_password using pwd_context.verify()")


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """Create a signed JWT access token.

    TODO:
    1. Make a copy of data dict.
    2. Set "exp" claim to UTC now + expires_delta (or settings.ACCESS_TOKEN_EXPIRE_MINUTES).
    3. Encode using jwt.encode() with settings.SECRET_KEY and settings.ALGORITHM.
    """
    raise NotImplementedError("TODO: Implement create_access_token using jwt.encode()")


def decode_access_token(token: str) -> dict:
    """Decode and validate a JWT access token.

    TODO:
    1. Decode using jwt.decode() with settings.SECRET_KEY and algorithms=[settings.ALGORITHM].
    2. Return the decoded payload dict.
    3. Raise jwt.PyJWTError if decoding fails or token is expired.
    """
    raise NotImplementedError("TODO: Implement decode_access_token using jwt.decode()")
