from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.clients import Client, ClientCreate
from crud.clients import create_client, get_clients, get_client_by_id
from dependencies import get_db

router = APIRouter(
    prefix="/clients",
    tags=["clients"]
)

@router.post("/", response_model=Client)
def create_client_endpoint(client: ClientCreate, db: Session = Depends(get_db)):
    """Crea un nuovo cliente"""
    return create_client(db, client=client)

@router.get("/", response_model=List[Client])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Ottieni l'elenco dei clienti con paginazione"""
    return get_clients(db, skip=skip, limit=limit)

@router.get("/{client_id}", response_model=Client)
def read_client(client_id: int, db: Session = Depends(get_db)):
    """Ottieni i dettagli di un singolo cliente"""
    db_client = get_client_by_id(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Cliente non trovato")
    return db_client
