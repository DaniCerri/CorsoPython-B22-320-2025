from sqlalchemy.orm import Session
from models.client import Client
from schemas.clients import ClientCreate

def create_client(db: Session, client: ClientCreate):
    db_client = Client(**client.model_dump())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Client).offset(skip).limit(limit).all()

def get_client_by_id(db: Session, client_id: int):
    return db.query(Client).filter(Client.client_id == client_id).first()
