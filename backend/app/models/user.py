<<<<<<< HEAD
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship       
=======
from sqlalchemy import Column, Integer, String, Boolean, DateTime
>>>>>>> f7a6a7b2d1e121e2b4dcf655bc90cd4169040d64
from sqlalchemy.sql import func
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
<<<<<<< HEAD

=======
>>>>>>> f7a6a7b2d1e121e2b4dcf655bc90cd4169040d64
    id              = Column(Integer, primary_key=True, index=True)
    email           = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active       = Column(Boolean, default=True)
    role            = Column(String, nullable=False)
<<<<<<< HEAD

    # Nueva columna para vincular cliente → entrenador
    trainer_id      = Column(Integer, ForeignKey("users.id"), nullable=True)

    created_at      = Column(DateTime(timezone=True), server_default=func.now())
    updated_at      = Column(DateTime(timezone=True), onupdate=func.now())

    # Relación para acceder a trainer.clients y client.trainer
    trainer         = relationship("User", remote_side=[id], backref="clients")
=======
    created_at      = Column(DateTime(timezone=True), server_default=func.now())
    updated_at      = Column(DateTime(timezone=True), onupdate=func.now())
>>>>>>> f7a6a7b2d1e121e2b4dcf655bc90cd4169040d64
