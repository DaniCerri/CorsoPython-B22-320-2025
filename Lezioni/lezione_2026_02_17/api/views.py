from rest_framework import viewsets
from .models import Dispositivo, Luogo, Manutenzione
from .serializers import DispositivoSerializer, LuogoSerializer, ManutenzioneSerializer

class LuogoViewSet(viewsets.ModelViewSet):
    queryset = Luogo.objects.all()
    serializer_class = LuogoSerializer

class DispositivoViewSet(viewsets.ModelViewSet):
    serializer_class = DispositivoSerializer

    def get_queryset(self):
        queryset = Dispositivo.objects.all()  # Accettiamo tutti i tipi di richieste

        # Definiamo la lettura del parametro 'luogo' dalla richiesta GET
        luogo_param = self.request.query_params.get('luogo', None)
        # Cerchiamo di ottenere il valore del parametro, altrimenti None

        # Controlliamo se è stato passato il parametro per la ricerca per luogo
        if luogo_param:
            queryset = queryset.filter(luogo__nome__icontains=luogo_param)
            # luogo__nome__icontains significa che Django implicitamente per le relazioni descritte nel file models.py
            # fa un JOIN tra le tabelle Dispositivi e Luoghi. Poi prende il nome del luogo e lo controlla con il parametro
            # luogo_param, in modalità case insensitive -> LIKE

        return queryset

class ManutenzioneViewSet(viewsets.ModelViewSet):
    queryset = Manutenzione.objects.all()
    serializer_class = ManutenzioneSerializer

