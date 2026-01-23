from fastapi import APIRouter, HTTPException
from typing import List
import schemas
import db

router = APIRouter()

@router.get("/", response_model=List[schemas.LibroBase])
def get_books():
    return db.db_libri

@router.get("/complete", response_model=List[schemas.LibroCompleto])
def get_complete_books():
    # Per ogni libro, cerchiamo l'autore e ne inseriamo i dati
    lista_completa = []
    for i, libro in enumerate(db.db_libri):
        for autore in db.db_autori:
            if autore['id'] == libro['id_author']:
                libro['author_data'] = autore

        lista_completa.append(libro)
    return lista_completa

@router.get("/{book_id}")
def get_book(book_id: int):
    ...


