from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from app.db.database import Base
from app.models import *


def crear_pedido(db: Session, usuario_id: int):
    carrito = db.query(Carrito).filter(Carrito.usuario_id == usuario_id).first()
    if not carrito or not carrito.items:
        raise Exception("El carrito está vacío")

    total = sum(item.cantidad * item.producto.precio for item in carrito.items)
    pedido = Pedido(usuario_id=usuario_id, total=total)
    db.add(pedido)
    db.commit()
    db.refresh(pedido)

    for item in carrito.items:
        detalle = DetallePedido(
            pedido_id=pedido.id,
            producto_id=item.producto_id,
            cantidad=item.cantidad,
            precio_unitario=item.producto.precio
        )
        db.add(detalle)

    db.commit()

    for item in carrito.items:
        db.delete(item)
    db.commit()

    return pedido