from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import profiles  # Importamos tu router de perfiles
# Si luego agregas offers, proposals, etc. los importas igual:
# from app.routers import offers

app = FastAPI(
    title="API de Ventanería",
    description="API para gestionar perfiles, ofertas y más con Supabase",
    version="1.0.0",
)

# Configuración CORS (permite peticiones desde tu frontend local, si lo tienes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o ["http://localhost:3000"] si tienes frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Registro del router de perfiles
app.include_router(
    profiles.router,
    prefix="/profiles",  # prefijo de la ruta
    tags=["Profiles"]
)

# (opcional) si tienes más routers
# app.include_router(offers.router, prefix="/offers", tags=["Offers"])

@app.get("/")
def root():
    return {"message": "API funcionando correctamente 🚀"}
