from pydantic import BaseModel
from typing import List
from datetime import date as date_time
from models.invoice import InvoiceStatus
from schemas.tags import Tag
from schemas.clients import Client

# Schemi per gli ITEM
class InvoiceItemBase(BaseModel):
    description: str
    quantity: float
    unit_price: float

class InvoiceItemCreate(InvoiceItemBase):
    pass

class InvoiceItem(InvoiceItemBase):
    item_id: int
    invoice_id: int
    
    class Config:
        from_attributes = True

# Schemi per le INVOICE
class InvoiceBase(BaseModel):
    number: str
    date: date_time
    status: InvoiceStatus = InvoiceStatus.DRAFT

class InvoiceCreate(InvoiceBase):
    client_id: int
    tag_ids: List[int] = []  # Qui ci mettiamo solamente una lista di id dei tag che associamo alla fattura

class InvoiceResponse(InvoiceBase):
    invoice_id: int
    client: Client  # Dati completi del cliente invece del solo ID
    items: List[InvoiceItem] = []
    tags: List[Tag] = []
    total_amount: float

    class Config:
        from_attributes = True

# Schema semplificato per la lista di fatture (senza items)
class InvoiceList(InvoiceBase):
    invoice_id: int
    client: Client
    tags: List[Tag] = []
    total_amount: float

    class Config:
        from_attributes = True
