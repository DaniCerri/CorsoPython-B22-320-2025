from pydantic import BaseModel
from typing import List

# Partiamo dagli schemi con meno dipendenze -> ordini
class OrderBase(BaseModel):
    quantity: int

class OrderCreate(OrderBase):
    # Per creare un ordine ci servono gli id del cliente e della pizza
    customer_id: int
    pizza_id: int

class Order(OrderBase):
    order_id: int
    customer_id: int
    pizza_id: int

    class Config:
        from_attributes = True

# Schemi delle pizze
class PizzaBase(BaseModel):
    name: str
    price: float

class PizzaCreate(PizzaBase):
    pass

class Pizza(PizzaBase):
    pizza_id: int
    orders: List[Order] = []

    class Config:
        from_attributes = True

# Schemi dei clienti
class CustomerBase(BaseModel):
    name: str
    phone: str

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    customer_id: int
    orders: List[Order] = []

    class Config:
        from_attributes = True
