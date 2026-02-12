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

# TODO: Facciamo un endpoint GET /random/dice che lancia due dadi da 6 facce e restituisce la somma,
#   Se i due lanci sono uguali, alla somma aggiunge un bonus di 2 punti, chiaramente se il bonus è aggiunto o no
#   va segnalato nella risposta. La risposta avrà l'esito di ogni dado, la somma dei dadi, eventuale bonus e totale finale
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


