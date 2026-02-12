from django.urls import path
from .views import hello_world, today_date, random_dice, random_password, verifica_palindromo, calcola_patrimonio, \
    genera_tabellina, mini_calc

urlpatterns = [
    # Colleghiamo a livello di APP la funzione hello_world() al percorso "/hello"
    path('hello/', hello_world, name='hello-world'),
    path('date/today', today_date, name='today-date'),
    path('random/dice', random_dice, name='random-dice'),
    path('random/password', random_password, name='random-password'),
    path('verifica-palindromo', verifica_palindromo, name='verifica-palindromo'),
    path('calcolo-patrimonio', calcola_patrimonio, name='calcola-patrimonio'),
    path('calcola-tabellina/<int:base>', genera_tabellina, name='genera-tabellina'),
    path('mini-calc', mini_calc, name='mini-calc')
]

# http://127.0.0.1:8000/api/v1/hello/
# http://127.0.0.1:8000/api/v1/date/today
# http://127.0.0.1:8000/api/v1/random/dice
