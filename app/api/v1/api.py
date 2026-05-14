from fastapi import APIRouter, Depends

from app.api.v1 import auth, carrito, pedido, productos, categorias


api_router = APIRouter()

api_router.include_router(auth.router, prefix="/usuarios", tags=["auth"])
api_router.include_router(productos.router, prefix="/productos", tags=["productos"])
api_router.include_router(categorias.router, prefix="/categorias", tags=["categorias"])
api_router.include_router(carrito.router, prefix="/carrito", tags=["carrito"])
api_router.include_router(pedido.router, prefix="/pedidos", tags=["pedidos"])