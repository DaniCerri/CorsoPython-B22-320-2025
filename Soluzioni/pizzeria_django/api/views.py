from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Ingrediente, Pizza, Cliente, Ordine, VocePizzaOrdine
from .serializers import (
    IngredienteSerializer,
    PizzaSerializer,
    ClienteSerializer,
    OrdineSerializer,
    OrdineListSerializer,
    OrdineCreateSerializer,
    OrdineStatoUpdateSerializer,
    StoricoClienteSerializer,
)


class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    serializer_class = PizzaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']

    def get_queryset(self):
        qs = Pizza.objects.prefetch_related('ingredienti').all()
        vegetariane = self.request.query_params.get('vegetariane')
        senza_allergeni = self.request.query_params.get('senza_allergeni')
        if vegetariane and vegetariane.lower() == 'true':
            ids = [
                p.id for p in qs
                if p.ingredienti.exists() and all(i.vegetariano for i in p.ingredienti.all())
            ]
            qs = qs.filter(id__in=ids)
        if senza_allergeni and senza_allergeni.lower() == 'true':
            ids = [
                p.id for p in qs
                if not p.ingredienti.filter(allergene=True).exists()
            ]
            qs = qs.filter(id__in=ids)
        return qs

    def destroy(self, request, *args, **kwargs):
        pizza = self.get_object()
        pizza.disponibile = False
        pizza.save()
        return Response(PizzaSerializer(pizza).data)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    @action(methods=['GET'], detail=True, url_path='storico')
    def storico(self, request, pk=None):
        cliente = self.get_object()
        ordini = Ordine.objects.filter(cliente=cliente).prefetch_related('voci__pizza__ingredienti', 'voci__ingredienti_extra')
        totale = 0.0
        for ordine in ordini:
            for voce in ordine.voci.all():
                prezzo_pizza = voce.pizza.prezzo_base + sum(i.prezzo_extra for i in voce.pizza.ingredienti.all())
                prezzo_extra = sum(i.prezzo_extra for i in voce.ingredienti_extra.all())
                totale += (prezzo_pizza + prezzo_extra) * voce.quantita
        data = StoricoClienteSerializer({'ordini': ordini, 'totale_speso': totale}).data
        return Response(data)


class OrdineViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = OrdineCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data
        cliente = get_object_or_404(Cliente, pk=data['cliente_id'])

        ordine = Ordine.objects.create(
            cliente=cliente,
            note=data.get('note'),
            data_ora=timezone.now(),
            stato='ricevuto',
        )

        for voce_data in data['voci']:
            pizza = get_object_or_404(Pizza, pk=voce_data['pizza_id'])
            voce = VocePizzaOrdine.objects.create(
                ordine=ordine,
                pizza=pizza,
                quantita=voce_data['quantita'],
            )
            if voce_data.get('ingredienti_extra_ids'):
                extra_ings = Ingrediente.objects.filter(pk__in=voce_data['ingredienti_extra_ids'])
                voce.ingredienti_extra.set(extra_ings)

        return Response(OrdineSerializer(ordine).data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        ordine = get_object_or_404(Ordine, pk=pk)
        return Response(OrdineSerializer(ordine).data)

    @action(methods=['PATCH'], detail=True, url_path='stato')
    def aggiorna_stato(self, request, pk=None):
        ordine = get_object_or_404(Ordine, pk=pk)
        serializer = OrdineStatoUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        ordine.stato = serializer.validated_data['stato']
        ordine.save()
        return Response(OrdineSerializer(ordine).data)

    @action(methods=['GET'], detail=False, url_path='oggi')
    def oggi(self, request):
        oggi = timezone.localdate()
        ordini = (
            Ordine.objects.filter(data_ora__date=oggi)
            .order_by('data_ora')
            .prefetch_related('voci__pizza', 'voci__ingredienti_extra')
            .select_related('cliente')
        )
        return Response(OrdineListSerializer(ordini, many=True).data)
