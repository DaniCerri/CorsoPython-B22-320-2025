from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Pizza(Base):
    __tablename__ = "pizze"

    pizza_id = Column(Integer, primary_key=True, index=True)  # Default per gli ID
    nome = Column(String(50), unique=True, index=True)
    prezzo = Column(Float)

    # Relazione: una pizza può essere richiesta in molti ordini
    ordini = relationship("Ordine", back_populates="pizza")
