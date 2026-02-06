from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

class InvoiceItem(Base):
    __tablename__ = "invoice_items"

    invoice_item_id = Column(Integer, primary_key=True, index=True)
    description = Column(String(500))
    quantity = Column(Float, default=1.0)
    unit_price = Column(Float)

    invoice_id = Column(Integer, ForeignKey("invoices.invoice_id"))

    invoice = relationship("Invoice", back_populates="items")
