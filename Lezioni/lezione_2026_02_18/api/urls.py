from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudenteViewSet, ProfessoreViewSet, CorsoViewSet

# 1. Dichiariamo il router
router = DefaultRouter()
router.register(r'professori', ProfessoreViewSet)
router.register(r'studenti', StudenteViewSet)
router.register(r'corsi', CorsoViewSet)

# Variabile OBBLIGATORIA per dichiarare gli url
urlpatterns = [
    path('', include(router.urls))
]
