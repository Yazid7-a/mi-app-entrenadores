# backend/app/schemas/token.py

from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    """
    Datos que extraemos del payload JWT para buscar el usuario.
    """
    id: Optional[int] = None

    class Config:
        orm_mode = True
