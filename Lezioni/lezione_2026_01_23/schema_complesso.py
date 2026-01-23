"""
Gestiamo il catalogo dei film del nostro cinema.
Ogni film ha titolo, regista, durata, attori (>0), voto imdb.
Vogliamo gestire l'inserimento nel programma del nostro cinema di film nuovi e togliere
quelli "vecchi" [admin]
Del regista sappiamo nome e cognome, come degli attori

Ogni giornata ha in programma i 3 migliori film attivi per voto imdb

[admin]
La nostra dashboard ci deve permettere di inserire/eliminare film, registi e attori
"""
from pydantic import BaseModel
from typing import List

class RegistaBase(BaseModel):
    id: int
    name: str
    surname: str

class AttoreBase(BaseModel):
    id: int
    name: str
    surname: str

class FilmBase(BaseModel):
    id: int
    title: str
    id_director: int
    ids_actor: List[int]
    duration: int  # In secondi, va bene anche in minuti
    imdb: float  # Voto del film secondo imdb


