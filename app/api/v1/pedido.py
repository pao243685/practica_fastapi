from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.deps import get_current_user
from app import crud, schemas

router = APIRouter()

@router.post("", response_model=schemas.PedidoResponse, status_code=status.HTTP_201_CREATED, summary="Crear un nuevo pedido a partir del carrito")
def crear_pedido(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    carrito = crud.obtener_carrito(db, current_user.id)
    if not carrito.items:
        raise HTTPException(status_code=400, detail="El carrito está vacío")
    pedido = crud.crear_pedido(db, current_user.id)
    return pedido