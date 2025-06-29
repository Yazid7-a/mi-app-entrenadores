# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers import auth, trainers, clients, admin

app = FastAPI(title="Mi App de Entrenadores")

# --- CORS (ajusta orígenes en producción) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Routers ---
app.include_router(auth.router)
app.include_router(trainers.router,   prefix="/trainers", tags=["trainers"])
app.include_router(clients.router,    prefix="/clients",  tags=["clients"])
app.include_router(admin.router,      prefix="/admin",    tags=["admin"])

@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}
