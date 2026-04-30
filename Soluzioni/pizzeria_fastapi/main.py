from fastapi import FastAPI
from database import engine
from routers import ingredienti, pizze, clienti, ordini

import models.associations
import models.ingrediente
import models.pizza
import models.cliente
import models.ordine

from database import Base
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Pizzeria Da Mario",
    description="Backend per la gestione di menù, ingredienti e ordini di asporto",
    version="1.0.0",
)

app.include_router(ingredienti.router)
app.include_router(pizze.router)
app.include_router(clienti.router)
app.include_router(ordini.router)


@app.get("/")
def root():
    return {"message": "Benvenuti alla Pizzeria Da Mario!", "docs": "/docs"}
