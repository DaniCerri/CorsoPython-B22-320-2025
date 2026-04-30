import enum
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum, Text
from sqlalchemy.orm import relationship
from database import Base
from models.relazioni import voce_ingrediente_extra


# Andiamo a standardizzare le tipologie di stato ordine a disposizione
class StatoOrdine(str, enum.Enum):
    RICEVUTO = "ricevuto"
    IN_PREPARAZIONE = "in_preparazione"
    PRONTO = "pronto"
    CONSEGNATO = "consegnato"

class Ordine(Base):
    __tablename__ = "ordini"

    ordine_id = Column(Integer, primary_key=True, index=True)
    data_ora = Column(DateTime)
    stato = Column(Enum(StatoOrdine), default=StatoOrdine.RICEVUTO)
    note = Column(Text, nullable=True)  # Le eventuali note sono opzionali

    cliente_id = Column(Integer, ForeignKey("clienti.cliente_id"))
    cliente = relationship("Cliente", back_populates="ordini")
    voci = relationship("VocePizzaOrdine", back_populates="ordine", cascade="all, delete-orphan")

class VocePizzaOrdine(Base):
    __tablename__ = "voci_ordine"

    voce_id = Column(Integer, primary_key=True, index=True)
    quantita = Column(Integer, default=1)

    ordine_id = Column(Integer, ForeignKey("ordini.ordine_id"))
    pizza_id = Column(Integer, ForeignKey("pizze.pizza_id"))

    ordine = relationship("Ordine", back_populates="voci")
    pizza = relationship("Pizza", back_populates="voci")

    ingredienti_extra = relationship(
        "Ingrediente",
        secondary=voce_ingrediente_extra,
        back_populates="voci_extra"
    )


