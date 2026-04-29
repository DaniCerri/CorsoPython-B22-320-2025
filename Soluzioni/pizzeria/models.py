# Gestiamo una piccola pizzeria: ci sono pizze nel menù e clienti che fanno ordini.
# Ogni ordine è di un solo cliente e contiene una sola pizza con una certa quantità.
# Un cliente può fare tanti ordini, una pizza può comparire in tanti ordini.

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Pizza(Base):
    __tablename__ = "pizzas"

    pizza_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), unique=True, index=True)
    price = Column(Float)

    # Relazione: una pizza può essere ordinata in tanti ordini
    orders = relationship("Order", back_populates="pizza")


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    phone = Column(String(30))

    # Relazione: un cliente può fare tanti ordini
    orders = relationship("Order", back_populates="customer")


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, default=1)

    # Chiavi esterne: ogni ordine fa riferimento a un cliente e a una pizza
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    pizza_id = Column(Integer, ForeignKey("pizzas.pizza_id"))

    # Relazioni inverse
    customer = relationship("Customer", back_populates="orders")
    pizza = relationship("Pizza", back_populates="orders")
