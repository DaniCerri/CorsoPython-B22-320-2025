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
    cinema_hall.clear()  # puliamo la lista ma manteniamo lo stesso indirizzo in memoria
    cinema_hall.extend(nuovi_dati)  # Aggiungiamo i dati nuovi allo stesso indirizzo in memoria

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
# TODO: fare la media con un solo for (abbastanza implicito - list comprehension)

# 2.5 facciamo una funzione che estragga righe o colonne [della sala] dai dati
def raggruppa(tipo="colonna"):
    # Controlliamo che il tipo sia tra quelli disponibili, sennò diamo errore
    assert tipo in {"colonna", "riga"}, "Il tipo di raggruppamento deve essere 'riga' o 'colonna'"
    gruppi = {}

    for record in cinema_hall:
        chiave = record['number' if tipo == "colonna" else 'row']  # Otteniamo il nome della colonna/riga del posto corrente
        # Cerchiamo di prendere il gruppo con la stessa colonna dal dizionario
        gruppo = gruppi.get(chiave, [])
        gruppo.append(record) # Aggiungiamo il posto corrente all'elenco
        gruppi[chiave] = gruppo  # Sovrascriviamo l'elenco nel dizionario

    return gruppi

# 3. applicare queste funzioni sia alle righe che alle colonne [da ottenere]
@router.get("/stats")
def calcola_stats():
    righe = raggruppa("riga")
    colonne = raggruppa("colonna")

    media_righe = media_di_gruppi([value for value in righe.values()])
    media_colonne = media_di_gruppi([value for value in colonne.values()])

    conteggi_righe = {chiave: conta_prenotati(valore) for chiave, valore in righe.items()}
    conteggi_colonne = {chiave: conta_prenotati(valore) for chiave, valore in colonne.items()}
    # TODO: Fare una funzione 'aggrega' che data tipologia di raggruppamento faccia i 3 passaggi sopra

    return {
        "righe": {
            "media": media_righe,
            "conteggi": conteggi_righe
        },
        "colonne": {
            "media": media_colonne,
            "conteggi": conteggi_colonne
        },
    }


