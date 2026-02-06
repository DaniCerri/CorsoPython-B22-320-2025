from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas.tags import Tag, TagCreate
from crud.tags import create_tag, get_tags
from dependencies import get_db

router = APIRouter(
    prefix="/tags",
    tags=["tags"]
)

@router.post("/", response_model=Tag)
def create_tag_endpoint(tag: TagCreate, db: Session = Depends(get_db)):
    """Crea un nuovo tag"""
    return create_tag(db, tag=tag)

@router.get("/", response_model=List[Tag])
def read_tags(db: Session = Depends(get_db)):
    """Ottieni l'elenco di tutti i tag"""
    return get_tags(db)
