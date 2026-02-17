from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DispositivoViewSet, LuogoViewSet, ManutenzioneViewSet

# 1. Definiamo il router che raggruppa gli endpoint
router = DefaultRouter()

# 2. definiamo il gruppo di endpoint legati al 'Dispositivo'
router.register(r'dispositivi', DispositivoViewSet, basename='dispositivo')
router.register(r'luoghi', LuogoViewSet)
router.register(r'manutenzioni', ManutenzioneViewSet)
# La r davanti alla stringa dice a python di prendere quella stringa "raw" cioè senza sequenze di escape come ad esempio \n \s \t

urlpatterns = [
    path('', include(router.urls))
]

