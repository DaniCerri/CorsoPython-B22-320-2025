from fastapi import FastAPI
from database import engine
from routers import tags, clients, invoices

# Import dei modelli per creare le tabelle
from models.tag import Tag
from models.client import Client
from models.invoice import Invoice
from models.invoice_item import InvoiceItem
from models.invoice_tag_association import invoice_tags

# Crea le tabelle nel database
from database import Base
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Gestore di base delle fatture",
    description="Piccola API per la gestione (semplificata) delle fatture di una sola partita IVA",
    version="1.0.0"
)

# Includi i router
app.include_router(tags.router)
app.include_router(clients.router)
app.include_router(invoices.router)

@app.get("/")
def read_root():
    """Endpoint di benvenuto"""
    return {
        "message": "Benvenuto all'API di gestione fatture!",
        "docs": "/docs",
        "version": "1.0.0"
    }