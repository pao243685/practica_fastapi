from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db.database import get_db
from app.deps import require_admin

router = APIRouter()


@router.get("", response_model=list[schemas.CategoriaResponse])
def listar_categorias(db: Session = Depends(get_db)):
    return crud.obtener_categoría(db)


@router.post("", response_model=schemas.CategoriaResponse, status_code=status.HTTP_201_CREATED, dependencies=[Depends(require_admin)])
def crear_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    return crud.crear_categoria(db, categoria)
