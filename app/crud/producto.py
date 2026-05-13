from sqlalchemy.orm import Session

from app.models import Producto
from app.schemas import ProductoCreate


def listar_productos(db: Session):
    return db.query(Producto).all()


def crear_producto(db: Session, producto: ProductoCreate):
    db_producto = Producto(**producto.model_dump())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto


def actualizar_producto(db: Session, id: int, producto: ProductoCreate):
    db_producto = db.query(Producto).filter(Producto.id == id).first()
    if not db_producto:
        return None
    for key, value in producto.model_dump().items():
        setattr(db_producto, key, value)
    db.commit()
    db.refresh(db_producto)
    return db_producto


def eliminar_producto(db: Session, producto_id: int):
    db_producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not db_producto:
        return None
    db.delete(db_producto)
    db.commit()
    return db_producto


def obtener_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()
