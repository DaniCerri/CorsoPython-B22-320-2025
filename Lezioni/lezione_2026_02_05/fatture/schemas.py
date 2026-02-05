from pydantic import BaseModel
from typing import List, Optional
from datetime import date as date_time
from models import  InvoiceStatus

# Schemi per i TAG
class TagBase(BaseModel):
    name: str
    color: str = "#CCCCCC"  # Diamo un grigio di default

class TagCreate(TagBase):  # Non aggiungiamo niente dal TagBase
    pass

class Tag(TagBase):
    tag_id: int
    class Config:
        from_attributes = True

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
    client_id: int  # Completamente opzionale
    # TODO: Includere tutti i dati del cliente
    items: List[InvoiceItem] = []

    tags: List[Tag] = []

    total_amount: float

    class Config:
        from_attributes = True

# Schemi per i CLIENT
class ClientBase(BaseModel):
    name: str
    vat_number: str
    email: str

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    client_id: int
    class Config:
        from_attributes = True








