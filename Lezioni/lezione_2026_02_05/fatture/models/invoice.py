from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from database import Base
from models.invoice_status import InvoiceStatus
from models.invoice_tag_association import invoice_tags

# Classe per gestire le fatture
class Invoice(Base):
    __tablename__ = "invoices"

    invoice_id = Column(Integer, primary_key=True, index=True)
    number = Column(String(20), index=True)
    date = Column(Date)
    status = Column(Enum(InvoiceStatus), default=InvoiceStatus.DRAFT)

    client_id = Column(Integer, ForeignKey("clients.client_id"))

    client = relationship("Client", back_populates="invoices")
    items = relationship("InvoiceItem", back_populates="invoice")

    # Definiamo il secondo pezzo della relazione N:N
    tags = relationship("Tag", secondary=invoice_tags, back_populates="invoices")

    # Utilizzando il decoratore @property definiamo una funzione (metodo) della nostra classe che non viene salvato
    # nel database ma che per Pydantic sembrerà una "colonna" della nostra tabella.
    # Quindi potremo fare uno schema pydantic che restituirà anche ciò che fa la funzione sotto "@property" come
    # se fosse un attributo (anche se in realtà è una funzione)
    @property
    def total_amount(self):  # La funzione calcola il totale degli item nella fattura
        return sum(item.unit_price * item.quantity for item in self.items)
