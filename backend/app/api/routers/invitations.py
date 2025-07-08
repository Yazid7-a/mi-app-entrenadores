from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.invitation import InvitationCreate, InvitationRead
from app.services.invitation import create_invitation, use_invitation
from app.core.database import get_db

router = APIRouter(prefix="/invitations", tags=["invitations"])

@router.post("/", response_model=InvitationRead)
def post_invitation(inv_in: InvitationCreate, db: Session = Depends(get_db)):
    return create_invitation(db, inv_in)

@router.post("/use/{code}", response_model=InvitationRead)
def post_use_invitation(code: str, client_id: int, db: Session = Depends(get_db)):
    return use_invitation(db, code, client_id)
