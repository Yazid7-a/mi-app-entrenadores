# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.database import engine, Base
from app.api.routers import auth, invitations, trainers, clients, admin

# Crear tablas en desarrollo (en producción usar Alembic)
# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
)

# --- CORS (ajusta allow_origins en producción) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,  # p. ej. ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Routers ---
app.include_router(auth.router,        prefix="/auth",        tags=["auth"])
app.include_router(invitations.router, prefix="/invitations", tags=["invitations"])
app.include_router(trainers.router,    prefix="/trainers",    tags=["trainers"])
app.include_router(clients.router,     prefix="/clients",     tags=["clients"])
app.include_router(admin.router,       prefix="/admin",       tags=["admin"])

# --- Healthcheck ---
@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}
