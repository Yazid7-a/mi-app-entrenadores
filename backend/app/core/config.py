# backend/app/core/config.py

from typing import List
from pydantic import BaseSettings, AnyHttpUrl, validator

class Settings(BaseSettings):
    # Nombre y versión de la API
    PROJECT_NAME: str = "Fitapp"
    PROJECT_VERSION: str = "0.1.0-beta"

    # Orígenes permitidos para CORS; en desarrollo suele ser localhost:3000
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000"]

    # Variables obligatorias en .env
    DATABASE_URL: str
    JWT_SECRET_KEY: str

    # JWT
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"
        case_sensitive = True

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v):
        """
        Permite definir BACKEND_CORS_ORIGINS en .env como:
        BACKEND_CORS_ORIGINS=http://localhost:3000,https://mi-dominio.com
        """
        if isinstance(v, str):
            return [i.strip() for i in v.split(",") if i.strip()]
        return v

settings = Settings()
