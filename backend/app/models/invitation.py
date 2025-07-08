from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class Invitation(Base):
    __tablename__ = "invitations"
    id          = Column(Integer, primary_key=True, index=True)
    code        = Column(String, unique=True, index=True, nullable=False)
    trainer_id  = Column(Integer, ForeignKey("users.id"), nullable=False)
    used        = Column(Boolean, default=False)
    expires_at  = Column(DateTime(timezone=True), nullable=False)
    created_at  = Column(DateTime(timezone=True), server_default=func.now())
