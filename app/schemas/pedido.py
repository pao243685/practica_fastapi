from pydantic import BaseModel
from datetime import datetime


class DetallePedidoResponse(BaseModel):
    id: int
    producto_id: int
    cantidad: int
    precio_unitario: float

    class Config:
        from_attributes = True


class PedidoResponse(BaseModel):
    id: int
    usuario_id: int
    fecha: datetime
    total: float
    detalles: list[DetallePedidoResponse] = []

    class Config:
        from_attributes = True