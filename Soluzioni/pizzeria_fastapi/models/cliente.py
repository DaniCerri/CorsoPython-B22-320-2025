from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Cliente(Base):
    __tablename__ = "clienti"

    cliente_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), index=True)
    telefono = Column(String(30))
    indirizzo = Column(String(200))

    ordini = relationship("Ordine", back_populates="cliente")
