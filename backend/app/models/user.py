from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id              = Column(Integer, primary_key=True, index=True)
    email           = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active       = Column(Boolean, default=True)
    role            = Column(String, nullable=False)

    # FK self‐referencia para vincular cliente → trainer
    trainer_id      = Column(Integer, ForeignKey("users.id"), nullable=True)

    created_at      = Column(DateTime(timezone=True), server_default=func.now())
    updated_at      = Column(DateTime(timezone=True), onupdate=func.now())

    # Relación bidireccional: User.trainer y User.clients
    trainer         = relationship("User", remote_side=[id], backref="clients")
