from pydantic import BaseModel
from typing import List

# Questa è una situazione in cui i nomi delle variabili/attributi contano, devono essere gli stessi che usiamo in fase
# di dichiarazione delle tabelle del DB

# 1. Classe con gli attributi di base
class NoteBase(BaseModel):
    title: str
    content: str | None = None # Diamo di default il valore None

# 2. Creiamo la classe "responsabile" della creazione delle note, anche se vuota è meglio farla per rendere chiaro cosa
# fa il codice
class NoteCreate(NoteBase):
    pass

# 3. classe con la nota completa
class NoteComplete(NoteBase):
    id_note: int
    is_active: bool

    # Da utilizzare con sqlalchemy per passare impostazioni / informazioni
    class Config:
        from_attributes = True
        # Consente a pydantic di leggere gli attributi che gli arrivano non solo come chiavi di un dizionario ma anche
        # come attributi di un oggetto (es: note.id_note invece che essere note['id_note']