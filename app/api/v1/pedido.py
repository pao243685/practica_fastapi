from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from deps.deps import get_db, get_current_user
from app import crud, schemas

router = APIRouter()


@router.post("", response_model=schemas.PedidoResponse, status_code=status.HTTP_201_CREATED)
def crear_pedido(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    carrito = crud.obtener_carrito(db, current_user.id)
    if not carrito.items:
        raise HTTPException(status_code=400, detail="El carrito está vacío")
    pedido = crud.crear_pedido(db, current_user.id, carrito)
    return pedido