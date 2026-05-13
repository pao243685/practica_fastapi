# Centralize all schemas
from app.schemas.usuario import UsuarioBase, UsuarioCreate, UsuarioResponse
from app.schemas.producto import ProductoCreate, ProductoResponse
from app.schemas.categoria import CategoriaBase, CategoriaCreate, CategoriaResponse
from app.schemas.auth import Token

__all__ = [
    # Usuario
    "UsuarioBase",
    "UsuarioCreate",
    "UsuarioResponse",
    # Producto
    "ProductoCreate",
    "ProductoResponse",
    # Categoria
    "CategoriaBase",
    "CategoriaCreate",
    "CategoriaResponse",
    # Auth
    "Token",
]
