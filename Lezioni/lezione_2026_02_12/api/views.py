from rest_framework.decorators import api_view  # Gestire i metodi HTTP e la comunicazione
from rest_framework.response import Response  # Serializzare la risposta in formato HTTP
from datetime import datetime
import random

@api_view(['GET'])  # Un po' come @app.get() in fastAPI ma qua non definiamo il percorso
def hello_world(request):
    # Facciamo il dizionario con i dati da restituire al client
    data = {
        "message": "Prima prova di un'API REST in Django",
        "status": "successo"
    }

    # Restituiamo i dati attraverso Response
    return Response(data)

@api_view(['GET'])
def today_date(request):
    today = datetime.now()
    data = {
        "giorno": today.day,
        "mese": today.month,
        "anno": today.year,
        "ora": today.hour,
        "minuto": today.minute
    }

    return Response(data)

@api_view(['GET'])
def random_dice(request):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    bonus = 2 if dado1 == dado2 else 0
    totale = dado1 + dado2 + bonus

    data = {
        "dado1": dado1,
        "dado2": dado2,
        "bonus": bonus,
        "somma_dadi": dado1 + dado2,
        "messaggio": "Complimenti, hai un bonus!" if bonus else "Mi spiace, nessun bonus",
        "totale": totale
    }

    return Response(data)

# TODO: Passare in post il numeri di caratteri di cui fare la pw -> dobbiamo verificare che la lunghezza rispetti un
#  minimo di 3 caratteri

@api_view(['GET'])
def random_password(request):
    # definiamo la lunghezza finale della pw
    lunghezza = 20

    # definiamo i pool di caratteri da usare per la pw
    lettere = 'abcdefghijklmnopqrstuvwxyz'
    numeri = '0123456789'
    speciali = '!"%()@#+_-'

    # estraiamo quanti numeri per tipo di carattere
    numero_lettere = random.randint(1, lunghezza - 2)
    numero_numeri = random.randint(1, lunghezza - 1 - numero_lettere)
    numero_speciali = lunghezza - (numero_lettere + numero_numeri)

    # Estraiamo i caratteri che compongono la nostra password
    lettere_pw = random.choices(lettere + lettere.upper(), k=numero_lettere)
    numeri_pw = random.choices(numeri, k=numero_numeri)
    speciali_pw = random.choices(speciali, k=numero_speciali)

    # mettiamo insieme le liste e le mischiamo
    caratteri_totali = lettere_pw + numeri_pw + speciali_pw
    random.shuffle(caratteri_totali)

    # concateniamo i caratteri nell'ordine ottenuto in una stringa
    password = "".join(caratteri_totali)

    return Response({
        "password": password
    })

# Facciamo un endpoint che risponde a una richiesta POST
@api_view(['POST'])
def verifica_palindromo(request):
    """
    Questa funzione prende una stringa, toglie gli spazi e verifica se la stringa al contrario è uguale a quella originale
    """
    # 1. Dobbiamo ottenere i dati dalla richiesta
    input_utente = request.data.get('testo', '')

    # 2. Se non c'è input diamo "errore"
    if not input_utente:
        return Response({"errore": "Inserire un valore nel campo 'testo'"})

    # 3. Controlliamo se la stringa, pulita dagli spazi è un palindromo
    stringa = input_utente.replace(" ", "").lower()

    # Creiamo due indici (destro e sinistro) e vediamo se i caratteri a quegli indici sono diversi, se lo sono
    # la stringa non è palindroma abbiamo finito
    is_palindroma = True  # Di default partiamo pensando che la stringa sia palindroma, vediamo se saremo smentiti
    sinistra = 0  # Indice che scorre da sinistra a destra
    destra = len(stringa) - 1  # Indice che scorre da destra a sinistra

    passaggi = {}

    while sinistra < destra:
        passaggi[f"passagio_{sinistra}"] = {
            "sinistra": sinistra,
            "destra": destra,
            "carattere_sinistro": stringa[sinistra],
            "carattere_destro": stringa[destra],
            "parola_pulita": stringa,
            "lunghezza": len(stringa)
        }

        if stringa[sinistra] != stringa[destra]:
            is_palindroma = False
            break

        sinistra += 1
        destra -= 1

    return Response({
        "stringa": input_utente,
        "is_palindroma": is_palindroma,
        "pulita": stringa,
        "passaggi": passaggi
    })
