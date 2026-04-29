from pydantic import BaseModel
from typing import List

class OrdineBase(BaseModel):
    quantita: int

class OrdineCreate(OrdineBase):
    id_cliente: int
    id_pizza: int

class Ordine(OrdineBase):
    ordine_id: int
    id_cliente: int
    id_pizza: int

    class Config:
        from_attributes = True

