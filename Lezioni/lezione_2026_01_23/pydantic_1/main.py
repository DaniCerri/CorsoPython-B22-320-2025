from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel  # Questo è ciò che usiamo per i controlli
from typing import List  # Questo è ciò che usiamo per i controlli

# 1. facciamo il database "finto"
db_libreria = []

# 2. Creiamo lo SCHEMA Pydantic
class Libro(BaseModel):  # Eredita la configurazione da BaseModel
    # questi parametri sono tutti OBBLIGATORI
    title: str
    author: str
    pages: int
    year: int
    price: float
class LibroOut(BaseModel):
    title: str
    author: str
    year: int

# 3. Costruiamo il router
router = APIRouter()

@router.get("/", response_model=List[LibroOut])
# Dichiariamo che dalla funzione uscirà una lista di libri (con i dati dei libri)
def get_books():
    """
    Restituisce l'elenco completo di libri con tutti i dati
    """
    return db_libreria

@router.post("/new", status_code=201)
# Per la conferma useremo il codice 201 - Creato con successo
def create_book(new_book: Libro):
    """
    Crea un nuovo libro nel database se i dati sono corretti.
    Il controllo viene fatto automaticamente da Pydantic.
    :param new_book: oggetto di classe Libro
    """
    # Prima cosa controlliamo che il libro non esista già
    for libro in db_libreria:
        if libro['title'] == new_book.title and libro['author'] == new_book.author:
            raise HTTPException(
                status_code=409,
                detail=f"Il libro esiste già: id={libro['id']}"
            )

    # Inseriamo il nuovo libro nel DB
    id_libro = len(db_libreria) + 1
    dati_libro = new_book.model_dump()  # converte l'oggetto in dizionario
    dati_libro['id'] = id_libro  # Aggiungiamo il dato dell'id

    db_libreria.append(dati_libro)  # Lo aggiungiamo alla lista

    return {
        "message": "Libro creato con successo",
        "book": dati_libro
    }

# 4. Creiamo l'app e colleghiamo il router
app = FastAPI(
    title="Primo esempio Pydantic",
    description="Versione base di un'API per la creazione di libri",
    version="1.0.0"
)

app.include_router(
    router,
    prefix="/books",
    tags=['Libri']
)

@app.get("/")
def root():
    return {
        "message": "Vai su /docs per testare l'API"
    }






