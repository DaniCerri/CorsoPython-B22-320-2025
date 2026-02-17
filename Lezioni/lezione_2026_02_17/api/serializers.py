from rest_framework import serializers
from .models import Dispositivo

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = [
            'id',  # Un ID che si aspetta di default Django per identificare la riga
            'codice',
            'descrizione',
            'stato_operativo',
            'data_registrazione'
        ]