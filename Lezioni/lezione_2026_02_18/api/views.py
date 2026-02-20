from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Professore, Studente, Corso
from .serializers import ProfessoreSerializer, StudenteSerializer, CorsoSerializer

class ProfessoreViewSet(viewsets.ModelViewSet):
    queryset = Professore.objects.all()
    serializer_class = ProfessoreSerializer

class StudenteViewSet(viewsets.ModelViewSet):
    queryset = Studente.objects.all()
    serializer_class = StudenteSerializer

class CorsoViewSet(viewsets.ModelViewSet):
    queryset = Corso.objects.all()
    serializer_class = CorsoSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['nome', 'codice', 'professore__cognome']
    ordering_fields = ['crediti', 'nome']

    # URL: POST /api/v1/corsi/{ID_corso}/iscrivi
    @action(methods=['POST'], detail=True)
    def iscrivi(self, request, pk=None):
        corso = self.get_object()  # Prendiamo il corso dall'URL
        # Prendiamo l'id studente dal POST
        id_studente = request.data.get('id_studente')
        # Controlliamo che l'id_studente fosse nel POST
        if not id_studente:
            return Response(
                {
                    "error": "ID non presente nella richiesta"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Cerchiamo di ottenere lo studente
        studente = get_object_or_404(Studente, pk=id_studente)

        # Aggiungiamo lo studente al corso
        corso.studenti.add(studente)

        return Response(
            {
                'status': 'Studente aggiunto con successo',
                'corso': str(corso),
                'studente': studente.matricola
            },
            status=status.HTTP_200_OK
        )







