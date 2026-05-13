from sqlalchemy.orm import Session

from app.models import Categoria
from app.schemas import CategoriaCreate


def crear_categoria(db: Session, categoria: CategoriaCreate):
    db_categoria = Categoria(nombre=categoria.nombre)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria


def obtener_categoría(db: Session):
    return db.query(Categoria).all()
