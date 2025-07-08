from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class InvitationBase(BaseModel):
    trainer_id: int

class InvitationCreate(InvitationBase):
    expires_at: Optional[datetime] = None

class InvitationRead(InvitationBase):
    id: int
    code: str
    used: bool
    created_at: datetime
    expires_at: Optional[datetime]

    class Config:
        orm_mode = True
