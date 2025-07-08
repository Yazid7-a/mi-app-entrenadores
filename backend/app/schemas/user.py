from pydantic import BaseModel, EmailStr
from typing import Literal, Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    role: Literal["trainer", "client", "admin"]

class UserCreate(UserBase):
    password: str
<<<<<<< HEAD
    trainer_id: Optional[int] = None
=======
>>>>>>> f7a6a7b2d1e121e2b4dcf655bc90cd4169040d64

class UserRead(UserBase):
    id: int
    is_active: bool
<<<<<<< HEAD
    created_at: datetime
    updated_at: Optional[datetime]
    trainer_id: Optional[int]
=======
    created_at: datetime            # datetime en lugar de str
    updated_at: Optional[datetime]  # opcional, admite None
>>>>>>> f7a6a7b2d1e121e2b4dcf655bc90cd4169040d64

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str
