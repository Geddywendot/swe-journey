# Week 08 Hints

> **Rule:** Attempt the exercise for at least 30 minutes before reading Hint 1. Wait an additional 15 minutes before reading Hint 2 or 3.

---

## Exercise 8.1: Declarative SQLAlchemy 2.0 Async Models and Alembic Pipeline

### Hint Level 1 (Nudge)
Use `from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship` to define models.

### Hint Level 2 (Concept Name)
In `alembic/env.py`, configure `run_migrations_online` to use an `async_engine` with `async with connectable.connect() as connection: await connection.run_sync(do_run_migrations)`.

### Hint Level 3 (Direction)
Model definitions:
```python
from datetime import datetime, timezone
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    
    tasks: Mapped[list["Task"]] = relationship(back_populates="owner", cascade="all, delete-orphan")
```

---

## Exercise 8.2: Debug This — Missing Greenlet in Async SQLAlchemy & N+1 Query

### Hint Level 1 (Nudge)
In synchronous SQLAlchemy, reading `user.tasks` triggers a transparent SQL query behind the scenes. In async mode, transparent blocking queries are strictly prohibited, raising `MissingGreenlet`.

### Hint Level 2 (Concept Name)
Use `from sqlalchemy.orm import selectinload` inside the `select()` statement options.

### Hint Level 3 (Direction)
Refactored query:
```python
from sqlalchemy.orm import selectinload

@router.get("/users-with-tasks")
async def get_users_with_tasks(db: AsyncSession = Depends(get_db)):
    stmt = select(User).options(selectinload(User.tasks))
    result = await db.execute(stmt)
    users = result.scalars().all()
    
    return [
        {
            "id": user.id,
            "email": user.email,
            "tasks": [t.title for t in user.tasks]
        }
        for user in users
    ]
```

---

## Exercise 8.3: Project 3 Milestone — The Task Management API

### Hint Level 1 (Nudge)
In `src/task_api/security.py`, use `passlib.context.CryptContext(schemes=["bcrypt"], deprecated="auto")` or `pwdlib` for password hashing and `jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)` for tokens.

### Hint Level 2 (Concept Name)
When querying or modifying a task in `routers/tasks.py`, always filter by both `id == task_id` AND `user_id == current_user.id`. If no row is returned, return `404 Not Found` (do not return `403`, to avoid leaking whether a task with that ID exists).

### Hint Level 3 (Direction)
Dependency structure for `get_current_user`:
```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = int(payload.get("sub"))
        if user_id is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception
        
    user = await db.get(User, user_id)
    if user is None:
        raise credentials_exception
    return user
```
