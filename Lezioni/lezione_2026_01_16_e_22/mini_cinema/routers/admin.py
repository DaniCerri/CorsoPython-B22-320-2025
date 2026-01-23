from fastapi import APIRouter, HTTPException
from database import cinema_hall, rows, cols, init_cinema
import random
random.seed(42)

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Benvenuto nel router di admin. Gli endpoint sono..."}

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
def conta_prenotati(lista_posti: list[dict]) -> int:
    tot_prenotati = 0
    for posto in lista_posti:
        if posto['is_booked']:
            tot_prenotati += 1

    return tot_prenotati


# 2. fare una funzione che dati dei conteggi da quella sopra [e il numero] dica la media
def media_di_gruppi(gruppi: list[list[dict]]) -> float:
    lista_totali = []
    for gruppo in gruppi:
        totale_gruppo = conta_prenotati(gruppo)
        lista_totali.append(totale_gruppo)

    return sum(lista_totali) / len(lista_totali)

# 3. applicare queste funzioni sia alle righe che alle colonne [da ottenere]
