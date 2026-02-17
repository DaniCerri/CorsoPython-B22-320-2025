from rest_framework import viewsets
from .models import Dispositivo
from .serializers import DispositivoSerializer

class DispositivoViewSet(viewsets.ModelViewSet):
    queryset = Dispositivo.objects.all()  # Accettiamo tutti i tipi di richieste
    serializer_class = DispositivoSerializer  # Le facciamo passare attraverso il filtro che abbiamo creato prima



