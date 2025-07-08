from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from app.core.dependencies import get_current_trainer
from app.core.database import get_db
from app.schemas.user import UserRead
from app.services.client import list_clients   # <- aquí

router = APIRouter(prefix="/clients", tags=["clients"])


@router.get("", response_model=List[UserRead])
def read_clients(
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
    trainer = Depends(get_current_trainer),
):
    clients, total = list_clients(db, trainer.id, limit, offset)
    # Si quieres enviar el total en cabecera:
    # from fastapi import Response
    # response.headers["X-Total-Count"] = str(total)
    return clients
