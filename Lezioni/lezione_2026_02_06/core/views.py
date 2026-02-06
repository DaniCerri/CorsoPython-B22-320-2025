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

