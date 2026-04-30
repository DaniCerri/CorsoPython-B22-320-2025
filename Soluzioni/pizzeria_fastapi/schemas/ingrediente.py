from pydantic import BaseModel
from typing import Optional


class IngredienteBase(BaseModel):
    nome: str
    prezzo_extra: float = 0.0
    allergene: bool = False
    vegetariano: bool = True


class IngredienteCreate(IngredienteBase):
    pass


class IngredienteUpdate(BaseModel):
    nome: Optional[str] = None
    prezzo_extra: Optional[float] = None
    allergene: Optional[bool] = None
    vegetariano: Optional[bool] = None


class IngredienteResponse(IngredienteBase):
    ingrediente_id: int

    class Config:
        from_attributes = True
