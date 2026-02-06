from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.invoices import InvoiceCreate, InvoiceResponse, InvoiceList, InvoiceItem, InvoiceItemCreate
from crud.invoices import create_invoice, get_invoices, get_invoice, create_invoice_item
from dependencies import get_db

router = APIRouter(
    prefix="/invoices",
    tags=["invoices"]
)

@router.post("/", response_model=InvoiceResponse)
def create_invoice_endpoint(invoice: InvoiceCreate, db: Session = Depends(get_db)):
    """Crea una nuova fattura con i tag associati"""
    return create_invoice(db, invoice=invoice)

@router.get("/", response_model=List[InvoiceList])
def read_invoices(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Ottieni l'elenco delle fatture con paginazione"""
    return get_invoices(db, skip=skip, limit=limit)

@router.get("/{invoice_id}", response_model=InvoiceResponse)
def read_invoice(invoice_id: int, db: Session = Depends(get_db)):
    """Ottieni i dettagli completi di una fattura"""
    db_invoice = get_invoice(db, invoice_id=invoice_id)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Fattura non trovata")
    return db_invoice

@router.post("/{invoice_id}/items/", response_model=InvoiceItem)
def add_item_to_invoice(
    invoice_id: int, 
    item: InvoiceItemCreate, 
    db: Session = Depends(get_db)
):
    """Aggiungi una voce (item) a una fattura esistente"""
    return create_invoice_item(db, item=item, invoice_id=invoice_id)
