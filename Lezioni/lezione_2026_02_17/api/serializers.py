from rest_framework import serializers
from .models import Dispositivo, Luogo, Manutenzione

class LuogoSerializer(serializers.ModelSerializer):
    numero_dispositivi = serializers.SerializerMethodField()

    class Meta:
        model = Luogo
        fields = ['id', 'nome', 'piano', 'note', 'numero_dispositivi']  # Prende tutti i campi disponibili

    def get_numero_dispositivi(self, obj):
        return obj.dispositivi.count()


class ManutenzioneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manutenzione
        fields = "__all__"

class DispositivoSerializer(serializers.ModelSerializer):
    # Dobbiamo spiegare a Django che le colonne costo_totale e numero_interventi sono calcolate e non nel DB
    costo_totale = serializers.SerializerMethodField()
    # NB: 'costo_totale' deve essere lo stesso nome che usiamo per l'attributo nella classe, nome della colonna e sotto
    # in get_<ATTRIBUTO>() <- get_costo_totale
    numero_interventi = serializers.SerializerMethodField()

    class Meta:
        model = Dispositivo
        fields = ['id', 'codice', 'luogo', 'stato_operativo', 'costo_totale', 'numero_interventi']
        # fields = [
        #     'id',  # Un ID che si aspetta di default Django per identificare la riga
        #     'codice',
        #     'descrizione',
        #     'stato_operativo',
        #     'data_registrazione'
        # ]

    def get_costo_totale(self, obj):
        # 'obj' è l'istanza attuale del Dispositivo, da non confondere con il DispositivoSerializer che invece è "l'insieme di
        # regole da usare per utilizzare gli oggetti di classe Dispositivo"
        interventi = obj.manutenzioni.all()  # Otteniamo tutte le manutenzioni fatte su questo Dispositivo
        return sum(intervento.costo for intervento in interventi)

    def get_numero_interventi(self, obj):
        return obj.manutenzioni.count()