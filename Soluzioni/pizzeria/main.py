from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas, crud
from database import engine, SessionLocal

# ================= CONFIG =================

# 1. creiamo le tabelle se non presenti
models.Base.metadata.create_all(bind=engine)

# 2. Istanziamo la nostra app
app = FastAPI(
    title="Pizzeria API",
    description="Mini API per la gestione di una pizzeria con SQLAlchemy",
    version="1.0.0"
)

# 3. Funzione di dipendenza per creare le sessioni con il DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ================= ENDPOINT =================
# 1. Creazione pizza
@app.post("/pizzas/new", response_model=schemas.Pizza)
def create_pizza(pizza: schemas.PizzaCreate, db: Session = Depends(get_db)):
    return crud.create_pizza(db, pizza=pizza)

# 2. Creazione cliente
@app.post("/customers/new", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db, customer=customer)

# 3. Creazione ordine
@app.post("/orders/new", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order=order)

# 4. Endpoint per ottenere un cliente completo da ID
@app.get("/customers/{customer_id}", response_model=schemas.Customer)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db, customer_id=customer_id)
    if not db_customer:
        raise HTTPException(
            status_code=404,
            detail=f"Il cliente con id {customer_id} non è presente"
        )
    return db_customer

# 5. Endpoint per ottenere gli ordini di una certa pizza (per nome)
@app.get("/pizzas/{name}/orders", response_model=List[schemas.Order])
def read_orders_by_pizza_name(name: str, db: Session = Depends(get_db)):
    return crud.get_orders_by_pizza_name(db, name=name)
