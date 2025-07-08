# backend/app/services/invitation.py

import uuid
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.invitation import Invitation
from app.schemas.invitation import InvitationCreate
from app.models.user import User  # antes tenías 'from models.user', lo cambiamos a app.models

def create_invitation(db: Session, inv_in: InvitationCreate) -> Invitation:
    code = str(uuid.uuid4())
    inv = Invitation(
        code=code, # type: ignore
        trainer_id=inv_in.trainer_id, # type: ignore
        expires_at=inv_in.expires_at, # type: ignore
    )
    db.add(inv)
    db.commit()
    db.refresh(inv)
    return inv

def use_invitation(db: Session, code: str, client_id: int) -> Invitation:
    inv = (
        db.query(Invitation)
        .filter(
            Invitation.code == code,
            Invitation.used == False,
        ) # type: ignore
        .first()  # type: ignore[reportOptionalCall]
    )
    if not inv:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invitación inválida o ya usada"
        )
    # Marcamos la invitación como usada
    inv.used = True
    db.commit()

    # Vinculamos el cliente al trainer
    client = db.get(User, client_id)
    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente no encontrado"
        )
    client.trainer_id = inv.trainer_id # type: ignore
    db.commit()

    db.refresh(inv)
    return inv
