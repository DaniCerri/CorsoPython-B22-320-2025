"""
Data una lista di [liste di] spese andiamo a calcore un po' di statistiche
"""

def calcola_media(lista_spese: list[float]) -> float:
    """
    Funzione che calcola la media di una lista di numeri con la virgola.
    :param lista_spese: lista di spese di cui viene calcolata la media
    :return: media, float
    """
    media = sum(lista_spese) / len(lista_spese)  # Calcoliamo la media sempre come somma / n° di elementi
    return media  # Facciamo uscire la media calcolata dalla funzione

def calcola_varianza(lista_spese: list[float]) -> float:
    """
    Funzione che calcola la varianza di una lista di numeri di numeri con la virgola.
    :param lista_spese: lista di spese di cui viene calcolata la varianza
    :return: varianza, float
    """
    media = calcola_media(lista_spese)  # Utilizziamo la funzione fatta prima per calcolare la media
    # andiamo a calcolare lo scarto di ogni elemento della lista rispetto alla media e lo eleviamo al quadrato
    scarti = []
    for numero in lista_spese:
        scarto = (numero - media) ** 2
        scarti.append(scarto)
    # Calcoliamo la media degli scarti (che è la varianza)
    varianza = calcola_media(scarti)
    return varianza  # Facciamo uscire la varianza dalla funzione -> [la "restituiamo"]

def calcola_dev_std(lista_spese: list[float]) -> float:
    """
    Funzione che calcola la deviazione standard di una lista di numeri di numeri con la virgola.
    :param lista_spese: lista di spese di cui viene calcolata la deviazione standard
    :return: deviazione standard, float
    """
    # Calcoliamo la varianza con la funzione appena fatta
    varianza = calcola_varianza(lista_spese)

    # Calcoliamo la radice quadrata della varianza (che è la dev. std.)
    dev_std = varianza ** (1/2)

    return dev_std  # Restituiamo la deviazione standard calcolata

def separatori(titolo: str, carattere="-", lunghezza=50) -> tuple[str, str]: # Per dare un valore di default usiamo <parametro>=<valore>
    """
    Funzione che "calcola" due stringhe di separatori (intestazione e coda) lunghe uguali dato un titolo.
    :param titolo: Titolo della sezione
    :param carattere: Carattere utilizzato per essere ripetuto nel separatore
    :param lunghezza: Numero di volte che il carattere viene ripetuto prima del titolo (tot=2*lunghezza)
    :return: Due stringhe -> separatori per print
    """
    intestazione = f"{carattere * lunghezza} {titolo} {carattere * lunghezza}"
    coda = carattere * (len(intestazione) // len(carattere))

    return intestazione, coda  # Restituiamo entrambe le stringhe ottenute

def analizza_lista(lista_spese: list[float], nome: str) -> str:
    """
    Funzione che elabora e restituisce un'analisi completa di una lista di spese
    :param nome: Nome dell'elenco di spese
    :param lista_spese: Lista di spese float
    :return: Report completo, str
    """
    intestazione, coda = separatori(nome, lunghezza=10, carattere="-_-")  # Creiamo i separatori per la sezione <- Otteniamo entrambe le stringhe IN ORDINE DI USCITA
    media = calcola_media(lista_spese)  # Calcoliamo la media della lista
    dev_std = calcola_dev_std(lista_spese)  # Calcoliamo la deviazione standard
    spesa_max = max(lista_spese)  # Calcoliamo il massimo
    spesa_min = min(lista_spese)  # Calcoliamo il minimo
    n_spese = len(lista_spese)  # Otteniamo anche il numero di spese

    output = f"{intestazione}\n"  # Creiamo la stringa di output iniziando dall'intestazione
    output += f" * Media: {media:.2f} €\n"  # Aggiungiamo all'output la media
    output += f" * Deviazione standard: {dev_std:.2f} €\n"  # Aggiungiamo all'output la dev std
    output += f" * Spesa max: {spesa_max:.2f} €\n"  # Aggiungiamo all'output la spesa massima
    output += f" * Spesa min: {spesa_min:.2f} €\n"  # Aggiungiamo all'output la spesa minima
    output += f" * N° spese: {n_spese}\n"  # Aggiungiamo all'output il numero di spese
    output += coda  # Aggiungiamo all'output la coda (il separatore finale)

    return output  # Restituiamo la stringa di output

if __name__ == "__main__":  # Questo blocco che utilizziamo per usare le funzioni prende il nome di "main"
    # Codice per utilizzare le funzioni
    diz_spese = {
        "Settembre": [12, 23.2, 5, 6.7, 10],
        "Ottobre": [8.3, 12.2, 78.6, 45.6],
        "Novembre": [12.3, 8.2, 5, 98.6, 12, 4, 61, 2.3]
    }

    for mese, lista_spese in diz_spese.items():
        report = analizza_lista(lista_spese, mese)
        print(report)

