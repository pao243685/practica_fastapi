from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db.database import get_db
from app.deps import require_admin

router = APIRouter()


@router.get("", response_model=list[schemas.ProductoResponse])
def listar_productos(db: Session = Depends(get_db)):
    return crud.listar_productos(db)


@router.get("/{id}", response_model=schemas.ProductoResponse)
def obtener_producto(id: int, db: Session = Depends(get_db)):
    producto = crud.obtener_producto(db, id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto


@router.post("", response_model=schemas.ProductoResponse, status_code=status.HTTP_201_CREATED, dependencies=[Depends(require_admin)])
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.crear_producto(db, producto)


@router.put("/{id}", response_model=schemas.ProductoResponse, dependencies=[Depends(require_admin)])
def actualizar_producto(id: int, producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    db_producto = crud.actualizar_producto(db, id, producto)
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto


@router.delete("/{id}", dependencies=[Depends(require_admin)])
def eliminar_producto(id: int, db: Session = Depends(get_db)):
    producto = crud.eliminar_producto(db, id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": "Producto eliminado exitosamente", "producto": producto}
