from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from models.ordine import StatoOrdine
from schemas.pizza import PizzaResponse
from schemas.ingrediente import IngredienteResponse
from schemas.cliente import ClienteResponse


class VoceOrdineCreate(BaseModel):
    pizza_id: int
    quantita: int = Field(ge=1)
    ingredienti_extra_ids: List[int] = []


class VoceOrdineResponse(BaseModel):
    voce_id: int
    pizza: PizzaResponse
    quantita: int
    ingredienti_extra: List[IngredienteResponse] = []

    class Config:
        from_attributes = True


class OrdineCreate(BaseModel):
    cliente_id: int
    note: Optional[str] = None
    voci: List[VoceOrdineCreate] = Field(min_length=1)


class OrdineStatoUpdate(BaseModel):
    stato: StatoOrdine


class OrdineResponse(BaseModel):
    ordine_id: int
    data_ora: datetime
    stato: StatoOrdine
    note: Optional[str] = None
    cliente: ClienteResponse
    voci: List[VoceOrdineResponse] = []

    class Config:
        from_attributes = True


class OrdineList(BaseModel):
    ordine_id: int
    data_ora: datetime
    stato: StatoOrdine
    cliente: ClienteResponse

    class Config:
        from_attributes = True


class StoricoCliente(BaseModel):
    ordini: List[OrdineResponse]
    totale_speso: float
