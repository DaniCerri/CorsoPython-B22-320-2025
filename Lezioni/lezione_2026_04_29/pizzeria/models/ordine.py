from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Ordine(Base):
    __tablename__ = "ordini"

    ordine_id = Column(Integer, primary_key=True, index=True)
    quantita = Column(Integer, default=1)
    # mancano stato e data_ora

    # Relazioni con cliente e pizza
    id_cliente = Column(Integer, ForeignKey("clienti.cliente_id"))
    id_pizza = Column(Integer, ForeignKey("pizze.pizza_id"))

    # relazioni inverse (dalle tabelle di prima)
    cliente = relationship("Cliente", back_populates="ordini")
    pizza = relationship("Pizza", back_populates="ordini")
