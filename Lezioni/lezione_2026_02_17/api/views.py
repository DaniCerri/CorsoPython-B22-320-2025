from rest_framework import viewsets
from .models import Dispositivo, Luogo, Manutenzione
from .serializers import DispositivoSerializer, LuogoSerializer, ManutenzioneSerializer

class LuogoViewSet(viewsets.ModelViewSet):
    queryset = Luogo.objects.all()
    serializer_class = LuogoSerializer

class DispositivoViewSet(viewsets.ModelViewSet):
    queryset = Dispositivo.objects.all()  # Accettiamo tutti i tipi di richieste
    serializer_class = DispositivoSerializer  # Le facciamo passare attraverso il filtro che abbiamo creato prima

class ManutenzioneViewSet(viewsets.ModelViewSet):
    queryset = Manutenzione.objects.all()
    serializer_class = ManutenzioneSerializer

