# backend/app/core/dependencies.py

from typing import Optional, cast
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.database import get_db
from app.models.user import User
from app.schemas.token import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )
        sub = payload.get("sub")
        if sub is None:
            raise credentials_exception
        user_id = int(sub)
        token_data = TokenData(id=user_id)
    except (JWTError, ValueError):
        raise credentials_exception

    # Usamos cast para que Pylance entienda el tipo devuelto
    user = cast(Optional[User], db.get(User, token_data.id))

    if user is None or not user.is_active:
        raise credentials_exception

    # Aquí user es definitivamente un User
    return cast(User, user)


def require_role(role: str):
    def role_checker(current_user: User = Depends(get_current_user)) -> User:
        if current_user.role != role and current_user.role != "admin":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Permisos insuficientes: se requiere rol '{role}'",
            )
        return current_user
    return role_checker


get_current_trainer = require_role("trainer")
get_current_client  = require_role("client")
get_current_admin   = require_role("admin")
