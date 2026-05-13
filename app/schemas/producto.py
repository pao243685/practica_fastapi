from pydantic import BaseModel


class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    en_stock: bool = True
    categoria_id: int


class ProductoResponse(BaseModel):
    id: int
    nombre: str
    precio: float
    en_stock: bool
    categoria_id: int

    class Config:
        from_attributes = True
