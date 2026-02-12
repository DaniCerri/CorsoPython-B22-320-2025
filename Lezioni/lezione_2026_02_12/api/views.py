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

# TODO: fare una funzione che prenda un deposito iniziale [€], un contributo mensile [€] e un tasso mensile [%]
#   restituisce l'elenco mese per mese [(02, 2026), (03, 2026), ...] del valore del conto che tenga conto di incremento percentuale
#   e dell'incremento dato dal versamento mensile del regime per 30 anni

# es: conto_iniziale = 100, contributo_mensile: 10, tasso: 10%
# mese 1 (03, 2026): abbiamo (100 + 10) * 1.1 = 121
# mese 2 (04, 2026): abbiamo (121 + 10) * 1.1 = 144,1
# ...

@api_view(['POST'])
def calcola_patrimonio(request):
    date = datetime.now()
    mese, anno = date.month + 1, date.year

    anni = 30
    mesi_durata = anni * 12

    capitale_iniziale = request.data.get("capitale_inziale", 0)
    contributo_mensile = request.data.get("contributo_mensile", 0)
    tasso = request.data.get("tasso", 0) / 100 # -> Così otteniamo direttamente il coefficiente che ci piace

    data = {
        "mesi": [],
        "patrimonio_inziale": capitale_iniziale,
        "tasso": tasso,
        "contributo_mensile": contributo_mensile,
        "totale_versato": contributo_mensile * mesi_durata,
        # Opzionalmente potete poi mettere anche lo scarto tra versato e guadagnato
        "totale": 0
    }

    for mese_corrente in range(mese, mesi_durata + mese):
        # mese_corrente += mese
        mese_convertito = mese_corrente % 12
        anno_convertito = mese_corrente // 12 + anno

        patrimonio_iniziale = data['totale']
        patrimonio = patrimonio_iniziale + contributo_mensile
        patrimonio_a_fine_mese = patrimonio * (1 + tasso)

        row = {
            "id": f"({mese_convertito}, {anno_convertito})",
            "patrimonio": patrimonio_a_fine_mese
        }

        data['totale'] = patrimonio_a_fine_mese
        data['mesi'].append(row)

    return Response(data)

# il numero di cui calcolare la tabellina verrà poi passato attraverso la path dell'endpoint
# -> in fastapi scrivevamo @app.get("/percorso/{numero}")
# NB: La tipologia della variabile in fastAPI la avremmo scritta nella dichiarazione della funzione
# -> def funzione(..., numero: int)
@api_view(['GET'])
def genera_tabellina(request, base):
    tabellina = [base * i for i in range(1, 11)]

    return Response({
        "numero": base,
        "tabellina": tabellina,
        "formula": f"{base} * n, con n = 1, ..., 10"
    })

@api_view(['GET'])
def mini_calc(request):
    # es di richiesta: path/mini-calc?a=N&b=M
    # Senza la "&" avremmo solo un parametro a con il valore "Nb=M"
    # convertendo la query in path avremmo avuto -> path/mini-calc/<float:a>/<float:b>
    OPERAZIONI = {"sum", "sub", "mol", "div"}

    try:
        num_a = float(request.data.get('a', 0))
        num_b = float(request.data.get('b', 0))
        operazione = request.data.get('operazione', "")

        if operazione not in OPERAZIONI:
            return Response({"errore": f"l'operazione deve essere una tra {OPERAZIONI}"}, status=400)

        if operazione == "div" and num_b == 0:
            return Response({"errore": "Non si può dividere per 0"}, status=400)

        if operazione == "sum":
            risultato = num_a + num_b
        elif operazione == "sub":
            risultato = num_a - num_b
        elif operazione == "molt":
            risultato = num_a * num_b
        else:
            risultato = num_a / num_b

        return Response(
            {
                "operazione": f"Operazione da fare: {operazione}",
                "a": num_a,
                "b": num_b,
                "totale": risultato
            }
        )

    except ValueError:
        return Response({
            "errore": "Uno tra a e b (o entrambi) non è un numero",
            "a_ottenuto": request.data.get('a', None),
            "b_ottenuto": request.data.get('b', None)
        })










