from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        "nome_corso": "B22-320-2025",
        "linguaggio": "Python",
        "studenti": 12,
        "docente": "Daniele Cerrina",
        "argomenti": [
            "Basi di Python",
            "Funzioni",
            "OOP",
            "FastAPI",
            "Django"
        ]
    }
    # Django va a cercare i template dentro la cartella "template" automaticamente
    return render(request, 'core/index.html', context)

def iscriviti(request):
    if request.method == 'POST':  # Gestiamo il caso in cui ci sia una richiesta POST
        # 1. Recuperiamo i dati della richiesta POST
        nome_iscritto = request.POST.get('nome_form')
        email_iscritto = request.POST.get('email_form')

        # 2. Prepariamo i dati per la pagina di conferma
        dati_ricevuti = {
            'nome_iscritto': nome_iscritto,
            'email_iscritto': email_iscritto,
        }

        # 3. Presentiamo la pagina conferma
        return render(request, 'core/conferma.html', dati_ricevuti)

    return render(request, 'core/iscriviti.html')

