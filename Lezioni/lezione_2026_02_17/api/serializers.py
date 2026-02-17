from rest_framework import serializers
from .models import Dispositivo, Luogo, Manutenzione, Software

# TODO: fare query per avere per ogni software il numero di dispositivi su cui è installato

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

class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields = "__all__"

class DispositivoSerializer(serializers.ModelSerializer):
    # Dobbiamo spiegare a Django che le colonne costo_totale e numero_interventi sono calcolate e non nel DB
    costo_totale = serializers.SerializerMethodField()
    # NB: 'costo_totale' deve essere lo stesso nome che usiamo per l'attributo nella classe, nome della colonna e sotto
    # in get_<ATTRIBUTO>() <- get_costo_totale
    numero_interventi = serializers.SerializerMethodField()
    numero_software = serializers.SerializerMethodField()

    class Meta:
        model = Dispositivo
        fields = ['id', 'codice', 'descrizione', 'luogo', 'software_installati', 'numero_software', 'stato_operativo', 'costo_totale', 'numero_interventi']
        # depth = 1  # <- utile solamente per serializer di sola lettura

    # Questa funzione viene chiamata solamente per restituire i dati dal DB, quindi quando vogliamo scrivere i dati nel
    # db, Django si comporta come sempre, come se questa funzione non esistesse
    def to_representation(self, instance):
        # 1. Otteniamo la rappresentazione standard (cioè quella con gli ID di tutto e non i dati annidati)
        response = super().to_representation(instance)  # chiamiamo il metodo originale, presente nella classe serializers.ModelSerializer

        # 2. Sostituiamo l'id del luogo con l'oggetto completo
        if instance.luogo:  # Controlliamo se c'è, perchè potrebbe essere null
            response['luogo'] = LuogoSerializer(instance.luogo).data

        # 3. Facciamo lo stesso per i software
        # Siccome software_installati è una lista, possiamo non fare l'if
        response['software_installati'] = SoftwareSerializer(instance.software_installati.all(), many=True).data

        return response


    def get_costo_totale(self, obj):
        # 'obj' è l'istanza attuale del Dispositivo, da non confondere con il DispositivoSerializer che invece è "l'insieme di
        # regole da usare per utilizzare gli oggetti di classe Dispositivo"
        interventi = obj.manutenzioni.all()  # Otteniamo tutte le manutenzioni fatte su questo Dispositivo
        return sum(intervento.costo for intervento in interventi)

    def get_numero_interventi(self, obj):
        return obj.manutenzioni.count()

    def get_numero_software(self, obj):
        return obj.software_installati.count()