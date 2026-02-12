from django.urls import path
from .views import hello_world, today_date, random_dice

urlpatterns = [
    # Colleghiamo a livello di APP la funzione hello_world() al percorso "/hello"
    path('hello/', hello_world, name='hello-world'),
    path('date/today', today_date, name='today-date'),
    path('random/dice', random_dice, name='random-dice')
]

# http://127.0.0.1:8000/api/v1/hello/
# http://127.0.0.1:8000/api/v1/date/today
# http://127.0.0.1:8000/api/v1/random/dice
