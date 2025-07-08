# backend/app/services/auth.py

from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

# Importa sólo los esquemas que realmente usas:
from app.schemas.user import UserCreate, UserLogin

from app.core.config import settings
from app import models

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_ctx.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_ctx.verify(plain, hashed)


def create_user(db: Session, user_in: UserCreate) -> models.User:
    # 1) Comprueba si existe
    existing = db.query(models.User).filter(models.User.email == user_in.email).first() # type: ignore
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email ya registrado")
    # 2) Crea
    hashed = hash_password(user_in.password)
    db_user = models.User(
        email=user_in.email,
        hashed_password=hashed,
        role=user_in.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate(db: Session, form_data: UserLogin) -> str:
    user = db.query(models.User).filter(models.User.email == form_data.email).first() # type: ignore
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas"
        )
    to_encode = {"sub": str(user.id), "role": user.role}
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)
