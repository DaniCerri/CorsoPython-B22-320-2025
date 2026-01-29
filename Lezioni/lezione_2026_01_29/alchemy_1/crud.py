from matplotlib.pyplot import title
from sqlalchemy.orm import Session
import models, schemas

# Facciamo le funzioni che ci servono per interagire con il database
# 1. Scriviamo la funzione per ottenere una nota
def get_note(db: Session, id_note: int): # il parametro "db" che viene passato alla funzione è di tipo Session
    return db.query(models.Note).filter(models.Note.id_note == id_note).first()
    # db.query() selezione la tabella (e/o le colonne)
    # con .filter() applichiamo un "WHERE"
    # .first() Otteniamo solamente il primo risultato

# 2. Scriviamo la funzione che ottiene tutte le note
def get_notes(db: Session, skip: int = 0, limit: int = 100):
    # skip e limit vanno a limitare e gestire il numero di record che restituiamo contemporaneamente a chi ha fatto la
    # richiesta, non è quasi mai necessario ottenere tutto ciò che abbiamo ma possiamo suddividere la nostra risposta
    # in blocchi a partire da numero "skip" per "limit" record
    return db.query(models.Note).offset(skip).limit(limit).all()
    # db.query() fa lo stesso di prima
    # con .offset(skip) stacchiamo dalla risposta i primi "skip" elementi
    # [  con skip = 2
    #   riga_0, -> eliminata
    #   riga_1, -> eliminata
    #   riga_2,
    #   riga_3,
    #   riga_4,
    #   riga_5,
    # ]
    # da qua, applichiamo il limit, quindi contiamo "limit" righe e poi tronchiamo l'elenco
    # [  con skip = 2
    #   riga_0, -> eliminata
    #   riga_1, -> eliminata
    #   ---------------------------------------------------------
    #   riga_2, -> viene presa -> limit += 1 => 1
    #   riga_3, -> viene presa -> limit += 1 => 2
    #   riga_4, -> viene presa -> limit += 1 => 3
    #   ---------------------------------------------------------
    #   riga_5, -> viene eliminata
    # con limit = 3]

    # con .all() restituiamo la risposta tutta insieme

def create_note(db: Session, note: schemas.NoteCreate):
    # 1. Creiamo l'istanza del modello SQLAlchemy
    db_note = models.Note(
        title=note.title,
        content=note.content
    )

    # 2. Aggiungiamo la nota alla sessione
    db.add(db_note)

    # 3. Facciamo il commit della modifica (Salviamo effettivamente la modifica nel disco)
    db.commit()

    # 4. Facciamo il refresh del db "in RAM" per ottenere l'id della nota appena salvata
    db.refresh(db_note)

    return db_note







