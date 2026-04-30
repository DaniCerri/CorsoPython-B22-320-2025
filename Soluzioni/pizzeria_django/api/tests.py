from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework import status
from .models import Ingrediente, Pizza, Cliente, Ordine, VocePizzaOrdine


class OrdineCreateTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.mozzarella = Ingrediente.objects.create(nome="Mozzarella", prezzo_extra=0.5, allergene=True, vegetariano=True)
        self.pomodoro = Ingrediente.objects.create(nome="Pomodoro", prezzo_extra=0.0, allergene=False, vegetariano=True)
        self.margherita = Pizza.objects.create(nome="Margherita", prezzo_base=6.0, disponibile=True)
        self.margherita.ingredienti.set([self.mozzarella, self.pomodoro])
        self.cliente = Cliente.objects.create(nome="Mario Rossi", telefono="3331234567", indirizzo="Via Roma 1")

    def test_crea_ordine_completo(self):
        payload = {
            "cliente_id": self.cliente.pk,
            "note": "Senza cipolla",
            "voci": [
                {
                    "pizza_id": self.margherita.pk,
                    "quantita": 2,
                    "ingredienti_extra_ids": []
                }
            ]
        }
        response = self.client.post('/api/v1/ordini/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ordine.objects.count(), 1)
        self.assertEqual(VocePizzaOrdine.objects.count(), 1)
        self.assertEqual(response.data['stato'], 'ricevuto')
        self.assertEqual(response.data['voci'][0]['quantita'], 2)

    def test_crea_ordine_cliente_inesistente(self):
        payload = {
            "cliente_id": 9999,
            "voci": [{"pizza_id": self.margherita.pk, "quantita": 1, "ingredienti_extra_ids": []}]
        }
        response = self.client.post('/api/v1/ordini/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_crea_ordine_voci_vuote(self):
        payload = {
            "cliente_id": self.cliente.pk,
            "voci": []
        }
        response = self.client.post('/api/v1/ordini/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_crea_ordine_quantita_zero(self):
        payload = {
            "cliente_id": self.cliente.pk,
            "voci": [{"pizza_id": self.margherita.pk, "quantita": 0, "ingredienti_extra_ids": []}]
        }
        response = self.client.post('/api/v1/ordini/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_aggiorna_stato_ordine(self):
        ordine = Ordine.objects.create(
            cliente=self.cliente, data_ora=timezone.now(), stato='ricevuto'
        )
        response = self.client.patch(
            f'/api/v1/ordini/{ordine.pk}/stato/',
            {"stato": "in_preparazione"},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['stato'], 'in_preparazione')
