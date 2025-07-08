# backend/app/api/routers/auth.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# importa sólo lo que necesitas:
from app.schemas.user import UserCreate, UserRead, UserLogin
from app.schemas.token import Token

from app.core.database import get_db
from app.services.auth import create_user, authenticate

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup", response_model=UserRead, status_code=201)
def signup(user_in: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user_in)

@router.post("/login", response_model=Token)
def login(form_data: UserLogin, db: Session = Depends(get_db)):
    token = authenticate(db, form_data)
    return {"access_token": token, "token_type": "bearer"}
