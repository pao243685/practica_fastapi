from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.crud import carrito as crud_carrito
from app.db.database import get_db
from app.deps import get_current_user
from app import schemas

router = APIRouter()

@router.get("/", response_model=schemas.CarritoResponse, summary="Obtener el carrito del usuario")
def ver_carrito(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return crud_carrito.obtener_carrito(db, current_user.id)

@router.post("/agregar/{producto_id}", summary="Agregar un producto al carrito")
def agregar_producto(producto_id: int, cantidad: int = 1, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    carrito = crud_carrito.obtener_carrito(db, current_user.id)
    item = crud_carrito.agregar_item(db, carrito.id, producto_id, cantidad)
    return {"message": "Producto agregado al carrito", "item": item}

@router.delete("/eliminar/{item_id}", summary="Eliminar un producto del carrito")
def eliminar_item(item_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    crud_carrito.eliminar_item(db, item_id)
    return {"message": "Producto eliminado del carrito"}