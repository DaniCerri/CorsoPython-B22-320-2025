from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from models.invoice_tag_association import invoice_tags

# Tabella per salvare e gestire i tag
class Tag(Base):
    __tablename__ = "tags"

    tag_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)  # Es: "Urgente"
    color = Column(String(7))  # Es: "#FF0000" -> rosso

    # Dichiariamo la prima parte della relazione molti a molti
    invoices = relationship("Invoice", secondary=invoice_tags, back_populates="tags")
