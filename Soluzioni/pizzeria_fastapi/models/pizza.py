from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from database import Base
from models.associations import pizza_ingredienti


class Pizza(Base):
    __tablename__ = "pizze"

    pizza_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), unique=True, index=True)
    prezzo_base = Column(Float)
    descrizione = Column(String(500), nullable=True)
    disponibile = Column(Boolean, default=True)

    ingredienti = relationship("Ingrediente", secondary=pizza_ingredienti, back_populates="pizze")
    voci = relationship("VocePizzaOrdine", back_populates="pizza")

    @property
    def prezzo_totale(self):
        return self.prezzo_base + sum(i.prezzo_extra for i in self.ingredienti)
