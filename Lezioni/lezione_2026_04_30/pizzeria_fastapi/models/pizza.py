from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from database import Base
from models.relazioni import pizza_ingredienti


# ci manca una roba

class Pizza(Base):
    __tablename__ = "pizze"

    pizza_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(80), unique=True, index=True)
    prezzo_base = Column(Float)
    descrizione = Column(String(500), nullable=True)
    disponibile = Column(Boolean, default=True)

    # Inseriremo le relazioni utili
    ingredienti = relationship("Ingrediente", secondary=pizza_ingredienti, back_populates="pizze")
    voci = relationship("VocePizzaOrdine", back_populates="pizza")

    @property
    def prezzo_totale(self):
        return self.prezzo_base + ... # Somma degli ingredienti




