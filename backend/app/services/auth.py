from datetime import datetime, timedelta
from typing import Optional, cast
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException, status

from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from app.core.config import settings

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_ctx.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_ctx.verify(plain, hashed)


def create_user(db: Session, user_in: UserCreate) -> User:
    # 1) Comprobar si ya existe
    stmt = select(User).where(User.email == user_in.email)
    existing = db.execute(stmt).scalars().first()
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email ya registrado")

    # 2) Crear nuevo
    db_user = User()
    db_user.email = user_in.email
    db_user.hashed_password = hash_password(user_in.password)
    db_user.role = user_in.role
    if user_in.trainer_id is not None:
        db_user.trainer_id = user_in.trainer_id

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
    stmt = select(User).where(User.email == email)
    user = db.execute(stmt).scalars().first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)


def authenticate(db: Session, form_data: UserLogin) -> str:
    user = authenticate_user(db, form_data.email, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")
    return create_access_token({"sub": str(user.id), "role": user.role})
