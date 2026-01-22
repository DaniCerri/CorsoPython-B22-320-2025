from fastapi import APIRouter, HTTPException

import database
from database import cinema_hall, rows, cols, init_cinema
import random
random.seed(42)

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Benvenuto nel router di admin. Gli endpoint sono..."}

# TODO: facciamo un endpoint /random-seed che sceglie un numero casuale di posti casuali e li prenota
# prima di estrarre, prenotare etc, resettiamo cinema_hall (c'è una funzione da qualche parte)
# random.choice sceglie uno o più elementi di una lista
# random.sample sceglie un sottoinsieme casuale della lista
@router.get("/random-seed")
def random_seed():
    # 0. Resettiamo cinema_hall
    nuovi_dati = init_cinema()
    cinema_hall.clear()
    cinema_hall.extend(nuovi_dati)

    # 1. trovare il numero (casuale) di posti da prenotare
    n_posti = random.randint(1, rows * cols)

    # 2. scegliamo un sottoinsieme dei posti e li "prenotiamo"
    indici_da_prenotare = random.sample(range(rows * cols), n_posti)
    for indice in indici_da_prenotare:
        cinema_hall[indice]['is_booked'] = True

    # 3. Restituiamo l'elenco completo
    return {
        "prenotati": n_posti,
        "righe": rows,
        "colonne": cols,
        "database": cinema_hall
    }

# TODO: facciamo un endpoint /stats che restituisce le seguenti statistiche:
#  * riempimento per fila
#  * riempimento medio della sala (per file)
#  * lo stesso per colonne
# 1. fare una funzione che calcoli il conteggio di un insieme di posti
# 2. fare una funzione che dati dei conteggi da quella sopra [e il numero] dica la media
# 3. applicare queste funzioni sia alle righe che alle colonne [da ottenere]