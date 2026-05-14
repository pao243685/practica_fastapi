from fastapi import FastAPI
from .api.v1.api import api_router

app = FastAPI(
    title="E-commerce API",
    description="API para gestionar un carrito de " \
    "compras en un e-commerce",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"mensaje": "¡Bienvenido a FastAPI!"}


