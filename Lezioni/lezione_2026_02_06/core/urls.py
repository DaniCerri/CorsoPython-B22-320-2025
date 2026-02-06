from django.urls import path
from . import views

urlpatterns = [
    # Dichiariamo a Django che questa app (servizio) ha un percorso di ROOT
    # e deve rispondere con la funzione home() del file views.py
    path("", views.home, name="home")
]