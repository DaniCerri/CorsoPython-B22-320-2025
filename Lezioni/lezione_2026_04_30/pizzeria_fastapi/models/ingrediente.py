from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from database import Base
from models.relazioni import pizza_ingredienti, voce_ingrediente_extra

class Ingrediente(Base):
    __tablename__ = "ingredienti"

    ingrediente_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(80), unique=True, index=True)
    prezzo_extra = Column(Float, default=0.0)
    allergene = Column(Boolean, default=False)
    vegetariano = Column(Boolean, default=False)

    pizze = relationship("Pizza", secondary=pizza_ingredienti, back_populates="ingredienti")
    voci_extra = relationship(
        "VocePizzaOrdine",
        secondary=voce_ingrediente_extra,
        back_populates="ingredienti_extra"
    )
