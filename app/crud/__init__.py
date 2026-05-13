# Centralize all CRUD operations
from app.crud.usuario import obtener_usuario_email, obtener_usuario_id, crear_usuario
from app.crud.producto import listar_productos, crear_producto, actualizar_producto, eliminar_producto, obtener_producto
from app.crud.categoria import crear_categoria, obtener_categoría

__all__ = [
    # Usuario
    "obtener_usuario_email",
    "obtener_usuario_id",
    "crear_usuario",
    # Producto
    "listar_productos",
    "crear_producto",
    "actualizar_producto",
    "eliminar_producto",
    "obtener_producto",
    # Categoria
    "crear_categoria",
    "obtener_categoría",
]
