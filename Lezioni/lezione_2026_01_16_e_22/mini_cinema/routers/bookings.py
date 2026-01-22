from fastapi import APIRouter, HTTPException
from ..database import cinema_hall, rows, cols
import math

router = APIRouter()

# 1. Facciamo l'endpoint di root in cui spieghiamo il router
@router.get("/")
def booking_root():
    return {
        "message": "Visita /seats per i posti o /book/{seat_id} per prenotare un posto"
    }

# 2. Facciamo l'endpoint che fornisce la lista dei posti liberi disponibili
@router.get("/seats")
def get_available_seats():
    """
    Restituisce tutti i posti liberi disponibili o lista vuota se finiti
    """
    return [row for row in cinema_hall if not row['is_booked']]

@router.post("/book/{seat_id}")
def book_seat(seat_id: str):
    # 1. Rendere l'id tutto maiuscolo (normalizzazione input)
    seat_id = seat_id.upper()

    # 2. Cerca il posto nella lista
    target_seat = None  # variabile che usiamo per mettere l'indice del nostro
    # posto nella lista (se lo troviamo)

    for i, row in enumerate(cinema_hall):
        if row['id'] == seat_id:
            # 2.1 Se lo trovi, segnalo come esistente
            target_seat = i
            break  # Se abbiamo trovato il posto, non serve continuare a cercare

    # 3. Se il posto non esiste, dai errore 404
    if not target_seat: # Non lo abbiamo trovato, è rimasto None
        raise HTTPException(
            status_code=404,
            detail=f"Il posto {seat_id} non è presente in sala"
        )

    # 4. Se il posto è prenotato, dai errore 409 (conflict)
    if cinema_hall[target_seat]['is_booked']:
        raise HTTPException(
            status_code=409,
            detail=f"Il posto {seat_id} è già occupato"
        )

    # 5. Effettua la prenotazione e dai conferma
    cinema_hall[target_seat]['is_booked'] = True

    return {
        "message": f"Il posto {seat_id} è stato prenotato con successo"
    }

# 3. Facciamo una funzione che dia il miglior posto disponibile
@router.get("/seats/best")
def get_best_seat():
    # TODO: importare anche rows e cols dal file con cinema_hall
    # TODO: far mettere all'utente un indice di tolleranza (alto, medio, basso)
    ...

def gaussiana(media: float, var: float, x: float):
    primo_blocco = 1 / (var * math.sqrt(2 * math.pi))
    esponente = - (x - media) ** 2 / (2 * var ** 2)

    return primo_blocco * math.exp(esponente)













