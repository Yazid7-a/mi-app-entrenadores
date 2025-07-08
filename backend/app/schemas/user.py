from pydantic import BaseModel, EmailStr
from typing import Literal, Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    role: Literal["trainer", "client", "admin"]

class UserCreate(UserBase):
    password: str
    trainer_id: Optional[int] = None

class UserRead(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime]
    trainer_id: Optional[int]

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str
