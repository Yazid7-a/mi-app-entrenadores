 # backend/app/services/client.py

from typing import List, Tuple
from sqlalchemy import select, func
from sqlalchemy.orm import Session
from app.models.user import User

def list_clients(
    db: Session,
    trainer_id: int,
    limit: int,
    offset: int
) -> Tuple[List[User], int]:
    """
    Devuelve la lista de clientes de un trainer y el total.
    """
    # Contamos total
    total_q = select(func.count()).select_from(User).where(User.trainer_id == trainer_id)
    total: int = db.execute(total_q).scalar_one()

    # Recuperamos página
    clients_q = (
        select(User)
        .where(User.trainer_id == trainer_id)
        .limit(limit)
        .offset(offset)
    )
    clients: List[User] = db.execute(clients_q).scalars().all()

    return clients, total
