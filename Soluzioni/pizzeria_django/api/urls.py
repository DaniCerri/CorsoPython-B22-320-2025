from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IngredienteViewSet, PizzaViewSet, ClienteViewSet, OrdineViewSet

router = DefaultRouter()
router.register(r'ingredienti', IngredienteViewSet, basename='ingrediente')
router.register(r'pizze', PizzaViewSet, basename='pizza')
router.register(r'clienti', ClienteViewSet, basename='cliente')
router.register(r'ordini', OrdineViewSet, basename='ordine')

urlpatterns = [
    path('', include(router.urls)),
]
