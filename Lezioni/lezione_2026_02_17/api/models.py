from django.db import models

class Dispositivo(models.Model):
    codice = models.CharField(max_length=50, unique=True)  # Identificativo
    descrizione = models.TextField(blank=True, null=True)  # Paragrafo di testo, può essere testo vuoto o non essere settato
    stato_operativo = models.BooleanField(default=True)  # Booleano, di default settato a True
    data_registrazione = models.DateTimeField(auto_now_add=True)  # Datetime in cui viene registrato il dispositivo nel DB,
    # Anche questo si "setta" da solo

    def __str__(self):
        return self.codice

