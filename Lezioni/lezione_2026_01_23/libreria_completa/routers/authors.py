from fastapi import APIRouter, HTTPException
from typing import List
import schemas
import db

# Istanziamo il router con FastAPI
router = APIRouter()

@router.post("/create", status_code=201)
def create_author(new_author: schemas.AutoreBase):
    # Verifichiamo il duplicato
    if any(autore['id'] == new_author.id for autore in db.db_autori):
        raise HTTPException(
            status_code=409,
            detail=f"L'autore con id '{new_author.id}' esiste già"
        )

    # Se non abbiamo interrotto la funzione con un errore, salviamo l'autore nel DB
    author_data = new_author.model_dump()
    db.db_autori.append(author_data)

    return {
        "message": "L'autore è stato salvato con successo",
        "author": author_data
    }

# Endpoint per ottenere l'elenco di autori (senza libri)
@router.get("/", response_model=List[schemas.AutoreBase])
def get_authors():
    return db.db_autori

@router.get("/{id_author}", response_model=schemas.AutoreConLibri)
def get_author_completo(id_author: int):
    # 1. Cerchiamo di ottenere l'autore dal DB
    author = None
    for autore in db.db_autori:
        if autore['id'] == id_author:
            author = autore
            break

    # Se author è rimasto None, vuol dire che l'autore non esiste
    if not author:
        raise HTTPException(
            status_code=404,
            detail=f"L'autore con ID {id_author} non esiste"
        )

    # 2. Cerchiamo nel DB i libri che ha fatto (avranno id_author = a quello passato)
    books = [libro for libro in db.db_libri if libro['id_author'] == id_author]

    # 3. Uniamo e restituiamo i dati
    author['books'] = books

    return author
