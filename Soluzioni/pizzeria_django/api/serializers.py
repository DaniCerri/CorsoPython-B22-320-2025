from rest_framework import serializers
from .models import Ingrediente, Pizza, Cliente, Ordine, VocePizzaOrdine


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id', 'nome', 'prezzo_extra', 'allergene', 'vegetariano']


class PizzaSerializer(serializers.ModelSerializer):
    ingredienti = IngredienteSerializer(many=True, read_only=True)
    ingredienti_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Ingrediente.objects.all(), write_only=True, source='ingredienti', required=False
    )
    prezzo_totale = serializers.FloatField(read_only=True)

    class Meta:
        model = Pizza
        fields = ['id', 'nome', 'prezzo_base', 'descrizione', 'disponibile', 'prezzo_totale', 'ingredienti', 'ingredienti_ids']


class ClienteSerializer(serializers.ModelSerializer):
    def validate_telefono(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Il telefono non può essere vuoto.")
        return value

    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'telefono', 'indirizzo']


class VoceOrdineCreateSerializer(serializers.Serializer):
    pizza_id = serializers.IntegerField()
    quantita = serializers.IntegerField(min_value=1)
    ingredienti_extra_ids = serializers.ListField(child=serializers.IntegerField(), default=list)


class VoceOrdineSerializer(serializers.ModelSerializer):
    pizza = PizzaSerializer(read_only=True)
    ingredienti_extra = IngredienteSerializer(many=True, read_only=True)

    class Meta:
        model = VocePizzaOrdine
        fields = ['id', 'pizza', 'quantita', 'ingredienti_extra']


class OrdineSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    voci = VoceOrdineSerializer(many=True, read_only=True)

    class Meta:
        model = Ordine
        fields = ['id', 'data_ora', 'stato', 'note', 'cliente', 'voci']


class OrdineListSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)

    class Meta:
        model = Ordine
        fields = ['id', 'data_ora', 'stato', 'cliente']


class OrdineCreateSerializer(serializers.Serializer):
    cliente_id = serializers.IntegerField()
    note = serializers.CharField(required=False, allow_blank=True, allow_null=True, default=None)
    voci = serializers.ListField(child=VoceOrdineCreateSerializer(), min_length=1)


class OrdineStatoUpdateSerializer(serializers.Serializer):
    STATO_CHOICES = ['ricevuto', 'in_preparazione', 'pronto', 'consegnato']
    stato = serializers.ChoiceField(choices=STATO_CHOICES)


class StoricoClienteSerializer(serializers.Serializer):
    ordini = OrdineSerializer(many=True)
    totale_speso = serializers.FloatField()
