from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal

import models

app = FastAPI(
    title="API Pizzeria",
    description="Mini API di ripasso per gestire una pizzeria",
    version="1.0.0"
)

def get_db():
    db = SessionLocal()  # Creiamo una nuova sessione di collegamento al DB
    try:
        yield db
    finally:
        db.close()
