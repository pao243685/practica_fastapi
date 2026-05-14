from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String(255))
    es_admin = Column(Boolean, default=False)
    carritos = relationship("Carrito", back_populates="usuario")
    pedidos = relationship("Pedido", back_populates="usuario")