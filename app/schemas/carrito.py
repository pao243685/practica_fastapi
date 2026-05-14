from pydantic import BaseModel


class ItemCarritoResponse(BaseModel):
    id: int
    producto_id: int
    cantidad: int

    class Config:
        from_attributes = True


class CarritoResponse(BaseModel):
    id: int
    usuario_id: int
    items: list[ItemCarritoResponse] = []

    class Config:
        from_attributes = True